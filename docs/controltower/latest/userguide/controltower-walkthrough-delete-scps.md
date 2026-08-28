---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/controltower-walkthrough-delete-scps.html
---

# Delete SCPs
<a name="controltower-walkthrough-delete-scps"></a>

AWS Control Tower uses service control policies (SCPs) for its controls. This procedure walks through how to delete the SCPs specifically related to AWS Control Tower.

**To delete AWS Organizations SCPs**

1. Open the Organizations console at [https://console.aws.amazon.com/organizations/](https://console.aws.amazon.com/organizations/).

1. Open the **Policies** tab, and find the Service Control Policies (SCPs) that have the prefix **aws-guardrails-** and do the following for each SCP:

   1. Detach the SCP from the associated OU.

   1. Delete the SCP.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
