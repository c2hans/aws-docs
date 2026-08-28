---
source_url: https://docs.aws.amazon.com/solutions/latest/cost-optimizer-for-workspaces/insights-dashboard.html
---

# Operation Insights Dashboard
<a name="insights-dashboard"></a>

Cost Optimizer for Amazon Workspaces comes with an Operational Insights dashboard that allows you to monitor the operation of the solution and get insight into the running hours that have been saved by using this solution.

To access this dashboard:

1. Go to the AWS CloudWatch console.

1. Select **Dashboards** from the navigation menu.

1. Find and select the dashboard named `{stack-name}-Dashboard`.

The dashboard will display various operational metrics about the operations of your solution including counts of how many Workspaces are analyzed by the solution, information on changes taken, and insights about the container that is performing the analysis.

Sample data below:

 **Cost Optimizer for Amazon WorkSpaces overview**

![insights](http://docs.aws.amazon.com/solutions/latest/cost-optimizer-for-workspaces/images/insights.png)

 **Cost Optimizer for Amazon WorkSpaces insights**

![insights2](http://docs.aws.amazon.com/solutions/latest/cost-optimizer-for-workspaces/images/insights2.png)

 **Additional costs associated with this feature**

| Service | Cost per month |
| --- | --- |
| Custom CloudWatch Dashboard | $3.00 |
| Amazon ECS | $3.30 |
|  **Total**  |  **$6.30 / month**  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Cost Optimizer for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
