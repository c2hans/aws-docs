---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/post-deployment-configuration.html
---

# Post-Deployment Configuration
<a name="post-deployment-configuration"></a>

## 1. Create Initial User
<a name="create-initial-user"></a>

To create initial users:

1. Open the [Cognito console](https://console.aws.amazon.com/cognito/)

1. Select the User Pool created during deployment (the name follows the pattern `spatial-data-management-user-pool`)

1. Choose **Users** and then choose **Create user**

1. Choose **Create user**

1. Repeat steps 3-5 to create one or two additional test users

1. Select the first user you created

1. Choose **Add user to group**

1. Select the **SpatialDataManagementAdministrators** group

1. Choose **Add to group**

We recommend creating multiple test users (2-3 users) when performing a proof of concept or test run. The first user assigned to the SpatialDataManagementAdministrators group automatically has ownership of the Library and can assign permission levels to other users as they onboard. You can use the additional users to test different permission levels on various resources, simulating different access scenarios and validating the authorization model.

For more information, see [Creating and managing users](https://docs.aws.amazon.com/cognito/latest/developerguide/how-to-manage-user-accounts.html) in the Amazon Cognito Developer Guide.

## 2. Verify Deployment
<a name="verify-deployment"></a>

Access the web portal:

1. Open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/)

1. Select your stack and choose the **Outputs** tab

1. Copy the PortalUrl value

1. Open the URL in your web browser to verify the portal is accessible

1. Log in using one of the users you created in the previous step

1. Verify you can access the portal interface successfully

Upon successful login, you will see different interfaces depending on your user role:

 **Administrator User:**

![First-time login portal view for administrator users showing full access to all features and management capabilities](http://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/first-time-login-portal-browser-adminuser.png)

 **General User:**

![First-time login portal view for general users showing standard access to portal features](http://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/images/first-time-login-portal-browser-user.png)

**Note**
The interface you see on first-time login will vary based on your assigned user group and permissions. Administrator users (members of the SpatialDataManagementAdministrators group) have access to additional management features and system configuration options. General users who are not part of the administrators group and have not been granted specific permissions to the Default Library or any Projects will see the standard portal interface with limited access until additional permissions are assigned to them.

## Reuse existing networking infrastructure
<a name="reuse_existing_networking_infrastructure"></a>
