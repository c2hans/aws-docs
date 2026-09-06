---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateDomainUnit.html
---

# CreateDomainUnit
<a name="API_CreateDomainUnit"></a>

Creates a domain unit in Amazon DataZone.

## Request Syntax
<a name="API_CreateDomainUnit_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/domain-units HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "parentDomainUnitIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateDomainUnit_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_CreateDomainUnit_RequestSyntax) **   <a name="datazone-CreateDomainUnit-request-uri-domainIdentifier"></a>
The ID of the domain where you want to crate a domain unit.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_CreateDomainUnit_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateDomainUnit_RequestSyntax) **   <a name="datazone-CreateDomainUnit-request-clientToken"></a>
A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [description](#API_CreateDomainUnit_RequestSyntax) **   <a name="datazone-CreateDomainUnit-request-description"></a>
The description of the domain unit.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [name](#API_CreateDomainUnit_RequestSyntax) **   <a name="datazone-CreateDomainUnit-request-name"></a>
The name of the domain unit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w -]+`
Required: Yes

 ** [parentDomainUnitIdentifier](#API_CreateDomainUnit_RequestSyntax) **   <a name="datazone-CreateDomainUnit-request-parentDomainUnitIdentifier"></a>
The ID of the parent domain unit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`
Required: Yes

## Response Syntax
<a name="API_CreateDomainUnit_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "ancestorDomainUnitIds": [ "string" ],
   "createdAt": number,
   "createdBy": "string",
   "description": "string",
   "domainId": "string",
   "id": "string",
   "name": "string",
   "owners": [
      { ... }
   ],
   "parentDomainUnitId": "string"
}
```

## Response Elements
<a name="API_CreateDomainUnit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [ancestorDomainUnitIds](#API_CreateDomainUnit_ResponseSyntax) **   <a name="datazone-CreateDomainUnit-response-ancestorDomainUnitIds"></a>
The IDs of the ancestor domain units.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`

 ** [createdAt](#API_CreateDomainUnit_ResponseSyntax) **   <a name="datazone-CreateDomainUnit-response-createdAt"></a>
The timestamp at which the domain unit was created.
Type: Timestamp

 ** [createdBy](#API_CreateDomainUnit_ResponseSyntax) **   <a name="datazone-CreateDomainUnit-response-createdBy"></a>
The user who created the domain unit.
Type: String

 ** [description](#API_CreateDomainUnit_ResponseSyntax) **   <a name="datazone-CreateDomainUnit-response-description"></a>
The description of the domain unit.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_CreateDomainUnit_ResponseSyntax) **   <a name="datazone-CreateDomainUnit-response-domainId"></a>
The ID of the domain where the domain unit was created.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [id](#API_CreateDomainUnit_ResponseSyntax) **   <a name="datazone-CreateDomainUnit-response-id"></a>
The ID of the domain unit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`

 ** [name](#API_CreateDomainUnit_ResponseSyntax) **   <a name="datazone-CreateDomainUnit-response-name"></a>
The name of the domain unit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w -]+`

 ** [owners](#API_CreateDomainUnit_ResponseSyntax) **   <a name="datazone-CreateDomainUnit-response-owners"></a>
The owners of the domain unit.
Type: Array of [DomainUnitOwnerProperties](API_DomainUnitOwnerProperties.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

 ** [parentDomainUnitId](#API_CreateDomainUnit_ResponseSyntax) **   <a name="datazone-CreateDomainUnit-response-parentDomainUnitId"></a>
The ID of the parent domain unit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`

## Errors
<a name="API_CreateDomainUnit_Errors"></a>

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

## See Also
<a name="API_CreateDomainUnit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CreateDomainUnit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CreateDomainUnit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CreateDomainUnit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CreateDomainUnit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CreateDomainUnit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CreateDomainUnit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CreateDomainUnit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CreateDomainUnit)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CreateDomainUnit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CreateDomainUnit)
