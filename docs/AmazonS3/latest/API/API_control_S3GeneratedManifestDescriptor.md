---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3GeneratedManifestDescriptor.html
---

# S3GeneratedManifestDescriptor
<a name="API_control_S3GeneratedManifestDescriptor"></a>

Describes the specified job's generated manifest. Batch Operations jobs created with a ManifestGenerator populate details of this descriptor after execution of the ManifestGenerator.

## Contents
<a name="API_control_S3GeneratedManifestDescriptor_Contents"></a>

 ** Format **   <a name="AmazonS3-Type-control_S3GeneratedManifestDescriptor-Format"></a>
The format of the generated manifest.
Type: String
Valid Values: `S3InventoryReport_CSV_20211130`
Required: No

 ** Location **   <a name="AmazonS3-Type-control_S3GeneratedManifestDescriptor-Location"></a>
Contains the information required to locate a manifest object. Manifests can't be imported from directory buckets. For more information, see [Directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html).
Type: [JobManifestLocation](API_control_JobManifestLocation.md) data type
Required: No

## See Also
<a name="API_control_S3GeneratedManifestDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3GeneratedManifestDescriptor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3GeneratedManifestDescriptor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3GeneratedManifestDescriptor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
