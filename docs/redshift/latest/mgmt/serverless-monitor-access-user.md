---
source_url: https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-monitor-access-user.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Granting query monitoring permissions for a user
<a name="serverless-monitor-access-user"></a>

Users with `sys:monitor` permission can view all queries. In addition, users with `sys:operator` permission can cancel queries, analyze query history, and perform vacuum operations.

**To grant query monitoring permission for a user**

1. Enter the following command to provide system monitor access, where *user-name* is the name of the user for whom you want to provide access.

   ```
   grant role sys:monitor to "IAM:user-name";
   ```

1. (Optional) Enter the following command to provide system operator access, where *user-name* is the name of the user for whom you want to provide access.

   ```
   grant role sys:operator to "IAM:user-name";
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
