---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ModifyIntegration.html
---

# ModifyIntegration
<a name="API_ModifyIntegration"></a>

Modifies a Zero-ETL integration in the caller's account.

## Request Syntax
<a name="API_ModifyIntegration_RequestSyntax"></a>

```
{
   "DataFilter": "{{string}}",
   "Description": "{{string}}",
   "IntegrationConfig": {
      "ContinuousSync": {{boolean}},
      "RefreshInterval": "{{string}}",
      "SourceProperties": {
         "{{string}}" : "{{string}}"
      }
   },
   "IntegrationIdentifier": "{{string}}",
   "IntegrationName": "{{string}}"
}
```

## Request Parameters
<a name="API_ModifyIntegration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DataFilter](#API_ModifyIntegration_RequestSyntax) **   <a name="Glue-ModifyIntegration-request-DataFilter"></a>
Selects source tables for the integration using Maxwell filter syntax.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [Description](#API_ModifyIntegration_RequestSyntax) **   <a name="Glue-ModifyIntegration-request-Description"></a>
A description of the integration.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `[\S\s]*`
Required: No

 ** [IntegrationConfig](#API_ModifyIntegration_RequestSyntax) **   <a name="Glue-ModifyIntegration-request-IntegrationConfig"></a>
The configuration settings for the integration. Currently, only the RefreshInterval can be modified.
Type: [IntegrationConfig](API_IntegrationConfig.md) object
Required: No

 ** [IntegrationIdentifier](#API_ModifyIntegration_RequestSyntax) **   <a name="Glue-ModifyIntegration-request-IntegrationIdentifier"></a>
The Amazon Resource Name (ARN) for the integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [IntegrationName](#API_ModifyIntegration_RequestSyntax) **   <a name="Glue-ModifyIntegration-request-IntegrationName"></a>
A unique name for an integration in AWS Glue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## Response Syntax
<a name="API_ModifyIntegration_ResponseSyntax"></a>

```
{
   "AdditionalEncryptionContext": {
      "string" : "string"
   },
   "CreateTime": number,
   "DataFilter": "string",
   "Description": "string",
   "Errors": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string"
      }
   ],
   "IntegrationArn": "string",
   "IntegrationConfig": {
      "ContinuousSync": boolean,
      "RefreshInterval": "string",
      "SourceProperties": {
         "string" : "string"
      }
   },
   "IntegrationName": "string",
   "KmsKeyId": "string",
   "SourceArn": "string",
   "Status": "string",
   "Tags": [
      {
         "key": "string",
         "value": "string"
      }
   ],
   "TargetArn": "string"
}
```

## Response Elements
<a name="API_ModifyIntegration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AdditionalEncryptionContext](#API_ModifyIntegration_ResponseSyntax) **   <a name="Glue-ModifyIntegration-response-AdditionalEncryptionContext"></a>
An optional set of non-secret key–value pairs that contains additional contextual information for encryption.
Type: String to string map

 ** [CreateTime](#API_ModifyIntegration_ResponseSyntax) **   <a name="Glue-ModifyIntegration-response-CreateTime"></a>
The time when the integration was created, in UTC.
Type: Timestamp

 ** [DataFilter](#API_ModifyIntegration_ResponseSyntax) **   <a name="Glue-ModifyIntegration-response-DataFilter"></a>
Selects source tables for the integration using Maxwell filter syntax.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [Description](#API_ModifyIntegration_ResponseSyntax) **   <a name="Glue-ModifyIntegration-response-Description"></a>
A description of the integration.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `[\S\s]*`

 ** [Errors](#API_ModifyIntegration_ResponseSyntax) **   <a name="Glue-ModifyIntegration-response-Errors"></a>
A list of errors associated with the integration modification.
Type: Array of [IntegrationError](API_IntegrationError.md) objects

 ** [IntegrationArn](#API_ModifyIntegration_ResponseSyntax) **   <a name="Glue-ModifyIntegration-response-IntegrationArn"></a>
The Amazon Resource Name (ARN) for the integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [IntegrationConfig](#API_ModifyIntegration_ResponseSyntax) **   <a name="Glue-ModifyIntegration-response-IntegrationConfig"></a>
The updated configuration settings for the integration.
Type: [IntegrationConfig](API_IntegrationConfig.md) object

 ** [IntegrationName](#API_ModifyIntegration_ResponseSyntax) **   <a name="Glue-ModifyIntegration-response-IntegrationName"></a>
A unique name for an integration in AWS Glue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [KmsKeyId](#API_ModifyIntegration_ResponseSyntax) **   <a name="Glue-ModifyIntegration-response-KmsKeyId"></a>
The ARN of a KMS key used for encrypting the channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [SourceArn](#API_ModifyIntegration_ResponseSyntax) **   <a name="Glue-ModifyIntegration-response-SourceArn"></a>
The ARN of the source for the integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.

 ** [Status](#API_ModifyIntegration_ResponseSyntax) **   <a name="Glue-ModifyIntegration-response-Status"></a>
The status of the integration being modified.
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

 ** [Tags](#API_ModifyIntegration_ResponseSyntax) **   <a name="Glue-ModifyIntegration-response-Tags"></a>
Metadata assigned to the resource consisting of a list of key-value pairs.
Type: Array of [Tag](API_Tag.md) objects

 ** [TargetArn](#API_ModifyIntegration_ResponseSyntax) **   <a name="Glue-ModifyIntegration-response-TargetArn"></a>
The ARN of the target for the integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.

## Errors
<a name="API_ModifyIntegration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ConflictException **
The `CreatePartitions` API was called on a table that has indexes enabled.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** IntegrationConflictOperationFault **
The requested operation conflicts with another operation.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** IntegrationNotFoundFault **
The specified integration could not be found.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InvalidIntegrationStateFault **
The integration is in an invalid state.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InvalidStateException **
An error that indicates your data is in an invalid state.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ValidationException **
A value could not be validated.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_ModifyIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/ModifyIntegration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/ModifyIntegration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ModifyIntegration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/ModifyIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ModifyIntegration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/ModifyIntegration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/ModifyIntegration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/ModifyIntegration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/ModifyIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ModifyIntegration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
