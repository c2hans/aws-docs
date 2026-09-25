---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_Integration.html
---

# Integration
<a name="API_Integration"></a>

A connection between CloudWatch and an external system — such as a source of telemetry or configuration data, a messaging destination, or a model provider.

## Contents
<a name="API_Integration_Contents"></a>

 ** integrationId **   <a name="cloudwatchomni-Type-Integration-integrationId"></a>
The unique identifier of the integration.
Type: String
Required: Yes

 ** integrationType **   <a name="cloudwatchomni-Type-Integration-integrationType"></a>
The type of external system that an integration connects to, such as a source of configuration data, a messaging destination, or a model provider.
Type: String
Valid Values: `AWS_CONFIG_SLREC | SLACK | EXTERNAL_AGENT | AWS_INTEGRATION`
Required: Yes

 ** name **   <a name="cloudwatchomni-Type-Integration-name"></a>
The customer-provided name of the integration.
Type: String
Required: Yes

 ** status **   <a name="cloudwatchomni-Type-Integration-status"></a>
The current lifecycle state of an integration.
Type: String
Valid Values: `ACTIVE | DELETED | PENDING | PENDING_OAUTH | ERROR | FAILED`
Required: Yes

 ** authorizationUrl **   <a name="cloudwatchomni-Type-Integration-authorizationUrl"></a>
The URL the customer visits to authorize the integration. Present while an OAuth authorization is pending.
Type: String
Required: No

 ** authType **   <a name="cloudwatchomni-Type-Integration-authType"></a>
The authentication method that an integration uses to connect to its external system.
Type: String
Valid Values: `NONE | OAUTH2 | API_KEY`
Required: No

 ** createdAt **   <a name="cloudwatchomni-Type-Integration-createdAt"></a>
The time at which the integration was created.
Type: Timestamp
Required: No

 ** credentialArn **   <a name="cloudwatchomni-Type-Integration-credentialArn"></a>
The Amazon Resource Name (ARN) of the secret that stores the integration's credentials.
Type: String
Required: No

 ** errorMessage **   <a name="cloudwatchomni-Type-Integration-errorMessage"></a>
A human-readable description of why the integration is in an ERROR or FAILED state. Present only when the integration has failed.
Type: String
Required: No

 ** integrationArn **   <a name="cloudwatchomni-Type-Integration-integrationArn"></a>
The Amazon Resource Name (ARN) of the integration.
Type: String
Required: No

 ** integrationAttributes **   <a name="cloudwatchomni-Type-Integration-integrationAttributes"></a>
Provider-specific key/value attributes that configure the integration.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** roleArn **   <a name="cloudwatchomni-Type-Integration-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that CloudWatch assumes to access the external system.
Type: String
Required: No

 ** scope **   <a name="cloudwatchomni-Type-Integration-scope"></a>
Whether this integration is account-scoped (ACCOUNT, customer-created) or organization-scoped (ORGANIZATION, created by an org-enablement rule). Absent on legacy records is treated as ACCOUNT.
Type: String
Valid Values: `ACCOUNT | ORGANIZATION`
Required: No

 ** updatedAt **   <a name="cloudwatchomni-Type-Integration-updatedAt"></a>
The time at which the integration was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_Integration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/Integration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/Integration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/Integration)
