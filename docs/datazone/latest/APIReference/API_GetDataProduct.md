---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetDataProduct.html
---

# GetDataProduct
<a name="API_GetDataProduct"></a>

Gets the data product.

Prerequisites:
+ The data product ID must exist.
+ The domain must be valid and accessible.
+ User must have read or discovery permissions for the data product.

## Request Syntax
<a name="API_GetDataProduct_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/data-products/{{identifier}}?revision={{revision}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDataProduct_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetDataProduct_RequestSyntax) **   <a name="datazone-GetDataProduct-request-uri-domainIdentifier"></a>
The ID of the domain where the data product lives.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_GetDataProduct_RequestSyntax) **   <a name="datazone-GetDataProduct-request-uri-identifier"></a>
The ID of the data product.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [revision](#API_GetDataProduct_RequestSyntax) **   <a name="datazone-GetDataProduct-request-uri-revision"></a>
The revision of the data product.
Length Constraints: Minimum length of 1. Maximum length of 64.

## Request Body
<a name="API_GetDataProduct_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDataProduct_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_GetDataProduct_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetDataProduct_ResponseSyntax) **   <a name="datazone-GetDataProduct-response-createdAt"></a>
The timestamp at which the data product is created.
Type: Timestamp

 ** [createdBy](#API_GetDataProduct_ResponseSyntax) **   <a name="datazone-GetDataProduct-response-createdBy"></a>
The user who created the data product.
Type: String

 ** [description](#API_GetDataProduct_ResponseSyntax) **   <a name="datazone-GetDataProduct-response-description"></a>
The description of the data product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [domainId](#API_GetDataProduct_ResponseSyntax) **   <a name="datazone-GetDataProduct-response-domainId"></a>
The ID of the domain where the data product lives.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [firstRevisionCreatedAt](#API_GetDataProduct_ResponseSyntax) **   <a name="datazone-GetDataProduct-response-firstRevisionCreatedAt"></a>
The timestamp at which the first revision of the data product is created.
Type: Timestamp

 ** [firstRevisionCreatedBy](#API_GetDataProduct_ResponseSyntax) **   <a name="datazone-GetDataProduct-response-firstRevisionCreatedBy"></a>
The user who created the first revision of the data product.
Type: String

 ** [formsOutput](#API_GetDataProduct_ResponseSyntax) **   <a name="datazone-GetDataProduct-response-formsOutput"></a>
The metadata forms of the data product.
Type: Array of [FormOutput](API_FormOutput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [glossaryTerms](#API_GetDataProduct_ResponseSyntax) **   <a name="datazone-GetDataProduct-response-glossaryTerms"></a>
The glossary terms of the data product.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [id](#API_GetDataProduct_ResponseSyntax) **   <a name="datazone-GetDataProduct-response-id"></a>
The ID of the data product.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [items](#API_GetDataProduct_ResponseSyntax) **   <a name="datazone-GetDataProduct-response-items"></a>
The data assets of the data product.
Type: Array of [DataProductItem](API_DataProductItem.md) objects
Array Members: Minimum number of 1 item.

 ** [name](#API_GetDataProduct_ResponseSyntax) **   <a name="datazone-GetDataProduct-response-name"></a>
The name of the data product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [owningProjectId](#API_GetDataProduct_ResponseSyntax) **   <a name="datazone-GetDataProduct-response-owningProjectId"></a>
The ID of the owning project of the data product.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [revision](#API_GetDataProduct_ResponseSyntax) **   <a name="datazone-GetDataProduct-response-revision"></a>
The revision of the data product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [status](#API_GetDataProduct_ResponseSyntax) **   <a name="datazone-GetDataProduct-response-status"></a>
The status of the data product.
Type: String
Valid Values: `CREATED | CREATING | CREATE_FAILED`

## Errors
<a name="API_GetDataProduct_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_GetDataProduct_Examples"></a>

### Example
<a name="API_GetDataProduct_Example_1"></a>

This example illustrates one usage of GetDataProduct.

#### Sample Request
<a name="API_GetDataProduct_Example_1_Request"></a>

```
aws datazone get-data-product \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "dpd9m3nqx2wkfp"
```

#### Sample Response
<a name="API_GetDataProduct_Example_1_Response"></a>

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
<a name="API_GetDataProduct_Example_2"></a>

Failure case - missing parameter:

#### Sample Request
<a name="API_GetDataProduct_Example_2_Request"></a>

```
aws datazone get-data-product \
--domain-identifier "dzd_53ielnpxktdilj"
```

#### Sample Response
<a name="API_GetDataProduct_Example_2_Response"></a>

```
aws: error: the following arguments are required: —identifier
```

### Example
<a name="API_GetDataProduct_Example_3"></a>

Failure case - resource not found:

#### Sample Request
<a name="API_GetDataProduct_Example_3_Request"></a>

```
aws datazone get-data-product \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "dpd_nonexistent"
```

#### Sample Response
<a name="API_GetDataProduct_Example_3_Response"></a>

```
An error occurred (ResourceNotFoundException) when calling the GetDataProduct operation: Requested dataProduct cannot be found in domain
```

## See Also
<a name="API_GetDataProduct_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetDataProduct)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetDataProduct)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetDataProduct)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetDataProduct)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetDataProduct)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetDataProduct)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetDataProduct)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetDataProduct)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetDataProduct)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetDataProduct)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
