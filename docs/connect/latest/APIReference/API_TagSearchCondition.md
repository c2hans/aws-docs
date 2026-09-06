---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_TagSearchCondition.html
---

# TagSearchCondition
<a name="API_TagSearchCondition"></a>

The search criteria to be used to return tags.

## Contents
<a name="API_TagSearchCondition_Contents"></a>

 ** tagKey **   <a name="connect-Type-TagSearchCondition-tagKey"></a>
The tag key used in the tag search condition.
Type: String
Length Constraints: Maximum length of 128.
Required: No

 ** tagKeyComparisonType **   <a name="connect-Type-TagSearchCondition-tagKeyComparisonType"></a>
The type of comparison to be made when evaluating the tag key in tag search condition.
Type: String
Valid Values: `STARTS_WITH | CONTAINS | EXACT`
Required: No

 ** tagValue **   <a name="connect-Type-TagSearchCondition-tagValue"></a>
The tag value used in the tag search condition.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** tagValueComparisonType **   <a name="connect-Type-TagSearchCondition-tagValueComparisonType"></a>
The type of comparison to be made when evaluating the tag value in tag search condition.
Type: String
Valid Values: `STARTS_WITH | CONTAINS | EXACT`
Required: No

## See Also
<a name="API_TagSearchCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/TagSearchCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/TagSearchCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/TagSearchCondition)
