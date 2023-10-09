<script setup>
import { ref } from 'vue'
import ProfileGroup from './ProfileGroup.vue'

const groups = ref([
    {id: 1, name: "Group 1", description: "Happy guys", members: [
        {name: "John Doe", username: "johndown"},
        {name: "John One Doe", username: "johndown"},
        {name: "John Other Doe", username: "johndown"}, 
    ]},
    {id: 2, name: "Group 2", description: "Happy guys 2", members: [
        {name: "Diana Doe", username: "johndown"},
    ]},
    {id: 3, name: "Group 3", description: "Happy guys 3", members: [
        {name: "Chris Doe", username: "johndown"},
        {name: "John Von Doe", username: "johndown"}, 
    ]},
])

</script>

<template>
    <section class="container">
        <div class="my-3 p-3 bg-body rounded shadow-sm">
            <div class="d-flex justify-content-between border-bottom pb-2 mb-0">
                <h5>Groups</h5>
                <div class="btn-group btn-group-sm">
                    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#newGroup">New Group</button>
                        <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false" data-bs-auto-close="outside">
                            Join Group
                        </button>
                        <form class="dropdown-menu dropdown-menu-end p-3">
                            <div class="input-group">
                                <!--<label for="joinCode" class="form-label">Join code</label>-->
                                <input type="username" class="form-control form-control-sm" placeholder="Join code" required>
                                <button type="submit" class="btn btn-primary btn-sm">Join</button>
                                <div class="form-text">Enter a code from a friend.</div>
                            </div>
                            
                        </form>
                </div>
                    
            </div>
            <ProfileGroup 
                v-for="group in groups" 
                :group="group"
                :key="group.id"
            />
        </div>
    </section>

    <!-- Modal -->
    <div class="modal fade" id="newGroup" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="newGroupLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <h1 class="modal-title fs-5" id="newGroupLabel">Create a new group</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
            <form>
                <div class="mb-3">
                    <label for="recipient-name" class="col-form-label">Group name:</label>
                    <input type="text" class="form-control" id="recipient-name">
                </div>
                <div class="mb-3">
                    <label for="message-text" class="col-form-label">Group description:</label>
                    <textarea class="form-control" id="message-text"></textarea>
                </div>
                </form>
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary btn" data-bs-dismiss="modal">Cancel</button>
            <button type="button" class="btn btn-primary btn">Create Group</button>
        </div>
        </div>
    </div>
    </div>
</template>

<style>

.dropdown-menu {
    min-width:15rem;
}
</style>