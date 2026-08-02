---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateGlossary.html
---

# CreateGlossary
<a name="API_CreateGlossary"></a>

Creates an Amazon DataZone business glossary.

Specifies that this is a create glossary policy.

A glossary serves as the central repository for business terminology and definitions within an organization. It helps establish and maintain a common language across different departments and teams, reducing miscommunication and ensuring consistent interpretation of business concepts. Glossaries can include hierarchical relationships between terms, cross-references, and links to actual data assets, making them invaluable for both business users and technical teams trying to understand and use data correctly.

Prerequisites:
+ Domain must exist and be in an active state.
+ Owning project must exist and be accessible by the caller.
+ The glossary name must be unique within the domain.

## Request Syntax
<a name="API_CreateGlossary_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/glossaries HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "owningProjectIdentifier": "{{string}}",
   "status": "{{string}}",
   "usageRestrictions": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_CreateGlossary_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_CreateGlossary_RequestSyntax) **   <a name="datazone-CreateGlossary-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which this business glossary is created.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_CreateGlossary_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateGlossary_RequestSyntax) **   <a name="datazone-CreateGlossary-request-clientToken"></a>
A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [description](#API_CreateGlossary_RequestSyntax) **   <a name="datazone-CreateGlossary-request-description"></a>
The description of this business glossary.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** [name](#API_CreateGlossary_RequestSyntax) **   <a name="datazone-CreateGlossary-request-name"></a>
The name of this business glossary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [owningProjectIdentifier](#API_CreateGlossary_RequestSyntax) **   <a name="datazone-CreateGlossary-request-owningProjectIdentifier"></a>
The ID of the project that currently owns business glossary.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [status](#API_CreateGlossary_RequestSyntax) **   <a name="datazone-CreateGlossary-request-status"></a>
The status of this business glossary.
Type: String
Valid Values: `DISABLED | ENABLED`
Required: No

 ** [usageRestrictions](#API_CreateGlossary_RequestSyntax) **   <a name="datazone-CreateGlossary-request-usageRestrictions"></a>
The usage restriction of the restricted glossary.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `ASSET_GOVERNED_TERMS`
Required: No

## Response Syntax
<a name="API_CreateGlossary_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "description": "string",
   "domainId": "string",
   "id": "string",
   "name": "string",
   "owningProjectId": "string",
   "status": "string",
   "usageRestrictions": [ "string" ]
}
```

## Response Elements
<a name="API_CreateGlossary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [description](#API_CreateGlossary_ResponseSyntax) **   <a name="datazone-CreateGlossary-response-description"></a>
The description of this business glossary.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [domainId](#API_CreateGlossary_ResponseSyntax) **   <a name="datazone-CreateGlossary-response-domainId"></a>
The ID of the Amazon DataZone domain in which this business glossary is created.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [id](#API_CreateGlossary_ResponseSyntax) **   <a name="datazone-CreateGlossary-response-id"></a>
The ID of this business glossary.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [name](#API_CreateGlossary_ResponseSyntax) **   <a name="datazone-CreateGlossary-response-name"></a>
The name of this business glossary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [owningProjectId](#API_CreateGlossary_ResponseSyntax) **   <a name="datazone-CreateGlossary-response-owningProjectId"></a>
The ID of the project that currently owns this business glossary.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [status](#API_CreateGlossary_ResponseSyntax) **   <a name="datazone-CreateGlossary-response-status"></a>
The status of this business glossary.
Type: String
Valid Values: `DISABLED | ENABLED`

 ** [usageRestrictions](#API_CreateGlossary_ResponseSyntax) **   <a name="datazone-CreateGlossary-response-usageRestrictions"></a>
The usage restriction of the restricted glossary.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `ASSET_GOVERNED_TERMS`

## Errors
<a name="API_CreateGlossary_Errors"></a>

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
<a name="API_CreateGlossary_Examples"></a>

### Example
<a name="API_CreateGlossary_Example_1"></a>

This example illustrates one usage of CreateGlossary.

#### Sample Request
<a name="API_CreateGlossary_Example_1_Request"></a>

```
aws datazone create-glossary \
--domain-identifier "dzd_53ielnpxktdilj" \
--name "CustomerAnalyticsGlossary" \
--owning-project-identifier "prj7nx82mkl"
```

#### Sample Response
<a name="API_CreateGlossary_Example_1_Response"></a>

```
{
    "domainId": "dzd_53ielnpxktdilj",
    "id": "gls8m3nqx2wkfp",
    "name": "CustomerAnalyticsGlossary",
    "owningProjectId": "prj7nx82mkl",
    "status": "ENABLED"
}
```

### Example
<a name="API_CreateGlossary_Example_2"></a>

Failure case - duplicate term:

#### Sample Request
<a name="API_CreateGlossary_Example_2_Request"></a>

```
aws datazone create-glossary \
--domain-identifier "dzd_53ielnpxktdilj" \
--name "CustomerAnalyticsGlossary" \
--owning-project-identifier "prj7nx82mkl"
```

#### Sample Response
<a name="API_CreateGlossary_Example_2_Response"></a>

```
An error occurred (ConflictException) when calling the CreateGlossary operation: Conflict with businessGlossary gls8m3nqx2wkfp
```

### Example
<a name="API_CreateGlossary_Example_3"></a>

Failure case - missing required parameter:

#### Sample Request
<a name="API_CreateGlossary_Example_3_Request"></a>

```
aws datazone create-glossary \
--domain-identifier "dzd_53ielnpxktdilj" \
--owning-project-identifier "prj7nx82mkl"
```

#### Sample Response
<a name="API_CreateGlossary_Example_3_Response"></a>

```
aws: error: the following arguments are required: --name
```

## See Also
<a name="API_CreateGlossary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CreateGlossary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CreateGlossary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CreateGlossary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CreateGlossary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CreateGlossary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CreateGlossary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CreateGlossary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CreateGlossary)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CreateGlossary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CreateGlossary)
