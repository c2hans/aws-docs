---
source_url: https://docs.aws.amazon.com/application-discovery/latest/userguide/applications.html
---

AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

# Grouping servers in the AWS Migration Hub console
<a name="applications"></a>

Some of your discovered servers might need to be migrated together to remain functional. In this case, you can logically define and group discovered servers into applications.

As part of the grouping process, you can search, filter, and add tags.

**To group servers into a new or existing application**

1. Using your AWS account, sign in to the AWS Management Console and open the Migration Hub console at [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/).

1. In the Migration Hub console navigation pane under **Discover**, choose **Servers**.

1. In the servers list, select each server that you want to group into a new or existing application.

   To help choose servers for your group, you can search and filter on any criteria that you specify in the server list. Click inside the search bar and choose an item from the list, choose an operator from the next list, and then type in your criteria.

1. Optional: For each selected server, choose **Add tag**, type a value for **Key**, and then optionally type a value for **Value**.

1. Choose **Group as application** to create your application, or add to an existing one.

1. In the **Group as application** dialog box, choose **Group as a new application** or **Add to an existing application**.

   1. If you chose **Group as a new application**, type a name for **Application name**. Optionally, you can type a description for **Application description**.

   1. If you chose **Add to an existing application**, select the name of the application to add to in the list.

1. Choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
