---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteEndpointPolicy.html
---

# DeleteEndpointPolicy

Deletes the resource-based policy that is attached to an endpoint. After you delete the policy, other accounts can no longer send requests to the endpoint through an inference router. The endpoint continues to serve requests from your account. If the endpoint doesn't have a policy, the operation succeeds.

The change typically takes effect within 30 seconds, and can take up to 5 minutes. To revoke access for one account only, use [PutEndpointPolicy](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PutEndpointPolicy.html) to replace the policy with one that doesn't include that account.

## Request Syntax
<a name="API_DeleteEndpointPolicy_RequestSyntax"></a>

```
{
   "EndpointName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteEndpointPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndpointName](#API_DeleteEndpointPolicy_RequestSyntax) **   <a name="sagemaker-DeleteEndpointPolicy-request-EndpointName"></a>
The name of the endpoint. The endpoint must be in your account and in the current AWS Region.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Elements
<a name="API_DeleteEndpointPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteEndpointPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DeleteEndpointPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DeleteEndpointPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DeleteEndpointPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DeleteEndpointPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DeleteEndpointPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DeleteEndpointPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DeleteEndpointPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DeleteEndpointPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DeleteEndpointPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DeleteEndpointPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DeleteEndpointPolicy)
