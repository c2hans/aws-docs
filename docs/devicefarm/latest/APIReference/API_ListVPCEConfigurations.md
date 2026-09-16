---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListVPCEConfigurations.html
---

# ListVPCEConfigurations
<a name="API_ListVPCEConfigurations"></a>

Returns information about all Amazon Virtual Private Cloud (VPC) endpoint configurations in the AWS account.

## Request Syntax
<a name="API_ListVPCEConfigurations_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListVPCEConfigurations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListVPCEConfigurations_RequestSyntax) **   <a name="devicefarm-ListVPCEConfigurations-request-maxResults"></a>
An integer that specifies the maximum number of items you want to return in the API response.
Type: Integer
Required: No

 ** [nextToken](#API_ListVPCEConfigurations_RequestSyntax) **   <a name="devicefarm-ListVPCEConfigurations-request-nextToken"></a>
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListVPCEConfigurations_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "vpceConfigurations": [
      {
         "arn": "string",
         "serviceDnsName": "string",
         "vpceConfigurationDescription": "string",
         "vpceConfigurationName": "string",
         "vpceServiceName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListVPCEConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListVPCEConfigurations_ResponseSyntax) **   <a name="devicefarm-ListVPCEConfigurations-response-nextToken"></a>
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.

 ** [vpceConfigurations](#API_ListVPCEConfigurations_ResponseSyntax) **   <a name="devicefarm-ListVPCEConfigurations-response-vpceConfigurations"></a>
An array of `VPCEConfiguration` objects that contain information about your VPC endpoint configuration.
Type: Array of [VPCEConfiguration](API_VPCEConfiguration.md) objects

## Errors
<a name="API_ListVPCEConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ArgumentException **
An invalid argument was specified.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** ServiceAccountException **
There was a problem with the service account.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListVPCEConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/ListVPCEConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/ListVPCEConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/ListVPCEConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/ListVPCEConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/ListVPCEConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/ListVPCEConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/ListVPCEConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/ListVPCEConfigurations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/ListVPCEConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/ListVPCEConfigurations)
