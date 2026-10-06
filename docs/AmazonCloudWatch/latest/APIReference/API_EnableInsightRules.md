---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_EnableInsightRules.html
---

# EnableInsightRules
<a name="API_EnableInsightRules"></a>

Enables the specified Contributor Insights rules. When rules are enabled, they immediately begin analyzing log data.

## Request Syntax
<a name="API_EnableInsightRules_RequestSyntax"></a>

```
{
   "RuleNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_EnableInsightRules_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RuleNames](#API_EnableInsightRules_RequestSyntax) **   <a name="ACW-EnableInsightRules-request-RuleNames"></a>
An array of the rule names to enable. If you need to find out the names of your rules, use [DescribeInsightRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeInsightRules.html).
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x20-\x7E]+`
Required: Yes

## Response Syntax
<a name="API_EnableInsightRules_ResponseSyntax"></a>

```
{
   "Failures": [
      {
         "ExceptionType": "string",
         "FailureCode": "string",
         "FailureDescription": "string",
         "FailureResource": "string"
      }
   ]
}
```

## Response Elements
<a name="API_EnableInsightRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Failures](#API_EnableInsightRules_ResponseSyntax) **   <a name="ACW-EnableInsightRules-response-Failures"></a>
An array listing the rules that could not be enabled. You cannot disable or enable built-in rules.
Type: Array of [PartialFailure](API_PartialFailure.md) objects

## Errors
<a name="API_EnableInsightRules_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValue **
The value of an input parameter is bad or out-of-range.
 ** message **

HTTP Status Code: 400

 ** LimitExceededException **
The operation exceeded one or more limits.
HTTP Status Code: 400

 ** MissingParameter **
An input parameter that is required is missing.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_EnableInsightRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/EnableInsightRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/EnableInsightRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/EnableInsightRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/EnableInsightRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/EnableInsightRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/EnableInsightRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/EnableInsightRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/EnableInsightRules)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/EnableInsightRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/EnableInsightRules)
