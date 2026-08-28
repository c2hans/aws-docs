---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Events.RemovingSource.html
---

# Removing a source identifier from an Amazon RDS event notification subscription
<a name="USER_Events.RemovingSource"></a>

You can remove a source identifier (the Amazon RDS source generating the event) from a subscription if you no longer want to be notified of events for that source.

## Console
<a name="USER_Events.RemovingSource.Console"></a>

You can easily add or remove source identifiers using the Amazon RDS console by selecting or deselecting them when modifying a subscription. For more information, see [Modifying an Amazon RDS event notification subscription](USER_Events.Modifying.md).

## AWS CLI
<a name="USER_Events.RemovingSource.CLI"></a>

To remove a source identifier from an Amazon RDS event notification subscription, use the AWS CLI [`remove-source-identifier-from-subscription`](https://docs.aws.amazon.com/cli/latest/reference/rds/remove-source-identifier-from-subscription.html) command. Include the following required parameters:
+ `--subscription-name`
+ `--source-identifier`

**Example**
The following example removes the source identifier `mysqldb` from the `myrdseventsubscription` subscription.
For Linux, macOS, or Unix:

```
aws rds remove-source-identifier-from-subscription \
    --subscription-name {{myrdseventsubscription}} \
    --source-identifier {{mysqldb}}
```
For Windows:

```
aws rds remove-source-identifier-from-subscription ^
    --subscription-name {{myrdseventsubscription}} ^
    --source-identifier {{mysqldb}}
```

## API
<a name="USER_Events.RemovingSource.API"></a>

To remove a source identifier from an Amazon RDS event notification subscription, use the Amazon RDS API [`RemoveSourceIdentifierFromSubscription`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RemoveSourceIdentifierFromSubscription.html) command. Include the following required parameters:
+ `SubscriptionName`
+ `SourceIdentifier`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
