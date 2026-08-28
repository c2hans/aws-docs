---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/terminate-emr-serverless-application.html
---

# Stop or delete an EMR Serverless application from the Studio UI
<a name="terminate-emr-serverless-application"></a>

You can stop (transition to the `Stopped` state) or delete (transition to the `Deleted` state) an EMR Serverless application from the list of applications in the Studio UI.

**To stop or delete an application, navigate to the list of available EMR Serverless applications.**

1. In the Studio UI, navigate to the left-side panel and select the **Data** node in the left navigation menu. Then, scroll and choose the **Amazon EMR applications and clusters** option. This opens up a page that displays the Amazon EMR applications that you can access from within the Studio environment, under the **Serverless applications** tab.

1. Select the name of the application that you want to stop or delete, and then choose the corresponding **Stop** or **Delete** button.

1. A confirmation message informs you that any pending job will be lost permanently.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
