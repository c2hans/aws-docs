---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_UpdateApplication.html
---

# UpdateApplication
<a name="API_UpdateApplication"></a>

Updates the configuration of an existing application, including the IAM role and default KMS key.

## Request Syntax
<a name="API_UpdateApplication_RequestSyntax"></a>

```
POST /UpdateApplication HTTP/1.1
Content-type: application/json

{
   "applicationId": "{{string}}",
   "defaultKmsKeyId": "{{string}}",
   "roleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateApplication_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [applicationId](#API_UpdateApplication_RequestSyntax) **   <a name="securityagent-UpdateApplication-request-applicationId"></a>
The unique identifier of the application to update.
Type: String
Required: Yes

 ** [defaultKmsKeyId](#API_UpdateApplication_RequestSyntax) **   <a name="securityagent-UpdateApplication-request-defaultKmsKeyId"></a>
The updated identifier of the default AWS KMS key for the application.
Type: String
Required: No

 ** [roleArn](#API_UpdateApplication_RequestSyntax) **   <a name="securityagent-UpdateApplication-request-roleArn"></a>
The updated Amazon Resource Name (ARN) of the IAM role for the application.
Type: String
Required: No

## Response Syntax
<a name="API_UpdateApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationId": "string"
}
```

## Response Elements
<a name="API_UpdateApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationId](#API_UpdateApplication_ResponseSyntax) **   <a name="securityagent-UpdateApplication-response-applicationId"></a>
The unique identifier of the updated application.
Type: String

## Errors
<a name="API_UpdateApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_UpdateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/UpdateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/UpdateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/UpdateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/UpdateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/UpdateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/UpdateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/UpdateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/UpdateApplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/UpdateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/UpdateApplication)
