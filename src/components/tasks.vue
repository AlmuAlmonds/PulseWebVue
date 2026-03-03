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
                  <h2>CEDOC Operations Task Panel</h2>
                  <p style="color: #666; margin-top: 5px; font-size: 14px">
                    Real-time emergency incident management and responder
                    coordination for San Juan CEDOC
                  </p>
                </div>
              </div>
              <div class="col-md-6">
                <div class="breadcrumb-wrapper">
                  <nav aria-label="breadcrumb">
                    <ol class="breadcrumb">
                      <li class="breadcrumb-item">
                        <router-link to="/index">Dashboard</router-link>
                      </li>
                      <li class="breadcrumb-item active" aria-current="page">
                        Operations Tasks
                      </li>
                    </ol>
                  </nav>
                </div>
              </div>
            </div>
          </div>

          <!-- Filter Buttons -->
          <div class="filter-buttons">
            <button
              v-for="filter in filters"
              :key="filter.type"
              :class="[
                'status-badge',
                filter.type,
                { active: activeFilter === filter.type },
              ]"
              @click="setActiveFilter(filter.type)"
            >
              <i :class="filter.icon"></i> {{ filter.label }}
            </button>
          </div>

          <!-- Incident Cards Summary -->
          <div class="row mb-30">
            <div
              class="col-xl-3 col-lg-4 col-sm-6"
              v-for="summary in summaries"
              :key="summary.type"
            >
              <div class="icon-card mb-30">
                <div class="icon" :style="summary.iconStyle">
                  <i :class="summary.icon"></i>
                </div>
                <div class="content">
                  <h6 class="mb-10">{{ summary.label }}</h6>
                  <h3 class="text-bold mb-10">{{ summary.count }}</h3>
                  <p class="text-sm" :style="summary.textStyle">
                    <i :class="summary.trendIcon"></i> {{ summary.trendText }}
                    <span class="text-gray">{{ summary.trendSub }}</span>
                  </p>
                </div>
              </div>
            </div>
          </div>

          <!-- Emergency Incidents Table -->
          <div class="card-style mb-30">
            <div
              class="title d-flex flex-wrap justify-content-between align-items-center mb-20"
            >
              <h6 class="text-medium task-table-title">{{ tableTitle }}</h6>
              <button class="btn btn-sm btn-primary" @click="reportIncident">
                <i class="lni lni-plus"></i> Report Incident
              </button>
            </div>
            <div class="table-responsive">
              <table class="table">
                <thead>
                  <tr>
                    <th>Incident ID</th>
                    <th>Report Type</th>
                    <th>Reporter</th>
                    <th>Location</th>
                    <th>Priority</th>
                    <th>Assigned Responder</th>
                    <th>Status</th>
                    <th>Time Reported</th>
                    <th>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    v-for="incident in filteredIncidents"
                    :key="incident.id"
                    :class="incident.priorityClass"
                  >
                    <td>
                      <strong>{{ incident.id }}</strong>
                    </td>
                    <td>
                      <span class="type-badge">{{ incident.type }}</span>
                    </td>
                    <td>{{ incident.reporter }}</td>
                    <td>{{ incident.location }}</td>
                    <td>
                      <span :class="incident.priorityBadgeClass">{{
                        incident.priorityLabel
                      }}</span>
                    </td>
                    <td>{{ incident.responder }}</td>
                    <td>
                      <span
                        :class="['status-badge-inline', incident.statusClass]"
                        >{{ incident.statusIcon }}
                        {{ incident.statusLabel }}</span
                      >
                    </td>
                    <td>{{ incident.time }}</td>
                    <td>
                      <button
                        class="btn btn-sm btn-info"
                        @click="viewDetails(incident)"
                      >
                        <i class="lni lni-eye"></i>
                      </button>
                      <button
                        v-if="incident.status !== 'resolved'"
                        class="btn btn-sm btn-warning"
                        @click="assignResponder(incident)"
                      >
                        <i class="lni lni-user-1"></i>
                      </button>
                      <button
                        v-if="
                          incident.status === 'pending' ||
                          incident.status === 'inprogress' ||
                          incident.status === 'escalated'
                        "
                        class="btn btn-sm btn-danger"
                        @click="escalateIncident(incident)"
                      >
                        ⚠️
                      </button>
                      <button
                        v-if="incident.status === 'resolved'"
                        class="btn btn-sm btn-secondary"
                        @click="closeCase(incident)"
                      >
                        <i class="lni lni-check"></i>
                      </button>
                      <button
                        v-if="incident.status === 'resolved'"
                        class="btn btn-sm btn-secondary"
                        @click="noFurtherAction(incident)"
                      >
                        ✓
                      </button>
                      <button
                        v-if="incident.status === 'escalated'"
                        class="btn btn-sm btn-danger"
                        @click="multiAgencyCoordination(incident)"
                      >
                        🚨
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
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
  name: "tasks",
  data() {
    return {
      activeFilter: "pending",
      filters: [
        { type: "pending", label: "Pending Incidents", icon: "lni lni-timer" },
        {
          type: "inprogress",
          label: "Active Responses",
          icon: "lni lni-spinner-arrow",
        },
        {
          type: "resolved",
          label: "Resolved",
          icon: "lni lni-checkmark-circle",
        },
        {
          type: "escalated",
          label: "Escalated/Critical",
          icon: "lni lni-warning",
        },
      ],
      incidents: [
        {
          id: "INC-2026-001",
          type: "🚒 Fire",
          reporter: "Maria Santos",
          location: "Pinaglabanan St., San Juan",
          priority: "critical",
          priorityLabel: "Critical",
          priorityClass: "priority-critical",
          priorityBadgeClass: "priority-critical-badge",
          responder: "Responder Unit 01 (BFP)",
          status: "pending",
          statusLabel: "Pending",
          statusClass: "status-pending",
          statusIcon: "⏳",
          time: "02:15 PM",
        },
        {
          id: "INC-2026-002",
          type: "🚑 Medical",
          reporter: "John Reyes",
          location: "North Avenue, San Juan",
          priority: "high",
          priorityLabel: "High",
          priorityClass: "priority-high",
          priorityBadgeClass: "priority-high-badge",
          responder: "Responder Unit 05 (PNP-ACG)",
          status: "inprogress",
          statusLabel: "In Progress",
          statusClass: "status-inprogress",
          statusIcon: "🔄",
          time: "02:05 PM",
        },
        {
          id: "INC-2026-003",
          type: "⚠️ Disaster",
          reporter: "Anonymous Caller",
          location: "Canlubang Area, San Juan",
          priority: "high",
          priorityLabel: "High",
          priorityClass: "priority-high",
          priorityBadgeClass: "priority-high-badge",
          responder: "Responder Unit 02 & 03 (CDRRMO)",
          status: "inprogress",
          statusLabel: "In Progress",
          statusClass: "status-inprogress",
          statusIcon: "🔄",
          time: "01:45 PM",
        },
        {
          id: "INC-2026-004",
          type: "👮 Crime",
          reporter: "Witness (Confidential)",
          location: "Sta. Lucia Ave., San Juan",
          priority: "medium",
          priorityLabel: "Medium",
          priorityClass: "priority-medium",
          priorityBadgeClass: "priority-medium-badge",
          responder: "Responder Unit 07 (PNP)",
          status: "inprogress",
          statusLabel: "In Progress",
          statusClass: "status-inprogress",
          statusIcon: "🔄",
          time: "01:30 PM",
        },
        {
          id: "INC-2026-005",
          type: "🚗 Traffic",
          reporter: "CCTV Monitoring",
          location: "McArthur Highway, San Juan",
          priority: "low",
          priorityLabel: "Low",
          priorityClass: "priority-low",
          priorityBadgeClass: "priority-low-badge",
          responder: "Responder Unit 06 (Traffic)",
          status: "inprogress",
          statusLabel: "In Progress",
          statusClass: "status-inprogress",
          statusIcon: "🔄",
          time: "01:15 PM",
        },
        {
          id: "INC-2026-006",
          type: "🚑 Medical",
          reporter: "Concerned Citizen",
          location: "Commonwealth Ave., San Juan",
          priority: "medium",
          priorityLabel: "Medium",
          priorityClass: "priority-medium",
          priorityBadgeClass: "priority-medium-badge",
          responder: "Responder Unit 04 (RHU)",
          status: "resolved",
          statusLabel: "Resolved",
          statusClass: "status-resolved",
          statusIcon: "✓",
          time: "12:45 PM",
        },
        {
          id: "INC-2026-007",
          type: "⚠️ Welfare Check",
          reporter: "Barangay Official",
          location: "Amparo St., San Juan",
          priority: "low",
          priorityLabel: "Low",
          priorityClass: "priority-low",
          priorityBadgeClass: "priority-low-badge",
          responder: "Responder Unit 08 (Barangay)",
          status: "resolved",
          statusLabel: "Resolved",
          statusClass: "status-resolved",
          statusIcon: "✓",
          time: "11:30 AM",
        },
        {
          id: "INC-2026-008",
          type: "🚨 Disaster",
          reporter: "Emergency Hotline",
          location: "Bagong Komunidad, San Juan",
          priority: "critical",
          priorityLabel: "Critical",
          priorityClass: "priority-critical",
          priorityBadgeClass: "priority-critical-badge",
          responder: "Multi-agency Response (Escalated)",
          status: "escalated",
          statusLabel: "Escalated",
          statusClass: "status-escalated",
          statusIcon: "⚠️",
          time: "11:00 AM",
        },
      ],
    };
  },
  computed: {
    filteredIncidents() {
      return this.incidents.filter((i) => i.status === this.activeFilter);
    },
    tableTitle() {
      const statusCounts = {
        pending: this.incidents.filter((i) => i.status === "pending").length,
        inprogress: this.incidents.filter((i) => i.status === "inprogress")
          .length,
        resolved: this.incidents.filter((i) => i.status === "resolved").length,
        escalated: this.incidents.filter((i) => i.status === "escalated")
          .length,
      };
      if (this.activeFilter === "pending")
        return `PENDING INCIDENTS (${statusCounts.pending})`;
      if (this.activeFilter === "inprogress")
        return `ACTIVE RESPONSES (${statusCounts.inprogress})`;
      if (this.activeFilter === "resolved")
        return `RESOLVED INCIDENTS (${statusCounts.resolved})`;
      if (this.activeFilter === "escalated")
        return `ESCALATED/CRITICAL INCIDENTS (${statusCounts.escalated})`;
      return "ACTIVE INCIDENTS & RESPONSES";
    },
    summaries() {
      // For summary cards
      return [
        {
          type: "pending",
          label: "Pending Incidents",
          icon: "lni lni-timer",
          iconStyle: { background: "#ffc10720", color: "#ffc107" },
          count: this.incidents.filter((i) => i.status === "pending").length,
          trendIcon: "lni lni-arrow-up",
          trendText: "+2",
          trendSub: "last hour",
          textStyle: { color: "#ffc107" },
        },
        {
          type: "inprogress",
          label: "Active Responses",
          icon: "lni lni-spinner-arrow",
          iconStyle: { background: "#0dcaf020", color: "#0dcaf0" },
          count: this.incidents.filter((i) => i.status === "inprogress").length,
          trendIcon: "lni lni-pulse",
          trendText: "In Action",
          trendSub: "",
          textStyle: { color: "#0dcaf0" },
        },
        {
          type: "resolved",
          label: "Resolved Incidents",
          icon: "lni lni-checkmark-circle",
          iconStyle: { background: "#19875420", color: "#198754" },
          count: this.incidents.filter((i) => i.status === "resolved").length,
          trendIcon: "lni lni-arrow-up",
          trendText: "+18",
          trendSub: "this week",
          textStyle: { color: "#198754" },
        },
        {
          type: "escalated",
          label: "Escalated/Critical",
          icon: "lni lni-warning",
          iconStyle: { background: "#dc354520", color: "#dc3545" },
          count: this.incidents.filter((i) => i.status === "escalated").length,
          trendIcon: "lni lni-alert",
          trendText: "Requires Attention",
          trendSub: "",
          textStyle: { color: "#dc3545" },
        },
      ];
    },
  },
  methods: {
    setActiveFilter(type) {
      this.activeFilter = type;
    },
    reportIncident() {
      alert("Quick reporting feature: Submit new incident to CEDOC system");
    },
    viewDetails(incident) {
      alert(`View Details: ${incident.type} at ${incident.location}`);
    },
    assignResponder(incident) {
      alert("Assign backup responder or notify team");
    },
    escalateIncident(incident) {
      alert("Escalation authorized to backup units or emergency operations");
    },
    closeCase(incident) {
      alert("Case closed");
    },
    noFurtherAction(incident) {
      alert("No further action needed");
    },
    multiAgencyCoordination(incident) {
      alert("Multi-agency coordination initiated");
    },
  },
};
</script>

<style scoped>
.status-badge {
  padding: 6px 16px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
}
.status-badge.pending {
  background: #ffc10720;
  color: #ffc107;
  border: 2px solid #ffc107;
}
.status-badge.pending.active {
  background: #ffc107;
  color: white;
  border: 2px solid #ffc107;
}
.status-badge.active {
  background: #0dcaf020;
  color: #0dcaf0;
  border: 2px solid #0dcaf0;
}
.status-badge.active.active {
  background: #0dcaf0;
  color: white;
  border: 2px solid #0dcaf0;
}
.status-badge.resolved {
  background: #19875420;
  color: #198754;
  border: 2px solid #198754;
}
.status-badge.resolved.active {
  background: #198754;
  color: white;
  border: 2px solid #198754;
}
.status-badge.escalated {
  background: #dc354520;
  color: #dc3545;
  border: 2px solid #dc3545;
}
.status-badge.escalated.active {
  background: #dc3545;
  color: white;
  border: 2px solid #dc3545;
}
.filter-buttons {
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
  margin-bottom: 25px;
}
.task-table {
  background: white;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}
.task-table table {
  margin-bottom: 0;
}
.task-table th {
  background: #f8f9fa;
  font-weight: 600;
  font-size: 13px;
  color: #666;
  text-transform: uppercase;
  padding: 15px 20px;
  border: none;
}
.task-table td {
  padding: 15px 20px;
  vertical-align: middle;
  border-bottom: 1px solid #f0f0f0;
}
.task-table tr:last-child td {
  border-bottom: none;
}
.btn-open {
  background: #3b5998;
  color: white;
  border: none;
  padding: 6px 20px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  text-decoration: none;
  display: inline-block;
}
.btn-open:hover {
  background: #2d4373;
  color: white;
}
.type-badge {
  background: #e9ecef;
  color: #495057;
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 12px;
}
.priority-critical {
  background-color: #ffebee;
  border-left: 4px solid #dc3545;
}
.priority-high {
  background-color: #fff3e0;
  border-left: 4px solid #fd7e14;
}
.priority-medium {
  background-color: #fffbea;
  border-left: 4px solid #ffc107;
}
.priority-low {
  background-color: #e3f2fd;
  border-left: 4px solid #0dcaf0;
}
.priority-critical-badge,
.priority-high-badge,
.priority-medium-badge,
.priority-low-badge {
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 600;
}
.priority-critical-badge {
  background: #dc3545;
  color: white;
}
.priority-high-badge {
  background: #fd7e14;
  color: white;
}
.priority-medium-badge {
  background: #ffc107;
  color: #333;
}
.priority-low-badge {
  background: #0dcaf0;
  color: white;
}
.status-badge-inline {
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}
.status-pending {
  background: #ffc10720;
  color: #ffc107;
}
.status-inprogress {
  background: #0dcaf020;
  color: #0dcaf0;
}
.status-resolved {
  background: #19875420;
  color: #198754;
}
.status-escalated {
  background: #dc354520;
  color: #dc3545;
}
</style>
