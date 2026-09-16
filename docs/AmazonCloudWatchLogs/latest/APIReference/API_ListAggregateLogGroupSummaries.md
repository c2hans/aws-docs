---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListAggregateLogGroupSummaries.html
---

# ListAggregateLogGroupSummaries
<a name="API_ListAggregateLogGroupSummaries"></a>

Returns an aggregate summary of all log groups in the Region grouped by specified data source characteristics. Supports optional filtering by log group class, name patterns, and data sources. If you perform this action in a monitoring account, you can also return aggregated summaries of log groups from source accounts that are linked to the monitoring account. For more information about using cross-account observability to set up monitoring accounts and source accounts, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html).

The operation aggregates log groups by data source name and type and optionally format, providing counts of log groups that share these characteristics. The operation paginates results. By default, it returns up to 50 results and includes a token to retrieve more results.

## Request Syntax
<a name="API_ListAggregateLogGroupSummaries_RequestSyntax"></a>

```
{
   "accountIdentifiers": [ "{{string}}" ],
   "dataSources": [
      {
         "name": "{{string}}",
         "type": "{{string}}"
      }
   ],
   "groupBy": "{{string}}",
   "includeLinkedAccounts": {{boolean}},
   "limit": {{number}},
   "logGroupClass": "{{string}}",
   "logGroupNamePattern": "{{string}}",
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAggregateLogGroupSummaries_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [accountIdentifiers](#API_ListAggregateLogGroupSummaries_RequestSyntax) **   <a name="CWL-ListAggregateLogGroupSummaries-request-accountIdentifiers"></a>
When `includeLinkedAccounts` is set to `true`, use this parameter to specify the list of accounts to search. You can specify as many as 20 account IDs in the array.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

 ** [dataSources](#API_ListAggregateLogGroupSummaries_RequestSyntax) **   <a name="CWL-ListAggregateLogGroupSummaries-request-dataSources"></a>
Filters the results by data source characteristics to include only log groups associated with the specified data sources.
Type: Array of [DataSourceFilter](API_DataSourceFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** [groupBy](#API_ListAggregateLogGroupSummaries_RequestSyntax) **   <a name="CWL-ListAggregateLogGroupSummaries-request-groupBy"></a>
Specifies how to group the log groups in the summary.
Type: String
Valid Values: `DATA_SOURCE_NAME_TYPE_AND_FORMAT | DATA_SOURCE_NAME_AND_TYPE`
Required: Yes

 ** [includeLinkedAccounts](#API_ListAggregateLogGroupSummaries_RequestSyntax) **   <a name="CWL-ListAggregateLogGroupSummaries-request-includeLinkedAccounts"></a>
If you are using a monitoring account, set this to `true` to have the operation return log groups in the accounts listed in `accountIdentifiers`.
If this parameter is set to `true` and `accountIdentifiers` contains a null value, the operation returns all log groups in the monitoring account and all log groups in all source accounts that are linked to the monitoring account.
The default for this parameter is `false`.
Type: Boolean
Required: No

 ** [limit](#API_ListAggregateLogGroupSummaries_RequestSyntax) **   <a name="CWL-ListAggregateLogGroupSummaries-request-limit"></a>
The maximum number of aggregated summaries to return. If you omit this parameter, the default is up to 50 aggregated summaries.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [logGroupClass](#API_ListAggregateLogGroupSummaries_RequestSyntax) **   <a name="CWL-ListAggregateLogGroupSummaries-request-logGroupClass"></a>
Filters the results by log group class to include only log groups of the specified class.
Type: String
Valid Values: `STANDARD | INFREQUENT_ACCESS | DELIVERY`
Required: No

 ** [logGroupNamePattern](#API_ListAggregateLogGroupSummaries_RequestSyntax) **   <a name="CWL-ListAggregateLogGroupSummaries-request-logGroupNamePattern"></a>
Use this parameter to limit the returned log groups to only those with names that match the pattern that you specify. This parameter is a regular expression that can match prefixes and substrings, and supports wildcard matching and matching multiple patterns, as in the following examples.
+ Use `^` to match log group names by prefix.
+ For a substring match, specify the string to match. All matches are case sensitive
+ To match multiple patterns, separate them with a `|` as in the example `^/aws/lambda|discovery`
You can specify as many as five different regular expression patterns in this field, each of which must be between 3 and 24 characters. You can include the `^` symbol as many as five times, and include the `|` symbol as many as four times.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 129.
Pattern: `(\^?[\.\-_\/#A-Za-z0-9]{3,24})(\|\^?[\.\-_\/#A-Za-z0-9]{3,24}){0,4}`
Required: No

 ** [nextToken](#API_ListAggregateLogGroupSummaries_RequestSyntax) **   <a name="CWL-ListAggregateLogGroupSummaries-request-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_ListAggregateLogGroupSummaries_ResponseSyntax"></a>

```
{
   "aggregateLogGroupSummaries": [
      {
         "groupingIdentifiers": [
            {
               "key": "string",
               "value": "string"
            }
         ],
         "logGroupCount": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAggregateLogGroupSummaries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [aggregateLogGroupSummaries](#API_ListAggregateLogGroupSummaries_ResponseSyntax) **   <a name="CWL-ListAggregateLogGroupSummaries-response-aggregateLogGroupSummaries"></a>
The list of aggregate log group summaries grouped by the specified data source characteristics.
Type: Array of [AggregateLogGroupSummary](API_AggregateLogGroupSummary.md) objects

 ** [nextToken](#API_ListAggregateLogGroupSummaries_ResponseSyntax) **   <a name="CWL-ListAggregateLogGroupSummaries-response-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_ListAggregateLogGroupSummaries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

 ** ValidationException **
One of the parameters for the request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListAggregateLogGroupSummaries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/ListAggregateLogGroupSummaries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/ListAggregateLogGroupSummaries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/ListAggregateLogGroupSummaries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/ListAggregateLogGroupSummaries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/ListAggregateLogGroupSummaries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/ListAggregateLogGroupSummaries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/ListAggregateLogGroupSummaries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/ListAggregateLogGroupSummaries)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/ListAggregateLogGroupSummaries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/ListAggregateLogGroupSummaries)
