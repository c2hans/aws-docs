---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_TagListEntry.html
---

# TagListEntry
<a name="API_TagListEntry"></a>

A key-value pair representing a single tag that's been applied to an AWS resource.

## Contents
<a name="API_TagListEntry_Contents"></a>

 ** Key **   <a name="DataSync-Type-TagListEntry-Key"></a>
The key for an AWS resource tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9\s+=._:/-]+$`
Required: Yes

 ** Value **   <a name="DataSync-Type-TagListEntry-Value"></a>
The value for an AWS resource tag.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[a-zA-Z0-9\s+=._:@/-]+$`
Required: No

## See Also
<a name="API_TagListEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/TagListEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/TagListEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/TagListEntry)
