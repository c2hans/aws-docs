---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateVPCEConfiguration.html
---

# CreateVPCEConfiguration
<a name="API_CreateVPCEConfiguration"></a>

Creates a configuration record in Device Farm for your Amazon Virtual Private Cloud (VPC) endpoint.

## Request Syntax
<a name="API_CreateVPCEConfiguration_RequestSyntax"></a>

```
{
   "serviceDnsName": "{{string}}",
   "vpceConfigurationDescription": "{{string}}",
   "vpceConfigurationName": "{{string}}",
   "vpceServiceName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateVPCEConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [serviceDnsName](#API_CreateVPCEConfiguration_RequestSyntax) **   <a name="devicefarm-CreateVPCEConfiguration-request-serviceDnsName"></a>
The DNS name of the service running in your VPC that you want Device Farm to test.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: Yes

 ** [vpceConfigurationDescription](#API_CreateVPCEConfiguration_RequestSyntax) **   <a name="devicefarm-CreateVPCEConfiguration-request-vpceConfigurationDescription"></a>
An optional description that provides details about your VPC endpoint configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [vpceConfigurationName](#API_CreateVPCEConfiguration_RequestSyntax) **   <a name="devicefarm-CreateVPCEConfiguration-request-vpceConfigurationName"></a>
The friendly name you give to your VPC endpoint configuration, to manage your configurations more easily.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: Yes

 ** [vpceServiceName](#API_CreateVPCEConfiguration_RequestSyntax) **   <a name="devicefarm-CreateVPCEConfiguration-request-vpceServiceName"></a>
The name of the VPC endpoint service running in your AWS account that you want Device Farm to test.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_CreateVPCEConfiguration_ResponseSyntax"></a>

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
<a name="API_CreateVPCEConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [vpceConfiguration](#API_CreateVPCEConfiguration_ResponseSyntax) **   <a name="devicefarm-CreateVPCEConfiguration-response-vpceConfiguration"></a>
An object that contains information about your VPC endpoint configuration.
Type: [VPCEConfiguration](API_VPCEConfiguration.md) object

## Errors
<a name="API_CreateVPCEConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ArgumentException **
An invalid argument was specified.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** LimitExceededException **
A limit was exceeded.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** ServiceAccountException **
There was a problem with the service account.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateVPCEConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/CreateVPCEConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/CreateVPCEConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/CreateVPCEConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/CreateVPCEConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/CreateVPCEConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/CreateVPCEConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/CreateVPCEConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/CreateVPCEConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/CreateVPCEConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/CreateVPCEConfiguration)
