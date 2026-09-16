---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_UpdateVPCEConfiguration.html
---

# UpdateVPCEConfiguration
<a name="API_UpdateVPCEConfiguration"></a>

Updates information about an Amazon Virtual Private Cloud (VPC) endpoint configuration.

## Request Syntax
<a name="API_UpdateVPCEConfiguration_RequestSyntax"></a>

```
{
   "arn": "{{string}}",
   "serviceDnsName": "{{string}}",
   "vpceConfigurationDescription": "{{string}}",
   "vpceConfigurationName": "{{string}}",
   "vpceServiceName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateVPCEConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [arn](#API_UpdateVPCEConfiguration_RequestSyntax) **   <a name="devicefarm-UpdateVPCEConfiguration-request-arn"></a>
The Amazon Resource Name (ARN) of the VPC endpoint configuration you want to update.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

 ** [serviceDnsName](#API_UpdateVPCEConfiguration_RequestSyntax) **   <a name="devicefarm-UpdateVPCEConfiguration-request-serviceDnsName"></a>
The DNS (domain) name used to connect to your private service in your VPC. The DNS name must not already be in use on the internet.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [vpceConfigurationDescription](#API_UpdateVPCEConfiguration_RequestSyntax) **   <a name="devicefarm-UpdateVPCEConfiguration-request-vpceConfigurationDescription"></a>
An optional description that provides details about your VPC endpoint configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [vpceConfigurationName](#API_UpdateVPCEConfiguration_RequestSyntax) **   <a name="devicefarm-UpdateVPCEConfiguration-request-vpceConfigurationName"></a>
The friendly name you give to your VPC endpoint configuration to manage your configurations more easily.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [vpceServiceName](#API_UpdateVPCEConfiguration_RequestSyntax) **   <a name="devicefarm-UpdateVPCEConfiguration-request-vpceServiceName"></a>
The name of the VPC endpoint service running in your AWS account that you want Device Farm to test.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_UpdateVPCEConfiguration_ResponseSyntax"></a>

```
{
   "vpceConfiguration": {
      "arn": "string",
      "serviceDnsName": "string",
      "vpceConfigurationDescription": "string",
      "vpceConfigurationName": "string",
      "vpceServiceName": "string"
   }
}
```

## Response Elements
<a name="API_UpdateVPCEConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [vpceConfiguration](#API_UpdateVPCEConfiguration_ResponseSyntax) **   <a name="devicefarm-UpdateVPCEConfiguration-response-vpceConfiguration"></a>
An object that contains information about your VPC endpoint configuration.
Type: [VPCEConfiguration](API_VPCEConfiguration.md) object

## Errors
<a name="API_UpdateVPCEConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ArgumentException **
An invalid argument was specified.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** InvalidOperationException **
There was an error with the update request, or you do not have sufficient permissions to update this VPC endpoint configuration.
HTTP Status Code: 400

 ** NotFoundException **
The specified entity was not found.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** ServiceAccountException **
There was a problem with the service account.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

## See Also
<a name="API_UpdateVPCEConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/UpdateVPCEConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/UpdateVPCEConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/UpdateVPCEConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/UpdateVPCEConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/UpdateVPCEConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/UpdateVPCEConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/UpdateVPCEConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/UpdateVPCEConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/UpdateVPCEConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/UpdateVPCEConfiguration)
