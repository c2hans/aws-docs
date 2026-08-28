---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ExperimentDefinitionSummary.html
---

# ExperimentDefinitionSummary
<a name="API_ExperimentDefinitionSummary"></a>

Summary information about an experiment definition.

## Contents
<a name="API_ExperimentDefinitionSummary_Contents"></a>

 ** ApplicationId **   <a name="appconfig-Type-ExperimentDefinitionSummary-ApplicationId"></a>
The application ID.
Type: String
Pattern: `[a-z0-9]{4,7}`
Required: No

 ** ConfigurationProfileId **   <a name="appconfig-Type-ExperimentDefinitionSummary-ConfigurationProfileId"></a>
The configuration profile ID associated with the experiment.
Type: String
Pattern: `[a-z0-9]{4,7}`
Required: No

 ** CreatedAt **   <a name="appconfig-Type-ExperimentDefinitionSummary-CreatedAt"></a>
The date and time the experiment definition was created, in ISO 8601 format.
Type: Timestamp
Required: No

 ** EnvironmentId **   <a name="appconfig-Type-ExperimentDefinitionSummary-EnvironmentId"></a>
The environment ID where the experiment runs.
Type: String
Pattern: `[a-z0-9]{4,7}`
Required: No

 ** FlagKey **   <a name="appconfig-Type-ExperimentDefinitionSummary-FlagKey"></a>
The key of the feature flag used by the experiment.
Type: String
Pattern: `^[a-z][a-zA-Z0-9_-]{1,64}`
Required: No

 ** Hypothesis **   <a name="appconfig-Type-ExperimentDefinitionSummary-Hypothesis"></a>
The hypothesis that the experiment is designed to validate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** Id **   <a name="appconfig-Type-ExperimentDefinitionSummary-Id"></a>
The experiment definition ID.
Type: String
Pattern: `[a-z0-9]{4,7}`
Required: No

 ** Name **   <a name="appconfig-Type-ExperimentDefinitionSummary-Name"></a>
The name of the experiment definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Status **   <a name="appconfig-Type-ExperimentDefinitionSummary-Status"></a>
The current status of the experiment definition.
Type: String
Valid Values: `ACTIVE | IDLE | ARCHIVED`
Required: No

 ** UpdatedAt **   <a name="appconfig-Type-ExperimentDefinitionSummary-UpdatedAt"></a>
The date and time the experiment definition was last updated, in ISO 8601 format.
Type: Timestamp
Required: No

## See Also
<a name="API_ExperimentDefinitionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/ExperimentDefinitionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/ExperimentDefinitionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/ExperimentDefinitionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
