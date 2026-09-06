---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_ResponsePartitionKey.html
---

# ResponsePartitionKey
<a name="API_ResponsePartitionKey"></a>

If `PartitionBy` was specified in a `DescribeDimensionKeys` request, the dimensions are returned in an array. Each element in the array specifies one dimension.

## Contents
<a name="API_ResponsePartitionKey_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Dimensions **   <a name="performanceinsights-Type-ResponsePartitionKey-Dimensions"></a>
A dimension map that contains the dimensions for this partition.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: `.*\S.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_ResponsePartitionKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/ResponsePartitionKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/ResponsePartitionKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/ResponsePartitionKey)
