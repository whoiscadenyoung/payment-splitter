import Link from 'next/link';

export default function Navigation() {
    return (
        <nav className="navbar navbar-expand-lg bg-dark" data-bs-theme="dark">
        <div className="container-fluid">
          <a className="navbar-brand" href="#">Payment Splitter</a>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div className="navbar-nav me-auto">
            <Link className="nav-link active" aria-current="page" href="/">Home</Link>
            <Link className="nav-link" href="/about">About</Link>
            <Link className="nav-link" href="/profile">Profile</Link>
          </div>
          <a className="nav-link dropdown-toggle btn btn-primary position-relative" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            <i className="bi-person-circle navbar-icon"></i>
            <span className="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
              99+
              <span className="visually-hidden">unread messages</span>
            </span>
          </a>
          </div>
          </div>
        </nav>
    );
}