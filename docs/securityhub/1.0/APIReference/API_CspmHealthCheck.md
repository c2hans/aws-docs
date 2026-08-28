---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CspmHealthCheck.html
---

# CspmHealthCheck
<a name="API_CspmHealthCheck"></a>

Information about the operational status and health of a CSPM connector.

## Contents
<a name="API_CspmHealthCheck_Contents"></a>

 ** ConnectorStatus **   <a name="securityhub-Type-CspmHealthCheck-ConnectorStatus"></a>
The connectivity status of the connector.
Type: String
Valid Values: `CONNECTED | DEGRADED | FAILED_TO_CONNECT | UNKNOWN`
Required: Yes

 ** LastCheckedAt **   <a name="securityhub-Type-CspmHealthCheck-LastCheckedAt"></a>
The ISO 8601 UTC timestamp indicating when the health status was last checked.
Type: Timestamp
Required: Yes

 ** Issues **   <a name="securityhub-Type-CspmHealthCheck-Issues"></a>
A list of health issues associated with the connector.
Type: Array of  objects
Required: No

 ** Message **   <a name="securityhub-Type-CspmHealthCheck-Message"></a>
A message describing the reason for the current connector status.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_CspmHealthCheck_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/CspmHealthCheck)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/CspmHealthCheck)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/CspmHealthCheck)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
