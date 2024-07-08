// src/components/Dropdown.js
import React from 'react';

const months = [
  'January', 'February', 'March', 'April', 'May', 'June',
  'July', 'August', 'September', 'October', 'November', 'December'
];

const Dropdown = ({ selectedMonth, onMonthChange }) => (
  <select value={selectedMonth} onChange={e => onMonthChange(e.target.value)}>
    {months.map((month, index) => (
      <option key={index} value={index}>{month}</option>
    ))}
  </select>
);

export default Dropdown;
