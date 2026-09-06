---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

A tag that can be added to an MemoryDB resource. Tags are composed of a Key/Value pair. You can use tags to categorize and track all your MemoryDB resources. When you add or remove tags on clusters, those actions will be replicated to all nodes in the cluster. A tag with a null Value is permitted. For more information, see [Tagging your MemoryDB resources](https://docs.aws.amazon.com/MemoryDB/latest/devguide/tagging-resources.html)

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="MemoryDB-Type-Tag-Key"></a>
The key for the tag. May not be null.
Type: String
Required: No

 ** Value **   <a name="MemoryDB-Type-Tag-Value"></a>
The tag's value. May be null.
Type: String
Required: No

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/Tag)
