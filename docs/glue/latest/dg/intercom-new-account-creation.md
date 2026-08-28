---
source_url: https://docs.aws.amazon.com/glue/latest/dg/intercom-new-account-creation.html
---

# Creating a new Intercom account and configuring the client app
<a name="intercom-new-account-creation"></a>

**Creating a Intercom account**

1. Choose on the [Intercom URL](https://app.intercom.com/) and choose **Start my free trial** on right upper corner of the page.

1. Choose **Try for free button** on right upper corner of the page.

1. Choose the business type you require.

1. Enter all the information required on the page.

1. After entering all the information, choose **Register**.

**Creating an Intercom developer app**

To get the **Client Id** and **Client Secret**, you create a developer account.

1. Navigate to [https://app.intercom.com/](https://app.intercom.com/).

1. Enter the Email ID and Password/ Sign In Using Google and log in.

1. Choose **user profile** on the left bottom corner and choose settings.

1. Choose **Apps & Integration**.

1. Choose the **Developer Hub** tab under **Apps & Integration**.

1. Choose **New app** and create the app here.

1. Provide the app name and choose **Create** app.

1. Inside the app, navigate to the **Authentication** section.

1. Choose the **edit** and add redirect URIs. Add the your region-specific Redirect URL as `https://<aws-region>.console.aws.amazon.com/gluestudio/oauth`. For example, add `https://us-east-1.console.aws.amazon.com/gluestudio/oauth for the us-east-1 region`.

1. Get the generated **Client Id** and **Client Secret** in the Basic Information Section.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
