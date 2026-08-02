---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_OwnerProperties.html
---

# OwnerProperties
<a name="API_OwnerProperties"></a>

The properties of a domain unit's owner.

## Contents
<a name="API_OwnerProperties_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** group **   <a name="datazone-Type-OwnerProperties-group"></a>
Specifies that the domain unit owner is a group.
Type: [OwnerGroupProperties](API_OwnerGroupProperties.md) object
Required: No

 ** user **   <a name="datazone-Type-OwnerProperties-user"></a>
Specifies that the domain unit owner is a user.
Type: [OwnerUserProperties](API_OwnerUserProperties.md) object
Required: No

## See Also
<a name="API_OwnerProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/OwnerProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/OwnerProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/OwnerProperties)
