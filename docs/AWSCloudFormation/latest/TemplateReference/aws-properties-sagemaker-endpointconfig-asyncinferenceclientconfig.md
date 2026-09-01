---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-endpointconfig-asyncinferenceclientconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::EndpointConfig AsyncInferenceClientConfig
<a name="aws-properties-sagemaker-endpointconfig-asyncinferenceclientconfig"></a>

Configures the behavior of the client used by SageMaker to interact with the model container during asynchronous inference.

## Syntax
<a name="aws-properties-sagemaker-endpointconfig-asyncinferenceclientconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-endpointconfig-asyncinferenceclientconfig-syntax.json"></a>

```
{
  "[MaxConcurrentInvocationsPerInstance](#cfn-sagemaker-endpointconfig-asyncinferenceclientconfig-maxconcurrentinvocationsperinstance)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-endpointconfig-asyncinferenceclientconfig-syntax.yaml"></a>

```
  [MaxConcurrentInvocationsPerInstance](#cfn-sagemaker-endpointconfig-asyncinferenceclientconfig-maxconcurrentinvocationsperinstance): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-endpointconfig-asyncinferenceclientconfig-properties"></a>

`MaxConcurrentInvocationsPerInstance`  <a name="cfn-sagemaker-endpointconfig-asyncinferenceclientconfig-maxconcurrentinvocationsperinstance"></a>
The maximum number of concurrent requests sent by the SageMaker client to the model container. If no value is provided, SageMaker will choose an optimal value for you.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
