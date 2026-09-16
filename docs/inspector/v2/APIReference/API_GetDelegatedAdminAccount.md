---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetDelegatedAdminAccount.html
---

# GetDelegatedAdminAccount
<a name="API_GetDelegatedAdminAccount"></a>

Retrieves information about the Amazon Inspector delegated administrator for your organization.

## Request Syntax
<a name="API_GetDelegatedAdminAccount_RequestSyntax"></a>

```
POST /delegatedadminaccounts/get HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDelegatedAdminAccount_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetDelegatedAdminAccount_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDelegatedAdminAccount_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "delegatedAdmin": {
      "accountId": "string",
      "relationshipStatus": "string"
   }
}
```

## Response Elements
<a name="API_GetDelegatedAdminAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [delegatedAdmin](#API_GetDelegatedAdminAccount_ResponseSyntax) **   <a name="inspector2-GetDelegatedAdminAccount-response-delegatedAdmin"></a>
The AWS account ID of the Amazon Inspector delegated administrator.
Type: [DelegatedAdmin](API_DelegatedAdmin.md) object

## Errors
<a name="API_GetDelegatedAdminAccount_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 For `Enable`, you receive this error if you attempt to use a feature in an unsupported AWS Region.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed due to an internal failure of the Amazon Inspector service.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access an invalid resource. Make sure the resource is specified correctly.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation due to missing required fields or having invalid inputs.
 ** fields **
The fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_GetDelegatedAdminAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/GetDelegatedAdminAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/GetDelegatedAdminAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/GetDelegatedAdminAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/GetDelegatedAdminAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/GetDelegatedAdminAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/GetDelegatedAdminAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/GetDelegatedAdminAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/GetDelegatedAdminAccount)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/GetDelegatedAdminAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/GetDelegatedAdminAccount)
