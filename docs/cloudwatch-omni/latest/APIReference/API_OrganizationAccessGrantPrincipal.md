---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_OrganizationAccessGrantPrincipal.html
---

# OrganizationAccessGrantPrincipal
<a name="API_OrganizationAccessGrantPrincipal"></a>

The principal receiving an organization-level domain access grant. Specify principalId, principalAttributes, or both.

## Contents
<a name="API_OrganizationAccessGrantPrincipal_Contents"></a>

 ** principalType **   <a name="cloudwatchomni-Type-OrganizationAccessGrantPrincipal-principalType"></a>
The type of principal receiving the grant.
Type: String
Valid Values: `IDC_USER | IDC_GROUP | IAM_USER | IAM_ROLE | IAM_ROOT`
Required: Yes

 ** principalAttributes **   <a name="cloudwatchomni-Type-OrganizationAccessGrantPrincipal-principalAttributes"></a>
Attribute conditions for attribute-based access. When provided, the grant targets any principal matching all specified conditions. Supported only for IDC\_USER principals.
Type: Array of [AccessGrantPrincipalAttribute](API_AccessGrantPrincipalAttribute.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** principalId **   <a name="cloudwatchomni-Type-OrganizationAccessGrantPrincipal-principalId"></a>
The ID of the principal receiving the grant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9:/_+=,.@-]*`
Required: No

## See Also
<a name="API_OrganizationAccessGrantPrincipal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/OrganizationAccessGrantPrincipal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/OrganizationAccessGrantPrincipal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/OrganizationAccessGrantPrincipal)
