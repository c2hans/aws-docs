---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-workforce.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Workforce
<a name="aws-resource-sagemaker-workforce"></a>

A single private workforce, which is automatically created when you create your first private work team. You can create one private work force in each AWS Region. By default, any workforce-related API operation used in a specific region will apply to the workforce created in that region. To learn how to create a private workforce, see [Create a Private Workforce](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-create-private.html).

## Syntax
<a name="aws-resource-sagemaker-workforce-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-workforce-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::Workforce",
  "Properties" : {
      "[CognitoConfig](#cfn-sagemaker-workforce-cognitoconfig)" : {{CognitoConfig}},
      "[IpAddressType](#cfn-sagemaker-workforce-ipaddresstype)" : {{String}},
      "[OidcConfig](#cfn-sagemaker-workforce-oidcconfig)" : {{OidcConfig}},
      "[SourceIpConfig](#cfn-sagemaker-workforce-sourceipconfig)" : {{SourceIpConfig}},
      "[Tags](#cfn-sagemaker-workforce-tags)" : {{[ Tag, ... ]}},
      "[WorkforceName](#cfn-sagemaker-workforce-workforcename)" : {{String}},
      "[WorkforceVpcConfig](#cfn-sagemaker-workforce-workforcevpcconfig)" : {{WorkforceVpcConfigRequest}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-workforce-syntax.yaml"></a>

```
Type: AWS::SageMaker::Workforce
Properties:
  [CognitoConfig](#cfn-sagemaker-workforce-cognitoconfig): {{
    CognitoConfig}}
  [IpAddressType](#cfn-sagemaker-workforce-ipaddresstype): {{String}}
  [OidcConfig](#cfn-sagemaker-workforce-oidcconfig): {{
    OidcConfig}}
  [SourceIpConfig](#cfn-sagemaker-workforce-sourceipconfig): {{
    SourceIpConfig}}
  [Tags](#cfn-sagemaker-workforce-tags): {{
    - Tag}}
  [WorkforceName](#cfn-sagemaker-workforce-workforcename): {{String}}
  [WorkforceVpcConfig](#cfn-sagemaker-workforce-workforcevpcconfig): {{
    WorkforceVpcConfigRequest}}
```

## Properties
<a name="aws-resource-sagemaker-workforce-properties"></a>

`CognitoConfig`  <a name="cfn-sagemaker-workforce-cognitoconfig"></a>
The configuration of an Amazon Cognito workforce. A single Cognito workforce is created using and corresponds to a single [ Amazon Cognito user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html).
*Required*: No
*Type*: [CognitoConfig](aws-properties-sagemaker-workforce-cognitoconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IpAddressType`  <a name="cfn-sagemaker-workforce-ipaddresstype"></a>
The IP address type you specify - either `IPv4` only or `dualstack` (`IPv4` and `IPv6`) - to support your labeling workforce.
*Required*: No
*Type*: String
*Allowed values*: `ipv4 | dualstack`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OidcConfig`  <a name="cfn-sagemaker-workforce-oidcconfig"></a>
The configuration of an OIDC Identity Provider (IdP) private workforce.
*Required*: No
*Type*: [OidcConfig](aws-properties-sagemaker-workforce-oidcconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceIpConfig`  <a name="cfn-sagemaker-workforce-sourceipconfig"></a>
A list of one to ten IP address ranges ([CIDRs](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html)) to be added to the workforce allow list. By default, a workforce isn't restricted to specific IP addresses.
*Required*: No
*Type*: [SourceIpConfig](aws-properties-sagemaker-workforce-sourceipconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-sagemaker-workforce-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-workforce-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkforceName`  <a name="cfn-sagemaker-workforce-workforcename"></a>
The name of the private workforce.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]([a-zA-Z0-9\-]){0,62}$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WorkforceVpcConfig`  <a name="cfn-sagemaker-workforce-workforcevpcconfig"></a>
The configuration of a VPC workforce.
*Required*: No
*Type*: [WorkforceVpcConfigRequest](aws-properties-sagemaker-workforce-workforcevpcconfigrequest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-sagemaker-workforce-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-workforce-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-workforce-return-values-fn--getatt"></a>

####
<a name="aws-resource-sagemaker-workforce-return-values-fn--getatt-fn--getatt"></a>

`SubDomain`  <a name="SubDomain-fn::getatt"></a>
The subdomain for your OIDC Identity Provider.

`WorkforceArn`  <a name="WorkforceArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the private workforce.
