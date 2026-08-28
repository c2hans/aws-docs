---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/manage-endpoints-studio.html
---

# View endpoint details in SageMaker Studio
<a name="manage-endpoints-studio"></a>

In Amazon SageMaker Studio, you can view and manage your SageMaker AI Hosting endpoints. To learn more about Studio, see [Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio.html).

To find the list of your endpoints in SageMaker Studio do the following:

1. Open the Studio application.

1. In the left navigation pane, choose **Deployments**.

1. From the dropdown menu, choose **Endpoints**.

The **Endpoints** page opens, which lists all of your SageMaker AI Hosting endpoints. From this page, you can see the endpoints and their **Status**. You can also create a new endpoint, edit an existing endpoint, or delete an endpoint.

To see the details for a specific endpoint, choose an endpoint from the list. On the endpoint’s details page, you get an overview like the following screenshot.

![Screenshot of an endpoint's main page showing a summary of the endpoint details in Studio.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/inference/studio-endpoint-details-page.png)

Each endpoint details page contains the following tabs of information:

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
