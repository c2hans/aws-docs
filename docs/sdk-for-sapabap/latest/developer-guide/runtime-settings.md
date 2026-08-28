---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/runtime-settings.html
---

# Runtime settings
<a name="runtime-settings"></a>

This section covers the following topics.

**Note**
These settings are not transportable and are local to each SAP system.

**Topics**
+ [Log and trace](#log-trace)
+ [OPT-IN: enhanced telemetry](#enhanced-telemetry)
+ [Active scenario](#active-scenario)

## Log and trace
<a name="log-trace"></a>

You can activate a trace for debugging purposes. It is recommended to keep the trace level at **No Trace**, unless diagnosing a technical issue. For more information, see secure operation.

These settings are not applicable to SDK for SAP ABAP - BTP edition.

## OPT-IN: enhanced telemetry
<a name="enhanced-telemetry"></a>

All SDKs send telemetry information to AWS for support purposes. You can opt in for enhanced telemetry. This is particularly useful when you contact Support to identify the source of a particular API call. For more information, see [Trace](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/additional-topics.html#trace) and [Telemetry](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/additional-topics.html#telemetry).

These settings are not applicable to SDK for SAP ABAP - BTP edition.

## Active scenario
<a name="active-scenario"></a>

Activate your `DEFAULT` scenario in this transaction. This activation is required only once for each system and should not be changed unless the system is undergoing a multi-Region disaster recovery. In a multi-Region setup, you can use this setting to switch your SAP system to a disaster recovery environment or disaster recovery test scenarios.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for SAP ABAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-sapabap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
