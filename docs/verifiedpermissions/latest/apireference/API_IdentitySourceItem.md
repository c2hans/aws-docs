---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IdentitySourceItem.html
---

# IdentitySourceItem
<a name="API_IdentitySourceItem"></a>

A structure that defines an identity source.

This data type is a response parameter to the [ListIdentitySources](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListIdentitySources.html) operation.

## Contents
<a name="API_IdentitySourceItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** createdDate **   <a name="verifiedpermissions-Type-IdentitySourceItem-createdDate"></a>
The date and time the identity source was originally created.
Type: Timestamp
Required: Yes

 ** identitySourceId **   <a name="verifiedpermissions-Type-IdentitySourceItem-identitySourceId"></a>
The unique identifier of the identity source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-]*`
Required: Yes

 ** lastUpdatedDate **   <a name="verifiedpermissions-Type-IdentitySourceItem-lastUpdatedDate"></a>
The date and time the identity source was most recently updated.
Type: Timestamp
Required: Yes

 ** policyStoreId **   <a name="verifiedpermissions-Type-IdentitySourceItem-policyStoreId"></a>
The identifier of the policy store that contains the identity source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-/_]*`
Required: Yes

 ** principalEntityType **   <a name="verifiedpermissions-Type-IdentitySourceItem-principalEntityType"></a>
The Cedar entity type of the principals returned from the IdP associated with this identity source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `.*`
Required: Yes

 ** configuration **   <a name="verifiedpermissions-Type-IdentitySourceItem-configuration"></a>
Contains configuration information about an identity source.
Type: [ConfigurationItem](API_ConfigurationItem.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** details **   <a name="verifiedpermissions-Type-IdentitySourceItem-details"></a>
 *This member has been deprecated.*
A structure that contains the details of the associated identity provider (IdP).
Type: [IdentitySourceItemDetails](API_IdentitySourceItemDetails.md) object
Required: No

## See Also
<a name="API_IdentitySourceItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/IdentitySourceItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/IdentitySourceItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/IdentitySourceItem)
