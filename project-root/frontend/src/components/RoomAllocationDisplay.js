import React, { useState, useEffect } from 'react';
import axios from 'axios';

const RoomAllocationDisplay = () => {
  const [allocatedRooms, setAllocatedRooms] = useState([]);

  useEffect(() => {
    // Fetch allocated rooms data from backend API
    const fetchAllocatedRooms = async () => {
      try {
        const response = await axios.get('http://backend-api-url/allocated-rooms');
        setAllocatedRooms(response.data);
      } catch (error) {
        console.error('Error fetching allocated rooms:', error);
      }
    };

    fetchAllocatedRooms();
  }, []);

  return (
    <div className="room-allocation-display">
      <h2>Allocated Rooms</h2>
      <table>
        <thead>
          <tr>
            <th>Group ID</th>
            <th>Hostel Name</th>
            <th>Room Number</th>
            <th>Members Allocated</th>
          </tr>
        </thead>
        <tbody>
          {allocatedRooms.map(room => (
            <tr key={room.groupId}>
              <td>{room.groupId}</td>
              <td>{room.hostelName}</td>
              <td>{room.roomNumber}</td>
              <td>{room.membersAllocated}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default RoomAllocationDisplay;