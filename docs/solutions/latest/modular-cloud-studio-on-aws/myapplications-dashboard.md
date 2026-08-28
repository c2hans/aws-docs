---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/myapplications-dashboard.html
---

# myApplications Dashboard
<a name="myapplications-dashboard"></a>

The solution also registers resources under an application on the AWS myApplications dashboard. From this centralized dashboard, you can view further cost insights and configure and view further metrics for your solution by using services such as Security Hub, CloudWatch, and Cost Explorer.

The following figure depicts an example of the application view for this solution stack in myApplications.

 **Application View**

![application view](http://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/images/application-view.png)

The application name follows the naming schema `modular-cloud-studio-on-aws-[Hub|Spoke]-[MCSDeploymentId]`. Each application is deployed and managed on a region-by-region basis. Hub region have the application created during initial deployment, spoke regions receive their dedicated applications automatically upon successful region enablement. Any EC2 instance launched within an MCS VPC will have its associated costs included and tracked under the respective application.

**Note**
Some Third-Party module resources may not be automatically tracked in this dashboard.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
