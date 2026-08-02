---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetDeliveryDestinationPolicy.html
---

# GetDeliveryDestinationPolicy
<a name="API_GetDeliveryDestinationPolicy"></a>

Retrieves the delivery destination policy assigned to the delivery destination that you specify. For more information about delivery destinations and their policies, see [PutDeliveryDestinationPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.html).

## Request Syntax
<a name="API_GetDeliveryDestinationPolicy_RequestSyntax"></a>

```
{
   "deliveryDestinationName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDeliveryDestinationPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [deliveryDestinationName](#API_GetDeliveryDestinationPolicy_RequestSyntax) **   <a name="CWL-GetDeliveryDestinationPolicy-request-deliveryDestinationName"></a>
The name of the delivery destination that you want to retrieve the policy of.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[\w-]*`
Required: Yes

## Response Syntax
<a name="API_GetDeliveryDestinationPolicy_ResponseSyntax"></a>

```
{
   "policy": {
      "deliveryDestinationPolicy": "string"
   }
}
```

## Response Elements
<a name="API_GetDeliveryDestinationPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policy](#API_GetDeliveryDestinationPolicy_ResponseSyntax) **   <a name="CWL-GetDeliveryDestinationPolicy-response-policy"></a>
The IAM policy for this delivery destination.
Type: [Policy](API_Policy.md) object

## Errors
<a name="API_GetDeliveryDestinationPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

 ** ValidationException **
One of the parameters for the request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_GetDeliveryDestinationPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/GetDeliveryDestinationPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/GetDeliveryDestinationPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/GetDeliveryDestinationPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/GetDeliveryDestinationPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/GetDeliveryDestinationPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/GetDeliveryDestinationPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/GetDeliveryDestinationPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/GetDeliveryDestinationPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/GetDeliveryDestinationPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/GetDeliveryDestinationPolicy)
