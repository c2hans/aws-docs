---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicNamedEntity.html
---

# TopicNamedEntity
<a name="API_TopicNamedEntity"></a>

A structure that represents a named entity.

## Contents
<a name="API_TopicNamedEntity_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** EntityName **   <a name="QS-Type-TopicNamedEntity-EntityName"></a>
The name of the named entity.
Type: String
Length Constraints: Maximum length of 256.
Required: Yes

 ** Definition **   <a name="QS-Type-TopicNamedEntity-Definition"></a>
The definition of a named entity.
Type: Array of [NamedEntityDefinition](API_NamedEntityDefinition.md) objects
Required: No

 ** EntityDescription **   <a name="QS-Type-TopicNamedEntity-EntityDescription"></a>
The description of the named entity.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** EntitySynonyms **   <a name="QS-Type-TopicNamedEntity-EntitySynonyms"></a>
The other names or aliases for the named entity.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** PresentationOrder **   <a name="QS-Type-TopicNamedEntity-PresentationOrder"></a>
The presentation order of the named entity.
Type: Integer
Required: No

 ** RankOrder **   <a name="QS-Type-TopicNamedEntity-RankOrder"></a>
The rank order of the named entity.
Type: Integer
Required: No

 ** SemanticEntityType **   <a name="QS-Type-TopicNamedEntity-SemanticEntityType"></a>
The type of named entity that a topic represents.
Type: [SemanticEntityType](API_SemanticEntityType.md) object
Required: No

 ** Sort **   <a name="QS-Type-TopicNamedEntity-Sort"></a>
The sort configuration of the named entity.
Type: Array of [NamedEntitySort](API_NamedEntitySort.md) objects
Array Members: Maximum number of 1 item.
Required: No

## See Also
<a name="API_TopicNamedEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopicNamedEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopicNamedEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopicNamedEntity)
