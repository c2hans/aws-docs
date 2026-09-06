---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PublicWorkforceTaskPrice.html
---

# PublicWorkforceTaskPrice
<a name="API_PublicWorkforceTaskPrice"></a>

Defines the amount of money paid to an Amazon Mechanical Turk worker for each task performed.

Use one of the following prices for bounding box tasks. Prices are in US dollars and should be based on the complexity of the task; the longer it takes in your initial testing, the more you should offer.
+ 0.036
+ 0.048
+ 0.060
+ 0.072
+ 0.120
+ 0.240
+ 0.360
+ 0.480
+ 0.600
+ 0.720
+ 0.840
+ 0.960
+ 1.080
+ 1.200

Use one of the following prices for image classification, text classification, and custom tasks. Prices are in US dollars.
+ 0.012
+ 0.024
+ 0.036
+ 0.048
+ 0.060
+ 0.072
+ 0.120
+ 0.240
+ 0.360
+ 0.480
+ 0.600
+ 0.720
+ 0.840
+ 0.960
+ 1.080
+ 1.200

Use one of the following prices for semantic segmentation tasks. Prices are in US dollars.
+ 0.840
+ 0.960
+ 1.080
+ 1.200

Use one of the following prices for Textract AnalyzeDocument Important Form Key Amazon Augmented AI review tasks. Prices are in US dollars.
+ 2.400
+ 2.280
+ 2.160
+ 2.040
+ 1.920
+ 1.800
+ 1.680
+ 1.560
+ 1.440
+ 1.320
+ 1.200
+ 1.080
+ 0.960
+ 0.840
+ 0.720
+ 0.600
+ 0.480
+ 0.360
+ 0.240
+ 0.120
+ 0.072
+ 0.060
+ 0.048
+ 0.036
+ 0.024
+ 0.012

Use one of the following prices for Rekognition DetectModerationLabels Amazon Augmented AI review tasks. Prices are in US dollars.
+ 1.200
+ 1.080
+ 0.960
+ 0.840
+ 0.720
+ 0.600
+ 0.480
+ 0.360
+ 0.240
+ 0.120
+ 0.072
+ 0.060
+ 0.048
+ 0.036
+ 0.024
+ 0.012

Use one of the following prices for Amazon Augmented AI custom human review tasks. Prices are in US dollars.
+ 1.200
+ 1.080
+ 0.960
+ 0.840
+ 0.720
+ 0.600
+ 0.480
+ 0.360
+ 0.240
+ 0.120
+ 0.072
+ 0.060
+ 0.048
+ 0.036
+ 0.024
+ 0.012

## Contents
<a name="API_PublicWorkforceTaskPrice_Contents"></a>

 ** AmountInUsd **   <a name="sagemaker-Type-PublicWorkforceTaskPrice-AmountInUsd"></a>
Defines the amount of money paid to an Amazon Mechanical Turk worker in United States dollars.
Type: [USD](API_USD.md) object
Required: No

## See Also
<a name="API_PublicWorkforceTaskPrice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/PublicWorkforceTaskPrice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/PublicWorkforceTaskPrice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/PublicWorkforceTaskPrice)
