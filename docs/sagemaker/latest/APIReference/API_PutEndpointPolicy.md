---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PutEndpointPolicy.html
---

# PutEndpointPolicy
<a name="API_PutEndpointPolicy"></a>

Attaches a resource-based policy to an endpoint. With an endpoint policy, you can allow other AWS accounts to send requests to your endpoint, or to inference components on it, through an inference router. The policy that you specify replaces the endpoint's existing policy, if it has one.

You can't attach a policy to an endpoint whose status is `Deleting` or `Failed`. SageMaker AI rejects a policy that doesn't follow the endpoint policy rules. For information about the policy rules, see [Use destinations in other accounts](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-router-cross-account.html).

Policy changes typically take effect within 30 seconds, and can take up to 5 minutes. If you delete the endpoint, its policy is also deleted, and a new endpoint with the same name has no policy.

## Request Syntax
<a name="API_PutEndpointPolicy_RequestSyntax"></a>

```
{
   "EndpointName": "{{string}}",
   "ResourcePolicy": "{{string}}"
}
```

## Request Parameters
<a name="API_PutEndpointPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndpointName](#API_PutEndpointPolicy_RequestSyntax) **   <a name="sagemaker-PutEndpointPolicy-request-EndpointName"></a>
The name of the endpoint. The endpoint must be in your account and in the current AWS Region.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [ResourcePolicy](#API_PutEndpointPolicy_RequestSyntax) **   <a name="sagemaker-PutEndpointPolicy-request-ResourcePolicy"></a>
The endpoint policy, as a JSON policy document. The policy can contain only ASCII characters. For information about the policy rules, see [Use destinations in other accounts](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-router-cross-account.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20480.
Pattern: `.*(?:[ \r\n\t].*)*.*`
Required: Yes

## Response Syntax
<a name="API_PutEndpointPolicy_ResponseSyntax"></a>

```
{
   "EndpointArn": "string"
}
```

## Response Elements
<a name="API_PutEndpointPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EndpointArn](#API_PutEndpointPolicy_ResponseSyntax) **   <a name="sagemaker-PutEndpointPolicy-response-EndpointArn"></a>
The Amazon Resource Name (ARN) of the endpoint.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:endpoint/.*`

## Errors
<a name="API_PutEndpointPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_PutEndpointPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/PutEndpointPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/PutEndpointPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/PutEndpointPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/PutEndpointPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/PutEndpointPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/PutEndpointPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/PutEndpointPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/PutEndpointPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/PutEndpointPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/PutEndpointPolicy)
