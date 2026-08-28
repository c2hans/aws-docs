---
source_url: https://docs.aws.amazon.com/dms/latest/sbs/bigquery-redshift-migration-step-6.html
---

# Step 6: Convert Database Schemas
<a name="bigquery-redshift-migration-step-6"></a>

After you create a new AWS SCT project, convert your source database schemas and apply converted code to your target database.

1. In the tree in the left panel, choose your source dataset. Open the context (right-click) menu, and choose **Convert schema**.

1. Choose **Yes** for the confirmation message. AWS SCT then converts your schema to the target database format.

1.  AWS SCT also generates the assessment report. This report includes database objects that require manual conversion. To view this report, choose **View**, and then choose **Assessment report view**.

1. On the **Action items** tab, AWS SCT provides you with the recommended actions for each conversion issue.

1. Check the report and make changes in your source or converted code where necessary. You can optionally save the report as a .CSV or .PDF file for later analysis.

1. Choose **Action Items**, and review any recommendations that you see.

1. In the tree in the right panel, choose the converted schema. Open the context (right-click) menu, and choose **Apply to database** to apply the schema scripts to the target Amazon Redshift cluster.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
