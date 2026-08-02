---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_RelationPattern.html
---

# RelationPattern
<a name="API_RelationPattern"></a>

The pattern describing the query's relational traversal.

## Contents
<a name="API_RelationPattern_Contents"></a>

 ** relationDirection **   <a name="datazone-Type-RelationPattern-relationDirection"></a>
The direction to query.
Type: String
Valid Values: `IN | OUT`
Required: Yes

 ** relationType **   <a name="datazone-Type-RelationPattern-relationType"></a>
The type of relation to query.
Type: String
Valid Values: `LINEAGE`
Required: Yes

 ** maxPathLength **   <a name="datazone-Type-RelationPattern-maxPathLength"></a>
The number of hops to query.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5.
Required: No

## See Also
<a name="API_RelationPattern_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/RelationPattern)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/RelationPattern)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/RelationPattern)
