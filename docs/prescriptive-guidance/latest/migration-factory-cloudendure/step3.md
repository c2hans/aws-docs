---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-factory-cloudendure/step3.html
---

# Step 3. Validate the migration
<a name="step3"></a>

After installing the replication agent on the source machines, you monitor the status of data replication and resolve issues such as permissions or network performance.

If you have a small migration, you can verify the replication status manually from the MGN console. However, if you have large-scale migrations, servers across multiple projects, and servers in multiple waves, this verification can be difficult. For example, if you have 100 servers in wave 1, you must repeat the following steps 100 times to verify their replication status:
+ Find the target AWS account and Region for the server.
+ Log in to the MGN console, and then search for the server name.
+ Check the progress bar and update the status of the server on your spreadsheet.

Cloud Migration Factory includes an automation script that you run once for all servers. The script retries every 5 minutes until the status of every server in wave 1 changes to *Continuous Data Replication*, and it updates the replication status in the Cloud Migration Factory database.

For detailed instructions, see [Verify the replication status](https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/list-of-automated-migration-activities-using-factory-web-console.html#verify-the-replication-status) in the *Cloud Migration Factory Implementation Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
