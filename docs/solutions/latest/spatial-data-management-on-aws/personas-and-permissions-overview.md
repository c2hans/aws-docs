---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/personas-and-permissions-overview.html
---

# Personas and Permissions Overview
<a name="personas-and-permissions-overview"></a>

Spatial Data Management on AWS uses resource-based access control to provide fine-grained permissions management. The solution does not define business personas as fixed roles in the system. Instead, it provides flexible permission levels (Owner, Manager, Contributor, and Viewer) that can be assigned to users on specific resources (libraries, projects, and assets). Projects also support a Consumer level for download-only access. This approach allows customers to grant appropriate permissions to users based on their actual responsibilities and needs, rather than predefined role assignments. The business personas described in this guide (IT Admin, Project Admin, Asset Creator, and Asset Consumer) represent common user types to help you understand how to apply permissions effectively in your organization.

## Business Personas
<a name="business-personas"></a>

These are the general business personas a typical customer will have.

### IT Admin
<a name="it-admin"></a>

Manages cloud infrastructure, security, and system integrations. Responsible for deployment, maintenance, and ensuring compliance with the organization’s IT policies.

 **Work Style** – Domain: Generalist; Cloud/Ops: Expert; Learning: Reader

 **Goals** – The IT Admin aims to establish a secure and scalable environment while seamlessly integrating Spatial Data Management on AWS into the organization’s existing technology stack. Their focus is on implementing robust governance policies and access controls to ensure smooth operations across multiple projects and teams.

 **Example Roles** – DevOps Engineers, System Administrators, Cloud Architects

### Project Admin
<a name="project-admin"></a>

Oversees project workflows, manages team access, and coordinates asset organization. Creates metadata schemas and defines processing pipelines for specific projects.

 **Work Style** – Domain: Specialist; Cloud/Ops: Learner; Learning: Doer

 **Goals** – The Project Admin strives to optimize team workflows by establishing standardized metadata schemas and configuring efficient processing pipelines. They actively monitor resource usage and team productivity to ensure project deliverables meet quality standards and timelines.

 **Example Roles** – BIM Managers, Project Coordinators, Asset Managers, Quality Assurance Leads

### Asset Creator
<a name="asset-creator"></a>

Creates, modifies, and processes three-dimensional (3D) assets and point cloud data. Includes both internal teams and external contractors who capture field data using scanning devices. Uses the solution daily for asset management, data upload, and file processing tasks.

 **Work Style** – Domain: Specialist (internal) or Mixed (contractors); Cloud/Ops: Learner to Novice; Learning: Doer

 **Goals** – Asset Creators focus on streamlining their daily workflows through efficient organization and processing of digital assets. For field teams, this extends to managing scanning projects and ensuring quality data capture. They need seamless collaboration capabilities to share work with team members and track project deliverables.

 **Example Roles** – Internal: 3D Artists, CAD Engineers, Point Cloud Specialists, Digital Twin Engineers. External: Scanning Service Providers, Drone Operators, Survey Teams, Reality Capture Specialists, Field Data Collection Teams

### Asset Consumer
<a name="asset-consumer"></a>

Uses processed assets in downstream applications and workflows. Interacts with the solution primarily through integrated applications or for asset retrieval. May include stakeholders who need to visualize or reference processed data without direct manipulation.

 **Work Style** – Domain: Generalist; Cloud/Ops: Novice; Learning: Reader or Visual

 **Goals** – Asset Consumers need quick access to finalized assets for their specific use cases, whether visualization, analysis, or integration into other applications. They require reliable ways to retrieve current versions of assets and monitor project status, often working through familiar tools and interfaces rather than directly with Spatial Data Management on AWS.

 **Example Roles** – Business Users: Project Managers, Facility Managers, Asset Integrity Managers, Plant Operations Supervisors. Technical Users: Digital Twin Engineers, Process Control Engineers, Simulation Engineers, Data Scientists. Field Users: Inspection Teams, Maintenance Crews, Field Operations Staff, Safety Inspectors, Equipment Operators

## Permission Model and Access Control
<a name="permission-model-and-access-control"></a>

Business personas map to resource based access with permission levels that govern access to features.

### Initial Admin Setup
<a name="initial-admin-setup"></a>

By default, the solution creates an Amazon Cognito group named `SpatialDataManagementAdministrators` with Owner access to all resources. This group enables IT Admins to designate an initial administrator user from the Cognito user pool or connected identity provider. This first admin can then assign permission levels to other users and groups within the application.

### User Access Initialization
<a name="user-access-initialization"></a>

Any user connected through a Cognito user group (who is not part of `SpatialDataManagementAdministrators`) starts with no permissions. An administrator in the `SpatialDataManagementAdministrators` group or another user with permission delegation rights must explicitly assign an access level before the user can organize and begin work.

### Permission Levels
<a name="permission-levels"></a>

Each resource supports permission levels – Owner, Manager, Contributor, and Viewer – that define what actions users can perform within the solution. Projects also support a Consumer level between Viewer and Contributor for download-only access.

The permission levels provide the following access:
+  **Owner** – Full access to all resources and actions, including access management on that resource and child resources
+  **Manager** – Can create, update, and manage access on the resource and child resources
+  **Contributor** – Can create and update the resource and child resources
+  **Consumer** (Projects only) – Can view and download file content, but cannot create or modify resources
+  **Viewer** – Can view resource metadata only. On Projects, cannot download file content
