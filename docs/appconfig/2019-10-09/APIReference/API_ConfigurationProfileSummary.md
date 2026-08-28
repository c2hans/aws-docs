---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ConfigurationProfileSummary.html
---

# ConfigurationProfileSummary
<a name="API_ConfigurationProfileSummary"></a>

A summary of a configuration profile.

## Contents
<a name="API_ConfigurationProfileSummary_Contents"></a>

 ** ApplicationId **   <a name="appconfig-Type-ConfigurationProfileSummary-ApplicationId"></a>
The application ID.
Type: String
Pattern: `[a-z0-9]{4,7}`
Required: No

 ** Id **   <a name="appconfig-Type-ConfigurationProfileSummary-Id"></a>
The ID of the configuration profile.
Type: String
Pattern: `[a-z0-9]{4,7}`
Required: No

 ** LocationUri **   <a name="appconfig-Type-ConfigurationProfileSummary-LocationUri"></a>
The URI location of the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** Name **   <a name="appconfig-Type-ConfigurationProfileSummary-Name"></a>
The name of the configuration profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Type **   <a name="appconfig-Type-ConfigurationProfileSummary-Type"></a>
The type of configurations contained in the profile. AWS AppConfig supports `feature flags` and `freeform` configurations. We recommend you create feature flag configurations to enable or disable new features and freeform configurations to distribute configurations to an application. When calling this API, enter one of the following values for `Type`:
 `AWS.AppConfig.FeatureFlags`
 `AWS.Freeform`
Type: String
Pattern: `^[a-zA-Z0-9\.\-]+`
Required: No

 ** ValidatorTypes **   <a name="appconfig-Type-ConfigurationProfileSummary-ValidatorTypes"></a>
The types of validators in the configuration profile.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `JSON_SCHEMA | LAMBDA`
Required: No

## See Also
<a name="API_ConfigurationProfileSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/ConfigurationProfileSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/ConfigurationProfileSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/ConfigurationProfileSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
