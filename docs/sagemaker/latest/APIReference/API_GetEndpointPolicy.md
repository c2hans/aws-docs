---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_GetEndpointPolicy.html
---

# GetEndpointPolicy
<a name="API_GetEndpointPolicy"></a>

Returns the resource-based policy that is attached to an endpoint. If the endpoint doesn't have a policy, you get a `ValidationException`.

## Request Syntax
<a name="API_GetEndpointPolicy_RequestSyntax"></a>

```
{
   "EndpointName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetEndpointPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndpointName](#API_GetEndpointPolicy_RequestSyntax) **   <a name="sagemaker-GetEndpointPolicy-request-EndpointName"></a>
The name of the endpoint. The endpoint must be in your account and in the current AWS Region.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_GetEndpointPolicy_ResponseSyntax"></a>

```
{
   "EndpointArn": "string",
   "EndpointName": "string",
   "ResourcePolicy": "string"
}
```

## Response Elements
<a name="API_GetEndpointPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EndpointArn](#API_GetEndpointPolicy_ResponseSyntax) **   <a name="sagemaker-GetEndpointPolicy-response-EndpointArn"></a>
The Amazon Resource Name (ARN) of the endpoint.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:endpoint/.*`

 ** [EndpointName](#API_GetEndpointPolicy_ResponseSyntax) **   <a name="sagemaker-GetEndpointPolicy-response-EndpointName"></a>
The name of the endpoint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [ResourcePolicy](#API_GetEndpointPolicy_ResponseSyntax) **   <a name="sagemaker-GetEndpointPolicy-response-ResourcePolicy"></a>
The endpoint policy, as a JSON policy document.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20480.
Pattern: `.*(?:[ \r\n\t].*)*.*`

## Errors
<a name="API_GetEndpointPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_GetEndpointPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/GetEndpointPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/GetEndpointPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/GetEndpointPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/GetEndpointPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/GetEndpointPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/GetEndpointPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/GetEndpointPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/GetEndpointPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/GetEndpointPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/GetEndpointPolicy)
