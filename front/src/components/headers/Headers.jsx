import { NavLink } from 'react-router-dom';
import Menu from '../../static/image/menu.svg'

const Header = () => {


    return (
        <header className="header">
            <div className="container">
                <div className="header_items">

                    <NavLink to={"/"} className="logo">Logo</NavLink>
                    <div className="menu">
                        <img src={Menu} alt="menu" />
                    </div>

                </div>
            </div>
        </header>
    )
}

export default Header;