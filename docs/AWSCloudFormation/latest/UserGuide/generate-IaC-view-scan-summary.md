---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/generate-IaC-view-scan-summary.html
---

# View the scan summary in the CloudFormation console
<a name="generate-IaC-view-scan-summary"></a>

After the scan completes, you can view a visualization of resources found during the scan to help you identify the concentration of resources across different product types.

**To view information about resources found during the scan**

1. Open the [IaC generator page](https://console.aws.amazon.com/cloudformation/home?#iac-generator) of the CloudFormation console.

1. On the navigation bar at the top of the screen, choose the AWS Region that contains the resource scan to view.

1. From the navigation pane, choose **IaC generator**.

1. Under **Scanned resources breakdown**, you'll find a visual breakdown of the scanned resources by product type, for example, **Compute** and **Storage**.

1. To customize the number of product types displayed, choose **Filter displayed data**. This helps you tailor the visualization to focus on the product types that you're most interested in.

1. On the right side of the page is the **Scan summary details** panel. To open the panel, choose the **open panel** icon.

![The IaC generator console provides a visual breakdown of scanned resources.](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/images/IaC-generator-scan-summary.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
