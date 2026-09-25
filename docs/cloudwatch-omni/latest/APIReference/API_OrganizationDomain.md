---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_OrganizationDomain.html
---

# OrganizationDomain
<a name="API_OrganizationDomain"></a>

Detailed information about an organization domain.

## Contents
<a name="API_OrganizationDomain_Contents"></a>

 ** createdAt **   <a name="cloudwatchomni-Type-OrganizationDomain-createdAt"></a>
The timestamp when the organization domain was created.
Type: Timestamp
Required: Yes

 ** domainArn **   <a name="cloudwatchomni-Type-OrganizationDomain-domainArn"></a>
The Amazon Resource Name (ARN) of the organization domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: Yes

 ** domainEndpointUrl **   <a name="cloudwatchomni-Type-OrganizationDomain-domainEndpointUrl"></a>
The HTTPS endpoint URL for accessing the organization domain.
Type: String
Required: Yes

 ** domainId **   <a name="cloudwatchomni-Type-OrganizationDomain-domainId"></a>
The unique ID of the organization domain.
Type: String
Pattern: `d-[0-9a-z]{1,25}`
Required: Yes

 ** identityProviders **   <a name="cloudwatchomni-Type-OrganizationDomain-identityProviders"></a>
The identity providers configured for the organization domain.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `IAM | IDC`
Required: Yes

 ** organizationId **   <a name="cloudwatchomni-Type-OrganizationDomain-organizationId"></a>
The ID of the AWS Organization that owns the domain.
Type: String
Required: Yes

 ** ownerAccountId **   <a name="cloudwatchomni-Type-OrganizationDomain-ownerAccountId"></a>
The AWS account ID that owns the organization domain.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: Yes

 ** region **   <a name="cloudwatchomni-Type-OrganizationDomain-region"></a>
The Region where this organization domain was created.
Type: String
Required: Yes

 ** status **   <a name="cloudwatchomni-Type-OrganizationDomain-status"></a>
Current status of the organization domain.
Type: String
Valid Values: `ACTIVE`
Required: Yes

 ** updatedAt **   <a name="cloudwatchomni-Type-OrganizationDomain-updatedAt"></a>
The timestamp when the organization domain was last updated.
Type: Timestamp
Required: Yes

 ** customEndpointUrls **   <a name="cloudwatchomni-Type-OrganizationDomain-customEndpointUrls"></a>
Additional endpoint URLs derived from the domain name.
Type: Array of strings
Required: No

 ** domainAccessRoleArn **   <a name="cloudwatchomni-Type-OrganizationDomain-domainAccessRoleArn"></a>
The ARN of the customer-provided IAM role in the management account used for domain access.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-zA-Z-]*:iam::[0-9]{12}:role/.+`
Required: No

 ** identityCenterApplicationArn **   <a name="cloudwatchomni-Type-OrganizationDomain-identityCenterApplicationArn"></a>
The ARN of the Identity Center application. Absent for IAM-only domains.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: No

 ** identityProviderConfiguration **   <a name="cloudwatchomni-Type-OrganizationDomain-identityProviderConfiguration"></a>
Identity provider configuration for the organization domain.
Type: [IdentityProviderConfiguration](API_IdentityProviderConfiguration.md) object
Required: No

 ** name **   <a name="cloudwatchomni-Type-OrganizationDomain-name"></a>
A name that identifies the organization domain.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-z0-9]+(-[a-z0-9]+)*`
Required: No

## See Also
<a name="API_OrganizationDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/OrganizationDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/OrganizationDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/OrganizationDomain)
