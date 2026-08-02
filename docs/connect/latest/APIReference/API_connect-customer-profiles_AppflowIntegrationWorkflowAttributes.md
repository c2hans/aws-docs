---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_AppflowIntegrationWorkflowAttributes.html
---

# AppflowIntegrationWorkflowAttributes
<a name="API_connect-customer-profiles_AppflowIntegrationWorkflowAttributes"></a>

Structure holding all `APPFLOW_INTEGRATION` specific workflow attributes.

## Contents
<a name="API_connect-customer-profiles_AppflowIntegrationWorkflowAttributes_Contents"></a>

 ** ConnectorProfileName **   <a name="connect-Type-connect-customer-profiles_AppflowIntegrationWorkflowAttributes-ConnectorProfileName"></a>
The name of the AppFlow connector profile used for ingestion.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[\w/!@#+=.-]+`
Required: Yes

 ** SourceConnectorType **   <a name="connect-Type-connect-customer-profiles_AppflowIntegrationWorkflowAttributes-SourceConnectorType"></a>
Specifies the source connector type, such as Salesforce, ServiceNow, and Marketo. Indicates source of ingestion.
Type: String
Valid Values: `Salesforce | Marketo | Zendesk | Servicenow | S3`
Required: Yes

 ** RoleArn **   <a name="connect-Type-connect-customer-profiles_AppflowIntegrationWorkflowAttributes-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role. Customer Profiles assumes this role to create resources on your behalf as part of workflow execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_connect-customer-profiles_AppflowIntegrationWorkflowAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/AppflowIntegrationWorkflowAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/AppflowIntegrationWorkflowAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/AppflowIntegrationWorkflowAttributes)
