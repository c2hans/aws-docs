---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferencecomponent-inferencecomponentstartupparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceComponent InferenceComponentStartupParameters
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentstartupparameters"></a>

Settings that take effect while the model container starts up.

## Syntax
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentstartupparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentstartupparameters-syntax.json"></a>

```
{
  "[ContainerStartupHealthCheckTimeoutInSeconds](#cfn-sagemaker-inferencecomponent-inferencecomponentstartupparameters-containerstartuphealthchecktimeoutinseconds)" : {{Integer}},
  "[ModelDataDownloadTimeoutInSeconds](#cfn-sagemaker-inferencecomponent-inferencecomponentstartupparameters-modeldatadownloadtimeoutinseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentstartupparameters-syntax.yaml"></a>

```
  [ContainerStartupHealthCheckTimeoutInSeconds](#cfn-sagemaker-inferencecomponent-inferencecomponentstartupparameters-containerstartuphealthchecktimeoutinseconds): {{Integer}}
  [ModelDataDownloadTimeoutInSeconds](#cfn-sagemaker-inferencecomponent-inferencecomponentstartupparameters-modeldatadownloadtimeoutinseconds): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentstartupparameters-properties"></a>

`ContainerStartupHealthCheckTimeoutInSeconds`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentstartupparameters-containerstartuphealthchecktimeoutinseconds"></a>
The timeout value, in seconds, for your inference container to pass health check by Amazon S3 Hosting. For more information about health check, see [How Your Container Should Respond to Health Check (Ping) Requests](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html#your-algorithms-inference-algo-ping-requests).
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `3600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelDataDownloadTimeoutInSeconds`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentstartupparameters-modeldatadownloadtimeoutinseconds"></a>
The timeout value, in seconds, to download and extract the model that you want to host from Amazon S3 to the individual inference instance associated with this inference component.
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `3600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
