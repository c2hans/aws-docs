---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteVocabulary.html
---

# DeleteVocabulary
<a name="API_DeleteVocabulary"></a>

Deletes the vocabulary that has the given identifier.

## Request Syntax
<a name="API_DeleteVocabulary_RequestSyntax"></a>

```
POST /vocabulary-remove/{{InstanceId}}/{{VocabularyId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteVocabulary_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_DeleteVocabulary_RequestSyntax) **   <a name="connect-DeleteVocabulary-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [VocabularyId](#API_DeleteVocabulary_RequestSyntax) **   <a name="connect-DeleteVocabulary-request-uri-VocabularyId"></a>
The identifier of the custom vocabulary.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Request Body
<a name="API_DeleteVocabulary_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteVocabulary_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "State": "string",
   "VocabularyArn": "string",
   "VocabularyId": "string"
}
```

## Response Elements
<a name="API_DeleteVocabulary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [State](#API_DeleteVocabulary_ResponseSyntax) **   <a name="connect-DeleteVocabulary-response-State"></a>
The current state of the custom vocabulary.
Type: String
Valid Values: `CREATION_IN_PROGRESS | ACTIVE | CREATION_FAILED | DELETE_IN_PROGRESS`

 ** [VocabularyArn](#API_DeleteVocabulary_ResponseSyntax) **   <a name="connect-DeleteVocabulary-response-VocabularyArn"></a>
The Amazon Resource Name (ARN) of the custom vocabulary.
Type: String

 ** [VocabularyId](#API_DeleteVocabulary_ResponseSyntax) **   <a name="connect-DeleteVocabulary-response-VocabularyId"></a>
The identifier of the custom vocabulary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

## Errors
<a name="API_DeleteVocabulary_Errors"></a>

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

 ** ResourceInUseException **
That resource is already in use (for example, you're trying to add a record with the same name as an existing record). If you are trying to delete a resource (for example, DeleteHoursOfOperation or DeletePredefinedAttribute), remove its reference from related resources and then try again.
 ** ResourceId **
The identifier for the resource.
 ** ResourceType **
The type of resource.
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
<a name="API_DeleteVocabulary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DeleteVocabulary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DeleteVocabulary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DeleteVocabulary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DeleteVocabulary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DeleteVocabulary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DeleteVocabulary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DeleteVocabulary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DeleteVocabulary)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DeleteVocabulary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DeleteVocabulary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
