import '../styles/global.scss';
import { useEffect } from 'react';

export default function App({ Component, pageProps }) {
  useEffect(() => {
    require("bootstrap/dist/js/bootstrap.bundle")
  })
    return <Component {...pageProps} />;
  }