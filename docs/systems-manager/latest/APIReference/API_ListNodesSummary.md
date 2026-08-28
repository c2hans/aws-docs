---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListNodesSummary.html
---

# ListNodesSummary
<a name="API_ListNodesSummary"></a>

Generates a summary of managed instance/node metadata based on the filters and aggregators you specify. Results are grouped by the input aggregator you specify.

## Request Syntax
<a name="API_ListNodesSummary_RequestSyntax"></a>

```
{
   "Aggregators": [
      {
         "Aggregators": [
            "NodeAggregator"
         ],
         "AggregatorType": "{{string}}",
         "AttributeName": "{{string}}",
         "TypeName": "{{string}}"
      }
   ],
   "Filters": [
      {
         "Key": "{{string}}",
         "Type": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SyncName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListNodesSummary_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Aggregators](#API_ListNodesSummary_RequestSyntax) **   <a name="systemsmanager-ListNodesSummary-request-Aggregators"></a>
Specify one or more aggregators to return a count of managed nodes that match that expression. For example, a count of managed nodes by operating system.
Type: Array of [NodeAggregator](API_NodeAggregator.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: Yes

 ** [Filters](#API_ListNodesSummary_RequestSyntax) **   <a name="systemsmanager-ListNodesSummary-request-Filters"></a>
One or more filters. Use a filter to generate a summary that matches your specified filter criteria.
Type: Array of [NodeFilter](API_NodeFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** [MaxResults](#API_ListNodesSummary_RequestSyntax) **   <a name="systemsmanager-ListNodesSummary-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListNodesSummary_RequestSyntax) **   <a name="systemsmanager-ListNodesSummary-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.) The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: String
Required: No

 ** [SyncName](#API_ListNodesSummary_RequestSyntax) **   <a name="systemsmanager-ListNodesSummary-request-SyncName"></a>
The name of the AWS managed resource data sync to retrieve information about.
For cross-account/cross-Region configurations, this parameter is required, and the name of the supported resource data sync is `AWS-QuickSetup-ManagedNode`.
For single account/single-Region configurations, the parameter is not required.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## Response Syntax
<a name="API_ListNodesSummary_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Summary": [
      {
         "string" : "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListNodesSummary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListNodesSummary_ResponseSyntax) **   <a name="systemsmanager-ListNodesSummary-response-NextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

 ** [Summary](#API_ListNodesSummary_ResponseSyntax) **   <a name="systemsmanager-ListNodesSummary-response-Summary"></a>
A collection of objects reporting information about your managed nodes, such as the count of nodes by operating system.
Type: Array of string to string maps
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Map Entries: Minimum number of 0 items. Maximum number of 3 items.
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Value Length Constraints: Minimum length of 0. Maximum length of 4096.

## Errors
<a name="API_ListNodesSummary_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidAggregatorException **
The specified aggregator isn't valid for the group type. Verify that the aggregator you provided is supported.
HTTP Status Code: 400

 ** InvalidFilter **
The filter name isn't valid. Verify that you entered the correct name and try again.
HTTP Status Code: 400

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

 ** ResourceDataSyncNotFoundException **
The specified sync name wasn't found.
HTTP Status Code: 400

 ** UnsupportedOperationException **
This operation is not supported for the current account. You must first enable the Systems Manager integrated experience in your account.
HTTP Status Code: 400

## Examples
<a name="API_ListNodesSummary_Examples"></a>

### Example
<a name="API_ListNodesSummary_Example_1"></a>

This example illustrates one usage of ListNodesSummary.

#### Sample Request
<a name="API_ListNodesSummary_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.ListNodesSummary
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20241119/25T150301Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240325/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 197

{
 "SyncName": "AWS-QuickSetup-ManagedNode",
 "Aggregators":
  [
    {"AggregatorType": "Count",
     "TypeName": "Instance",
     "AttributeName": "Region"}
  ],
  "Filters":
  [
    {"Key": "InstanceStatus",
     "Values":
      ["Active"],
     "Type": "Equal"}
  ],
  "MaxResults" : 2,
  "NextToken": "A9lT8CAxj9aDFRi+MNA---truncated---oFq08IEXAMPLE"
 }
```

### Example
<a name="API_ListNodesSummary_Example_2"></a>

This example illustrates one usage of ListNodesSummary.

#### Sample Response
<a name="API_ListNodesSummary_Example_2_Response"></a>

```
{
    "Summary": [
        {
            "Count": "26",
            "Region": "us-east-1"
        },
        {
            "Count": "7",
            "Region": "us-east-2"
        }
    ]
}
```

## See Also
<a name="API_ListNodesSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/ListNodesSummary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/ListNodesSummary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ListNodesSummary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/ListNodesSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ListNodesSummary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/ListNodesSummary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/ListNodesSummary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/ListNodesSummary)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/ListNodesSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ListNodesSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
