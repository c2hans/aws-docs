---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_PackageAggregationResponse.html
---

# PackageAggregationResponse
<a name="API_PackageAggregationResponse"></a>

A response that contains the results of a finding aggregation by image layer.

## Contents
<a name="API_PackageAggregationResponse_Contents"></a>

 ** packageName **   <a name="inspector2-Type-PackageAggregationResponse-packageName"></a>
The name of the operating system package.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** accountId **   <a name="inspector2-Type-PackageAggregationResponse-accountId"></a>
The ID of the AWS account associated with the findings.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** severityCounts **   <a name="inspector2-Type-PackageAggregationResponse-severityCounts"></a>
An object that contains the count of matched findings per severity.
Type: [SeverityCounts](API_SeverityCounts.md) object
Required: No

## See Also
<a name="API_PackageAggregationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/PackageAggregationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/PackageAggregationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/PackageAggregationResponse)
