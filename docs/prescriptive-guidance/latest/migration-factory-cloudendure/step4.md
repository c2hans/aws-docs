---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-factory-cloudendure/step4.html
---

# Step 4. Perform migration boot-up testing
<a name="step4"></a>

After data replication is complete on all servers, you need to test the instance boot-up process and make sure that everything works as expected from the operating system perspective. That is, the EC2 instance must pass the 2/2 (system status and instance status) health checks.

## Launch servers for boot-up testing
<a name="4-launch-servers"></a>

If you're migrating a small number of servers, you can select the server and launch it directly from the MGN console. However, for large-scale migrations, it's more efficient to launch all the servers together from the Cloud Migration Factory web console. This console provides a single Launch servers button to automate the following processes:
+ Verifying replication status and making sure that the lag time is less than 180 minutes.
+ Updating the Amazon EC2 launch templates for all servers in the given wave with the metadata in the Cloud Migration Factory database.
+ Sending all servers to an MGN job and launching them in test mode.

For detailed instructions, see [Launch instances for testing](https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/list-of-automated-migration-activities-using-factory-web-console.html#launch-instances-for-testing) in the *Cloud Migration Factory Implementation Guide*.

## Verify instance boot-up status
<a name="4-status-check"></a>

It will take 15–30 minutes for the server instances to boot up. You can check the status manually by logging into the Amazon EC2 console, searching for the server name, and checking the status. You will see a "2/2 checks passed" message, which indicates that the instance is healthy from an infrastructure perspective.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-factory-cloudendure/images/guide-img/3ff8a3b6-fa4d-412f-ba5f-3d8aad3942a7/images/f5ea5253-7bf2-4660-90d8-cd18c2ececc7.png)

However, for a large-scale migration, it's time-consuming to check the status of each instance, so Cloud Migration Factory provides a single automation script to verify the 2/2 status for all machines in a given wave.

If an instance fails the 2/2 status checks, contact [AWS Support](https://aws.amazon.com/premiumsupport/) for assistance.

For detailed instructions, see [Verify the target instance status](https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/list-of-automated-migration-activities-using-factory-web-console.html#verify-the-target-instance-status) in the *Cloud Migration Factory Implementation Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
