---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_AwsJsonSubstitutionCommandPreprocessorConfig.html
---

# AwsJsonSubstitutionCommandPreprocessorConfig
<a name="API_AwsJsonSubstitutionCommandPreprocessorConfig"></a>

Configures the command to treat the `payloadTemplate` as a JSON document for preprocessing. This preprocessor substitutes placeholders with parameter values to generate the command execution request payload.

## Contents
<a name="API_AwsJsonSubstitutionCommandPreprocessorConfig_Contents"></a>

 ** outputFormat **   <a name="iot-Type-AwsJsonSubstitutionCommandPreprocessorConfig-outputFormat"></a>
Converts the command preprocessor result to the format defined by this parameter, before sending it to the device.
Type: String
Valid Values: `JSON | CBOR`
Required: Yes

## See Also
<a name="API_AwsJsonSubstitutionCommandPreprocessorConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/AwsJsonSubstitutionCommandPreprocessorConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/AwsJsonSubstitutionCommandPreprocessorConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/AwsJsonSubstitutionCommandPreprocessorConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
