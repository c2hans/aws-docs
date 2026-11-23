---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-endpointpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::EndpointPolicy

Attaches a resource-based policy to an endpoint. With an endpoint policy, you can allow other AWS accounts to send requests to your endpoint, or to inference components on it, through an inference router. The policy that you specify replaces the endpoint's existing policy, if it has one.

You can't attach a policy to an endpoint whose status is `Deleting` or `Failed`. SageMaker AI rejects a policy that doesn't follow the endpoint policy rules. For information about the policy rules, see [Use destinations in other accounts](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-router-cross-account.html).

Policy changes typically take effect within 30 seconds, and can take up to 5 minutes. If you delete the endpoint, its policy is also deleted, and a new endpoint with the same name has no policy.

## Syntax
<a name="aws-resource-sagemaker-endpointpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-endpointpolicy-syntax.json"></a>

```json
{
  "Type" : "AWS::SageMaker::EndpointPolicy",
  "Properties" : {
      "[EndpointArn](#cfn-sagemaker-endpointpolicy-endpointarn)" : {{String}},
      "[PolicyDocument](#cfn-sagemaker-endpointpolicy-policydocument)" : {{Json}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-endpointpolicy-syntax.yaml"></a>

```yaml
Type: AWS::SageMaker::EndpointPolicy
Properties:
  [EndpointArn](#cfn-sagemaker-endpointpolicy-endpointarn): {{String}}
  [PolicyDocument](#cfn-sagemaker-endpointpolicy-policydocument): {{Json}}
```

## Properties
<a name="aws-resource-sagemaker-endpointpolicy-properties"></a>

`EndpointArn`  <a name="cfn-sagemaker-endpointpolicy-endpointarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:endpoint/`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PolicyDocument`  <a name="cfn-sagemaker-endpointpolicy-policydocument"></a>
Property description not available.
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-sagemaker-endpointpolicy-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-endpointpolicy-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-endpointpolicy-return-values-fn--getatt"></a>

####
<a name="aws-resource-sagemaker-endpointpolicy-return-values-fn--getatt-fn--getatt"></a>

`EndpointName`  <a name="EndpointName-fn::getatt"></a>
Property description not available.
