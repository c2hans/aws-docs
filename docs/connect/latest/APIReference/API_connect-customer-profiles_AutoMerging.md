---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_AutoMerging.html
---

# AutoMerging
<a name="API_connect-customer-profiles_AutoMerging"></a>

Configuration settings for how to perform the auto-merging of profiles.

## Contents
<a name="API_connect-customer-profiles_AutoMerging_Contents"></a>

 ** Enabled **   <a name="connect-Type-connect-customer-profiles_AutoMerging-Enabled"></a>
The flag that enables the auto-merging of duplicate profiles.
Type: Boolean
Required: Yes

 ** ConflictResolution **   <a name="connect-Type-connect-customer-profiles_AutoMerging-ConflictResolution"></a>
How the auto-merging process should resolve conflicts between different profiles. For example, if Profile A and Profile B have the same `FirstName` and `LastName` (and that is the matching criteria), which `EmailAddress` should be used?
Type: [ConflictResolution](API_connect-customer-profiles_ConflictResolution.md) object
Required: No

 ** Consolidation **   <a name="connect-Type-connect-customer-profiles_AutoMerging-Consolidation"></a>
A list of matching attributes that represent matching criteria. If two profiles meet at least one of the requirements in the matching attributes list, they will be merged.
Type: [Consolidation](API_connect-customer-profiles_Consolidation.md) object
Required: No

 ** MinAllowedConfidenceScoreForMerging **   <a name="connect-Type-connect-customer-profiles_AutoMerging-MinAllowedConfidenceScoreForMerging"></a>
A number between 0 and 1 that represents the minimum confidence score required for profiles within a matching group to be merged during the auto-merge process. A higher score means higher similarity required to merge profiles.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 1.0.
Required: No

## See Also
<a name="API_connect-customer-profiles_AutoMerging_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/AutoMerging)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/AutoMerging)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/AutoMerging)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
