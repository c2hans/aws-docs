---
source_url: https://docs.aws.amazon.com/connect-decisions/latest/adminguide/getting-started-accessing-your-instance.html
---

# Accessing your instance
<a name="getting-started-accessing-your-instance"></a>

 Using the console is the easiest way to manage your service resources and configurations. The console provides an intuitive web-based interface where you can view, create, modify, and monitor your resources.

 To access the Amazon Connect Decisions console, you must have a minimum set of permissions. These permissions must allow you to list and view details about the Amazon Connect Decisions resources in your AWS account. If you create an identity-based policy that is more restrictive than the minimum required permissions, the console won't function as intended for entities (users or roles) with that policy.

 You don't need to allow minimum console permissions for users that are making calls only to the or the AWS API. Instead, allow access to only the actions that match the API operation that they're trying to perform.

 As an Amazon Connect Decisions administrator, you should have received an email invite to the Amazon Connect Decisions web application.

1.  You can either choose the link in the email or on the Amazon Connect Decisions console dashboard, under **Sub-domain**, choose **web URL**.

1.  The **Amazon Connect Decisions** web application login page appears.

1.  Enter the AWS IAM Identity Center user credentials and choose **Sign in**.

1.  Each user that you added receives an email message with a link that goes to Amazon Connect Decisions, or you can choose **Copy link** and send the link to the users.

 After successfully logging in, you will land at your personalized Home Page. Refer to Understanding your Homepage in the user guide to understand your home page better.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
