---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-shield-protection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Shield::Protection
<a name="aws-resource-shield-protection"></a>

Enables AWS Shield Advanced for a specific AWS resource. The resource can be an Amazon CloudFront distribution, Amazon Route 53 hosted zone, AWS Global Accelerator standard accelerator, Elastic IP Address, Application Load Balancer, or a Classic Load Balancer. You can protect Amazon EC2 instances and Network Load Balancers by association with protected Amazon EC2 Elastic IP addresses.

 **Configure a single `AWS::Shield::Protection`**

Use this protection to protect a single resource at a time.

To configure this Shield Advanced protection through CloudFormation, you must be subscribed to Shield Advanced. You can subscribe through the [Shield Advanced console](https://console.aws.amazon.com/wafv2/shieldv2#/) and through the APIs. For more information, see [Subscribe to AWS Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/enable-ddos-prem.html).

See example templates for Shield Advanced in CloudFormation at [aws-samples/aws-shield-advanced-examples](https://github.com/aws-samples/aws-shield-advanced-examples).

 **Configure Shield Advanced using AWS CloudFormation and AWS Firewall Manager**

You might be able to use Firewall Manager with AWS CloudFormation to configure Shield Advanced across multiple accounts and protected resources. To do this, your accounts must be part of an organization in AWS Organizations. You can use Firewall Manager to configure Shield Advanced protections for any resource types except for Amazon Route 53 or AWS Global Accelerator.

For an example of this, see the one-click configuration guidance published by the AWS technical community at [One-click deployment of Shield Advanced](https://youtu.be/LCA3FwMk_QE).

 **Configure multiple protections through the Shield Advanced console**

You can add protection to multiple resources at once through the [Shield Advanced console](https://console.aws.amazon.com/wafv2/shieldv2#/). For more information see [Getting Started with AWS Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-ddos.html) and [Managing resource protections in AWS Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-manage-protected-resources.html).

## Syntax
<a name="aws-resource-shield-protection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-shield-protection-syntax.json"></a>

```
{
  "Type" : "AWS::Shield::Protection",
  "Properties" : {
      "[ApplicationLayerAutomaticResponseConfiguration](#cfn-shield-protection-applicationlayerautomaticresponseconfiguration)" : {{ApplicationLayerAutomaticResponseConfiguration}},
      "[HealthCheckArns](#cfn-shield-protection-healthcheckarns)" : {{[ String, ... ]}},
      "[Name](#cfn-shield-protection-name)" : {{String}},
      "[ResourceArn](#cfn-shield-protection-resourcearn)" : {{String}},
      "[Tags](#cfn-shield-protection-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-shield-protection-syntax.yaml"></a>

```
Type: AWS::Shield::Protection
Properties:
  [ApplicationLayerAutomaticResponseConfiguration](#cfn-shield-protection-applicationlayerautomaticresponseconfiguration): {{
    ApplicationLayerAutomaticResponseConfiguration}}
  [HealthCheckArns](#cfn-shield-protection-healthcheckarns): {{
    - String}}
  [Name](#cfn-shield-protection-name): {{String}}
  [ResourceArn](#cfn-shield-protection-resourcearn): {{String}}
  [Tags](#cfn-shield-protection-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-shield-protection-properties"></a>

`ApplicationLayerAutomaticResponseConfiguration`  <a name="cfn-shield-protection-applicationlayerautomaticresponseconfiguration"></a>
The automatic application layer DDoS mitigation settings for the protection. This configuration determines whether Shield Advanced automatically manages rules in the web ACL in order to respond to application layer events that Shield Advanced determines to be DDoS attacks.
If you use CloudFormation to manage the web ACLs that you use with Shield Advanced automatic mitigation, see the additional guidance about web ACL management in the `AWS::WAFv2::WebACL` resource description.
*Required*: No
*Type*: [ApplicationLayerAutomaticResponseConfiguration](aws-properties-shield-protection-applicationlayerautomaticresponseconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HealthCheckArns`  <a name="cfn-shield-protection-healthcheckarns"></a>
The ARN (Amazon Resource Name) of the health check to associate with the protection. Health-based detection provides improved responsiveness and accuracy in attack detection and mitigation.
You can use this option with any resource type except for Route 53 hosted zones.
For more information, see [Configuring health-based detection using health checks](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-health-checks.html) in the *AWS Shield Advanced Developer Guide*.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `2048 | 1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-shield-protection-name"></a>
The name of the protection. For example, `My CloudFront distributions`.
If you change the name of an existing protection, Shield Advanced deletes the protection and replaces it with a new one. While this is happening, the protection isn't available on the AWS resource.
*Required*: Yes
*Type*: String
*Pattern*: `[ a-zA-Z0-9_\.\-]*`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceArn`  <a name="cfn-shield-protection-resourcearn"></a>
The ARN (Amazon Resource Name) of the AWS resource that is protected.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-shield-protection-tags"></a>
Key:value pairs associated with an AWS resource. The key:value pair can be anything you define. Typically, the tag key represents a category (such as "environment") and the tag value represents a specific value within that category (such as "test," "development," or "production"). You can add up to 50 tags to each AWS resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-shield-protection-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-shield-protection-return-values"></a>

### Ref
<a name="aws-resource-shield-protection-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN (Amazon Resource Name) of the protection.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-shield-protection-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-shield-protection-return-values-fn--getatt-fn--getatt"></a>

`ProtectionArn`  <a name="ProtectionArn-fn::getatt"></a>
The ARN (Amazon Resource Name) of the new protection.

`ProtectionId`  <a name="ProtectionId-fn::getatt"></a>
The ID of the new protection.

## Examples
<a name="aws-resource-shield-protection--examples"></a>

**Topics**
+ [Create a network layer protection](#aws-resource-shield-protection--examples--Create_a_network_layer_protection)
+ [Create an application layer protection](#aws-resource-shield-protection--examples--Create_an_application_layer_protection)

### Create a network layer protection
<a name="aws-resource-shield-protection--examples--Create_a_network_layer_protection"></a>

The following shows an example protection configuration for an Amazon EC2 Elastic IP address.

#### YAML
<a name="aws-resource-shield-protection--examples--Create_a_network_layer_protection--yaml"></a>

```
Resources:
  EIP:
    Type: AWS::EC2::EIP
  Protection:
    Type: AWS::Shield::Protection
    Properties:
      Name: 'MyEIPProtection'
            ResourceArn: !Sub 'arn:${AWS::Partition}:ec2:${AWS::Region}:${AWS::AccountId}:eip-allocation/${EIP.AllocationId}'
```

#### JSON
<a name="aws-resource-shield-protection--examples--Create_a_network_layer_protection--json"></a>

```
{
    "Resources": {
        "EIP": {
            "Type": "AWS::EC2::EIP"
        },
        "Protection": {
            "Type": "AWS::Shield::Protection",
            "Properties": {
                "Name": "MyEIPProtection",
                "ResourceArn": {
                    "Fn::Sub": "arn:${AWS::Partition}:ec2:${AWS::Region}:${AWS::AccountId}:eip-allocation/${EIP.AllocationId}"
                }
            }
        }
    }
}
```

### Create an application layer protection
<a name="aws-resource-shield-protection--examples--Create_an_application_layer_protection"></a>

The following shows an example layer 7 protection configuration for an application load balancer. The protection includes a health check and has application layer automatic response enabled. The load balancer must be associated with an AWS WAF web ACL that has a rate-based rule defined in it.

#### YAML
<a name="aws-resource-shield-protection--examples--Create_an_application_layer_protection--yaml"></a>

```
Resources:
  # Create L7 Protection
  Protection:
    Type: AWS::Shield::Protection
    DependsOn:
    - WebACLAssociation
    Properties:
      Name: 'MyL7Protection'
      ResourceArn: !Ref ALB
      HealthCheckArns:
        - !Sub 'arn:${AWS::Partition}:route53:::healthcheck/${HealthCheck}'
      ApplicationLayerAutomaticResponseConfiguration:
        Status: ENABLED
        Action:
          Block: { }
```

#### JSON
<a name="aws-resource-shield-protection--examples--Create_an_application_layer_protection--json"></a>

```
{
    "Resources": {
        "Protection": {
            "Type": "AWS::Shield::Protection",
            "DependsOn": [
                "WebACLAssociation"
            ],
            "Properties": {
                "Name": "MyL7Protection",
                "ResourceArn": {
                    "Ref": "ALB"
                },
                "HealthCheckArns": [
                    {
                        "Fn::Sub": "arn:${AWS::Partition}:route53:::healthcheck/${HealthCheck}"
                    }
                ],
                "ApplicationLayerAutomaticResponseConfiguration": {
                    "Status": "ENABLED",
                    "Action": {
                        "Block": {}
                    }
                }
            }
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
