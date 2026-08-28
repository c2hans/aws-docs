---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProcessingS3Input.html
---

# ProcessingS3Input
<a name="API_ProcessingS3Input"></a>

Configuration for downloading input data from Amazon S3 into the processing container.

## Contents
<a name="API_ProcessingS3Input_Contents"></a>

 ** S3DataType **   <a name="sagemaker-Type-ProcessingS3Input-S3DataType"></a>
Whether you use an `S3Prefix` or a `ManifestFile` for the data type. If you choose `S3Prefix`, `S3Uri` identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for the processing job. If you choose `ManifestFile`, `S3Uri` identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for the processing job.
Type: String
Valid Values: `ManifestFile | S3Prefix`
Required: Yes

 ** S3Uri **   <a name="sagemaker-Type-ProcessingS3Input-S3Uri"></a>
The URI of the Amazon S3 prefix Amazon SageMaker downloads data required to run a processing job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** LocalPath **   <a name="sagemaker-Type-ProcessingS3Input-LocalPath"></a>
The local path in your container where you want Amazon SageMaker to write input data to. `LocalPath` is an absolute path to the input data and must begin with `/opt/ml/processing/`. `LocalPath` is a required parameter when `AppManaged` is `False` (default).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: No

 ** S3CompressionType **   <a name="sagemaker-Type-ProcessingS3Input-S3CompressionType"></a>
Whether to GZIP-decompress the data in Amazon S3 as it is streamed into the processing container. `Gzip` can only be used when `Pipe` mode is specified as the `S3InputMode`. In `Pipe` mode, Amazon SageMaker streams input data from the source directly to your container without using the EBS volume.
Type: String
Valid Values: `None | Gzip`
Required: No

 ** S3DataDistributionType **   <a name="sagemaker-Type-ProcessingS3Input-S3DataDistributionType"></a>
Whether to distribute the data from Amazon S3 to all processing instances with `FullyReplicated`, or whether the data from Amazon S3 is sharded by Amazon S3 key, downloading one shard of data to each processing instance.
Type: String
Valid Values: `FullyReplicated | ShardedByS3Key`
Required: No

 ** S3InputMode **   <a name="sagemaker-Type-ProcessingS3Input-S3InputMode"></a>
Whether to use `File` or `Pipe` input mode. In File mode, Amazon SageMaker copies the data from the input source onto the local ML storage volume before starting your processing container. This is the most commonly used input mode. In `Pipe` mode, Amazon SageMaker streams input data from the source directly to your processing container into named pipes without using the ML storage volume.
Type: String
Valid Values: `Pipe | File`
Required: No

## See Also
<a name="API_ProcessingS3Input_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ProcessingS3Input)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ProcessingS3Input)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ProcessingS3Input)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
