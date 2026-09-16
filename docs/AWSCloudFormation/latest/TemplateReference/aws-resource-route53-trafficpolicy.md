---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-trafficpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53::TrafficPolicy
<a name="aws-resource-route53-trafficpolicy"></a>

A complex type that contains settings for a traffic policy.

## Syntax
<a name="aws-resource-route53-trafficpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-route53-trafficpolicy-syntax.json"></a>

```
{
  "Type" : "AWS::Route53::TrafficPolicy",
  "Properties" : {
      "[Comment](#cfn-route53-trafficpolicy-comment)" : {{String}},
      "[Document](#cfn-route53-trafficpolicy-document)" : {{String}},
      "[Name](#cfn-route53-trafficpolicy-name)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-route53-trafficpolicy-syntax.yaml"></a>

```
Type: AWS::Route53::TrafficPolicy
Properties:
  [Comment](#cfn-route53-trafficpolicy-comment): {{String}}
  [Document](#cfn-route53-trafficpolicy-document): {{String}}
  [Name](#cfn-route53-trafficpolicy-name): {{String}}
```

## Properties
<a name="aws-resource-route53-trafficpolicy-properties"></a>

`Comment`  <a name="cfn-route53-trafficpolicy-comment"></a>
The comment that you specify in the `CreateTrafficPolicy` request, if any.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Document`  <a name="cfn-route53-trafficpolicy-document"></a>
The definition of a traffic policy in JSON format. You specify the JSON document to use for a new traffic policy in the `CreateTrafficPolicy` request. For more information about the JSON format, see [Traffic Policy Document Format](https://docs.aws.amazon.com/Route53/latest/APIReference/api-policies-traffic-policy-document-format.html).
*Required*: Yes
*Type*: String
*Maximum*: `102400`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-route53-trafficpolicy-name"></a>
The name that you specified when you created the traffic policy.
*Required*: Yes
*Type*: String
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-route53-trafficpolicy-return-values"></a>

### Ref
<a name="aws-resource-route53-trafficpolicy-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-route53-trafficpolicy-return-values-fn--getatt"></a>

####
<a name="aws-resource-route53-trafficpolicy-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`Id`  <a name="Id-fn::getatt"></a>
The ID that Amazon Route 53 assigned to a traffic policy when you created it.

`Type`  <a name="Type-fn::getatt"></a>
The DNS type of the resource record sets that Amazon Route 53 creates when you use a traffic policy to create a traffic policy instance.

`Version`  <a name="Version-fn::getatt"></a>
The version number that Amazon Route 53 assigns to a traffic policy. For a new traffic policy, the value of `Version` is always 1.
