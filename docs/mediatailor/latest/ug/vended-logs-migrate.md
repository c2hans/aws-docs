---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/vended-logs-migrate.html
---

# Migrating your AWS Elemental MediaTailor logging strategy
<a name="vended-logs-migrate"></a>

 If you change the log strategy from Legacy CloudWatch to vended logs, MediaTailor will make this change as soon as you save the updates. To avoid interruptions in your logging workflow, use the following steps to migrate your logging strategy.

1. Follow the steps as described in [Using vended logs](vended-logs.md). For [Enable vended logs in MediaTailor](vended-logs.md#vended-logs-config), select *both* logging strategies (**Vended logs** and **Legacy CloudWatch**).

   MediaTailor will send logs through both vended logs and directly to CloudWatch Logs.

1. Make the necessary changes in your workflow that are dependent on your logging strategy and delivery destination.

1. Revisit [Enable vended logs in MediaTailor](vended-logs.md#vended-logs-config) and remove **Legacy CloudWatch** from the **Logging strategies**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
