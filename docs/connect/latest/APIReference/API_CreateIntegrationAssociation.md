---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateIntegrationAssociation.html
---

# CreateIntegrationAssociation
<a name="API_CreateIntegrationAssociation"></a>

Creates an AWS resource association with an Connect Customer instance.

## Request Syntax
<a name="API_CreateIntegrationAssociation_RequestSyntax"></a>

```
PUT /instance/{{InstanceId}}/integration-associations HTTP/1.1
Content-type: application/json

{
   "IntegrationArn": "{{string}}",
   "IntegrationType": "{{string}}",
   "SourceApplicationName": "{{string}}",
   "SourceApplicationUrl": "{{string}}",
   "SourceType": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateIntegrationAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreateIntegrationAssociation_RequestSyntax) **   <a name="connect-CreateIntegrationAssociation-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreateIntegrationAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [IntegrationArn](#API_CreateIntegrationAssociation_RequestSyntax) **   <a name="connect-CreateIntegrationAssociation-request-IntegrationArn"></a>
The Amazon Resource Name (ARN) of the integration.
When integrating with AWS End User Messaging, the Connect Customer and AWS End User Messaging instances must be in the same account.
Type: String
Required: Yes

 ** [IntegrationType](#API_CreateIntegrationAssociation_RequestSyntax) **   <a name="connect-CreateIntegrationAssociation-request-IntegrationType"></a>
The type of information to be ingested.
Type: String
Valid Values: `EVENT | VOICE_ID | PINPOINT_APP | WISDOM_ASSISTANT | WISDOM_KNOWLEDGE_BASE | WISDOM_QUICK_RESPONSES | Q_MESSAGE_TEMPLATES | CASES_DOMAIN | APPLICATION | FILE_SCANNER | SES_IDENTITY | ANALYTICS_CONNECTOR | CALL_TRANSFER_CONNECTOR | COGNITO_USER_POOL | MESSAGE_PROCESSOR`
Required: Yes

 ** [SourceApplicationName](#API_CreateIntegrationAssociation_RequestSyntax) **   <a name="connect-CreateIntegrationAssociation-request-SourceApplicationName"></a>
The name of the external application. This field is only required for the EVENT integration type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_ -]+$`
Required: No

 ** [SourceApplicationUrl](#API_CreateIntegrationAssociation_RequestSyntax) **   <a name="connect-CreateIntegrationAssociation-request-SourceApplicationUrl"></a>
The URL for the external application. This field is only required for the EVENT integration type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

 ** [SourceType](#API_CreateIntegrationAssociation_RequestSyntax) **   <a name="connect-CreateIntegrationAssociation-request-SourceType"></a>
The type of the data source. This field is only required for the EVENT integration type.
Type: String
Valid Values: `SALESFORCE | ZENDESK | CASES`
Required: No

 ** [Tags](#API_CreateIntegrationAssociation_RequestSyntax) **   <a name="connect-CreateIntegrationAssociation-request-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateIntegrationAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "IntegrationAssociationArn": "string",
   "IntegrationAssociationId": "string"
}
```

## Response Elements
<a name="API_CreateIntegrationAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IntegrationAssociationArn](#API_CreateIntegrationAssociation_ResponseSyntax) **   <a name="connect-CreateIntegrationAssociation-response-IntegrationAssociationArn"></a>
The Amazon Resource Name (ARN) for the association.
Type: String

 ** [IntegrationAssociationId](#API_CreateIntegrationAssociation_ResponseSyntax) **   <a name="connect-CreateIntegrationAssociation-response-IntegrationAssociationId"></a>
The identifier for the integration association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.

## Errors
<a name="API_CreateIntegrationAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DuplicateResourceException **
A resource with the specified name already exists.
HTTP Status Code: 409

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_CreateIntegrationAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateIntegrationAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateIntegrationAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateIntegrationAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateIntegrationAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateIntegrationAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateIntegrationAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateIntegrationAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateIntegrationAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateIntegrationAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateIntegrationAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
