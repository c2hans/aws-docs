---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/ug/step-create-mpts-tab-output.html
---

# Output tab
<a name="step-create-mpts-tab-output"></a>

| Field | Description |
| --- | --- |
| URI, Interface, Virtual Source Address | Required. The address to the destination on the downstream system. Conductor Live will deliver the MPTS to this address. |
| Output listening | Check this field if you want to enable output listening, which is a form of resiliency that protects against failures within the muxing pipeline. You can only enable output listening if you have set up Elemental Statmux for 1-to-1 node redundancy because the feature requires two nodes.<br />For information about how this feature works when the MPTS is running, see [Resiliency features in Elemental Statmux](worker-nodes-other-resiliency.md). |
| Add Destination | Choose this button if you are implementing statmux output redundancy. With this redundancy feature, you want the Elemental Statmux node to deliver the MPTS to two different downstream systems. You must specify the destination of the second downstream system.<br />For information about how this feature works when the MPTS is running, see [Resiliency features in Elemental Statmux](worker-nodes-other-resiliency.md). |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
