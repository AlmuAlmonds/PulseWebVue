import { createRouter, createWebHistory } from 'vue-router'
import axios from 'axios'

import RoleSelection from '@/components/RoleSelection.vue'
import AdminSignIn from '@/components/AdminSignIn.vue'
import DispatcherSignIn from '@/components/DispatcherSignIn.vue'
import DispatchDashboard from '@/components/DispatchDashboard.vue'
import UserSignIn from '@/components/UserSignIn.vue'
import AdminDashboard from '@/components/AdminDashboard.vue'
import Accounts from '@/components/accounts.vue'

const routes = [
  { path: '/', component: RoleSelection },
  { path: '/admin', alias: ['/AdminSignIn'], component: AdminSignIn },
  { path: '/dispatcher', component: DispatcherSignIn },
  { path: '/DispatchDashboard', alias: ['/dispatchdashboard'], component: DispatchDashboard, meta: { requiresDispatcherAuth: true } },
  { path: '/user', component: UserSignIn },
  { path: '/AdminDashboard', alias: ['/admindashboard'], component: AdminDashboard, meta: { requiresAdminAuth: true } },
  { path: '/accounts', name: 'Accounts', component: Accounts}
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('authToken')
  const role = localStorage.getItem('authRole')

  if (to.meta.requiresAdminAuth) {
    if (!token || role !== '1') {
      next('/AdminSignIn')
      return
    }

    axios.defaults.headers.common.Authorization = `Bearer ${token}`
    next()
    return
  }

  if (to.meta.requiresDispatcherAuth) {
    if (!token || role !== '2') {
      next('/dispatcher')
      return
    }

    axios.defaults.headers.common.Authorization = `Bearer ${token}`
    next()
    return
  }

  next()
})

export default router