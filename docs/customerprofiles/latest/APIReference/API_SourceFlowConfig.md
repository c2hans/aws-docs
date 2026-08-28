---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_SourceFlowConfig.html
---

# SourceFlowConfig
<a name="API_connect-customer-profiles_SourceFlowConfig"></a>

Contains information about the configuration of the source connector used in the flow.

## Contents
<a name="API_connect-customer-profiles_SourceFlowConfig_Contents"></a>

 ** ConnectorType **   <a name="connect-Type-connect-customer-profiles_SourceFlowConfig-ConnectorType"></a>
The type of connector, such as Salesforce, Marketo, and so on.
Type: String
Valid Values: `Salesforce | Marketo | Zendesk | Servicenow | S3`
Required: Yes

 ** SourceConnectorProperties **   <a name="connect-Type-connect-customer-profiles_SourceFlowConfig-SourceConnectorProperties"></a>
Specifies the information that is required to query a particular source connector.
Type: [SourceConnectorProperties](API_connect-customer-profiles_SourceConnectorProperties.md) object
Required: Yes

 ** ConnectorProfileName **   <a name="connect-Type-connect-customer-profiles_SourceFlowConfig-ConnectorProfileName"></a>
The name of the AppFlow connector profile. This name must be unique for each connector profile in the AWS account.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[\w/!@#+=.-]+`
Required: No

 ** IncrementalPullConfig **   <a name="connect-Type-connect-customer-profiles_SourceFlowConfig-IncrementalPullConfig"></a>
Defines the configuration for a scheduled incremental data pull. If a valid configuration is provided, the fields specified in the configuration are used when querying for the incremental data pull.
Type: [IncrementalPullConfig](API_connect-customer-profiles_IncrementalPullConfig.md) object
Required: No

## See Also
<a name="API_connect-customer-profiles_SourceFlowConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/SourceFlowConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/SourceFlowConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/SourceFlowConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
