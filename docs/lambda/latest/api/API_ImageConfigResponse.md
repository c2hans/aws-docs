---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_ImageConfigResponse.html
---

# ImageConfigResponse
<a name="API_ImageConfigResponse"></a>

Response to a `GetFunctionConfiguration` request.

## Contents
<a name="API_ImageConfigResponse_Contents"></a>

 ** Error **   <a name="lambda-Type-ImageConfigResponse-Error"></a>
Error response to `GetFunctionConfiguration`.
Type: [ImageConfigError](API_ImageConfigError.md) object
Required: No

 ** ImageConfig **   <a name="lambda-Type-ImageConfigResponse-ImageConfig"></a>
Configuration values that override the container image Dockerfile.
Type: [ImageConfig](API_ImageConfig.md) object
Required: No

## See Also
<a name="API_ImageConfigResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/ImageConfigResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/ImageConfigResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/ImageConfigResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
