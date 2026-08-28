---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/howtochangeURL.html
---

# Customizing the AWS access portal URL
<a name="howtochangeURL"></a>

By default, you can access the AWS access portal by using a URL that follows this format: `d-{{xxxxxxxxxx}}.awsapps.com/start`. You can customize the URL as follows: `{{your_subdomain}}.awsapps.com/start`.

**Important**
 If you change the AWS access portal URL, you cannot edit it later.

**To customize your URL**

1. Open the AWS IAM Identity Center console at [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/).

1. In the IAM Identity Center console, choose **Dashboard** in the navigation pane and locate the **Settings summary** section.

1. Choose the **Customize** button below your AWS access portal URL.
**Note**
If the **Customize** button doesn't display, it means that the AWS access portal has already been customized. Customizing the AWS access portal URL is a one-time operation that cannot be reversed.

1. Enter your desired subdomain name and choose **Save**.

You can now sign in to the AWS Console through your AWS access portal with your customized URL.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
