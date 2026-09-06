---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_Validator.html
---

# Validator
<a name="API_Validator"></a>

A validator provides a syntactic or semantic check to ensure the configuration that you want to deploy functions as intended. To validate your application configuration data, you provide a schema or an AWS Lambda function that runs against the configuration. The configuration deployment or update can only proceed when the configuration data is valid. For more information, see [About validators](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-profile.html#appconfig-creating-configuration-and-profile-validators) in the * AWS AppConfig User Guide*.

## Contents
<a name="API_Validator_Contents"></a>

 ** Content **   <a name="appconfig-Type-Validator-Content"></a>
Either the JSON Schema content or the Amazon Resource Name (ARN) of an Lambda function.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32768.
Required: Yes

 ** Type **   <a name="appconfig-Type-Validator-Type"></a>
 AWS AppConfig supports validators of type `JSON_SCHEMA` and `LAMBDA`
Type: String
Valid Values: `JSON_SCHEMA | LAMBDA`
Required: Yes

## See Also
<a name="API_Validator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/Validator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/Validator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/Validator)
