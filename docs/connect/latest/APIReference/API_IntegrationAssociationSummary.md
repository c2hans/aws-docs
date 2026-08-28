---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_IntegrationAssociationSummary.html
---

# IntegrationAssociationSummary
<a name="API_IntegrationAssociationSummary"></a>

Contains summary information about the associated AppIntegrations.

## Contents
<a name="API_IntegrationAssociationSummary_Contents"></a>

 ** InstanceId **   <a name="connect-Type-IntegrationAssociationSummary-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** IntegrationArn **   <a name="connect-Type-IntegrationAssociationSummary-IntegrationArn"></a>
The Amazon Resource Name (ARN) for the AppIntegration.
Type: String
Required: No

 ** IntegrationAssociationArn **   <a name="connect-Type-IntegrationAssociationSummary-IntegrationAssociationArn"></a>
The Amazon Resource Name (ARN) for the AppIntegration association.
Type: String
Required: No

 ** IntegrationAssociationId **   <a name="connect-Type-IntegrationAssociationSummary-IntegrationAssociationId"></a>
The identifier for the AppIntegration association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** IntegrationType **   <a name="connect-Type-IntegrationAssociationSummary-IntegrationType"></a>
The integration type.
Type: String
Valid Values: `EVENT | VOICE_ID | PINPOINT_APP | WISDOM_ASSISTANT | WISDOM_KNOWLEDGE_BASE | WISDOM_QUICK_RESPONSES | Q_MESSAGE_TEMPLATES | CASES_DOMAIN | APPLICATION | FILE_SCANNER | SES_IDENTITY | ANALYTICS_CONNECTOR | CALL_TRANSFER_CONNECTOR | COGNITO_USER_POOL | MESSAGE_PROCESSOR`
Required: No

 ** SourceApplicationName **   <a name="connect-Type-IntegrationAssociationSummary-SourceApplicationName"></a>
The user-provided, friendly name for the external application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_ -]+$`
Required: No

 ** SourceApplicationUrl **   <a name="connect-Type-IntegrationAssociationSummary-SourceApplicationUrl"></a>
The URL for the external application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

 ** SourceType **   <a name="connect-Type-IntegrationAssociationSummary-SourceType"></a>
The name of the source.
Type: String
Valid Values: `SALESFORCE | ZENDESK | CASES`
Required: No

## See Also
<a name="API_IntegrationAssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/IntegrationAssociationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/IntegrationAssociationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/IntegrationAssociationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
