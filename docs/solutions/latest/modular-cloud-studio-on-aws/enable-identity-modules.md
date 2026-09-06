---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/enable-identity-modules.html
---

# Step 2: Enable Identity modules
<a name="enable-identity-modules"></a>

Follow these steps to enable the Identity module.

1. Navigate to the MCS web console (see [Launch the stack](launch-the-stack.md) for details).

1. Select **Identity** from the left navigation pane.

1. Choose **Deploy New Module**.

1. Based on your use cases, follow the steps in [Create AWS Managed Microsoft Active Directory](#create-aws-managed-microsoft-active-directory) for creating a new AWS Directory Service instance, or follow the steps in [Import Custom Microsoft Active Directory](#import-custom-microsoft-active-directory) to import an existing Active Directory by providing the required attributes.

## Option 2.a: Create AWS Managed Microsoft Active Directory
<a name="create-aws-managed-microsoft-active-directory"></a>

1. For **Select Region**, select the Region where you want the Directory Service to be created. There should be only one hub Region option if you have not deployed any spoke Regions.

1. For **Select Identity** module, select **Create AWS Managed Microsoft Active Directory** and choose **Next**.

1. For **Configure AD settings**, review the parameters for this module and modify them as necessary. This module uses the following default values.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/enable-identity-modules.html)

1. For **Configure Tag Settings**, review the tags for this module and modify them as necessary. By default, this module uses tags defined in the main solution stack.

1. For **Review and deploy module**, choose **Deploy Module**.

1. The status of the Identity module shows as **Enabling in progress**. The deployment of this module takes approximately 30 minutes. After the deployment is complete, the status of the Identity module shows as **Enabled**.

1. An AWS Managed Microsoft AD will be created under Standard Edition using `mad.mcs.int` as the DNS name. To retrieve the StudioAdmin credentials, navigate to the [AWS Secrets Manager console](https://console.aws.amazon.com/secretsmanager) and locate the secret at `/[MCSDeploymentId]/Identity/StudioAdminActiveDirectoryLoginCredentials`. Select the **Overview** tab and click the **Retrieve secret value** button to display both the StudioAdmin username and password. Alternatively, you can access the credentials directly by clicking the **View** button on the MCS Web UI and following the direct link to the secret.
**Note**
When modifying the StudioAdmin password through AWS Directory Service console, ensure you manually update the corresponding secret in AWS Secrets Manager to maintain synchronization. Follow the steps to reset the user password.

1. Sign in to the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/), and follow the steps for [Creating an AWS Managed Microsoft AD user](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_create_user.html) if additional users are needed.

**Important**
In addition to the StudioAdmin user, three additional users are created by the managed AD module:
 **Admin**
Required user created by the directory service
Password location in Secret Manager: `/[MCSDeploymentId]/Identity/DefaultAdminActiveDirectoryLoginCredentials`
 **SA\_AdConnectorUser**
Created by the MCS Managed AD module
Service account used by AD Connectors in the spoke regions
Password location in Secret Manager: `/[MCSDeploymentId]/Identity/AdConnectorServiceAccountActiveDirectoryLoginCredentials`
Follow the steps in [Password Rotation](password-rotation.md) to update the password
 **SA\_McsModulesUser**
Created by the MCS Managed AD module
Service account used by modules for AD configuration setup
Password location in Secret Manager: `/[MCSDeploymentId]/Identity/McsModulesServiceAccountActiveDirectoryLoginCredentials`
Follow the steps in [Password Rotation](password-rotation.md) to update the password

## Option 2.b: Import Custom Microsoft Active Directory
<a name="import-custom-microsoft-active-directory"></a>

## Pre-deployment requirements
<a name="pre-deployment-requirements-2"></a>

1. DNS Resolver Security Group

   1. Ensure a security group exists for the Route 53 resolver endpoint in your target VPC

   1. Verify the security group has two outbound rules configured to allow DNS traffic:

      1. Type: DNS (TCP), Destination: 0.0.0.0/0, Port: 53

      1. Type: DNS (UDP), Destination: 0.0.0.0/0, Port: 53

1. Route 53 Outbound Endpoint

   1. Ensure a Route 53 outbound endpoint exists in the VPC where your Active Directory domain controllers are located

   1. Verify the endpoint is configured with appropriate IP addresses in private subnets across different Availability Zones

   1. Confirm the endpoint is associated with the DNS Resolver Security Group

1. Route 53 Resolver Rule

   1. Ensure a resolver rule exists for your Active Directory domain name

   1. Verify the rule is associated with the target VPC and the outbound endpoint

   1. Confirm the rule forwards DNS queries to your Active Directory domain controllers

## Deploying the MCS Unmanaged Active Directory Module
<a name="deploying-the-mcs-unmanaged-active-directory-module"></a>

1. For **Select Region**, select the Region where you want the Directory Service to be created. There should be only one hub Region option if you have not deployed any spoke Regions.

1. For **Select Identity module**, select **Import Custom Microsoft Active Directory** and choose **Next.**

1. For **Configure AD settings**, review the parameters for this module and modify them as necessary. This module uses the following default values.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/enable-identity-modules.html)

1. For **Configure Tag Settings**, review the tags for this module and modify them as necessary. By default, this module uses tags defined in the main solution stack.

1. Choose **Next**.

1. On the **Review** page, verify all the parameters that you provided and choose **Deploy Module** if you confirm that they are correct.

1. The status of the Identity module shows as **Enabling in progress**. The deployment of this module takes approximately five minutes. After the deployment is complete, the status of the network module shows as **Enabled.**

1. Required manual configuration: navigate to `/[MCSDeploymentId]/Identity/McsModulesServiceAccountActiveDirectoryLoginCredentials` in the secret manager, update the credentials with your Active Directory service by replacing the username and password fields.

**Important**
The service account is essential for MCS modules configuration, such as Amazon FSx for Windows and Leostream broker module. Failed to update the credentials before deployment will cause module deployment failure and prevent proper service configuration.
