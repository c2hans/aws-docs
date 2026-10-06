---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListManagedInsightRules.html
---

# ListManagedInsightRules
<a name="API_ListManagedInsightRules"></a>

 Returns a list that contains the number of managed Contributor Insights rules in your account.

## Request Syntax
<a name="API_ListManagedInsightRules_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceARN": "{{string}}"
}
```

## Request Parameters
<a name="API_ListManagedInsightRules_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListManagedInsightRules_RequestSyntax) **   <a name="ACW-ListManagedInsightRules-request-MaxResults"></a>
 The maximum number of results to return in one operation. If you omit this parameter, the default number is used. The default number is `100`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [NextToken](#API_ListManagedInsightRules_RequestSyntax) **   <a name="ACW-ListManagedInsightRules-request-NextToken"></a>
 Include this value to get the next set of rules if the value was returned by the previous operation.
Type: String
Required: No

 ** [ResourceARN](#API_ListManagedInsightRules_RequestSyntax) **   <a name="ACW-ListManagedInsightRules-request-ResourceARN"></a>
 The ARN of an AWS resource that has managed Contributor Insights rules.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## Response Syntax
<a name="API_ListManagedInsightRules_ResponseSyntax"></a>

```
{
   "ManagedRules": [
      {
         "ResourceARN": "string",
         "RuleState": {
            "RuleName": "string",
            "State": "string"
         },
         "TemplateName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListManagedInsightRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ManagedRules](#API_ListManagedInsightRules_ResponseSyntax) **   <a name="ACW-ListManagedInsightRules-response-ManagedRules"></a>
 The managed rules that are available for the specified AWS resource.
Type: Array of [ManagedRuleDescription](API_ManagedRuleDescription.md) objects

 ** [NextToken](#API_ListManagedInsightRules_ResponseSyntax) **   <a name="ACW-ListManagedInsightRules-response-NextToken"></a>
 Include this value to get the next set of rules if the value was returned by the previous operation.
Type: String

## Errors
<a name="API_ListManagedInsightRules_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextToken **
The next token specified is invalid.
 ** message **

HTTP Status Code: 400

 ** InvalidParameterValue **
The value of an input parameter is bad or out-of-range.
 ** message **

HTTP Status Code: 400

 ** MissingParameter **
An input parameter that is required is missing.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_ListManagedInsightRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/ListManagedInsightRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/ListManagedInsightRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/ListManagedInsightRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/ListManagedInsightRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ListManagedInsightRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/ListManagedInsightRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/ListManagedInsightRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/ListManagedInsightRules)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/ListManagedInsightRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/ListManagedInsightRules)
