---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ConnectorProfile.html
---

# ConnectorProfile
<a name="API_ConnectorProfile"></a>

 Describes an instance of a connector. This includes the provided name, credentials ARN, connection-mode, and so on. To keep the API intuitive and extensible, the fields that are common to all types of connector profiles are explicitly specified at the top level. The rest of the connector-specific properties are available via the `connectorProfileProperties` field.

## Contents
<a name="API_ConnectorProfile_Contents"></a>

 ** connectionMode **   <a name="appflow-Type-ConnectorProfile-connectionMode"></a>
 Indicates the connection mode and if it is public or private.
Type: String
Valid Values: `Public | Private`
Required: No

 ** connectorLabel **   <a name="appflow-Type-ConnectorProfile-connectorLabel"></a>
The label for the connector profile being created.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[a-zA-Z0-9][\w!@#.-]+`
Required: No

 ** connectorProfileArn **   <a name="appflow-Type-ConnectorProfile-connectorProfileArn"></a>
 The Amazon Resource Name (ARN) of the connector profile.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `arn:aws:appflow:.*:[0-9]+:.*`
Required: No

 ** connectorProfileName **   <a name="appflow-Type-ConnectorProfile-connectorProfileName"></a>
 The name of the connector profile. The name is unique for each `ConnectorProfile` in the AWS account.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[\w/!@#+=.-]+`
Required: No

 ** connectorProfileProperties **   <a name="appflow-Type-ConnectorProfile-connectorProfileProperties"></a>
 The connector-specific properties of the profile configuration.
Type: [ConnectorProfileProperties](API_ConnectorProfileProperties.md) object
Required: No

 ** connectorType **   <a name="appflow-Type-ConnectorProfile-connectorType"></a>
 The type of connector, such as Salesforce, Amplitude, and so on.
Type: String
Valid Values: `Salesforce | Singular | Slack | Redshift | S3 | Marketo | Googleanalytics | Zendesk | Servicenow | Datadog | Trendmicro | Snowflake | Dynatrace | Infornexus | Amplitude | Veeva | EventBridge | LookoutMetrics | Upsolver | Honeycode | CustomerProfiles | SAPOData | CustomConnector | Pardot`
Required: No

 ** createdAt **   <a name="appflow-Type-ConnectorProfile-createdAt"></a>
 Specifies when the connector profile was created.
Type: Timestamp
Required: No

 ** credentialsArn **   <a name="appflow-Type-ConnectorProfile-credentialsArn"></a>
 The Amazon Resource Name (ARN) of the connector profile credentials.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `arn:aws:.*:.*:[0-9]+:.*`
Required: No

 ** lastUpdatedAt **   <a name="appflow-Type-ConnectorProfile-lastUpdatedAt"></a>
 Specifies when the connector profile was last updated.
Type: Timestamp
Required: No

 ** privateConnectionProvisioningState **   <a name="appflow-Type-ConnectorProfile-privateConnectionProvisioningState"></a>
 Specifies the private connection provisioning state.
Type: [PrivateConnectionProvisioningState](API_PrivateConnectionProvisioningState.md) object
Required: No

## See Also
<a name="API_ConnectorProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/ConnectorProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/ConnectorProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/ConnectorProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
