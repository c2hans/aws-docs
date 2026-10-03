---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_HealthCheck.html
---

# HealthCheck
<a name="API_HealthCheck"></a>

Information about the operational status and health of a connectorV2.

## Contents
<a name="API_HealthCheck_Contents"></a>

 ** ConnectorStatus **   <a name="securityhub-Type-HealthCheck-ConnectorStatus"></a>
The status of the connectorV2.
Type: String
Valid Values: `CONNECTED | DEGRADED | FAILED_TO_CONNECT | PENDING_AUTHORIZATION | PENDING_CONFIGURATION | UNKNOWN`
Required: Yes

 ** LastCheckedAt **   <a name="securityhub-Type-HealthCheck-LastCheckedAt"></a>
ISO 8601 UTC timestamp for the time check the health status of the connectorV2.
Type: Timestamp
Required: Yes

 ** Issues **   <a name="securityhub-Type-HealthCheck-Issues"></a>
A list of health issues associated with the connector, including error codes and messages.
Type: Array of [HealthIssue](API_HealthIssue.md) objects
Required: No

 ** Message **   <a name="securityhub-Type-HealthCheck-Message"></a>
The message for the reason of connectorStatus change.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_HealthCheck_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/HealthCheck)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/HealthCheck)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/HealthCheck)
