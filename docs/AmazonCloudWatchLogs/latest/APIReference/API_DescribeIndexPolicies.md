---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeIndexPolicies.html
---

# DescribeIndexPolicies
<a name="API_DescribeIndexPolicies"></a>

Returns the field index policies of the specified log group. For more information about field index policies, see [PutIndexPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutIndexPolicy.html).

If a specified log group has a log-group level index policy, that policy is returned by this operation.

If a specified log group doesn't have a log-group level index policy, but an account-wide index policy applies to it, that account-wide policy is returned by this operation.

To find information about only account-level policies, use [DescribeAccountPolicies](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeAccountPolicies.html) instead.

## Request Syntax
<a name="API_DescribeIndexPolicies_RequestSyntax"></a>

```
{
   "logGroupIdentifiers": [ "{{string}}" ],
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeIndexPolicies_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [logGroupIdentifiers](#API_DescribeIndexPolicies_RequestSyntax) **   <a name="CWL-DescribeIndexPolicies-request-logGroupIdentifiers"></a>
An array containing the name or ARN of the log group that you want to retrieve field index policies for.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w#+=/:,.@-]*`
Required: Yes

 ** [nextToken](#API_DescribeIndexPolicies_RequestSyntax) **   <a name="CWL-DescribeIndexPolicies-request-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_DescribeIndexPolicies_ResponseSyntax"></a>

```
{
   "indexPolicies": [
      {
         "lastUpdateTime": number,
         "logGroupIdentifier": "string",
         "policyDocument": "string",
         "policyName": "string",
         "source": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeIndexPolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [indexPolicies](#API_DescribeIndexPolicies_ResponseSyntax) **   <a name="CWL-DescribeIndexPolicies-response-indexPolicies"></a>
An array containing the field index policies.
Type: Array of [IndexPolicy](API_IndexPolicy.md) objects

 ** [nextToken](#API_DescribeIndexPolicies_ResponseSyntax) **   <a name="CWL-DescribeIndexPolicies-response-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_DescribeIndexPolicies_Errors"></a>

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
<a name="API_DescribeIndexPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/DescribeIndexPolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/DescribeIndexPolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/DescribeIndexPolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/DescribeIndexPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/DescribeIndexPolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/DescribeIndexPolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/DescribeIndexPolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/DescribeIndexPolicies)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/DescribeIndexPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/DescribeIndexPolicies)
