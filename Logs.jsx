import { useEffect, useState } from 'react';

const API_BASE = import.meta.env.VITE_API_BASE;

export default function Logs() {
  const [logs, setLogs] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(\`\${API_BASE}/logs\`)
      .then((res) => res.json())
      .then(setLogs)
      .finally(() => setLoading(false));
  }, []);

  return (
    <div className="p-6 font-sans">
      <h1 className="text-xl font-bold mb-4">Valuation Logs</h1>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <table className="table-auto w-full border">
          <thead>
            <tr className="bg-gray-200">
              <th className="border px-4 py-2">Timestamp</th>
              <th className="border px-4 py-2">Valuation</th>
              <th className="border px-4 py-2">Confidence</th>
            </tr>
          </thead>
          <tbody>
            {logs.map((entry, idx) => {
              const fields = entry.fields || {};
              return (
                <tr key={idx}>
                  <td className="border px-4 py-2">{fields.Timestamp || '—'}</td>
                  <td className="border px-4 py-2">{fields.Valuation || '—'}</td>
                  <td className="border px-4 py-2">{fields.Confidence || '—'}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      )}
    </div>
  );
}
