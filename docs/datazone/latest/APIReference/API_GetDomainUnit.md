---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetDomainUnit.html
---

# GetDomainUnit
<a name="API_GetDomainUnit"></a>

Gets the details of the specified domain unit.

## Request Syntax
<a name="API_GetDomainUnit_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/domain-units/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDomainUnit_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetDomainUnit_RequestSyntax) **   <a name="datazone-GetDomainUnit-request-uri-domainIdentifier"></a>
The ID of the domain where you want to get a domain unit.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_GetDomainUnit_RequestSyntax) **   <a name="datazone-GetDomainUnit-request-uri-identifier"></a>
The identifier of the domain unit that you want to get.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`
Required: Yes

## Request Body
<a name="API_GetDomainUnit_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDomainUnit_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "createdBy": "string",
   "description": "string",
   "domainId": "string",
   "id": "string",
   "lastUpdatedAt": number,
   "lastUpdatedBy": "string",
   "name": "string",
   "owners": [
      { ... }
   ],
   "parentDomainUnitId": "string"
}
```

## Response Elements
<a name="API_GetDomainUnit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetDomainUnit_ResponseSyntax) **   <a name="datazone-GetDomainUnit-response-createdAt"></a>
The time stamp at which the domain unit was created.
Type: Timestamp

 ** [createdBy](#API_GetDomainUnit_ResponseSyntax) **   <a name="datazone-GetDomainUnit-response-createdBy"></a>
The user who created the domain unit.
Type: String

 ** [description](#API_GetDomainUnit_ResponseSyntax) **   <a name="datazone-GetDomainUnit-response-description"></a>
The description of the domain unit.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_GetDomainUnit_ResponseSyntax) **   <a name="datazone-GetDomainUnit-response-domainId"></a>
The ID of the domain in which the domain unit lives.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [id](#API_GetDomainUnit_ResponseSyntax) **   <a name="datazone-GetDomainUnit-response-id"></a>
The ID of the domain unit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`

 ** [lastUpdatedAt](#API_GetDomainUnit_ResponseSyntax) **   <a name="datazone-GetDomainUnit-response-lastUpdatedAt"></a>
The timestamp at which the domain unit was last updated.
Type: Timestamp

 ** [lastUpdatedBy](#API_GetDomainUnit_ResponseSyntax) **   <a name="datazone-GetDomainUnit-response-lastUpdatedBy"></a>
The user who last updated the domain unit.
Type: String

 ** [name](#API_GetDomainUnit_ResponseSyntax) **   <a name="datazone-GetDomainUnit-response-name"></a>
The name of the domain unit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w -]+`

 ** [owners](#API_GetDomainUnit_ResponseSyntax) **   <a name="datazone-GetDomainUnit-response-owners"></a>
The owners of the domain unit.
Type: Array of [DomainUnitOwnerProperties](API_DomainUnitOwnerProperties.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

 ** [parentDomainUnitId](#API_GetDomainUnit_ResponseSyntax) **   <a name="datazone-GetDomainUnit-response-parentDomainUnitId"></a>
The ID of the parent domain unit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`

## Errors
<a name="API_GetDomainUnit_Errors"></a>

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

## See Also
<a name="API_GetDomainUnit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetDomainUnit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetDomainUnit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetDomainUnit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetDomainUnit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetDomainUnit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetDomainUnit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetDomainUnit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetDomainUnit)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetDomainUnit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetDomainUnit)
