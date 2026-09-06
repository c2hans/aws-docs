---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ExperimentRunSummary.html
---

# ExperimentRunSummary
<a name="API_ExperimentRunSummary"></a>

Summary information about an experiment run.

## Contents
<a name="API_ExperimentRunSummary_Contents"></a>

 ** Description **   <a name="appconfig-Type-ExperimentRunSummary-Description"></a>
A description of the experiment run.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** EndedAt **   <a name="appconfig-Type-ExperimentRunSummary-EndedAt"></a>
The date and time the experiment run ended, in ISO 8601 format.
Type: Timestamp
Required: No

 ** ExperimentDefinitionId **   <a name="appconfig-Type-ExperimentRunSummary-ExperimentDefinitionId"></a>
The experiment definition ID.
Type: String
Pattern: `[a-z0-9]{4,7}`
Required: No

 ** Run **   <a name="appconfig-Type-ExperimentRunSummary-Run"></a>
The experiment run number.
Type: Integer
Required: No

 ** StartedAt **   <a name="appconfig-Type-ExperimentRunSummary-StartedAt"></a>
The date and time the experiment run started, in ISO 8601 format.
Type: Timestamp
Required: No

 ** Status **   <a name="appconfig-Type-ExperimentRunSummary-Status"></a>
The current status of the experiment run.
Type: String
Valid Values: `RUNNING | DONE`
Required: No

 ** UpdatedAt **   <a name="appconfig-Type-ExperimentRunSummary-UpdatedAt"></a>
The date and time the experiment run was last updated, in ISO 8601 format.
Type: Timestamp
Required: No

## See Also
<a name="API_ExperimentRunSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/ExperimentRunSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/ExperimentRunSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/ExperimentRunSummary)
