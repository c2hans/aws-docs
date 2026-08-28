---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/review-and-publish.html
---

# Review and publish your AWS Resilience Hub application
<a name="review-and-publish"></a>

After creating the application, you can still review the application and edit its resources. After you finish, choose **Publish** to publish the application.

**Note**
AWS Resilience Hub scans your application resources in the background and checks if they can be grouped in a more efficient way that will improve the accuracy of the assessments. If AWS Resilience Hub identifies resources that can be grouped into relevant AppComponents, it displays **Resource grouping recommendations** information alert in the **Application structure** tab of the application page and you can review them by choosing **Review recommendations**. For more information, see [AWS Resilience Hub resource grouping recommendations](grouping-recommendation.md).

For more information about reviewing the application and editing its resources, see the following:
+ [Viewing an AWS Resilience Hub application summary](view-app-summary.md)
+ [Editing AWS Resilience Hub application resources](application-resources.md)

## Next
<a name="run-assessment-start-next"></a>

 [Run an assessment of your AWS Resilience Hub application](run-assessment-start.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
