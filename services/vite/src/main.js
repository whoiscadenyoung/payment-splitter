// Import our custom CSS
import './assets/styles.scss'

// Import only necessary bootstrap components from JavaScript
import { Modal } from 'bootstrap';

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
