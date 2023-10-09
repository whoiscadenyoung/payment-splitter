import Head from 'next/head';
import styles from '../styles/Home.module.css';
import Layout from '../components/layout';
import Groups from '../components/profile/groups';
import Expenses from '../components/profile/expenses';

export default function Home() {
  return (
    <Layout>
      <Head>
        <title>Create Next App</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Groups></Groups>
      <Expenses></Expenses>
    </Layout>
    );
  }