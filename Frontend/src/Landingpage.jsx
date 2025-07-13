import React from 'react';
import {
  BarChart3, Shield, Users, MapPin, TrendingUp, Droplet,
  CheckCircle, ArrowRight, Waves
} from 'lucide-react';

const LandingPage = () => {
  // CSS styles as JavaScript objects
  const styles = {
    hero: {
      minHeight: '60vh',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      background: 'linear-gradient(135deg, #e3f2fd 0%, #90caf9 100%)',
      padding: '4rem 1rem 2rem 1rem',
      borderRadius: '0 0 3rem 3rem',
      boxShadow: '0 8px 32px 0 rgba(33,150,243,0.10)'
    },
    heroTitle: {
      fontSize: '3rem',
      fontWeight: '800',
      color: '#1976d2',
      marginBottom: '1rem',
      letterSpacing: '1px',
      textAlign: 'center'
    },
    heroSubtitle: {
      fontSize: '1.5rem',
      color: '#1565c0',
      marginBottom: '2rem',
      textAlign: 'center'
    },
    statsSection: {
      background: 'rgba(255,255,255,0.85)',
      padding: '2rem 0',
      borderRadius: '2rem',
      margin: '2rem 0',
      boxShadow: '0 4px 24px 0 rgba(33,150,243,0.10)'
    },
    statBox: {
      textAlign: 'center',
      marginBottom: '1rem'
    },
    statNumber: {
      fontSize: '2.5rem',
      fontWeight: '700',
      color: '#1976d2'
    },
    statLabel: {
      color: '#1976d2',
      fontSize: '1.1rem'
    },
    featuresSection: {
      padding: '3rem 0',
      background: 'linear-gradient(120deg, #e3f2fd 60%, #bbdefb 100%)',
      borderRadius: '2rem',
      marginBottom: '2rem'
    },
    featureCard: {
      background: '#fff',
      borderRadius: '1.5rem',
      boxShadow: '0 4px 24px 0 rgba(33,150,243,0.10)',
      padding: '2rem',
      margin: '1rem',
      transition: 'box-shadow 0.3s, transform 0.3s',
      border: '1px solid #e3f2fd',
      cursor: 'pointer'
    },
    featureIcon: {
      background: '#e3f2fd',
      borderRadius: '1rem',
      padding: '0.75rem',
      marginBottom: '1rem',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center'
    },
    featureTitle: {
      fontSize: '1.25rem',
      fontWeight: '700',
      color: '#1976d2',
      marginBottom: '0.5rem'
    },
    featureDesc: {
      color: '#1976d2',
      fontSize: '1rem'
    },
    benefitsSection: {
      background: 'linear-gradient(90deg, #1976d2 60%, #64b5f6 100%)',
      color: '#fff',
      padding: '3rem 0',
      borderRadius: '2rem',
      marginBottom: '2rem'
    },
    benefitCard: {
      background: 'rgba(255,255,255,0.10)',
      borderRadius: '1.5rem',
      padding: '2rem',
      margin: '1rem',
      border: '1px solid rgba(255,255,255,0.18)',
      color: '#fff'
    },
    ctaSection: {
      padding: '3rem 0',
      textAlign: 'center'
    },
    ctaTitle: {
      fontSize: '2.5rem',
      fontWeight: '800',
      color: '#1976d2',
      marginBottom: '1rem'
    },
    ctaDesc: {
      fontSize: '1.25rem',
      color: '#1565c0',
      marginBottom: '2rem'
    },
    ctaButtons: {
      display: 'flex',
      justifyContent: 'center',
      gap: '2rem'
    },
    ctaBtn: {
      background: 'linear-gradient(90deg, #1976d2 60%, #64b5f6 100%)',
      color: '#fff',
      fontWeight: '700',
      fontSize: '1.2rem',
      padding: '1rem 2.5rem',
      border: 'none',
      borderRadius: '2rem',
      boxShadow: '0 4px 16px 0 rgba(33,150,243,0.10)',
      cursor: 'pointer',
      transition: 'background 0.3s, transform 0.2s, box-shadow 0.2s',
      outline: 'none',
      textDecoration: 'none',
      display: 'inline-block'
    }
  };

  const features = [
    {
      icon: <BarChart3 className="w-8 h-8 text-blue-600" />,
      title: "Real-time Monitoring",
      description: "Track water quality parameters in real-time with advanced sensors and instant alerts for any anomalies."
    },
    {
      icon: <Shield className="w-8 h-8 text-blue-600" />,
      title: "Safety Compliance",
      description: "Ensure water meets safety standards with automated compliance checking and regulatory reporting."
    },
    {
      icon: <MapPin className="w-8 h-8 text-blue-600" />,
      title: "Location Tracking",
      description: "Monitor multiple water sources across different locations with GPS-enabled tracking and mapping."
    },
    {
      icon: <TrendingUp className="w-8 h-8 text-blue-600" />,
      title: "Predictive Analytics",
      description: "Identify trends and predict potential issues before they occur using machine learning algorithms."
    },
    {
      icon: <Users className="w-8 h-8 text-blue-600" />,
      title: "Team Collaboration",
      description: "Share data and insights with your team, assign tasks, and manage water quality projects collaboratively."
    },
    {
      icon: <Droplet className="w-8 h-8 text-blue-600" />,
      title: "Comprehensive Testing",
      description: "Monitor pH, turbidity, dissolved oxygen, temperature, and other critical water quality indicators."
    }
  ];

  const stats = [
    { number: "10,000+", label: "Water Sources Monitored" },
    { number: "99.9%", label: "Uptime Reliability" },
    { number: "500+", label: "Organizations Trust Us" },
    { number: "24/7", label: "Continuous Monitoring" }
  ];

  // GitHub SVG icon
  const githubIcon = (
    <svg height="24" width="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{verticalAlign: 'middle'}}>
      <path d="M12 2C6.48 2 2 6.58 2 12.26c0 4.48 2.87 8.28 6.84 9.63.5.09.68-.22.68-.48 0-.24-.01-.87-.01-1.7-2.78.62-3.37-1.36-3.37-1.36-.45-1.18-1.11-1.5-1.11-1.5-.91-.64.07-.63.07-.63 1.01.07 1.54 1.06 1.54 1.06.89 1.56 2.34 1.11 2.91.85.09-.66.35-1.11.63-1.37-2.22-.26-4.56-1.14-4.56-5.07 0-1.12.39-2.03 1.03-2.75-.1-.26-.45-1.3.1-2.7 0 0 .84-.28 2.75 1.05A9.38 9.38 0 0 1 12 6.84c.85.004 1.71.12 2.51.34 1.91-1.33 2.75-1.05 2.75-1.05.55 1.4.2 2.44.1 2.7.64.72 1.03 1.63 1.03 2.75 0 3.94-2.34 4.81-4.57 5.07.36.32.68.94.68 1.9 0 1.37-.01 2.47-.01 2.81 0 .27.18.58.69.48A10.01 10.01 0 0 0 22 12.26C22 6.58 17.52 2 12 2z" fill="#fff"/>
    </svg>
  );

  // Project description section (below hero)
  const descriptionSection = (
    <section style={{
      background: 'rgba(33,150,243,0.08)',
      borderRadius: '1.5rem',
      boxShadow: '0 4px 24px 0 rgba(33,150,243,0.10)',
      padding: '2.5rem 2rem',
      margin: '2rem auto',
      maxWidth: 700,
      color: '#1976d2',
      fontSize: '1.08rem',
      fontWeight: 500,
      lineHeight: 1.7,
      textAlign: 'left',
    }}>
      <h2 style={{fontWeight: 800, fontSize: '2rem', marginBottom: '1rem', color: '#1565c0', textAlign: 'center'}}>About This Project</h2>
      <ul style={{paddingLeft: 0, listStyle: 'none'}}>
        <li><b>Model:</b> Trained on 3,250 water quality samples</li>
        <li><b>Accuracy:</b> 85% (baseline: 67-75%)</li>
        <li><b>Version:</b> Beta 0.1</li>
        <li><b>Features:</b>
          <ul style={{margin: '0.5rem 0 0 1.2rem', fontWeight: 400, color: '#1976d2'}}>
            <li>• Potability prediction</li>
            <li>• Secure authentication (Google/email)</li>
            <li>• Interactive dashboard</li>
            <li>• User-specific prediction history</li>
          </ul>
        </li>
        <li style={{marginTop: '0.7rem'}}><b>Upcoming:</b>
          <ul style={{margin: '0.5rem 0 0 1.2rem', fontWeight: 400, color: '#1976d2'}}>
            <li>• Real-time data from India WRIS</li>
            <li>• Map integration for location-based monitoring</li>
          </ul>
        </li>
      </ul>
      <div style={{marginTop: '1.2rem', fontSize: '0.98rem', color: '#1976d2', opacity: 0.8}}>
        <b>Note:</b> This is a research project. Results are for guidance only, not a substitute for certified lab testing.
      </div>
    </section>
  );

  const handleFeatureHover = (e) => {
    e.currentTarget.style.boxShadow = '0 8px 32px 0 rgba(33,150,243,0.18)';
    e.currentTarget.style.transform = 'translateY(-8px) scale(1.03)';
    e.currentTarget.style.borderColor = '#90caf9';
  };

  const handleFeatureLeave = (e) => {
    e.currentTarget.style.boxShadow = '0 4px 24px 0 rgba(33,150,243,0.10)';
    e.currentTarget.style.transform = 'translateY(0) scale(1)';
    e.currentTarget.style.borderColor = '#e3f2fd';
  };

  const handleButtonHover = (e) => {
    e.currentTarget.style.background = 'linear-gradient(90deg, #1565c0 60%, #1976d2 100%)';
    e.currentTarget.style.transform = 'translateY(-4px) scale(1.04)';
    e.currentTarget.style.boxShadow = '0 8px 32px 0 rgba(33,150,243,0.18)';
  };

  const handleButtonLeave = (e) => {
    e.currentTarget.style.background = 'linear-gradient(90deg, #1976d2 60%, #64b5f6 100%)';
    e.currentTarget.style.transform = 'translateY(0) scale(1)';
    e.currentTarget.style.boxShadow = '0 4px 16px 0 rgba(33,150,243,0.10)';
  };

  return (
    <div style={{position: 'relative'}}>
      {/* Hero Section */}
      <div style={styles.hero}>
        <div style={{maxWidth: '1280px', margin: '0 auto'}}>
          <div style={{textAlign: 'center'}}>
            <div style={{display: 'flex', justifyContent: 'center', marginBottom: '2rem'}}>
              <div style={{position: 'relative'}}>
                <div style={{
                  width: '6rem', 
                  height: '6rem',
                  background: 'linear-gradient(135deg, #1976d2, #00bcd4)',
                  borderRadius: '50%',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  boxShadow: '0 4px 16px rgba(25, 118, 210, 0.3)'
                }}>
                  <Waves style={{width: '3rem', height: '3rem', color: 'white'}} />
                </div>
                <div style={{
                  position: 'absolute',
                  top: '-0.5rem',
                  right: '-0.5rem',
                  width: '1.5rem',
                  height: '1.5rem',
                  background: '#22c55e',
                  borderRadius: '50%',
                  border: '4px solid white',
                  animation: 'pulse 2s infinite'
                }}></div>
              </div>
            </div>
            <h1 style={styles.heroTitle}>
              Welcome to{' '}
              <span style={{background: 'linear-gradient(to right, #1976d2, #64b5f6)', WebkitBackgroundClip: 'text', color: 'transparent'}}>
                Water Quality
              </span>{' '}
              Prediction
            </h1>
            <p style={styles.heroSubtitle}>
               Predict water potability with ease. Secure, fast, and insightful monitoring system for communities worldwide.
            </p>
            <div style={styles.ctaButtons}>
              <a 
                href="/register" 
                style={styles.ctaBtn}
                onMouseEnter={handleButtonHover}
                onMouseLeave={handleButtonLeave}
              >
                Create Free Account
              </a>
              <a 
                href="/login" 
                style={styles.ctaBtn}
                onMouseEnter={handleButtonHover}
                onMouseLeave={handleButtonLeave}
              >
                Sign In
              </a>
            </div>
          </div>
        </div>
      </div>

      {/* Project Description Section */}
      {descriptionSection}

      {/* Stats Section */}
      <div style={styles.statsSection}>
        <div style={{maxWidth: '1280px', margin: '0 auto', padding: '0 1rem'}}>
          <div style={{display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '2rem'}}>
            {stats.map((stat, index) => (
              <div key={index} style={styles.statBox}>
                <div style={styles.statNumber}>{stat.number}</div>
                <div style={styles.statLabel}>{stat.label}</div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Features Section */}
      <div style={styles.featuresSection}>
        <div style={{maxWidth: '1280px', margin: '0 auto'}}>
          <div style={{textAlign: 'center', marginBottom: '4rem'}}>
            <h2 style={{...styles.heroTitle, fontSize: '2.5rem'}}>Powerful Features for Water Quality Management</h2>
            <p style={{...styles.heroSubtitle, fontSize: '1.25rem'}}>Our comprehensive platform provides everything you need to monitor, analyze, and predict water quality with precision</p>
          </div>
          <div style={{display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '2rem', padding: '0 1rem'}}>
            {features.map((feature, index) => (
              <div 
                key={index} 
                style={styles.featureCard}
                onMouseEnter={handleFeatureHover}
                onMouseLeave={handleFeatureLeave}
              >
                <div style={styles.featureIcon}>{feature.icon}</div>
                <h3 style={styles.featureTitle}>{feature.title}</h3>
                <p style={styles.featureDesc}>{feature.description}</p>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Benefits Section */}
      <div style={styles.benefitsSection}>
        <div style={{maxWidth: '1280px', margin: '0 auto', padding: '0 1rem'}}>
          <div style={{textAlign: 'center', marginBottom: '4rem'}}>
            <h2 style={{...styles.ctaTitle, color: '#fff'}}>Why Choose Water Quality Prediction?</h2>
            <p style={{...styles.ctaDesc, color: '#e3f2fd'}}>Join thousands of organizations worldwide who trust our platform</p>
          </div>
          <div style={{display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '2rem'}}>
            <div style={styles.benefitCard}>
              <CheckCircle style={{width: '2rem', height: '2rem', color: '#4ade80', marginBottom: '1rem'}} />
              <h3 style={{...styles.featureTitle, color: '#fff'}}>Interactive Dashboard</h3>
              <p style={{color: '#e3f2fd'}}>Visualize your water quality data with interactive charts, graphs, and real-time updates. Get instant insights and make data-driven decisions with our intuitive interface.</p>
            </div>
            <div style={styles.benefitCard}>
              <CheckCircle style={{width: '2rem', height: '2rem', color: '#4ade80', marginBottom: '1rem'}} />
              <h3 style={{...styles.featureTitle, color: '#fff'}}>Google Sign-in Supported</h3>
              <p style={{color: '#e3f2fd'}}>Secure and convenient authentication with Google sign-in integration. Access your account quickly and safely with enterprise-grade security.</p>
            </div>
          </div>
        </div>
      </div>

      {/* CTA Section */}
      <div style={styles.ctaSection}>
        <div style={{maxWidth: '1024px', margin: '0 auto', textAlign: 'center'}}>
          <h2 style={styles.ctaTitle}>Ready to Start Monitoring Water Quality?</h2>
          <p style={styles.ctaDesc}>Join our platform today and ensure the safety and quality of your water sources</p>
          <div style={styles.ctaButtons}>
            <a 
              href="/register" 
              style={styles.ctaBtn}
              onMouseEnter={handleButtonHover}
              onMouseLeave={handleButtonLeave}
            >
              Create Free Account
            </a>
            <a 
              href="/login" 
              style={styles.ctaBtn}
              onMouseEnter={handleButtonHover}
              onMouseLeave={handleButtonLeave}
            >
              Sign In
            </a>
          </div>
        </div>
      </div>

      {/* Footer */}
      <footer style={{
        background: 'linear-gradient(90deg, #1976d2 60%, #64b5f6 100%)',
        color: '#fff',
        padding: '1.5rem 0',
        textAlign: 'center',
        fontWeight: 500,
        fontSize: '1.1rem',
        letterSpacing: '0.5px',
        marginTop: '2rem',
        borderTopLeftRadius: '2rem',
        borderTopRightRadius: '2rem',
      }}>
        Made with ❤️ by <span style={{fontWeight: 700}}>Parth Mhatre</span> |
        <a href="https://github.com/Parth-S-Mhatre" target="_blank" rel="noopener noreferrer" style={{color: '#fff', marginLeft: 8, display: 'inline-block', verticalAlign: 'middle'}} aria-label="GitHub">
          {githubIcon}
        </a>
      </footer>
      
      <style jsx>{`
        @keyframes pulse {
          0%, 100% { opacity: 1; }
          50% { opacity: 0.5; }
        }
      `}</style>
    </div>
  );
};

export default LandingPage;

