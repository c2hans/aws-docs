---
source_url: https://docs.aws.amazon.com/dms/latest/sbs/chap-mongodb2documentdb.03.html
---

# Create an AWS DMS replication instance for MongoDB migration
<a name="chap-mongodb2documentdb.03"></a>

To perform replication in AWS DMS, you need a replication instance.

1. Open the AWS DMS console at https://console.aws.amazon.com/dms/v2/.

1. In the navigation pane, choose **Replication instances**.

1. Choose **Create replication instance** and enter the following information:
   + For **Name**, enter `mongodb2docdb`.
   + For **Description**, enter `MongoDB to Amazon DocumentDB replication instance`.
   + For **Instance class**, keep the default value.
   + For **Engine version**, keep the default value.
   + For **VPC**, choose your default VPC.
   + For **Multi-AZ**, choose **No**.
   + For **Publicly accessible**, enable this option.

   When the settings are as you want them, choose **Create replication instance**.

**Note**
You can begin using your replication instance when its status becomes **available**. This can take several minutes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
