---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetDomain.html
---

# GetDomain
<a name="API_GetDomain"></a>

Gets an Amazon DataZone domain.

## Request Syntax
<a name="API_GetDomain_RequestSyntax"></a>

```
GET /v2/domains/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDomain_RequestParameters"></a>

The request uses the following URI parameters.

 ** [identifier](#API_GetDomain_RequestSyntax) **   <a name="datazone-GetDomain-request-uri-identifier"></a>
The identifier of the specified Amazon DataZone domain.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_GetDomain_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDomain_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "createdAt": number,
   "description": "string",
   "domainExecutionRole": "string",
   "domainVersion": "string",
   "id": "string",
   "kmsKeyIdentifier": "string",
   "lastUpdatedAt": number,
   "name": "string",
   "portalUrl": "string",
   "rootDomainUnitId": "string",
   "serviceRole": "string",
   "singleSignOn": {
      "idcInstanceArn": "string",
      "type": "string",
      "userAssignment": "string"
   },
   "status": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetDomain_ResponseSyntax) **   <a name="datazone-GetDomain-response-arn"></a>
The ARN of the specified Amazon DataZone domain.
Type: String

 ** [createdAt](#API_GetDomain_ResponseSyntax) **   <a name="datazone-GetDomain-response-createdAt"></a>
The timestamp of when the Amazon DataZone domain was created.
Type: Timestamp

 ** [description](#API_GetDomain_ResponseSyntax) **   <a name="datazone-GetDomain-response-description"></a>
The description of the Amazon DataZone domain.
Type: String

 ** [domainExecutionRole](#API_GetDomain_ResponseSyntax) **   <a name="datazone-GetDomain-response-domainExecutionRole"></a>
The domain execution role with which the Amazon DataZone domain is created.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+`

 ** [domainVersion](#API_GetDomain_ResponseSyntax) **   <a name="datazone-GetDomain-response-domainVersion"></a>
The version of the domain.
Type: String
Valid Values: `V1 | V2`

 ** [id](#API_GetDomain_ResponseSyntax) **   <a name="datazone-GetDomain-response-id"></a>
The identifier of the specified Amazon DataZone domain.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [kmsKeyIdentifier](#API_GetDomain_ResponseSyntax) **   <a name="datazone-GetDomain-response-kmsKeyIdentifier"></a>
The identifier of the AWS Key Management Service (KMS) key that is used to encrypt the Amazon DataZone domain, metadata, and reporting data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`

 ** [lastUpdatedAt](#API_GetDomain_ResponseSyntax) **   <a name="datazone-GetDomain-response-lastUpdatedAt"></a>
The timestamp of when the Amazon DataZone domain was last updated.
Type: Timestamp

 ** [name](#API_GetDomain_ResponseSyntax) **   <a name="datazone-GetDomain-response-name"></a>
The name of the Amazon DataZone domain.
Type: String

 ** [portalUrl](#API_GetDomain_ResponseSyntax) **   <a name="datazone-GetDomain-response-portalUrl"></a>
The URL of the data portal for this Amazon DataZone domain.
Type: String

 ** [rootDomainUnitId](#API_GetDomain_ResponseSyntax) **   <a name="datazone-GetDomain-response-rootDomainUnitId"></a>
The ID of the root domain in Amazon Datazone.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`

 ** [serviceRole](#API_GetDomain_ResponseSyntax) **   <a name="datazone-GetDomain-response-serviceRole"></a>
The service role of the domain.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+`

 ** [singleSignOn](#API_GetDomain_ResponseSyntax) **   <a name="datazone-GetDomain-response-singleSignOn"></a>
The single sing-on option of the specified Amazon DataZone domain.
Type: [SingleSignOn](API_SingleSignOn.md) object

 ** [status](#API_GetDomain_ResponseSyntax) **   <a name="datazone-GetDomain-response-status"></a>
The status of the specified Amazon DataZone domain.
Type: String
Valid Values: `CREATING | AVAILABLE | CREATION_FAILED | DELETING | DELETED | DELETION_FAILED`

 ** [tags](#API_GetDomain_ResponseSyntax) **   <a name="datazone-GetDomain-response-tags"></a>
The tags specified for the Amazon DataZone domain.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\w \.:/=+@-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[\w \.:/=+@-]*`

## Errors
<a name="API_GetDomain_Errors"></a>

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
<a name="API_GetDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetDomain)
