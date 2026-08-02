---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_MetadataInfo.html
---

# MetadataInfo
<a name="API_MetadataInfo"></a>

A structure containing metadata information for a schema version.

## Contents
<a name="API_MetadataInfo_Contents"></a>

 ** CreatedTime **   <a name="Glue-Type-MetadataInfo-CreatedTime"></a>
The time at which the entry was created.
Type: String
Required: No

 ** MetadataValue **   <a name="Glue-Type-MetadataInfo-MetadataValue"></a>
The metadata key’s corresponding value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9+-=._./@]+`
Required: No

 ** OtherMetadataValueList **   <a name="Glue-Type-MetadataInfo-OtherMetadataValueList"></a>
Other metadata belonging to the same metadata key.
Type: Array of [OtherMetadataValueListItem](API_OtherMetadataValueListItem.md) objects
Required: No

## See Also
<a name="API_MetadataInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/MetadataInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/MetadataInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/MetadataInfo)
