---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_S3Location.html
---

# S3Location
<a name="API_S3Location"></a>

Information about the location of application artifacts stored in Amazon S3.

## Contents
<a name="API_S3Location_Contents"></a>

 ** bucket **   <a name="CodeDeploy-Type-S3Location-bucket"></a>
The name of the Amazon S3 bucket where the application revision is stored.
Type: String
Required: No

 ** bundleType **   <a name="CodeDeploy-Type-S3Location-bundleType"></a>
The file type of the application revision. Must be one of the following:
+  `tar`: A tar archive file.
+  `tgz`: A compressed tar archive file.
+  `zip`: A zip archive file.
+  `YAML`: A YAML-formatted file.
+  `JSON`: A JSON-formatted file.
Type: String
Valid Values: `tar | tgz | zip | YAML | JSON`
Required: No

 ** eTag **   <a name="CodeDeploy-Type-S3Location-eTag"></a>
The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.
If the ETag is not specified as an input parameter, ETag validation of the object is skipped.
Type: String
Required: No

 ** key **   <a name="CodeDeploy-Type-S3Location-key"></a>
The name of the Amazon S3 object that represents the bundled artifacts for the application revision.
Type: String
Required: No

 ** version **   <a name="CodeDeploy-Type-S3Location-version"></a>
A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.
If the version is not specified, the system uses the most recent version by default.
Type: String
Required: No

## See Also
<a name="API_S3Location_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/S3Location)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/S3Location)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/S3Location)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
