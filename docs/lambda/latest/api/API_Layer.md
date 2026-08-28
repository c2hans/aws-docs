---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_Layer.html
---

# Layer
<a name="API_Layer"></a>

An [AWS Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html).

## Contents
<a name="API_Layer_Contents"></a>

 ** Arn **   <a name="lambda-Type-Layer-Arn"></a>
The Amazon Resource Name (ARN) of the function layer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `arn:[a-zA-Z0-9-]+:lambda:[a-zA-Z0-9-]+:\d{12}:layer:[a-zA-Z0-9-_]+:[0-9]+`
Required: No

 ** CodeSize **   <a name="lambda-Type-Layer-CodeSize"></a>
The size of the layer archive in bytes.
Type: Long
Required: No

 ** SigningJobArn **   <a name="lambda-Type-Layer-SigningJobArn"></a>
The Amazon Resource Name (ARN) of a signing job.
Type: String
Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`
Required: No

 ** SigningProfileVersionArn **   <a name="lambda-Type-Layer-SigningProfileVersionArn"></a>
The Amazon Resource Name (ARN) for a signing profile version.
Type: String
Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`
Required: No

## See Also
<a name="API_Layer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/Layer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/Layer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/Layer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
