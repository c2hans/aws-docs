---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ConnectorHealth.html
---

# ConnectorHealth
<a name="API_ConnectorHealth"></a>

The health and connectivity status of a connector, including the last time the status was checked and any diagnostic message. Returned as part of the `Connector` structure.

## Contents
<a name="API_ConnectorHealth_Contents"></a>

 ** connectorStatus **   <a name="inspector2-Type-ConnectorHealth-connectorStatus"></a>
The health status of the connector.
Type: String
Valid Values: `CONNECTED | DEGRADED | FAILED_TO_CONNECT | PENDING_AUTHORIZATION | PENDING_CONFIGURATION | UNKNOWN`
Required: Yes

 ** lastCheckedAt **   <a name="inspector2-Type-ConnectorHealth-lastCheckedAt"></a>
The date and time when the connector health was last checked.
Type: Timestamp
Required: Yes

 ** message **   <a name="inspector2-Type-ConnectorHealth-message"></a>
A message providing additional details about the connector health status.
Type: String
Required: No

## See Also
<a name="API_ConnectorHealth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ConnectorHealth)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ConnectorHealth)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ConnectorHealth)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
