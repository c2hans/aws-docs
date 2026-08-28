---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_InvalidConfigurationDetail.html
---

# InvalidConfigurationDetail
<a name="API_InvalidConfigurationDetail"></a>

Detailed information about the bad request exception error when creating a hosted configuration version.

## Contents
<a name="API_InvalidConfigurationDetail_Contents"></a>

 ** Constraint **   <a name="appconfig-Type-InvalidConfigurationDetail-Constraint"></a>
The invalid or out-of-range validation constraint in your JSON schema that failed validation.
Type: String
Required: No

 ** Location **   <a name="appconfig-Type-InvalidConfigurationDetail-Location"></a>
Location of the validation constraint in the configuration JSON schema that failed validation.
Type: String
Required: No

 ** Reason **   <a name="appconfig-Type-InvalidConfigurationDetail-Reason"></a>
The reason for an invalid configuration error.
Type: String
Required: No

 ** Type **   <a name="appconfig-Type-InvalidConfigurationDetail-Type"></a>
The type of error for an invalid configuration.
Type: String
Required: No

 ** Value **   <a name="appconfig-Type-InvalidConfigurationDetail-Value"></a>
Details about an error with AWS Lambda when a synchronous extension experiences an error during an invocation.
Type: String
Required: No

## See Also
<a name="API_InvalidConfigurationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/InvalidConfigurationDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/InvalidConfigurationDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/InvalidConfigurationDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
