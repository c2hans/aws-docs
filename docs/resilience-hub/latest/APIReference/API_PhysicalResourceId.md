---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_PhysicalResourceId.html
---

# PhysicalResourceId
<a name="API_PhysicalResourceId"></a>

Defines a physical resource identifier.

## Contents
<a name="API_PhysicalResourceId_Contents"></a>

 ** identifier **   <a name="resiliencehub-Type-PhysicalResourceId-identifier"></a>
Identifier of the physical resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** type **   <a name="resiliencehub-Type-PhysicalResourceId-type"></a>
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
Type: String
Valid Values: `Arn | Native`
Required: Yes

 ** awsAccountId **   <a name="resiliencehub-Type-PhysicalResourceId-awsAccountId"></a>
The AWS account that owns the physical resource.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** awsRegion **   <a name="resiliencehub-Type-PhysicalResourceId-awsRegion"></a>
The AWS Region that the physical resource is located in.
Type: String
Pattern: `[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]`
Required: No

## See Also
<a name="API_PhysicalResourceId_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/PhysicalResourceId)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/PhysicalResourceId)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/PhysicalResourceId)
