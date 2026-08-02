---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetUploadJobPath.html
---

# GetUploadJobPath
<a name="API_connect-customer-profiles_GetUploadJobPath"></a>

This API retrieves the pre-signed URL and client token for uploading the file associated with the upload job.

## Request Syntax
<a name="API_connect-customer-profiles_GetUploadJobPath_RequestSyntax"></a>

```
GET /domains/{{DomainName}}/upload-jobs/{{JobId}}/path HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_GetUploadJobPath_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_GetUploadJobPath_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetUploadJobPath-request-uri-DomainName"></a>
The unique name of the domain containing the upload job.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [JobId](#API_connect-customer-profiles_GetUploadJobPath_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetUploadJobPath-request-uri-JobId"></a>
The unique identifier of the upload job to retrieve the upload path for. This is generated from the CreateUploadJob API.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_GetUploadJobPath_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_GetUploadJobPath_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ClientToken": "string",
   "Url": "string",
   "ValidUntil": number
}
```

## Response Elements
<a name="API_connect-customer-profiles_GetUploadJobPath_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClientToken](#API_connect-customer-profiles_GetUploadJobPath_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetUploadJobPath-response-ClientToken"></a>
The plaintext data key used to encrypt the upload file.
To persist to the pre-signed url, use the client token and MD5 client token as header. The required headers are as follows:
+ x-amz-server-side-encryption-customer-key: Client Token
+ x-amz-server-side-encryption-customer-key-MD5: MD5 Client Token
+ x-amz-server-side-encryption-customer-algorithm: AES256
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.

 ** [Url](#API_connect-customer-profiles_GetUploadJobPath_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetUploadJobPath-response-Url"></a>
The pre-signed S3 URL for uploading the CSV file associated with the upload job.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `.*`

 ** [ValidUntil](#API_connect-customer-profiles_GetUploadJobPath_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetUploadJobPath-response-ValidUntil"></a>
The expiry timestamp for the pre-signed URL, after which the URL will no longer be valid.
Type: Timestamp

## Errors
<a name="API_connect-customer-profiles_GetUploadJobPath_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** InternalServerException **
An internal service error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource does not exist, or access was denied.
HTTP Status Code: 404

 ** ThrottlingException **
You exceeded the maximum number of requests.
HTTP Status Code: 429

## See Also
<a name="API_connect-customer-profiles_GetUploadJobPath_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/GetUploadJobPath)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/GetUploadJobPath)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/GetUploadJobPath)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/GetUploadJobPath)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/GetUploadJobPath)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/GetUploadJobPath)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/GetUploadJobPath)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/GetUploadJobPath)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/GetUploadJobPath)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/GetUploadJobPath)
