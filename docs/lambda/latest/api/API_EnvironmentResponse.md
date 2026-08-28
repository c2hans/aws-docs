---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_EnvironmentResponse.html
---

# EnvironmentResponse
<a name="API_EnvironmentResponse"></a>

The results of an operation to update or read environment variables. If the operation succeeds, the response contains the environment variables. If it fails, the response contains details about the error.

## Contents
<a name="API_EnvironmentResponse_Contents"></a>

 ** Error **   <a name="lambda-Type-EnvironmentResponse-Error"></a>
Error messages for environment variables that couldn't be applied.
Type: [EnvironmentError](API_EnvironmentError.md) object
Required: No

 ** Variables **   <a name="lambda-Type-EnvironmentResponse-Variables"></a>
Environment variable key-value pairs. Omitted from AWS CloudTrail logs.
Type: String to string map
Key Pattern: `[a-zA-Z]([a-zA-Z0-9_])+`
Required: No

## See Also
<a name="API_EnvironmentResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/EnvironmentResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/EnvironmentResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/EnvironmentResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
