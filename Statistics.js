// src/components/Statistics.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Statistics = ({ month }) => {
  const [stats, setStats] = useState({ totalSales: 0, soldItems: 0, notSoldItems: 0 });

  useEffect(() => {
    fetchStatistics();
  }, [month]);

  const fetchStatistics = async () => {
    const response = await axios.get(`/api/statistics?month=${month}`);
    setStats(response.data);
  };

  return (
    <div>
      <div>Total Sales: {stats.totalSales}</div>
      <div>Sold Items: {stats.soldItems}</div>
      <div>Not Sold Items: {stats.notSoldItems}</div>
    </div>
  );
};

export default Statistics;
