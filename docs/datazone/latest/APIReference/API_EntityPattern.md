---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_EntityPattern.html
---

# EntityPattern
<a name="API_EntityPattern"></a>

The pattern describing the entities to be matched during the graph query.

## Contents
<a name="API_EntityPattern_Contents"></a>

 ** entityType **   <a name="datazone-Type-EntityPattern-entityType"></a>
The type of entity to be matched during the graph query.
Type: String
Valid Values: `LINEAGE_NODE`
Required: Yes

 ** identifier **   <a name="datazone-Type-EntityPattern-identifier"></a>
The identifier of the root entity to start traversal from during the graph query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2086.
Required: Yes

 ** filters **   <a name="datazone-Type-EntityPattern-filters"></a>
A search filter clause in Amazon DataZone.
Type: [FilterClause](API_FilterClause.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_EntityPattern_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/EntityPattern)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/EntityPattern)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/EntityPattern)
