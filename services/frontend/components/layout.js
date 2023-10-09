import Navigation from "./navigation";

export default function Layout({ children }) {
    return (
      <>
        <Navigation></Navigation>
        <main>{children}</main>
      </>
    );
  }