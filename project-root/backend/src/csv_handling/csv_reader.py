import pandas as pd

def read_csv_file(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

def group_by_id(data):
    grouped_data = data.groupby('Group ID')
    return grouped_data

def filter_by_gender(data, gender):
    filtered_data = data[data['Gender'] == gender]
    return filtered_data

def filter_by_capacity(data, capacity):
    filtered_data = data[data['Capacity'] >= capacity]
    return filtered_data

def merge_data(group_data, hostel_data):
    merged_data = pd.merge(group_data, hostel_data, how='inner', on='Gender')
    return merged_data

def allocate_rooms(group_data, hostel_data):
    allocation_data = pd.DataFrame(columns=['Group ID', 'Hostel Name', 'Room Number', 'Members Allocated'])
    
    for index, row in group_data.iterrows():
        group_id = row['Group ID']
        members = row['Members']
        
        available_hostels = filter_by_gender(hostel_data, row['Gender'])
        available_hostels = filter_by_capacity(available_hostels, members)
        
        if not available_hostels.empty:
            selected_hostel = available_hostels.iloc[0]
            allocation_data = allocation_data.append({'Group ID': group_id, 'Hostel Name': selected_hostel['Hostel Name'], 'Room Number': selected_hostel['Room Number'], 'Members Allocated': members}, ignore_index=True)
    
    return allocation_data

# Main function to handle CSV file reading and room allocation
def main(group_file_path, hostel_file_path):
    group_data = read_csv_file(group_file_path)
    hostel_data = read_csv_file(hostel_file_path)
    
    if group_data is not None and hostel_data is not None:
        group_data_grouped = group_by_id(group_data)
        allocated_rooms = allocate_rooms(group_data_grouped, hostel_data)
        
        return allocated_rooms
    else:
        return None

# Example usage
if __name__ == "__main__":
    allocation_result = main('path/to/group_info.csv', 'path/to/hostel_info.csv')
    if allocation_result is not None:
        print(allocation_result)
    else:
        print("Error in allocation process")