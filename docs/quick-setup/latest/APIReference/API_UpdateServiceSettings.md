---
source_url: https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_UpdateServiceSettings.html
---

# UpdateServiceSettings
<a name="API_UpdateServiceSettings"></a>

Updates settings configured for Quick Setup.

## Request Syntax
<a name="API_UpdateServiceSettings_RequestSyntax"></a>

```
PUT /serviceSettings HTTP/1.1
Content-type: application/json

{
   "ExplorerEnablingRoleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateServiceSettings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateServiceSettings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ExplorerEnablingRoleArn](#API_UpdateServiceSettings_RequestSyntax) **   <a name="quicksetup-UpdateServiceSettings-request-ExplorerEnablingRoleArn"></a>
The IAM role used to enable Explorer.
Type: String
Pattern: `arn:aws(-cn|-us-gov)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+.*`
Required: No

## Response Syntax
<a name="API_UpdateServiceSettings_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateServiceSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateServiceSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The requester has insufficient permissions to perform the operation.
HTTP Status Code: 403

 ** ConflictException **
Another request is being processed. Wait a few minutes and try again.
HTTP Status Code: 409

 ** InternalServerException **
An error occurred on the server side.
HTTP Status Code: 500

 ** ThrottlingException **
The request or operation exceeds the maximum allowed request rate per AWS account and AWS Region.
HTTP Status Code: 429

 ** ValidationException **
The request is invalid. Verify the values provided for the request parameters are accurate.
HTTP Status Code: 400

## See Also
<a name="API_UpdateServiceSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-quicksetup-2018-05-10/UpdateServiceSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-quicksetup-2018-05-10/UpdateServiceSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-quicksetup-2018-05-10/UpdateServiceSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-quicksetup-2018-05-10/UpdateServiceSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-quicksetup-2018-05-10/UpdateServiceSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-quicksetup-2018-05-10/UpdateServiceSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-quicksetup-2018-05-10/UpdateServiceSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-quicksetup-2018-05-10/UpdateServiceSettings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-quicksetup-2018-05-10/UpdateServiceSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-quicksetup-2018-05-10/UpdateServiceSettings)
