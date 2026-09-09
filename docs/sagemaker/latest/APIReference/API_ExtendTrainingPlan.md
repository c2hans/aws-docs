---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ExtendTrainingPlan.html
---

# ExtendTrainingPlan
<a name="API_ExtendTrainingPlan"></a>

Extends an existing training plan by purchasing an extension offering. This allows you to add additional compute capacity time to your training plan without creating a new plan or reconfiguring your workloads.

To find available extension offerings, use the ` [SearchTrainingPlanOfferings](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SearchTrainingPlanOfferings.html) ` API with the `TrainingPlanArn` parameter.

To view the history of extensions for a training plan, use the ` [DescribeTrainingPlanExtensionHistory](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrainingPlanExtensionHistory.html) ` API.

## Request Syntax
<a name="API_ExtendTrainingPlan_RequestSyntax"></a>

```
{
   "TrainingPlanExtensionOfferingId": "{{string}}"
}
```

## Request Parameters
<a name="API_ExtendTrainingPlan_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TrainingPlanExtensionOfferingId](#API_ExtendTrainingPlan_RequestSyntax) **   <a name="sagemaker-ExtendTrainingPlan-request-TrainingPlanExtensionOfferingId"></a>
The unique identifier of the extension offering to purchase. You can retrieve this ID from the `TrainingPlanExtensionOfferings` in the response of the `SearchTrainingPlanOfferings` API.
Type: String
Required: Yes

## Response Syntax
<a name="API_ExtendTrainingPlan_ResponseSyntax"></a>

```
{
   "TrainingPlanExtensions": [
      {
         "AvailabilityZone": "string",
         "AvailabilityZoneId": "string",
         "CurrencyCode": "string",
         "DurationHours": number,
         "PaymentStatus": "string",
         "Status": "string",
         "TrainingPlanExtensionOfferingId": "string",
         "UpfrontFee": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ExtendTrainingPlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TrainingPlanExtensions](#API_ExtendTrainingPlan_ResponseSyntax) **   <a name="sagemaker-ExtendTrainingPlan-response-TrainingPlanExtensions"></a>
The list of extensions for the training plan, including the newly created extension.
Type: Array of [TrainingPlanExtension](API_TrainingPlanExtension.md) objects
Array Members: Minimum number of 0 items.

## Errors
<a name="API_ExtendTrainingPlan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_ExtendTrainingPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ExtendTrainingPlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ExtendTrainingPlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ExtendTrainingPlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ExtendTrainingPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ExtendTrainingPlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ExtendTrainingPlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ExtendTrainingPlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ExtendTrainingPlan)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ExtendTrainingPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ExtendTrainingPlan)
