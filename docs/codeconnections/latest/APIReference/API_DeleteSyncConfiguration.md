---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_DeleteSyncConfiguration.html
---

# DeleteSyncConfiguration
<a name="API_DeleteSyncConfiguration"></a>

Deletes the sync configuration for a specified repository and connection.

## Request Syntax
<a name="API_DeleteSyncConfiguration_RequestSyntax"></a>

```
{
   "ResourceName": "{{string}}",
   "SyncType": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteSyncConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceName](#API_DeleteSyncConfiguration_RequestSyntax) **   <a name="codeconnections-DeleteSyncConfiguration-request-ResourceName"></a>
The name of the AWS resource associated with the sync configuration to be deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[0-9A-Za-z]+[0-9A-Za-z_\\-]*$`
Required: Yes

 ** [SyncType](#API_DeleteSyncConfiguration_RequestSyntax) **   <a name="codeconnections-DeleteSyncConfiguration-request-SyncType"></a>
The type of sync configuration to be deleted.
Type: String
Valid Values: `CFN_STACK_SYNC`
Required: Yes

## Response Elements
<a name="API_DeleteSyncConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteSyncConfiguration_Errors"></a>

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

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

## See Also
<a name="API_DeleteSyncConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeconnections-2023-12-01/DeleteSyncConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeconnections-2023-12-01/DeleteSyncConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/DeleteSyncConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeconnections-2023-12-01/DeleteSyncConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/DeleteSyncConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeconnections-2023-12-01/DeleteSyncConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeconnections-2023-12-01/DeleteSyncConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeconnections-2023-12-01/DeleteSyncConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeconnections-2023-12-01/DeleteSyncConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/DeleteSyncConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeConnections. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeconnections` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
