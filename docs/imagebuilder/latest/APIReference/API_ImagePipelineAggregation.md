---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImagePipelineAggregation.html
---

# ImagePipelineAggregation
<a name="API_ImagePipelineAggregation"></a>

Contains vulnerability counts for a specific image pipeline.

## Contents
<a name="API_ImagePipelineAggregation_Contents"></a>

 ** imagePipelineArn **   <a name="imagebuilder-Type-ImagePipelineAggregation-imagePipelineArn"></a>
The Amazon Resource Name (ARN) that identifies the image pipeline for this aggregation.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):image-pipeline/[a-z0-9-_]+$`
Required: No

 ** severityCounts **   <a name="imagebuilder-Type-ImagePipelineAggregation-severityCounts"></a>
Counts by severity level for medium severity and higher level findings, plus a total for all of the findings for the specified image pipeline.
Type: [SeverityCounts](API_SeverityCounts.md) object
Required: No

## See Also
<a name="API_ImagePipelineAggregation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ImagePipelineAggregation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ImagePipelineAggregation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ImagePipelineAggregation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
