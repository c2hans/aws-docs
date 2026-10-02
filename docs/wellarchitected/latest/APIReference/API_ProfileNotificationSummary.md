---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ProfileNotificationSummary.html
---

# ProfileNotificationSummary
<a name="API_ProfileNotificationSummary"></a>

The profile notification summary.

## Contents
<a name="API_ProfileNotificationSummary_Contents"></a>

 ** CurrentProfileVersion **   <a name="wellarchitected-Type-ProfileNotificationSummary-CurrentProfileVersion"></a>
The current profile version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[A-Za-z0-9-]+`
Required: No

 ** LatestProfileVersion **   <a name="wellarchitected-Type-ProfileNotificationSummary-LatestProfileVersion"></a>
The latest profile version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[A-Za-z0-9-]+`
Required: No

 ** ProfileArn **   <a name="wellarchitected-Type-ProfileNotificationSummary-ProfileArn"></a>
The profile ARN.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2084.
Pattern: `arn:aws[-a-z]*:wellarchitected:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:profile/[a-z0-9]+`
Required: No

 ** ProfileName **   <a name="wellarchitected-Type-ProfileNotificationSummary-ProfileName"></a>
The profile name.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Required: No

 ** Type **   <a name="wellarchitected-Type-ProfileNotificationSummary-Type"></a>
Type of notification.
Type: String
Valid Values: `PROFILE_ANSWERS_UPDATED | PROFILE_DELETED`
Required: No

 ** WorkloadId **   <a name="wellarchitected-Type-ProfileNotificationSummary-WorkloadId"></a>
The ID assigned to the workload. This ID is unique within an AWS Region.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`
Required: No

 ** WorkloadName **   <a name="wellarchitected-Type-ProfileNotificationSummary-WorkloadName"></a>
The name of the workload.
The name must be unique within an account within an AWS Region. Spaces and capitalization are ignored when checking for uniqueness.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Required: No

## See Also
<a name="API_ProfileNotificationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ProfileNotificationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ProfileNotificationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ProfileNotificationSummary)
