---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DataSetReference.html
---

# DataSetReference
<a name="API_DataSetReference"></a>

Contains information about the dataset use and it's source.

## Contents
<a name="API_DataSetReference_Contents"></a>

 ** datasetArn **   <a name="iotsitewise-Type-DataSetReference-datasetArn"></a>
The [ARN](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) of the dataset. The format is `arn:${Partition}:iotsitewise:${Region}:${Account}:dataset/${DatasetId}`.
Type: String
Required: No

 ** source **   <a name="iotsitewise-Type-DataSetReference-source"></a>
The data source for the dataset.
Type: [Source](API_Source.md) object
Required: No

## See Also
<a name="API_DataSetReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DataSetReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DataSetReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DataSetReference)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
