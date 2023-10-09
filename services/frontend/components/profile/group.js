export default function Group({ group }) {
    const memberItems = group.members.map((member, index) => 
        <li key={member.id} className="member-item py-1 me-2">
            <a className="member-link" href={member.username}>
                <i className="bi-person-circle"></i>
                {member.name}
            </a>
            {group.members.length !== index + 1 ? <span>,</span> : ''}
        </li>
    );
    return (
    <div className="d-flex text-muted pt-3">
        <div className="feature-icon bg-primary bg-gradient flex-shrink-0 me-2">
            <i className="bi-people-fill group-icon"></i>
        </div>
        
        <div className="pb-3 mb-0 small lh-sm border-bottom">
            <strong className="d-block text-gray-dark">{group.name}</strong>
            {group.description}
            <ul className="member-list d-flex flex-row">
                {memberItems}
            </ul>
        </div>
    </div>
    );
}