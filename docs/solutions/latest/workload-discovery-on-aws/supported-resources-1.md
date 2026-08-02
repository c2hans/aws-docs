---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/supported-resources-1.html
---

# Supported resources
<a name="supported-resources-1"></a>

The solution supports all the resource types that AWS Config supports, as listed [here](https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html). The following table contains the supported resources that Workload Discovery on AWS discovers that aren’t supported by AWS Config. Details are provided in the corresponding AWS documentation listing.

| Resource type | Source | Description |
| --- | --- | --- |
| AWS::ApiGateway::Method | SDK |  [getMethod](https://docs.aws.amazon.com/apigateway/latest/api/API_GetMethod.html)  |
| AWS::ApiGateway::Resource | SDK |  [getResource](https://docs.aws.amazon.com/apigateway/latest/api/API_GetResources.html)  |
| AWS::APIGateway::Authorizer | SDK |  [getAuthorizers](https://docs.aws.amazon.com/apigateway/latest/api/API_GetAuthorizers.html)  |
| AWS::Bedrock::Agent | SDK |  [GetAgent](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html)  |
| AWS::Bedrock::AgentVersion | SDK |  [ListAgentVersions](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListAgentVersions.html)  |
| AWS::Bedrock::CustomModel | SDK |  [GetCustomModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetCustomModel.html)  |
| AWS::Bedrock::DataSource | SDK |  [GetDataSource](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetDataSource.html)  |
| AWS::Bedrock::FoundationModel | SDK |  [ListFoundationModels](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListFoundationModels.html)  |
| AWS::Bedrock::ImportedModel | SDK |  [GetImportedModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetImportedModel.html)  |
| AWS::Bedrock::InferenceProfile | SDK |  [GetInferenceProfile](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetInferenceProfile.html)  |
| AWS::Bedrock::KnowledgeBase | SDK |  [GetKnowledgeBase](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetKnowledgeBase.html)  |
| AWS::DynamoDB::Stream | SDK |  [describeStream](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_DescribeStream.html)  |
| AWS::EC2::Spot | SDK |  [describeSpotInstanceRequests](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotInstanceRequests.html)  |
| AWS::EC2::SpotFleet | SDK |  [describeSpotFleetRequests](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotFleetRequests.html)  |
| AWS::ECS::Task | SDK |  [describe-tasks](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTasks.html)  |
| AWS::EKS::Nodegroup | SDK |  [describeNodegroup](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeNodegroup.html)  |
| AWS::ElasticLoadBalancingV2::TargetGroup | SDK |  [describeTargetGroups](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html)  |
| AWS::Glue::Connection | SDK |  [GetConnections](https://docs.aws.amazon.com/glue/latest/webapi/API_GetConnections.html)  |
| AWS::Glue::Crawler | SDK |  [BatchGetCrawlers](https://docs.aws.amazon.com/glue/latest/webapi/API_BatchGetCrawlers.html)  |
| AWS::Glue::Database | SDK |  [GetDatabases](https://docs.aws.amazon.com/glue/latest/webapi/API_GetDatabases.html)  |
| AWS::Glue::Tables | SDK |  [GetTables](https://docs.aws.amazon.com/glue/latest/webapi/API_GetTables.html)  |
| AWS::IAM::AWSManagedPolicy | SDK |  [getAccountAuthorizationDetails](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountAuthorizationDetails.html)  |
| AWS::OpenSearchServerless::Collection | SDK |  [BatchGetCollection](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_BatchGetCollection.html)  |
