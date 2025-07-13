import React, { useState } from 'react'
import { Navigate, Link } from 'react-router-dom'
import { useAuth } from './index'
import { doCreateUserWithEmailAndPassword } from '../firebase/auth'
import styles from './login.module.css';

const Register = () => {

    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [confirmPassword, setconfirmPassword] = useState('')
    const [isRegistering, setIsRegistering] = useState(false)
    const [errorMessage] = useState('')

    const { userLoggedIn } = useAuth()

    const onSubmit = async (e) => {
        e.preventDefault()
        if(!isRegistering) {
            setIsRegistering(true)
            await doCreateUserWithEmailAndPassword(email, password)
        }
    }

    // Add a spinner component
    const Spinner = () => (
      <svg className="animate-spin h-5 w-5 text-white inline-block ml-2" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
        <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
        <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8z"></path>
      </svg>
    );

    return (
        <div className={styles.loginBg}>
            {userLoggedIn && (<Navigate to={'/home'} replace={true} />)}
            <main style={{ minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                <div className={styles.loginCard}>
                    <div className={styles.loginTitle}>Create a New Account</div>
                    <form onSubmit={onSubmit}>
                        <label>Email</label>
                        <input className={styles.loginInput} type="email" autoComplete='email' required value={email} onChange={(e) => { setEmail(e.target.value) }} />
                        <label>Password</label>
                        <input className={styles.loginInput} disabled={isRegistering} type="password" autoComplete='new-password' required value={password} onChange={(e) => { setPassword(e.target.value) }} />
                        <label>Confirm Password</label>
                        <input className={styles.loginInput} disabled={isRegistering} type="password" autoComplete='off' required value={confirmPassword} onChange={(e) => { setconfirmPassword(e.target.value) }} />
                        {errorMessage && (<span style={{ color: 'red', fontWeight: 'bold' }}>{errorMessage}</span>)}
                        <button type="submit" disabled={isRegistering} className={styles.loginBtn}>
                            {isRegistering ? (<><span>Signing Up...</span><Spinner /></>) : 'Sign Up'}
                        </button>
                        <div style={{ textAlign: 'center', margin: '1rem 0 0.5rem 0' }}>
                            Already have an account? <Link to={'/login'} className={styles.link}>Continue</Link>
                        </div>
                    </form>
                </div>
            </main>
        </div>
    )
}

export default Register