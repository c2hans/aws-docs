---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-endpointconfig-crossregiontrafficconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::EndpointConfig CrossRegionTrafficConfig

The cross-Region traffic cap for an endpoint. The cap limits the requests per second that the endpoint accepts from inference routers in other AWS Regions. The cap is `MaxCrossRegionPercentPerEndpoint` percent of `MaxInvocationsPerSecondPerInstance` multiplied by the number of `InService` instances, rounded up. All production variants and inference components of the endpoint share it. Requests that you send to the endpoint directly aren't counted. A request over the cap fails with a `ThrottlingException`.

## Syntax
<a name="aws-properties-sagemaker-endpointconfig-crossregiontrafficconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-endpointconfig-crossregiontrafficconfig-syntax.json"></a>

```json
{
  "[MaxCrossRegionPercentPerEndpoint](#cfn-sagemaker-endpointconfig-crossregiontrafficconfig-maxcrossregionpercentperendpoint)" : {{Integer}},
  "[MaxInvocationsPerSecondPerInstance](#cfn-sagemaker-endpointconfig-crossregiontrafficconfig-maxinvocationspersecondperinstance)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-endpointconfig-crossregiontrafficconfig-syntax.yaml"></a>

```yaml
  [MaxCrossRegionPercentPerEndpoint](#cfn-sagemaker-endpointconfig-crossregiontrafficconfig-maxcrossregionpercentperendpoint): {{Integer}}
  [MaxInvocationsPerSecondPerInstance](#cfn-sagemaker-endpointconfig-crossregiontrafficconfig-maxinvocationspersecondperinstance): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-endpointconfig-crossregiontrafficconfig-properties"></a>

`MaxCrossRegionPercentPerEndpoint`  <a name="cfn-sagemaker-endpointconfig-crossregiontrafficconfig-maxcrossregionpercentperendpoint"></a>
The percentage of the endpoint's capacity that requests from inference routers in other AWS Regions can use.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxInvocationsPerSecondPerInstance`  <a name="cfn-sagemaker-endpointconfig-crossregiontrafficconfig-maxinvocationspersecondperinstance"></a>
The number of invocations per second that you expect one `InService` instance to serve. One value applies to every production variant, whatever its instance type.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
