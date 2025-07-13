import React from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useAuth } from './index'
import { doSignOut } from '../firebase/auth'

const Header = () => {
    const navigate = useNavigate()
    const { userLoggedIn } = useAuth()
    return (
        <nav className="flex flex-row gap-x-4 w-full z-20 fixed top-0 left-0 h-14 border-b place-content-center items-center bg-white/80 backdrop-blur-md shadow-md px-8 animate-fade-in-down transition-all duration-500">
            <Link to="/" className="text-xl font-bold text-blue-700 tracking-wide hover:text-blue-900 transition-colors duration-200">Water Quality</Link>
            <div className="flex-1"></div>
            {userLoggedIn ? (
                <button
                    onClick={() => { doSignOut().then(() => { navigate('/login') }) }}
                    className="text-sm text-white bg-blue-600 px-4 py-2 rounded-lg shadow hover:bg-blue-700 transition-all duration-300"
                >Logout</button>
            ) : (
                <>
                    <Link className="text-sm text-blue-600 hover:text-blue-800 px-4 py-2 rounded-lg transition-all duration-300" to={'/login'}>Login</Link>
                    <Link className="text-sm text-blue-600 hover:text-blue-800 px-4 py-2 rounded-lg transition-all duration-300" to={'/register'}>Register</Link>
                </>
            )}
        </nav>
    )
}

export default Header