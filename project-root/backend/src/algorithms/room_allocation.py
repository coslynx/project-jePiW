import pandas as pd

def group_members_by_id(group_info):
    grouped = group_info.groupby('Group ID')
    return {group_id: group_info for group_id, group_info in grouped}

def allocate_rooms(group_info, hostel_info):
    group_members = group_members_by_id(group_info)
    allocations = []

    for group_id, members in group_members.items():
        hostel_subset = hostel_info[hostel_info['Gender'] == members['Gender'].iloc[0]]
        hostel_subset = hostel_subset[hostel_subset['Capacity'] >= members['Members'].iloc[0]]
        
        if not hostel_subset.empty:
            allocation = hostel_subset.iloc[0]
            allocations.append({
                'Group ID': group_id,
                'Hostel Name': allocation['Hostel Name'],
                'Room Number': allocation['Room Number'],
                'Members Allocated': allocation['Capacity']
            })
        else:
            allocations.append({
                'Group ID': group_id,
                'Hostel Name': 'Not available',
                'Room Number': 'Not available',
                'Members Allocated': 'Not available'
            })
    
    return pd.DataFrame(allocations)