---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/troubleshooting.html
---

# Troubleshooting
<a name="troubleshooting"></a>

This section provides troubleshooting instructions for deploying and using the solution.

Known limitations addresses unsupported features of the solution. [Known issues](#known-issues) provides instructions to mitigate known errors. If these instructions do not address your issue, [Contact AWS Support](contact-aws-support.md) provides instructions for opening an AWS Support case for this solution.

## Known limitations
<a name="known-limitations"></a>

### Limitation: Spoke Region Leostream Gateway routing
<a name="limitation-spoke-region-leostream-gateway-routing"></a>

When a user connects to a workstation, the Global Accelerator directs them to the nearest Leostream Gateway. The user can only establish a successful connection if the workstation is located in the same spoke Region or in the hub Region. Routing between different spoke Regions with the Leostream Gateway is not supported.

For instance, consider a setup where `us-east-1` is the hub Region, and `us-west-2` and `eu-central-1` are spoke Regions. If a user near `eu-central-1` attempts to connect to a workstation located in `us-west-2`, the connection will fail.

### Limitation: vCPU capacity requirement
<a name="limitation-vcpu-capacity-requirement"></a>

When building Windows or Linux AMIs in the workstation module, the solution uses an EC2 Image Builder pipeline that requires a g4dn.xlarge instance. By default, AWS accounts have a vCPU limit of 0 for G-type instances. You may encounter the following error message:

 `An error occurred (VcpuLimitExceeded) when calling the RunInstances operation: You have requested more vCPU capacity than your current vCPU limit of 0 allows for the instance bucket that the specified instance type belongs to.`

You will need to request a quota increase in the [AWS Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/).

## Known issues
<a name="known-issues"></a>

### Problem: Register module failed
<a name="problem-register-module-failed"></a>

If during module registration, you received an error message for a Third-Party Module, check that the [manifest file](module-manifest-schema.md) is correct, and that template is a valid CloudFormation template. If there are problems with these files, the MCS web console shows an error with more information.

#### Resolution
<a name="resolution"></a>

Complete the following task to clean up a module from the `Register Failed` state:

1. In the hub Region, sign in to the [Service Catalog console](https://console.aws.amazon.com/servicecatalog/).

1. Ensure that no products were created in Service Catalog for the module that was registered. If there were, disassociate the from any MCS portfolio and remove the product. See [Deleting provisioned products](https://docs.aws.amazon.com/servicecatalog/latest/userguide/enduser-delete.html) for more information.

1. Sign in to the [DynamoDB console](https://console.aws.amazon.com/dynamodb/).

1. In the **Registered Modules** table, check for a row that represents the module that failed registration. If it exists, [remove that row](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.DeleteData.html).

1. In the **Modules Mapping** table, check for a row that contains the name of the module that failed registration. It will be in the field called **module\_pks**. If it is the only entry in that row, remove that row. Otherwise, modify that list and only remove the module partition key from it, leaving the others in place.

1. In the **External Module**\* table, if the imported the module was custom made and not one of the Third-Party Modules, remove the row. Otherwise, change the status of it to `AVAILABLE`.

1. Refresh the UI and try to register the module again.

### Problem: Enable module failed
<a name="problem-enable-module-failed"></a>

If you receive a **CREATE\_FAILED** status when enabling a module, sign in to the [Service Catalog console](https://console.aws.amazon.com/servicecatalog/) and ensure that the provisioned product received the correct inputs at deployment.

#### Resolution
<a name="resolution-2"></a>

Follow the instructions in [Disable a module](module-enablement.md#disable-a-module) to clean up a module from the Enable Failed state.

### Problem: Disable module failed
<a name="problem-disable-module-failed"></a>

If you received a **DELETE\_FAILED** message when disabling a module, sign in to the [Service Catalog console](https://console.aws.amazon.com/servicecatalog/) and ensure that the provisioned product received the correct inputs at deployment.

#### Resolution
<a name="resolution-3"></a>

Complete the following task to clean up a module from the `Disable Failed` state:

1. In the hub Region, sign in to the [Service Catalog console](https://console.aws.amazon.com/servicecatalog/).

1. Navigate to **Provisioned Products** using the left hand navigation panel.

1. Find the provisioned product for the module that failed to disable. For Third-Party Modules, it will have the same name as what is listed in the manifest file. [Terminate the provisioned product](https://docs.aws.amazon.com/servicecatalog/latest/userguide/enduser-delete.html) for this module.

1. Sign in to the [DynamoDB console](https://console.aws.amazon.com/dynamodb/).

1. In the **Enabled Modules** table, check for a row that represents the module that failed to disable. The row will have a field in the **module\_name** column that corresponds to the name of the module that failed disable. If this is a Third-Party Module, the name is listed in the module’s manifest. [Remove that row](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.DeleteData.html).

1. In the **Enabled Modules** table, check for a row that has the module name listed in **active\_dependents**. Remove any mention of that module in that column, without removing other entries in the list.

1. In the **Registered Modules** table, ensure that the module’s status is `REGISTERED`.

1. Ensure that there are no remnants of the module that failed to delete. For example, deleting the Service Catalog product for Leostream Broker doesn’t remove the AMIs or EC2 instances.

1. Refresh the UI and try disabling the module again.

### Problem: Deregister module failed
<a name="problem-deregister-module-failed"></a>

If you receive a **FAILED** message when de-registering a module during spoke stack deployment, follow these steps. If the module has been enabled, disable the module first.

#### Resolution
<a name="resolution-4"></a>

Complete the following task to clean up a module from the `De-Register Failed` state:

1. In the hub Region, sign in to the [Service Catalog console](https://console.aws.amazon.com/servicecatalog/).

1. Ensure that no product exists in Service Catalog for the module you are attempting to de-register. If one exists, disassociate it from the MCS portfolio and remove the product.

1. Sign in to the [DynamoDB console](https://console.aws.amazon.com/dynamodb/).

1. In the **Registered Modules** table, check for a row that represents the module that failed registration. If it exists, [remove that row](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.DeleteData.html).

1. In the **Modules Mapping** table, check for a row that contains the name of the module that failed registration. It will be in the field called **module\_pks**. If it is the only entry in that row, remove that row. Otherwise, modify that list and only remove the module partition key from it, leaving the others in place.

1. In the **External Module** table, if the imported the module was custom made and not one of the Third-Party Modules, remove the row. Otherwise, change the status of it to `AVAILABLE`.

### Problem: Reset MCS admin credentials or add new user
<a name="problem-reset-mcs-admin-credentials-or-add-new-user"></a>

These steps can only be completed if the user has privileges to create or edit credentials in Amazon Cognito. As such, this section is applicable to the admin that deployed MCS originally and has advanced permissions. If you want to reset the admin credentials or add a new authorized user, follow these steps.

#### Resolution
<a name="resolution-5"></a>

Complete the following tasks to update login information to the MCS portal:

1. In the hub Region, navigate to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/).

1. Select the user pool for your MCS deployment.

1. If you want to reset the admin password, select that user, and in the following screen navigate to **Actions**, then **Reset Password**. Otherwise, select **Create user** and follow the steps there. Associate an email with the new user.

### Problem: Enable Module failed with error message "Invalid Logging Configuration: The CloudWatch Logs Resource Policy size was exceeded."
<a name="problem-enable-module-failed-with-error-message-invalid-logging-configuration-the-cloudwatch-logs-resource-policy-size-was-exceeded"></a>

#### Resolution
<a name="resolution-6"></a>

This error occurs when the CloudWatch Logs resource policy exceeds the maximum size limit. These resource policies exist at the account level. To resolve this issue, follow the instructions in [Disable a module](module-enablement.md#disable-a-module) to clean up a module from the Enable Failed state. Then, modify your CloudWatch Logs resource policy to reduce its size or add a wildcard to vendedlog resource policies. For more information, consult the CloudWatch Log documentation regarding [CloudWatch Log Resource Policies](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-CWL.html). Once done, re-enable the module.

### Problem: Connection to Leostream Workstation failed with "Unable to connect" error message when using Unmanaged Active Directory
<a name="problem-connection-to-leostream-workstation-failed-with-unable-to-connect-error-message-when-using-unmanaged-active-directory"></a>

If you received an "Unable to connect" error within your Amazon DCV client and are using an Unmanaged Active Directory to deploy your Leostream broker and gateway, follow these steps.

#### Resolution
<a name="resolution-7"></a>

This error occurs when the required DNS resolver resources are not properly configured for your Unmanaged Active Directory, preventing domain name resolution and blocking connections to Leostream workstations. Follow the instructions in [Import Custom Microsoft Active Directory](enable-identity-modules.md#import-custom-microsoft-active-directory) to ensure you have the correct configurations for Unmanaged Active Directory.

### Problem: Leostream Gateway module enablement failure due to Leostream API unauthorized error code (401)
<a name="problem-leostream-gateway-module-enablement-failure-due-to-leostream-api-unauthorized-error-code-401"></a>

During deployment, the Leostream Gateway module may occasionally receive a 401 (Unauthorized) response from the Leostream Broker cluster API. This occurs despite the system properly generating new authentication tokens and implementing standard retry mechanisms. This causes the deployment of the Leostream Gateway module to fail.

Our engineering team has confirmed this is an issue within the Leostream system and is actively working with Leostream to implement a permanent resolution.

#### Resolution
<a name="resolution-8"></a>

If you encounter this API authentication issue during deployment, please follow these steps:

1. Disable the affected Leostream Gateway module instance via Modular Cloud Studio UI

1. Wait until the Leostream Gateway module disables — If you encounter a disablement failure, follow steps below

1. Redeploy the module

 **Note:** In rare instances where module deletion is incomplete via the standard interface, use the CloudFormation console to complete the process:

1. Navigate to the CloudFormation console

1. Locate and select the relevant stack

1. Choose the "Delete" option from the Actions menu

1. If prompted about deletion failures for custom resources, you may safely ignore deleting those to proceed removing the stack

### Problem: Building the AMI of Leostream Broker or Leostream Gateway in non-USA regions sometimes results in connection issues that rollback the stack
<a name="problem-building-the-ami-of-leostream-broker-or-leostream-gateway-in-non-usa-regions-sometimes-results-in-connection-issues-that-rollback-the-stack"></a>

AMI builds for Leostream Broker and Gateway EC2 instances occasionally fail in non-US regions due to connectivity issues with Leostream’s hosted servers. These failures typically manifest as connection timeouts (HTTP 522 errors) or end-of-file errors when downloading package installers, often occurring during off-peak hours, and result in CloudFormation stack rollbacks.

#### Resolution
<a name="resolution-9"></a>

Disable the failed module from MCS UI, retry enabling the module again.
