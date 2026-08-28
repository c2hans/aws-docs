---
source_url: https://docs.aws.amazon.com/dms/latest/userguide/getting-started-apply.html
---

# Apply the converted code for DMS Schema Conversion
<a name="getting-started-apply"></a>

DMS Schema Conversion doesn't immediately apply the converted code to your target database. To update your target database, you can use the SQL scripts that you created in the previous step. Alternatively, use the following procedure to apply the converted code from DMS Schema Conversion.

**To apply the converted code**

1. In the target database pane, choose the converted database schema. Also, select the check box for the name of this schema.

1. For **Actions**, choose **Apply changes**. The **Apply changes** dialog box appears.

1. Choose **Apply** to confirm your choice.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
