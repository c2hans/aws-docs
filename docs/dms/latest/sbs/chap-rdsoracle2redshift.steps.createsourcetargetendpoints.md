---
source_url: https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2redshift.steps.createsourcetargetendpoints.html
---

# Step 8: Create AWS DMS Source and Target Endpoints
<a name="chap-rdsoracle2redshift.steps.createsourcetargetendpoints"></a>

While your replication instance is being created, you can specify the source and target database endpoints using the [AWS Management Console](https://console.aws.amazon.com/). However, you can only test connectivity after the replication instance has been created, because the replication instance is used in the connection.

1. Specify your connection information for the source Oracle database and the target Amazon Redshift database. The following table describes the source settings.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2redshift.steps.createsourcetargetendpoints.html)

   The following table describes the target settings.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2redshift.steps.createsourcetargetendpoints.html)

   The completed page should look like the following.
![Advanced section](http://docs.aws.amazon.com/dms/latest/sbs/images/sbs-rdsor2redshift19.5.png)

1. Wait for the status to say **Replication instance created successfully.**.

1. To test the source and target connections, choose **Run Test** for the source and target connections.

1. Choose **Next**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
