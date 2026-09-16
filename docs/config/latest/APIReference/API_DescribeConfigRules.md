---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigRules.html
---

# DescribeConfigRules
<a name="API_DescribeConfigRules"></a>

Returns details about your AWS Config rules.

## Request Syntax
<a name="API_DescribeConfigRules_RequestSyntax"></a>

```
{
   "ConfigRuleNames": [ "{{string}}" ],
   "Filters": {
      "EvaluationMode": "{{string}}",
      "RuleEvaluationVisibility": "{{string}}"
   },
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeConfigRules_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigRuleNames](#API_DescribeConfigRules_RequestSyntax) **   <a name="config-DescribeConfigRules-request-ConfigRuleNames"></a>
The names of the AWS Config rules for which you want details. If you do not specify any names, AWS Config returns details for all your rules.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9_-]+`
Required: No

 ** [Filters](#API_DescribeConfigRules_RequestSyntax) **   <a name="config-DescribeConfigRules-request-Filters"></a>
Returns a list of Detective or Proactive AWS Config rules. By default, this API returns an unfiltered list. For more information on Detective or Proactive AWS Config rules, see [**Evaluation Mode**](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config-rules.html) in the * AWS Config Developer Guide*.
Type: [DescribeConfigRulesFilters](API_DescribeConfigRulesFilters.md) object
Required: No

 ** [NextToken](#API_DescribeConfigRules_RequestSyntax) **   <a name="config-DescribeConfigRules-request-NextToken"></a>
The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeConfigRules_ResponseSyntax"></a>

```
{
   "ConfigRules": [
      {
         "ConfigRuleArn": "string",
         "ConfigRuleId": "string",
         "ConfigRuleName": "string",
         "ConfigRuleState": "string",
         "CreatedBy": "string",
         "Description": "string",
         "EvaluationModes": [
            {
               "Mode": "string"
            }
         ],
         "InputParameters": "string",
         "MaximumExecutionFrequency": "string",
         "RuleEvaluationVisibility": "string",
         "Scope": {
            "ComplianceResourceId": "string",
            "ComplianceResourceTypes": [ "string" ],
            "ServicePrincipals": [ "string" ],
            "TagKey": "string",
            "TagValue": "string"
         },
         "Source": {
            "CustomPolicyDetails": {
               "EnableDebugLogDelivery": boolean,
               "PolicyRuntime": "string",
               "PolicyText": "string"
            },
            "Owner": "string",
            "SourceDetails": [
               {
                  "EventSource": "string",
                  "MaximumExecutionFrequency": "string",
                  "MessageType": "string"
               }
            ],
            "SourceIdentifier": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeConfigRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConfigRules](#API_DescribeConfigRules_ResponseSyntax) **   <a name="config-DescribeConfigRules-response-ConfigRules"></a>
The details about your AWS Config rules.
Type: Array of [ConfigRule](API_ConfigRule.md) objects

 ** [NextToken](#API_DescribeConfigRules_ResponseSyntax) **   <a name="config-DescribeConfigRules-response-NextToken"></a>
The string that you use in a subsequent request to get the next page of results in a paginated response.
Type: String

## Errors
<a name="API_DescribeConfigRules_Errors"></a>

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
<a name="API_DescribeConfigRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/DescribeConfigRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/DescribeConfigRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DescribeConfigRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/DescribeConfigRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DescribeConfigRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/DescribeConfigRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/DescribeConfigRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/DescribeConfigRules)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/DescribeConfigRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DescribeConfigRules)
