---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetDataProtectionPolicy.html
---

# GetDataProtectionPolicy
<a name="API_GetDataProtectionPolicy"></a>

Returns information about a log group data protection policy.

## Request Syntax
<a name="API_GetDataProtectionPolicy_RequestSyntax"></a>

```
{
   "logGroupIdentifier": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDataProtectionPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [logGroupIdentifier](#API_GetDataProtectionPolicy_RequestSyntax) **   <a name="CWL-GetDataProtectionPolicy-request-logGroupIdentifier"></a>
The name or ARN of the log group that contains the data protection policy that you want to see.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w#+=/:,.@-]*`
Required: Yes

## Response Syntax
<a name="API_GetDataProtectionPolicy_ResponseSyntax"></a>

```
{
   "lastUpdatedTime": number,
   "logGroupIdentifier": "string",
   "policyDocument": "string"
}
```

## Response Elements
<a name="API_GetDataProtectionPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [lastUpdatedTime](#API_GetDataProtectionPolicy_ResponseSyntax) **   <a name="CWL-GetDataProtectionPolicy-response-lastUpdatedTime"></a>
The date and time that this policy was most recently updated.
Type: Long
Valid Range: Minimum value of 0.

 ** [logGroupIdentifier](#API_GetDataProtectionPolicy_ResponseSyntax) **   <a name="CWL-GetDataProtectionPolicy-response-logGroupIdentifier"></a>
The log group name or ARN that you specified in your request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w#+=/:,.@-]*`

 ** [policyDocument](#API_GetDataProtectionPolicy_ResponseSyntax) **   <a name="CWL-GetDataProtectionPolicy-response-policyDocument"></a>
The data protection policy document for this log group.
Type: String

## Errors
<a name="API_GetDataProtectionPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
A parameter is specified incorrectly.
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
<a name="API_GetDataProtectionPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/GetDataProtectionPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/GetDataProtectionPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/GetDataProtectionPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/GetDataProtectionPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/GetDataProtectionPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/GetDataProtectionPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/GetDataProtectionPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/GetDataProtectionPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/GetDataProtectionPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/GetDataProtectionPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
