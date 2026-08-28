---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_CodeSigningConfig.html
---

# CodeSigningConfig
<a name="API_CodeSigningConfig"></a>

Details about a [Code signing configuration](https://docs.aws.amazon.com/lambda/latest/dg/configuration-codesigning.html).

## Contents
<a name="API_CodeSigningConfig_Contents"></a>

 ** AllowedPublishers **   <a name="lambda-Type-CodeSigningConfig-AllowedPublishers"></a>
List of allowed publishers.
Type: [AllowedPublishers](API_AllowedPublishers.md) object
Required: Yes

 ** CodeSigningConfigArn **   <a name="lambda-Type-CodeSigningConfig-CodeSigningConfigArn"></a>
The Amazon Resource Name (ARN) of the Code signing configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}:\d{12}:code-signing-config:csc-[a-z0-9]{17}`
Required: Yes

 ** CodeSigningConfigId **   <a name="lambda-Type-CodeSigningConfig-CodeSigningConfigId"></a>
Unique identifer for the Code signing configuration.
Type: String
Pattern: `csc-[a-zA-Z0-9-_\.]{17}`
Required: Yes

 ** CodeSigningPolicies **   <a name="lambda-Type-CodeSigningConfig-CodeSigningPolicies"></a>
The code signing policy controls the validation failure action for signature mismatch or expiry.
Type: [CodeSigningPolicies](API_CodeSigningPolicies.md) object
Required: Yes

 ** LastModified **   <a name="lambda-Type-CodeSigningConfig-LastModified"></a>
The date and time that the Code signing configuration was last modified, in ISO-8601 format (YYYY-MM-DDThh:mm:ss.sTZD).
Type: String
Required: Yes

 ** Description **   <a name="lambda-Type-CodeSigningConfig-Description"></a>
Code signing configuration description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_CodeSigningConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/CodeSigningConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/CodeSigningConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/CodeSigningConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
