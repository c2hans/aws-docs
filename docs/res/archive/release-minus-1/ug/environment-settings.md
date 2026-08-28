---
source_url: https://docs.aws.amazon.com/res/archive/release-minus-1/ug/environment-settings.html
---

# Environment settings
<a name="environment-settings"></a>

The **Environment settings** page displays product configuration details, such as:
+ General

  You can edit the web portal title and subtitle, and add custom links to the web portal login page. To configure custom links:

  1. Navigate to **Environment Management** > **Environment Settings**.

  1. Under the **General** tab, choose **Edit**.

  1. In the **Custom Links** section, choose **Add Link**.

  1. Enter a **Title** and **URL** for each link you want to display on the login page.

  1. Choose **Submit** to save your changes.

  Custom links appear on the web portal login page, allowing administrators to direct users to resources such as internal documentation, support pages, or acceptable use policies.
![Custom links configuration in Environment Settings](http://docs.aws.amazon.com/res/archive/release-minus-1/ug/images/web-links-edit-form.png)
+ Identity Provider

  Displays information such as Single Sign-On status.
+ Network

  Displays VPC ID, Prefix list IDs for access.
+ Directory Service

  Displays active directory settings and service account secrets manager ARN for username and password.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Research and Engineering Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query res` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
