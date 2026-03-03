<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goAdmin = () => {
  router.push('/admin')
}

const goUser = () => {
  router.push('/user')
}

const goDispatcher = () => {
  router.push('/dispatcher')
}
</script>

<template>
  <div class="signin-container">
    <div class="signin-card">
      <img class="brand-logo" src="@/assets/images/PULSE OG.png" alt="Brand Logo" />
      <h1>Welcome Back!</h1>
      <p class="subtitle">Please click or tap your destination.</p>

      <button class="btn btn-admin" @click="goAdmin">Admin</button>
      <button class="btn btn-dispatcher" @click="goDispatcher">Dispatcher</button>
      <button class="btn btn-user" @click="goUser">User</button>

      <p class="legal-text">By using this service, you understand and agree to the PULSE Online Services <a href="#">Terms of Use</a> and <a href="#">Privacy Statement</a></p>
    </div>
  </div>
</template>

<style scoped>
.signin-container {
  background: url('@/assets/images/San_Juan_City_Hall.jpg') center/cover no-repeat;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
}

.signin-card {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(6px);
  border-radius: 16px;
  padding: 48px 32px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 100%;
  max-width: 500px;
  margin: 20px;
  text-align: center;
}

.brand-logo {
  width: 100px;
  height: 100px;
  object-fit: contain;
  margin: 0 auto 16px;
}

h1 {
  font-weight: 700;
  margin-bottom: 8px;
  font-size: 1.5rem;
  color: #1f2937;
}

.subtitle {
  color: #6b7280;
  margin-bottom: 28px;
  font-size: 0.95rem;
}

.btn {
  width: 100%;
  padding: 16px 18px;
  font-size: 1.1rem;
  border: none;
  cursor: pointer;
  border-radius: 6px;
  font-weight: 600;
  transition: all 0.3s ease;
  margin-bottom: 12px;
}

.btn-admin {
  background-color: #2563eb;
  color: white;
}

.btn-admin:hover {
  background-color: #1d4ed8;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.4);
}

.btn-user {
  background-color: #10b981;
  color: white;
}

.btn-user:hover {
  background-color: #059669;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.4);
}

.btn-dispatcher {
  background-color: #dc2626;
  color: white;
}

.btn-dispatcher:hover {
  background-color: #b91c1c;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(220, 38, 38, 0.4);
}

.legal-text {
  color: #6b7280;
  margin-top: 20px;
  font-size: 0.8rem;
  text-align: center;
  line-height: 1.5;
}

.legal-text a {
  color: #667eea;
  text-decoration: none;
}

.legal-text a:hover {
  text-decoration: underline;
}
</style>