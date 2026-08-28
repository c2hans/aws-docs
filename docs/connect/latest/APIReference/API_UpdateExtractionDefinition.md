---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateExtractionDefinition.html
---

# UpdateExtractionDefinition
<a name="API_UpdateExtractionDefinition"></a>

Updates an extraction definition in the specified Connect Customer instance.

## Request Syntax
<a name="API_UpdateExtractionDefinition_RequestSyntax"></a>

```
PUT /extraction-definitions/{{InstanceId}}/{{ExtractionDefinitionId}} HTTP/1.1
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
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateExtractionDefinition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ExtractionDefinitionId](#API_UpdateExtractionDefinition_RequestSyntax) **   <a name="connect-UpdateExtractionDefinition-request-uri-ExtractionDefinitionId"></a>
The identifier of the extraction definition to update.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_UpdateExtractionDefinition_RequestSyntax) **   <a name="connect-UpdateExtractionDefinition-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_UpdateExtractionDefinition_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_UpdateExtractionDefinition_RequestSyntax) **   <a name="connect-UpdateExtractionDefinition-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field.
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [Display](#API_UpdateExtractionDefinition_RequestSyntax) **   <a name="connect-UpdateExtractionDefinition-request-Display"></a>
The display settings for the extraction definition.
Type: [ExtractionDefinitionDisplay](API_ExtractionDefinitionDisplay.md) object
Required: No

 ** [ExtractionConfiguration](#API_UpdateExtractionDefinition_RequestSyntax) **   <a name="connect-UpdateExtractionDefinition-request-ExtractionConfiguration"></a>
The configuration that defines how data is extracted, including the prompt hint and not-found behavior.
Type: [ExtractionConfiguration](API_ExtractionConfiguration.md) object
Required: Yes

 ** [Name](#API_UpdateExtractionDefinition_RequestSyntax) **   <a name="connect-UpdateExtractionDefinition-request-Name"></a>
The name of the extraction definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

## Response Syntax
<a name="API_UpdateExtractionDefinition_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateExtractionDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateExtractionDefinition_Errors"></a>

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

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_UpdateExtractionDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateExtractionDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateExtractionDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateExtractionDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateExtractionDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateExtractionDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateExtractionDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateExtractionDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateExtractionDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateExtractionDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateExtractionDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
