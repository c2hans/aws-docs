---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_CreateField.html
---

# CreateField
<a name="API_connect-cases_CreateField"></a>

Creates a field in the Cases domain. This field is used to define the case object model (that is, defines what data can be captured on cases) in a Cases domain.

## Request Syntax
<a name="API_connect-cases_CreateField_RequestSyntax"></a>

```
POST /domains/{{domainId}}/fields HTTP/1.1
Content-type: application/json

{
   "attributes": { ... },
   "description": "{{string}}",
   "name": "{{string}}",
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-cases_CreateField_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainId](#API_connect-cases_CreateField_RequestSyntax) **   <a name="connect-connect-cases_CreateField-request-uri-domainId"></a>
The unique identifier of the Cases domain.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Request Body
<a name="API_connect-cases_CreateField_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [attributes](#API_connect-cases_CreateField_RequestSyntax) **   <a name="connect-connect-cases_CreateField-request-attributes"></a>
Union of field attributes.
Type: [FieldAttributes](API_connect-cases_FieldAttributes.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [description](#API_connect-cases_CreateField_RequestSyntax) **   <a name="connect-connect-cases_CreateField-request-description"></a>
The description of the field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** [name](#API_connect-cases_CreateField_RequestSyntax) **   <a name="connect-connect-cases_CreateField-request-name"></a>
The name of the field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*[\S]`
Required: Yes

 ** [type](#API_connect-cases_CreateField_RequestSyntax) **   <a name="connect-connect-cases_CreateField-request-type"></a>
Defines the data type, some system constraints, and default display of the field.
Type: String
Valid Values: `Text | Number | Boolean | DateTime | SingleSelect | Url | User`
Required: Yes

## Response Syntax
<a name="API_connect-cases_CreateField_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "fieldArn": "string",
   "fieldId": "string"
}
```

## Response Elements
<a name="API_connect-cases_CreateField_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [fieldArn](#API_connect-cases_CreateField_ResponseSyntax) **   <a name="connect-connect-cases_CreateField-response-fieldArn"></a>
The Amazon Resource Name (ARN) of the field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

 ** [fieldId](#API_connect-cases_CreateField_ResponseSyntax) **   <a name="connect-connect-cases_CreateField-response-fieldId"></a>
The unique identifier of a field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

## Errors
<a name="API_connect-cases_CreateField_Errors"></a>

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

 ** ServiceQuotaExceededException **
The service quota has been exceeded. For a list of service quotas, see [Connect Customer Service Quotas](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html) in the *Connect Customer Administrator Guide*.
HTTP Status Code: 402

 ** ThrottlingException **
The rate has been exceeded for this API. Please try again after a few minutes.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. Check the syntax and try again.
HTTP Status Code: 400

## Examples
<a name="API_connect-cases_CreateField_Examples"></a>

### Request and Response example
<a name="API_connect-cases_CreateField_Example_1"></a>

This example illustrates one usage of CreateField.

```
{
  "name": "Color",
  "type": "Text",
  "description": "The color of the item"
}
```

```
{
  "fieldArn": "arn:aws:cases:us-west-2:[account_id]:domain/[domain_id]/field/[field_id]",
  "fieldId": "[field_id]"
}
```

## See Also
<a name="API_connect-cases_CreateField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcases-2022-10-03/CreateField)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcases-2022-10-03/CreateField)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/CreateField)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcases-2022-10-03/CreateField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/CreateField)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcases-2022-10-03/CreateField)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcases-2022-10-03/CreateField)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcases-2022-10-03/CreateField)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcases-2022-10-03/CreateField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/CreateField)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
