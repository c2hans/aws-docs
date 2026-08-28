---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_Milestone.html
---

# Milestone
<a name="API_Milestone"></a>

A milestone return object.

## Contents
<a name="API_Milestone_Contents"></a>

 ** MilestoneName **   <a name="wellarchitected-Type-Milestone-MilestoneName"></a>
The name of the milestone in a workload.
Milestone names must be unique within a workload.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Required: No

 ** MilestoneNumber **   <a name="wellarchitected-Type-Milestone-MilestoneNumber"></a>
The milestone number.
A workload can have a maximum of 100 milestones.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** RecordedAt **   <a name="wellarchitected-Type-Milestone-RecordedAt"></a>
The date and time recorded in Unix format (seconds).
Type: Timestamp
Required: No

 ** Workload **   <a name="wellarchitected-Type-Milestone-Workload"></a>
A workload return object.
Type: [Workload](API_Workload.md) object
Required: No

## See Also
<a name="API_Milestone_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/Milestone)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/Milestone)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/Milestone)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected Tool. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
