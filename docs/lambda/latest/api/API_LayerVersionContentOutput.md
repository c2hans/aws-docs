---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_LayerVersionContentOutput.html
---

# LayerVersionContentOutput
<a name="API_LayerVersionContentOutput"></a>

Details about a version of an [AWS Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html).

## Contents
<a name="API_LayerVersionContentOutput_Contents"></a>

 ** CodeSha256 **   <a name="lambda-Type-LayerVersionContentOutput-CodeSha256"></a>
The SHA-256 hash of the layer archive.
Type: String
Required: No

 ** CodeSize **   <a name="lambda-Type-LayerVersionContentOutput-CodeSize"></a>
The size of the layer archive in bytes.
Type: Long
Required: No

 ** Location **   <a name="lambda-Type-LayerVersionContentOutput-Location"></a>
A link to the layer archive in Amazon S3 that is valid for 10 minutes.
Type: String
Required: No

 ** ResolvedS3Object **   <a name="lambda-Type-LayerVersionContentOutput-ResolvedS3Object"></a>
The resolved Amazon S3 object that contains the layer archive.
Type: [ResolvedS3Object](API_ResolvedS3Object.md) object
Required: No

 ** SigningJobArn **   <a name="lambda-Type-LayerVersionContentOutput-SigningJobArn"></a>
The Amazon Resource Name (ARN) of a signing job.
Type: String
Required: No

 ** SigningProfileVersionArn **   <a name="lambda-Type-LayerVersionContentOutput-SigningProfileVersionArn"></a>
The Amazon Resource Name (ARN) for a signing profile version.
Type: String
Required: No

## See Also
<a name="API_LayerVersionContentOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/LayerVersionContentOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/LayerVersionContentOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/LayerVersionContentOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
