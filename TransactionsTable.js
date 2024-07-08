// src/components/TransactionsTable.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TransactionsTable = ({ month, searchQuery }) => {
  const [transactions, setTransactions] = useState([]);
  const [page, setPage] = useState(1);

  useEffect(() => {
    fetchTransactions();
  }, [month, searchQuery, page]);

  const fetchTransactions = async () => {
    const response = await axios.get(`/api/transactions?month=${month}&search=${searchQuery}&page=${page}`);
    setTransactions(response.data);
  };

  return (
    <div>
      <input 
        type="text" 
        placeholder="Search transactions" 
        value={searchQuery} 
        onChange={e => setSearchQuery(e.target.value)} 
      />
      <table>
        <thead>
          <tr>
            <th>Title</th>
            <th>Description</th>
            <th>Price</th>
          </tr>
        </thead>
        <tbody>
          {transactions.map(tx => (
            <tr key={tx.id}>
              <td>{tx.title}</td>
              <td>{tx.description}</td>
              <td>{tx.price}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <button onClick={() => setPage(page - 1)} disabled={page === 1}>Previous</button>
      <button onClick={() => setPage(page + 1)}>Next</button>
    </div>
  );
};

export default TransactionsTable;
