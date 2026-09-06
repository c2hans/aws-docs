---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_PolicyGrantMember.html
---

# PolicyGrantMember
<a name="API_PolicyGrantMember"></a>

A member of the policy grant list.

## Contents
<a name="API_PolicyGrantMember_Contents"></a>

 ** createdAt **   <a name="datazone-Type-PolicyGrantMember-createdAt"></a>
Specifies the timestamp at which policy grant member was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="datazone-Type-PolicyGrantMember-createdBy"></a>
Specifies the user who created the policy grant member.
Type: String
Required: No

 ** detail **   <a name="datazone-Type-PolicyGrantMember-detail"></a>
The details of the policy grant member.
Type: [PolicyGrantDetail](API_PolicyGrantDetail.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** grantId **   <a name="datazone-Type-PolicyGrantMember-grantId"></a>
The ID of the policy grant.
Type: String
Pattern: `[A-Za-z0-9+/]{10}`
Required: No

 ** principal **   <a name="datazone-Type-PolicyGrantMember-principal"></a>
The principal of the policy grant member.
Type: [PolicyGrantPrincipal](API_PolicyGrantPrincipal.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_PolicyGrantMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/PolicyGrantMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/PolicyGrantMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/PolicyGrantMember)
