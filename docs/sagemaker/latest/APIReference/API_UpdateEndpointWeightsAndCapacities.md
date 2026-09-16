---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpointWeightsAndCapacities.html
---

# UpdateEndpointWeightsAndCapacities
<a name="API_UpdateEndpointWeightsAndCapacities"></a>

Updates variant weight of one or more variants associated with an existing endpoint, or capacity of one variant associated with an existing endpoint. When it receives the request, SageMaker sets the endpoint status to `Updating`. After updating the endpoint, it sets the status to `InService`. To check the status of an endpoint, use the [DescribeEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEndpoint.html) API.

## Request Syntax
<a name="API_UpdateEndpointWeightsAndCapacities_RequestSyntax"></a>

```
{
   "DesiredWeightsAndCapacities": [
      {
         "DesiredInstanceCount": {{number}},
         "DesiredWeight": {{number}},
         "ServerlessUpdateConfig": {
            "MaxConcurrency": {{number}},
            "ProvisionedConcurrency": {{number}}
         },
         "VariantName": "{{string}}"
      }
   ],
   "EndpointName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateEndpointWeightsAndCapacities_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DesiredWeightsAndCapacities](#API_UpdateEndpointWeightsAndCapacities_RequestSyntax) **   <a name="sagemaker-UpdateEndpointWeightsAndCapacities-request-DesiredWeightsAndCapacities"></a>
An object that provides new capacity and weight values for a variant.
Type: Array of [DesiredWeightAndCapacity](API_DesiredWeightAndCapacity.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** [EndpointName](#API_UpdateEndpointWeightsAndCapacities_RequestSyntax) **   <a name="sagemaker-UpdateEndpointWeightsAndCapacities-request-EndpointName"></a>
The name of an existing SageMaker endpoint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_UpdateEndpointWeightsAndCapacities_ResponseSyntax"></a>

```
{
   "EndpointArn": "string"
}
```

## Response Elements
<a name="API_UpdateEndpointWeightsAndCapacities_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EndpointArn](#API_UpdateEndpointWeightsAndCapacities_ResponseSyntax) **   <a name="sagemaker-UpdateEndpointWeightsAndCapacities-response-EndpointArn"></a>
The Amazon Resource Name (ARN) of the updated endpoint.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:endpoint/.*`

## Errors
<a name="API_UpdateEndpointWeightsAndCapacities_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_UpdateEndpointWeightsAndCapacities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateEndpointWeightsAndCapacities)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateEndpointWeightsAndCapacities)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateEndpointWeightsAndCapacities)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateEndpointWeightsAndCapacities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateEndpointWeightsAndCapacities)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateEndpointWeightsAndCapacities)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateEndpointWeightsAndCapacities)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateEndpointWeightsAndCapacities)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateEndpointWeightsAndCapacities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateEndpointWeightsAndCapacities)
