---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_PolicyGrantPrincipal.html
---

# PolicyGrantPrincipal
<a name="API_PolicyGrantPrincipal"></a>

The policy grant principal.

## Contents
<a name="API_PolicyGrantPrincipal_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** domainUnit **   <a name="datazone-Type-PolicyGrantPrincipal-domainUnit"></a>
The domain unit of the policy grant principal.
Type: [DomainUnitPolicyGrantPrincipal](API_DomainUnitPolicyGrantPrincipal.md) object
Required: No

 ** group **   <a name="datazone-Type-PolicyGrantPrincipal-group"></a>
The group of the policy grant principal.
Type: [GroupPolicyGrantPrincipal](API_GroupPolicyGrantPrincipal.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** project **   <a name="datazone-Type-PolicyGrantPrincipal-project"></a>
The project of the policy grant principal.
Type: [ProjectPolicyGrantPrincipal](API_ProjectPolicyGrantPrincipal.md) object
Required: No

 ** user **   <a name="datazone-Type-PolicyGrantPrincipal-user"></a>
The user of the policy grant principal.
Type: [UserPolicyGrantPrincipal](API_UserPolicyGrantPrincipal.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_PolicyGrantPrincipal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/PolicyGrantPrincipal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/PolicyGrantPrincipal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/PolicyGrantPrincipal)
