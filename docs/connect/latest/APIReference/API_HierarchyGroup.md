---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_HierarchyGroup.html
---

# HierarchyGroup
<a name="API_HierarchyGroup"></a>

Contains information about a hierarchy group.

## Contents
<a name="API_HierarchyGroup_Contents"></a>

 ** Arn **   <a name="connect-Type-HierarchyGroup-Arn"></a>
The Amazon Resource Name (ARN) of the hierarchy group.
Type: String
Required: No

 ** HierarchyPath **   <a name="connect-Type-HierarchyGroup-HierarchyPath"></a>
Information about the levels in the hierarchy group.
Type: [HierarchyPath](API_HierarchyPath.md) object
Required: No

 ** Id **   <a name="connect-Type-HierarchyGroup-Id"></a>
The identifier of the hierarchy group.
Type: String
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-HierarchyGroup-LastModifiedRegion"></a>
The AWS Region where this resource was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-HierarchyGroup-LastModifiedTime"></a>
The timestamp when this resource was last modified.
Type: Timestamp
Required: No

 ** LevelId **   <a name="connect-Type-HierarchyGroup-LevelId"></a>
The identifier of the level in the hierarchy group.
Type: String
Required: No

 ** Name **   <a name="connect-Type-HierarchyGroup-Name"></a>
The name of the hierarchy group.
Type: String
Required: No

 ** Tags **   <a name="connect-Type-HierarchyGroup-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_HierarchyGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/HierarchyGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/HierarchyGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/HierarchyGroup)
