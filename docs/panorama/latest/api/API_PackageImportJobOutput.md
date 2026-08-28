---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_PackageImportJobOutput.html
---

# PackageImportJobOutput
<a name="API_PackageImportJobOutput"></a>

Results of a package import job.

## Contents
<a name="API_PackageImportJobOutput_Contents"></a>

 ** OutputS3Location **   <a name="panorama-Type-PackageImportJobOutput-OutputS3Location"></a>
The package's output location.
Type: [OutPutS3Location](API_OutPutS3Location.md) object
Required: Yes

 ** PackageId **   <a name="panorama-Type-PackageImportJobOutput-PackageId"></a>
The package's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_\/]+`
Required: Yes

 ** PackageVersion **   <a name="panorama-Type-PackageImportJobOutput-PackageVersion"></a>
The package's version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([0-9]+)\.([0-9]+)`
Required: Yes

 ** PatchVersion **   <a name="panorama-Type-PackageImportJobOutput-PatchVersion"></a>
The package's patch version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-z0-9]+`
Required: Yes

## See Also
<a name="API_PackageImportJobOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/PackageImportJobOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/PackageImportJobOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/PackageImportJobOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Panorama. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query panorama` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
