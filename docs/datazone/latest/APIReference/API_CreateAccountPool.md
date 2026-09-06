---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateAccountPool.html
---

# CreateAccountPool
<a name="API_CreateAccountPool"></a>

Creates an account pool.

## Request Syntax
<a name="API_CreateAccountPool_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/account-pools HTTP/1.1
Content-type: application/json

{
   "accountSource": { ... },
   "description": "{{string}}",
   "name": "{{string}}",
   "resolutionStrategy": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateAccountPool_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_CreateAccountPool_RequestSyntax) **   <a name="datazone-CreateAccountPool-request-uri-domainIdentifier"></a>
The ID of the domain where the account pool is created.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_CreateAccountPool_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountSource](#API_CreateAccountPool_RequestSyntax) **   <a name="datazone-CreateAccountPool-request-accountSource"></a>
The source of accounts for the account pool. In the current release, it's either a static list of accounts provided by the customer or a custom AWS Lambda handler.
Type: [AccountSource](API_AccountSource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [description](#API_CreateAccountPool_RequestSyntax) **   <a name="datazone-CreateAccountPool-request-description"></a>
The description of the account pool.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [name](#API_CreateAccountPool_RequestSyntax) **   <a name="datazone-CreateAccountPool-request-name"></a>
The name of the account pool.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`
Required: Yes

 ** [resolutionStrategy](#API_CreateAccountPool_RequestSyntax) **   <a name="datazone-CreateAccountPool-request-resolutionStrategy"></a>
The mechanism used to resolve the account selection from the account pool.
Type: String
Valid Values: `MANUAL`
Required: Yes

## Response Syntax
<a name="API_CreateAccountPool_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "accountSource": { ... },
   "createdAt": "string",
   "createdBy": "string",
   "description": "string",
   "domainId": "string",
   "domainUnitId": "string",
   "id": "string",
   "lastUpdatedAt": "string",
   "name": "string",
   "resolutionStrategy": "string",
   "updatedBy": "string"
}
```

## Response Elements
<a name="API_CreateAccountPool_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [accountSource](#API_CreateAccountPool_ResponseSyntax) **   <a name="datazone-CreateAccountPool-response-accountSource"></a>
The source of accounts for the account pool. In the current release, it's either a static list of accounts provided by the customer or a custom AWS Lambda handler.
Type: [AccountSource](API_AccountSource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [createdAt](#API_CreateAccountPool_ResponseSyntax) **   <a name="datazone-CreateAccountPool-response-createdAt"></a>
The timestamp at which the account pool was created.
Type: Timestamp

 ** [createdBy](#API_CreateAccountPool_ResponseSyntax) **   <a name="datazone-CreateAccountPool-response-createdBy"></a>
The user who created the account pool.
Type: String

 ** [description](#API_CreateAccountPool_ResponseSyntax) **   <a name="datazone-CreateAccountPool-response-description"></a>
The description of the account pool.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_CreateAccountPool_ResponseSyntax) **   <a name="datazone-CreateAccountPool-response-domainId"></a>
The ID of the domain where the account pool is created.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [domainUnitId](#API_CreateAccountPool_ResponseSyntax) **   <a name="datazone-CreateAccountPool-response-domainUnitId"></a>
The ID of the domain where the account pool is created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`

 ** [id](#API_CreateAccountPool_ResponseSyntax) **   <a name="datazone-CreateAccountPool-response-id"></a>
The ID of the account pool.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [lastUpdatedAt](#API_CreateAccountPool_ResponseSyntax) **   <a name="datazone-CreateAccountPool-response-lastUpdatedAt"></a>
The timestamp at which the account pool was last updated.
Type: Timestamp

 ** [name](#API_CreateAccountPool_ResponseSyntax) **   <a name="datazone-CreateAccountPool-response-name"></a>
The name of the account pool.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`

 ** [resolutionStrategy](#API_CreateAccountPool_ResponseSyntax) **   <a name="datazone-CreateAccountPool-response-resolutionStrategy"></a>
The mechanism used to resolve the account selection from the account pool.
Type: String
Valid Values: `MANUAL`

 ** [updatedBy](#API_CreateAccountPool_ResponseSyntax) **   <a name="datazone-CreateAccountPool-response-updatedBy"></a>
The user who last updated the account pool.
Type: String

## Errors
<a name="API_CreateAccountPool_Errors"></a>

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
<a name="API_CreateAccountPool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CreateAccountPool)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CreateAccountPool)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CreateAccountPool)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CreateAccountPool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CreateAccountPool)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CreateAccountPool)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CreateAccountPool)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CreateAccountPool)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CreateAccountPool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CreateAccountPool)
