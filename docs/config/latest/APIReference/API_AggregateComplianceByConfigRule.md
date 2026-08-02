---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_AggregateComplianceByConfigRule.html
---

# AggregateComplianceByConfigRule
<a name="API_AggregateComplianceByConfigRule"></a>

Indicates whether an AWS Config rule is compliant based on account ID, region, compliance, and rule name.

A rule is compliant if all of the resources that the rule evaluated comply with it. It is noncompliant if any of these resources do not comply.

## Contents
<a name="API_AggregateComplianceByConfigRule_Contents"></a>

 ** AccountId **   <a name="config-Type-AggregateComplianceByConfigRule-AccountId"></a>
The 12-digit account ID of the source account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** AwsRegion **   <a name="config-Type-AggregateComplianceByConfigRule-AwsRegion"></a>
The source region from where the data is aggregated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Compliance **   <a name="config-Type-AggregateComplianceByConfigRule-Compliance"></a>
Indicates whether an AWS resource or AWS Config rule is compliant and provides the number of contributors that affect the compliance.
Type: [Compliance](API_Compliance.md) object
Required: No

 ** ConfigRuleName **   <a name="config-Type-AggregateComplianceByConfigRule-ConfigRuleName"></a>
The name of the AWS Config rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AggregateComplianceByConfigRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/AggregateComplianceByConfigRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/AggregateComplianceByConfigRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/AggregateComplianceByConfigRule)
