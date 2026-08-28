---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_CreateSyncConfiguration.html
---

# CreateSyncConfiguration
<a name="API_CreateSyncConfiguration"></a>

Creates a sync configuration which allows AWS to sync content from a Git repository to update a specified AWS resource. Parameters for the sync configuration are determined by the sync type.

## Request Syntax
<a name="API_CreateSyncConfiguration_RequestSyntax"></a>

```
{
   "Branch": "{{string}}",
   "ConfigFile": "{{string}}",
   "PublishDeploymentStatus": "{{string}}",
   "PullRequestComment": "{{string}}",
   "RepositoryLinkId": "{{string}}",
   "ResourceName": "{{string}}",
   "RoleArn": "{{string}}",
   "SyncType": "{{string}}",
   "TriggerResourceUpdateOn": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateSyncConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Branch](#API_CreateSyncConfiguration_RequestSyntax) **   <a name="codeconnections-CreateSyncConfiguration-request-Branch"></a>
The branch in the repository from which changes will be synced.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^.*$`
Required: Yes

 ** [ConfigFile](#API_CreateSyncConfiguration_RequestSyntax) **   <a name="codeconnections-CreateSyncConfiguration-request-ConfigFile"></a>
The file name of the configuration file that manages syncing between the connection and the repository. This configuration file is stored in the repository.
Type: String
Required: Yes

 ** [PublishDeploymentStatus](#API_CreateSyncConfiguration_RequestSyntax) **   <a name="codeconnections-CreateSyncConfiguration-request-PublishDeploymentStatus"></a>
Whether to enable or disable publishing of deployment status to source providers.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [PullRequestComment](#API_CreateSyncConfiguration_RequestSyntax) **   <a name="codeconnections-CreateSyncConfiguration-request-PullRequestComment"></a>
A toggle that specifies whether to enable or disable pull request comments for the sync configuration to be created.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [RepositoryLinkId](#API_CreateSyncConfiguration_RequestSyntax) **   <a name="codeconnections-CreateSyncConfiguration-request-RepositoryLinkId"></a>
The ID of the repository link created for the connection. A repository link allows Git sync to monitor and sync changes to files in a specified Git repository.
Type: String
Pattern: `^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$`
Required: Yes

 ** [ResourceName](#API_CreateSyncConfiguration_RequestSyntax) **   <a name="codeconnections-CreateSyncConfiguration-request-ResourceName"></a>
The name of the AWS resource (for example, a CloudFormation stack in the case of CFN\_STACK\_SYNC) that will be synchronized from the linked repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[0-9A-Za-z]+[0-9A-Za-z_\\-]*$`
Required: Yes

 ** [RoleArn](#API_CreateSyncConfiguration_RequestSyntax) **   <a name="codeconnections-CreateSyncConfiguration-request-RoleArn"></a>
The ARN of the IAM role that grants permission for AWS to use Git sync to update a given AWS resource on your behalf.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:aws(-[\w]+)*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [SyncType](#API_CreateSyncConfiguration_RequestSyntax) **   <a name="codeconnections-CreateSyncConfiguration-request-SyncType"></a>
The type of sync configuration.
Type: String
Valid Values: `CFN_STACK_SYNC`
Required: Yes

 ** [TriggerResourceUpdateOn](#API_CreateSyncConfiguration_RequestSyntax) **   <a name="codeconnections-CreateSyncConfiguration-request-TriggerResourceUpdateOn"></a>
When to trigger Git sync to begin the stack update.
Type: String
Valid Values: `ANY_CHANGE | FILE_CHANGE`
Required: No

## Response Syntax
<a name="API_CreateSyncConfiguration_ResponseSyntax"></a>

```
{
   "SyncConfiguration": {
      "Branch": "string",
      "ConfigFile": "string",
      "OwnerId": "string",
      "ProviderType": "string",
      "PublishDeploymentStatus": "string",
      "PullRequestComment": "string",
      "RepositoryLinkId": "string",
      "RepositoryName": "string",
      "ResourceName": "string",
      "RoleArn": "string",
      "SyncType": "string",
      "TriggerResourceUpdateOn": "string"
   }
}
```

## Response Elements
<a name="API_CreateSyncConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SyncConfiguration](#API_CreateSyncConfiguration_ResponseSyntax) **   <a name="codeconnections-CreateSyncConfiguration-response-SyncConfiguration"></a>
The created sync configuration for the connection. A sync configuration allows AWS to sync content from a Git repository to update a specified AWS resource.
Type: [SyncConfiguration](API_SyncConfiguration.md) object

## Errors
<a name="API_CreateSyncConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConcurrentModificationException **
Exception thrown as a result of concurrent modification to an application. For example, two individuals attempting to edit the same application at the same time.
HTTP Status Code: 400

 ** InternalServerException **
Received an internal server exception. Try again later.
HTTP Status Code: 400

 ** InvalidInputException **
The input is not valid. Verify that the action is typed correctly.
HTTP Status Code: 400

 ** LimitExceededException **
Exceeded the maximum limit for connections.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
Unable to create resource. Resource already exists.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

## See Also
<a name="API_CreateSyncConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeconnections-2023-12-01/CreateSyncConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeconnections-2023-12-01/CreateSyncConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/CreateSyncConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeconnections-2023-12-01/CreateSyncConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/CreateSyncConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeconnections-2023-12-01/CreateSyncConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeconnections-2023-12-01/CreateSyncConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeconnections-2023-12-01/CreateSyncConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeconnections-2023-12-01/CreateSyncConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/CreateSyncConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeConnections. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeconnections` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
