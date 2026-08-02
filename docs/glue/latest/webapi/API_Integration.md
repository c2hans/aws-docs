---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Integration.html
---

# Integration
<a name="API_Integration"></a>

Describes a zero-ETL integration.

## Contents
<a name="API_Integration_Contents"></a>

 ** CreateTime **   <a name="Glue-Type-Integration-CreateTime"></a>
The time that the integration was created, in UTC.
Type: Timestamp
Required: Yes

 ** IntegrationArn **   <a name="Glue-Type-Integration-IntegrationArn"></a>
The Amazon Resource Name (ARN) for the integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** IntegrationName **   <a name="Glue-Type-Integration-IntegrationName"></a>
A unique name for the integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** SourceArn **   <a name="Glue-Type-Integration-SourceArn"></a>
The ARN for the source of the integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** Status **   <a name="Glue-Type-Integration-Status"></a>
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

 ** TargetArn **   <a name="Glue-Type-Integration-TargetArn"></a>
The ARN for the target of the integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** AdditionalEncryptionContext **   <a name="Glue-Type-Integration-AdditionalEncryptionContext"></a>
An optional set of non-secret key–value pairs that contains additional contextual information for encryption. This can only be provided if `KMSKeyId` is provided.
Type: String to string map
Required: No

 ** DataFilter **   <a name="Glue-Type-Integration-DataFilter"></a>
Selects source tables for the integration using Maxwell filter syntax.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** Description **   <a name="Glue-Type-Integration-Description"></a>
A description for the integration.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `[\S\s]*`
Required: No

 ** Errors **   <a name="Glue-Type-Integration-Errors"></a>
A list of errors associated with the integration.
Type: Array of [IntegrationError](API_IntegrationError.md) objects
Required: No

 ** IntegrationConfig **   <a name="Glue-Type-Integration-IntegrationConfig"></a>
Properties associated with the integration.
Type: [IntegrationConfig](API_IntegrationConfig.md) object
Required: No

 ** KmsKeyId **   <a name="Glue-Type-Integration-KmsKeyId"></a>
The ARN of a KMS key used for encrypting the channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** Tags **   <a name="Glue-Type-Integration-Tags"></a>
Metadata assigned to the resource consisting of a list of key-value pairs.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_Integration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Integration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Integration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Integration)
