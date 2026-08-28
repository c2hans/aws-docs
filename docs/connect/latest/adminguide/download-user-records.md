---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/download-user-records.html
---

# Download a user list from your Connect Customer instance
<a name="download-user-records"></a>

You can export a list of users from Connect Customer to a CSV file. Use **Select all** to select all users from the search results, regardless of page. You can export over 1,000 users at once.

1. Log in to the Connect Customer admin website at https://{{instance name}}.my.connect.aws/. Use an **Admin** account, or an account assigned to a security profile that has **Users and permissions - Users - View** permissions.

1. In Connect Customer, on the left navigation menu, choose **Users**.

1. Select the users you want to export. To select all users from the search results, choose **Select all**. Then choose **Download CSV**.
![The User management page with all search results selected and the Download CSV option.](http://docs.aws.amazon.com/connect/latest/adminguide/images/user-cloudscape-bulk-download.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
