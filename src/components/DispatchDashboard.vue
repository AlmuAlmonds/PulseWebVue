<script setup>
import { onBeforeUnmount, onMounted, ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const router = useRouter()
const userName = ref('Dispatch User')
const userRole = 'Dispatch'
const authCheckMessage = ref('')
const showUserMenu = ref(false)
const userMenuRef = ref(null)

const toggleUserMenu = () => {
  showUserMenu.value = !showUserMenu.value
}

const closeUserMenu = () => {
  showUserMenu.value = false
}

const goToSettings = () => {
  closeUserMenu()
  router.push('/accounts')
}

const handleLogout = () => {
  localStorage.removeItem('authToken')
  localStorage.removeItem('authRole')
  localStorage.removeItem('authFirstName')
  localStorage.removeItem('authLastName')
  delete axios.defaults.headers.common.Authorization
  closeUserMenu()
  router.push('/dispatcher')
}

const handleClickOutside = (event) => {
  if (userMenuRef.value && !userMenuRef.value.contains(event.target)) {
    closeUserMenu()
  }
}

const verifyDispatcherSession = async () => {
  const token = localStorage.getItem('authToken')
  const role = localStorage.getItem('authRole')

  if (!token || role !== '2') {
    router.push('/dispatcher')
    return
  }

  try {
    const response = await axios.get('http://127.0.0.1:8000/api/dispatch/dashboard/', {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })

    const firstName = response.data?.first_name || ''
    const lastName = response.data?.last_name || ''
    const fullName = `${firstName} ${lastName}`.trim()

    userName.value = fullName || 'Dispatch User'
    authCheckMessage.value = response.data?.message || 'Authenticated dispatcher session verified.'
  } catch (error) {
    if (error.response && (error.response.status === 401 || error.response.status === 403)) {
      localStorage.removeItem('authToken')
      localStorage.removeItem('authRole')
      localStorage.removeItem('authFirstName')
      localStorage.removeItem('authLastName')
      router.push('/dispatcher')
      return
    }

    authCheckMessage.value = 'Network error while verifying dispatcher session.'
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
  verifyDispatcherSession()
})

onBeforeUnmount(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>

<template>
  <div class="dashboard-container">
    <div class="sidebar">
      <div class="logo-section">
        <img src="@/assets/images/PULSE OG.png" alt="PULSE Logo" class="logo" />
        <span class="logo-text">PULSE Dispatch</span>
      </div>

      <nav class="nav-menu">
        <a href="#" class="nav-item active">
          <span class="icon">📊</span>
          <span>Dashboard</span>
        </a>
        <a href="#" class="nav-item">
          <span class="icon">🚨</span>
          <span>Emergencies</span>
        </a>
        <a href="#" class="nav-item">
          <span class="icon">🚓</span>
          <span>Dispatch</span>
        </a>
      </nav>

      <div class="security-section">
        <div class="section-title">OPERATIONS</div>
        <a href="#" class="nav-item">
          <span class="icon">📋</span>
          <span>Reports</span>
        </a>
      </div>
    </div>

    <div class="main-content">
      <div class="top-bar">
        <button class="menu-btn">← Menu</button>
        <div class="search-container">
          <input type="text" placeholder="Search..." class="search-input" />
        </div>
        <div class="top-bar-right" ref="userMenuRef">
          <button class="notification-btn">🔔</button>
          <button class="notification-btn">📢</button>
          <button class="user-profile" type="button" @click.stop="toggleUserMenu">
            <img src="@/assets/images/PULSE OG.png" alt="Avatar" class="avatar" />
            <div class="user-info">
              <div class="user-name">{{ userName }}</div>
              <div class="user-role">{{ userRole }}</div>
            </div>
          </button>

          <div v-if="showUserMenu" class="user-dropdown">
            <button class="dropdown-item" type="button" @click="goToSettings">Settings</button>
            <button class="dropdown-item logout" type="button" @click="handleLogout">Logout</button>
          </div>
        </div>
      </div>

      <div class="content">
        <div class="header-section">
          <h1>PULSE System Analytics</h1>
          <p class="subtitle">Real-time research evaluation and system performance metrics</p>
          <p v-if="authCheckMessage" class="subtitle">{{ authCheckMessage }}</p>
          <div class="time-display">04:10:14 PM</div>
        </div>

        <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-icon users">👥</div>
            <div class="stat-content">
              <h3>Total Users</h3>
              <div class="stat-number">2,847</div>
              <p class="stat-growth">12% growth this month</p>
            </div>
          </div>

          <div class="stat-card">
            <div class="stat-icon active">✓</div>
            <div class="stat-content">
              <h3>Active Users (Last 30d)</h3>
              <div class="stat-number">1,923</div>
              <p class="stat-growth active-growth">↑ 67.6% engagement rate</p>
            </div>
          </div>

          <div class="stat-card">
            <div class="stat-icon new">📝</div>
            <div class="stat-content">
              <h3>New Registrations</h3>
              <div class="stat-number">324</div>
              <p class="stat-growth">This month</p>
            </div>
          </div>

          <div class="stat-card">
            <div class="stat-icon reports">🔔</div>
            <div class="stat-content">
              <h3>Total Reports</h3>
              <div class="stat-number">5,246</div>
              <p class="stat-growth">↑ All-time aggregate</p>
            </div>
          </div>
        </div>

        <div class="charts-grid">
          <div class="chart-card">
            <h3>Total Emergency Reports</h3>
            <div class="dropdown">
              <select>
                <option>Yearly</option>
              </select>
            </div>
            <div class="chart-content">
              <div class="chart-number">2,847</div>
              <p>Reports this year (2026)</p>
              <div class="chart-placeholder">Chart Area</div>
            </div>
          </div>

          <div class="chart-card">
            <h3>Active Incidents</h3>
            <span class="live-badge">LIVE</span>
            <div class="incidents-content">
              <div class="incidents-count">47</div>
              <p>Currently being handled</p>
              <div class="incident-list">
                <div class="incident-item">
                  <span class="incident-dot open"></span>
                  <span>Open</span>
                  <span class="incident-number">18</span>
                </div>
                <div class="incident-item">
                  <span class="incident-dot progress"></span>
                  <span>In-Progress</span>
                  <span class="incident-number">21</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="dashboard-footer">
          <p>PULSE CEDOC Dispatch Panel</p>
          <div class="footer-links">
            <a href="#">Term & Conditions</a>
            <a href="#">Privacy & Security</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.dashboard-container {
  display: flex;
  min-height: 100vh;
  background-color: #f5f5f5;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

.sidebar {
  width: 256px;
  background: white;
  border-right: 1px solid #e5e7eb;
  padding: 20px;
  overflow-y: auto;
}

.logo-section {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 30px;
  padding-bottom: 20px;
  border-bottom: 1px solid #e5e7eb;
}

.logo {
  width: 40px;
  height: 40px;
  object-fit: contain;
}

.logo-text {
  font-size: 18px;
  font-weight: 600;
  color: #1f2937;
}

.nav-menu {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 30px;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  color: #6b7280;
  text-decoration: none;
  border-radius: 6px;
  transition: all 0.3s ease;
  cursor: pointer;
}

.nav-item:hover {
  background-color: #f3f4f6;
  color: #1f2937;
}

.nav-item.active {
  background-color: #e0e7ff;
  color: #2563eb;
}

.security-section {
  padding-top: 20px;
  border-top: 1px solid #e5e7eb;
}

.section-title {
  font-size: 12px;
  font-weight: 700;
  color: #f59e0b;
  text-transform: uppercase;
  margin-bottom: 12px;
  letter-spacing: 0.5px;
}

.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.top-bar {
  background: white;
  display: flex;
  align-items: center;
  gap: 20px;
  padding: 16px 30px;
  border-bottom: 1px solid #e5e7eb;
}

.menu-btn {
  background-color: #2563eb;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 600;
  transition: background-color 0.3s ease;
}

.menu-btn:hover {
  background-color: #1d4ed8;
}

.search-container {
  flex: 1;
  max-width: 400px;
}

.search-input {
  width: 100%;
  padding: 10px 16px;
  border: 1px solid #e5e7eb;
  border-radius: 6px;
  background-color: #f9fafb;
  font-size: 14px;
}

.search-input::placeholder {
  color: #9ca3af;
}

.top-bar-right {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-left: auto;
  position: relative;
}

.notification-btn {
  background: none;
  border: none;
  font-size: 20px;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.notification-btn:hover {
  transform: scale(1.1);
}

.user-profile {
  display: flex;
  align-items: center;
  gap: 12px;
  padding-left: 16px;
  border-left: 1px solid #e5e7eb;
  background: transparent;
  border-top: none;
  border-right: none;
  border-bottom: none;
  cursor: pointer;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  object-fit: cover;
}

.user-info {
  text-align: right;
}

.user-name {
  font-weight: 600;
  color: #1f2937;
  font-size: 14px;
}

.user-role {
  color: #6b7280;
  font-size: 12px;
}

.user-dropdown {
  position: absolute;
  top: calc(100% + 8px);
  right: 0;
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  min-width: 150px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  z-index: 20;
  overflow: hidden;
}

.dropdown-item {
  width: 100%;
  text-align: left;
  background: white;
  border: none;
  padding: 10px 14px;
  color: #1f2937;
  font-size: 14px;
  cursor: pointer;
}

.dropdown-item:hover {
  background-color: #f3f4f6;
}

.dropdown-item.logout {
  color: #dc2626;
}

.content {
  flex: 1;
  padding: 30px;
  overflow-y: auto;
}

.header-section {
  margin-bottom: 30px;
  position: relative;
}

.header-section h1 {
  font-size: 32px;
  color: #1f2937;
  margin-bottom: 8px;
}

.subtitle {
  color: #6b7280;
  font-size: 14px;
  margin-bottom: 20px;
}

.time-display {
  position: absolute;
  top: 0;
  right: 0;
  color: #9ca3af;
  font-size: 14px;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.stat-card {
  background: white;
  border-radius: 8px;
  padding: 24px;
  display: flex;
  gap: 16px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.stat-icon {
  width: 50px;
  height: 50px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  flex-shrink: 0;
}

.stat-icon.users {
  background-color: #dbeafe;
}

.stat-icon.active {
  background-color: #dcfce7;
}

.stat-icon.new {
  background-color: #fed7aa;
}

.stat-icon.reports {
  background-color: #fee2e2;
}

.stat-content h3 {
  font-size: 14px;
  color: #6b7280;
  font-weight: 500;
  margin-bottom: 8px;
}

.stat-number {
  font-size: 28px;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 8px;
}

.stat-growth {
  color: #3b82f6;
  font-size: 12px;
}

.stat-growth.active-growth {
  color: #10b981;
}

.charts-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.chart-card {
  background: white;
  border-radius: 8px;
  padding: 24px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  position: relative;
}

.chart-card h3 {
  font-size: 16px;
  color: #1f2937;
  margin-bottom: 16px;
}

.dropdown {
  position: absolute;
  top: 24px;
  right: 24px;
}

.dropdown select {
  padding: 6px 12px;
  border: 1px solid #e5e7eb;
  border-radius: 4px;
  background-color: white;
  cursor: pointer;
  font-size: 14px;
}

.chart-content {
  margin-top: 20px;
}

.chart-number {
  font-size: 32px;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 8px;
}

.chart-content p {
  color: #6b7280;
  font-size: 14px;
  margin-bottom: 20px;
}

.chart-placeholder {
  background: linear-gradient(135deg, #f0f0f0 0%, #e0e0e0 100%);
  height: 200px;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #9ca3af;
}

.live-badge {
  position: absolute;
  top: 24px;
  right: 24px;
  background-color: #dc2626;
  color: white;
  padding: 4px 12px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 600;
}

.incidents-content {
  margin-top: 20px;
}

.incidents-count {
  font-size: 32px;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 8px;
}

.incident-list {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.incident-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  background-color: #f9fafb;
  border-radius: 6px;
}

.incident-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  flex-shrink: 0;
}

.incident-dot.open {
  background-color: #fb923c;
}

.incident-dot.progress {
  background-color: #3b82f6;
}

.incident-item > span:nth-child(2) {
  flex: 1;
  color: #1f2937;
  font-size: 14px;
  font-weight: 500;
}

.incident-number {
  color: #1f2937;
  font-weight: 600;
}

.dashboard-footer {
  color: #9ca3af;
  font-size: 12px;
  text-align: center;
  padding-top: 20px;
  border-top: 1px solid #e5e7eb;
  margin-top: 20px;
}

.dashboard-footer p {
  margin-bottom: 8px;
}

.footer-links {
  display: flex;
  gap: 20px;
  justify-content: center;
}

.footer-links a {
  color: #9ca3af;
  text-decoration: none;
  transition: color 0.3s ease;
}

.footer-links a:hover {
  color: #6b7280;
}
</style>
