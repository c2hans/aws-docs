---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_BatchGetRouterInputError.html
---

# BatchGetRouterInputError
<a name="API_BatchGetRouterInputError"></a>

An error that occurred when retrieving multiple router inputs in the BatchGetRouterInput operation, including the ARN, error code, and error message.

## Contents
<a name="API_BatchGetRouterInputError_Contents"></a>

 ** arn **   <a name="mediaconnect-Type-BatchGetRouterInputError-arn"></a>
The Amazon Resource Name (ARN) of the router input for which the error occurred.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerInput:[a-z0-9]{12}`
Required: Yes

 ** code **   <a name="mediaconnect-Type-BatchGetRouterInputError-code"></a>
The error code associated with the error.
Type: String
Required: Yes

 ** message **   <a name="mediaconnect-Type-BatchGetRouterInputError-message"></a>
A message describing the error.
Type: String
Required: Yes

## See Also
<a name="API_BatchGetRouterInputError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/BatchGetRouterInputError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/BatchGetRouterInputError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/BatchGetRouterInputError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
