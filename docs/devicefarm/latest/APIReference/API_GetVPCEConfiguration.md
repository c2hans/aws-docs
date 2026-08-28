---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetVPCEConfiguration.html
---

# GetVPCEConfiguration
<a name="API_GetVPCEConfiguration"></a>

Returns information about the configuration settings for your Amazon Virtual Private Cloud (VPC) endpoint.

## Request Syntax
<a name="API_GetVPCEConfiguration_RequestSyntax"></a>

```
{
   "arn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetVPCEConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [arn](#API_GetVPCEConfiguration_RequestSyntax) **   <a name="devicefarm-GetVPCEConfiguration-request-arn"></a>
The Amazon Resource Name (ARN) of the VPC endpoint configuration you want to describe.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

## Response Syntax
<a name="API_GetVPCEConfiguration_ResponseSyntax"></a>

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
<a name="API_GetVPCEConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [vpceConfiguration](#API_GetVPCEConfiguration_ResponseSyntax) **   <a name="devicefarm-GetVPCEConfiguration-response-vpceConfiguration"></a>
An object that contains information about your VPC endpoint configuration.
Type: [VPCEConfiguration](API_VPCEConfiguration.md) object

## Errors
<a name="API_GetVPCEConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ArgumentException **
An invalid argument was specified.
 ** message **
Any additional information about the exception.
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
<a name="API_GetVPCEConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/GetVPCEConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/GetVPCEConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/GetVPCEConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/GetVPCEConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/GetVPCEConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/GetVPCEConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/GetVPCEConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/GetVPCEConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/GetVPCEConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/GetVPCEConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
