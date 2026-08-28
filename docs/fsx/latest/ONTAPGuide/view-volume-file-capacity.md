---
source_url: https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/view-volume-file-capacity.html
---

# Monitoring a volume's file capacity
<a name="view-volume-file-capacity"></a>

You can use either of the following methods to view the maximum number of files allowed and the number of files already used on a volume.
+ The CloudWatch volume metrics `FilesCapacity` and `FilesUsed`.
+ In the Amazon FSx console, navigate to the **Available files (inodes)** chart in your volume's **Monitoring** tab. The following image shows the **Available files (inodes)** on a volume decreasing over time.
![Image of a volume's Available files (inodes) graph in the Monitoring tab, as seen in the Amazon FSx console.](http://docs.aws.amazon.com/fsx/latest/ONTAPGuide/images/fsx-ontap-available-files.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
