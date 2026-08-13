---
source_url: https://docs.aws.amazon.com/account-access/latest/APIReference/API_GetEntitlement.html
---

# GetEntitlement
<a name="API_GetEntitlement"></a>

Retrieves details about a specific entitlement for an account access manager application, including the principal, IAM role, and target account.

## Request Syntax
<a name="API_GetEntitlement_RequestSyntax"></a>

```
GET /entitlements/{{entitlementId}}?applicationArn={{applicationArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEntitlement_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationArn](#API_GetEntitlement_RequestSyntax) **   <a name="accountaccess-GetEntitlement-request-uri-applicationArn"></a>
Specifies the ARN of the application that the entitlement belongs to.
Length Constraints: Minimum length of 49. Maximum length of 2048.
Pattern: `arn:[a-z0-9-]+:account-access:[a-z0-9]+(-[a-z0-9]+)*:[0-9]{12}:application/[a-zA-Z0-9-]+`
Required: Yes

 ** [entitlementId](#API_GetEntitlement_RequestSyntax) **   <a name="accountaccess-GetEntitlement-request-uri-entitlementId"></a>
Specifies the unique identifier of the entitlement to retrieve.
Required: Yes

## Request Body
<a name="API_GetEntitlement_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEntitlement_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationArn": "string",
   "createdAt": "string",
   "entitlement": { ... },
   "entitlementId": "string"
}
```

## Response Elements
<a name="API_GetEntitlement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationArn](#API_GetEntitlement_ResponseSyntax) **   <a name="accountaccess-GetEntitlement-response-applicationArn"></a>
The ARN of the application that the entitlement belongs to.
Type: String
Length Constraints: Minimum length of 49. Maximum length of 2048.
Pattern: `arn:[a-z0-9-]+:account-access:[a-z0-9]+(-[a-z0-9]+)*:[0-9]{12}:application/[a-zA-Z0-9-]+`

 ** [createdAt](#API_GetEntitlement_ResponseSyntax) **   <a name="accountaccess-GetEntitlement-response-createdAt"></a>
The date and time when the entitlement was created.
Type: Timestamp

 ** [entitlement](#API_GetEntitlement_ResponseSyntax) **   <a name="accountaccess-GetEntitlement-response-entitlement"></a>
The entitlement details, including the principal, IAM role, and target account.
Type: [EntitlementDetails](API_EntitlementDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [entitlementId](#API_GetEntitlement_ResponseSyntax) **   <a name="accountaccess-GetEntitlement-response-entitlementId"></a>
The unique identifier of the entitlement.
Type: String

## Errors
<a name="API_GetEntitlement_Errors"></a>

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

 ** ThrottlingException **
The request was denied due to request throttling. Try your request again later.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by the service. Check your request parameters and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_GetEntitlement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-access-2018-05-10/GetEntitlement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-access-2018-05-10/GetEntitlement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-access-2018-05-10/GetEntitlement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-access-2018-05-10/GetEntitlement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-access-2018-05-10/GetEntitlement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-access-2018-05-10/GetEntitlement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-access-2018-05-10/GetEntitlement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-access-2018-05-10/GetEntitlement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/account-access-2018-05-10/GetEntitlement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-access-2018-05-10/GetEntitlement)
