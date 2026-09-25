---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_DomainSummary.html
---

# DomainSummary
<a name="API_DomainSummary"></a>

Summary of a domain. Call GetDomain for the full domain.

## Contents
<a name="API_DomainSummary_Contents"></a>

 ** createdAt **   <a name="cloudwatchomni-Type-DomainSummary-createdAt"></a>
The timestamp when the domain was created.
Type: Timestamp
Required: Yes

 ** domainId **   <a name="cloudwatchomni-Type-DomainSummary-domainId"></a>
The unique ID of the domain.
Type: String
Pattern: `d-[0-9a-z]{1,25}`
Required: Yes

 ** status **   <a name="cloudwatchomni-Type-DomainSummary-status"></a>
Current status of the domain.
Type: String
Valid Values: `ACTIVE`
Required: Yes

 ** updatedAt **   <a name="cloudwatchomni-Type-DomainSummary-updatedAt"></a>
The timestamp when the domain was last updated.
Type: Timestamp
Required: Yes

 ** domainArn **   <a name="cloudwatchomni-Type-DomainSummary-domainArn"></a>
The Amazon Resource Name (ARN) of the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: No

 ** identityCenterInstanceArn **   <a name="cloudwatchomni-Type-DomainSummary-identityCenterInstanceArn"></a>
Identity Center instance ARN configured for the domain. Absent for IAM-only domains.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z-]*:sso:::instance/[a-zA-Z0-9-]+`
Required: No

 ** name **   <a name="cloudwatchomni-Type-DomainSummary-name"></a>
A name that identifies the domain.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-z0-9]+(-[a-z0-9]+)*`
Required: No

 ** region **   <a name="cloudwatchomni-Type-DomainSummary-region"></a>
The Region where this domain was created.
Type: String
Required: No

## See Also
<a name="API_DomainSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/DomainSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/DomainSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/DomainSummary)
