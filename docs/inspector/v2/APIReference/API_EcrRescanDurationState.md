---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_EcrRescanDurationState.html
---

# EcrRescanDurationState
<a name="API_EcrRescanDurationState"></a>

Details about the state of your ECR re-scan duration settings. The ECR re-scan duration defines how long an ECR image will be actively scanned by Amazon Inspector. When the number of days since an image was last pushed exceeds the duration configured for image pull date, and the duration configured for image pull date, the monitoring state of that image becomes `inactive` and all associated findings are scheduled for closure.

## Contents
<a name="API_EcrRescanDurationState_Contents"></a>

 ** pullDateRescanDuration **   <a name="inspector2-Type-EcrRescanDurationState-pullDateRescanDuration"></a>
The rescan duration configured for image pull date.
Type: String
Valid Values: `DAYS_14 | DAYS_30 | DAYS_60 | DAYS_90 | DAYS_180 | DAYS_3 | DAYS_7`
Required: No

 ** pullDateRescanMode **   <a name="inspector2-Type-EcrRescanDurationState-pullDateRescanMode"></a>
The pull date for the re-scan mode.
Type: String
Valid Values: `LAST_PULL_DATE | LAST_IN_USE_AT`
Required: No

 ** rescanDuration **   <a name="inspector2-Type-EcrRescanDurationState-rescanDuration"></a>
The rescan duration configured for image push date.
Type: String
Valid Values: `LIFETIME | DAYS_30 | DAYS_180 | DAYS_14 | DAYS_60 | DAYS_90 | DAYS_3 | DAYS_7`
Required: No

 ** status **   <a name="inspector2-Type-EcrRescanDurationState-status"></a>
The status of changes to the ECR automated re-scan duration.
Type: String
Valid Values: `SUCCESS | PENDING | FAILED`
Required: No

 ** updatedAt **   <a name="inspector2-Type-EcrRescanDurationState-updatedAt"></a>
A timestamp representing when the last time the ECR scan duration setting was changed.
Type: Timestamp
Required: No

## See Also
<a name="API_EcrRescanDurationState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/EcrRescanDurationState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/EcrRescanDurationState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/EcrRescanDurationState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
