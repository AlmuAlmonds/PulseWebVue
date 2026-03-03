import { createRouter, createWebHistory } from 'vue-router'

import RoleSelection from '@/components/RoleSelection.vue'
import AdminSignIn from '@/components/AdminSignIn.vue'
import DispatcherSignIn from '@/components/DispatcherSignIn.vue'
import UserSignIn from '@/components/UserSignIn.vue'
import AdminDashboard from '@/components/AdminDashboard.vue'
import Accounts from '@/components/accounts.vue'

const routes = [
  { path: '/', component: RoleSelection },
  { path: '/admin', component: AdminSignIn },
  { path: '/dispatcher', component: DispatcherSignIn },
  { path: '/user', component: UserSignIn },
  { path: '/admindashboard', component: AdminDashboard },
  { path: '/accounts', name: 'Accounts', component: Accounts}
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router