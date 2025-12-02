import { Link, useNavigate } from 'react-router-dom';
import { useState, useEffect } from 'react';
import './Navbar.css';

function Navbar() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    checkAuth();
    // Listen for auth changes
    window.addEventListener('authChange', checkAuth);
    return () => window.removeEventListener('authChange', checkAuth);
  }, []);

  const checkAuth = async () => {
    try {
      const response = await fetch('http://localhost:5001/api/auth/check', {
        credentials: 'include',
      });

      const data = await response.json();
      setIsAuthenticated(data.authenticated);
    } catch (err) {
      console.error('Auth check error:', err);
      setIsAuthenticated(false);
    }
  };

  const handleLogout = async () => {
    try {
      await fetch('http://localhost:5001/api/logout', {
        method: 'POST',
        credentials: 'include',
      });

      setIsAuthenticated(false);
      navigate('/');
      // Trigger auth change event
      window.dispatchEvent(new Event('authChange'));
    } catch (err) {
      console.error('Logout error:', err);
    }
  };

  return (
    <nav className='navbar'>
      <div className='navbar-container'>
        <Link to='/' className='navbar-logo'>
          PDM
        </Link>
        <div className='navbar-links'>
          <Link to='/' className='nav-link'>
            Home
          </Link>
          {!isAuthenticated ? (
            <>
              <Link to='/login' className='nav-link'>
                Login
              </Link>
              <Link to='/signup' className='nav-link'>
                Signup
              </Link>
            </>
          ) : (
            <button onClick={handleLogout} className='nav-link logout-btn'>
              Signout
            </button>
          )}
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
