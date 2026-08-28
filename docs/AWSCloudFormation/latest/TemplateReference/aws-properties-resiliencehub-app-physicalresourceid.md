---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resiliencehub-app-physicalresourceid.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHub::App PhysicalResourceId
<a name="aws-properties-resiliencehub-app-physicalresourceid"></a>

Defines a physical resource identifier.

## Syntax
<a name="aws-properties-resiliencehub-app-physicalresourceid-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resiliencehub-app-physicalresourceid-syntax.json"></a>

```
{
  "[AwsAccountId](#cfn-resiliencehub-app-physicalresourceid-awsaccountid)" : {{String}},
  "[AwsRegion](#cfn-resiliencehub-app-physicalresourceid-awsregion)" : {{String}},
  "[Identifier](#cfn-resiliencehub-app-physicalresourceid-identifier)" : {{String}},
  "[Type](#cfn-resiliencehub-app-physicalresourceid-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-resiliencehub-app-physicalresourceid-syntax.yaml"></a>

```
  [AwsAccountId](#cfn-resiliencehub-app-physicalresourceid-awsaccountid): {{String}}
  [AwsRegion](#cfn-resiliencehub-app-physicalresourceid-awsregion): {{String}}
  [Identifier](#cfn-resiliencehub-app-physicalresourceid-identifier): {{String}}
  [Type](#cfn-resiliencehub-app-physicalresourceid-type): {{String}}
```

## Properties
<a name="aws-properties-resiliencehub-app-physicalresourceid-properties"></a>

`AwsAccountId`  <a name="cfn-resiliencehub-app-physicalresourceid-awsaccountid"></a>
The AWS account that owns the physical resource.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AwsRegion`  <a name="cfn-resiliencehub-app-physicalresourceid-awsregion"></a>
The AWS Region that the physical resource is located in.
*Required*: No
*Type*: String
*Pattern*: `^[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Identifier`  <a name="cfn-resiliencehub-app-physicalresourceid-identifier"></a>
Identifier of the physical resource.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-resiliencehub-app-physicalresourceid-type"></a>
Specifies the type of physical resource identifier.
Arn
The resource identifier is an Amazon Resource Name (ARN) and it can identify the following list of resources:
+  `AWS::ECS::Service`
+  `AWS::EFS::FileSystem`
+  `AWS::ElasticLoadBalancingV2::LoadBalancer`
+  `AWS::Lambda::Function`
+  `AWS::SNS::Topic`
Native
The resource identifier is an AWS Resilience Hub-native identifier and it can identify the following list of resources:
+  `AWS::ApiGateway::RestApi`
+  `AWS::ApiGatewayV2::Api`
+  `AWS::AutoScaling::AutoScalingGroup`
+  `AWS::DocDB::DBCluster`
+  `AWS::DocDB::DBGlobalCluster`
+  `AWS::DocDB::DBInstance`
+  `AWS::DynamoDB::GlobalTable`
+  `AWS::DynamoDB::Table`
+  `AWS::EC2::EC2Fleet`
+  `AWS::EC2::Instance`
+  `AWS::EC2::NatGateway`
+  `AWS::EC2::Volume`
+  `AWS::ElasticLoadBalancing::LoadBalancer`
+  `AWS::RDS::DBCluster`
+  `AWS::RDS::DBInstance`
+  `AWS::RDS::GlobalCluster`
+  `AWS::Route53::RecordSet`
+  `AWS::S3::Bucket`
+  `AWS::SQS::Queue`
*Required*: Yes
*Type*: String
*Pattern*: `Arn|Native`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
