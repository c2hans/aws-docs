---
source_url: https://docs.aws.amazon.com/dlm/latest/APIReference/API_LifecyclePolicySummary.html
---

# LifecyclePolicySummary
<a name="API_LifecyclePolicySummary"></a>

Summary information about a lifecycle policy.

## Contents
<a name="API_LifecyclePolicySummary_Contents"></a>

 ** DefaultPolicy **   <a name="dlm-Type-LifecyclePolicySummary-DefaultPolicy"></a>
 **[Default policies only]** The type of default policy. Values include:
+  `VOLUME` - Default policy for EBS snapshots
+  `INSTANCE` - Default policy for EBS-backed AMIs
Type: Boolean
Required: No

 ** Description **   <a name="dlm-Type-LifecyclePolicySummary-Description"></a>
The description of the lifecycle policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[0-9A-Za-z _-]+`
Required: No

 ** PolicyId **   <a name="dlm-Type-LifecyclePolicySummary-PolicyId"></a>
The identifier of the lifecycle policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `policy-[a-f0-9]+`
Required: No

 ** PolicyType **   <a name="dlm-Type-LifecyclePolicySummary-PolicyType"></a>
The type of policy. `EBS_SNAPSHOT_MANAGEMENT` indicates that the policy manages the lifecycle of Amazon EBS snapshots. `IMAGE_MANAGEMENT` indicates that the policy manages the lifecycle of EBS-backed AMIs. `EVENT_BASED_POLICY` indicates that the policy automates cross-account snapshot copies for snapshots that are shared with your account.
Type: String
Valid Values: `EBS_SNAPSHOT_MANAGEMENT | IMAGE_MANAGEMENT | EVENT_BASED_POLICY`
Required: No

 ** State **   <a name="dlm-Type-LifecyclePolicySummary-State"></a>
The activation state of the lifecycle policy.
Type: String
Valid Values: `ENABLED | DISABLED | ERROR`
Required: No

 ** Tags **   <a name="dlm-Type-LifecyclePolicySummary-Tags"></a>
The tags.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `[\p{all}]*`
Required: No

## See Also
<a name="API_LifecyclePolicySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dlm-2018-01-12/LifecyclePolicySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dlm-2018-01-12/LifecyclePolicySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dlm-2018-01-12/LifecyclePolicySummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Lifecycle Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dlm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
