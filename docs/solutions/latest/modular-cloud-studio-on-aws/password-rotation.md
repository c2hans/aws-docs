---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/password-rotation.html
---

# Password rotation
<a name="password-rotation"></a>

## Overview and prerequisites
<a name="overview-and-prerequisites"></a>

Password rotation is a critical security practice that helps maintain the integrity of your MCS deployment. AWS Managed Microsoft AD passwords expire every 90 days and must be rotated manually to prevent service disruptions.

 **Before you begin:**
+ Plan this activity during a maintenance window as users may experience temporary authentication issues
+ Ensure you have administrative access to AWS Directory Service, Secrets Manager, and relevant service consoles

## Active Directory password rotation
<a name="active-directory-password-rotation"></a>

When you create an AWS Managed Microsoft AD through the identity module, three account users are created for authentication throughout the solution:
+  **StudioAdmin** - Admin user for end-user access
+  **SA\_AdConnectorUser** - Service account for cross-region AD communication
+  **SA\_McsModulesUser** - General service account for MCS modules (e.g., syncing Microsoft AD users with Leostream module)

### Step 1: Reset passwords in AWS Managed Microsoft AD
<a name="step-1-reset-passwords-in-aws-managed-microsoft-ad"></a>

1. Navigate to the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/)

1. Locate the AWS Managed Microsoft AD instance associated with MCS (default domain: `studio.mcs.internal`)
**Tip**
If you’re unsure of the Directory ID, log in to the MCS console via the CloudFront URL, go to the Identity tab, and click External Link.

1. Click on the Directory ID to open the directory details

1. Click **Actions** → **Reset User Password**

1. For each user:

   1. Enter the username

   1. Generate a secure password meeting complexity requirements

   1. Enter and confirm the new password

   1. Record the password securely for use in subsequent steps

   1. Click **Reset Password**

   1. Wait for confirmation message before proceeding to the next user

### Step 2: Synchronize password changes
<a name="step-2-synchronize-password-changes"></a>

After resetting passwords in Active Directory, you must update the corresponding secrets and configurations in dependent services.

#### Update AWS Secrets Manager
<a name="update-aws-secrets-manager"></a>

1. Navigate to the [AWS Secrets Manager console](https://console.aws.amazon.com/secretsmanager/)

1. Update the following secrets with their corresponding new passwords:

<table>
<thead>
  <tr><th>User</th><th>Secret Name Pattern</th></tr>
</thead>
<tbody>
  <tr><td>StudioAdmin</td><td> <code>/[MCSDeploymentId]/Identity/StudioAdminActiveDirectoryLoginCredentials</code> </td></tr>
  <tr><td>SA_AdConnectorUser</td><td> <code>/[MCSDeploymentId]/Identity/AdConnectorServiceAccountActiveDirectoryLoginCredentials</code> </td></tr>
  <tr><td>SA_McsModulesUser</td><td> <code>/[MCSDeploymentId]/Identity/McsModulesServiceAccountActiveDirectoryLoginCredentials</code> </td></tr>
</tbody>
</table>

1. For each secret:

   1. Click on the secret name

   1. Click **Retrieve Secret Value**

   1. Update the password field with the corresponding new password

   1.  **Save** the changes

#### Update AD Connector (spoke Regions)
<a name="update-ad-connector-spoke-regions"></a>

For each spoke region with an AD Connector:

1. Use the Region Selector to navigate to the spoke region

1. Go to the [Directory Service console](https://console.aws.amazon.com/directoryservicev2/)

1. Click on the AD Connector with the MCS domain name

1. Navigate to **Network and Security**

1. Scroll to **Service Account Credentials** and click **Update**

1. Set the password to match the new SA\_AdConnectorUser password

1. Click **Update**

1. Wait for the status to show "Active" before proceeding to the next region

**Important**
Wait approximately 1 hour before attempting to log in to workstations in spoke Regions after updating the AD Connector password.

#### Update Leostream Active Directory authentication
<a name="update-leostream-active-directory-authentication"></a>

1. Log in to the Leostream management dashboard using the admin user

1. Navigate to **Setup** → **Authentication Servers** → **Edit**

1. Locate the authentication server configuration section

1. Update the password field with the new SA\_McsModulesUser password

1. Click **Save**

1. Test the connection by attempting to authenticate a test user

After completing this update, you can log in to Leostream Gateway with Amazon DCV using the new StudioAdmin password or any other user credentials from the AWS Managed Microsoft AD.

#### Update storage modules
<a name="update-storage-modules"></a>

 **Amazon FSx for Lustre**: Password changes are automatically synchronized. No manual action required.

 **Amazon FSx for Windows**: Manual password synchronization is required.

1. Navigate to the [Amazon FSx console](https://console.aws.amazon.com/fsx/)

1. Click on your Windows file system

1. Go to **Network and Security**

1. Locate the **Service Account** section with SA\_McsModulesUser

1. Click **Update** next to the service account credentials

1. Set the password to match the new SA\_McsModulesUser password

1. Monitor the **Updates** section for completion of the Service Account Credential update

1. Verify the file system status remains "Available" after the update

If the Amazon FSx Windows module shows as misconfigured after password expiration:

1. Click **Attempt Recovery** to reconfigure the module

1. Wait for the update to complete

1. Verify the module status returns to available

## Manually rotating the Leostream database secret
<a name="manually-rotating-the-leostream-database-secret"></a>

This solution doesn’t provide automatic secrets rotation. Depending on your security requirements, you may consider manually rotating the credentials for your Leostream Connection Broker database. Follow these steps to manually rotate PostgreSQL database credentials:

1.  **Log into to the admin dashhoard with admin**

   Log into the Leostream Broker through the Leostream Gateway with "admin" credentials. That is located at: `/[MCSDeploymentId]/WorkstationManagement/Leostream/Console/AdminUserCredentials`.

1.  **Switch Leostream Credentials**

   This step is necessary. Without this temporary switch, the gateway cannot connect to the broker when the new password is changed. To update the corresponding credentials in the Leostream Connection Broker, see the [Leostream Administrator’s Guide](https://leostream.com/wp-content/uploads/2018/11/leostream-administrators-guide.pdf). This updates the Leostream settings to use the new database password. Under the Systems > Maintenance, choose DATABASE OPTIONS > Switch to PostgreSQL database. You will use the postgres default admin credentials to make this switch. This is located at `LeostreamBrokerStorageSitCD-*`.

1.  **Leostream Connection Broker Restart Time**

   The Broker will take a couple of minutes to restart for you to be able to log in.

1.  **Update the PostgreSQL user password**

   To change the password of the PostgreSQL "leostream" user, follow the instructions provided in the PostgreSQL documentation [SQL ALTER USER Command](https://www.postgresql.org/docs/8.0/sql-alteruser.html). Ensure you modify only the "leostream" user credentials, not the default administrator account. This helps you ensure that the database credentials are updated correctly at the database level.

1.  **Update secret in Secrets Manager**

   Locate the secret at: `/[MCSDeploymentId]/WorkstationManagement/Leostream/Database/Credentials`, then update the secret with the new credentials.

   ```
   *Update Leostream credentials*
   ```

   To update the corresponding credentials in the Leostream Connection Broker, see the [Leostream Administrator’s Guide](https://leostream.com/wp-content/uploads/2018/11/leostream-administrators-guide.pdf). This updates the Leostream settings to use the new database password. Under the Systems > Maintenance, choose DATABASE OPTIONS > Switch to PostgreSQL database. You will switch back to the "leostream" user. This is located at `/[MCSDeploymentId]/WorkstationManagement/Leostream/Database/Credentials`.

1.  **Leostream Connection Broker Restart Time**

   The Broker will take a couple of minutes to restart for you to be able to log in.

The following secrets can be rotated using a similar process:
+  `/[MCSDeploymentId]/WorkstationManagement/Leostream/API/ServiceUserCredentials`
+  `/[MCSDeploymentId]/WorkstationManagement/Leostream/Console/AdminUserCredential`
