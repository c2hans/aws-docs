---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_PolicyComplianceStatus.html
---

# PolicyComplianceStatus
<a name="API_PolicyComplianceStatus"></a>

Indicates whether the account is compliant with the specified policy. An account is considered noncompliant if it includes resources that are not protected by the policy, for AWS WAF and Shield Advanced policies, or that are noncompliant with the policy, for security group policies.

## Contents
<a name="API_PolicyComplianceStatus_Contents"></a>

 ** EvaluationResults **   <a name="fms-Type-PolicyComplianceStatus-EvaluationResults"></a>
An array of `EvaluationResult` objects.
Type: Array of [EvaluationResult](API_EvaluationResult.md) objects
Required: No

 ** IssueInfoMap **   <a name="fms-Type-PolicyComplianceStatus-IssueInfoMap"></a>
Details about problems with dependent services, such as AWS WAF or AWS Config, and the error message received that indicates the problem with the service.
Type: String to string map
Valid Keys: `AWSCONFIG | AWSWAF | AWSSHIELD_ADVANCED | AWSVPC`
Value Length Constraints: Minimum length of 1. Maximum length of 4096.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=,+\-@]*)$`
Required: No

 ** LastUpdated **   <a name="fms-Type-PolicyComplianceStatus-LastUpdated"></a>
Timestamp of the last update to the `EvaluationResult` objects.
Type: Timestamp
Required: No

 ** MemberAccount **   <a name="fms-Type-PolicyComplianceStatus-MemberAccount"></a>
The member account ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9]+$`
Required: No

 ** PolicyId **   <a name="fms-Type-PolicyComplianceStatus-PolicyId"></a>
The ID of the AWS Firewall Manager policy.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-z0-9A-Z-]{36}$`
Required: No

 ** PolicyName **   <a name="fms-Type-PolicyComplianceStatus-PolicyName"></a>
The name of the AWS Firewall Manager policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** PolicyOwner **   <a name="fms-Type-PolicyComplianceStatus-PolicyOwner"></a>
The AWS account that created the AWS Firewall Manager policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9]+$`
Required: No

## See Also
<a name="API_PolicyComplianceStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/PolicyComplianceStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/PolicyComplianceStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/PolicyComplianceStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
