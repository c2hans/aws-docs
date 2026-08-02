---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

A tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. You can use tags to categorize and track all your ElastiCache resources, with the exception of global replication group. When you add or remove tags on replication groups, those actions will be replicated to all nodes in the replication group. A tag with a null Value is permitted.

## Contents
<a name="API_Tag_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Key **
The key for the tag. May not be null.
Type: String
Required: No

 ** Value **
The tag's value. May be null.
Type: String
Required: No

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/Tag)
