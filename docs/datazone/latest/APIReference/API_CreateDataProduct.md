---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateDataProduct.html
---

# CreateDataProduct
<a name="API_CreateDataProduct"></a>

Creates a data product.

A data product is a comprehensive package that combines data assets with their associated metadata, documentation, and access controls. It's designed to serve specific business needs or use cases, making it easier for users to find and consume data appropriately. Data products include important information about data quality, freshness, and usage guidelines, effectively bridging the gap between data producers and consumers while ensuring proper governance.

Prerequisites:
+ The domain must exist and be accessible.
+ The owning project must be valid and active.
+ The name must be unique within the domain (no existing data product with the same name).
+ User must have create permissions for data products in the project.

## Request Syntax
<a name="API_CreateDataProduct_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/data-products HTTP/1.1
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
   "name": "{{string}}",
   "owningProjectIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateDataProduct_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_CreateDataProduct_RequestSyntax) **   <a name="datazone-CreateDataProduct-request-uri-domainIdentifier"></a>
The ID of the domain where the data product is created.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_CreateDataProduct_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateDataProduct_RequestSyntax) **   <a name="datazone-CreateDataProduct-request-clientToken"></a>
A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [description](#API_CreateDataProduct_RequestSyntax) **   <a name="datazone-CreateDataProduct-request-description"></a>
The description of the data product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [formsInput](#API_CreateDataProduct_RequestSyntax) **   <a name="datazone-CreateDataProduct-request-formsInput"></a>
The metadata forms of the data product.
Type: Array of [FormInput](API_FormInput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [glossaryTerms](#API_CreateDataProduct_RequestSyntax) **   <a name="datazone-CreateDataProduct-request-glossaryTerms"></a>
The glossary terms of the data product.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** [items](#API_CreateDataProduct_RequestSyntax) **   <a name="datazone-CreateDataProduct-request-items"></a>
The data assets of the data product.
Type: Array of [DataProductItem](API_DataProductItem.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [name](#API_CreateDataProduct_RequestSyntax) **   <a name="datazone-CreateDataProduct-request-name"></a>
The name of the data product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [owningProjectIdentifier](#API_CreateDataProduct_RequestSyntax) **   <a name="datazone-CreateDataProduct-request-owningProjectIdentifier"></a>
The ID of the owning project of the data product.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Response Syntax
<a name="API_CreateDataProduct_ResponseSyntax"></a>

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
<a name="API_CreateDataProduct_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreateDataProduct_ResponseSyntax) **   <a name="datazone-CreateDataProduct-response-createdAt"></a>
The timestamp at which the data product was created.
Type: Timestamp

 ** [createdBy](#API_CreateDataProduct_ResponseSyntax) **   <a name="datazone-CreateDataProduct-response-createdBy"></a>
The user who created the data product.
Type: String

 ** [description](#API_CreateDataProduct_ResponseSyntax) **   <a name="datazone-CreateDataProduct-response-description"></a>
The description of the data product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [domainId](#API_CreateDataProduct_ResponseSyntax) **   <a name="datazone-CreateDataProduct-response-domainId"></a>
The ID of the domain where the data product lives.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [firstRevisionCreatedAt](#API_CreateDataProduct_ResponseSyntax) **   <a name="datazone-CreateDataProduct-response-firstRevisionCreatedAt"></a>
The timestamp at which the first revision of the data product was created.
Type: Timestamp

 ** [firstRevisionCreatedBy](#API_CreateDataProduct_ResponseSyntax) **   <a name="datazone-CreateDataProduct-response-firstRevisionCreatedBy"></a>
The user who created the first revision of the data product.
Type: String

 ** [formsOutput](#API_CreateDataProduct_ResponseSyntax) **   <a name="datazone-CreateDataProduct-response-formsOutput"></a>
The metadata forms of the data product.
Type: Array of [FormOutput](API_FormOutput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [glossaryTerms](#API_CreateDataProduct_ResponseSyntax) **   <a name="datazone-CreateDataProduct-response-glossaryTerms"></a>
The glossary terms of the data product.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [id](#API_CreateDataProduct_ResponseSyntax) **   <a name="datazone-CreateDataProduct-response-id"></a>
The ID of the data product.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [items](#API_CreateDataProduct_ResponseSyntax) **   <a name="datazone-CreateDataProduct-response-items"></a>
The data assets of the data product.
Type: Array of [DataProductItem](API_DataProductItem.md) objects
Array Members: Minimum number of 1 item.

 ** [name](#API_CreateDataProduct_ResponseSyntax) **   <a name="datazone-CreateDataProduct-response-name"></a>
The name of the data product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [owningProjectId](#API_CreateDataProduct_ResponseSyntax) **   <a name="datazone-CreateDataProduct-response-owningProjectId"></a>
The ID of the owning project of the data product.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [revision](#API_CreateDataProduct_ResponseSyntax) **   <a name="datazone-CreateDataProduct-response-revision"></a>
The revision of the data product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [status](#API_CreateDataProduct_ResponseSyntax) **   <a name="datazone-CreateDataProduct-response-status"></a>
The status of the data product.
Type: String
Valid Values: `CREATED | CREATING | CREATE_FAILED`

## Errors
<a name="API_CreateDataProduct_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request has exceeded the specified service quota.
HTTP Status Code: 402

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
<a name="API_CreateDataProduct_Examples"></a>

### Example
<a name="API_CreateDataProduct_Example_1"></a>

This example illustrates one usage of CreateDataProduct.

#### Sample Request
<a name="API_CreateDataProduct_Example_1_Request"></a>

```
aws datazone create-data-product \
--domain-identifier "dzd_53ielnpxktdilj" \
--name "CustomerInsightsDataProduct" \
--owning-project-identifier "prj7nx82mkl"
```

#### Sample Response
<a name="API_CreateDataProduct_Example_1_Response"></a>

```
{
    "createdAt": 1752602810.307,
    "createdBy": "usr7nx82mkl",
    "domainId": "dzd_53ielnpxktdilj",
    "firstRevisionCreatedAt": 1752602810.307,
    "firstRevisionCreatedBy": "usr7nx82mkl",
    "formsOutput": [],
    "id": "dpd9m3nqx2wkfp",
    "name": "CustomerInsightsDataProduct",
    "owningProjectId": "prj7nx82mkl",
    "revision": "1",
    "status": "CREATED"
}
```

### Example
<a name="API_CreateDataProduct_Example_2"></a>

Failure case - missing parameter:

#### Sample Request
<a name="API_CreateDataProduct_Example_2_Request"></a>

```
aws datazone create-data-product \
--domain-identifier "dzd_53ielnpxktdilj" \
--name "CustomerInsightsDataProduct"
```

#### Sample Response
<a name="API_CreateDataProduct_Example_2_Response"></a>

```
aws: error: the following arguments are required: —owning-project-identifier
```

### Example
<a name="API_CreateDataProduct_Example_3"></a>

Failure case - duplicate term:

#### Sample Request
<a name="API_CreateDataProduct_Example_3_Request"></a>

```
aws datazone create-data-product \
--domain-identifier "dzd_53ielnpxktdilj" \
--name "CustomerInsightsDataProduct" \
--owning-project-identifier "prj7nx82mkl"
```

#### Sample Response
<a name="API_CreateDataProduct_Example_3_Response"></a>

```
An error occurred (ConflictException) when calling the CreateDataProduct operation: Conflict with dataProduct c5rerxaqjys59j
```

## See Also
<a name="API_CreateDataProduct_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CreateDataProduct)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CreateDataProduct)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CreateDataProduct)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CreateDataProduct)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CreateDataProduct)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CreateDataProduct)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CreateDataProduct)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CreateDataProduct)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CreateDataProduct)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CreateDataProduct)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
