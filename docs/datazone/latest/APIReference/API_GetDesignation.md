---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetDesignation.html
---

# GetDesignation
<a name="API_GetDesignation"></a>

Gets the details of a designation, including its Cedar permit policy. Returns the full designation record for both system-managed and user-created designations.

## Request Syntax
<a name="API_GetDesignation_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/designations/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDesignation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetDesignation_RequestSyntax) **   <a name="datazone-GetDesignation-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain that contains the designation.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_GetDesignation_RequestSyntax) **   <a name="datazone-GetDesignation-request-uri-identifier"></a>
The unique ID of the designation to retrieve.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_GetDesignation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDesignation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "createdBy": "string",
   "deletionProtection": boolean,
   "description": "string",
   "designationType": "string",
   "domainId": "string",
   "id": "string",
   "lastUpdatedAt": "string",
   "name": "string",
   "policy": "string"
}
```

## Response Elements
<a name="API_GetDesignation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetDesignation_ResponseSyntax) **   <a name="datazone-GetDesignation-response-createdAt"></a>
The date and time when the designation was created.
Type: Timestamp

 ** [createdBy](#API_GetDesignation_ResponseSyntax) **   <a name="datazone-GetDesignation-response-createdBy"></a>
The identifier of the Amazon DataZone user who created the designation.
Type: String

 ** [deletionProtection](#API_GetDesignation_ResponseSyntax) **   <a name="datazone-GetDesignation-response-deletionProtection"></a>
Specifies whether deletion protection is enabled for this designation. When `true`, `DeleteDesignation` is rejected until protection is disabled through `UpdateDesignation`.
Type: Boolean

 ** [description](#API_GetDesignation_ResponseSyntax) **   <a name="datazone-GetDesignation-response-description"></a>
A human-readable description of the designation and its intended use.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [designationType](#API_GetDesignation_ResponseSyntax) **   <a name="datazone-GetDesignation-response-designationType"></a>
The classification of this designation. Valid values:
+  `MANAGED` — System-defined designations that cannot be modified or deleted.
+  `USER_CREATED` — Designations created through `CreateDesignation`.
Type: String
Valid Values: `MANAGED | USER_CREATED`

 ** [domainId](#API_GetDesignation_ResponseSyntax) **   <a name="datazone-GetDesignation-response-domainId"></a>
The identifier of the Amazon DataZone domain that contains the designation.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [id](#API_GetDesignation_ResponseSyntax) **   <a name="datazone-GetDesignation-response-id"></a>
The unique ID of the designation.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [lastUpdatedAt](#API_GetDesignation_ResponseSyntax) **   <a name="datazone-GetDesignation-response-lastUpdatedAt"></a>
The date and time when the designation was last updated.
Type: Timestamp

 ** [name](#API_GetDesignation_ResponseSyntax) **   <a name="datazone-GetDesignation-response-name"></a>
The name of the designation. The name is unique within the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`

 ** [policy](#API_GetDesignation_ResponseSyntax) **   <a name="datazone-GetDesignation-response-policy"></a>
The Cedar permit policy that governs the actions holders of this designation are allowed to perform.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.

## Errors
<a name="API_GetDesignation_Errors"></a>

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
<a name="API_GetDesignation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetDesignation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetDesignation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetDesignation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetDesignation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetDesignation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetDesignation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetDesignation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetDesignation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetDesignation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetDesignation)
