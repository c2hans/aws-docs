---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_JobManifest.html
---

# JobManifest
<a name="API_control_JobManifest"></a>

Contains the configuration information for a job's manifest.

## Contents
<a name="API_control_JobManifest_Contents"></a>

 ** Location **   <a name="AmazonS3-Type-control_JobManifest-Location"></a>
Contains the information required to locate the specified job's manifest. Manifests can't be imported from directory buckets. For more information, see [Directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html).
Type: [JobManifestLocation](API_control_JobManifestLocation.md) data type
Required: Yes

 ** Spec **   <a name="AmazonS3-Type-control_JobManifest-Spec"></a>
Describes the format of the specified job's manifest. If the manifest is in CSV format, also describes the columns contained within the manifest.
Type: [JobManifestSpec](API_control_JobManifestSpec.md) data type
Required: Yes

## See Also
<a name="API_control_JobManifest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/JobManifest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/JobManifest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/JobManifest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
