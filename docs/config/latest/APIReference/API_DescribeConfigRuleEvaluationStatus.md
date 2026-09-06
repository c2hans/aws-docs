---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigRuleEvaluationStatus.html
---

# DescribeConfigRuleEvaluationStatus
<a name="API_DescribeConfigRuleEvaluationStatus"></a>

Returns status information for each of your AWS Config managed rules. The status includes information such as the last time AWS Config invoked the rule, the last time AWS Config failed to invoke the rule, and the related error for the last failure.

## Request Syntax
<a name="API_DescribeConfigRuleEvaluationStatus_RequestSyntax"></a>

```
{
   "ConfigRuleNames": [ "{{string}}" ],
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeConfigRuleEvaluationStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigRuleNames](#API_DescribeConfigRuleEvaluationStatus_RequestSyntax) **   <a name="config-DescribeConfigRuleEvaluationStatus-request-ConfigRuleNames"></a>
The name of the AWS Config managed rules for which you want status information. If you do not specify any names, AWS Config returns status information for all AWS Config managed rules that you use.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9_-]+`
Required: No

 ** [Limit](#API_DescribeConfigRuleEvaluationStatus_RequestSyntax) **   <a name="config-DescribeConfigRuleEvaluationStatus-request-Limit"></a>
The number of rule evaluation results that you want returned.
This parameter is required if the rule limit for your account is more than the default of 1000 rules.
For information about requesting a rule limit increase, see [AWS Config Limits](http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_config) in the * AWS General Reference Guide*.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 50.
Required: No

 ** [NextToken](#API_DescribeConfigRuleEvaluationStatus_RequestSyntax) **   <a name="config-DescribeConfigRuleEvaluationStatus-request-NextToken"></a>
The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeConfigRuleEvaluationStatus_ResponseSyntax"></a>

```
{
   "ConfigRulesEvaluationStatus": [
      {
         "ConfigRuleArn": "string",
         "ConfigRuleId": "string",
         "ConfigRuleName": "string",
         "FirstActivatedTime": number,
         "FirstEvaluationStarted": boolean,
         "LastDeactivatedTime": number,
         "LastDebugLogDeliveryStatus": "string",
         "LastDebugLogDeliveryStatusReason": "string",
         "LastDebugLogDeliveryTime": number,
         "LastErrorCode": "string",
         "LastErrorMessage": "string",
         "LastFailedEvaluationTime": number,
         "LastFailedInvocationTime": number,
         "LastSuccessfulEvaluationTime": number,
         "LastSuccessfulInvocationTime": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeConfigRuleEvaluationStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConfigRulesEvaluationStatus](#API_DescribeConfigRuleEvaluationStatus_ResponseSyntax) **   <a name="config-DescribeConfigRuleEvaluationStatus-response-ConfigRulesEvaluationStatus"></a>
Status information about your AWS Config managed rules.
Type: Array of [ConfigRuleEvaluationStatus](API_ConfigRuleEvaluationStatus.md) objects

 ** [NextToken](#API_DescribeConfigRuleEvaluationStatus_ResponseSyntax) **   <a name="config-DescribeConfigRuleEvaluationStatus-response-NextToken"></a>
The string that you use in a subsequent request to get the next page of results in a paginated response.
Type: String

## Errors
<a name="API_DescribeConfigRuleEvaluationStatus_Errors"></a>

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
<a name="API_DescribeConfigRuleEvaluationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/DescribeConfigRuleEvaluationStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/DescribeConfigRuleEvaluationStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DescribeConfigRuleEvaluationStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/DescribeConfigRuleEvaluationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DescribeConfigRuleEvaluationStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/DescribeConfigRuleEvaluationStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/DescribeConfigRuleEvaluationStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/DescribeConfigRuleEvaluationStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/DescribeConfigRuleEvaluationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DescribeConfigRuleEvaluationStatus)
