import React, { useState, useEffect } from 'react';
import { Button } from 'react-bootstrap';
import axios from 'axios';

const DownloadCsv = () => {
  const [csvData, setCsvData] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/download-csv')
      .then(response => {
        setCsvData(response.data);
      })
      .catch(error => {
        console.error('Error fetching CSV data: ', error);
      });
  }, []);

  const downloadCsvFile = () => {
    const csvContent = "Group ID, Hostel Name, Room Number, Members Allocated\n";
    csvData.forEach(row => {
      csvContent += `${row.groupId}, ${row.hostelName}, ${row.roomNumber}, ${row.membersAllocated}\n`;
    });

    const blob = new Blob([csvContent], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'room_allocation.csv';
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div>
      <h2>Download Allocated Rooms CSV</h2>
      <Button variant="primary" onClick={downloadCsvFile}>
        Download CSV
      </Button>
    </div>
  );
};

export default DownloadCsv;