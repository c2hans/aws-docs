---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/step-6-create-module-intercommunication.html
---

# Step 6: Create module intercommunication
<a name="step-6-create-module-intercommunication"></a>

To facilitate a pattern known as dynamic dependency loading, the configuration data is stored on the Systems Manager Parameter Store so that it can be lazy-loaded exactly when it is needed by an MCS module.

The following is the structure of all parameters output by MCS:

```
/{deployment_id}/{module_type}/{component}
```
+  **deployment\_id** - This value is generated when MCS is first deployed and is configured on the Lambda function serving API requests. When deploying any module (including Third-Party Modules), the `deployment_id` is provided as a CloudFormation parameter. The `deployment_id` is always prefixed with `mcs-`.
+  **module\_type** - This value is the type of the module providing the output. The same type can be used by multiple mutually-exclusive modules that provide the same output such as AWS Managed Microsoft AD, compared to unmanaged Microsoft Active Directory.
+  **component** - The name of the component providing the output. There could be one or multiple paths as part of this value.

As an example, see the following Managed Active Directory module with its input and output parameters (created after completing the steps to [Create Third-Party Modules for MCS](create-third-party-modules-for-mcs.md)):
+ MCS Managed Active Directory module - inputs:

```
/{deployment_id}/Network/VpcId
/{deployment_id}/Network/PrivateSubnet1/AZ
/{deployment_id}/Network/PrivateSubnet1/SubnetID
/{deployment_id}/Network/PrivateSubnet2/AZ
/{deployment_id}/Network/PrivateSubnet2/SubnetID
```
+ MCS Managed Active Directory module - outputs:

```
/{deployment_id}/Identity/ActiveDirectoryId
/{deployment_id}/Identity/ActiveDirectoryServerIP1
/{deployment_id}/Identity/ActiveDirectoryServerIP2
/{deployment_id}/Identity/ActiveDirectoryDomainName
/{deployment_id}/Identity/ActiveDirectorySecretArn
/{deployment_id}/Identity/DefaultActiveDirectoryLoginCredentials
/{deployment_id}/Identity/StudioAdminDirectoryLoginCredentials
```

For more information on parameters, see the [Module parameters](module-parameters.md) section
