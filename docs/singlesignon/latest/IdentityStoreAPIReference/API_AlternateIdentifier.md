---
source_url: https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_AlternateIdentifier.html
---

# AlternateIdentifier
<a name="API_AlternateIdentifier"></a>

A unique identifier for a user or group that is not the primary identifier. This value can be an identifier from an external identity provider (IdP) that is associated with the user, the group, or a unique attribute.

## Contents
<a name="API_AlternateIdentifier_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** ExternalId **   <a name="singlesignon-Type-AlternateIdentifier-ExternalId"></a>
The identifier issued to this resource by an external identity provider.
Type: [ExternalId](API_ExternalId.md) object
Required: No

 ** UniqueAttribute **   <a name="singlesignon-Type-AlternateIdentifier-UniqueAttribute"></a>
An entity attribute that's unique to a specific entity.
Type: [UniqueAttribute](API_UniqueAttribute.md) object
Required: No

## See Also
<a name="API_AlternateIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/identitystore-2020-06-15/AlternateIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/identitystore-2020-06-15/AlternateIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/identitystore-2020-06-15/AlternateIdentifier)
