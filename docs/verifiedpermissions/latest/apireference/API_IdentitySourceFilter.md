---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IdentitySourceFilter.html
---

# IdentitySourceFilter
<a name="API_IdentitySourceFilter"></a>

A structure that defines characteristics of an identity source that you can use to filter.

This data type is a request parameter for the [ListIdentityStores](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListIdentityStores.html) operation.

## Contents
<a name="API_IdentitySourceFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** principalEntityType **   <a name="verifiedpermissions-Type-IdentitySourceFilter-principalEntityType"></a>
The Cedar entity type of the principals returned by the identity provider (IdP) associated with this identity source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `.*`
Required: No

## See Also
<a name="API_IdentitySourceFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/IdentitySourceFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/IdentitySourceFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/IdentitySourceFilter)
