---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_IntegrationResourceProperty.html
---

# IntegrationResourceProperty
<a name="API_IntegrationResourceProperty"></a>

A structure representing an integration resource property.

## Contents
<a name="API_IntegrationResourceProperty_Contents"></a>

 ** ResourceArn **   <a name="Glue-Type-IntegrationResourceProperty-ResourceArn"></a>
The connection ARN of the source, or the database ARN of the target.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** ResourcePropertyArn **   <a name="Glue-Type-IntegrationResourceProperty-ResourcePropertyArn"></a>
The resource ARN created through this create API. The format is something like arn:aws:glue:<region>:<account\_id>:integrationresourceproperty/\*
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** SourceProcessingProperties **   <a name="Glue-Type-IntegrationResourceProperty-SourceProcessingProperties"></a>
The resource properties associated with the integration source.
Type: [SourceProcessingProperties](API_SourceProcessingProperties.md) object
Required: No

 ** TargetProcessingProperties **   <a name="Glue-Type-IntegrationResourceProperty-TargetProcessingProperties"></a>
The resource properties associated with the integration target.
Type: [TargetProcessingProperties](API_TargetProcessingProperties.md) object
Required: No

## See Also
<a name="API_IntegrationResourceProperty_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/IntegrationResourceProperty)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/IntegrationResourceProperty)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/IntegrationResourceProperty)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
