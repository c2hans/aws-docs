---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetSyncBlockerSummary.html
---

# GetSyncBlockerSummary
<a name="API_GetSyncBlockerSummary"></a>

Returns a list of the most recent sync blockers.

## Request Syntax
<a name="API_GetSyncBlockerSummary_RequestSyntax"></a>

```
{
   "ResourceName": "{{string}}",
   "SyncType": "{{string}}"
}
```

## Request Parameters
<a name="API_GetSyncBlockerSummary_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceName](#API_GetSyncBlockerSummary_RequestSyntax) **   <a name="codeconnections-GetSyncBlockerSummary-request-ResourceName"></a>
The name of the AWS resource currently blocked from automatically being synced from a Git repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[0-9A-Za-z]+[0-9A-Za-z_\\-]*$`
Required: Yes

 ** [SyncType](#API_GetSyncBlockerSummary_RequestSyntax) **   <a name="codeconnections-GetSyncBlockerSummary-request-SyncType"></a>
The sync type for the sync blocker summary.
Type: String
Valid Values: `CFN_STACK_SYNC`
Required: Yes

## Response Syntax
<a name="API_GetSyncBlockerSummary_ResponseSyntax"></a>

```
{
   "SyncBlockerSummary": {
      "LatestBlockers": [
         {
            "Contexts": [
               {
                  "Key": "string",
                  "Value": "string"
               }
            ],
            "CreatedAt": number,
            "CreatedReason": "string",
            "Id": "string",
            "ResolvedAt": number,
            "ResolvedReason": "string",
            "Status": "string",
            "Type": "string"
         }
      ],
      "ParentResourceName": "string",
      "ResourceName": "string"
   }
}
```

## Response Elements
<a name="API_GetSyncBlockerSummary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SyncBlockerSummary](#API_GetSyncBlockerSummary_ResponseSyntax) **   <a name="codeconnections-GetSyncBlockerSummary-response-SyncBlockerSummary"></a>
The list of sync blockers for a specified resource.
Type: [SyncBlockerSummary](API_SyncBlockerSummary.md) object

## Errors
<a name="API_GetSyncBlockerSummary_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
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

## See Also
<a name="API_GetSyncBlockerSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeconnections-2023-12-01/GetSyncBlockerSummary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeconnections-2023-12-01/GetSyncBlockerSummary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/GetSyncBlockerSummary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeconnections-2023-12-01/GetSyncBlockerSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/GetSyncBlockerSummary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeconnections-2023-12-01/GetSyncBlockerSummary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeconnections-2023-12-01/GetSyncBlockerSummary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeconnections-2023-12-01/GetSyncBlockerSummary)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeconnections-2023-12-01/GetSyncBlockerSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/GetSyncBlockerSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeConnections. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeconnections` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
