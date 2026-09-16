---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_UpdateHost.html
---

# UpdateHost
<a name="API_UpdateHost"></a>

Updates a specified host with the provided configurations.

## Request Syntax
<a name="API_UpdateHost_RequestSyntax"></a>

```
{
   "HostArn": "{{string}}",
   "ProviderEndpoint": "{{string}}",
   "VpcConfiguration": {
      "SecurityGroupIds": [ "{{string}}" ],
      "SubnetIds": [ "{{string}}" ],
      "TlsCertificate": "{{string}}",
      "VpcId": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateHost_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [HostArn](#API_UpdateHost_RequestSyntax) **   <a name="codeconnections-UpdateHost-request-HostArn"></a>
The Amazon Resource Name (ARN) of the host to be updated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws(-[\w]+)*:(codestar-connections|codeconnections):.+:[0-9]{12}:host\/.+`
Required: Yes

 ** [ProviderEndpoint](#API_UpdateHost_RequestSyntax) **   <a name="codeconnections-UpdateHost-request-ProviderEndpoint"></a>
The URL or endpoint of the host to be updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*`
Required: No

 ** [VpcConfiguration](#API_UpdateHost_RequestSyntax) **   <a name="codeconnections-UpdateHost-request-VpcConfiguration"></a>
The VPC configuration of the host to be updated. A VPC must be configured and the infrastructure to be represented by the host must already be connected to the VPC.
Type: [VpcConfiguration](API_VpcConfiguration.md) object
Required: No

## Response Elements
<a name="API_UpdateHost_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateHost_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Two conflicting operations have been made on the same resource.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Resource not found. Verify the connection resource ARN and try again.
HTTP Status Code: 400

 ** ResourceUnavailableException **
Resource not found. Verify the ARN for the host resource and try again.
HTTP Status Code: 400

 ** UnsupportedOperationException **
The operation is not supported. Check the connection status and try again.
HTTP Status Code: 400

## See Also
<a name="API_UpdateHost_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeconnections-2023-12-01/UpdateHost)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeconnections-2023-12-01/UpdateHost)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/UpdateHost)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeconnections-2023-12-01/UpdateHost)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/UpdateHost)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeconnections-2023-12-01/UpdateHost)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeconnections-2023-12-01/UpdateHost)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeconnections-2023-12-01/UpdateHost)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codeconnections-2023-12-01/UpdateHost)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/UpdateHost)
