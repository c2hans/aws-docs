---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryCodeOutput.html
---

# CanaryCodeOutput
<a name="API_CanaryCodeOutput"></a>

This structure contains information about the canary's Lambda handler and where its code is stored by CloudWatch Synthetics.

## Contents
<a name="API_CanaryCodeOutput_Contents"></a>

 ** BlueprintTypes **   <a name="synthetics-Type-CanaryCodeOutput-BlueprintTypes"></a>
 `BlueprintTypes` is a list of templates that enable simplified canary creation. You can create canaries for common monitoring scenarios by providing only a JSON configuration file instead of writing custom scripts. The only supported value is `multi-checks`.
Multi-checks monitors HTTP/DNS/SSL/TCP endpoints with built-in authentication schemes (Basic, API Key, OAuth, SigV4) and assertion capabilities. When you specify `BlueprintTypes`, the `Handler` field cannot be specified since the blueprint provides a pre-defined entry point.
 `BlueprintTypes` is supported only on canaries for syn-nodejs-3.0 runtime or later.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[0-9a-zA-Z_\-\.]+`
Required: No

 ** Dependencies **   <a name="synthetics-Type-CanaryCodeOutput-Dependencies"></a>
A list of dependencies that are used for running this canary. The dependencies are specified as a key-value pair, where the key is the type of dependency and the value is the dependency reference.
Type: Array of [Dependency](API_Dependency.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** Handler **   <a name="synthetics-Type-CanaryCodeOutput-Handler"></a>
The entry point to use for the source code when running the canary.
This field is required when you don't specify `BlueprintTypes` and is not allowed when you specify `BlueprintTypes`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** SourceLocationArn **   <a name="synthetics-Type-CanaryCodeOutput-SourceLocationArn"></a>
The ARN of the Lambda layer where Synthetics stores the canary script code.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_CanaryCodeOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/CanaryCodeOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/CanaryCodeOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/CanaryCodeOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Synthetics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSynthetics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
