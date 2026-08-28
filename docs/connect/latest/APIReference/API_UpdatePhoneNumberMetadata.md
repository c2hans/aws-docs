---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdatePhoneNumberMetadata.html
---

# UpdatePhoneNumberMetadata
<a name="API_UpdatePhoneNumberMetadata"></a>

Updates a phone number’s metadata.

**Important**
To verify the status of a previous UpdatePhoneNumberMetadata operation, call the [DescribePhoneNumber](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribePhoneNumber.html) API.

## Request Syntax
<a name="API_UpdatePhoneNumberMetadata_RequestSyntax"></a>

```
PUT /phone-number/{{PhoneNumberId}}/metadata HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "PhoneNumberDescription": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdatePhoneNumberMetadata_RequestParameters"></a>

The request uses the following URI parameters.

 ** [PhoneNumberId](#API_UpdatePhoneNumberMetadata_RequestSyntax) **   <a name="connect-UpdatePhoneNumberMetadata-request-uri-PhoneNumberId"></a>
The Amazon Resource Name (ARN) or resource ID of the phone number.
Required: Yes

## Request Body
<a name="API_UpdatePhoneNumberMetadata_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_UpdatePhoneNumberMetadata_RequestSyntax) **   <a name="connect-UpdatePhoneNumberMetadata-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [PhoneNumberDescription](#API_UpdatePhoneNumberMetadata_RequestSyntax) **   <a name="connect-UpdatePhoneNumberMetadata-request-PhoneNumberDescription"></a>
The description of the phone number.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `^[\W\S_]*`
Required: No

## Response Syntax
<a name="API_UpdatePhoneNumberMetadata_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdatePhoneNumberMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdatePhoneNumberMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** IdempotencyException **
An entity with the same name already exists.
HTTP Status Code: 409

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

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
<a name="API_UpdatePhoneNumberMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdatePhoneNumberMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdatePhoneNumberMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdatePhoneNumberMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdatePhoneNumberMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdatePhoneNumberMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdatePhoneNumberMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdatePhoneNumberMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdatePhoneNumberMetadata)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdatePhoneNumberMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdatePhoneNumberMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
