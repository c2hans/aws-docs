---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-trafficpolicyinstance.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53::TrafficPolicyInstance
<a name="aws-resource-route53-trafficpolicyinstance"></a>

A complex type that contains settings for the new traffic policy instance.

## Syntax
<a name="aws-resource-route53-trafficpolicyinstance-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-route53-trafficpolicyinstance-syntax.json"></a>

```
{
  "Type" : "AWS::Route53::TrafficPolicyInstance",
  "Properties" : {
      "[HostedZoneId](#cfn-route53-trafficpolicyinstance-hostedzoneid)" : {{String}},
      "[Name](#cfn-route53-trafficpolicyinstance-name)" : {{String}},
      "[TrafficPolicyId](#cfn-route53-trafficpolicyinstance-trafficpolicyid)" : {{String}},
      "[TrafficPolicyVersion](#cfn-route53-trafficpolicyinstance-trafficpolicyversion)" : {{Integer}},
      "[TTL](#cfn-route53-trafficpolicyinstance-ttl)" : {{Integer}}
    }
}
```

### YAML
<a name="aws-resource-route53-trafficpolicyinstance-syntax.yaml"></a>

```
Type: AWS::Route53::TrafficPolicyInstance
Properties:
  [HostedZoneId](#cfn-route53-trafficpolicyinstance-hostedzoneid): {{String}}
  [Name](#cfn-route53-trafficpolicyinstance-name): {{String}}
  [TrafficPolicyId](#cfn-route53-trafficpolicyinstance-trafficpolicyid): {{String}}
  [TrafficPolicyVersion](#cfn-route53-trafficpolicyinstance-trafficpolicyversion): {{Integer}}
  [TTL](#cfn-route53-trafficpolicyinstance-ttl): {{Integer}}
```

## Properties
<a name="aws-resource-route53-trafficpolicyinstance-properties"></a>

`HostedZoneId`  <a name="cfn-route53-trafficpolicyinstance-hostedzoneid"></a>
The ID of the hosted zone that Amazon Route 53 created resource record sets in.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Z0-9]{1,32}$`
*Maximum*: `32`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-route53-trafficpolicyinstance-name"></a>
The DNS name, such as www.example.com, for which Amazon Route 53 responds to queries by using the resource record sets that are associated with this traffic policy instance.
*Required*: Yes
*Type*: String
*Pattern*: `^[^A-Z\s]+\.$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrafficPolicyId`  <a name="cfn-route53-trafficpolicyinstance-trafficpolicyid"></a>
The ID of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-f-]{1,36}$`
*Minimum*: `1`
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrafficPolicyVersion`  <a name="cfn-route53-trafficpolicyinstance-trafficpolicyversion"></a>
The version of the traffic policy that Amazon Route 53 used to create resource record sets in the specified hosted zone.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TTL`  <a name="cfn-route53-trafficpolicyinstance-ttl"></a>
The TTL that Amazon Route 53 assigned to all of the resource record sets that it created in the specified hosted zone.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-route53-trafficpolicyinstance-return-values"></a>

### Ref
<a name="aws-resource-route53-trafficpolicyinstance-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-route53-trafficpolicyinstance-return-values-fn--getatt"></a>

####
<a name="aws-resource-route53-trafficpolicyinstance-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`Id`  <a name="Id-fn::getatt"></a>
The ID that Amazon Route 53 assigned to the new traffic policy instance.

`State`  <a name="State-fn::getatt"></a>
The value of `State` is one of the following values:
Applied
Amazon Route 53 has finished creating resource record sets, and changes have propagated to all Route 53 edge locations.
Creating
Route 53 is creating the resource record sets. Use `GetTrafficPolicyInstance` to confirm that the `CreateTrafficPolicyInstance` request completed successfully.
Failed
Route 53 wasn't able to create or update the resource record sets. When the value of `State` is `Failed`, see `Message` for an explanation of what caused the request to fail.

`TrafficPolicyType`  <a name="TrafficPolicyType-fn::getatt"></a>
The DNS type that Amazon Route 53 assigned to all of the resource record sets that it created for this traffic policy instance.
