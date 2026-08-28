---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/AppComponent.html
---

# Managing Application Components
<a name="AppComponent"></a>

An Application Component (AppComponent) is a group of related AWS resources that work and fail as a single unit. For example, if you have a primary and replica database, both the databases belong to the same AppComponent. AWS Resilience Hub has rules that govern which AWS resources can belong to which AppComponent type. For example, a `DBInstance` can belong to `AWS::ResilienceHub::DatabaseAppComponent` and not to `AWS::ResilienceHub::ComputeAppComponent`.

The AWS Resilience Hub AppComponents support the following resources:
+ `AWS::ResilienceHub::ComputeAppComponent`
  + `AWS::ApiGateway::RestApi`
  + `AWS::ApiGatewayV2::Api`
  + `AWS::AutoScaling::AutoScalingGroup`
  + `AWS::EC2::Instance`
  + `AWS::ECS::Service`
  + `AWS::EKS::Deployment`
  + `AWS::EKS::ReplicaSet`
  + `AWS::EKS::Pod`
  + `AWS::Lambda::Function`
  + `AWS::StepFunctions::StateMachine`
+ `AWS::ResilienceHub::DatabaseAppComponent`
  + `AWS::DocDB::DBCluster`
  + `AWS::DynamoDB::Table`
  + `AWS::ElastiCache::CacheCluster`
  + `AWS::ElastiCache::GlobalReplicationGroup`
  + `AWS::ElastiCache::ReplicationGroup`
  + `AWS::ElastiCache::ServerlessCache`
  + `AWS::RDS::DBCluster`
  + `AWS::RDS::DBInstance`
+ `AWS::ResilienceHub::NetworkingAppComponent`
  + `AWS::EC2::NatGateway`
  + `AWS::ElasticLoadBalancing::LoadBalancer`
  + `AWS::ElasticLoadBalancingV2::LoadBalancer`
  + `AWS::Route53::RecordSet`
+ `AWS:ResilienceHub::NotificationAppComponent`
  + `AWS::SNS::Topic`
+ `AWS::ResilienceHub::QueueAppComponent`
  + `AWS::SQS::Queue`
+ `AWS::ResilienceHub::StorageAppComponent`
  + `AWS::Backup::BackupPlan`
  + `AWS::EC2::Volume`
  + `AWS::EFS::FileSystem`
  + `AWS::FSx::FileSystem`
**Note**
Currently, AWS Resilience Hub supports Amazon FSx for Windows File Server only.
  + `AWS::S3::Bucket`

**Topics**
+ [Grouping resources in an Application Component](AppComponent.grouping.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
