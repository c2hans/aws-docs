---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TransformS3DataSource.html
---

# TransformS3DataSource
<a name="API_TransformS3DataSource"></a>

Describes the S3 data source.

## Contents
<a name="API_TransformS3DataSource_Contents"></a>

 ** S3DataType **   <a name="sagemaker-Type-TransformS3DataSource-S3DataType"></a>
If you choose `S3Prefix`, `S3Uri` identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for batch transform.
If you choose `ManifestFile`, `S3Uri` identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for batch transform.
The following values are compatible: `ManifestFile`, `S3Prefix`
The following value is not compatible: `AugmentedManifestFile`
Type: String
Valid Values: `ManifestFile | S3Prefix | AugmentedManifestFile | Converse`
Required: Yes

 ** S3Uri **   <a name="sagemaker-Type-TransformS3DataSource-S3Uri"></a>
Depending on the value specified for the `S3DataType`, identifies either a key name prefix or a manifest. For example:
+  A key name prefix might look like this: `s3://bucketname/exampleprefix/`.
+  A manifest might look like this: `s3://bucketname/example.manifest`

   The manifest is an S3 object which is a JSON file with the following format:

   `[ {"prefix": "s3://customer_bucket/some/prefix/"},`

   `"relative/path/to/custdata-1",`

   `"relative/path/custdata-2",`

   `...`

   `"relative/path/custdata-N"`

   `]`

   The preceding JSON matches the following `S3Uris`:

   `s3://customer_bucket/some/prefix/relative/path/to/custdata-1`

   `s3://customer_bucket/some/prefix/relative/path/custdata-2`

   `...`

   `s3://customer_bucket/some/prefix/relative/path/custdata-N`

   The complete set of `S3Uris` in this manifest constitutes the input data for the channel for this datasource. The object that each `S3Uris` points to must be readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

## See Also
<a name="API_TransformS3DataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TransformS3DataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TransformS3DataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TransformS3DataSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
