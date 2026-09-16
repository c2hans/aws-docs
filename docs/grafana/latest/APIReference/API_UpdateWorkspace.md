---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdateWorkspace.html
---

# UpdateWorkspace
<a name="API_UpdateWorkspace"></a>

Modifies an existing Amazon Managed Grafana workspace. If you use this operation and omit any optional parameters, the existing values of those parameters are not changed.

To modify the user authentication methods that the workspace uses, such as SAML or IAM Identity Center, use [UpdateWorkspaceAuthentication](https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdateWorkspaceAuthentication.html).

To modify which users in the workspace have the `Admin` and `Editor` Grafana roles, use [UpdatePermissions](https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdatePermissions.html).

## Request Syntax
<a name="API_UpdateWorkspace_RequestSyntax"></a>

```
PUT /workspaces/{{workspaceId}} HTTP/1.1
Content-type: application/json

{
   "accountAccessType": "{{string}}",
   "ipAddressType": "{{string}}",
   "networkAccessControl": {
      "prefixListIds": [ "{{string}}" ],
      "vpceIds": [ "{{string}}" ]
   },
   "organizationRoleName": "{{string}}",
   "permissionType": "{{string}}",
   "removeNetworkAccessConfiguration": {{boolean}},
   "removeVpcConfiguration": {{boolean}},
   "stackSetName": "{{string}}",
   "vpcConfiguration": {
      "securityGroupIds": [ "{{string}}" ],
      "subnetIds": [ "{{string}}" ]
   },
   "workspaceDataSources": [ "{{string}}" ],
   "workspaceDescription": "{{string}}",
   "workspaceName": "{{string}}",
   "workspaceNotificationDestinations": [ "{{string}}" ],
   "workspaceOrganizationalUnits": [ "{{string}}" ],
   "workspaceRoleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateWorkspace_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceId](#API_UpdateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-UpdateWorkspace-request-uri-workspaceId"></a>
The ID of the workspace to update.
Pattern: `g-[0-9a-f]{10}`
Required: Yes

## Request Body
<a name="API_UpdateWorkspace_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountAccessType](#API_UpdateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-UpdateWorkspace-request-accountAccessType"></a>
Specifies whether the workspace can access AWS resources in this AWS account only, or whether it can also access AWS resources in other accounts in the same organization. If you specify `ORGANIZATION`, you must specify which organizational units the workspace can access in the `workspaceOrganizationalUnits` parameter.
Type: String
Valid Values: `CURRENT_ACCOUNT | ORGANIZATION`
Required: No

 ** [ipAddressType](#API_UpdateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-UpdateWorkspace-request-ipAddressType"></a>
Specifies whether the workspace supports IPv4 only, or IPv4 and IPv6. Valid values are `IPv4` and `DualStack`. For more information about IP address types, see [Network access control](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-nac.html).
Type: String
Valid Values: `IPv4 | DualStack`
Required: No

 ** [networkAccessControl](#API_UpdateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-UpdateWorkspace-request-networkAccessControl"></a>
The configuration settings for network access to your workspace.
When this is configured, only listed IP addresses and VPC endpoints will be able to access your workspace. Standard Grafana authentication and authorization will still be required.
If this is not configured, or is removed, then all IP addresses and VPC endpoints will be allowed. Standard Grafana authentication and authorization will still be required.
Type: [NetworkAccessConfiguration](API_NetworkAccessConfiguration.md) object
Required: No

 ** [organizationRoleName](#API_UpdateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-UpdateWorkspace-request-organizationRoleName"></a>
The name of an IAM role that already exists to use to access resources through Organizations. This can only be used with a workspace that has the `permissionType` set to `CUSTOMER_MANAGED`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [permissionType](#API_UpdateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-UpdateWorkspace-request-permissionType"></a>
Use this parameter if you want to change a workspace from `SERVICE_MANAGED` to `CUSTOMER_MANAGED`. This allows you to manage the permissions that the workspace uses to access datasources and notification channels. If the workspace is in a member AWS account of an organization, and that account is not a delegated administrator account, and you want the workspace to access data sources in other AWS accounts in the organization, you must choose `CUSTOMER_MANAGED`.
If you specify this as `CUSTOMER_MANAGED`, you must also specify a `workspaceRoleArn` that the workspace will use for accessing AWS resources.
For more information on the role and permissions needed, see [Amazon Managed Grafana permissions and policies for AWS data sources and notification channels](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-manage-permissions.html)
Do not use this to convert a `CUSTOMER_MANAGED` workspace to `SERVICE_MANAGED`. Do not include this parameter if you want to leave the workspace as `SERVICE_MANAGED`.
You can convert a `CUSTOMER_MANAGED` workspace to `SERVICE_MANAGED` using the Amazon Managed Grafana console. For more information, see [Managing permissions for data sources and notification channels](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-datasource-and-notification.html).
Type: String
Valid Values: `CUSTOMER_MANAGED | SERVICE_MANAGED`
Required: No

 ** [removeNetworkAccessConfiguration](#API_UpdateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-UpdateWorkspace-request-removeNetworkAccessConfiguration"></a>
Whether to remove the network access configuration from the workspace.
Setting this to `true` and providing a `networkAccessControl` to set will return an error.
If you remove this configuration by setting this to `true`, then all IP addresses and VPC endpoints will be allowed. Standard Grafana authentication and authorization will still be required.
Type: Boolean
Required: No

 ** [removeVpcConfiguration](#API_UpdateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-UpdateWorkspace-request-removeVpcConfiguration"></a>
Whether to remove the VPC configuration from the workspace.
Setting this to `true` and providing a `vpcConfiguration` to set will return an error.
Type: Boolean
Required: No

 ** [stackSetName](#API_UpdateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-UpdateWorkspace-request-stackSetName"></a>
The name of the AWS CloudFormation stack set to use to generate IAM roles to be used for this workspace.
Type: String
Required: No

 ** [vpcConfiguration](#API_UpdateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-UpdateWorkspace-request-vpcConfiguration"></a>
The configuration settings for an Amazon VPC that contains data sources for your Grafana workspace to connect to.
Type: [VpcConfiguration](API_VpcConfiguration.md) object
Required: No

 ** [workspaceDataSources](#API_UpdateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-UpdateWorkspace-request-workspaceDataSources"></a>
This parameter is for internal use only, and should not be used.
Type: Array of strings
Valid Values: `AMAZON_OPENSEARCH_SERVICE | CLOUDWATCH | PROMETHEUS | XRAY | TIMESTREAM | SITEWISE | ATHENA | REDSHIFT | TWINMAKER`
Required: No

 ** [workspaceDescription](#API_UpdateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-UpdateWorkspace-request-workspaceDescription"></a>
A description for the workspace. This is used only to help you identify this workspace.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [workspaceName](#API_UpdateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-UpdateWorkspace-request-workspaceName"></a>
A new name for the workspace to update.
Type: String
Pattern: `[a-zA-Z0-9-._~]{1,255}`
Required: No

 ** [workspaceNotificationDestinations](#API_UpdateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-UpdateWorkspace-request-workspaceNotificationDestinations"></a>
Specify the AWS notification channels that you plan to use in this workspace. Specifying these data sources here enables Amazon Managed Grafana to create IAM roles and permissions that allow Amazon Managed Grafana to use these channels.
Type: Array of strings
Valid Values: `SNS`
Required: No

 ** [workspaceOrganizationalUnits](#API_UpdateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-UpdateWorkspace-request-workspaceOrganizationalUnits"></a>
Specifies the organizational units that this workspace is allowed to use data sources from, if this workspace is in an account that is part of an organization.
Type: Array of strings
Required: No

 ** [workspaceRoleArn](#API_UpdateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-UpdateWorkspace-request-workspaceRoleArn"></a>
Specifies an IAM role that grants permissions to AWS resources that the workspace accesses, such as data sources and notification channels. If this workspace has `permissionType` `CUSTOMER_MANAGED`, then this role is required.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_UpdateWorkspace_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "workspace": {
      "accountAccessType": "string",
      "authentication": {
         "providers": [ "string" ],
         "samlConfigurationStatus": "string"
      },
      "created": number,
      "dataSources": [ "string" ],
      "degradedWorkspaceReason": "string",
      "description": "string",
      "endpoint": "string",
      "freeTrialConsumed": boolean,
      "freeTrialExpiration": number,
      "grafanaToken": "string",
      "grafanaVersion": "string",
      "id": "string",
      "ipAddressType": "string",
      "kmsKeyId": "string",
      "licenseExpiration": number,
      "licenseType": "string",
      "modified": number,
      "name": "string",
      "networkAccessControl": {
         "prefixListIds": [ "string" ],
         "vpceIds": [ "string" ]
      },
      "notificationDestinations": [ "string" ],
      "organizationalUnits": [ "string" ],
      "organizationRoleName": "string",
      "permissionType": "string",
      "stackSetName": "string",
      "status": "string",
      "tags": {
         "string" : "string"
      },
      "vpcConfiguration": {
         "securityGroupIds": [ "string" ],
         "subnetIds": [ "string" ]
      },
      "workspaceRoleArn": "string"
   }
}
```

## Response Elements
<a name="API_UpdateWorkspace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [workspace](#API_UpdateWorkspace_ResponseSyntax) **   <a name="ManagedGrafana-UpdateWorkspace-response-workspace"></a>
A structure containing data about the workspace that was created.
Type: [WorkspaceDescription](API_WorkspaceDescription.md) object

## Errors
<a name="API_UpdateWorkspace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ConflictException **
A resource was in an inconsistent state during an update or a deletion.
 ** message **
A description of the error.
 ** resourceId **
The ID of the resource that is associated with the error.
 ** resourceType **
The type of the resource that is associated with the error.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error while processing the request. Retry the request.
 ** message **
A description of the error.
 ** retryAfterSeconds **
How long to wait before you retry this operation.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist.
 ** message **
The value of a parameter in the request caused an error.
 ** resourceId **
The ID of the resource that is associated with the error.
 ** resourceType **
The type of the resource that is associated with the error.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because of request throttling. Retry the request.
 ** message **
A description of the error.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The value of a parameter in the request caused an error.
 ** serviceCode **
The ID of the service that is associated with the error.
HTTP Status Code: 429

 ** ValidationException **
The value of a parameter in the request caused an error.
 ** fieldList **
A list of fields that might be associated with the error.
 ** message **
A description of the error.
 ** reason **
The reason that the operation failed.
HTTP Status Code: 400

## See Also
<a name="API_UpdateWorkspace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/grafana-2020-08-18/UpdateWorkspace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/grafana-2020-08-18/UpdateWorkspace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/UpdateWorkspace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/grafana-2020-08-18/UpdateWorkspace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/UpdateWorkspace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/grafana-2020-08-18/UpdateWorkspace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/grafana-2020-08-18/UpdateWorkspace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/grafana-2020-08-18/UpdateWorkspace)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/grafana-2020-08-18/UpdateWorkspace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/UpdateWorkspace)
