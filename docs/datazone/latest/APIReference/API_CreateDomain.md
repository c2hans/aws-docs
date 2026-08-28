---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateDomain.html
---

# CreateDomain
<a name="API_CreateDomain"></a>

Creates an Amazon DataZone domain.

## Request Syntax
<a name="API_CreateDomain_RequestSyntax"></a>

```
POST /v2/domains HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "domainExecutionRole": "{{string}}",
   "domainVersion": "{{string}}",
   "kmsKeyIdentifier": "{{string}}",
   "name": "{{string}}",
   "serviceRole": "{{string}}",
   "singleSignOn": {
      "idcInstanceArn": "{{string}}",
      "type": "{{string}}",
      "userAssignment": "{{string}}"
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateDomain_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateDomain_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateDomain_RequestSyntax) **   <a name="datazone-CreateDomain-request-clientToken"></a>
A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.
Type: String
Required: No

 ** [description](#API_CreateDomain_RequestSyntax) **   <a name="datazone-CreateDomain-request-description"></a>
The description of the Amazon DataZone domain.
Type: String
Required: No

 ** [domainExecutionRole](#API_CreateDomain_RequestSyntax) **   <a name="datazone-CreateDomain-request-domainExecutionRole"></a>
The domain execution role that is created when an Amazon DataZone domain is created. The domain execution role is created in the AWS account that houses the Amazon DataZone domain.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+`
Required: No

 ** [domainVersion](#API_CreateDomain_RequestSyntax) **   <a name="datazone-CreateDomain-request-domainVersion"></a>
The version of the domain that is created.
Type: String
Valid Values: `V1 | V2`
Required: No

 ** [kmsKeyIdentifier](#API_CreateDomain_RequestSyntax) **   <a name="datazone-CreateDomain-request-kmsKeyIdentifier"></a>
The identifier of the AWS Key Management Service (KMS) key that is used to encrypt the Amazon DataZone domain, metadata, and reporting data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`
Required: No

 ** [name](#API_CreateDomain_RequestSyntax) **   <a name="datazone-CreateDomain-request-name"></a>
The name of the Amazon DataZone domain.
Type: String
Required: Yes

 ** [serviceRole](#API_CreateDomain_RequestSyntax) **   <a name="datazone-CreateDomain-request-serviceRole"></a>
The service role of the domain that is created.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+`
Required: No

 ** [singleSignOn](#API_CreateDomain_RequestSyntax) **   <a name="datazone-CreateDomain-request-singleSignOn"></a>
The single-sign on configuration of the Amazon DataZone domain.
Type: [SingleSignOn](API_SingleSignOn.md) object
Required: No

 ** [tags](#API_CreateDomain_RequestSyntax) **   <a name="datazone-CreateDomain-request-tags"></a>
The tags specified for the Amazon DataZone domain.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\w \.:/=+@-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[\w \.:/=+@-]*`
Required: No

## Response Syntax
<a name="API_CreateDomain_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string",
   "description": "string",
   "domainExecutionRole": "string",
   "domainVersion": "string",
   "id": "string",
   "kmsKeyIdentifier": "string",
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
<a name="API_CreateDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateDomain_ResponseSyntax) **   <a name="datazone-CreateDomain-response-arn"></a>
The ARN of the Amazon DataZone domain.
Type: String

 ** [description](#API_CreateDomain_ResponseSyntax) **   <a name="datazone-CreateDomain-response-description"></a>
The description of the Amazon DataZone domain.
Type: String

 ** [domainExecutionRole](#API_CreateDomain_ResponseSyntax) **   <a name="datazone-CreateDomain-response-domainExecutionRole"></a>
The domain execution role that is created when an Amazon DataZone domain is created. The domain execution role is created in the AWS account that houses the Amazon DataZone domain.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+`

 ** [domainVersion](#API_CreateDomain_ResponseSyntax) **   <a name="datazone-CreateDomain-response-domainVersion"></a>
The version of the domain that is created.
Type: String
Valid Values: `V1 | V2`

 ** [id](#API_CreateDomain_ResponseSyntax) **   <a name="datazone-CreateDomain-response-id"></a>
The identifier of the Amazon DataZone domain.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [kmsKeyIdentifier](#API_CreateDomain_ResponseSyntax) **   <a name="datazone-CreateDomain-response-kmsKeyIdentifier"></a>
The identifier of the AWS Key Management Service (KMS) key that is used to encrypt the Amazon DataZone domain, metadata, and reporting data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`

 ** [name](#API_CreateDomain_ResponseSyntax) **   <a name="datazone-CreateDomain-response-name"></a>
The name of the Amazon DataZone domain.
Type: String

 ** [portalUrl](#API_CreateDomain_ResponseSyntax) **   <a name="datazone-CreateDomain-response-portalUrl"></a>
The URL of the data portal for this Amazon DataZone domain.
Type: String

 ** [rootDomainUnitId](#API_CreateDomain_ResponseSyntax) **   <a name="datazone-CreateDomain-response-rootDomainUnitId"></a>
The ID of the root domain unit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`

 ** [serviceRole](#API_CreateDomain_ResponseSyntax) **   <a name="datazone-CreateDomain-response-serviceRole"></a>
Te service role of the domain that is created.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+`

 ** [singleSignOn](#API_CreateDomain_ResponseSyntax) **   <a name="datazone-CreateDomain-response-singleSignOn"></a>
The single-sign on configuration of the Amazon DataZone domain.
Type: [SingleSignOn](API_SingleSignOn.md) object

 ** [status](#API_CreateDomain_ResponseSyntax) **   <a name="datazone-CreateDomain-response-status"></a>
The status of the Amazon DataZone domain.
Type: String
Valid Values: `CREATING | AVAILABLE | CREATION_FAILED | DELETING | DELETED | DELETION_FAILED`

 ** [tags](#API_CreateDomain_ResponseSyntax) **   <a name="datazone-CreateDomain-response-tags"></a>
The tags specified for the Amazon DataZone domain.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\w \.:/=+@-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[\w \.:/=+@-]*`

## Errors
<a name="API_CreateDomain_Errors"></a>

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
<a name="API_CreateDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CreateDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CreateDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CreateDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CreateDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CreateDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CreateDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CreateDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CreateDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CreateDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CreateDomain)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
