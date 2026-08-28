---
source_url: https://docs.aws.amazon.com/datazone/latest/userguide/create-new-project.html
---

# Create a new project
<a name="create-new-project"></a>

In Amazon DataZone, projects enable a group of users to collaborate on various business use cases that involve publishing, discovering, subscribing to, and consuming data assets in the Amazon DataZone catalog. For more information, see [Amazon DataZone terminology and concepts](datazone-concepts.md).

Any Amazon DataZone user with the required permissions to access the data portal can create an Amazon DataZone project.

To create a new project complete the following steps.

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone) and sign in with the AWS account where the domain was created, then choose **Open data portal**.

1. In the Amazon DataZone data portal, choose **Create Project**.

1. Specify values for the following fields, and then choose **Create project**:
   + **Name** – The project name.
   + **Description** – A description of the project.
   + **Domain unit** – The domain unit under which you want to create this project.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
