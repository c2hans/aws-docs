---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-visualizations-additional-info.html
---

# Understanding the dollar estimate of the CPU cost for frames
<a name="working-with-visualizations-additional-info"></a>

Amazon CodeGuru Profiler provides an estimated dollar value for the active CPU cost of a frame. The value is an estimation that can help you understand where your optimization efforts will be most valuable.

To view a frame's dollar estimate, pause over the frame. When you pause over other frames, you see a dollar value estimation that's based on that frame's portion of the total CPU time.

**Note**
This estimated value does not represent your monthly bill.

The estimated dollar value shown on the **ALL** frame represents the yearly cost of the compute fleet seen during profiling. This is based on the on-demand AWS compute pricing in the AWS Region of your profiling group.

To view information about your compute fleet, choose **Actions**, then choose **Additional proﬁling data information**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
