---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeFieldIndexes.html
---

# DescribeFieldIndexes
<a name="API_DescribeFieldIndexes"></a>

Returns a list of field indexes discovered in log data. By default, the response includes the `DEFAULT`, `CUSTOM`, and `INACTIVE` index categories. To return indexes from other categories, use the `indexCategories` parameter.

For more information about field index policies, see [PutIndexPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutIndexPolicy.html).

## Request Syntax
<a name="API_DescribeFieldIndexes_RequestSyntax"></a>

```
{
   "indexCategories": [ "{{string}}" ],
   "logGroupIdentifiers": [ "{{string}}" ],
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeFieldIndexes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [indexCategories](#API_DescribeFieldIndexes_RequestSyntax) **   <a name="CWL-DescribeFieldIndexes-request-indexCategories"></a>
The index categories to return. The following values are supported:
+  `DEFAULT`: Fields that CloudWatch Logs indexes by default. Examples include `@logStream` and `@data_format`.
+  `CUSTOM`: Fields that you added manually to the field index policy. CloudWatch Logs always indexes these fields. These fields count toward the quota of 20 fields for each log group.
+  `AUTO`: Fields that CloudWatch Logs indexes automatically based on your query patterns and usage. These fields do not count toward the field index quota. CloudWatch Logs might update these fields based on changes in your query patterns. To keep a field indexed permanently, add it to an account-level or log-group level field index policy.
+  `INACTIVE`: Fields that CloudWatch Logs indexed before but does not index now. This happens if you remove a field from the field index policy or if CloudWatch Logs automatically selects a different field based on your queries.
If you omit this parameter, the response includes the `DEFAULT`, `CUSTOM`, and `INACTIVE` categories.
For more information about automatically indexed fields and using the `AUTO` category, see [Automatically indexed fields](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing-Automatic.html).
Type: Array of strings
Array Members: Maximum number of 4 items.
Valid Values: `DEFAULT | CUSTOM | AUTO | INACTIVE`
Required: No

 ** [logGroupIdentifiers](#API_DescribeFieldIndexes_RequestSyntax) **   <a name="CWL-DescribeFieldIndexes-request-logGroupIdentifiers"></a>
An array containing the names or ARNs of the log groups that you want to retrieve field indexes for.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w#+=/:,.@-]*`
Required: Yes

 ** [nextToken](#API_DescribeFieldIndexes_RequestSyntax) **   <a name="CWL-DescribeFieldIndexes-request-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_DescribeFieldIndexes_ResponseSyntax"></a>

```
{
   "fieldIndexes": [
      {
         "fieldIndexName": "string",
         "firstEventTime": number,
         "indexCategory": "string",
         "lastEventTime": number,
         "lastScanTime": number,
         "logGroupIdentifier": "string",
         "type": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeFieldIndexes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [fieldIndexes](#API_DescribeFieldIndexes_ResponseSyntax) **   <a name="CWL-DescribeFieldIndexes-response-fieldIndexes"></a>
An array containing the field index information.
Type: Array of [FieldIndex](API_FieldIndex.md) objects

 ** [nextToken](#API_DescribeFieldIndexes_ResponseSyntax) **   <a name="CWL-DescribeFieldIndexes-response-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_DescribeFieldIndexes_Errors"></a>

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

## See Also
<a name="API_DescribeFieldIndexes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/DescribeFieldIndexes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/DescribeFieldIndexes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/DescribeFieldIndexes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/DescribeFieldIndexes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/DescribeFieldIndexes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/DescribeFieldIndexes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/DescribeFieldIndexes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/DescribeFieldIndexes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/DescribeFieldIndexes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/DescribeFieldIndexes)
