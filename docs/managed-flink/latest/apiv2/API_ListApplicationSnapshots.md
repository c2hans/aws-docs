---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ListApplicationSnapshots.html
---

# ListApplicationSnapshots
<a name="API_ListApplicationSnapshots"></a>

Lists information about the current application snapshots.

## Request Syntax
<a name="API_ListApplicationSnapshots_RequestSyntax"></a>

```
{
   "ApplicationName": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListApplicationSnapshots_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationName](#API_ListApplicationSnapshots_RequestSyntax) **   <a name="APIReference-ListApplicationSnapshots-request-ApplicationName"></a>
The name of an existing application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [Limit](#API_ListApplicationSnapshots_RequestSyntax) **   <a name="APIReference-ListApplicationSnapshots-request-Limit"></a>
The maximum number of application snapshots to list.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListApplicationSnapshots_RequestSyntax) **   <a name="APIReference-ListApplicationSnapshots-request-NextToken"></a>
Use this parameter if you receive a `NextToken` response in a previous request that indicates that there is more output available. Set it to the value of the previous call's `NextToken` response to indicate where the output should continue from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## Response Syntax
<a name="API_ListApplicationSnapshots_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "SnapshotSummaries": [
      {
         "ApplicationEncryptionConfigurationDescription": {
            "KeyId": "string",
            "KeyType": "string"
         },
         "ApplicationVersionId": number,
         "RuntimeEnvironment": "string",
         "SnapshotCreationTimestamp": number,
         "SnapshotName": "string",
         "SnapshotStatus": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListApplicationSnapshots_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListApplicationSnapshots_ResponseSyntax) **   <a name="APIReference-ListApplicationSnapshots-response-NextToken"></a>
The token for the next set of results, or `null` if there are no additional results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.

 ** [SnapshotSummaries](#API_ListApplicationSnapshots_ResponseSyntax) **   <a name="APIReference-ListApplicationSnapshots-response-SnapshotSummaries"></a>
A collection of objects containing information about the application snapshots.
Type: Array of [SnapshotDetails](API_SnapshotDetails.md) objects

## Errors
<a name="API_ListApplicationSnapshots_Errors"></a>

 ** InvalidArgumentException **
The specified input parameter value is not valid.
HTTP Status Code: 400

 ** UnsupportedOperationException **
The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation.
HTTP Status Code: 400

## See Also
<a name="API_ListApplicationSnapshots_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/ListApplicationSnapshots)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/ListApplicationSnapshots)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ListApplicationSnapshots)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/ListApplicationSnapshots)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ListApplicationSnapshots)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/ListApplicationSnapshots)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/ListApplicationSnapshots)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/ListApplicationSnapshots)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/ListApplicationSnapshots)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ListApplicationSnapshots)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
