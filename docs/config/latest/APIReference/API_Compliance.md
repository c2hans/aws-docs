---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_Compliance.html
---

# Compliance
<a name="API_Compliance"></a>

Indicates whether an AWS resource or AWS Config rule is compliant and provides the number of contributors that affect the compliance.

## Contents
<a name="API_Compliance_Contents"></a>

 ** ComplianceContributorCount **   <a name="config-Type-Compliance-ComplianceContributorCount"></a>
The number of AWS resources or AWS Config rules that cause a result of `NON_COMPLIANT`, up to a maximum number.
Type: [ComplianceContributorCount](API_ComplianceContributorCount.md) object
Required: No

 ** ComplianceType **   <a name="config-Type-Compliance-ComplianceType"></a>
Indicates whether an AWS resource or AWS Config rule is compliant.
A resource is compliant if it complies with all of the AWS Config rules that evaluate it. A resource is noncompliant if it does not comply with one or more of these rules.
A rule is compliant if all of the resources that the rule evaluates comply with it. A rule is noncompliant if any of these resources do not comply.
 AWS Config returns the `INSUFFICIENT_DATA` value when no evaluation results are available for the AWS resource or AWS Config rule.
For the `Compliance` data type, AWS Config supports only `COMPLIANT`, `NON_COMPLIANT`, and `INSUFFICIENT_DATA` values. AWS Config does not support the `NOT_APPLICABLE` value for the `Compliance` data type.
Type: String
Valid Values: `COMPLIANT | NON_COMPLIANT | NOT_APPLICABLE | INSUFFICIENT_DATA`
Required: No

## See Also
<a name="API_Compliance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/Compliance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/Compliance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/Compliance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
