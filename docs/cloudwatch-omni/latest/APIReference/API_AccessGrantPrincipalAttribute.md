---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_AccessGrantPrincipalAttribute.html
---

# AccessGrantPrincipalAttribute
<a name="API_AccessGrantPrincipalAttribute"></a>

A single attribute condition used to match principals for attribute-based access.

## Contents
<a name="API_AccessGrantPrincipalAttribute_Contents"></a>

 ** key **   <a name="cloudwatchomni-Type-AccessGrantPrincipalAttribute-key"></a>
The Identity Center user attribute to match on. One of userName, active, userStatus, displayName, email, name.givenName, name.familyName, enterprise.department, enterprise.division, enterprise.organization, enterprise.costCenter, or enterprise.employeeNumber. Each key may appear only once per grant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** value **   <a name="cloudwatchomni-Type-AccessGrantPrincipalAttribute-value"></a>
The attribute value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

## See Also
<a name="API_AccessGrantPrincipalAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/AccessGrantPrincipalAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/AccessGrantPrincipalAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/AccessGrantPrincipalAttribute)
