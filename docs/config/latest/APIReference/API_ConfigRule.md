---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigRule.html
---

# ConfigRule
<a name="API_ConfigRule"></a>

 AWS Config rules evaluate the configuration settings of your AWS resources. A rule can run when AWS Config detects a configuration change to an AWS resource or at a periodic frequency that you choose (for example, every 24 hours). There are two types of rules: * AWS Config Managed Rules* and * AWS Config Custom Rules*.

 AWS Config Managed Rules are predefined, customizable rules created by AWS Config. For a list of managed rules, see [List of AWS Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html).

 AWS Config Custom Rules are rules that you create from scratch. There are two ways to create AWS Config custom rules: with Lambda functions ([AWS Lambda Developer Guide](https://docs.aws.amazon.com/config/latest/developerguide/gettingstarted-concepts.html#gettingstarted-concepts-function)) and with Guard ([Guard GitHub Repository](https://github.com/aws-cloudformation/cloudformation-guard)), a policy-as-code language. AWS Config custom rules created with AWS Lambda are called * AWS Config Custom Lambda Rules* and AWS Config custom rules created with Guard are called * AWS Config Custom Policy Rules*.

For more information about developing and using AWS Config rules, see [Evaluating Resource with AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) in the * AWS Config Developer Guide*.

**Note**
You can use the AWS CLI and AWS SDKs if you want to create a rule that triggers evaluations for your resources when AWS Config delivers the configuration snapshot. For more information, see [ConfigSnapshotDeliveryProperties](API_ConfigSnapshotDeliveryProperties.md).

## Contents
<a name="API_ConfigRule_Contents"></a>

 ** Source **   <a name="config-Type-ConfigRule-Source"></a>
Provides the rule owner (` AWS ` for managed rules, `CUSTOM_POLICY` for Custom Policy rules, and `CUSTOM_LAMBDA` for Custom Lambda rules), the rule identifier, and the notifications that cause the function to evaluate your AWS resources.
Type: [Source](API_Source.md) object
Required: Yes

 ** ConfigRuleArn **   <a name="config-Type-ConfigRule-ConfigRuleArn"></a>
The Amazon Resource Name (ARN) of the AWS Config rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ConfigRuleId **   <a name="config-Type-ConfigRule-ConfigRuleId"></a>
The ID of the AWS Config rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ConfigRuleName **   <a name="config-Type-ConfigRule-ConfigRuleName"></a>
The name that you assign to the AWS Config rule. The name is required if you are adding a new rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

 ** ConfigRuleState **   <a name="config-Type-ConfigRule-ConfigRuleState"></a>
Indicates whether the AWS Config rule is active or is currently being deleted by AWS Config. It can also indicate the evaluation status for the AWS Config rule.
 AWS Config sets the state of the rule to `EVALUATING` temporarily after you use the `StartConfigRulesEvaluation` request to evaluate your resources against the AWS Config rule.
 AWS Config sets the state of the rule to `DELETING_RESULTS` temporarily after you use the `DeleteEvaluationResults` request to delete the current evaluation results for the AWS Config rule.
 AWS Config temporarily sets the state of a rule to `DELETING` after you use the `DeleteConfigRule` request to delete the rule. After AWS Config deletes the rule, the rule and all of its evaluations are erased and are no longer available.
Type: String
Valid Values: `ACTIVE | DELETING | DELETING_RESULTS | EVALUATING`
Required: No

 ** CreatedBy **   <a name="config-Type-ConfigRule-CreatedBy"></a>
Service principal name of the service that created the rule.
The field is populated only if the service-linked rule is created by a service. The field is empty if you create your own rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** Description **   <a name="config-Type-ConfigRule-Description"></a>
The description that you provide for the AWS Config rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** EvaluationModes **   <a name="config-Type-ConfigRule-EvaluationModes"></a>
The modes the AWS Config rule can be evaluated in. The valid values are distinct objects. By default, the value is Detective evaluation mode only.
Type: Array of [EvaluationModeConfiguration](API_EvaluationModeConfiguration.md) objects
Required: No

 ** InputParameters **   <a name="config-Type-ConfigRule-InputParameters"></a>
A string, in JSON format, that is passed to the AWS Config rule Lambda function.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** MaximumExecutionFrequency **   <a name="config-Type-ConfigRule-MaximumExecutionFrequency"></a>
The maximum frequency with which AWS Config runs evaluations for a rule. You can specify a value for `MaximumExecutionFrequency` when:
+ This is for an AWS Config managed rule that is triggered at a periodic frequency.
+ Your custom rule is triggered when AWS Config delivers the configuration snapshot. For more information, see [ConfigSnapshotDeliveryProperties](API_ConfigSnapshotDeliveryProperties.md).
By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the `MaximumExecutionFrequency` parameter.
Type: String
Valid Values: `One_Hour | Three_Hours | Six_Hours | Twelve_Hours | TwentyFour_Hours`
Required: No

 ** RuleEvaluationVisibility **   <a name="config-Type-ConfigRule-RuleEvaluationVisibility"></a>
Indicates whether you can get [Evaluation](API_Evaluation.md)s for the AWS Config rule. You can get [Evaluation](API_Evaluation.md)s for the AWS AWS Config rule if this value is `EXTERNAL`. You cannot get [Evaluation](API_Evaluation.md)s for the AWS AWS Config rule if this value is `INTERNAL`.
Type: String
Valid Values: `EXTERNAL | INTERNAL`
Required: No

 ** Scope **   <a name="config-Type-ConfigRule-Scope"></a>
Defines which resources can trigger an evaluation for the rule. The scope can include one or more resource types, a combination of one resource type and one resource ID, or a combination of a tag key and value. Specify a scope to constrain the resources that can trigger an evaluation for the rule. If you do not specify a scope, evaluations are triggered when any resource in the recording group changes.
Type: [Scope](API_Scope.md) object
Required: No

## See Also
<a name="API_ConfigRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ConfigRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ConfigRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ConfigRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
