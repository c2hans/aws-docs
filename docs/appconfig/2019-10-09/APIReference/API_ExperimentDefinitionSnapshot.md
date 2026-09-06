---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ExperimentDefinitionSnapshot.html
---

# ExperimentDefinitionSnapshot
<a name="API_ExperimentDefinitionSnapshot"></a>

A snapshot of the experiment definition captured at the time an experiment run was started. This preserves the configuration that was active during the run.

## Contents
<a name="API_ExperimentDefinitionSnapshot_Contents"></a>

 ** ApplicationId **   <a name="appconfig-Type-ExperimentDefinitionSnapshot-ApplicationId"></a>
The application ID at the time the run was started.
Type: String
Pattern: `[a-z0-9]{4,7}`
Required: No

 ** AudienceDescription **   <a name="appconfig-Type-ExperimentDefinitionSnapshot-AudienceDescription"></a>
The audience description at the time the run was started.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** AudienceRule **   <a name="appconfig-Type-ExperimentDefinitionSnapshot-AudienceRule"></a>
The audience rule at the time the run was started.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Required: No

 ** ConfigurationProfileId **   <a name="appconfig-Type-ExperimentDefinitionSnapshot-ConfigurationProfileId"></a>
The configuration profile ID at the time the run was started.
Type: String
Pattern: `[a-z0-9]{4,7}`
Required: No

 ** Control **   <a name="appconfig-Type-ExperimentDefinitionSnapshot-Control"></a>
The control treatment at the time the run was started.
Type: [Treatment](API_Treatment.md) object
Required: No

 ** EnvironmentId **   <a name="appconfig-Type-ExperimentDefinitionSnapshot-EnvironmentId"></a>
The environment ID at the time the run was started.
Type: String
Pattern: `[a-z0-9]{4,7}`
Required: No

 ** FlagKey **   <a name="appconfig-Type-ExperimentDefinitionSnapshot-FlagKey"></a>
The feature flag key at the time the run was started.
Type: String
Pattern: `^[a-z][a-zA-Z0-9_-]{1,64}`
Required: No

 ** Hypothesis **   <a name="appconfig-Type-ExperimentDefinitionSnapshot-Hypothesis"></a>
The hypothesis at the time the run was started.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** Id **   <a name="appconfig-Type-ExperimentDefinitionSnapshot-Id"></a>
The experiment definition ID.
Type: String
Pattern: `[a-z0-9]{4,7}`
Required: No

 ** LaunchCriteria **   <a name="appconfig-Type-ExperimentDefinitionSnapshot-LaunchCriteria"></a>
The launch criteria at the time the run was started.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** Name **   <a name="appconfig-Type-ExperimentDefinitionSnapshot-Name"></a>
The name of the experiment definition at the time the run was started.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Treatments **   <a name="appconfig-Type-ExperimentDefinitionSnapshot-Treatments"></a>
The treatments at the time the run was started.
Type: Array of [Treatment](API_Treatment.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

## See Also
<a name="API_ExperimentDefinitionSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/ExperimentDefinitionSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/ExperimentDefinitionSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/ExperimentDefinitionSnapshot)
