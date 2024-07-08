// src/components/BarChart.js
import React, { useState, useEffect } from 'react';
import { Bar } from 'react-chartjs-2';
import axios from 'axios';

const BarChart = ({ month }) => {
  const [data, setData] = useState({ labels: [], datasets: [] });

  useEffect(() => {
    fetchChartData();
  }, [month]);

  const fetchChartData = async () => {
    const response = await axios.get(`/api/chart-data?month=${month}`);
    const chartData = response.data;
    setData({
      labels: chartData.labels,
      datasets: [{
        label: 'Price Range',
        data: chartData.data,
        backgroundColor: 'rgba(75,192,192,0.4)',
        borderColor: 'rgba(75,192,192,1)',
        borderWidth: 1,
      }]
    });
  };

  return <Bar data={data} />;
};

export default BarChart;
