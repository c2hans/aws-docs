---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_UpdateDomain.html
---

# UpdateDomain
<a name="API_UpdateDomain"></a>

Updates a Amazon DataZone domain.

## Request Syntax
<a name="API_UpdateDomain_RequestSyntax"></a>

```
PUT /v2/domains/{{identifier}}?clientToken={{clientToken}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "domainExecutionRole": "{{string}}",
   "name": "{{string}}",
   "serviceRole": "{{string}}",
   "singleSignOn": {
      "idcInstanceArn": "{{string}}",
      "type": "{{string}}",
      "userAssignment": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateDomain_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_UpdateDomain_RequestSyntax) **   <a name="datazone-UpdateDomain-request-uri-clientToken"></a>
A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.

 ** [identifier](#API_UpdateDomain_RequestSyntax) **   <a name="datazone-UpdateDomain-request-uri-identifier"></a>
The ID of the AWS domain that is to be updated.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_UpdateDomain_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateDomain_RequestSyntax) **   <a name="datazone-UpdateDomain-request-description"></a>
The description to be updated as part of the `UpdateDomain` action.
Type: String
Required: No

 ** [domainExecutionRole](#API_UpdateDomain_RequestSyntax) **   <a name="datazone-UpdateDomain-request-domainExecutionRole"></a>
The domain execution role to be updated as part of the `UpdateDomain` action.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+`
Required: No

 ** [name](#API_UpdateDomain_RequestSyntax) **   <a name="datazone-UpdateDomain-request-name"></a>
The name to be updated as part of the `UpdateDomain` action.
Type: String
Required: No

 ** [serviceRole](#API_UpdateDomain_RequestSyntax) **   <a name="datazone-UpdateDomain-request-serviceRole"></a>
The service role of the domain.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+`
Required: No

 ** [singleSignOn](#API_UpdateDomain_RequestSyntax) **   <a name="datazone-UpdateDomain-request-singleSignOn"></a>
The single sign-on option to be updated as part of the `UpdateDomain` action.
Type: [SingleSignOn](API_SingleSignOn.md) object
Required: No

## Response Syntax
<a name="API_UpdateDomain_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "description": "string",
   "domainExecutionRole": "string",
   "id": "string",
   "lastUpdatedAt": number,
   "name": "string",
   "rootDomainUnitId": "string",
   "serviceRole": "string",
   "singleSignOn": {
      "idcInstanceArn": "string",
      "type": "string",
      "userAssignment": "string"
   }
}
```

## Response Elements
<a name="API_UpdateDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [description](#API_UpdateDomain_ResponseSyntax) **   <a name="datazone-UpdateDomain-response-description"></a>
The description to be updated as part of the `UpdateDomain` action.
Type: String

 ** [domainExecutionRole](#API_UpdateDomain_ResponseSyntax) **   <a name="datazone-UpdateDomain-response-domainExecutionRole"></a>
The domain execution role to be updated as part of the `UpdateDomain` action.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+`

 ** [id](#API_UpdateDomain_ResponseSyntax) **   <a name="datazone-UpdateDomain-response-id"></a>
The identifier of the Amazon DataZone domain.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [lastUpdatedAt](#API_UpdateDomain_ResponseSyntax) **   <a name="datazone-UpdateDomain-response-lastUpdatedAt"></a>
Specifies the timestamp of when the domain was last updated.
Type: Timestamp

 ** [name](#API_UpdateDomain_ResponseSyntax) **   <a name="datazone-UpdateDomain-response-name"></a>
The name to be updated as part of the `UpdateDomain` action.
Type: String

 ** [rootDomainUnitId](#API_UpdateDomain_ResponseSyntax) **   <a name="datazone-UpdateDomain-response-rootDomainUnitId"></a>
The ID of the root domain unit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`

 ** [serviceRole](#API_UpdateDomain_ResponseSyntax) **   <a name="datazone-UpdateDomain-response-serviceRole"></a>
The service role of the domain.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+`

 ** [singleSignOn](#API_UpdateDomain_ResponseSyntax) **   <a name="datazone-UpdateDomain-response-singleSignOn"></a>
The single sign-on option of the Amazon DataZone domain.
Type: [SingleSignOn](API_SingleSignOn.md) object

## Errors
<a name="API_UpdateDomain_Errors"></a>

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

## See Also
<a name="API_UpdateDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/UpdateDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/UpdateDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/UpdateDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/UpdateDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/UpdateDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/UpdateDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/UpdateDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/UpdateDomain)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/UpdateDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/UpdateDomain)
