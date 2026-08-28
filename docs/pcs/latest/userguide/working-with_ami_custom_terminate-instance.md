---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/working-with_ami_custom_terminate-instance.html
---

# Step 7 – Terminate the temporary instance
<a name="working-with_ami_custom_terminate-instance"></a>

After you have confirmed that your AMI works as intended with AWS PCS, you can terminate the temporary instance to stop incurring charges for it.

**To terminate the temporary instance**

1.  Open the [Amazon EC2 console](https://console.aws.amazon.com/ec2).

1.  In the navigation pane, choose **Instances**.

1.  Select the temporary instance that you created and choose **Actions**, **Instance state**, **Terminate instance**.

1.  When prompted to confirm, choose **Terminate**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
