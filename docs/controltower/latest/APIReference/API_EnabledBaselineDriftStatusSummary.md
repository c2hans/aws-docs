---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnabledBaselineDriftStatusSummary.html
---

# EnabledBaselineDriftStatusSummary
<a name="API_EnabledBaselineDriftStatusSummary"></a>

The drift summary of the enabled baseline. AWS Control Tower reports inheritance drift when an enabled baseline configuration of a member account is different than the configuration that applies to the OU. AWS Control Tower reports this type of drift for a parent or child enabled baseline. One way to repair this drift by resetting the parent enabled baseline, on the OU.

For example, you may see this type of drift if you move accounts between OUs, but the accounts are not yet (re-)enrolled.

## Contents
<a name="API_EnabledBaselineDriftStatusSummary_Contents"></a>

 ** types **   <a name="controltower-Type-EnabledBaselineDriftStatusSummary-types"></a>
The types of drift that can be detected for an enabled baseline. AWS Control Tower detects inheritance drift on enabled baselines that apply at the OU level.
Type: [EnabledBaselineDriftTypes](API_EnabledBaselineDriftTypes.md) object
Required: No

## See Also
<a name="API_EnabledBaselineDriftStatusSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/EnabledBaselineDriftStatusSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/EnabledBaselineDriftStatusSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/EnabledBaselineDriftStatusSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
