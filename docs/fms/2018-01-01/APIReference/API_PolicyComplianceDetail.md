---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_PolicyComplianceDetail.html
---

# PolicyComplianceDetail
<a name="API_PolicyComplianceDetail"></a>

Describes the noncompliant resources in a member account for a specific AWS Firewall Manager policy. A maximum of 100 entries are displayed. If more than 100 resources are noncompliant, `EvaluationLimitExceeded` is set to `True`.

## Contents
<a name="API_PolicyComplianceDetail_Contents"></a>

 ** EvaluationLimitExceeded **   <a name="fms-Type-PolicyComplianceDetail-EvaluationLimitExceeded"></a>
Indicates if over 100 resources are noncompliant with the AWS Firewall Manager policy.
Type: Boolean
Required: No

 ** ExpiredAt **   <a name="fms-Type-PolicyComplianceDetail-ExpiredAt"></a>
A timestamp that indicates when the returned information should be considered out of date.
Type: Timestamp
Required: No

 ** IssueInfoMap **   <a name="fms-Type-PolicyComplianceDetail-IssueInfoMap"></a>
Details about problems with dependent services, such as AWS WAF or AWS Config, and the error message received that indicates the problem with the service.
Type: String to string map
Valid Keys: `AWSCONFIG | AWSWAF | AWSSHIELD_ADVANCED | AWSVPC`
Value Length Constraints: Minimum length of 1. Maximum length of 4096.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=,+\-@]*)$`
Required: No

 ** MemberAccount **   <a name="fms-Type-PolicyComplianceDetail-MemberAccount"></a>
The AWS account ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9]+$`
Required: No

 ** PolicyId **   <a name="fms-Type-PolicyComplianceDetail-PolicyId"></a>
The ID of the AWS Firewall Manager policy.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-z0-9A-Z-]{36}$`
Required: No

 ** PolicyOwner **   <a name="fms-Type-PolicyComplianceDetail-PolicyOwner"></a>
The AWS account that created the AWS Firewall Manager policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9]+$`
Required: No

 ** Violators **   <a name="fms-Type-PolicyComplianceDetail-Violators"></a>
An array of resources that aren't protected by the AWS WAF or Shield Advanced policy or that aren't in compliance with the security group policy.
Type: Array of [ComplianceViolator](API_ComplianceViolator.md) objects
Required: No

## See Also
<a name="API_PolicyComplianceDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/PolicyComplianceDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/PolicyComplianceDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/PolicyComplianceDetail)
