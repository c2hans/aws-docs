---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetRelationshipSummary.html
---

# AssetRelationshipSummary
<a name="API_AssetRelationshipSummary"></a>

Contains information about assets that are related to one another.

## Contents
<a name="API_AssetRelationshipSummary_Contents"></a>

 ** relationshipType **   <a name="iotsitewise-Type-AssetRelationshipSummary-relationshipType"></a>
The relationship type of the assets in this relationship. This value is one of the following:
+  `HIERARCHY` – The assets are related through an asset hierarchy. If you specify this relationship type, this asset relationship includes the `hierarchyInfo` object.
Type: String
Valid Values: `HIERARCHY`
Required: Yes

 ** hierarchyInfo **   <a name="iotsitewise-Type-AssetRelationshipSummary-hierarchyInfo"></a>
The assets that are related through an asset hierarchy.
This object is present if the `relationshipType` is `HIERARCHY`.
Type: [AssetHierarchyInfo](API_AssetHierarchyInfo.md) object
Required: No

## See Also
<a name="API_AssetRelationshipSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/AssetRelationshipSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/AssetRelationshipSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/AssetRelationshipSummary)
