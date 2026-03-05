<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const props = defineProps({
  onBack: Function
})

const router = useRouter()
const email = ref('')
const password = ref('')
const errorMessage = ref('')

const goBack = () => {
  if (typeof props.onBack === 'function') {
    props.onBack()
    return
  }

  router.push('/')
}

const handleSignIn = async () => {
  errorMessage.value = ''

  try {
    localStorage.removeItem('authToken')
    localStorage.removeItem('authRole')
    localStorage.removeItem('authFirstName')
    localStorage.removeItem('authLastName')

    const response = await axios.post(
      'http://127.0.0.1:8000/api/login/',
      {
        email: email.value,
        password: password.value
      }
    )

    const token = response.data?.token || response.data?.access || response.data?.access_token
    const role = response.data?.role_id ?? response.data?.role ?? response.data?.user?.role_id
    const firstName = response.data?.first_name || response.data?.user?.first_name || ''
    const lastName = response.data?.last_name || response.data?.user?.last_name || ''

    if (!token) {
      errorMessage.value = 'Login failed. No authentication token was returned.'
      return
    }

    if (String(role) !== '2') {
      errorMessage.value = 'Access denied. Responders only.'
      return
    }

    localStorage.setItem('authToken', token)
    localStorage.setItem('authRole', String(role))
    localStorage.setItem('authFirstName', firstName)
    localStorage.setItem('authLastName', lastName)
    axios.defaults.headers.common.Authorization = `Bearer ${token}`

    router.push('/DispatchDashboard')
  } catch (error) {
    if (error.response) {
      if (error.response.status === 400 || error.response.status === 401) {
        errorMessage.value = 'Invalid email or password.'
        return
      }

      if (error.response.data?.detail) {
        errorMessage.value = error.response.data.detail
        return
      }

      if (error.response.data?.error) {
        errorMessage.value = error.response.data.error
        return
      }

      errorMessage.value = 'Login failed. Please try again.'
    } else {
      errorMessage.value = 'Network error. Please check your connection and try again.'
    }
  }
}
</script>

<template>
  <div class="signin-container">
    <div class="signin-card">
      <button class="back-link" type="button" @click="goBack">← Back to Role Selection</button>
      
      <h1>Dispatcher Sign In</h1>
      
      <form @submit.prevent="handleSignIn">
        <input 
          type="email" 
          v-model="email"
          placeholder="Email" 
          class="input-field"
          required
        />
        <input 
          type="password" 
          v-model="password"
          placeholder="Password" 
          class="input-field"
          required
        />
        <button type="submit" class="btn btn-signin">Sign In</button>
      </form>

      <p v-if="errorMessage" class="error-text">{{ errorMessage }}</p>
      
      <p class="footer-text">
        By using this service, you understand and agree to the PULSE Online Services
        <a href="#">Terms of Use</a> and <a href="#">Privacy Statement</a>
      </p>
    </div>
  </div>
</template>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.signin-container {
  min-height: 100vh;
  background-image: url('@/assets/images/San_Juan_City_Hall.jpg');
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
}

.signin-card {
  background: white;
  border-radius: 12px;
  padding: 40px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
  max-width: 500px;
  width: 90%;
}

.back-link {
  background: none;
  border: none;
  color: #dc2626;
  cursor: pointer;
  font-size: 14px;
  margin-bottom: 20px;
  padding: 0;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s ease;
}

.back-link:hover {
  color: #b91c1c;
  text-decoration: underline;
}

h1 {
  color: #1f2937;
  font-size: 28px;
  margin-bottom: 30px;
  font-weight: 600;
  text-align: center;
}

form {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-bottom: 30px;
}

.input-field {
  padding: 12px 16px;
  border: 1px solid #e5e7eb;
  border-radius: 6px;
  font-size: 14px;
  font-family: inherit;
  transition: border-color 0.3s ease;
}

.input-field:focus {
  outline: none;
  border-color: #dc2626;
  box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.1);
}

.input-field::placeholder {
  color: #9ca3af;
}

.btn-signin {
  padding: 12px;
  background-color: #dc2626;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-top: 10px;
}

.btn-signin:hover {
  background-color: #b91c1c;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(220, 38, 38, 0.4);
}

.error-text {
  color: #dc2626;
  font-size: 14px;
  text-align: center;
  margin-bottom: 16px;
}

.footer-text {
  color: #9ca3af;
  font-size: 12px;
  text-align: center;
  line-height: 1.5;
}

.footer-text a {
  color: #dc2626;
  text-decoration: none;
}

.footer-text a:hover {
  text-decoration: underline;
}
</style>
