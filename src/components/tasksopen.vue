<template>
  <div>
    <!-- Preloader -->
    <div id="preloader">
      <div class="spinner"></div>
    </div>

    <!-- Sidebar Navigation -->
    <aside class="sidebar-nav-wrapper">
      <div class="navbar-logo">
        <router-link
          to="/index"
          style="
            display: flex;
            align-items: center;
            gap: 10px;
            text-decoration: none;
          "
        >
          <img
            src="../images/PULSE OG.png"
            alt="logo"
            style="width: 45px; height: 45px; object-fit: contain"
          />
          <span style="font-size: 18px; font-weight: 600; color: #3b5998"
            >PULSE Admin</span
          >
        </router-link>
      </div>
      <nav class="sidebar-nav">
        <ul>
          <!-- ...existing code for sidebar links... -->
          <li class="nav-item active">
            <router-link to="/tasks">
              <span class="icon">
                <!-- ...existing code... -->
              </span>
              <span class="text">Tasks</span>
            </router-link>
          </li>
        </ul>
      </nav>
    </aside>
    <div class="overlay"></div>

    <!-- Main Wrapper -->
    <main class="main-wrapper">
      <!-- Header -->
      <header class="header">
        <!-- ...existing code for header... -->
      </header>

      <!-- Section -->
      <section class="section">
        <div class="container-fluid">
          <div class="title-wrapper pt-30">
            <div class="row align-items-center">
              <div class="col-md-6">
                <div class="title">
                  <h2>Overview</h2>
                </div>
              </div>
              <div class="col-md-6">
                <div class="breadcrumb-wrapper">
                  <nav aria-label="breadcrumb">
                    <ol class="breadcrumb">
                      <li class="breadcrumb-item">
                        <router-link to="/index">Dashboard</router-link>
                      </li>
                      <li class="breadcrumb-item">
                        <router-link to="/tasks">Tasks</router-link>
                      </li>
                      <li class="breadcrumb-item active" aria-current="page">
                        Details
                      </li>
                    </ol>
                  </nav>
                </div>
              </div>
            </div>
          </div>

          <!-- Back Button -->
          <router-link to="/tasks" class="btn btn-back mb-20">
            <i class="lni lni-arrow-left"></i> Back to Tasks
          </router-link>

          <!-- Details Card -->
          <div class="details-card">
            <h2 class="details-title">DETAILS</h2>
            <div class="details-info">
              <div class="details-info-item">
                REQUEST NO: <span>{{ task.requestNo }}</span>
              </div>
              <div class="details-info-item">
                REQUESTED BY: <span>{{ task.requestedBy }}</span>
              </div>
              <div class="details-info-item">
                DATE & TIME REQUESTED: <span>{{ task.dateTime }}</span>
              </div>
              <div class="details-info-item">
                REQUEST TYPE: <span>{{ task.requestType }}</span>
              </div>
            </div>
            <h3 class="description-title">DESCRIPTION</h3>
            <div class="description-box">
              <p>{{ task.description }}</p>
            </div>
            <div class="row align-items-center">
              <div class="col-md-6">
                <div class="status-section">
                  <label>STATUS:</label>
                  <select class="status-select" v-model="task.status">
                    <option value="">SELECT</option>
                    <option value="pending">Pending</option>
                    <option value="in-progress">In Progress</option>
                    <option value="completed">Completed</option>
                    <option value="cancelled">Cancelled</option>
                  </select>
                </div>
              </div>
              <div class="col-md-6 text-end">
                <button class="btn-resolve" @click="resolveTask">
                  RESOLVE
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Footer -->
      <footer class="footer">
        <!-- ...existing code for footer... -->
      </footer>
    </main>
  </div>
</template>

<script>
export default {
  name: "tasksopen",
  data() {
    return {
      task: {
        requestNo: "###",
        requestedBy: "###",
        dateTime: "###",
        requestType: "###",
        description: "PEDE PO MAGPAPALIT NG ###?",
        status: "",
      },
    };
  },
  methods: {
    resolveTask() {
      alert("Task resolved!");
      this.task.status = "completed";
    },
  },
};
</script>

<style scoped>
.details-card {
  background: white;
  border-radius: 15px;
  padding: 30px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}
.details-title {
  color: #3b5998;
  font-size: 28px;
  font-weight: 700;
  margin-bottom: 20px;
  letter-spacing: 1px;
}
.details-info {
  display: flex;
  flex-wrap: wrap;
  gap: 30px;
  margin-bottom: 25px;
  padding-bottom: 15px;
  border-bottom: 1px solid #eee;
}
.details-info-item {
  font-size: 13px;
  color: #666;
}
.details-info-item span {
  color: #3b5998;
  font-weight: 600;
}
.description-title {
  color: #3b5998;
  font-size: 22px;
  font-weight: 600;
  margin-bottom: 15px;
}
.description-box {
  background: #f5f5f5;
  border-radius: 10px;
  padding: 25px;
  min-height: 200px;
  margin-bottom: 25px;
}
.description-box p {
  color: #333;
  font-size: 15px;
  line-height: 1.6;
  margin: 0;
}
.status-section {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 20px;
}
.status-section label {
  font-weight: 600;
  font-size: 14px;
  color: #333;
}
.status-select {
  padding: 8px 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 14px;
  min-width: 150px;
}
.btn-resolve {
  background: #3b5998;
  color: white;
  border: none;
  padding: 10px 30px;
  border-radius: 5px;
  font-size: 14px;
  font-weight: 600;
  float: right;
}
.btn-resolve:hover {
  background: #2d4373;
  color: white;
}
.btn-back {
  background: #6c757d;
  color: white;
  border: none;
  padding: 8px 20px;
  border-radius: 5px;
  font-size: 13px;
  margin-bottom: 20px;
}
.btn-back:hover {
  background: #5a6268;
  color: white;
}
</style>
