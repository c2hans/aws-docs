---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_LayerVersionContentInput.html
---

# LayerVersionContentInput
<a name="API_LayerVersionContentInput"></a>

A ZIP archive that contains the contents of an [AWS Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html). You can specify either an Amazon S3 location, or upload a layer archive directly.

## Contents
<a name="API_LayerVersionContentInput_Contents"></a>

 ** S3Bucket **   <a name="lambda-Type-LayerVersionContentInput-S3Bucket"></a>
The Amazon S3 bucket of the layer archive.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[0-9A-Za-z\.\-_]*(?<!\.)`
Required: No

 ** S3Key **   <a name="lambda-Type-LayerVersionContentInput-S3Key"></a>
The Amazon S3 key of the layer archive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** S3ObjectStorageMode **   <a name="lambda-Type-LayerVersionContentInput-S3ObjectStorageMode"></a>
Specifies how the layer archive is stored. Valid values:
+  `COPY` (default) – Uploads a copy of your layer archive to Lambda.
+  `REFERENCE` – Lambda references the layer archive from the specified Amazon S3 bucket.
Type: String
Valid Values: `COPY | REFERENCE`
Required: No

 ** S3ObjectVersion **   <a name="lambda-Type-LayerVersionContentInput-S3ObjectVersion"></a>
For versioned objects, the version of the layer archive object to use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** ZipFile **   <a name="lambda-Type-LayerVersionContentInput-ZipFile"></a>
The base64-encoded contents of the layer archive. AWS SDK and AWS CLI clients handle the encoding for you.
Type: Base64-encoded binary data object
Required: No

## See Also
<a name="API_LayerVersionContentInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/LayerVersionContentInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/LayerVersionContentInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/LayerVersionContentInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
