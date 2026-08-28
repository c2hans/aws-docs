---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_UpdateDomainUnit.html
---

# UpdateDomainUnit
<a name="API_UpdateDomainUnit"></a>

Updates the domain unit.

## Request Syntax
<a name="API_UpdateDomainUnit_RequestSyntax"></a>

```
PUT /v2/domains/{{domainIdentifier}}/domain-units/{{identifier}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateDomainUnit_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_UpdateDomainUnit_RequestSyntax) **   <a name="datazone-UpdateDomainUnit-request-uri-domainIdentifier"></a>
The ID of the domain where you want to update a domain unit.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_UpdateDomainUnit_RequestSyntax) **   <a name="datazone-UpdateDomainUnit-request-uri-identifier"></a>
The ID of the domain unit that you want to update.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`
Required: Yes

## Request Body
<a name="API_UpdateDomainUnit_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateDomainUnit_RequestSyntax) **   <a name="datazone-UpdateDomainUnit-request-description"></a>
The description of the domain unit that you want to update.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [name](#API_UpdateDomainUnit_RequestSyntax) **   <a name="datazone-UpdateDomainUnit-request-name"></a>
The name of the domain unit that you want to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w -]+`
Required: No

## Response Syntax
<a name="API_UpdateDomainUnit_ResponseSyntax"></a>

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
<a name="API_UpdateDomainUnit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_UpdateDomainUnit_ResponseSyntax) **   <a name="datazone-UpdateDomainUnit-response-createdAt"></a>
The time stamp at which the domain unit that you want to update was created.
Type: Timestamp

 ** [createdBy](#API_UpdateDomainUnit_ResponseSyntax) **   <a name="datazone-UpdateDomainUnit-response-createdBy"></a>
The user who created the domain unit that you want to update.
Type: String

 ** [description](#API_UpdateDomainUnit_ResponseSyntax) **   <a name="datazone-UpdateDomainUnit-response-description"></a>
The description of the domain unit that you want to update.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_UpdateDomainUnit_ResponseSyntax) **   <a name="datazone-UpdateDomainUnit-response-domainId"></a>
The ID of the domain where you want to update the domain unit.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [id](#API_UpdateDomainUnit_ResponseSyntax) **   <a name="datazone-UpdateDomainUnit-response-id"></a>
The ID of the domain unit that you want to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`

 ** [lastUpdatedAt](#API_UpdateDomainUnit_ResponseSyntax) **   <a name="datazone-UpdateDomainUnit-response-lastUpdatedAt"></a>
The timestamp at which the domain unit was last updated.
Type: Timestamp

 ** [lastUpdatedBy](#API_UpdateDomainUnit_ResponseSyntax) **   <a name="datazone-UpdateDomainUnit-response-lastUpdatedBy"></a>
The user who last updated the domain unit.
Type: String

 ** [name](#API_UpdateDomainUnit_ResponseSyntax) **   <a name="datazone-UpdateDomainUnit-response-name"></a>
The name of the domain unit that you want to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w -]+`

 ** [owners](#API_UpdateDomainUnit_ResponseSyntax) **   <a name="datazone-UpdateDomainUnit-response-owners"></a>
The owners of the domain unit that you want to update.
Type: Array of [DomainUnitOwnerProperties](API_DomainUnitOwnerProperties.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

 ** [parentDomainUnitId](#API_UpdateDomainUnit_ResponseSyntax) **   <a name="datazone-UpdateDomainUnit-response-parentDomainUnitId"></a>
The ID of the parent domain unit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`

## Errors
<a name="API_UpdateDomainUnit_Errors"></a>

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

## See Also
<a name="API_UpdateDomainUnit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/UpdateDomainUnit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/UpdateDomainUnit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/UpdateDomainUnit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/UpdateDomainUnit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/UpdateDomainUnit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/UpdateDomainUnit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/UpdateDomainUnit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/UpdateDomainUnit)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/UpdateDomainUnit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/UpdateDomainUnit)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
