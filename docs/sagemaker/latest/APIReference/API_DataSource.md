---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DataSource.html
---

# DataSource
<a name="API_DataSource"></a>

Describes the location of the channel data.

## Contents
<a name="API_DataSource_Contents"></a>

 ** DatasetSource **   <a name="sagemaker-Type-DataSource-DatasetSource"></a>
 The dataset resource that's associated with a channel.
Type: [DatasetSource](API_DatasetSource.md) object
Required: No

 ** FileSystemDataSource **   <a name="sagemaker-Type-DataSource-FileSystemDataSource"></a>
The file system that is associated with a channel.
Type: [FileSystemDataSource](API_FileSystemDataSource.md) object
Required: No

 ** S3DataSource **   <a name="sagemaker-Type-DataSource-S3DataSource"></a>
The S3 location of the data source that is associated with a channel.
Type: [S3DataSource](API_S3DataSource.md) object
Required: No

## See Also
<a name="API_DataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DataSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
