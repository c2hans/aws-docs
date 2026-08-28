---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_StartConfigRulesEvaluation.html
---

# StartConfigRulesEvaluation
<a name="API_StartConfigRulesEvaluation"></a>

Runs an on-demand evaluation for the specified AWS Config rules against the last known configuration state of the resources. Use `StartConfigRulesEvaluation` when you want to test that a rule you updated is working as expected. `StartConfigRulesEvaluation` does not re-record the latest configuration state for your resources. It re-runs an evaluation against the last known state of your resources.

You can specify up to 25 AWS Config rules per request.

An existing `StartConfigRulesEvaluation` call for the specified rules must complete before you can call the API again. If you chose to have AWS Config stream to an Amazon SNS topic, you will receive a `ConfigRuleEvaluationStarted` notification when the evaluation starts.

**Note**
You don't need to call the `StartConfigRulesEvaluation` API to run an evaluation for a new rule. When you create a rule, AWS Config evaluates your resources against the rule automatically.

The `StartConfigRulesEvaluation` API is useful if you want to run on-demand evaluations, such as the following example:

1. You have a custom rule that evaluates your IAM resources every 24 hours.

1. You update your Lambda function to add additional conditions to your rule.

1. Instead of waiting for the next periodic evaluation, you call the `StartConfigRulesEvaluation` API.

1.  AWS Config invokes your Lambda function and evaluates your IAM resources.

1. Your custom rule will still run periodic evaluations every 24 hours.

## Request Syntax
<a name="API_StartConfigRulesEvaluation_RequestSyntax"></a>

```
{
   "ConfigRuleNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_StartConfigRulesEvaluation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigRuleNames](#API_StartConfigRulesEvaluation_RequestSyntax) **   <a name="config-StartConfigRulesEvaluation-request-ConfigRuleNames"></a>
The list of names of AWS Config rules that you want to run evaluations for.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

## Response Elements
<a name="API_StartConfigRulesEvaluation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StartConfigRulesEvaluation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.
HTTP Status Code: 400

 ** LimitExceededException **
For `PutServiceLinkedConfigurationRecorder` API, this exception is thrown if the number of service-linked roles in the account exceeds the limit.
For `StartConfigRulesEvaluation` API, this exception is thrown if an evaluation is in progress or if you call the [StartConfigRulesEvaluation](#API_StartConfigRulesEvaluation) API more than once per minute.
For `PutConfigurationAggregator` API, this exception is thrown if the number of accounts and aggregators exceeds the limit.
HTTP Status Code: 400

 ** NoSuchConfigRuleException **
The AWS Config rule in the request is not valid. Verify that the rule is an AWS Config Process Check rule, that the rule name is correct, and that valid Amazon Resouce Names (ARNs) are used before trying again.
HTTP Status Code: 400

 ** ResourceInUseException **
You see this exception in the following cases:
+ For DeleteConfigRule, AWS Config is deleting this rule. Try your request again later.
+ For DeleteConfigRule, the rule is deleting your evaluation results. Try your request again later.
+ For DeleteConfigRule, a remediation action is associated with the rule and AWS Config cannot delete this rule. Delete the remediation action associated with the rule before deleting the rule and try your request again later.
+ For PutConfigOrganizationRule, organization AWS Config rule deletion is in progress. Try your request again later.
+ For DeleteOrganizationConfigRule, organization AWS Config rule creation is in progress. Try your request again later.
+ For PutConformancePack and PutOrganizationConformancePack, a conformance pack creation, update, and deletion is in progress. Try your request again later.
+ For DeleteConformancePack, a conformance pack creation, update, and deletion is in progress. Try your request again later.
HTTP Status Code: 400

## See Also
<a name="API_StartConfigRulesEvaluation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/StartConfigRulesEvaluation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/StartConfigRulesEvaluation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/StartConfigRulesEvaluation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/StartConfigRulesEvaluation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/StartConfigRulesEvaluation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/StartConfigRulesEvaluation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/StartConfigRulesEvaluation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/StartConfigRulesEvaluation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/StartConfigRulesEvaluation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/StartConfigRulesEvaluation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
