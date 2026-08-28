---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_RegistrationConfig.html
---

# RegistrationConfig
<a name="API_RegistrationConfig"></a>

The registration configuration.

## Contents
<a name="API_RegistrationConfig_Contents"></a>

 ** roleArn **   <a name="iot-Type-RegistrationConfig-roleArn"></a>
The ARN of the role.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** templateBody **   <a name="iot-Type-RegistrationConfig-templateBody"></a>
The template body.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.
Pattern: `[\s\S]*`
Required: No

 ** templateName **   <a name="iot-Type-RegistrationConfig-templateName"></a>
The name of the provisioning template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9A-Za-z_-]+$`
Required: No

## See Also
<a name="API_RegistrationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/RegistrationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/RegistrationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/RegistrationConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
