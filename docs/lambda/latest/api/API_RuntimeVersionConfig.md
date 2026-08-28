---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_RuntimeVersionConfig.html
---

# RuntimeVersionConfig
<a name="API_RuntimeVersionConfig"></a>

The ARN of the runtime and any errors that occured.

## Contents
<a name="API_RuntimeVersionConfig_Contents"></a>

 ** Error **   <a name="lambda-Type-RuntimeVersionConfig-Error"></a>
Error response when Lambda is unable to retrieve the runtime version for a function.
Type: [RuntimeVersionError](API_RuntimeVersionError.md) object
Required: No

 ** RuntimeVersionArn **   <a name="lambda-Type-RuntimeVersionConfig-RuntimeVersionArn"></a>
The ARN of the runtime version you want the function to use.
Type: String
Length Constraints: Minimum length of 26. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*):lambda:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}::runtime:.+`
Required: No

## See Also
<a name="API_RuntimeVersionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/RuntimeVersionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/RuntimeVersionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/RuntimeVersionConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
