---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_AddEntityOwner.html
---

# AddEntityOwner
<a name="API_AddEntityOwner"></a>

Adds the owner of an entity (a domain unit).

## Request Syntax
<a name="API_AddEntityOwner_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/entities/{{entityType}}/{{entityIdentifier}}/addOwner HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "owner": { ... }
}
```

## URI Request Parameters
<a name="API_AddEntityOwner_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_AddEntityOwner_RequestSyntax) **   <a name="datazone-AddEntityOwner-request-uri-domainIdentifier"></a>
The ID of the domain in which you want to add the entity owner.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [entityIdentifier](#API_AddEntityOwner_RequestSyntax) **   <a name="datazone-AddEntityOwner-request-uri-entityIdentifier"></a>
The ID of the entity to which you want to add an owner.
Required: Yes

 ** [entityType](#API_AddEntityOwner_RequestSyntax) **   <a name="datazone-AddEntityOwner-request-uri-entityType"></a>
The type of an entity.
Valid Values: `DOMAIN_UNIT`
Required: Yes

## Request Body
<a name="API_AddEntityOwner_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_AddEntityOwner_RequestSyntax) **   <a name="datazone-AddEntityOwner-request-clientToken"></a>
A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [owner](#API_AddEntityOwner_RequestSyntax) **   <a name="datazone-AddEntityOwner-request-owner"></a>
The owner that you want to add to the entity.
Type: [OwnerProperties](API_OwnerProperties.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_AddEntityOwner_ResponseSyntax"></a>

```
HTTP/1.1 201
```

## Response Elements
<a name="API_AddEntityOwner_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response with an empty HTTP body.

## Errors
<a name="API_AddEntityOwner_Errors"></a>

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
<a name="API_AddEntityOwner_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/AddEntityOwner)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/AddEntityOwner)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/AddEntityOwner)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/AddEntityOwner)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/AddEntityOwner)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/AddEntityOwner)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/AddEntityOwner)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/AddEntityOwner)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/AddEntityOwner)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/AddEntityOwner)
