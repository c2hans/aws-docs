---
source_url: https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-query-versions.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Managing query versions
<a name="query-editor-v2-query-versions"></a>

Every time you save a SQL query, the query editor v2 saves it as a new version. You can browse earlier query versions, save a copy of a query, or restore a query.

**To manage query versions**

1. Choose **Queries** from the navigation pane.

1. Open the context (right-click) menu for the query that you want to work with.

1. Choose **Version history** to open a list of versions of the query.

1. On the **Version history** page, you can do the following:
   + **Revert to selected** – Revert to the selected version and continue your work with this version.
   + **Save selected as** – Create a new query in the editor.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
