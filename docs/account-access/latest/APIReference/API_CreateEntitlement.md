---
source_url: https://docs.aws.amazon.com/account-access/latest/APIReference/API_CreateEntitlement.html
---

# CreateEntitlement
<a name="API_CreateEntitlement"></a>

Creates an entitlement (assignment) in account access manager. An entitlement (assignment) grants a principal (IAM Identity Center user or group) permission to assume a specified IAM role in an AWS account. This operation is idempotent.

## Request Syntax
<a name="API_CreateEntitlement_RequestSyntax"></a>

```
POST /entitlements HTTP/1.1
Content-type: application/json

{
   "applicationArn": "{{string}}",
   "entitlement": { ... }
}
```

## URI Request Parameters
<a name="API_CreateEntitlement_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateEntitlement_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [applicationArn](#API_CreateEntitlement_RequestSyntax) **   <a name="accountaccess-CreateEntitlement-request-applicationArn"></a>
Specifies the ARN of the application to create the entitlement for.
Type: String
Length Constraints: Minimum length of 49. Maximum length of 2048.
Pattern: `arn:[a-z0-9-]+:account-access:[a-z0-9]+(-[a-z0-9]+)*:[0-9]{12}:application/[a-zA-Z0-9-]+`
Required: Yes

 ** [entitlement](#API_CreateEntitlement_RequestSyntax) **   <a name="accountaccess-CreateEntitlement-request-entitlement"></a>
Specifies the entitlement configuration, including the principal and the IAM role to grant access to.
Type: [Entitlement](API_Entitlement.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_CreateEntitlement_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "entitlementId": "string"
}
```

## Response Elements
<a name="API_CreateEntitlement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [entitlementId](#API_CreateEntitlement_ResponseSyntax) **   <a name="accountaccess-CreateEntitlement-response-entitlementId"></a>
The unique identifier of the created entitlement.
Type: String

## Errors
<a name="API_CreateEntitlement_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this operation.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource.
HTTP Status Code: 409

 ** InternalServerException **
An internal service error occurred. Try your request again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist. Verify that the resource identifier is correct and that the resource exists in the current Region.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request exceeds a service quota for your account.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling. Try your request again later.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by the service. Check your request parameters and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_CreateEntitlement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-access-2018-05-10/CreateEntitlement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-access-2018-05-10/CreateEntitlement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-access-2018-05-10/CreateEntitlement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-access-2018-05-10/CreateEntitlement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-access-2018-05-10/CreateEntitlement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-access-2018-05-10/CreateEntitlement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-access-2018-05-10/CreateEntitlement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-access-2018-05-10/CreateEntitlement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/account-access-2018-05-10/CreateEntitlement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-access-2018-05-10/CreateEntitlement)
