---
source_url: https://docs.aws.amazon.com/glue/latest/dg/console-crawlers-details.html
---

# Viewing crawler results and details
<a name="console-crawlers-details"></a>

 After the crawler runs successfully, it creates table definitions in the Data Catalog. Choose **Tables** in the navigation pane to see the tables that were created by your crawler in the database that you specified.

 You can view information related to the crawler itself as follows:
+ The **Crawlers** page on the AWS Glue console displays the following properties for a crawler:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/console-crawlers-details.html)
+  To view the history of a crawler, choose **Crawlers** in the navigation pane to see the crawlers you created. Choose a crawler from the list of available crawlers. You can view the crawler properties and view the crawler history in the **Crawler runs** tab.

   The Crawler runs tab displays information about each time the crawler ran, including ** Start time (UTC),** **End time (UTC)**, **Duration**, **Status**, **DPU hours**, and **Table changes**.

  The Crawler runs tab displays only the crawls that have occurred since the launch date of the crawler history feature, and only retains up to 12 months of crawls. Older crawls will not be returned.
+ To see additional information, choose a tab in the crawler details page. Each tab will display information related to the crawler.
  +  **Schedule**: Any schedules created for the crawler will be visible here.
  +  **Data sources**: All data sources scanned by the crawler will be visible here.
  +  **Classifiers**: All classifiers assigned to the crawler will be visible here.
  +  **Tags**: Any tags created and assigned to an AWS resource will be visible here.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
