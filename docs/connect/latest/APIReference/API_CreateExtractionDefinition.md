---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateExtractionDefinition.html
---

# CreateExtractionDefinition
<a name="API_CreateExtractionDefinition"></a>

Creates an extraction definition in the specified Connect Customer instance. An extraction definition specifies how structured data is extracted from customer interactions using generative AI, including the prompt hint that guides extraction and the behavior when a value cannot be found.

## Request Syntax
<a name="API_CreateExtractionDefinition_RequestSyntax"></a>

```
POST /extraction-definitions/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Display": {
      "Label": "{{string}}"
   },
   "ExtractionConfiguration": {
      "NotFoundBehavior": {
         "Behavior": "{{string}}",
         "DefaultValue": "{{string}}"
      },
      "PromptHint": "{{string}}"
   },
   "Name": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateExtractionDefinition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreateExtractionDefinition_RequestSyntax) **   <a name="connect-CreateExtractionDefinition-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreateExtractionDefinition_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateExtractionDefinition_RequestSyntax) **   <a name="connect-CreateExtractionDefinition-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field.
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [Display](#API_CreateExtractionDefinition_RequestSyntax) **   <a name="connect-CreateExtractionDefinition-request-Display"></a>
The display settings for the extraction definition, including the label shown in the agent workspace.
Type: [ExtractionDefinitionDisplay](API_ExtractionDefinitionDisplay.md) object
Required: No

 ** [ExtractionConfiguration](#API_CreateExtractionDefinition_RequestSyntax) **   <a name="connect-CreateExtractionDefinition-request-ExtractionConfiguration"></a>
The configuration that defines how data is extracted, including the prompt hint and not-found behavior.
Type: [ExtractionConfiguration](API_ExtractionConfiguration.md) object
Required: Yes

 ** [Name](#API_CreateExtractionDefinition_RequestSyntax) **   <a name="connect-CreateExtractionDefinition-request-Name"></a>
A unique name of the extraction definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** [Tags](#API_CreateExtractionDefinition_RequestSyntax) **   <a name="connect-CreateExtractionDefinition-request-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateExtractionDefinition_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ExtractionDefinitionArn": "string",
   "ExtractionDefinitionId": "string"
}
```

## Response Elements
<a name="API_CreateExtractionDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExtractionDefinitionArn](#API_CreateExtractionDefinition_ResponseSyntax) **   <a name="connect-CreateExtractionDefinition-response-ExtractionDefinitionArn"></a>
The Amazon Resource Name (ARN) of the extraction definition.
Type: String

 ** [ExtractionDefinitionId](#API_CreateExtractionDefinition_ResponseSyntax) **   <a name="connect-CreateExtractionDefinition-response-ExtractionDefinitionId"></a>
The identifier of the extraction definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_CreateExtractionDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

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

 ** ResourceConflictException **
A resource already has that name.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The service quota has been exceeded.
 ** Reason **
The reason for the exception.
HTTP Status Code: 402

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_CreateExtractionDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateExtractionDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateExtractionDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateExtractionDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateExtractionDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateExtractionDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateExtractionDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateExtractionDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateExtractionDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateExtractionDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateExtractionDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
