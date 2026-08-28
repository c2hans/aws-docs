---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/troubleshoot-connect-adobe-analytics.html
---

# I can't create or refresh a dataset from an existing Adobe Analytics data source
<a name="troubleshoot-connect-adobe-analytics"></a>

As of May 1, 2022, Quick Sight no longer supports legacy OAuth and version 1.3 and SOAP API operations in Adobe Analytics. If you experience failures while trying to create or refresh a dataset from an existing Adobe Analytics data source, you might have a stale access token.

**To troubleshoot failures while creating or refreshing a dataset from an existing Adobe Analytics data source**

1. Open Quick Sight and choose **Data** at left.

1. Choose **New** then **Dataset**.

1. On the **Create a dataset** page, choose the Adobe Analytics data source that you want to update from the list of existing data sources.

1. Choose **Edit data source**.

1. On the **Edit Adobe Analytics data source** page that opens, choose **Update data source** to reauthorize the Adobe Analytics connection.

1. Try recreating or refreshing the dataset again. The dataset creation or refresh should succeed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
