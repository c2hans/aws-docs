---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_TagOptionDetail.html
---

# TagOptionDetail
<a name="API_TagOptionDetail"></a>

Information about a TagOption.

## Contents
<a name="API_TagOptionDetail_Contents"></a>

 ** Active **   <a name="servicecatalog-Type-TagOptionDetail-Active"></a>
The TagOption active state.
Type: Boolean
Required: No

 ** Id **   <a name="servicecatalog-Type-TagOptionDetail-Id"></a>
The TagOption identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** Key **   <a name="servicecatalog-Type-TagOptionDetail-Key"></a>
The TagOption key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** Owner **   <a name="servicecatalog-Type-TagOptionDetail-Owner"></a>
The AWS account Id of the owner account that created the TagOption.
Type: String
Required: No

 ** Value **   <a name="servicecatalog-Type-TagOptionDetail-Value"></a>
The TagOption value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_TagOptionDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/TagOptionDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/TagOptionDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/TagOptionDetail)
