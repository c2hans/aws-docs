---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_Domain.html
---

# Domain
<a name="API_Domain"></a>

Detailed information about a domain.

## Contents
<a name="API_Domain_Contents"></a>

 ** createdAt **   <a name="cloudwatchomni-Type-Domain-createdAt"></a>
The timestamp when the domain was created.
Type: Timestamp
Required: Yes

 ** domainArn **   <a name="cloudwatchomni-Type-Domain-domainArn"></a>
The Amazon Resource Name (ARN) of the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: Yes

 ** domainEndpointUrl **   <a name="cloudwatchomni-Type-Domain-domainEndpointUrl"></a>
The HTTPS endpoint URL for accessing the domain.
Type: String
Required: Yes

 ** domainId **   <a name="cloudwatchomni-Type-Domain-domainId"></a>
The unique ID of the domain.
Type: String
Pattern: `d-[0-9a-z]{1,25}`
Required: Yes

 ** identityProviders **   <a name="cloudwatchomni-Type-Domain-identityProviders"></a>
The identity providers configured for the domain.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `IAM | IDC`
Required: Yes

 ** region **   <a name="cloudwatchomni-Type-Domain-region"></a>
The Region where this domain was created.
Type: String
Required: Yes

 ** status **   <a name="cloudwatchomni-Type-Domain-status"></a>
Current status of the domain.
Type: String
Valid Values: `ACTIVE`
Required: Yes

 ** updatedAt **   <a name="cloudwatchomni-Type-Domain-updatedAt"></a>
The timestamp when the domain was last updated.
Type: Timestamp
Required: Yes

 ** customEndpointUrls **   <a name="cloudwatchomni-Type-Domain-customEndpointUrls"></a>
Additional endpoint URLs derived from the domain name.
Type: Array of strings
Required: No

 ** identityCenterApplicationArn **   <a name="cloudwatchomni-Type-Domain-identityCenterApplicationArn"></a>
The ARN of the Identity Center application. Absent for IAM-only domains.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: No

 ** identityProviderConfiguration **   <a name="cloudwatchomni-Type-Domain-identityProviderConfiguration"></a>
Identity provider configuration for the domain.
Type: [IdentityProviderConfiguration](API_IdentityProviderConfiguration.md) object
Required: No

 ** name **   <a name="cloudwatchomni-Type-Domain-name"></a>
A name that identifies the domain.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-z0-9]+(-[a-z0-9]+)*`
Required: No

## See Also
<a name="API_Domain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/Domain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/Domain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/Domain)
