// src/App.js
import React, { useState } from 'react';
import Dropdown from './components/Dropdown';
import TransactionsTable from './components/TransactionsTable';
import Statistics from './components/Statistics';
import BarChart from './components/BarChart';

const App = () => {
  const [selectedMonth, setSelectedMonth] = useState(2); // March (0-indexed)
  const [searchQuery, setSearchQuery] = useState('');

  return (
    <div>
      <Dropdown selectedMonth={selectedMonth} onMonthChange={setSelectedMonth} />
      <Statistics month={selectedMonth} />
      <TransactionsTable month={selectedMonth} searchQuery={searchQuery} />
      <BarChart month={selectedMonth} />
    </div>
  );
};

export default App;
