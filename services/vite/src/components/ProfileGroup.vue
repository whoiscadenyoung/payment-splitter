<script setup>
defineProps(['group'])
</script>

<template>
    <div class="d-flex text-muted pt-3">
        <div class="feature-icon bg-primary bg-gradient flex-shrink-0 me-2">
            <i class="bi-people-fill group-icon"></i>
        </div>
        
        <p class="pb-3 mb-0 small lh-sm border-bottom">
            <strong class="d-block text-gray-dark">{{ group.name }}</strong>
            {{ group.description }}
            <ul class="member-list d-flex flex-row">
                <li class="member-item py-1 me-2" v-for="(member, index) in group.members" :key="member.username">
                    <a class="member-link" href="{{ member.username }}">
                        <i class="bi-person-circle"></i>
                        {{ member.name }}
                    </a>
                    <span v-if="index !== group.members.length - 1">,</span>
                </li>
            </ul>
        </p>
    </div>

    
</template>
<style>
.member-list {
    list-style: none;
    padding-left: 0;
    margin-bottom: 0;
}
.member-item {

}
.member-link {
    text-decoration: none;
}
.group-icon {
    color: white;
}
.feature-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 3rem;
    height: 3rem;
    font-size: 2rem;
    color: #fff;
    border-radius: .75rem;
}
</style>