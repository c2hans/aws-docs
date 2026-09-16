---
source_url: https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/Welcome.html
---

# Welcome
<a name="Welcome"></a>

The AWS services in the following list support the Resource Groups Tagging API `TagResources` and `UntagResources` operations.

The `GetResources`, `GetTagKeys`, and `GetTagValues` operations support all resource types.

**Note**
This list includes only those AWS services that work with the Resource Groups Tagging API.
If an AWS service isn't listed below, you might still be able to tag that service's resources by using the service's native tagging operations instead of using the Resource Groups Tagging API operations. See the documentation for an individual service for information about that service's native tagging operations.
This lets you tag resources by using the AWS CLI version of the service's operation. For example, you could tag an IAM role by using a command similar to the following:
 `aws iam tag-role --role-name ProdAppRole --tags Key=CostCenter,Value=1234`
For a list of the AWS services that work with Tag Editor, see [Supported Resources](https://docs.aws.amazon.com/ARG/latest/userguide/supported-resources.html) in the * AWS Resource Groups User Guide*.
IAM users and roles can only be used in `TagResources` and `UntagResources` operations. The `GetResources` operation does not currently support IAM users and roles.
+  [AWS Amplify](https://docs.aws.amazon.com/amplify)
+  [AWS Amplify UI Builder](https://docs.aws.amazon.com/amplify)
+  [Amazon API Gateway](https://docs.aws.amazon.com/apigateway)
+  [Amazon Route 53 Application Recovery Controller](https://docs.aws.amazon.com/amazonarc)
+  [Recovery readiness in Amazon Route 53 Application Recovery Controller](https://docs.aws.amazon.com/recovery-readiness/latest/api/what-is-recovery-readiness.html)
+  [AWS AppConfig](https://docs.aws.amazon.com/appconfig)
+  [Amazon AppFlow](https://docs.aws.amazon.com/appflow)
+  [Amazon AppIntegrations](https://docs.aws.amazon.com/connect/latest/APIReference/Welcome.html#Welcome_Amazon_AppIntegrations_Service)
+  [AWS App Runner](https://docs.aws.amazon.com/apprunner)
+  [Amazon AppStream 2.0](https://docs.aws.amazon.com/appstream2)
+  [AWS AppSync](https://docs.aws.amazon.com/appsync)
+  [AWS App Mesh](https://docs.aws.amazon.com/app-mesh)
+  [Amazon Athena](https://docs.aws.amazon.com/athena)
+  [AWS Audit Manager](https://docs.aws.amazon.com/audit-manager)
+  [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide)
+  [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling)

  The `TagResources` and `UntagResources` operations of AWS Resource Groups Tagging API work as documented with Amazon EC2 Auto Scaling Groups. However, the `GetTagKeys`, `GetTagValues` and `GetResources` operations aren't supported at this time and return an empty response for this service.
+  [AWS B2B Data Interchange](https://docs.aws.amazon.com/b2bi/latest/userguide)
+  [AWS Backup](https://docs.aws.amazon.com/aws-backup)
+  [AWS Backup Gateway](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_Operations_AWS_Backup_Gateway.html)
+  [AWS Batch](https://docs.aws.amazon.com/batch)
+  [Amazon Bedrock](https://docs.aws.amazon.com/bedrock)
+  [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore)
+  [AWS Billing and Cost Management Data Exports](https://docs.aws.amazon.com/account-billing)
+  [AWS Billing and Cost Management Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-getting-started.html)
+  [Amazon Braket](https://docs.aws.amazon.com/braket)
+  [AWS Certificate Manager](https://docs.aws.amazon.com/acm)
+  [AWS Private Certificate Authority](https://docs.aws.amazon.com/acm)
+  [AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide)
+  [AWS Cloud9](https://docs.aws.amazon.com/cloud9)
+  [Amazon Cloud Directory](https://docs.aws.amazon.com/clouddirectory)
+  [AWS Cloud Map](https://docs.aws.amazon.com/cloud-map)
+  [AWS CloudFormation](https://docs.aws.amazon.com/cloudformation)
+  [Amazon CloudFront](https://docs.aws.amazon.com/cloudfront)
+  [AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm)
+  [AWS CloudTrail](https://docs.aws.amazon.com/cloudtrail)
+  [Amazon CloudWatch (alarms only)](https://docs.aws.amazon.com/cloudwatch)
+  [Amazon CloudWatch Events](https://docs.aws.amazon.com/cloudwatch/?id=docs_gateway#amazon-cloudwatch-events)
+  [Amazon CloudWatch Internet Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html)
+  [Amazon CloudWatch Logs](https://docs.aws.amazon.com/cloudwatch/?id=docs_gateway#amazon-cloudwatch-logs)
+  [Amazon CloudWatch Observability Access Manager](https://docs.aws.amazon.com/OAM/latest/APIReference/Welcome.html)
+  [Amazon CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html)
+  [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/cloudwatch)
+  [AWS CodeArtifact](https://docs.aws.amazon.com/codeartifact)
+  [AWS CodeBuild](https://docs.aws.amazon.com/codebuild)
+  [AWS CodeCommit](https://docs.aws.amazon.com/codecommit)
+  [AWS CodeConnections](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/)
+  [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy)
+  [Amazon CodeGuru Profiler](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/)
+  [Amazon CodeGuru Reviewer](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/)
+  [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline)
+  [AWS CodeStar](https://docs.aws.amazon.com/codestar)
+  [Amazon Cognito Identity](https://docs.aws.amazon.com/cognito)
+  [Amazon Cognito User Pools](https://docs.aws.amazon.com/cognito)
+  [Amazon Comprehend](https://docs.aws.amazon.com/comprehend)
+  [AWS Config](https://docs.aws.amazon.com/config)
+  [Amazon Connect](http://aws.amazon.com/connect/resources/?whats-new-cards#Documentation)
+  [Amazon Connect Campaigns](https://docs.aws.amazon.com/connect)
+  [Amazon Connect Customer Profiles](https://docs.aws.amazon.com/connect/latest/adminguide/customer-profiles.html)
+  [AWS Data Exchange](https://docs.aws.amazon.com/data-exchange)
+  [Amazon Data Lifecycle Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html)
+  [AWS Data Pipeline](https://docs.aws.amazon.com/data-pipeline)
+  [AWS Database Migration Service](https://docs.aws.amazon.com/dms)
+  [AWS DataSync](https://docs.aws.amazon.com/datasync)
+  [Amazon DataZone](https://docs.aws.amazon.com/datazone)
+  [AWS Deadline Cloud](https://docs.aws.amazon.com/deadline-cloud/latest/userguide)
+  [Amazon Detective](https://docs.aws.amazon.com/detective)
+  [AWS Device Farm](https://docs.aws.amazon.com/devicefarm)
+  [AWS Direct Connect](https://docs.aws.amazon.com/directconnect)
+  [AWS Directory Service](https://docs.aws.amazon.com/directory-service)
+  [Amazon DocumentDB Elastic Clusters](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-using-elastic-clusters.html)
+  [Amazon DynamoDB](https://docs.aws.amazon.com/dynamodb)
+  [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/ebs)
+  [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2)
+  [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder)
+  [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/ecr)
+  [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/ecs)
+  [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks)
+  [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elastic-beanstalk)
+  [Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/efs)
+  [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing)
+  [Amazon Elastic Inference](https://docs.aws.amazon.com/elastic-inference)
+  [Amazon ElastiCache](https://docs.aws.amazon.com/elasticache)
+  [AWS Elemental MediaConnect](https://docs.aws.amazon.com/mediaconnect)
+  [AWS Elemental MediaConvert](https://docs.aws.amazon.com/mediaconvert)
+  [AWS Elemental MediaLive](https://docs.aws.amazon.com/medialive)
+  [AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage)
+  [AWS Elemental MediaPackage v2](https://docs.aws.amazon.com/mediapackage)
+  [AWS Elemental MediaPackage VoD](https://docs.aws.amazon.com/mediapackage)
+  [AWS Elemental MediaTailor](https://docs.aws.amazon.com/mediatailor)
+  [Amazon MemoryDB](https://docs.aws.amazon.com/memorydb)
+  [Amazon EMR](https://docs.aws.amazon.com/emr)
+  [Amazon EMR on EKS (EMR containers)](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/)
+  [Amazon EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide)
+  [AWS Entity Resolution](https://docs.aws.amazon.com/entityresolution/latest/userguide)
+  [Amazon EventBridge Pipes](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html)
+  [Amazon EventBridge Scheduler](https://docs.aws.amazon.com/scheduler/latest/UserGuide)
+  [Amazon EventBridge Schema](https://docs.aws.amazon.com/eventbridge)
+  [AWS Fault Injection Simulator](https://docs.aws.amazon.com/fis/latest/userguide)
+  [AWS Firewall Manager](https://docs.aws.amazon.com/firewall-manager)
+  [Amazon Forecast](https://docs.aws.amazon.com/forecast)
+  [Amazon Fraud Detector](https://docs.aws.amazon.com/frauddetector)
+  [Amazon FSx](https://docs.aws.amazon.com/fsx)
+  [Amazon GameLift](https://docs.aws.amazon.com/gamelift)
+  [Amazon S3 Glacier](https://docs.aws.amazon.com/s3/?id=docs_gateway#amazon-s3-glacier)
+  [AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator)
+  [AWS Ground Station](https://docs.aws.amazon.com/ground-station)
+  [AWS Glue](https://docs.aws.amazon.com/glue)
+  [AWS Glue DataBrew](https://docs.aws.amazon.com/glue)
+  [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty)
+  [AWS Health Imaging](https://docs.aws.amazon.com/healthimaging/latest/devguide)
+  [AWS HealthLake](https://docs.aws.amazon.com/healthlake)
+  [Amazon HealthOmics](https://docs.aws.amazon.com/omics)
+  [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/iam) – at this time, you can tag only the following IAM resources using the Resource Groups Tagging API:
  +  `instance-profile`
  +  `mfa`
  +  `oidc-provider`
  +  `policy`
  +  `role`
  +  `saml-provider`
  +  `server-certificate`
  +  `user`

This document was last published on September 15, 2026.
