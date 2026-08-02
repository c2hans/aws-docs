---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImageAggregation.html
---

# ImageAggregation
<a name="API_ImageAggregation"></a>

Contains vulnerability counts for a specific image.

## Contents
<a name="API_ImageAggregation_Contents"></a>

 ** imageBuildVersionArn **   <a name="imagebuilder-Type-ImageAggregation-imageBuildVersionArn"></a>
The Amazon Resource Name (ARN) that identifies the image for this aggregation.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):image/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`
Required: No

 ** severityCounts **   <a name="imagebuilder-Type-ImageAggregation-severityCounts"></a>
Counts by severity level for medium severity and higher level findings, plus a total for all of the findings for the specified image.
Type: [SeverityCounts](API_SeverityCounts.md) object
Required: No

## See Also
<a name="API_ImageAggregation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ImageAggregation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ImageAggregation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ImageAggregation)
