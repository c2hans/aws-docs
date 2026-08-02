---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/getting-started-users.html
---

# Getting Started for users
<a name="getting-started-users"></a>

## Test or Proof of Concept Setup
<a name="test-proof-of-concept-setup"></a>

If you are evaluating Spatial Data Management on AWS or running a proof of concept, follow this streamlined setup:

1. Complete the [IT Administrator setup](#it-administrator-initial-setup) to designate a Library Owner

1. Create 2-3 test users in Amazon Cognito (see [Designate Initial Administrator](#designate-initial-administrator))

1. Have each test user sign in once to initialize their accounts

1. As the Library Owner, assign different permission levels to test users:
   + Assign one user as **Manager** to test permission management capabilities
   + Assign one user as **Contributor** to test content creation workflows
   + Assign one user as **Viewer** to test read-only access

1. Choose a user (Library Owner or Contributor) and follow the [Upload your first asset](upload-first-asset.md) guide to create your first project and upload your first asset

This setup allows you to evaluate the solution’s permission model and test different user workflows.

## IT Administrator: Initial Setup
<a name="it-administrator-initial-setup"></a>

**Important**
This section is for IT Administrators only. Complete these steps immediately after deploying the solution and before general users access the system.

After deploying Spatial Data Management on AWS, the IT Administrator must designate an initial administrator user who will manage the solution.

### Designate Initial Administrator
<a name="designate-initial-administrator"></a>

1. Open the [Amazon Cognito console](https://console.aws.amazon.com/cognito/)

1. Select the User Pool created by the solution (the name follows the pattern `SpatialDataManagement-user-pool`)

1. Choose **Users**, and then choose **Create user**

1. Enter the username and temporary password for your initial administrator

1. Choose **Create user**

1. Select the newly created user from the user list

1. Choose **Add user to group**

1. Select the **SpatialDataManagementAdministrators** group

1. Choose **Add to group**

This user is now the initial administrator and will automatically become the Library Owner for your instance of SDMA.

**Note**
Spatial Data Management on AWS supports one Library per deployment. The first user added to the `SpatialDataManagementAdministrators` group automatically receives Owner permissions for the Library and can then assign permissions to other users as they are onboarded.

## Library Owner: Initial Setup
<a name="library-owner-initial-setup"></a>

**Important**
This section is for the initial Library Owner (the user added to the `SpatialDataManagementAdministrators` group). Complete these steps after the IT Administrator has designated you as the Library Owner.

As the Library Owner, you have full control over the Spatial Data Management permissions management. You can immediately start using the application to create projects and assets, but you must also onboard other users by assigning them appropriate permission levels.

### Onboard Additional Users
<a name="onboard-additional-users"></a>

Before you can assign permissions to other users, they must first sign in to the application at least once.

1. Have the IT Administrator create user accounts in Amazon Cognito for all team members who need access

1. Provide each user with:
   + The portal URL
   + Their Amazon Cognito credentials

1. Instruct each user to sign in to the portal once to initialize their account
**Note**
When users sign in for the first time, they will not be able to perform any operations because they have no assigned permissions. This initial sign-in is required to register them in the system so you can assign permissions.

1. After users have signed in once, you can assign them permission levels:
   + Navigate to the Library, Project, or Asset where you want to grant access
   + Choose **Manage Access** or **Members**
   + Select the user from the list of available users
   + Assign the appropriate permission level:
     +  **Owner** – Full access including permission management
     +  **Manager** – Can create, update, and manage access
     +  **Contributor** – Can create and update resources
     +  **Viewer** – Read-only access

### Start Using the Application
<a name="start-using-the-application"></a>

As the Library Owner, you can immediately begin:
+ Creating projects to organize your spatial data
+ Defining asset templates to standardize metadata
+ Uploading and managing spatial assets
+ Configuring connectors for external system integration

For detailed instructions on these tasks, see the sections below.

## General User: Getting Started
<a name="general-user-getting-started"></a>

This section is for general users who have been granted access to Spatial Data Management on AWS by the Library Owner or an administrator.

### Initial Sign-In
<a name="initial-sign-in"></a>

When you first receive your credentials:

1. Obtain the following from your administrator:
   + Portal URL
   + Amazon Cognito username
   + Temporary password

1. Open the portal URL in your web browser

1. Sign in with your Amazon Cognito credentials

1. If prompted, change your temporary password to a permanent password

**Note**
After your first sign-in, you may not be able to perform any operations until the Library Owner or an administrator assigns you appropriate permissions. Contact your administrator if you need access to specific projects or assets.
