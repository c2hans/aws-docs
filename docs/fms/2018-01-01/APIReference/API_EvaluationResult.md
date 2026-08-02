---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_EvaluationResult.html
---

# EvaluationResult
<a name="API_EvaluationResult"></a>

Describes the compliance status for the account. An account is considered noncompliant if it includes resources that are not protected by the specified policy or that don't comply with the policy.

## Contents
<a name="API_EvaluationResult_Contents"></a>

 ** ComplianceStatus **   <a name="fms-Type-EvaluationResult-ComplianceStatus"></a>
Describes an AWS account's compliance with the AWS Firewall Manager policy.
Type: String
Valid Values: `COMPLIANT | NON_COMPLIANT`
Required: No

 ** EvaluationLimitExceeded **   <a name="fms-Type-EvaluationResult-EvaluationLimitExceeded"></a>
Indicates that over 100 resources are noncompliant with the AWS Firewall Manager policy.
Type: Boolean
Required: No

 ** ViolatorCount **   <a name="fms-Type-EvaluationResult-ViolatorCount"></a>
The number of resources that are noncompliant with the specified policy. For AWS WAF and Shield Advanced policies, a resource is considered noncompliant if it is not associated with the policy. For security group policies, a resource is considered noncompliant if it doesn't comply with the rules of the policy and remediation is disabled or not possible.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_EvaluationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/EvaluationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/EvaluationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/EvaluationResult)
