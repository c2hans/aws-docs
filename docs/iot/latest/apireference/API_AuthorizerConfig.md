---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_AuthorizerConfig.html
---

# AuthorizerConfig
<a name="API_AuthorizerConfig"></a>

An object that specifies the authorization service for a domain.

## Contents
<a name="API_AuthorizerConfig_Contents"></a>

 ** allowAuthorizerOverride **   <a name="iot-Type-AuthorizerConfig-allowAuthorizerOverride"></a>
A Boolean that specifies whether the domain configuration's authorization service can be overridden.
Type: Boolean
Required: No

 ** defaultAuthorizerName **   <a name="iot-Type-AuthorizerConfig-defaultAuthorizerName"></a>
The name of the authorization service for a domain configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w=,@-]+`
Required: No

## See Also
<a name="API_AuthorizerConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/AuthorizerConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/AuthorizerConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/AuthorizerConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
