---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DatasetStats.html
---

# DatasetStats
<a name="API_DatasetStats"></a>

 Provides statistics about a dataset. For more information, see [DescribeDataset](API_DescribeDataset.md).

## Contents
<a name="API_DatasetStats_Contents"></a>

 ** ErrorEntries **   <a name="rekognition-Type-DatasetStats-ErrorEntries"></a>
 The total number of entries that contain at least one error.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** LabeledEntries **   <a name="rekognition-Type-DatasetStats-LabeledEntries"></a>
 The total number of images in the dataset that have labels.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** TotalEntries **   <a name="rekognition-Type-DatasetStats-TotalEntries"></a>
 The total number of images in the dataset.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** TotalLabels **   <a name="rekognition-Type-DatasetStats-TotalLabels"></a>
 The total number of labels declared in the dataset.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_DatasetStats_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DatasetStats)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/DatasetStats)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/DatasetStats)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
