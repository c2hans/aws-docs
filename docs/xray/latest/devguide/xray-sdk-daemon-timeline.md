---
source_url: https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-daemon-timeline.html
---

# X-Ray SDK and Daemon Support timeline
<a name="xray-sdk-daemon-timeline"></a>

The following table lists the dates and the level of support for X-Ray SDKs and Daemon.

| SDK and daemon phase | Start date | End date | Support provided |
| --- | --- | --- | --- |
| General availability | NA | February 25th, 2026 | X-Ray SDKs and Daemon are fully supported. AWS provides regular SDK and daemon releases that include bug and security fixes. |
| Maintenance mode | February 25th, 2026 | N/A | AWS will limit X-Ray SDK and Daemon releases to address security issues only. The SDKs/Daemon will not receive new feature enhancements. |

We recommend that you migrate to OpenTelemetry solutions for instrumenting your application and sending traces to AWS X-Ray. For more information on migrating to OpenTelemetry, see [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation ](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-migration.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
