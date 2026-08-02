---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateDataProductRevision.html
---

# CreateDataProductRevision
<a name="API_CreateDataProductRevision"></a>

Creates a data product revision.

Prerequisites:
+ The original data product must exist in the given domain.
+ User must have permissions on the data product.
+ The domain must be valid and accessible.
+ The new revision name must comply with naming constraints (if required).

## Request Syntax
<a name="API_CreateDataProductRevision_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/data-products/{{identifier}}/revisions HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "formsInput": [
      {
         "content": "{{string}}",
         "formName": "{{string}}",
         "typeIdentifier": "{{string}}",
         "typeRevision": "{{string}}"
      }
   ],
   "glossaryTerms": [ "{{string}}" ],
   "items": [
      {
         "glossaryTerms": [ "{{string}}" ],
         "identifier": "{{string}}",
         "itemType": "{{string}}",
         "revision": "{{string}}"
      }
   ],
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateDataProductRevision_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_CreateDataProductRevision_RequestSyntax) **   <a name="datazone-CreateDataProductRevision-request-uri-domainIdentifier"></a>
The ID of the domain where the data product revision is created.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_CreateDataProductRevision_RequestSyntax) **   <a name="datazone-CreateDataProductRevision-request-uri-identifier"></a>
The ID of the data product revision.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_CreateDataProductRevision_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateDataProductRevision_RequestSyntax) **   <a name="datazone-CreateDataProductRevision-request-clientToken"></a>
A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [description](#API_CreateDataProductRevision_RequestSyntax) **   <a name="datazone-CreateDataProductRevision-request-description"></a>
The description of the data product revision.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [formsInput](#API_CreateDataProductRevision_RequestSyntax) **   <a name="datazone-CreateDataProductRevision-request-formsInput"></a>
The metadata forms of the data product revision.
Type: Array of [FormInput](API_FormInput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [glossaryTerms](#API_CreateDataProductRevision_RequestSyntax) **   <a name="datazone-CreateDataProductRevision-request-glossaryTerms"></a>
The glossary terms of the data product revision.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** [items](#API_CreateDataProductRevision_RequestSyntax) **   <a name="datazone-CreateDataProductRevision-request-items"></a>
The data assets of the data product revision.
Type: Array of [DataProductItem](API_DataProductItem.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [name](#API_CreateDataProductRevision_RequestSyntax) **   <a name="datazone-CreateDataProductRevision-request-name"></a>
The name of the data product revision.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_CreateDataProductRevision_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "createdAt": number,
   "createdBy": "string",
   "description": "string",
   "domainId": "string",
   "firstRevisionCreatedAt": number,
   "firstRevisionCreatedBy": "string",
   "formsOutput": [
      {
         "content": "string",
         "formName": "string",
         "typeName": "string",
         "typeRevision": "string"
      }
   ],
   "glossaryTerms": [ "string" ],
   "id": "string",
   "items": [
      {
         "glossaryTerms": [ "string" ],
         "identifier": "string",
         "itemType": "string",
         "revision": "string"
      }
   ],
   "name": "string",
   "owningProjectId": "string",
   "revision": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateDataProductRevision_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreateDataProductRevision_ResponseSyntax) **   <a name="datazone-CreateDataProductRevision-response-createdAt"></a>
The timestamp at which the data product revision is created.
Type: Timestamp

 ** [createdBy](#API_CreateDataProductRevision_ResponseSyntax) **   <a name="datazone-CreateDataProductRevision-response-createdBy"></a>
The user who created the data product revision.
Type: String

 ** [description](#API_CreateDataProductRevision_ResponseSyntax) **   <a name="datazone-CreateDataProductRevision-response-description"></a>
The description of the data product revision.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [domainId](#API_CreateDataProductRevision_ResponseSyntax) **   <a name="datazone-CreateDataProductRevision-response-domainId"></a>
The ID of the domain where data product revision is created.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [firstRevisionCreatedAt](#API_CreateDataProductRevision_ResponseSyntax) **   <a name="datazone-CreateDataProductRevision-response-firstRevisionCreatedAt"></a>
The timestamp at which the first revision of the data product is created.
Type: Timestamp

 ** [firstRevisionCreatedBy](#API_CreateDataProductRevision_ResponseSyntax) **   <a name="datazone-CreateDataProductRevision-response-firstRevisionCreatedBy"></a>
The user who created the first revision of the data product.
Type: String

 ** [formsOutput](#API_CreateDataProductRevision_ResponseSyntax) **   <a name="datazone-CreateDataProductRevision-response-formsOutput"></a>
The metadata forms of the data product revision.
Type: Array of [FormOutput](API_FormOutput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [glossaryTerms](#API_CreateDataProductRevision_ResponseSyntax) **   <a name="datazone-CreateDataProductRevision-response-glossaryTerms"></a>
The glossary terms of the data product revision.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [id](#API_CreateDataProductRevision_ResponseSyntax) **   <a name="datazone-CreateDataProductRevision-response-id"></a>
The ID of the data product revision.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [items](#API_CreateDataProductRevision_ResponseSyntax) **   <a name="datazone-CreateDataProductRevision-response-items"></a>
The data assets of the data product revision.
Type: Array of [DataProductItem](API_DataProductItem.md) objects
Array Members: Minimum number of 1 item.

 ** [name](#API_CreateDataProductRevision_ResponseSyntax) **   <a name="datazone-CreateDataProductRevision-response-name"></a>
The name of the data product revision.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [owningProjectId](#API_CreateDataProductRevision_ResponseSyntax) **   <a name="datazone-CreateDataProductRevision-response-owningProjectId"></a>
The ID of the owning project of the data product revision.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [revision](#API_CreateDataProductRevision_ResponseSyntax) **   <a name="datazone-CreateDataProductRevision-response-revision"></a>
The revision of the data product revision.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [status](#API_CreateDataProductRevision_ResponseSyntax) **   <a name="datazone-CreateDataProductRevision-response-status"></a>
The status of the data product revision.
Type: String
Valid Values: `CREATED | CREATING | CREATE_FAILED`

## Errors
<a name="API_CreateDataProductRevision_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict while performing this action.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## Examples
<a name="API_CreateDataProductRevision_Examples"></a>

### Example
<a name="API_CreateDataProductRevision_Example_1"></a>

This example illustrates one usage of CreateDataProductRevision.

#### Sample Request
<a name="API_CreateDataProductRevision_Example_1_Request"></a>

```
aws datazone create-data-product-revision \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "dpd9m3nqx2wkfp" \
--name "CustomerInsights-v2"
```

#### Sample Response
<a name="API_CreateDataProductRevision_Example_1_Response"></a>

```
{
    "createdAt": 1752602995.424,
    "createdBy": "usr7nx82mkl",
    "domainId": "dzd_53ielnpxktdilj",
    "firstRevisionCreatedAt": 1752602810.307,
    "firstRevisionCreatedBy": "usr7nx82mkl",
    "formsOutput": [],
    "id": "dpd9m3nqx2wkfp",
    "name": "CustomerInsights-v2",
    "owningProjectId": "prj7nx82mkl",
    "revision": "2",
    "status": "CREATED"
}
```

### Example
<a name="API_CreateDataProductRevision_Example_2"></a>

Failure case - missing parameter:

#### Sample Request
<a name="API_CreateDataProductRevision_Example_2_Request"></a>

```
aws datazone create-data-product-revision \
--domain-identifier "dzd_53ielnpxktdilj" \
--name "CustomerInsights-v2"
```

#### Sample Response
<a name="API_CreateDataProductRevision_Example_2_Response"></a>

```
aws: error: the following arguments are required: —identifier
```

### Example
<a name="API_CreateDataProductRevision_Example_3"></a>

Failure case - resource not found:

#### Sample Request
<a name="API_CreateDataProductRevision_Example_3_Request"></a>

```
aws datazone create-data-product-revision \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "dpd_nonexistent" \
--name "CustomerInsights-v2"
```

#### Sample Response
<a name="API_CreateDataProductRevision_Example_3_Response"></a>

```
An error occurred (ResourceNotFoundException) when calling the CreateDataProductRevision operation: Requested dataProduct cannot be found in domain
```

## See Also
<a name="API_CreateDataProductRevision_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CreateDataProductRevision)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CreateDataProductRevision)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CreateDataProductRevision)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CreateDataProductRevision)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CreateDataProductRevision)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CreateDataProductRevision)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CreateDataProductRevision)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CreateDataProductRevision)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CreateDataProductRevision)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CreateDataProductRevision)
