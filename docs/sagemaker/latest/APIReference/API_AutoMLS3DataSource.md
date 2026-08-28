---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLS3DataSource.html
---

# AutoMLS3DataSource
<a name="API_AutoMLS3DataSource"></a>

Describes the Amazon S3 data source.

## Contents
<a name="API_AutoMLS3DataSource_Contents"></a>

 ** S3DataType **   <a name="sagemaker-Type-AutoMLS3DataSource-S3DataType"></a>
The data type.
+ If you choose `S3Prefix`, `S3Uri` identifies a key name prefix. SageMaker AI uses all objects that match the specified key name prefix for model training.

  The `S3Prefix` should have the following format:

   `s3://DOC-EXAMPLE-BUCKET/DOC-EXAMPLE-FOLDER-OR-FILE`
+ If you choose `ManifestFile`, `S3Uri` identifies an object that is a manifest file containing a list of object keys that you want SageMaker AI to use for model training.

  A `ManifestFile` should have the format shown below:

   `[ {"prefix": "s3://DOC-EXAMPLE-BUCKET/DOC-EXAMPLE-FOLDER/DOC-EXAMPLE-PREFIX/"}, `

   `"DOC-EXAMPLE-RELATIVE-PATH/DOC-EXAMPLE-FOLDER/DATA-1",`

   `"DOC-EXAMPLE-RELATIVE-PATH/DOC-EXAMPLE-FOLDER/DATA-2",`

   `... "DOC-EXAMPLE-RELATIVE-PATH/DOC-EXAMPLE-FOLDER/DATA-N" ]`
+ If you choose `AugmentedManifestFile`, `S3Uri` identifies an object that is an augmented manifest file in JSON lines format. This file contains the data you want to use for model training. `AugmentedManifestFile` is available for V2 API jobs only (for example, for jobs created by calling `CreateAutoMLJobV2`).

  Here is a minimal, single-record example of an `AugmentedManifestFile`:

   `{"source-ref": "s3://DOC-EXAMPLE-BUCKET/DOC-EXAMPLE-FOLDER/cats/cat.jpg",`

   `"label-metadata": {"class-name": "cat"` }

  For more information on `AugmentedManifestFile`, see [Provide Dataset Metadata to Training Jobs with an Augmented Manifest File](https://docs.aws.amazon.com/sagemaker/latest/dg/augmented-manifest.html).
Type: String
Valid Values: `ManifestFile | S3Prefix | AugmentedManifestFile`
Required: Yes

 ** S3Uri **   <a name="sagemaker-Type-AutoMLS3DataSource-S3Uri"></a>
The URL to the Amazon S3 data source. The Uri refers to the Amazon S3 prefix or ManifestFile depending on the data type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

## See Also
<a name="API_AutoMLS3DataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AutoMLS3DataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AutoMLS3DataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AutoMLS3DataSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
