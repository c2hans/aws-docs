---
source_url: https://docs.aws.amazon.com/account-access/latest/APIReference/API_GetApplication.html
---

# GetApplication
<a name="API_GetApplication"></a>

Retrieves details about an account access manager application, including its status, identity source, and tags.

## Request Syntax
<a name="API_GetApplication_RequestSyntax"></a>

```
GET /applications/{{applicationArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationArn](#API_GetApplication_RequestSyntax) **   <a name="accountaccess-GetApplication-request-uri-applicationArn"></a>
Specifies the ARN of the application to retrieve.
Length Constraints: Minimum length of 49. Maximum length of 2048.
Pattern: `arn:[a-z0-9-]+:account-access:[a-z0-9]+(-[a-z0-9]+)*:[0-9]{12}:application/[a-zA-Z0-9-]+`
Required: Yes

## Request Body
<a name="API_GetApplication_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "error": {
      "code": "string",
      "message": "string"
   },
   "identitySource": { ... },
   "status": "string",
   "tags": {
      "string" : "string"
   },
   "tenantId": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_GetApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetApplication_ResponseSyntax) **   <a name="accountaccess-GetApplication-response-createdAt"></a>
The date and time when the application was created.
Type: Timestamp

 ** [error](#API_GetApplication_ResponseSyntax) **   <a name="accountaccess-GetApplication-response-error"></a>
The error details if the application is in a failed state.
Type: [ErrorDetails](API_ErrorDetails.md) object

 ** [identitySource](#API_GetApplication_ResponseSyntax) **   <a name="accountaccess-GetApplication-response-identitySource"></a>
The identity source details for the application, including the IAM Identity Center instance configuration.
Type: [IdentitySourceDetails](API_IdentitySourceDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [status](#API_GetApplication_ResponseSyntax) **   <a name="accountaccess-GetApplication-response-status"></a>
The current status of the application.
Type: String
Valid Values: `CREATE_IN_PROGRESS | ACTIVE | DELETE_IN_PROGRESS | CREATE_FAILED | DELETE_FAILED`

 ** [tags](#API_GetApplication_ResponseSyntax) **   <a name="accountaccess-GetApplication-response-tags"></a>
The tags associated with the application.
Type: String to string map

 ** [tenantId](#API_GetApplication_ResponseSyntax) **   <a name="accountaccess-GetApplication-response-tenantId"></a>
The tenant identifier associated with the application.
Type: String

 ** [updatedAt](#API_GetApplication_ResponseSyntax) **   <a name="accountaccess-GetApplication-response-updatedAt"></a>
The date and time when the application was last updated.
Type: Timestamp

## Errors
<a name="API_GetApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
An internal service error occurred. Try your request again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist. Verify that the resource identifier is correct and that the resource exists in the current Region.
HTTP Status Code: 404

 ** ValidationException **
The input does not satisfy the constraints specified by the service. Check your request parameters and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_GetApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-access-2018-05-10/GetApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-access-2018-05-10/GetApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-access-2018-05-10/GetApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-access-2018-05-10/GetApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-access-2018-05-10/GetApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-access-2018-05-10/GetApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-access-2018-05-10/GetApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-access-2018-05-10/GetApplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/account-access-2018-05-10/GetApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-access-2018-05-10/GetApplication)
