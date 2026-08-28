---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_InboundIntegration.html
---

# InboundIntegration
<a name="API_InboundIntegration"></a>

A structure for an integration that writes data into a resource.

## Contents
<a name="API_InboundIntegration_Contents"></a>

 ** CreateTime **   <a name="Glue-Type-InboundIntegration-CreateTime"></a>
The time that the integration was created, in UTC.
Type: Timestamp
Required: Yes

 ** IntegrationArn **   <a name="Glue-Type-InboundIntegration-IntegrationArn"></a>
The ARN of the zero-ETL integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** SourceArn **   <a name="Glue-Type-InboundIntegration-SourceArn"></a>
The ARN of the source resource for the integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** Status **   <a name="Glue-Type-InboundIntegration-Status"></a>
The possible statuses are:
+ CREATING: The integration is being created.
+ ACTIVE: The integration creation succeeds.
+ MODIFYING: The integration is being modified.
+ FAILED: The integration creation fails.
+ DELETING: The integration is deleted.
+ SYNCING: The integration is synchronizing.
+ NEEDS\_ATTENTION: The integration needs attention, such as synchronization.
Type: String
Valid Values: `CREATING | ACTIVE | MODIFYING | FAILED | DELETING | SYNCING | NEEDS_ATTENTION`
Required: Yes

 ** TargetArn **   <a name="Glue-Type-InboundIntegration-TargetArn"></a>
The ARN of the target resource for the integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** Errors **   <a name="Glue-Type-InboundIntegration-Errors"></a>
A list of errors associated with the integration.
Type: Array of [IntegrationError](API_IntegrationError.md) objects
Required: No

 ** IntegrationConfig **   <a name="Glue-Type-InboundIntegration-IntegrationConfig"></a>
Properties associated with the integration.
Type: [IntegrationConfig](API_IntegrationConfig.md) object
Required: No

## See Also
<a name="API_InboundIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/InboundIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/InboundIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/InboundIntegration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
