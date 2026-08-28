---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_BatchGetField.html
---

# BatchGetField
<a name="API_connect-cases_BatchGetField"></a>

Returns the description for the list of fields in the request parameters.

## Request Syntax
<a name="API_connect-cases_BatchGetField_RequestSyntax"></a>

```
POST /domains/{{domainId}}/fields-batch HTTP/1.1
Content-type: application/json

{
   "fields": [
      {
         "id": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_connect-cases_BatchGetField_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainId](#API_connect-cases_BatchGetField_RequestSyntax) **   <a name="connect-connect-cases_BatchGetField-request-uri-domainId"></a>
The unique identifier of the Cases domain.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Request Body
<a name="API_connect-cases_BatchGetField_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [fields](#API_connect-cases_BatchGetField_RequestSyntax) **   <a name="connect-connect-cases_BatchGetField-request-fields"></a>
A list of unique field identifiers.
Type: Array of [FieldIdentifier](API_connect-cases_FieldIdentifier.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: Yes

## Response Syntax
<a name="API_connect-cases_BatchGetField_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errors": [
      {
         "errorCode": "string",
         "id": "string",
         "message": "string"
      }
   ],
   "fields": [
      {
         "attributes": { ... },
         "createdTime": "string",
         "deleted": boolean,
         "description": "string",
         "fieldArn": "string",
         "fieldId": "string",
         "lastModifiedTime": "string",
         "name": "string",
         "namespace": "string",
         "tags": {
            "string" : "string"
         },
         "type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_connect-cases_BatchGetField_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_connect-cases_BatchGetField_ResponseSyntax) **   <a name="connect-connect-cases_BatchGetField-response-errors"></a>
A list of field errors.
Type: Array of [FieldError](API_connect-cases_FieldError.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [fields](#API_connect-cases_BatchGetField_ResponseSyntax) **   <a name="connect-connect-cases_BatchGetField-response-fields"></a>
A list of detailed field information.
Type: Array of [GetFieldResponse](API_connect-cases_GetFieldResponse.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

## Errors
<a name="API_connect-cases_BatchGetField_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_connect-cases_BatchGetField_Examples"></a>

### Request and Response example
<a name="API_connect-cases_BatchGetField_Example_1"></a>

This example illustrates one usage of BatchGetField.

```
{
   "fields":[
   {
      "id":"[field_id_1]"
   },
   {
      "id":"[field_id_2]"
   },
   {
      "id":"case_id"
   }
   ]
}
```

```
{
   "errors":[
     ],
     "fields":[
      {
      "description":"Test with description",
      "fieldArn":"arn:aws:cases:us-west-2:[account_id]:domain/[domain_id]/field/[field_id_1]",
      "fieldId":"[field_id_1]",
      "name":"field1",
      "namespace":"Custom",
      "tags":{
         "resourceArn":"arn:aws:cases:us-west-2:[account_id]:domain/[domain_id]/field/5a17045a-9150-48f9-8cd5-8a5946585b73"
         },
      "type":"SingleSelect"
      },
      {
      "description":"Unique Identifier of the case",
      "fieldArn":"arn:aws:cases:us-west-2:[account_id]:domain/[domain_id]/field/case_id",
      "fieldId":"case_id",
      "name":"Case Id",
      "namespace":"System",
      "tags":{
         "resourceArn":"arn:aws:cases:us-west-2:[account_id]:domain/[domain_id]/field/case_id"
         },
      "type":"Text"
      },
      {
         "description":"test",
         "fieldArn":"arn:aws:cases:us-west-2:[account_id]:domain/[domain_id]/field/[field_id_2]",
         "fieldId":"[field_id_2]",
         "name":"field2",
         "namespace":"Custom",
         "tags":{
            "resourceArn":"arn:aws:cases:us-west-2:[account_id]:domain/[domain_id]/field/[field_id_2]"
            },
      "type":"SingleSelect"
      }
   ]
}
```

## See Also
<a name="API_connect-cases_BatchGetField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcases-2022-10-03/BatchGetField)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcases-2022-10-03/BatchGetField)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/BatchGetField)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcases-2022-10-03/BatchGetField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/BatchGetField)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcases-2022-10-03/BatchGetField)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcases-2022-10-03/BatchGetField)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcases-2022-10-03/BatchGetField)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcases-2022-10-03/BatchGetField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/BatchGetField)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
