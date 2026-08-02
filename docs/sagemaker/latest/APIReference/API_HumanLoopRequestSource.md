---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HumanLoopRequestSource.html
---

# HumanLoopRequestSource
<a name="API_HumanLoopRequestSource"></a>

Container for configuring the source of human task requests.

## Contents
<a name="API_HumanLoopRequestSource_Contents"></a>

 ** AwsManagedHumanLoopRequestSource **   <a name="sagemaker-Type-HumanLoopRequestSource-AwsManagedHumanLoopRequestSource"></a>
Specifies whether Amazon Rekognition or Amazon Textract are used as the integration source. The default field settings and JSON parsing rules are different based on the integration source. Valid values:
Type: String
Valid Values: `AWS/Rekognition/DetectModerationLabels/Image/V3 | AWS/Textract/AnalyzeDocument/Forms/V1`
Required: Yes

## See Also
<a name="API_HumanLoopRequestSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/HumanLoopRequestSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/HumanLoopRequestSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/HumanLoopRequestSource)
