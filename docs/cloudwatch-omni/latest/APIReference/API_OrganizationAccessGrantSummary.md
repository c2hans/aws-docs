---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_OrganizationAccessGrantSummary.html
---

# OrganizationAccessGrantSummary
<a name="API_OrganizationAccessGrantSummary"></a>

Summary of an organization access grant. Call GetDomainAccessGrantForOrganization for the full grant.

## Contents
<a name="API_OrganizationAccessGrantSummary_Contents"></a>

 ** createdAt **   <a name="cloudwatchomni-Type-OrganizationAccessGrantSummary-createdAt"></a>
The timestamp when the access grant was created.
Type: Timestamp
Required: Yes

 ** domainId **   <a name="cloudwatchomni-Type-OrganizationAccessGrantSummary-domainId"></a>
The ID of the organization domain the grant belongs to.
Type: String
Pattern: `d-[0-9a-z]{1,25}`
Required: Yes

 ** grantArn **   <a name="cloudwatchomni-Type-OrganizationAccessGrantSummary-grantArn"></a>
The Amazon Resource Name (ARN) of the access grant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: Yes

 ** grantId **   <a name="cloudwatchomni-Type-OrganizationAccessGrantSummary-grantId"></a>
The unique ID of the access grant.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** grantType **   <a name="cloudwatchomni-Type-OrganizationAccessGrantSummary-grantType"></a>
Who manages the grant.
Type: String
Valid Values: `SERVICE_MANAGED | CUSTOMER_MANAGED`
Required: Yes

 ** permission **   <a name="cloudwatchomni-Type-OrganizationAccessGrantSummary-permission"></a>
The permission granted.
Type: String
Valid Values: `ADMIN`
Required: Yes

 ** principal **   <a name="cloudwatchomni-Type-OrganizationAccessGrantSummary-principal"></a>
The principal receiving the grant.
Type: [OrganizationAccessGrantPrincipal](API_OrganizationAccessGrantPrincipal.md) object
Required: Yes

 ** updatedAt **   <a name="cloudwatchomni-Type-OrganizationAccessGrantSummary-updatedAt"></a>
The timestamp when the access grant was last updated.
Type: Timestamp
Required: Yes

 ** name **   <a name="cloudwatchomni-Type-OrganizationAccessGrantSummary-name"></a>
A name that identifies the access grant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

## See Also
<a name="API_OrganizationAccessGrantSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/OrganizationAccessGrantSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/OrganizationAccessGrantSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/OrganizationAccessGrantSummary)
