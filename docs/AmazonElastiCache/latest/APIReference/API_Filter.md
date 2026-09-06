---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_Filter.html
---

# Filter
<a name="API_Filter"></a>

Used to streamline results of a search based on the property being filtered.

## Contents
<a name="API_Filter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **
The property being filtered. For example, UserId.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** Values.member.N **
The property values to filter on. For example, "user-123".
Type: Array of strings
Array Members: Minimum number of 1 item.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/Filter)
