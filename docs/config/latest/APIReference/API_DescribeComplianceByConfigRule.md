---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeComplianceByConfigRule.html
---

# DescribeComplianceByConfigRule
<a name="API_DescribeComplianceByConfigRule"></a>

Indicates whether the specified AWS Config rules are compliant. If a rule is noncompliant, this operation returns the number of AWS resources that do not comply with the rule.

A rule is compliant if all of the evaluated resources comply with it. It is noncompliant if any of these resources do not comply.

If AWS Config has no current evaluation results for the rule, it returns `INSUFFICIENT_DATA`. This result might indicate one of the following conditions:
+  AWS Config has never invoked an evaluation for the rule. To check whether it has, use the `DescribeConfigRuleEvaluationStatus` action to get the `LastSuccessfulInvocationTime` and `LastFailedInvocationTime`.
+ The rule's AWS Lambda function is failing to send evaluation results to AWS Config. Verify that the role you assigned to your configuration recorder includes the `config:PutEvaluations` permission. If the rule is a custom rule, verify that the AWS Lambda execution role includes the `config:PutEvaluations` permission.
+ The rule's AWS Lambda function has returned `NOT_APPLICABLE` for all evaluation results. This can occur if the resources were deleted or removed from the rule's scope.

## Request Syntax
<a name="API_DescribeComplianceByConfigRule_RequestSyntax"></a>

```
{
   "ComplianceTypes": [ "{{string}}" ],
   "ConfigRuleNames": [ "{{string}}" ],
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeComplianceByConfigRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ComplianceTypes](#API_DescribeComplianceByConfigRule_RequestSyntax) **   <a name="config-DescribeComplianceByConfigRule-request-ComplianceTypes"></a>
Filters the results by compliance.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Valid Values: `COMPLIANT | NON_COMPLIANT | NOT_APPLICABLE | INSUFFICIENT_DATA`
Required: No

 ** [ConfigRuleNames](#API_DescribeComplianceByConfigRule_RequestSyntax) **   <a name="config-DescribeComplianceByConfigRule-request-ConfigRuleNames"></a>
Specify one or more AWS Config rule names to filter the results by rule.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9_-]+`
Required: No

 ** [NextToken](#API_DescribeComplianceByConfigRule_RequestSyntax) **   <a name="config-DescribeComplianceByConfigRule-request-NextToken"></a>
The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeComplianceByConfigRule_ResponseSyntax"></a>

```
{
   "ComplianceByConfigRules": [
      {
         "Compliance": {
            "ComplianceContributorCount": {
               "CapExceeded": boolean,
               "CappedCount": number
            },
            "ComplianceType": "string"
         },
         "ConfigRuleName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeComplianceByConfigRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ComplianceByConfigRules](#API_DescribeComplianceByConfigRule_ResponseSyntax) **   <a name="config-DescribeComplianceByConfigRule-response-ComplianceByConfigRules"></a>
Indicates whether each of the specified AWS Config rules is compliant.
Type: Array of [ComplianceByConfigRule](API_ComplianceByConfigRule.md) objects

 ** [NextToken](#API_DescribeComplianceByConfigRule_ResponseSyntax) **   <a name="config-DescribeComplianceByConfigRule-response-NextToken"></a>
The string that you use in a subsequent request to get the next page of results in a paginated response.
Type: String

## Errors
<a name="API_DescribeComplianceByConfigRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The specified next token is not valid. Specify the `nextToken` string that was returned in the previous response to get the next page of results.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.
HTTP Status Code: 400

 ** NoSuchConfigRuleException **
The AWS Config rule in the request is not valid. Verify that the rule is an AWS Config Process Check rule, that the rule name is correct, and that valid Amazon Resouce Names (ARNs) are used before trying again.
HTTP Status Code: 400

## See Also
<a name="API_DescribeComplianceByConfigRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/DescribeComplianceByConfigRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/DescribeComplianceByConfigRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DescribeComplianceByConfigRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/DescribeComplianceByConfigRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DescribeComplianceByConfigRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/DescribeComplianceByConfigRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/DescribeComplianceByConfigRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/DescribeComplianceByConfigRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/DescribeComplianceByConfigRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DescribeComplianceByConfigRule)
