---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/edit-quick-responses.html
---

# Edit quick responses in Connect Customer
<a name="edit-quick-responses"></a>

This topic explains how to use the Connect Customer admin website to edit a quick response. To edit a quick response programmatically, see [UpdateQuickResponse](https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_UpdateQuickResponse.html) in the *agent assist API Reference*.

**To edit a response**

1. Log in to the Connect Customer admin website at https://*instance name*.my.connect.aws/. Use an **Admin** account, or an account assigned to a security profile that has **Content Management - Quick responses - Edit** permission.

1. On the navigation bar, choose **Content Management**, then **Quick responses**.
![Menu showing Content Management and Quick responses.](http://docs.aws.amazon.com/connect/latest/adminguide/images/agent-application-1.png)

1. On the **Quick responses** page, choose the name of the quick response that you want to edit. You can also select the checkbox next to the response, then choose **Edit**.

1. As needed, change the following fields:
   + **Name**
   + **Description**
   + **Shortcut key**
   + **Routing Profiles**
   + **Activate/Deactivate quick response**
   + **Content**
   + **Channel**

1. Choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
