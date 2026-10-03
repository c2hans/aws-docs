---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_HealthIssue.html
---

# HealthIssue
<a name="API_HealthIssue"></a>

Represents a specific health issue detected for a connector.

## Contents
<a name="API_HealthIssue_Contents"></a>

 ** Code **   <a name="securityhub-Type-HealthIssue-Code"></a>
The error code that identifies the type of health issue.
Type: String
Valid Values: `AUTHENTICATION_FAILURE | STREAM_AUTHORIZATION_FAILURE | DISCOVERY_FAILURE | STREAM_LIMIT_EXCEEDED | STREAM_DISCONNECTED | RECORDING_FAILURE | NO_HEALTH_DATA`
Required: Yes

 ** Message **   <a name="securityhub-Type-HealthIssue-Message"></a>
A human-readable message that describes the health issue.
Type: String
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_HealthIssue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/HealthIssue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/HealthIssue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/HealthIssue)
