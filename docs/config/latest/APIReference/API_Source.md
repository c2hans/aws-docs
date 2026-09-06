---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_Source.html
---

# Source
<a name="API_Source"></a>

Provides the CustomPolicyDetails, the rule owner (` AWS ` for managed rules, `CUSTOM_POLICY` for Custom Policy rules, and `CUSTOM_LAMBDA` for Custom Lambda rules), the rule identifier, and the events that cause the evaluation of your AWS resources.

## Contents
<a name="API_Source_Contents"></a>

 ** Owner **   <a name="config-Type-Source-Owner"></a>
Indicates whether AWS or the customer owns and manages the AWS Config rule.
 AWS Config Managed Rules are predefined rules owned by AWS. For more information, see [AWS Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html) in the * AWS Config developer guide*.
 AWS Config Custom Rules are rules that you can develop either with Guard (`CUSTOM_POLICY`) or AWS Lambda (`CUSTOM_LAMBDA`). For more information, see [AWS Config Custom Rules ](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html) in the * AWS Config developer guide*.
Type: String
Valid Values: `CUSTOM_LAMBDA | AWS | CUSTOM_POLICY`
Required: Yes

 ** CustomPolicyDetails **   <a name="config-Type-Source-CustomPolicyDetails"></a>
Provides the runtime system, policy definition, and whether debug logging is enabled. Required when owner is set to `CUSTOM_POLICY`.
Type: [CustomPolicyDetails](API_CustomPolicyDetails.md) object
Required: No

 ** SourceDetails **   <a name="config-Type-Source-SourceDetails"></a>
Provides the source and the message types that cause AWS Config to evaluate your AWS resources against a rule. It also provides the frequency with which you want AWS Config to run evaluations for the rule if the trigger type is periodic.
If the owner is set to `CUSTOM_POLICY`, the only acceptable values for the AWS Config rule trigger message type are `ConfigurationItemChangeNotification` and `OversizedConfigurationItemChangeNotification`.
Type: Array of [SourceDetail](API_SourceDetail.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Required: No

 ** SourceIdentifier **   <a name="config-Type-Source-SourceIdentifier"></a>
For AWS Config Managed rules, a predefined identifier from a list. For example, `IAM_PASSWORD_POLICY` is a managed rule. To reference a managed rule, see [List of AWS Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html).
For AWS Config Custom Lambda rules, the identifier is the Amazon Resource Name (ARN) of the rule's AWS Lambda function, such as `arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name`.
For AWS Config Custom Policy rules, this field will be ignored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_Source_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/Source)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/Source)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/Source)
