<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
    <nav class="navbar navbar-expand-lg bg-dark" data-bs-theme="dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Payment Splitter</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div class="navbar-nav me-auto">
            <RouterLink class="nav-link active" aria-current="page" to="/">Home</RouterLink>
            <RouterLink class="nav-link" to="/about">About</RouterLink>
            <RouterLink class="nav-link" to="/profile">Profile</RouterLink>
          </div>
          <a class="nav-link dropdown-toggle btn btn-primary position-relative" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            <i class="bi-person-circle navbar-icon"></i>
            <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
                99+
                <span class="visually-hidden">unread messages</span>
            </span>
          </a>
        </div>
        </div>
    </nav>
</template>

<style>
.navbar-icon {
    color: white;
}
</style>