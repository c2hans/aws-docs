---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/aws-apis.html
---

# AWS APIs
<a name="aws-apis"></a>

As detailed in the [prerequisites](prerequisites.md#verify-your-vpc-configuration), if you are deploying the solution to an existing VPC, the following services must be accessible from your private subnets.

## API Gateway
<a name="api-gateway"></a>
+  [GetAuthorizers](https://docs.aws.amazon.com/apigateway/latest/api/API_GetAuthorizers.html)
+  [GetIntegration](https://docs.aws.amazon.com/apigateway/latest/api/API_GetIntegration.html)
+  [GetMethod](https://docs.aws.amazon.com/apigateway/latest/api/API_GetMethod.html)
+  [GetResources](https://docs.aws.amazon.com/apigateway/latest/api/API_GetResources.html)
+  [GetRestApis](https://docs.aws.amazon.com/apigateway/latest/api/API_GetRestApis.html)

## Amazon Bedrock
<a name="bedrock"></a>
+  [GetAgent](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html)
+  [GetCustomModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetCustomModel.html)
+  [GetDataSource](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetDataSource.html)
+  [GetInferenceProfile](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetInferenceProfile.html)
+  [GetImportedModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetImportedModel.html)
+  [GetKnowledgeBase](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetKnowledgeBase.html)
+  [ListAgentVersions](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListAgentVersions.html)
+  [ListFoundationModels](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListFoundationModels.html)

## Amazon Cognito
<a name="cognito"></a>
+  [DescribeUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserPool.html)

## AWS Config
<a name="config"></a>
+  [BatchGetAggregateResourceConfig](https://docs.aws.amazon.com/config/latest/APIReference/API_BatchGetAggregateResourceConfig.html)
+  [DescribeConfigurationAggregators](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationAggregators.html)
+  [ListAggregateDiscoveredResources](https://docs.aws.amazon.com/config/latest/APIReference/API_ListAggregateDiscoveredResources.html)
+  [SelectAggregateResourceConfig](https://docs.aws.amazon.com/config/latest/APIReference/API_SelectAggregateResourceConfig.html)

## DynamoDB Streams
<a name="dynamodb-streams"></a>
+  [DescribeStream](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_DescribeStream.html)

## Amazon EC2
<a name="amazon-ec2"></a>
+  [DescribeInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html)
+  [DescribeSpotFleetRequests](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotFleetRequests.html)
+  [DescribeSpotInstanceRequests](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotInstanceRequests.html)
+  [DescribeTransitGatewayAttachments](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayAttachments.html)

## Amazon Elastic Load Balancer
<a name="amazon-elastic-load-balancer"></a>
+  [DescribeLoadBalancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html)
+  [DescribeListeners](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeListeners.html)
+  [DescribeTargetGroups](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html)
+  [DescribeTargetHealth](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetHealth.html)

## Amazon Elastic Kubernetes Service
<a name="amazon-elastic-kubernetes-service"></a>
+  [DescribeNodegroup](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeNodegroup.html)
+  [ListNodegroups](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListNodegroups.html)

## AWS Glue
<a name="glue"></a>
+  [BatchGetCrawlers](https://docs.aws.amazon.com/glue/latest/webapi/API_BatchGetCrawlers.html)
+  [GetConnections](https://docs.aws.amazon.com/glue/latest/webapi/API_GetConnections.html)
+  [GetDatabases](https://docs.aws.amazon.com/glue/latest/webapi/API_GetDatabases.html)
+  [GetTables](https://docs.aws.amazon.com/glue/latest/webapi/API_GetTables.html)

## IAM
<a name="iam"></a>
+  [GetAccountAuthorizationDetails](https://docs.aws.amazon.com/IAM/latest/APIReference/API_Operations.html)
+  [ListPolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListPolicies.html)

## AWS Lambda
<a name="lambda"></a>
+  [GetFunction](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunction.html)
+  [GetFunctionConfiguration](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionConfiguration.html)
+  [ListEventSourceMappings](https://docs.aws.amazon.com/lambda/latest/dg/API_ListEventSourceMappings.html)

## Amazon OpenSearch Service
<a name="opensearch-service"></a>
+  [DescribeDomains](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomains.html)
+  [ListDomainNames](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListDomainNames.html)

## Amazon OpenSearch Serverless
<a name="opensearch-serverless"></a>
+  [BatchGetCollection](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_BatchGetCollection.html)

## AWS Organizations
<a name="organizations"></a>
+  [ListAccounts](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccounts.html)
+  [ListAccountsForParent](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccountsForParent.html)
+  [ListOrganizationalUnitsForParent](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListOrganizationalUnitsForParent.html)
+  [ListRoots](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListRoots.html)

## Amazon Simple Notification Service
<a name="amazon-simple-notification-service"></a>
+  [ListSubscriptions](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListSubscriptions.html)

## Amazon Security Token Service
<a name="amazon-security-token-service"></a>
+  [AssumeRole](https://docs.aws.amazon.com/organizations/latest/APIReference/API_AssumeRole.html)
