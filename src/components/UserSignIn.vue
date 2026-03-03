<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const props = defineProps({
  onBack: Function
})

const emit = defineEmits(['signin-success'])
const router = useRouter()

const rememberMe = ref(false)
const showSignUp = ref(false)

// Signup form fields
const firstName = ref('')
const lastName = ref('')
const phone = ref('')
const email = ref('')
const password = ref('')
const confirmPassword = ref('')

const goBack = () => {
  if (typeof props.onBack === 'function') {
    props.onBack()
    return
  }

  router.push('/')
}

const handleSignIn = () => {
  console.log('User sign in', { rememberMe: rememberMe.value })
  emit('signin-success')
}

const handleSignUp = async () => {
  if (password.value !== confirmPassword.value) {
    alert("Passwords do not match")
    return
  }

  try {
    const response = await axios.post(
      "http://127.0.0.1:8000/api/signup/",
      {
        first_name: firstName.value,
        last_name: lastName.value,
        phone_number: phone.value,
        email: email.value,
        password: password.value,
        role: 3
      }
    )

    alert(response.data.message)
    showSignUp.value = false

  } catch (error) {
    if (error.response && error.response.data) {
      alert(JSON.stringify(error.response.data))
    } else {
      alert("Signup failed")
    }
  }
}
</script>

<template>
  <div class="signin-container">
    <div class="signin-card">
      <button class="back-link" type="button" @click="goBack">← Back to Role Selection</button>
      
      <h1>User Sign In</h1>
      
      <form @submit.prevent="handleSignIn">
        <input 
          type="text" 
          placeholder="Username or Email" 
          class="input-field"
          required
        />
        <input 
          type="password" 
          placeholder="Password" 
          class="input-field"
          required
        />
        
        <div class="remember-me">
          <input 
            type="checkbox" 
            id="remember" 
            v-model="rememberMe"
            class="checkbox"
          />
          <label for="remember">Remember me</label>
        </div>
        
        <button type="submit" class="btn btn-signin">Sign In</button>
      </form>
      
      <div class="divider">or</div>
      
      <button class="btn btn-signup" @click="() => showSignUp = true">Create Account</button>
      
      <div class="links">
        <button class="forgot-password" @click="handleForgotPassword">Forgot Password?</button>
      </div>
      
      <p class="footer-text">
        By using this service, you understand and agree to the PULSE Online Services
        <a href="#">Terms of Use</a> and <a href="#">Privacy Statement</a>
      </p>
    </div>
    
    <!-- Signup Modal -->
    <div v-if="showSignUp" class="modal-overlay" @click="showSignUp = false">
      <div class="modal-card" @click.stop>
        <button class="close-btn" @click="showSignUp = false">×</button>
        <h2>Create Account</h2>
        
       <form @submit.prevent="handleSignUp">
  <div class="name-row">
    <input type="text" v-model="firstName" placeholder="First Name" class="input-field" required />
    <input type="text" v-model="lastName" placeholder="Last Name" class="input-field" required />
  </div>

  <input type="tel" v-model="phone" placeholder="Phone Number" class="input-field" required />
  <input type="email" v-model="email" placeholder="Email" class="input-field" required />
  <input type="password" v-model="password" placeholder="Password" class="input-field" required />
  <input type="password" v-model="confirmPassword" placeholder="Confirm Password" class="input-field" required />

  <button type="submit" class="btn btn-signin">Sign Up</button>
</form>
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
  color: #2563eb;
  cursor: pointer;
  font-size: 14px;
  margin-bottom: 20px;
  padding: 0;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s ease;
}

.back-link:hover {
  color: #1d4ed8;
  text-decoration: underline;
}

h1 {
  color: #1f2937;
  font-size: 28px;
  margin-bottom: 30px;
  font-weight: 600;
  text-align: center;
}

h2 {
  color: #1f2937;
  font-size: 24px;
  margin-bottom: 20px;
  font-weight: 600;
  text-align: center;
}

form {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-bottom: 20px;
}

.name-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
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
  border-color: #2563eb;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.input-field::placeholder {
  color: #9ca3af;
}

.remember-me {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 8px 0;
}

.checkbox {
  width: 18px;
  height: 18px;
  cursor: pointer;
  accent-color: #2563eb;
}

.remember-me label {
  cursor: pointer;
  font-size: 14px;
  color: #6b7280;
}

.btn {
  padding: 12px;
  border: none;
  border-radius: 6px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-signin {
  background-color: #2563eb;
  color: white;
  margin-top: 10px;
}

.btn-signin:hover {
  background-color: #1d4ed8;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.4);
}

.btn-signup {
  background-color: #10b981;
  color: white;
  width: 100%;
  margin-bottom: 10px;
}

.btn-signup:hover {
  background-color: #059669;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.4);
}

.divider {
  text-align: center;
  color: #9ca3af;
  margin: 20px 0;
  font-size: 14px;
}

.links {
  text-align: center;
  margin-bottom: 20px;
}

.forgot-password {
  background: none;
  border: none;
  color: #2563eb;
  cursor: pointer;
  font-size: 14px;
  text-decoration: none;
  font-weight: 500;
  padding: 0;
  transition: color 0.3s ease;
}

.forgot-password:hover {
  color: #1d4ed8;
  text-decoration: underline;
}

.footer-text {
  color: #9ca3af;
  font-size: 12px;
  text-align: center;
  line-height: 1.5;
}

.footer-text a {
  color: #2563eb;
  text-decoration: none;
}

.footer-text a:hover {
  text-decoration: underline;
}

/* Modal styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-card {
  background: white;
  border-radius: 12px;
  padding: 40px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  max-width: 500px;
  width: 90%;
  position: relative;
}

.close-btn {
  position: absolute;
  top: 15px;
  right: 15px;
  background: none;
  border: none;
  font-size: 32px;
  color: #9ca3af;
  cursor: pointer;
  transition: color 0.3s ease;
  padding: 0;
  width: 30px;
  height: 30px;
}

.close-btn:hover {
  color: #1f2937;
}
</style>
