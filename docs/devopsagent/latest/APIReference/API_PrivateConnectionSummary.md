---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_PrivateConnectionSummary.html
---

# PrivateConnectionSummary
<a name="API_PrivateConnectionSummary"></a>

Summary of a Private Connection.

## Contents
<a name="API_PrivateConnectionSummary_Contents"></a>

 ** name **   <a name="devopsagent-Type-PrivateConnectionSummary-name"></a>
The name of the Private Connection.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 30.
Pattern: `[a-z0-9]([a-z0-9-]*[a-z0-9])?`
Required: Yes

 ** status **   <a name="devopsagent-Type-PrivateConnectionSummary-status"></a>
The status of the Private Connection.
Type: String
Valid Values: `ACTIVE | CREATE_IN_PROGRESS | CREATE_FAILED | DELETE_IN_PROGRESS | DELETE_FAILED`
Required: Yes

 ** type **   <a name="devopsagent-Type-PrivateConnectionSummary-type"></a>
The type of the Private Connection.
Type: String
Valid Values: `SELF_MANAGED | SERVICE_MANAGED`
Required: Yes

 ** certificateExpiryTime **   <a name="devopsagent-Type-PrivateConnectionSummary-certificateExpiryTime"></a>
The expiry time of the certificate associated with the Private Connection. Only present when a certificate is associated.
Type: Timestamp
Required: No

 ** dnsResolution **   <a name="devopsagent-Type-PrivateConnectionSummary-dnsResolution"></a>
DNS resolution mode for the Private Connection's resource gateway.
Type: String
Valid Values: `PUBLIC | IN_VPC`
Required: No

 ** failureMessage **   <a name="devopsagent-Type-PrivateConnectionSummary-failureMessage"></a>
Message describing the reason for a failed Private Connection, if applicable.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** hostAddress **   <a name="devopsagent-Type-PrivateConnectionSummary-hostAddress"></a>
IP address or DNS name of the target resource. Only present for service-managed Private Connections.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9.:\-]+`
Required: No

 ** resourceConfigurationId **   <a name="devopsagent-Type-PrivateConnectionSummary-resourceConfigurationId"></a>
The Resource Configuration ARN. Only present for self-managed Private Connections.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}|rcfg-[0-9a-z]{17})`
Required: No

 ** resourceGatewayId **   <a name="devopsagent-Type-PrivateConnectionSummary-resourceGatewayId"></a>
The service-managed Resource Gateway ARN. Only present for service-managed Private Connections.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourcegateway/rgw-[0-9a-z]{17}`
Required: No

 ** vpcId **   <a name="devopsagent-Type-PrivateConnectionSummary-vpcId"></a>
VPC identifier of the service-managed Resource Gateway. Only present for service-managed Private Connections.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 50.
Pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`
Required: No

## See Also
<a name="API_PrivateConnectionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/PrivateConnectionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/PrivateConnectionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/PrivateConnectionSummary)
