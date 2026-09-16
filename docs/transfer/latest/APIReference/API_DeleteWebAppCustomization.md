---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_DeleteWebAppCustomization.html
---

# DeleteWebAppCustomization
<a name="API_DeleteWebAppCustomization"></a>

Deletes the `WebAppCustomization` object that corresponds to the web app ID specified.

## Request Syntax
<a name="API_DeleteWebAppCustomization_RequestSyntax"></a>

```
{
   "WebAppId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteWebAppCustomization_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [WebAppId](#API_DeleteWebAppCustomization_RequestSyntax) **   <a name="TransferFamily-DeleteWebAppCustomization-request-WebAppId"></a>
Provide the unique identifier for the web app that contains the customizations that you are deleting.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `webapp-[0-9a-f]{17}`
Required: Yes

## Response Elements
<a name="API_DeleteWebAppCustomization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteWebAppCustomization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConflictException **
This exception is thrown when the `UpdateServer` is called for a file transfer protocol-enabled server that has VPC as the endpoint type and the server's `VpcEndpointID` is not in the available state.
HTTP Status Code: 400

 ** InternalServiceError **
This exception is thrown when an error occurs in the AWS Transfer Family service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
This exception is thrown when a resource is not found by the AWSTransfer Family service.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

## See Also
<a name="API_DeleteWebAppCustomization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transfer-2018-11-05/DeleteWebAppCustomization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transfer-2018-11-05/DeleteWebAppCustomization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/DeleteWebAppCustomization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transfer-2018-11-05/DeleteWebAppCustomization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/DeleteWebAppCustomization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transfer-2018-11-05/DeleteWebAppCustomization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transfer-2018-11-05/DeleteWebAppCustomization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transfer-2018-11-05/DeleteWebAppCustomization)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/transfer-2018-11-05/DeleteWebAppCustomization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/DeleteWebAppCustomization)
