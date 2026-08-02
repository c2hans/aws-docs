---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_CreateWorkspace.html
---

# CreateWorkspace
<a name="API_CreateWorkspace"></a>

Creates a *workspace*. In a workspace, you can create Grafana dashboards and visualizations to analyze your metrics, logs, and traces. You don't have to build, package, or deploy any hardware to run the Grafana server.

Don't use `CreateWorkspace` to modify an existing workspace. Instead, use [UpdateWorkspace](https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdateWorkspace.html).

## Request Syntax
<a name="API_CreateWorkspace_RequestSyntax"></a>

```
POST /workspaces HTTP/1.1
Content-type: application/json

{
   "accountAccessType": "{{string}}",
   "authenticationProviders": [ "{{string}}" ],
   "clientToken": "{{string}}",
   "configuration": "{{string}}",
   "grafanaVersion": "{{string}}",
   "ipAddressType": "{{string}}",
   "kmsKeyId": "{{string}}",
   "networkAccessControl": {
      "prefixListIds": [ "{{string}}" ],
      "vpceIds": [ "{{string}}" ]
   },
   "organizationRoleName": "{{string}}",
   "permissionType": "{{string}}",
   "stackSetName": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
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
<a name="API_CreateWorkspace_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateWorkspace_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountAccessType](#API_CreateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspace-request-accountAccessType"></a>
Specifies whether the workspace can access AWS resources in this AWS account only, or whether it can also access AWS resources in other accounts in the same organization. If you specify `ORGANIZATION`, you must specify which organizational units the workspace can access in the `workspaceOrganizationalUnits` parameter.
Type: String
Valid Values: `CURRENT_ACCOUNT | ORGANIZATION`
Required: Yes

 ** [authenticationProviders](#API_CreateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspace-request-authenticationProviders"></a>
Specifies whether this workspace uses SAML 2.0, AWS IAM Identity Center, or both to authenticate users for using the Grafana console within a workspace. For more information, see [User authentication in Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/authentication-in-AMG.html).
Type: Array of strings
Valid Values: `AWS_SSO | SAML`
Required: Yes

 ** [clientToken](#API_CreateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspace-request-clientToken"></a>
A unique, case-sensitive, user-provided identifier to ensure the idempotency of the request.
Type: String
Pattern: `[!-~]{1,64}`
Required: No

 ** [configuration](#API_CreateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspace-request-configuration"></a>
The configuration string for the workspace that you create. For more information about the format and configuration options available, see [Working in your Grafana workspace](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-workspace.html).
Type: String
Length Constraints: Minimum length of 2. Maximum length of 65536.
Required: No

 ** [grafanaVersion](#API_CreateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspace-request-grafanaVersion"></a>
Specifies the version of Grafana to support in the new workspace. If not specified, defaults to the latest version (for example, 10.4).
To get a list of supported versions, use the `ListVersions` operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [ipAddressType](#API_CreateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspace-request-ipAddressType"></a>
Specifies whether the workspace supports IPv4 only, or IPv4 and IPv6. Valid values are `IPv4` and `DualStack`. For more information about IP address types, see [Network access control](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-nac.html).
Type: String
Valid Values: `IPv4 | DualStack`
Required: No

 ** [kmsKeyId](#API_CreateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspace-request-kmsKeyId"></a>
The ID or ARN of the AWS Key Management Service key to use for encrypting workspace data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]+`
Required: No

 ** [networkAccessControl](#API_CreateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspace-request-networkAccessControl"></a>
Configuration for network access to your workspace.
When this is configured, only listed IP addresses and VPC endpoints will be able to access your workspace. Standard Grafana authentication and authorization will still be required.
If this is not configured, or is removed, then all IP addresses and VPC endpoints will be allowed. Standard Grafana authentication and authorization will still be required.
Type: [NetworkAccessConfiguration](API_NetworkAccessConfiguration.md) object
Required: No

 ** [organizationRoleName](#API_CreateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspace-request-organizationRoleName"></a>
The name of an IAM role that already exists to use with Organizations to access AWS data sources and notification channels in other accounts in an organization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [permissionType](#API_CreateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspace-request-permissionType"></a>
When creating a workspace through the AWS API, CLI or AWS CloudFormation, you must manage IAM roles and provision the permissions that the workspace needs to use AWS data sources and notification channels.
You must also specify a `workspaceRoleArn` for a role that you will manage for the workspace to use when accessing those datasources and notification channels.
The ability for Amazon Managed Grafana to create and update IAM roles on behalf of the user is supported only in the Amazon Managed Grafana console, where this value may be set to `SERVICE_MANAGED`.
Use only the `CUSTOMER_MANAGED` permission type when creating a workspace with the API, CLI or AWS CloudFormation.
For more information, see [Amazon Managed Grafana permissions and policies for AWS data sources and notification channels](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-manage-permissions.html).
Type: String
Valid Values: `CUSTOMER_MANAGED | SERVICE_MANAGED`
Required: Yes

 ** [stackSetName](#API_CreateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspace-request-stackSetName"></a>
The name of the AWS CloudFormation stack set to use to generate IAM roles to be used for this workspace.
Type: String
Required: No

 ** [tags](#API_CreateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspace-request-tags"></a>
The list of tags associated with the workspace.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [vpcConfiguration](#API_CreateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspace-request-vpcConfiguration"></a>
The configuration settings for an Amazon VPC that contains data sources for your Grafana workspace to connect to.
Connecting to a private VPC is not yet available in the Asia Pacific (Seoul) Region (ap-northeast-2).
Type: [VpcConfiguration](API_VpcConfiguration.md) object
Required: No

 ** [workspaceDataSources](#API_CreateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspace-request-workspaceDataSources"></a>
This parameter is for internal use only, and should not be used.
Type: Array of strings
Valid Values: `AMAZON_OPENSEARCH_SERVICE | CLOUDWATCH | PROMETHEUS | XRAY | TIMESTREAM | SITEWISE | ATHENA | REDSHIFT | TWINMAKER`
Required: No

 ** [workspaceDescription](#API_CreateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspace-request-workspaceDescription"></a>
A description for the workspace. This is used only to help you identify this workspace.
Pattern: `^[\\p{L}\\p{Z}\\p{N}\\p{P}]{0,2048}$`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [workspaceName](#API_CreateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspace-request-workspaceName"></a>
The name for the workspace. It does not have to be unique.
Type: String
Pattern: `[a-zA-Z0-9-._~]{1,255}`
Required: No

 ** [workspaceNotificationDestinations](#API_CreateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspace-request-workspaceNotificationDestinations"></a>
Specify the AWS notification channels that you plan to use in this workspace. Specifying these data sources here enables Amazon Managed Grafana to create IAM roles and permissions that allow Amazon Managed Grafana to use these channels.
Type: Array of strings
Valid Values: `SNS`
Required: No

 ** [workspaceOrganizationalUnits](#API_CreateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspace-request-workspaceOrganizationalUnits"></a>
Specifies the organizational units that this workspace is allowed to use data sources from, if this workspace is in an account that is part of an organization.
Type: Array of strings
Required: No

 ** [workspaceRoleArn](#API_CreateWorkspace_RequestSyntax) **   <a name="ManagedGrafana-CreateWorkspace-request-workspaceRoleArn"></a>
Specified the IAM role that grants permissions to the AWS resources that the workspace will view data from, including both data sources and notification channels. You are responsible for managing the permissions for this role as new data sources or notification channels are added.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_CreateWorkspace_ResponseSyntax"></a>

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
<a name="API_CreateWorkspace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [workspace](#API_CreateWorkspace_ResponseSyntax) **   <a name="ManagedGrafana-CreateWorkspace-response-workspace"></a>
A structure containing data about the workspace that was created.
Type: [WorkspaceDescription](API_WorkspaceDescription.md) object

## Errors
<a name="API_CreateWorkspace_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
 ** message **
A description of the error.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** resourceId **
The ID of the resource that is associated with the error.
 ** resourceType **
The type of the resource that is associated with the error.
 ** serviceCode **
The value of a parameter in the request caused an error.
HTTP Status Code: 402

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
<a name="API_CreateWorkspace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/grafana-2020-08-18/CreateWorkspace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/grafana-2020-08-18/CreateWorkspace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/CreateWorkspace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/grafana-2020-08-18/CreateWorkspace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/CreateWorkspace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/grafana-2020-08-18/CreateWorkspace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/grafana-2020-08-18/CreateWorkspace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/grafana-2020-08-18/CreateWorkspace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/grafana-2020-08-18/CreateWorkspace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/CreateWorkspace)
