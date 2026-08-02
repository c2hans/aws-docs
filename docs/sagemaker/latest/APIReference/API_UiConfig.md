---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UiConfig.html
---

# UiConfig
<a name="API_UiConfig"></a>

Provided configuration information for the worker UI for a labeling job. Provide either `HumanTaskUiArn` or `UiTemplateS3Uri`.

For named entity recognition, 3D point cloud and video frame labeling jobs, use `HumanTaskUiArn`.

For all other Ground Truth built-in task types and custom task types, use `UiTemplateS3Uri` to specify the location of a worker task template in Amazon S3.

## Contents
<a name="API_UiConfig_Contents"></a>

 ** HumanTaskUiArn **   <a name="sagemaker-Type-UiConfig-HumanTaskUiArn"></a>
The ARN of the worker task template used to render the worker UI and tools for labeling job tasks.
Use this parameter when you are creating a labeling job for named entity recognition, 3D point cloud and video frame labeling jobs. Use your labeling job task type to select one of the following ARNs and use it with this parameter when you create a labeling job. Replace `aws-region` with the AWS Region you are creating your labeling job in. For example, replace `aws-region` with `us-west-1` if you create a labeling job in US West (N. California).
 **Named Entity Recognition**
Use the following `HumanTaskUiArn` for named entity recognition labeling jobs:
 `arn:aws:sagemaker:aws-region:394669845002:human-task-ui/NamedEntityRecognition`
 **3D Point Cloud HumanTaskUiArns**
Use this `HumanTaskUiArn` for 3D point cloud object detection and 3D point cloud object detection adjustment labeling jobs.
+  `arn:aws:sagemaker:aws-region:394669845002:human-task-ui/PointCloudObjectDetection`
 Use this `HumanTaskUiArn` for 3D point cloud object tracking and 3D point cloud object tracking adjustment labeling jobs.
+  `arn:aws:sagemaker:aws-region:394669845002:human-task-ui/PointCloudObjectTracking`
 Use this `HumanTaskUiArn` for 3D point cloud semantic segmentation and 3D point cloud semantic segmentation adjustment labeling jobs.
+  `arn:aws:sagemaker:aws-region:394669845002:human-task-ui/PointCloudSemanticSegmentation`
 **Video Frame HumanTaskUiArns**
Use this `HumanTaskUiArn` for video frame object detection and video frame object detection adjustment labeling jobs.
+  `arn:aws:sagemaker:region:394669845002:human-task-ui/VideoObjectDetection`
 Use this `HumanTaskUiArn` for video frame object tracking and video frame object tracking adjustment labeling jobs.
+  `arn:aws:sagemaker:aws-region:394669845002:human-task-ui/VideoObjectTracking`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]+:[0-9]{12}:human-task-ui/.*`
Required: No

 ** UiTemplateS3Uri **   <a name="sagemaker-Type-UiConfig-UiTemplateS3Uri"></a>
The Amazon S3 bucket location of the UI template, or worker task template. This is the template used to render the worker UI and tools for labeling job tasks. For more information about the contents of a UI template, see [ Creating Your Custom Labeling Task Template](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-custom-templates-step2.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

## See Also
<a name="API_UiConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UiConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UiConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UiConfig)
