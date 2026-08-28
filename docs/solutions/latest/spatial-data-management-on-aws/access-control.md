---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/access-control.html
---

# Access Management
<a name="access-control"></a>

## Overview
<a name="overview"></a>

Spatial Data Management on AWS (SDMA) uses resource-based access control to provide fine-grained permissions management. This means permissions are assigned on specific resources (Libraries, Projects, Asset Templates, and Connectors) rather than globally across the entire system.

### Key Concepts
<a name="_key-concepts"></a>
+  **Resource-based permissions** – Each resource has its own set of members with specific permission levels
+  **Permission inheritance** – Library-level permissions can grant access to child resources (Projects, Asset Templates, Connectors)
+  **User and group access** – Permissions can be assigned to individual users or to groups of users
+  **Permission levels** – Owner, Manager, Contributor, and Viewer provide different levels of access across all resource types. Projects also support a Consumer level for download-only access
+  **Access Management tab** – Resources with permissions have an Access Management tab where you can add or remove members (individual users or groups)

## Permission Levels
<a name="permission-levels"></a>

Each resource supports permission levels that define what actions you can perform. Libraries, Asset Templates, and Connectors support four levels: Owner, Manager, Contributor, and Viewer. Projects support an additional Consumer level between Viewer and Contributor that grants file download access without write permissions. The Spatial Data Portal shows or hides UI elements based on your permission level.

### Permission Level Summary
<a name="permission-level-summary"></a>

The following table provides a high-level overview of the permission levels and their relative capabilities. These capabilities apply across all resource types (Libraries, Projects, Asset Templates, and Connectors), though specific actions vary by resource. The Consumer level is available on Projects only.

**Permission Level Capabilities**

| Capability | Owner | Manager | Contributor | Viewer |
| --- | --- | --- | --- | --- |
| View resource details | ✓ | ✓ | ✓ | ✓ |
| Create child resources (Projects, Assets, etc.) | ✓ | ✓ | ✓ |  |
| Update resource details | ✓ | ✓ | ✓ |  |
| Delete resource | ✓ |  |  |  |
| Add members at any level | ✓ |  |  |  |
| Add Contributors or Viewers | ✓ | ✓ |  |  |
| Remove members at any level | ✓ |  |  |  |
| Remove Contributors or Viewers | ✓ | ✓ |  |  |
| View all members | ✓ | ✓ | ✓ |  |

### Permission level details
<a name="permission-level-summary-details"></a>

#### Owner
<a name="owner"></a>
+ Full control over the resource and all its child resources
+ Can add or remove members at any permission level
+ Can delete the resource (except Libraries, which cannot be deleted)
+ Has access to all administrative features in the Spatial Data Portal

#### Manager
<a name="manager"></a>
+ Can create and update resources
+ Can add or remove Contributors and Viewers (but not Owners or other Managers)
+ Cannot delete resources
+ Can operate on access management features in the Spatial Data Portal

#### Contributor
<a name="contributor"></a>
+ Can create and update resources
+ Cannot manage members or delete resources
+ Can view the list of members
+ Has access to create and edit features in the Spatial Data Portal

#### Consumer (Projects only)
<a name="consumer"></a>
+ Can view resource details and download file content
+ Can obtain temporary credentials for asset downloads via the CLI or desktop application
+ Cannot create, update, or delete anything
+ Cannot see the list of members
+ Has access to view and download features in the Spatial Data Portal

**Note**
Consumer is only available on Projects. It provides the same read and download access as Contributor without any write permissions. Use Consumer when you want to grant file download access to users who should not be able to create or modify assets.

#### Viewer
<a name="viewer"></a>
+ Read-only access to resource metadata (names, descriptions, file listings, attributes)
+ Can see file metadata and server-generated thumbnail previews
+ Cannot download file content or obtain temporary credentials for asset downloads on Projects
+ Cannot create, update, or delete anything
+ Cannot see the list of members
+ Has access only to view features in the Spatial Data Portal

## Library-level Creation Control
<a name="library-level-creation-control"></a>

The permission model separates resource creation from resource operation. This design provides granular control over who can create primary resource types versus who can use and operate them.

### How it works
<a name="_how-it-works"></a>
+ To create new Projects, Asset Templates, or Connectors, you need at least Contributor permissions on the Library itself
+ When you create a resource, you automatically become its Owner
+ Library-level permissions also directly inherit to all resources under that Library
+ This separation allows organizations to grant full operational control over individual resources to their owners without providing them higher-level access to create new primary resources

### Example scenarios
<a name="_example-scenarios"></a>

 **Alice is a Library Contributor:**
+ She can create new Projects, Asset Templates, and Connectors
+ When she creates a Project, she automatically becomes the Owner of that Project
+ She can add other users or groups as members of her Project

 **Bob is a Project Owner but only a Library Viewer:**
+ He has full control over his Project (can manage members, delete Assets, etc.)
+ He cannot create new Projects because he’s only a Viewer at the Library level
+ He must ask a Library Owner, Manager, or Contributor to create new Projects

 **Carol has no Library permissions:**
+ She cannot see the Library or any resources unless explicitly granted access
+ She must be added as a member to specific Projects, Asset Templates, or Connectors
+ Once added to a Project as a Contributor, she can create Assets within that Project, but still cannot create new Projects

## Detailed Actions by Resource Type
<a name="detailed-actions-by-resource-type"></a>

Each resource type has specific actions available at each permission level. The tables below show exactly what you can do with each resource based on your permission level.

### Library Actions
<a name="library-actions"></a>

**Library Permission Actions**

| Action | Owner | Manager | Contributor | Viewer |
| --- | --- | --- | --- | --- |
| View Library details and list all Libraries | ✓ | ✓ | ✓ | ✓ |
| View Library permissions | ✓ | ✓ | ✓ | ✓ |
| Search Assets and Files across the Library | ✓ | ✓ | ✓ | ✓ |
| View child resources (Projects, Asset Templates, Connectors) | ✓ | ✓ | ✓ | ✓ |
| View Library members | ✓ | ✓ | ✓ |  |
| Create Projects, Asset Templates, and Connectors | ✓ | ✓ | ✓ |  |
| Get credentials for Library operations | ✓ | ✓ | ✓ |  |
| Perform Contributor actions on child resources | ✓ | ✓ | ✓ |  |
| Query audit events | ✓ | ✓ |  |  |
| Manage Library members (Contributors and Viewers only) | ✓ | ✓ |  |  |
| Perform Manager actions on child resources | ✓ | ✓ |  |  |
| Manage Library members (all levels) | ✓ |  |  |  |
| Perform Owner actions on child resources | ✓ |  |  |  |

### Project Actions
<a name="project-actions"></a>

**Project Permission Actions**

| Action | Owner | Manager | Contributor | Consumer | Viewer |
| --- | --- | --- | --- | --- | --- |
| View Project details and list all Projects | ✓ | ✓ | ✓ | ✓ | ✓ |
| View Assets and Asset versions | ✓ | ✓ | ✓ | ✓ | ✓ |
| List and view File metadata | ✓ | ✓ | ✓ | ✓ | ✓ |
| View Project attributes | ✓ | ✓ | ✓ | ✓ | ✓ |
| Download file content | ✓ | ✓ | ✓ | ✓ |  |
| Get credentials for downloading Assets | ✓ | ✓ | ✓ | ✓ |  |
| View Project members | ✓ | ✓ | ✓ |  |  |
| Update Project details | ✓ | ✓ | ✓ |  |  |
| Create and update Assets | ✓ | ✓ | ✓ |  |  |
| Trigger Connectors on Assets | ✓ | ✓ | ✓ |  |  |
| Get credentials for Asset upload operations | ✓ | ✓ | ✓ |  |  |
| Manage all Project attributes | ✓ | ✓ | ✓ |  |  |
| Delete Assets | ✓ | ✓ |  |  |  |
| Manage Project members (Contributors, Consumers, and Viewers only) | ✓ | ✓ |  |  |  |
| Delete Project | ✓ |  |  |  |  |
| Manage Project members (all levels) | ✓ |  |  |  |  |

### Asset Template Actions
<a name="asset-template-actions"></a>

**Asset Template Permission Actions**

| Action | Owner | Manager | Contributor | Viewer |
| --- | --- | --- | --- | --- |
| View Asset Template details and list all Asset Templates | ✓ | ✓ | ✓ | ✓ |
| List Assets using this template | ✓ | ✓ | ✓ | ✓ |
| View Project associations | ✓ | ✓ | ✓ | ✓ |
| View all known attributes | ✓ | ✓ | ✓ | ✓ |
| View Asset Template members | ✓ | ✓ | ✓ |  |
| Update Asset Template details | ✓ | ✓ | ✓ |  |
| Manage Project associations | ✓ | ✓ |  |  |
| Request and delete Connector associations | ✓ | ✓ |  |  |
| Manage Asset Template members (Contributors and Viewers only) | ✓ | ✓ |  |  |
| Delete Asset Template | ✓ |  |  |  |
| Manage Asset Template members (all levels) | ✓ |  |  |  |

### Connector Actions
<a name="connector-actions"></a>

**Connector Permission Actions**

| Action | Owner | Manager | Contributor | Viewer |
| --- | --- | --- | --- | --- |
| View Connector details and list all Connectors | ✓ | ✓ | ✓ | ✓ |
| View Connector resources | ✓ | ✓ | ✓ | ✓ |
| View Asset Template associations | ✓ | ✓ | ✓ | ✓ |
| View Connector permissions | ✓ | ✓ | ✓ | ✓ |
| View all known attributes | ✓ | ✓ | ✓ | ✓ |
| View Connector members | ✓ | ✓ | ✓ |  |
| Update Connector configuration | ✓ | ✓ | ✓ |  |
| Manage Asset Template associations | ✓ | ✓ |  |  |
| Manage Connector members (Contributors and Viewers only) | ✓ | ✓ |  |  |
| Delete Connector | ✓ | ✓ |  |  |
| Manage Connector members (all levels) | ✓ |  |  |  |

## Resource Types
<a name="resource-types"></a>

The solution has four main resource types, each with its own permission management.

### Library
<a name="library"></a>

 **What it is:** The top-level container for all resources in your SDMA deployment.

 **Key characteristics:**
+ There is one Library per deployment
+ Cannot be deleted
+ The `SpatialDataManagementAdministrators` group automatically has Owner permissions (this is a Cognito group created at deployment time; you can add individual users or other groups to it)
+ Library permissions can grant access to all child resources (Projects, Asset Templates, Connectors)

 **In the Spatial Data Portal:**
+ Access via the "Library" or "Home" icon in main navigation
+ View members in the "Members" tab
+ No "Delete" button (Libraries cannot be deleted)

 **Permission inheritance:**
+ If you’re a Library Owner, you have Owner access to all Projects, Asset Templates, and Connectors
+ If you’re a Library Manager, you have Manager access to all child resources
+ If you’re a Library Contributor, you have Contributor access to all child resources

### Project
<a name="project"></a>

 **What it is:** A logical grouping of related Assets.

 **Key characteristics:**
+ Assets inherit Project permissions (no separate asset-level permissions)
+ Projects support five permission levels: Owner, Manager, Contributor, Consumer, and Viewer
+ Project Consumers can view all Assets and download file content
+ Project Viewers can view Asset metadata but cannot download file content
+ Project Contributors can create and update Assets in the Project

 **In the Spatial Data Portal:**
+ View all Projects: Library → "Content" tab → "Projects" section
+ Project details page shows name and description
+ Access Management tab shows who has access (if you’re a Contributor or higher)

### Asset Template
<a name="asset-template"></a>

 **What it is:** Defines structure, validation rules, and lifecycle management for content within Projects, including how they transform, distribute, or integrate content with connected applications.
+ Independent permissions from Projects
+ Must be explicitly associated with Projects before use (requires Manager or Owner approval on the Project)
+ Once associated, any Project member can create or update Assets using that template without needing explicit permissions on the template itself
+ Can be associated with multiple Projects
+ Library-level permissions grant access to Asset Templates

 **In the Spatial Data Portal:**
+ View all Asset Templates: Library → "Content" tab → "Asset templates" section
+ Template details page shows schema and validation rules
+ Access Management tab shows who has access

<a name="connector"></a> **What it is:** Enables integration with external systems and automated workflows.

 **Key characteristics:**
+ Independent permissions from Projects and Asset Templates
+ Must be explicitly associated with Asset Templates before use (requires Manager or Owner approval on the Asset Template)
+ Once associated, any user with access to Assets using that template can utilize the connector without needing explicit permissions on the connector itself
+ Can be associated with multiple Asset Templates
+ Library-level permissions grant access to Connectors

 **In the Spatial Data Portal:**
+ View all Connectors: Library → "Content" tab → "Connectors" section
+ Connector details page shows configuration and status
+ Access Management tab shows who has access

### View your permission level
<a name="managing-permissions-in-the-portal"></a>

The Spatial Data Portal controls what you can see and do based on your permission level. To understand your access:
+ Observe which buttons and actions are available
+ If you see the Access Management tab, you have Contributor, Manager, or Owner permissions
+ If you see "Create" and "Edit" buttons, you have Contributor or higher permissions
+ If you see "View" and "Download" options, you have Consumer or higher permissions on a Project
+ If you only see "View" options without download controls, you have Viewer permissions on a Project

### View members
<a name="viewing-members"></a>

To see who has access to a resource, complete the following steps.

1. Navigate to the resource (Project, Asset Template, or Connector)

1. Choose the **Access Management** tab

1. View the list of users and groups with access

1. See each member’s permission level

**Note**
You must be a Contributor or higher to view the Access Management tab.

### Add members
<a name="adding-members"></a>

To grant someone access to a resource, complete the following steps.

1. Navigate to the resource

1. Choose the **Access Management** tab

1. Choose the **Add Member** button

1. Select the user or group

1. Choose the permission level:
   +  **Managers can add:** Contributors, Consumers, and Viewers only
   +  **Owners can add:** Any permission level
   +  **Note:** Consumer is only available when adding members to Projects

1. Choose **Add**

**Note**
You must be a Manager or Owner to add members.

### Change permission levels
<a name="changing-permission-levels"></a>

To change someone’s permission level, complete the following steps.

1. Navigate to the resource

1. Choose the **Members** tab

1. Find the member in the list

1. Choose the **Edit** icon next to their name

1. Select the new permission level

1. Choose **Save**

 **Restrictions:**
+ Managers can only change Contributors and Viewers
+ Owners can change any permission level
+ You cannot change your own permission level

### Removing members
<a name="removing-members"></a>

To remove someone’s access:

1. Navigate to the resource

1. Choose the **Members** tab

1. Find the member in the list

1. Choose the **Remove** icon next to their name

1. Confirm the removal

 **Restrictions:**
+ Managers can only remove Contributors and Viewers
+ Owners can remove any permission level
+ You cannot remove the last Owner from a resource

### Understanding Group Permissions
<a name="understanding-group-permissions"></a>

 **What are groups?**
+ Groups are collections of users managed in your identity provider
+ Permissions can be assigned to groups instead of individual users
+ Users automatically inherit permissions from their groups

 **How it works in the Spatial Data Portal:**
+ Groups appear in the Members list with a group icon
+ Users see their effective permission level (highest from all groups)
+ Removing a user from a group removes their inherited permissions

 **Example:**
+ User Alice is in the "Engineering Team" group
+ "Engineering Team" has Contributor access to a Project
+ Alice automatically has Contributor access to that Project
+ If Alice is removed from "Engineering Team", she loses access (unless she has direct permissions)

## Understanding Your Access
<a name="understanding-your-access"></a>

### Effective Permission Level
<a name="effective-permission-level"></a>

Your "effective permission level" is the highest permission you have on a resource, considering:
+ Direct permissions assigned to you
+ Permissions inherited from groups you belong to
+ Permissions inherited from the Library (if applicable)

 **Example:**
+ You have Viewer access directly on a Project
+ You’re in a group with Contributor access to the same Project
+ Your effective permission level is Contributor (the higher of the two)

### What You Can See and Do
<a name="what-you-can-see-and-do"></a>

The Spatial Data Portal automatically shows or hides UI elements based on your permission level:

 **Create Button:**
+ Visible if you’re a Contributor, Manager, or Owner
+ Hidden if you’re a Consumer or Viewer

 **Edit Button:**
+ Visible if you’re a Contributor, Manager, or Owner
+ Hidden if you’re a Consumer or Viewer

 **Download Button (Projects):**
+ Visible if you’re a Consumer, Contributor, Manager, or Owner
+ Hidden if you’re a Viewer

 **Delete Button:**
+ Visible only if you’re an Owner
+ Hidden for all other permission levels

 **Access Management Tab:**
+ Visible if you’re a Contributor, Manager, or Owner
+ Hidden if you’re a Consumer or Viewer

## Resource Associations and Approvals
<a name="resource-associations"></a>

Resource associations in SDMA require approval from both parties. This two-way approval process ensures that both resource owners consent to the association.

### Association Types
<a name="association-types"></a>

There are two types of resource associations:
+  **Asset Template to Project** – Associates an Asset Template with a Project, allowing Assets in that Project to use the template’s schema
+  **Connector to Asset Template** – Associates a Connector with an Asset Template, enabling automated workflows when Assets are created or updated

### Association Workflow
<a name="association-workflow"></a>

Each association follows a two-step request and approval process:

1.  **Request** – One party requests the association

1.  **Approve or Reject** – The other party reviews and approves or rejects the request

#### Asset Template to Project Association
<a name="asset-template-to-project-association"></a>

 **Step 1: Request Association (Project Owner or Manager)**

1. Navigate to your Project

1. Select the Asset Templates tab

1. Choose "Request Association" and select the Asset Template

1. The request is sent to the Asset Template Owner or Manager

 **Step 2: Approve or Reject (Asset Template Owner or Manager)**

1. Navigate to the Asset Template

1. View pending association requests

1. Approve or reject the request from the Project

 **Who can perform these actions:**
+ Request association: Project Owner or Manager
+ Approve/reject association: Asset Template Owner or Manager

#### Connector to Asset Template Association
<a name="connector-to-asset-template-association"></a>

 **Step 1: Request Association (Asset Template Owner or Manager)**

1. Navigate to your Asset Template

1. Select the Connectors tab

1. Choose "Request Association" and select the Connector

1. The request is sent to the Connector Owner or Manager

 **Step 2: Approve or Reject (Connector Owner or Manager)**

1. Navigate to the Connector

1. View pending association requests

1. Approve or reject the request from the Asset Template

 **Who can perform these actions:**
+ Request association: Asset Template Owner or Manager
+ Approve/reject association: Connector Owner or Manager

### Why Two-Way Approval?
<a name="why-two-way-approval"></a>

The two-way approval process ensures:
+  **Consent from both parties** – Both resource owners agree to the association
+  **Control over resource usage** – Asset Template and Connector owners control which Projects can use their resources
+  **Security** – Prevents unauthorized use of templates and connectors across different teams or organizations

### Removing Associations
<a name="removing-associations"></a>

Either party can remove an association at any time:
+ Project Owners/Managers can remove Asset Template associations from their Projects
+ Asset Template Owners/Managers can remove Connector associations from their Asset Templates
+ Asset Template Owners/Managers can remove Project associations from their Asset Templates
+ Connector Owners/Managers can remove Asset Template associations from their Connectors

## Common Workflows
<a name="common-workflows"></a>

### Setting Up a New Project
<a name="setting-up-a-new-project"></a>

 **As a Library Owner or Manager:**

1. Create the Project (from the home page, select "Create project")

1. Add team members with appropriate permissions:
   + Add Project Managers (can manage team access)
   + Add Contributors (can create and update Assets)
   + Add Consumers (can view and download Assets)
   + Add Viewers (can view Asset metadata only)

1. Associate Asset Templates if needed

1. Configure Connectors for automated workflows

### Onboarding a New Team Member
<a name="onboarding-a-new-team-member"></a>

 **As a Project Manager or Owner:**

1. Determine what access they need:
   + Owner: Full control (rare, usually for project leads)
   + Manager: Can manage team access
   + Contributor: Can create and update Assets
   + Consumer: Can view and download Assets (no write access)
   + Viewer: Read-only access to metadata (no file downloads)

1. Add them to the appropriate resources:
   + Add to Library for organization-wide access
   + Add to specific Projects for project-specific access

1. Consider using groups for easier management:
   + Add user to existing group instead of individual permissions
   + Groups make it easier to manage multiple users

### Transitioning Project Ownership
<a name="transitioning-project-ownership"></a>

**Note**
 **Best Practice:** When starting a new Project, assign a group as the Owner rather than individual users. This prevents ownership issues when people change roles or leave the organization, and allows IT administrators to manage ownership transitions through your identity provider without needing access to the application.

 **Using Groups for Ownership (Recommended):**

1. Use an existing team or role-based group from your identity provider (e.g., "Engineering-Team", "Site-Managers", or "GIS-Admins")

1. Add the group as a Project Owner

1. When ownership transitions are needed:
   + Add new owners to the group in your identity provider
   + Remove departing owners from the group in your identity provider
   + No changes needed in the Spatial Data Portal

1. Groups typically represent teams with multiple members, ensuring someone always has access. In the rare case where a group has only one member, IT administrators can add new members through the identity provider to recover access

 **Transitioning Individual Ownership (Alternative):**

If you’re using individual user permissions instead of groups:

1. Add the new owner as a member with Owner permission

1. Verify they can access all resources

1. Optionally remove your own Owner permission (if stepping away)

1. Ensure at least one Owner remains on the Project

**Note**
You cannot remove the last Owner from a resource.

### Managing External Contractors
<a name="managing-external-contractors"></a>

 **As a Project Manager or Owner:**

1. Create a group for contractors (e.g., "External-Scanning-Team")

1. Add the group to specific Projects with Contributor access

1. Add contractor users to the group

1. When contract ends, remove users from the group (permissions automatically revoked)

 **Benefits of using groups:**
+ Easier to manage multiple contractors
+ Consistent permissions across all contractors
+ Quick onboarding and offboarding

## Troubleshooting
<a name="troubleshooting"></a>

### "You do not have permission to access that resource"
<a name="you-do-not-have-permission-to-access-that-resource"></a>

 **Possible causes:**
+ You’re a Viewer trying to create or update resources
+ You’re a Contributor trying to manage members
+ You’re a Manager trying to delete a resource or add Owners

 **Solutions:**
+ Check your permission badge on the resource page
+ Contact a Manager or Owner to request higher permissions
+ Verify you’re accessing the correct resource

### "Cannot see the Members tab"
<a name="cannot-see-the-members-tab"></a>

 **Cause:** You’re a Viewer on this resource.

 **Solution:** Viewers cannot see the Members tab. Contact a Manager or Owner if you need to know who has access.

### "Cannot add Owner or Manager permissions"
<a name="cannot-add-owner-or-manager-permissions"></a>

 **Cause:** You’re a Manager, and Managers can only add Contributors and Viewers.

 **Solution:** Contact an Owner to add Owners or Managers.

### "Cannot remove a member"
<a name="cannot-remove-a-member"></a>

 **Possible causes:**
+ You’re trying to remove an Owner or Manager (only Owners can do this)
+ You’re trying to remove the last Owner (not allowed)

 **Solutions:**
+ Contact an Owner to remove Owners or Managers
+ Add another Owner before removing the last one

### "My permission level doesn’t match what I expect"
<a name="my-permission-level-doesnt-match-what-i-expect"></a>

 **Possible causes:**
+ You have permissions from multiple sources (direct \+ groups \+ Library)
+ Your effective permission is the highest from all sources

 **Solution:**
+ Check the Members tab to see all your permission sources
+ Contact an Owner if you need different permissions

### "Group permissions not working"
<a name="group-permissions-not-working"></a>

 **Possible causes:**
+ You’re not actually a member of the group in your identity provider
+ Group name doesn’t match exactly
+ Recent group changes haven’t propagated yet

 **Solutions:**
+ Verify your group membership with your IT administrator
+ Wait a few minutes for changes to propagate
+ Try logging out and back in

### "Viewer cannot download files"
<a name="viewer-cannot-download-files"></a>

 **Cause:** Viewers on Projects have read-only access to file metadata but cannot download file content or obtain temporary credentials for asset downloads.

 **Solution:** Upgrade the member to Consumer permission level, which grants file download access without write permissions. A Project Manager or Owner can change the permission level from the Access Management tab.

## Glossary
<a name="glossary"></a>

| Term | Definition |
| --- | --- |
| Permission Level | The level of access you have on a resource (Owner, Manager, Contributor, Consumer, or Viewer). Consumer is available on Projects only. |
| Effective Permission Level | The highest permission level you have on a resource, considering all sources (direct, groups, Library) |
| Resource | An entity in SDMA (Library, Project, Asset Template, or Connector) |
| Member | A user or group with permissions on a resource |
| Group | A collection of users managed in your identity provider |
| Permission Inheritance | Library-level permissions that automatically grant access to child resources |
| Direct Permission | Permission assigned directly to you (not through a group) |
| Group Permission | Permission you inherit from a group you belong to |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Spatial Data Management on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
