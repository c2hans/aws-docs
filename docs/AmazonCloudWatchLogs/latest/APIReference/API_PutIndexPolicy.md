---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutIndexPolicy.html
---

# PutIndexPolicy
<a name="API_PutIndexPolicy"></a>

Creates or updates a *field index policy* for the specified log group. Only log groups in the Standard log class support field index policies. For more information about log classes, see [Log classes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html).

You can use field index policies to create *field indexes* on fields found in log events in the log group. Creating field indexes speeds up and lowers the costs for CloudWatch Logs Insights queries that reference those field indexes, because these queries attempt to skip the processing of log events that are known to not match the indexed field. Good fields to index are fields that you often need to query for and fields or values that match only a small fraction of the total log events. Common examples of indexes include request ID, session ID, userID, and instance IDs. For more information, see [Create field indexes to improve query performance and reduce costs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing.html).

You can configure indexed fields as *facets* to enable interactive exploration and filtering of your logs in the CloudWatch Logs Insights console. Facets allow you to view value distributions and counts for indexed fields without running queries. When you create a field index, you can optionally set it as a facet to enable this interactive analysis capability. For more information, see [Use facets to group and explore logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Facets.html).

To find the fields that are in your log group events, use the [GetLogGroupFields](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogGroupFields.html) operation.

For example, suppose you have created a field index for `requestId`. Then, any CloudWatch Logs Insights query on that log group that includes `requestId = value ` or `requestId IN [value, value, ...]` will process fewer log events to reduce costs, and have improved performance.

CloudWatch Logs provides default field indexes for all log groups in the Standard log class. Default field indexes are automatically available for the following fields:
+  `@logStream`
+  `@aws.region`
+  `@aws.account`
+  `@source.log`
+  `traceId`

Default field indexes are in addition to any custom field indexes you define within your policy. Default field indexes are not counted towards your field index quota.

Each index policy has the following quotas and restrictions:
+ As many as 20 fields can be included in the policy.
+ Each field name can include as many as 100 characters.

Matches of log events to the names of indexed fields are case-sensitive. For example, a field index of `RequestId` won't match a log event containing `requestId`.

Log group-level field index policies created with `PutIndexPolicy` override account-level field index policies created with [PutAccountPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutAccountPolicy.html) that apply to log groups. If you use `PutIndexPolicy` to create a field index policy for a log group, that log group uses only that policy for log group-level indexing, including any facet configurations. The log group ignores any account-wide field index policy that applies to log groups, but data source-based account policies may still apply.

## Request Syntax
<a name="API_PutIndexPolicy_RequestSyntax"></a>

```
{
   "logGroupIdentifier": "{{string}}",
   "policyDocument": "{{string}}"
}
```

## Request Parameters
<a name="API_PutIndexPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [logGroupIdentifier](#API_PutIndexPolicy_RequestSyntax) **   <a name="CWL-PutIndexPolicy-request-logGroupIdentifier"></a>
Specify either the log group name or log group ARN to apply this field index policy to. If you specify an ARN, use the format arn:aws:logs:*region*:*account-id*:log-group:*log\_group\_name* Don't include an \* at the end.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w#+=/:,.@-]*`
Required: Yes

 ** [policyDocument](#API_PutIndexPolicy_RequestSyntax) **   <a name="CWL-PutIndexPolicy-request-policyDocument"></a>
The index policy document, in JSON format. The following is an example of an index policy document that creates indexes with different types.
 `"policyDocument": "{"Fields": [ "TransactionId" ], "FieldsV2": {"RequestId": {"type": "FIELD_INDEX"}, "APIName": {"type": "FACET"}, "StatusCode": {"type": "FACET"}}}"`
You can use `FieldsV2` to specify the type for each field. Supported types are `FIELD_INDEX` and `FACET`. Field names within `Fields` and `FieldsV2` must be mutually exclusive.
The policy document must include at least one field index. For more information about the fields that can be included and other restrictions, see [Field index syntax and quotas](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing-Syntax.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: Yes

## Response Syntax
<a name="API_PutIndexPolicy_ResponseSyntax"></a>

```
{
   "indexPolicy": {
      "lastUpdateTime": number,
      "logGroupIdentifier": "string",
      "policyDocument": "string",
      "policyName": "string",
      "source": "string"
   }
}
```

## Response Elements
<a name="API_PutIndexPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [indexPolicy](#API_PutIndexPolicy_ResponseSyntax) **   <a name="CWL-PutIndexPolicy-response-indexPolicy"></a>
The index policy that you just created or updated.
Type: [IndexPolicy](API_IndexPolicy.md) object

## Errors
<a name="API_PutIndexPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** LimitExceededException **
You have reached the maximum number of resources that can be created.
HTTP Status Code: 400

 ** OperationAbortedException **
Multiple concurrent requests to update the same resource were in conflict.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

## Examples
<a name="API_PutIndexPolicy_Examples"></a>

### Create index policy for a log group
<a name="API_PutIndexPolicy_Example_1"></a>

The following example creates an index policy that indexes two fields, `RequestId` and `TransactionId`.

#### Sample Request
<a name="API_PutIndexPolicy_Example_1_Request"></a>

```
{
    "logGroupIdentifier": "service-logs",
    "policyDocument": {
        "Fields": ["RequestId", "TransactionId"]
    }
}
```

## See Also
<a name="API_PutIndexPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/PutIndexPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/PutIndexPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/PutIndexPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/PutIndexPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/PutIndexPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/PutIndexPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/PutIndexPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/PutIndexPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/PutIndexPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/PutIndexPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
