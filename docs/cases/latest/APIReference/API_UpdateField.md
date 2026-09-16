---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_UpdateField.html
---

# UpdateField
<a name="API_connect-cases_UpdateField"></a>

Updates the properties of an existing field.

## Request Syntax
<a name="API_connect-cases_UpdateField_RequestSyntax"></a>

```
PUT /domains/{{domainId}}/fields/{{fieldId}} HTTP/1.1
Content-type: application/json

{
   "attributes": { ... },
   "description": "{{string}}",
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-cases_UpdateField_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainId](#API_connect-cases_UpdateField_RequestSyntax) **   <a name="connect-connect-cases_UpdateField-request-uri-domainId"></a>
The unique identifier of the Cases domain.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [fieldId](#API_connect-cases_UpdateField_RequestSyntax) **   <a name="connect-connect-cases_UpdateField-request-uri-fieldId"></a>
The unique identifier of a field.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Request Body
<a name="API_connect-cases_UpdateField_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [attributes](#API_connect-cases_UpdateField_RequestSyntax) **   <a name="connect-connect-cases_UpdateField-request-attributes"></a>
Union of field attributes.
Type: [FieldAttributes](API_connect-cases_FieldAttributes.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [description](#API_connect-cases_UpdateField_RequestSyntax) **   <a name="connect-connect-cases_UpdateField-request-description"></a>
The description of a field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** [name](#API_connect-cases_UpdateField_RequestSyntax) **   <a name="connect-connect-cases_UpdateField-request-name"></a>
The name of the field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*[\S]`
Required: No

## Response Syntax
<a name="API_connect-cases_UpdateField_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-cases_UpdateField_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-cases_UpdateField_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.
HTTP Status Code: 409

 ** InternalServerException **
We couldn't process your request because of an issue with the server. Try again later.
 ** retryAfterSeconds **
Advice to clients on when the call can be safely retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
We couldn't find the requested resource. Check that your resources exists and were created in the same AWS Region as your request, and try your request again.
 ** resourceId **
Unique identifier of the resource affected.
 ** resourceType **
Type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
The rate has been exceeded for this API. Please try again after a few minutes.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. Check the syntax and try again.
HTTP Status Code: 400

## Examples
<a name="API_connect-cases_UpdateField_Examples"></a>

### Request and Response example
<a name="API_connect-cases_UpdateField_Example_1"></a>

This example illustrates one usage of UpdateField.

```
{
  "name": "updated_field_name"
}
```

```
{ }
```

## See Also
<a name="API_connect-cases_UpdateField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcases-2022-10-03/UpdateField)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcases-2022-10-03/UpdateField)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/UpdateField)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcases-2022-10-03/UpdateField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/UpdateField)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcases-2022-10-03/UpdateField)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcases-2022-10-03/UpdateField)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcases-2022-10-03/UpdateField)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connectcases-2022-10-03/UpdateField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/UpdateField)
