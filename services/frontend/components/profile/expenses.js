import { useState, useEffect } from 'react'

export default function Expenses() {
    const [data, setData] = useState(null)
    const [isLoading, setLoading] = useState(true)
    
    useEffect(() => {
        const fetchData = async () => {
            try {
                fetch('http://localhost:8000/users')
                .then((res) => res.json())
                .then((newData) => {
                    setData(newData)
                    setLoading(false)
                })
            } catch (err) {
                console.log(err)
            }
        }
        fetchData();
    }, [])

    if (isLoading) return <p>Loading...</p>
    if (!data) return <p>No user data</p>

    return (
        <section className="container">
            <div className="my-3 p-3 bg-body rounded shadow-sm">
                <div className="d-flex justify-content-between border-bottom pb-2 mb-0">
                    <h5>Expenses</h5>      
                </div>
                {data && data.map((user) => <p>{user.email}</p>)}
            </div>
        </section>
    )
}