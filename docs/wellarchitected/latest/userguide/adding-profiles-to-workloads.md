---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/userguide/adding-profiles-to-workloads.html
---

# Adding a profile to a workload in AWS WA Tool
<a name="adding-profiles-to-workloads"></a>

You can add a profile to an existing workload, or when defining a workload, to speed up the workload review process. AWS WA Tool uses the information gathered from your profile to prioritize questions in the workload review that are relevant to your business.

For more information on adding a profile when defining a workload, see [Defining a workload in AWS WA Tool](define-workload.md).

**To add a profile to an existing workload**

1. Select **Workloads** in the left navigation pane, and select the name of the workload you want to associate with a profile.
**Note**
Only one profile can be associated with a workload.

1. In the **Profile** section, choose **Add profile**.

1. Select the profile you want to apply to the workload from the list of available profiles, or choose **Create profile**. For more information, see [Creating a profile](creating-a-profile.md).

1. Choose **Save**.

The **Workload overview** displays a count of prioritized questions answered and prioritized risks based on the information in the associated profile. Choose **Continue reviewing** to address the prioritized questions in the workload review. For more information, see [Documenting a workload in AWS WA Tool](start-workflow-review.md).

The **Profile** section displays the name, description, ARN, version, and last updated date for the profile associated with the workload.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
