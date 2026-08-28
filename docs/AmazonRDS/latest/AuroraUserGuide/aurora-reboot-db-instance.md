---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-reboot-db-instance.html
---

# Rebooting a DB instance within an Aurora cluster
<a name="aurora-reboot-db-instance"></a>

 This procedure is the most important operation that you take when performing reboots with Aurora. Many of the maintenance procedures involve rebooting one or more Aurora DB instances in a particular order.

## Console
<a name="USER_RebootInstance.Console"></a>

**To reboot a DB instance**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1.  In the navigation pane, choose **Databases**, and then choose the DB instance that you want to reboot.

1.  For **Actions**, choose **Reboot**.

    The **Reboot DB Instance** page appears.

1.  Choose **Reboot** to reboot your DB instance.

    Or choose **Cancel**.

## AWS CLI
<a name="USER_RebootInstance.CLI"></a>

 To reboot a DB instance by using the AWS CLI, call the [`reboot-db-instance`](https://docs.aws.amazon.com/cli/latest/reference/rds/reboot-db-instance.html) command.

**Example**
For Linux, macOS, or Unix:

```
aws rds reboot-db-instance \
    --db-instance-identifier {{mydbinstance}}
```
For Windows:

```
aws rds reboot-db-instance ^
    --db-instance-identifier {{mydbinstance}}
```

## RDS API
<a name="USER_RebootInstance.API"></a>

 To reboot a DB instance by using the Amazon RDS API, call the [`RebootDBInstance`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RebootDBInstance.html) operation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
