---
source_url: https://docs.aws.amazon.com/dms/latest/sbs/chap-on-premoracle2aurora.steps.createreplicationinstance.html
---

# Step 3: Create a Replication Instance
<a name="chap-on-premoracle2aurora.steps.createreplicationinstance"></a>

An AWS DMS replication instance performs the actual data migration between source and target. The replication instance also caches the changes during the migration. How much CPU and memory capacity a replication instance has influences the overall time required for the migration. Use the following procedure to set the parameters for a replication instance.

To create an AWS DMS replication instance, do the following:

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/), and open the AWS DMS console at https://console.aws.amazon.com/dms/v2/ and choose **Replication instances**. If you are signed in as an AWS Identity and Access Management (IAM) user, you must have the appropriate permissions to access AWS DMS. For more information on the permissions required, see [IAM Permissions](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#CHAP_Security.IAMPermissions).

1. Choose **Create replication instance**.

1. On the **Create replication instance** page, specify your replication instance information as shown following.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/dms/latest/sbs/chap-on-premoracle2aurora.steps.createreplicationinstance.html)

1. In the **Advanced** section, set the **Allocated storage (GB)** parameter, and then choose **Next**.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/dms/latest/sbs/chap-on-premoracle2aurora.steps.createreplicationinstance.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
