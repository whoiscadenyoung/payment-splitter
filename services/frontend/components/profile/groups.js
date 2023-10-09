import Group from './group';

const groups = [
    {id: 1, name: "Group 1", description: "Happy guys", members: [
        {id: 0, name: "John Doe", username: "johndown"},
        {id: 1, name: "John One Doe", username: "johndown"},
        {id: 2, name: "John Other Doe", username: "johndown"}, 
    ]},
    {id: 2, name: "Group 2", description: "Happy guys 2", members: [
        {id: 3, name: "Diana Doe", username: "johndown"},
    ]},
    {id: 3, name: "Group 3", description: "Happy guys 3", members: [
        {id: 4, name: "Chris Doe", username: "johndown"},
        {id: 5, name: "John Von Doe", username: "johndown"}, 
    ]},
]

export default function Groups() {
    const groupItems = groups.map((group) =>
        <Group group={group} key={group.id}></Group>
    );
    return (
        <>
        <section className="container">
        <div className="my-3 p-3 bg-body rounded shadow-sm">
            <div className="d-flex justify-content-between border-bottom pb-2 mb-0">
                <h5>Groups</h5>
                <div className="btn-group btn-group-sm">
                    <button type="button" className="btn btn-primary" data-bs-toggle="modal" data-bs-target="#newGroup">New Group</button>
                        <button type="button" className="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false" data-bs-auto-close="outside">
                            Join Group
                        </button>
                        <form className="dropdown-menu dropdown-menu-end p-3">
                            <div className="input-group">
                                <label htmlFor="joinCode" className="form-label">Join code</label>
                                <input type="username" className="form-control form-control-sm" placeholder="Join code" required/>
                                <button type="submit" className="btn btn-primary btn-sm">Join</button>
                                <div className="form-text">Enter a code from a friend.</div>
                            </div>
                            
                        </form>
                </div>
                    
            </div>
            {groupItems}
        </div>
    </section>

    <div className="modal fade" id="newGroup" data-bs-backdrop="static" data-bs-keyboard="false" tabIndex="-1" aria-labelledby="newGroupLabel" aria-hidden="true">
    <div className="modal-dialog">
        <div className="modal-content">
        <div className="modal-header">
            <h1 className="modal-title fs-5" id="newGroupLabel">Create a new group</h1>
            <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div className="modal-body">
            <form>
                <div className="mb-3">
                    <label htmlFor="recipient-name" className="col-form-label">Group name:</label>
                    <input type="text" className="form-control" id="recipient-name"/>
                </div>
                <div className="mb-3">
                    <label htmlFor="message-text" className="col-form-label">Group description:</label>
                    <textarea className="form-control" id="message-text"></textarea>
                </div>
                </form>
        </div>
        <div className="modal-footer">
            <button type="button" className="btn btn-secondary btn" data-bs-dismiss="modal">Cancel</button>
            <button type="button" className="btn btn-primary btn">Create Group</button>
        </div>
        </div>
    </div>
    </div>
    </>

    );
}