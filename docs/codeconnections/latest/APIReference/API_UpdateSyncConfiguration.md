---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_UpdateSyncConfiguration.html
---

# UpdateSyncConfiguration
<a name="API_UpdateSyncConfiguration"></a>

Updates the sync configuration for your connection and a specified external Git repository.

## Request Syntax
<a name="API_UpdateSyncConfiguration_RequestSyntax"></a>

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
<a name="API_UpdateSyncConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Branch](#API_UpdateSyncConfiguration_RequestSyntax) **   <a name="codeconnections-UpdateSyncConfiguration-request-Branch"></a>
The branch for the sync configuration to be updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^.*$`
Required: No

 ** [ConfigFile](#API_UpdateSyncConfiguration_RequestSyntax) **   <a name="codeconnections-UpdateSyncConfiguration-request-ConfigFile"></a>
The configuration file for the sync configuration to be updated.
Type: String
Required: No

 ** [PublishDeploymentStatus](#API_UpdateSyncConfiguration_RequestSyntax) **   <a name="codeconnections-UpdateSyncConfiguration-request-PublishDeploymentStatus"></a>
Whether to enable or disable publishing of deployment status to source providers.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [PullRequestComment](#API_UpdateSyncConfiguration_RequestSyntax) **   <a name="codeconnections-UpdateSyncConfiguration-request-PullRequestComment"></a>
TA toggle that specifies whether to enable or disable pull request comments for the sync configuration to be updated.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [RepositoryLinkId](#API_UpdateSyncConfiguration_RequestSyntax) **   <a name="codeconnections-UpdateSyncConfiguration-request-RepositoryLinkId"></a>
The ID of the repository link for the sync configuration to be updated.
Type: String
Pattern: `^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$`
Required: No

 ** [ResourceName](#API_UpdateSyncConfiguration_RequestSyntax) **   <a name="codeconnections-UpdateSyncConfiguration-request-ResourceName"></a>
The name of the AWS resource for the sync configuration to be updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[0-9A-Za-z]+[0-9A-Za-z_\\-]*$`
Required: Yes

 ** [RoleArn](#API_UpdateSyncConfiguration_RequestSyntax) **   <a name="codeconnections-UpdateSyncConfiguration-request-RoleArn"></a>
The ARN of the IAM role for the sync configuration to be updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:aws(-[\w]+)*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** [SyncType](#API_UpdateSyncConfiguration_RequestSyntax) **   <a name="codeconnections-UpdateSyncConfiguration-request-SyncType"></a>
The sync type for the sync configuration to be updated.
Type: String
Valid Values: `CFN_STACK_SYNC`
Required: Yes

 ** [TriggerResourceUpdateOn](#API_UpdateSyncConfiguration_RequestSyntax) **   <a name="codeconnections-UpdateSyncConfiguration-request-TriggerResourceUpdateOn"></a>
When to trigger Git sync to begin the stack update.
Type: String
Valid Values: `ANY_CHANGE | FILE_CHANGE`
Required: No

## Response Syntax
<a name="API_UpdateSyncConfiguration_ResponseSyntax"></a>

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
<a name="API_UpdateSyncConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SyncConfiguration](#API_UpdateSyncConfiguration_ResponseSyntax) **   <a name="codeconnections-UpdateSyncConfiguration-response-SyncConfiguration"></a>
The information returned for the sync configuration to be updated.
Type: [SyncConfiguration](API_SyncConfiguration.md) object

## Errors
<a name="API_UpdateSyncConfiguration_Errors"></a>

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

 ** ResourceNotFoundException **
Resource not found. Verify the connection resource ARN and try again.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** UpdateOutOfSyncException **
The update is out of sync. Try syncing again.
HTTP Status Code: 400

## See Also
<a name="API_UpdateSyncConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeconnections-2023-12-01/UpdateSyncConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeconnections-2023-12-01/UpdateSyncConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/UpdateSyncConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeconnections-2023-12-01/UpdateSyncConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/UpdateSyncConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeconnections-2023-12-01/UpdateSyncConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeconnections-2023-12-01/UpdateSyncConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeconnections-2023-12-01/UpdateSyncConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeconnections-2023-12-01/UpdateSyncConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/UpdateSyncConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeConnections. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeconnections` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
