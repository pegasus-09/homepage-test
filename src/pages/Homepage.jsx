import React from 'react';

const Homepage = () => {
  return (
    <div style={{
      backgroundColor: '#F7F6F3',
      color: '#2E2E2E',
      minHeight: '100vh',
      fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", sans-serif'
    }}>
      <nav style={{
        position: 'sticky',
        top: 0,
        zIndex: 999,
        backgroundColor: '#5B6C8F',
        padding: '0.6rem 2rem',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        borderRadius: '0 0 12px 12px'
      }}>
        <div style={{ fontSize: '1.2rem', fontWeight: 700, color: 'white' }}>
          🎓 AI Career Guidance
        </div>
        <div style={{ display: 'flex', gap: '1.2rem' }}>
          <button style={{ background: 'transparent', color: 'white', border: 'none', cursor: 'pointer' }}>Home</button>
          <button style={{ background: 'transparent', color: 'white', border: 'none', cursor: 'pointer' }}>Assessment</button>
          <button style={{ background: 'transparent', color: 'white', border: 'none', cursor: 'pointer' }}>About</button>
          <button style={{ background: 'transparent', color: 'white', border: 'none', cursor: 'pointer' }}>Login</button>
        </div>
      </nav>

      <main style={{ maxWidth: '1200px', margin: '0 auto', padding: '2rem' }}>
        <h1 style={{ color: '#5B6C8F', fontSize: '2.5rem', marginBottom: '1rem' }}>
          Helping students choose their future, intelligently
        </h1>

        <p style={{ fontSize: '1.1rem', marginBottom: '2rem' }}>
          This platform uses <strong>psychometric assessments</strong>, <strong>academic interests</strong>,
          and <strong>AI-driven analysis</strong> to help high school students make
          informed university and career decisions.
        </p>

        <hr style={{ margin: '2rem 0', border: 'none', borderTop: '1px solid #ccc' }} />

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '1.5rem', marginTop: '2rem' }}>
          <div style={{
            backgroundColor: '#E8DFD8',
            padding: '1.5rem',
            borderRadius: '12px'
          }}>
            <h3 style={{ color: '#5B6C8F', marginBottom: '1rem' }}>🧠 Psychometric Testing</h3>
            <p>Structured assessments to understand how students think and learn.</p>
          </div>

          <div style={{
            backgroundColor: '#E8DFD8',
            padding: '1.5rem',
            borderRadius: '12px'
          }}>
            <h3 style={{ color: '#5B6C8F', marginBottom: '1rem' }}>🎯 Career Matching</h3>
            <p>AI-based mapping to university courses and career clusters.</p>
          </div>

          <div style={{
            backgroundColor: '#E8DFD8',
            padding: '1.5rem',
            borderRadius: '12px'
          }}>
            <h3 style={{ color: '#5B6C8F', marginBottom: '1rem' }}>📊 Personalised Insights</h3>
            <p>Clear explanations and reports designed for students and parents.</p>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Homepage;
