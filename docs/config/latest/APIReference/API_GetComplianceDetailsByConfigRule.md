---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_GetComplianceDetailsByConfigRule.html
---

# GetComplianceDetailsByConfigRule
<a name="API_GetComplianceDetailsByConfigRule"></a>

Returns the evaluation results for the specified AWS Config rule. The results indicate which AWS resources were evaluated by the rule, when each resource was last evaluated, and whether each resource complies with the rule.

## Request Syntax
<a name="API_GetComplianceDetailsByConfigRule_RequestSyntax"></a>

```
{
   "ComplianceTypes": [ "{{string}}" ],
   "ConfigRuleName": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetComplianceDetailsByConfigRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ComplianceTypes](#API_GetComplianceDetailsByConfigRule_RequestSyntax) **   <a name="config-GetComplianceDetailsByConfigRule-request-ComplianceTypes"></a>
Filters the results by compliance.
 `INSUFFICIENT_DATA` is a valid `ComplianceType` that is returned when an AWS Config rule cannot be evaluated. However, `INSUFFICIENT_DATA` cannot be used as a `ComplianceType` for filtering results.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Valid Values: `COMPLIANT | NON_COMPLIANT | NOT_APPLICABLE | INSUFFICIENT_DATA`
Required: No

 ** [ConfigRuleName](#API_GetComplianceDetailsByConfigRule_RequestSyntax) **   <a name="config-GetComplianceDetailsByConfigRule-request-ConfigRuleName"></a>
The name of the AWS Config rule for which you want compliance information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [Limit](#API_GetComplianceDetailsByConfigRule_RequestSyntax) **   <a name="config-GetComplianceDetailsByConfigRule-request-Limit"></a>
The maximum number of evaluation results returned on each page. The default is 10. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_GetComplianceDetailsByConfigRule_RequestSyntax) **   <a name="config-GetComplianceDetailsByConfigRule-request-NextToken"></a>
The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String
Required: No

## Response Syntax
<a name="API_GetComplianceDetailsByConfigRule_ResponseSyntax"></a>

```
{
   "EvaluationResults": [
      {
         "Annotation": "string",
         "ComplianceType": "string",
         "ConfigRuleInvokedTime": number,
         "EvaluationResultIdentifier": {
            "EvaluationResultQualifier": {
               "ConfigRuleName": "string",
               "EvaluationMode": "string",
               "ResourceId": "string",
               "ResourceType": "string"
            },
            "OrderingTimestamp": number,
            "ResourceEvaluationId": "string"
         },
         "ResultRecordedTime": number,
         "ResultToken": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetComplianceDetailsByConfigRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EvaluationResults](#API_GetComplianceDetailsByConfigRule_ResponseSyntax) **   <a name="config-GetComplianceDetailsByConfigRule-response-EvaluationResults"></a>
Indicates whether the AWS resource complies with the specified AWS Config rule.
Type: Array of [EvaluationResult](API_EvaluationResult.md) objects

 ** [NextToken](#API_GetComplianceDetailsByConfigRule_ResponseSyntax) **   <a name="config-GetComplianceDetailsByConfigRule-response-NextToken"></a>
The string that you use in a subsequent request to get the next page of results in a paginated response.
Type: String

## Errors
<a name="API_GetComplianceDetailsByConfigRule_Errors"></a>

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
<a name="API_GetComplianceDetailsByConfigRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/GetComplianceDetailsByConfigRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/GetComplianceDetailsByConfigRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/GetComplianceDetailsByConfigRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/GetComplianceDetailsByConfigRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/GetComplianceDetailsByConfigRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/GetComplianceDetailsByConfigRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/GetComplianceDetailsByConfigRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/GetComplianceDetailsByConfigRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/GetComplianceDetailsByConfigRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/GetComplianceDetailsByConfigRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
