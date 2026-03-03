<template>
  <div>
    <!-- Preloader -->
    <div id="preloader">
      <div class="spinner"></div>
    </div>

    <!-- Sidebar Navigation -->
    <aside class="sidebar-nav-wrapper">
      <div class="navbar-logo">
        <router-link to="/admin">
          <img src="../images/PULSE OG.png" alt="logo" style="width: 45px; height: 45px; object-fit: contain;" />
          <span style="font-size: 18px; font-weight: 600; color: #3b5998;">PULSE Admin</span>
        </router-link>
      </div>
      <nav class="sidebar-nav">
        <ul>
          <li class="nav-item">
            <router-link to="/admin" class="nav-link">
              <span class="icon">
                <!-- Dashboard SVG -->
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M8.74999 18.3333C12.2376 18.3333 15.1364 15.8128 15.7244 12.4941C15.8448 11.8143 15.2737 11.25 14.5833 11.25H9.99999C9.30966 11.25 8.74999 10.6903 8.74999 10V5.41666C8.74999 4.7263 8.18563 4.15512 7.50586 4.27556C4.18711 4.86357 1.66666 7.76243 1.66666 11.25C1.66666 15.162 4.83797 18.3333 8.74999 18.3333Z" />
                  <path d="M17.0833 10C17.7737 10 18.3432 9.43708 18.2408 8.75433C17.7005 5.14918 14.8508 2.29947 11.2457 1.75912C10.5629 1.6568 10 2.2263 10 2.91665V9.16666C10 9.62691 10.3731 10 10.8333 10H17.0833Z" />
                </svg>
              </span>
              <span class="text">Dashboard</span>
            </router-link>
          </li>
          <!-- ...existing sidebar items, replace <a> with <router-link> as needed... -->
        </ul>
      </nav>
    </aside>
    <div class="overlay"></div>

    <!-- Main Wrapper -->
    <main class="main-wrapper">
      <!-- Header -->
      <header class="header">
        <!-- ...existing header code... -->
      </header>

      <!-- Form Elements Section -->
      <section class="tab-components">
        <div class="container-fluid">
          <div class="title-wrapper pt-30">
            <div class="row align-items-center">
              <div class="col-md-6">
                <div class="title">
                  <h2>Form Elements</h2>
                </div>
              </div>
              <div class="col-md-6">
                <div class="breadcrumb-wrapper">
                  <nav aria-label="breadcrumb">
                    <ol class="breadcrumb">
                      <li class="breadcrumb-item">
                        <router-link to="/admin">Dashboard</router-link>
                      </li>
                      <li class="breadcrumb-item">
                        <router-link to="#">Forms</router-link>
                      </li>
                      <li class="breadcrumb-item active" aria-current="page">
                        Form Elements
                      </li>
                    </ol>
                  </nav>
                </div>
              </div>
            </div>
          </div>

          <!-- Form Elements Wrapper -->
          <div class="form-elements-wrapper">
            <div class="row">
              <div class="col-lg-6">
                <!-- Input Fields -->
                <div class="card-style mb-30">
                  <h6 class="mb-25">Input Fields</h6>
                  <div class="input-style-1">
                    <label>Full Name</label>
                    <input type="text" placeholder="Full Name" />
                  </div>
                  <div class="input-style-2">
                    <input type="text" placeholder="Full Name" />
                    <span class="icon"> <i class="lni lni-user"></i> </span>
                  </div>
                  <div class="input-style-3">
                    <input type="text" placeholder="Full Name" />
                    <span class="icon"><i class="lni lni-user"></i></span>
                  </div>
                </div>

                <!-- Selects -->
                <div class="card-style mb-30">
                  <h6 class="mb-25">Selects</h6>
                  <div class="select-style-1">
                    <label>Category</label>
                    <div class="select-position">
                      <select>
                        <option value="">Select category</option>
                        <option value="">Category one</option>
                        <option value="">Category two</option>
                        <option value="">Category three</option>
                      </select>
                    </div>
                  </div>
                  <div class="select-style-2">
                    <div class="select-position">
                      <select>
                        <option value="">Select category</option>
                        <option value="">Category one</option>
                        <option value="">Category two</option>
                        <option value="">Category three</option>
                      </select>
                    </div>
                  </div>
                </div>

                <!-- Time and Date -->
                <div class="card-style mb-30">
                  <h6 class="mb-25">Time and Date</h6>
                  <div class="input-style-1">
                    <label>Date</label>
                    <input type="date" />
                  </div>
                  <div class="input-style-2">
                    <input type="date" />
                    <span class="icon"><i class="lni lni-chevron-down"></i></span>
                  </div>
                  <div class="input-style-2">
                    <input type="time" />
                  </div>
                </div>

                <!-- Toggle Switch Input -->
                <div class="card-style mb-30">
                  <h6 class="mb-25">Toggle switch input</h6>
                  <div class="form-check form-switch toggle-switch mb-30">
                    <input class="form-check-input" type="checkbox" id="toggleSwitch1" />
                    <label class="form-check-label" for="toggleSwitch1">Default switch checkbox input</label>
                  </div>
                  <div class="form-check form-switch toggle-switch">
                    <input class="form-check-input" type="checkbox" id="toggleSwitch2" checked />
                    <label class="form-check-label" for="toggleSwitch2">Default switch checkbox input</label>
                  </div>
                </div>
              </div>
              <div class="col-lg-6">
                <!-- Textarea -->
                <div class="card-style mb-30">
                  <h6 class="mb-25">Textarea</h6>
                  <div class="input-style-1">
                    <label>Message</label>
                    <textarea placeholder="Message" rows="5"></textarea>
                  </div>
                  <div class="input-style-3">
                    <textarea placeholder="Message" rows="5"></textarea>
                    <span class="icon"><i class="lni lni-text-format"></i></span>
                  </div>
                </div>

                <!-- Checkbox -->
                <div class="card-style mb-30">
                  <h6 class="mb-25">Checkbox</h6>
                  <div class="form-check checkbox-style mb-20">
                    <input class="form-check-input" type="checkbox" value="" id="checkbox-1" />
                    <label class="form-check-label" for="checkbox-1">Default Checkbox</label>
                  </div>
                  <div class="form-check checkbox-style mb-20">
                    <input class="form-check-input" type="checkbox" value="" id="checkbox-2" disabled />
                    <label class="form-check-label" for="checkbox-2">Disabled Checkbox</label>
                  </div>
                  <div class="form-check checkbox-style checkbox-success mb-20">
                    <input class="form-check-input" type="checkbox" value="" id="checkbox-3" />
                    <label class="form-check-label" for="checkbox-3">Success Checkbox</label>
                  </div>
                  <div class="form-check checkbox-style checkbox-warning mb-20">
                    <input class="form-check-input" type="checkbox" value="" id="checkbox-4" />
                    <label class="form-check-label" for="checkbox-4">Warning Checkbox</label>
                  </div>
                  <div class="form-check checkbox-style checkbox-danger mb-20">
                    <input class="form-check-input" type="checkbox" value="" id="checkbox-5" />
                    <label class="form-check-label" for="checkbox-5">Danger Checkbox</label>
                  </div>
                </div>

                <!-- Radio -->
                <div class="card-style mb-30">
                  <h6 class="mb-25">Radio</h6>
                  <div class="form-check radio-style mb-20">
                    <input class="form-check-input" type="radio" value="" id="radio-1" />
                    <label class="form-check-label" for="radio-1">Default Radio</label>
                  </div>
                  <div class="form-check radio-style mb-20">
                    <input class="form-check-input" type="radio" value="" id="radio-2" disabled />
                    <label class="form-check-label" for="radio-2">Disabled Radio</label>
                  </div>
                  <div class="form-check radio-style radio-success mb-20">
                    <input class="form-check-input" type="radio" value="" id="radio-3" />
                    <label class="form-check-label" for="radio-3">Success Radio</label>
                  </div>
                  <div class="form-check radio-style radio-warning mb-20">
                    <input class="form-check-input" type="radio" value="" id="radio-4" />
                    <label class="form-check-label" for="radio-4">Warning Radio</label>
                  </div>
                  <div class="form-check radio-style radio-danger mb-20">
                    <input class="form-check-input" type="radio" value="" id="radio-5" />
                    <label class="form-check-label" for="radio-5">Danger Radio</label>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Footer -->
      <footer class="footer">
        <!-- ...existing footer code... -->
      </footer>
    </main>
  </div>
</template>

<script>
export default {
  name: "FormElements",
};
</script>

<style scoped>
@import "assets/css/bootstrap.min.css";
@import "assets/css/lineicons.css";
@import "assets/css/materialdesignicons.min.css";
@import "assets/css/fullcalendar.css";
@import "assets/css/main.css";
</style>
