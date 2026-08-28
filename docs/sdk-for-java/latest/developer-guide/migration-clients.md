---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-clients.html
---

# Client changes
<a name="migration-clients"></a>

## Client builders
<a name="client-builder"></a>

You must create all clients using the client builder method. Constructors are no longer available.

**Example of creating a client in version 1.x**

```
AmazonDynamoDB ddbClient = AmazonDynamoDBClientBuilder.defaultClient();
AmazonDynamoDBClient ddbClient = new AmazonDynamoDBClient();
```

**Example of creating a client in version 2.x**

```
DynamoDbClient ddbClient = DynamoDbClient.create();
DynamoDbClient ddbClient = DynamoDbClient.builder().build();
```

## Client class names
<a name="class-names"></a>

All client class names are now fully camel cased and no longer prefixed by `Amazon`. These changes are aligned with names used in the AWS CLI.

**Example of class names in 1.x**

```
AmazonDynamoDB
AWSACMPCAAsyncClient
```

**Example of class names in 2.x**

```
DynamoDbClient
AcmAsyncClient
```

**Client class name changes**

| 1.x Client | 2.x Client |
| --- | --- |
| com.amazonaws.services.acmpca.AWSACMPCAAsyncClient | software.amazon.awssdk.services.acm.AcmAsyncClient |
| com.amazonaws.services.acmpca.AWSACMPCAClient | software.amazon.awssdk.services.acm.AcmClient |
| com.amazonaws.services.alexaforbusiness.AmazonAlexaForBusinessAsyncClient | software.amazon.awssdk.services.alexaforbusiness.AlexaForBusinessAsyncClient |
| com.amazonaws.services.alexaforbusiness.AmazonAlexaForBusinessClient | software.amazon.awssdk.services.alexaforbusiness.AlexaForBusinessClient |
| com.amazonaws.services.apigateway.AmazonApiGatewayAsyncClient | software.amazon.awssdk.services.apigateway.ApiGatewayAsyncClient |
| com.amazonaws.services.apigateway.AmazonApiGatewayClient | software.amazon.awssdk.services.apigateway.ApiGatewayClient |
| com.amazonaws.services.applicationautoscaling.AWSApplicationAutoScalingAsyncClient | software.amazon.awssdk.services.applicationautoscaling.ApplicationAutoScalingAsyncClient |
| com.amazonaws.services.applicationautoscaling.AWSApplicationAutoScalingClient | software.amazon.awssdk.services.applicationautoscaling.ApplicationAutoScalingClient |
| com.amazonaws.services.applicationdiscovery.AWSApplicationDiscoveryAsyncClient | software.amazon.awssdk.services.applicationdiscovery.ApplicationDiscoveryAsyncClient |
| com.amazonaws.services.applicationdiscovery.AWSApplicationDiscoveryClient | software.amazon.awssdk.services.applicationdiscovery.ApplicationDiscoveryClient |
| com.amazonaws.services.appstream.AmazonAppStreamAsyncClient | software.amazon.awssdk.services.appstream.AppStreamAsyncClient |
| com.amazonaws.services.appstream.AmazonAppStreamClient | software.amazon.awssdk.services.appstream.AppStreamClient |
| com.amazonaws.services.appsync.AWSAppSyncAsyncClient | software.amazon.awssdk.services.appsync.AppSyncAsyncClient |
| com.amazonaws.services.appsync.AWSAppSyncClient | software.amazon.awssdk.services.appsync.AppSyncClient |
| com.amazonaws.services.athena.AmazonAthenaAsyncClient | software.amazon.awssdk.services.athena.AthenaAsyncClient |
| com.amazonaws.services.athena.AmazonAthenaClient | software.amazon.awssdk.services.athena.AthenaClient |
| com.amazonaws.services.autoscaling.AmazonAutoScalingAsyncClient | software.amazon.awssdk.services.autoscaling.AutoScalingAsyncClient |
| com.amazonaws.services.autoscaling.AmazonAutoScalingClient | software.amazon.awssdk.services.autoscaling.AutoScalingClient |
| com.amazonaws.services.autoscalingplans.AWSAutoScalingPlansAsyncClient | software.amazon.awssdk.services.autoscalingplans.AutoScalingPlansAsyncClient |
| com.amazonaws.services.autoscalingplans.AWSAutoScalingPlansClient | software.amazon.awssdk.services.autoscalingplans.AutoScalingPlansClient |
| com.amazonaws.services.batch.AWSBatchAsyncClient | software.amazon.awssdk.services.batch.BatchAsyncClient |
| com.amazonaws.services.batch.AWSBatchClient | software.amazon.awssdk.services.batch.BatchClient |
| com.amazonaws.services.budgets.AWSBudgetsAsyncClient | software.amazon.awssdk.services.budgets.BudgetsAsyncClient |
| com.amazonaws.services.budgets.AWSBudgetsClient | software.amazon.awssdk.services.budgets.BudgetsClient |
| com.amazonaws.services.certificatemanager.AWSCertificateManagerAsyncClient | software.amazon.awssdk.services.acm.AcmAsyncClient |
| com.amazonaws.services.certificatemanager.AWSCertificateManagerClient | software.amazon.awssdk.services.acm.AcmClient |
| com.amazonaws.services.cloud9.AWSCloud9AsyncClient | software.amazon.awssdk.services.cloud9.Cloud9AsyncClient |
| com.amazonaws.services.cloud9.AWSCloud9Client | software.amazon.awssdk.services.cloud9.Cloud9Client |
| com.amazonaws.services.clouddirectory.AmazonCloudDirectoryAsyncClient | software.amazon.awssdk.services.clouddirectory.CloudDirectoryAsyncClient |
| com.amazonaws.services.clouddirectory.AmazonCloudDirectoryClient | software.amazon.awssdk.services.clouddirectory.CloudDirectoryClient |
| com.amazonaws.services.cloudformation.AmazonCloudFormationAsyncClient | software.amazon.awssdk.services.cloudformation.CloudFormationAsyncClient |
| com.amazonaws.services.cloudformation.AmazonCloudFormationClient | software.amazon.awssdk.services.cloudformation.CloudFormationClient |
| com.amazonaws.services.cloudfront.AmazonCloudFrontAsyncClient | software.amazon.awssdk.services.cloudfront.CloudFrontAsyncClient |
| com.amazonaws.services.cloudfront.AmazonCloudFrontClient | software.amazon.awssdk.services.cloudfront.CloudFrontClient |
| com.amazonaws.services.cloudhsm.AWSCloudHSMAsyncClient | software.amazon.awssdk.services.cloudhsm.CloudHsmAsyncClient |
| com.amazonaws.services.cloudhsm.AWSCloudHSMClient | software.amazon.awssdk.services.cloudhsm.CloudHsmClient |
| com.amazonaws.services.cloudhsmv2.AWSCloudHSMV2AsyncClient | software.amazon.awssdk.services.cloudhsmv2.CloudHsmV2AsyncClient |
| com.amazonaws.services.cloudhsmv2.AWSCloudHSMV2Client | software.amazon.awssdk.services.cloudhsmv2.CloudHsmV2Client |
| com.amazonaws.services.cloudsearchdomain.AmazonCloudSearchDomainAsyncClient | software.amazon.awssdk.services.cloudsearchdomain.CloudSearchDomainAsyncClient |
| com.amazonaws.services.cloudsearchdomain.AmazonCloudSearchDomainClient | software.amazon.awssdk.services.cloudsearchdomain.CloudSearchDomainClient |
| com.amazonaws.services.cloudsearchv2.AmazonCloudSearchAsyncClient | software.amazon.awssdk.services.cloudsearch.CloudSearchAsyncClient |
| com.amazonaws.services.cloudsearchv2.AmazonCloudSearchClient | software.amazon.awssdk.services.cloudsearch.CloudSearchClient |
| com.amazonaws.services.cloudtrail.AWSCloudTrailAsyncClient | software.amazon.awssdk.services.cloudtrail.CloudTrailAsyncClient |
| com.amazonaws.services.cloudtrail.AWSCloudTrailClient | software.amazon.awssdk.services.cloudtrail.CloudTrailClient |
| com.amazonaws.services.cloudwatch.AmazonCloudWatchAsyncClient | software.amazon.awssdk.services.cloudwatch.CloudWatchAsyncClient |
| com.amazonaws.services.cloudwatch.AmazonCloudWatchClient | software.amazon.awssdk.services.cloudwatch.CloudWatchClient |
| com.amazonaws.services.cloudwatchevents.AmazonCloudWatchEventsAsyncClient | software.amazon.awssdk.services.cloudwatchevents.CloudWatchEventsAsyncClient |
| com.amazonaws.services.cloudwatchevents.AmazonCloudWatchEventsClient | software.amazon.awssdk.services.cloudwatchevents.CloudWatchEventsClient |
| com.amazonaws.services.codebuild.AWSCodeBuildAsyncClient | software.amazon.awssdk.services.codebuild.CodeBuildAsyncClient |
| com.amazonaws.services.codebuild.AWSCodeBuildClient | software.amazon.awssdk.services.codebuild.CodeBuildClient |
| com.amazonaws.services.codecommit.AWSCodeCommitAsyncClient | software.amazon.awssdk.services.codecommit.CodeCommitAsyncClient |
| com.amazonaws.services.codecommit.AWSCodeCommitClient | software.amazon.awssdk.services.codecommit.CodeCommitClient |
| com.amazonaws.services.codedeploy.AmazonCodeDeployAsyncClient | software.amazon.awssdk.services.codedeploy.CodeDeployAsyncClient |
| com.amazonaws.services.codedeploy.AmazonCodeDeployClient | software.amazon.awssdk.services.codedeploy.CodeDeployClient |
| com.amazonaws.services.codepipeline.AWSCodePipelineAsyncClient | software.amazon.awssdk.services.codepipeline.CodePipelineAsyncClient |
| com.amazonaws.services.codepipeline.AWSCodePipelineClient | software.amazon.awssdk.services.codepipeline.CodePipelineClient |
| com.amazonaws.services.codestar.AWSCodeStarAsyncClient | software.amazon.awssdk.services.codestar.CodeStarAsyncClient |
| com.amazonaws.services.codestar.AWSCodeStarClient | software.amazon.awssdk.services.codestar.CodeStarClient |
| com.amazonaws.services.cognitoidentity.AmazonCognitoIdentityAsyncClient | software.amazon.awssdk.services.cognitoidentity.CognitoIdentityAsyncClient |
| com.amazonaws.services.cognitoidentity.AmazonCognitoIdentityClient | software.amazon.awssdk.services.cognitoidentity.CognitoIdentityClient |
| com.amazonaws.services.cognitoidp.AWSCognitoIdentityProviderAsyncClient | software.amazon.awssdk.services.cognitoidentityprovider.CognitoIdentityProviderAsyncClient |
| com.amazonaws.services.cognitoidp.AWSCognitoIdentityProviderClient | software.amazon.awssdk.services.cognitoidentityprovider.CognitoIdentityProviderClient |
| com.amazonaws.services.cognitosync.AmazonCognitoSyncAsyncClient | software.amazon.awssdk.services.cognitosync.CognitoSyncAsyncClient |
| com.amazonaws.services.cognitosync.AmazonCognitoSyncClient | software.amazon.awssdk.services.cognitosync.CognitoSyncClient |
| com.amazonaws.services.comprehend.AmazonComprehendAsyncClient | software.amazon.awssdk.services.comprehend.ComprehendAsyncClient |
| com.amazonaws.services.comprehend.AmazonComprehendClient | software.amazon.awssdk.services.comprehend.ComprehendClient |
| com.amazonaws.services.config.AmazonConfigAsyncClient | software.amazon.awssdk.services.config.ConfigAsyncClient |
| com.amazonaws.services.config.AmazonConfigClient | software.amazon.awssdk.services.config.ConfigClient |
| com.amazonaws.services.connect.AmazonConnectAsyncClient | software.amazon.awssdk.services.connect.ConnectAsyncClient |
| com.amazonaws.services.connect.AmazonConnectClient | software.amazon.awssdk.services.connect.ConnectClient |
| com.amazonaws.services.costandusagereport.AWSCostAndUsageReportAsyncClient | software.amazon.awssdk.services.costandusagereport.CostAndUsageReportAsyncClient |
| com.amazonaws.services.costandusagereport.AWSCostAndUsageReportClient | software.amazon.awssdk.services.costandusagereport.CostAndUsageReportClient |
| com.amazonaws.services.costexplorer.AWSCostExplorerAsyncClient | software.amazon.awssdk.services.costexplorer.CostExplorerAsyncClient |
| com.amazonaws.services.costexplorer.AWSCostExplorerClient | software.amazon.awssdk.services.costexplorer.CostExplorerClient |
| com.amazonaws.services.databasemigrationservice.AWSDatabaseMigrationServiceAsyncClient | software.amazon.awssdk.services.databasemigration.DatabaseMigrationAsyncClient |
| com.amazonaws.services.databasemigrationservice.AWSDatabaseMigrationServiceClient | software.amazon.awssdk.services.databasemigration.DatabaseMigrationClient |
| com.amazonaws.services.datapipeline.DataPipelineAsyncClient | software.amazon.awssdk.services.datapipeline.DataPipelineAsyncClient |
| com.amazonaws.services.datapipeline.DataPipelineClient | software.amazon.awssdk.services.datapipeline.DataPipelineAsyncClient |
| com.amazonaws.services.dax.AmazonDaxAsyncClient | software.amazon.awssdk.services.dax.DaxAsyncClient |
| com.amazonaws.services.dax.AmazonDaxClient | software.amazon.awssdk.services.dax.DaxClient |
| com.amazonaws.services.devicefarm.AWSDeviceFarmAsyncClient | software.amazon.awssdk.services.devicefarm.DeviceFarmAsyncClient |
| com.amazonaws.services.devicefarm.AWSDeviceFarmClient | software.amazon.awssdk.services.devicefarm.DeviceFarmClient |
| com.amazonaws.services.directconnect.AmazonDirectConnectAsyncClient | software.amazon.awssdk.services.directconnect.DirectConnectAsyncClient |
| com.amazonaws.services.directconnect.AmazonDirectConnectClient | software.amazon.awssdk.services.directconnect.DirectConnectClient |
| com.amazonaws.services.directory.AWSDirectoryServiceAsyncClient | software.amazon.awssdk.services.directory.DirectoryAsyncClient |
| com.amazonaws.services.directory.AWSDirectoryServiceClient | software.amazon.awssdk.services.directory.DirectoryClient |
| com.amazonaws.services.dlm.AmazonDLMAsyncClient | software.amazon.awssdk.services.dlm.DlmAsyncClient |
| com.amazonaws.services.dlm.AmazonDLMClient | software.amazon.awssdk.services.dlm.DlmClient |
| com.amazonaws.services.dynamodbv2.AmazonDynamoDBAsyncClient | software.amazon.awssdk.services.dynamodb.DynamoDbAsyncClient |
| com.amazonaws.services.dynamodbv2.AmazonDynamoDBClient | software.amazon.awssdk.services.dynamodb.DynamoDbClient |
| com.amazonaws.services.dynamodbv2.AmazonDynamoDBStreamsAsyncClient | software.amazon.awssdk.services.dynamodb.streams.DynamoDbStreamsAsyncClient |
| com.amazonaws.services.dynamodbv2.AmazonDynamoDBStreamsClient | software.amazon.awssdk.services.dynamodb.streams.DynamoDbStreamsClient |
| com.amazonaws.services.ec2.AmazonEC2AsyncClient | software.amazon.awssdk.services.ec2.Ec2AsyncClient |
| com.amazonaws.services.ec2.AmazonEC2Client | software.amazon.awssdk.services.ec2.Ec2Client |
| com.amazonaws.services.ecr.AmazonECRAsyncClient | software.amazon.awssdk.services.ecr.EcrAsyncClient |
| com.amazonaws.services.ecr.AmazonECRClient | software.amazon.awssdk.services.ecr.EcrClient |
| com.amazonaws.services.ecs.AmazonECSAsyncClient | software.amazon.awssdk.services.ecs.EcsAsyncClient |
| com.amazonaws.services.ecs.AmazonECSClient | software.amazon.awssdk.services.ecs.EcsClient |
| com.amazonaws.services.eks.AmazonEKSAsyncClient | software.amazon.awssdk.services.eks.EksAsyncClient |
| com.amazonaws.services.eks.AmazonEKSClient | software.amazon.awssdk.services.eks.EksClient |
| com.amazonaws.services.elasticache.AmazonElastiCacheAsyncClient | software.amazon.awssdk.services.elasticache.ElastiCacheAsyncClient |
| com.amazonaws.services.elasticache.AmazonElastiCacheClient | software.amazon.awssdk.services.elasticache.ElastiCacheClient |
| com.amazonaws.services.elasticbeanstalk.AWSElasticBeanstalkAsyncClient | software.amazon.awssdk.services.elasticbeanstalk.ElasticBeanstalkAsyncClient |
| com.amazonaws.services.elasticbeanstalk.AWSElasticBeanstalkClient | software.amazon.awssdk.services.elasticbeanstalk.ElasticBeanstalkClient |
| com.amazonaws.services.elasticfilesystem.AmazonElasticFileSystemAsyncClient | software.amazon.awssdk.services.efs.EfsAsyncClient |
| com.amazonaws.services.elasticfilesystem.AmazonElasticFileSystemClient | software.amazon.awssdk.services.efs.EfsClient |
| com.amazonaws.services.elasticloadbalancing.AmazonElasticLoadBalancingAsyncClient | software.amazon.awssdk.services.elasticloadbalancing.ElasticLoadBalancingAsyncClient |
| com.amazonaws.services.elasticloadbalancing.AmazonElasticLoadBalancingClient | software.amazon.awssdk.services.elasticloadbalancing.ElasticLoadBalancingClient |
| com.amazonaws.services.elasticloadbalancingv2.AmazonElasticLoadBalancingAsyncClient | software.amazon.awssdk.services.elasticloadbalancingv2.ElasticLoadBalancingV2AsyncClient |
| com.amazonaws.services.elasticloadbalancingv2.AmazonElasticLoadBalancingClient | software.amazon.awssdk.services.elasticloadbalancingv2.ElasticLoadBalancingV2Client |
| com.amazonaws.services.elasticmapreduce.AmazonElasticMapReduceAsyncClient | software.amazon.awssdk.services.emr.EmrAsyncClient |
| com.amazonaws.services.elasticmapreduce.AmazonElasticMapReduceClient | software.amazon.awssdk.services.emr.EmrClient |
| com.amazonaws.services.elasticsearch.AWSElasticsearchAsyncClient | software.amazon.awssdk.services.elasticsearch.ElasticsearchAsyncClient |
| com.amazonaws.services.elasticsearch.AWSElasticsearchClient | software.amazon.awssdk.services.elasticsearch.ElasticsearchClient |
| com.amazonaws.services.elastictranscoder.AmazonElasticTranscoderAsyncClient | software.amazon.awssdk.services.elastictranscoder.ElasticTranscoderAsyncClient |
| com.amazonaws.services.elastictranscoder.AmazonElasticTranscoderClient | software.amazon.awssdk.services.elastictranscoder.ElasticTranscoderClient |
| com.amazonaws.services.fms.AWSFMSAsyncClient | software.amazon.awssdk.services.fms.FmsAsyncClient |
| com.amazonaws.services.fms.AWSFMSClient | software.amazon.awssdk.services.fms.FmsClient |
| com.amazonaws.services.gamelift.AmazonGameLiftAsyncClient | software.amazon.awssdk.services.gamelift.GameLiftAsyncClient |
| com.amazonaws.services.gamelift.AmazonGameLiftClient | software.amazon.awssdk.services.gamelift.GameLiftClient |
| com.amazonaws.services.glacier.AmazonGlacierAsyncClient | software.amazon.awssdk.services.glacier.GlacierAsyncClient |
| com.amazonaws.services.glacier.AmazonGlacierClient | software.amazon.awssdk.services.glacier.GlacierClient |
| com.amazonaws.services.glue.AWSGlueAsyncClient | software.amazon.awssdk.services.glue.GlueAsyncClient |
| com.amazonaws.services.glue.AWSGlueClient | software.amazon.awssdk.services.glue.GlueClient |
| com.amazonaws.services.greengrass.AWSGreengrassAsyncClient | software.amazon.awssdk.services.greengrass.GreengrassAsyncClient |
| com.amazonaws.services.greengrass.AWSGreengrassClient | software.amazon.awssdk.services.greengrass.GreengrassClient |
| com.amazonaws.services.guardduty.AmazonGuardDutyAsyncClient | software.amazon.awssdk.services.guardduty.GuardDutyAsyncClient |
| com.amazonaws.services.guardduty.AmazonGuardDutyClient | software.amazon.awssdk.services.guardduty.GuardDutyClient |
| com.amazonaws.services.health.AWSHealthAsyncClient | software.amazon.awssdk.services.health.HealthAsyncClient |
| com.amazonaws.services.health.AWSHealthClient | software.amazon.awssdk.services.health.HealthClient |
| com.amazonaws.services.identitymanagement.AmazonIdentityManagementAsyncClient | software.amazon.awssdk.services.iam.IamAsyncClient |
| com.amazonaws.services.identitymanagement.AmazonIdentityManagementClient | software.amazon.awssdk.services.iam.IamClient |
| com.amazonaws.services.importexport.AmazonImportExportAsyncClient | {{Deprecated}} |
| com.amazonaws.services.importexport.AmazonImportExportClient | {{Deprecated}} |
| com.amazonaws.services.inspector.AmazonInspectorAsyncClient | software.amazon.awssdk.services.inspector.InspectorAsyncClient |
| com.amazonaws.services.inspector.AmazonInspectorClient | software.amazon.awssdk.services.inspector.InspectorClient |
| com.amazonaws.services.iot.AWSIotAsyncClient | software.amazon.awssdk.services.iot.IotAsyncClient |
| com.amazonaws.services.iot.AWSIotClient | software.amazon.awssdk.services.iot.IotClient |
| com.amazonaws.services.iot1clickdevices.AWSIoT1ClickDevicesAsyncClient | software.amazon.awssdk.services.iot1clickdevices.Iot1ClickDevicesAsyncClient |
| com.amazonaws.services.iot1clickdevices.AWSIoT1ClickDevicesClient | software.amazon.awssdk.services.iot1clickdevices.Iot1ClickDevicesClient |
| com.amazonaws.services.iot1clickprojects.AWSIoT1ClickProjectsAsyncClient | software.amazon.awssdk.services.iot1clickprojects.Iot1ClickProjectsAsyncClient |
| com.amazonaws.services.iot1clickprojects.AWSIoT1ClickProjectsClient | software.amazon.awssdk.services.iot1clickprojects.Iot1ClickProjectsClient |
| com.amazonaws.services.iotanalytics.AWSIoTAnalyticsAsyncClient | software.amazon.awssdk.services.iotanalytics.IotAnalyticsAsyncClient |
| com.amazonaws.services.iotanalytics.AWSIoTAnalyticsClient | software.amazon.awssdk.services.iotanalytics.IotAnalyticsClient |
| com.amazonaws.services.iotdata.AWSIotDataAsyncClient | software.amazon.awssdk.services.iotdata.IotDataAsyncClient |
| com.amazonaws.services.iotdata.AWSIotDataClient | software.amazon.awssdk.services.iotdata.IotDataClient |
| com.amazonaws.services.iotjobsdataplane.AWSIoTJobsDataPlaneAsyncClient | software.amazon.awssdk.services.iotdataplane.IotDataPlaneAsyncClient |
| com.amazonaws.services.iotjobsdataplane.AWSIoTJobsDataPlaneClient | software.amazon.awssdk.services.iotdataplane.IotDataPlaneClient |
| com.amazonaws.services.kinesis.AmazonKinesisAsyncClient | software.amazon.awssdk.services.kinesis.KinesisAsyncClient |
| com.amazonaws.services.kinesis.AmazonKinesisClient | software.amazon.awssdk.services.kinesis.KinesisClient |
| com.amazonaws.services.kinesisanalytics.AmazonKinesisAnalyticsAsyncClient | software.amazon.awssdk.services.kinesisanalytics.KinesisAnalyticsAsyncClient |
| com.amazonaws.services.kinesisanalytics.AmazonKinesisAnalyticsClient | software.amazon.awssdk.services.kinesisanalytics.KinesisAnalyticsClient |
| com.amazonaws.services.kinesisfirehose.AmazonKinesisFirehoseAsyncClient | software.amazon.awssdk.services.firehose.FirehoseAsyncClient |
| com.amazonaws.services.kinesisfirehose.AmazonKinesisFirehoseClient | software.amazon.awssdk.services.firehose.FirehoseClient |
| com.amazonaws.services.kinesisvideo.AmazonKinesisVideoArchivedMediaAsyncClient | software.amazon.awssdk.services.kinesisvideoarchivedmedia.KinesisVideoArchivedMediaAsyncClient |
| com.amazonaws.services.kinesisvideo.AmazonKinesisVideoArchivedMediaClient | software.amazon.awssdk.services.kinesisvideoarchivedmedia.KinesisVideoArchivedMediaClient |
| com.amazonaws.services.kinesisvideo.AmazonKinesisVideoAsyncClient | software.amazon.awssdk.services.kinesisvideo.KinesisVideoAsyncClient |
| com.amazonaws.services.kinesisvideo.AmazonKinesisVideoClient | software.amazon.awssdk.services.kinesisvideo.KinesisVideoClient |
| com.amazonaws.services.kinesisvideo.AmazonKinesisVideoMediaAsyncClient | software.amazon.awssdk.services.kinesisvideomedia.KinesisVideoMediaAsyncClient |
| com.amazonaws.services.kinesisvideo.AmazonKinesisVideoMediaClient | software.amazon.awssdk.services.kinesisvideomedia.KinesisVideoMediaClient |
| com.amazonaws.services.kinesisvideo.AmazonKinesisVideoPutMediaClient | Not Supported  |
| com.amazonaws.services.kms.AWSKMSAsyncClient | software.amazon.awssdk.services.kms.KmsAsyncClient |
| com.amazonaws.services.kms.AWSKMSClient | software.amazon.awssdk.services.kms.KmsClient |
| com.amazonaws.services.lambda.AWSLambdaAsyncClient | software.amazon.awssdk.services.lambda.LambdaAsyncClient |
| com.amazonaws.services.lambda.AWSLambdaClient | software.amazon.awssdk.services.lambda.LambdaClient |
| com.amazonaws.services.lexmodelbuilding.AmazonLexModelBuildingAsyncClient | software.amazon.awssdk.services.lexmodelbuilding.LexModelBuildingAsyncClient |
| com.amazonaws.services.lexmodelbuilding.AmazonLexModelBuildingClient | software.amazon.awssdk.services.lexmodelbuilding.LexModelBuildingClient |
| com.amazonaws.services.lexruntime.AmazonLexRuntimeAsyncClient | software.amazon.awssdk.services.lexruntime.LexRuntimeAsyncClient |
| com.amazonaws.services.lexruntime.AmazonLexRuntimeClient | software.amazon.awssdk.services.lexruntime.LexRuntimeClient |
| com.amazonaws.services.lightsail.AmazonLightsailAsyncClient | software.amazon.awssdk.services.lightsail.LightsailAsyncClient |
| com.amazonaws.services.lightsail.AmazonLightsailClient | software.amazon.awssdk.services.lightsail.LightsailClient |
| com.amazonaws.services.logs.AWSLogsAsyncClient | software.amazon.awssdk.services.logs.LogsAsyncClient |
| com.amazonaws.services.logs.AWSLogsClient | software.amazon.awssdk.services.logs.LogsClient |
| com.amazonaws.services.machinelearning.AmazonMachineLearningAsyncClient | software.amazon.awssdk.services.machinelearning.MachineLearningAsyncClient |
| com.amazonaws.services.machinelearning.AmazonMachineLearningClient | software.amazon.awssdk.services.machinelearning.MachineLearningClient |
| com.amazonaws.services.macie.AmazonMacieAsyncClient | software.amazon.awssdk.services.macie.MacieAsyncClient |
| com.amazonaws.services.macie.AmazonMacieClient | software.amazon.awssdk.services.macie.MacieClient |
| com.amazonaws.services.marketplacecommerceanalytics.AWSMarketplaceCommerceAnalyticsAsyncClient | software.amazon.awssdk.services.marketplacecommerceanalytics.MarketplaceCommerceAnalyticsAsyncClient |
| com.amazonaws.services.marketplacecommerceanalytics.AWSMarketplaceCommerceAnalyticsClient | software.amazon.awssdk.services.marketplacecommerceanalytics.MarketplaceCommerceAnalyticsClient |
| com.amazonaws.services.marketplaceentitlement.AWSMarketplaceEntitlementAsyncClient | software.amazon.awssdk.services.marketplaceentitlement.MarketplaceEntitlementAsyncClient |
| com.amazonaws.services.marketplaceentitlement.AWSMarketplaceEntitlementClient | software.amazon.awssdk.services.marketplaceentitlement.MarketplaceEntitlementClient |
| com.amazonaws.services.marketplacemetering.AWSMarketplaceMeteringAsyncClient | software.amazon.awssdk.services.marketplacemetering.MarketplaceMeteringAsyncClient |
| com.amazonaws.services.marketplacemetering.AWSMarketplaceMeteringClient | software.amazon.awssdk.services.marketplacemetering.MarketplaceMeteringClient |
| com.amazonaws.services.mediaconvert.AWSMediaConvertAsyncClient | software.amazon.awssdk.services.mediaconvert.MediaConvertAsyncClient |
| com.amazonaws.services.mediaconvert.AWSMediaConvertClient | software.amazon.awssdk.services.mediaconvert.MediaConvertClient |
| com.amazonaws.services.medialive.AWSMediaLiveAsyncClient | software.amazon.awssdk.services.medialive.MediaLiveAsyncClient |
| com.amazonaws.services.medialive.AWSMediaLiveClient | software.amazon.awssdk.services.medialive.MediaLiveClient |
| com.amazonaws.services.mediapackage.AWSMediaPackageAsyncClient | software.amazon.awssdk.services.mediapackage.MediaPackageAsyncClient |
| com.amazonaws.services.mediapackage.AWSMediaPackageClient | software.amazon.awssdk.services.mediapackage.MediaPackageClient |
| com.amazonaws.services.mediastore.AWSMediaStoreAsyncClient | software.amazon.awssdk.services.mediastore.MediaStoreAsyncClient |
| com.amazonaws.services.mediastore.AWSMediaStoreClient | software.amazon.awssdk.services.mediastore.MediaStoreClient |
| com.amazonaws.services.mediastoredata.AWSMediaStoreDataAsyncClient | software.amazon.awssdk.services.mediastoredata.MediaStoreDataAsyncClient |
| com.amazonaws.services.mediastoredata.AWSMediaStoreDataClient | software.amazon.awssdk.services.mediastoredata.MediaStoreDataClient |
| com.amazonaws.services.mediatailor.AWSMediaTailorAsyncClient | software.amazon.awssdk.services.mediatailor.MediaTailorAsyncClient |
| com.amazonaws.services.mediatailor.AWSMediaTailorClient | software.amazon.awssdk.services.mediatailor.MediaTailorClient |
| com.amazonaws.services.migrationhub.AWSMigrationHubAsyncClient | software.amazon.awssdk.services.migrationhub.MigrationHubAsyncClient |
| com.amazonaws.services.migrationhub.AWSMigrationHubClient | software.amazon.awssdk.services.migrationhub.MigrationHubClient |
| com.amazonaws.services.mobile.AWSMobileAsyncClient | software.amazon.awssdk.services.mobile.MobileAsyncClient |
| com.amazonaws.services.mobile.AWSMobileClient | software.amazon.awssdk.services.mobile.MobileClient |
| com.amazonaws.services.mq.AmazonMQAsyncClient | software.amazon.awssdk.services.mq.MqAsyncClient |
| com.amazonaws.services.mq.AmazonMQClient | software.amazon.awssdk.services.mq.MqClient |
| com.amazonaws.services.mturk.AmazonMTurkAsyncClient | software.amazon.awssdk.services.mturk.MTurkAsyncClient |
| com.amazonaws.services.mturk.AmazonMTurkClient | software.amazon.awssdk.services.mturk.MTurkClient |
| com.amazonaws.services.neptune.AmazonNeptuneAsyncClient | software.amazon.awssdk.services.neptune.NeptuneAsyncClient |
| com.amazonaws.services.neptune.AmazonNeptuneClient | software.amazon.awssdk.services.neptune.NeptuneClient |
| com.amazonaws.services.opsworks.AWSOpsWorksAsyncClient | software.amazon.awssdk.services.opsworks.OpsWorksAsyncClient |
| com.amazonaws.services.opsworks.AWSOpsWorksClient | software.amazon.awssdk.services.opsworks.OpsWorksClient |
| com.amazonaws.services.opsworkscm.AWSOpsWorksCMAsyncClient | software.amazon.awssdk.services.opsworkscm.OpsWorksCmAsyncClient |
| com.amazonaws.services.opsworkscm.AWSOpsWorksCMClient | software.amazon.awssdk.services.opsworkscm.OpsWorksCmClient |
| com.amazonaws.services.organizations.AWSOrganizationsAsyncClient | software.amazon.awssdk.services.organizations.OrganizationsAsyncClient |
| com.amazonaws.services.organizations.AWSOrganizationsClient | software.amazon.awssdk.services.organizations.OrganizationsClient |
| com.amazonaws.services.pi.AWSPIAsyncClient | software.amazon.awssdk.services.pi.PiAsyncClient |
| com.amazonaws.services.pi.AWSPIClient | software.amazon.awssdk.services.pi.PiClient |
| com.amazonaws.services.pinpoint.AmazonPinpointAsyncClient | software.amazon.awssdk.services.pinpoint.PinpointAsyncClient |
| com.amazonaws.services.pinpoint.AmazonPinpointClient | software.amazon.awssdk.services.pinpoint.PinpointClient |
| com.amazonaws.services.polly.AmazonPollyAsyncClient | software.amazon.awssdk.services.polly.PollyAsyncClient |
| com.amazonaws.services.polly.AmazonPollyClient | software.amazon.awssdk.services.polly.PollyClient |
| com.amazonaws.services.pricing.AWSPricingAsyncClient | software.amazon.awssdk.services.pricing.PricingAsyncClient |
| com.amazonaws.services.pricing.AWSPricingClient | software.amazon.awssdk.services.pricing.PricingClient |
| com.amazonaws.services.rds.AmazonRDSAsyncClient | software.amazon.awssdk.services.rds.RdsAsyncClient |
| com.amazonaws.services.rds.AmazonRDSClient | software.amazon.awssdk.services.rds.RdsClient |
| com.amazonaws.services.redshift.AmazonRedshiftAsyncClient | software.amazon.awssdk.services.redshift.RedshiftAsyncClient |
| com.amazonaws.services.redshift.AmazonRedshiftClient | software.amazon.awssdk.services.redshift.RedshiftClient |
| com.amazonaws.services.rekognition.AmazonRekognitionAsyncClient | software.amazon.awssdk.services.rekognition.RekognitionAsyncClient |
| com.amazonaws.services.rekognition.AmazonRekognitionClient | software.amazon.awssdk.services.rekognition.RekognitionClient |
| com.amazonaws.services.resourcegroups.AWSResourceGroupsAsyncClient | software.amazon.awssdk.services.resourcegroups.ResourceGroupsAsyncClient |
| com.amazonaws.services.resourcegroups.AWSResourceGroupsClient | software.amazon.awssdk.services.resourcegroups.ResourceGroupsClient |
| com.amazonaws.services.resourcegroupstaggingapi.AWSResourceGroupsTaggingAPIAsyncClient | software.amazon.awssdk.services.resourcegroupstaggingapi.ResourceGroupsTaggingApiAsyncClient |
| com.amazonaws.services.resourcegroupstaggingapi.AWSResourceGroupsTaggingAPIClient | software.amazon.awssdk.services.resourcegroupstaggingapi.ResourceGroupsTaggingApiClient |
| com.amazonaws.services.route53.AmazonRoute53AsyncClient | software.amazon.awssdk.services.route53.Route53AsyncClient |
| com.amazonaws.services.route53.AmazonRoute53Client | software.amazon.awssdk.services.route53.Route53Client |
| com.amazonaws.services.route53domains.AmazonRoute53DomainsAsyncClient | software.amazon.awssdk.services.route53domains.Route53DomainsAsyncClient |
| com.amazonaws.services.route53domains.AmazonRoute53DomainsClient | software.amazon.awssdk.services.route53domains.Route53DomainsClient |
| com.amazonaws.services.s3.AmazonS3Client | software.amazon.awssdk.services.s3.S3Client |
| com.amazonaws.services.sagemaker.AmazonSageMakerAsyncClient | software.amazon.awssdk.services.sagemaker.SageMakerAsyncClient |
| com.amazonaws.services.sagemaker.AmazonSageMakerClient | software.amazon.awssdk.services.sagemaker.SageMakerClient |
| com.amazonaws.services.sagemakerruntime.AmazonSageMakerRuntimeAsyncClient | software.amazon.awssdk.services.sagemakerruntime.SageMakerRuntimeAsyncClient |
| com.amazonaws.services.sagemakerruntime.AmazonSageMakerRuntimeClient | software.amazon.awssdk.services.sagemakerruntime.SageMakerRuntimeClient |
| com.amazonaws.services.secretsmanager.AWSSecretsManagerAsyncClient | software.amazon.awssdk.services.secretsmanager.SecretsManagerAsyncClient |
| com.amazonaws.services.secretsmanager.AWSSecretsManagerClient | software.amazon.awssdk.services.secretsmanager.SecretsManagerClient |
| com.amazonaws.services.securitytoken.AWSSecurityTokenServiceAsyncClient | software.amazon.awssdk.services.sts.StsAsyncClient |
| com.amazonaws.services.securitytoken.AWSSecurityTokenServiceClient | software.amazon.awssdk.services.sts.StsClient |
| com.amazonaws.services.serverlessapplicationrepository.AWSServerlessApplicationRepositoryAsyncClient | software.amazon.awssdk.services.serverlessapplicationrepository.ServerlessApplicationRepositoryAsyncClient |
| com.amazonaws.services.serverlessapplicationrepository.AWSServerlessApplicationRepositoryClient | software.amazon.awssdk.services.serverlessapplicationrepository.ServerlessApplicationRepositoryClient |
| com.amazonaws.services.servermigration.AWSServerMigrationAsyncClient | software.amazon.awssdk.services.sms.SmsAsyncClient |
| com.amazonaws.services.servermigration.AWSServerMigrationClient | software.amazon.awssdk.services.sms.SmsClient |
| com.amazonaws.services.servicecatalog.AWSServiceCatalogAsyncClient | software.amazon.awssdk.services.servicecatalog.ServiceCatalogAsyncClient |
| com.amazonaws.services.servicecatalog.AWSServiceCatalogClient | software.amazon.awssdk.services.servicecatalog.ServiceCatalogClient |
| com.amazonaws.services.servicediscovery.AWSServiceDiscoveryAsyncClient | software.amazon.awssdk.services.servicediscovery.ServiceDiscoveryAsyncClient |
| com.amazonaws.services.servicediscovery.AWSServiceDiscoveryClient | software.amazon.awssdk.services.servicediscovery.ServiceDiscoveryClient |
| com.amazonaws.services.shield.AWSShieldAsyncClient | software.amazon.awssdk.services.shield.ShieldAsyncClient |
| com.amazonaws.services.shield.AWSShieldClient | software.amazon.awssdk.services.shield.ShieldClient |
| com.amazonaws.services.simpledb.AmazonSimpleDBAsyncClient | software.amazon.awssdk.services.simpledb.SimpleDbAsyncClient |
| com.amazonaws.services.simpledb.AmazonSimpleDBClient | software.amazon.awssdk.services.simpledb.SimpleDbClient |
| com.amazonaws.services.simpleemail.AmazonSimpleEmailServiceAsyncClient | software.amazon.awssdk.services.ses.SesAsyncClient |
| com.amazonaws.services.simpleemail.AmazonSimpleEmailServiceClient | software.amazon.awssdk.services.ses.SesClient |
| com.amazonaws.services.simplesystemsmanagement.AWSSimpleSystemsManagementAsyncClient | software.amazon.awssdk.services.ssm.SsmAsyncClient |
| com.amazonaws.services.simplesystemsmanagement.AWSSimpleSystemsManagementClient | software.amazon.awssdk.services.ssm.SsmClient |
| com.amazonaws.services.simpleworkflow.AmazonSimpleWorkflowAsyncClient | software.amazon.awssdk.services.swf.SwfAsyncClient |
| com.amazonaws.services.simpleworkflow.AmazonSimpleWorkflowClient | software.amazon.awssdk.services.swf.SwfClient |
| com.amazonaws.services.snowball.AmazonSnowballAsyncClient | software.amazon.awssdk.services.snowball.SnowballAsyncClient |
| com.amazonaws.services.snowball.AmazonSnowballClient | software.amazon.awssdk.services.snowball.SnowballClient |
| com.amazonaws.services.sns.AmazonSNSAsyncClient | software.amazon.awssdk.services.sns.SnsAsyncClient |
| com.amazonaws.services.sns.AmazonSNSClient | software.amazon.awssdk.services.sns.SnsClient |
| com.amazonaws.services.sqs.AmazonSQSAsyncClient | software.amazon.awssdk.services.sqs.SqsAsyncClient |
| com.amazonaws.services.sqs.AmazonSQSClient | software.amazon.awssdk.services.sqs.SqsClient |
| com.amazonaws.services.stepfunctions.AWSStepFunctionsAsyncClient | software.amazon.awssdk.services.sfn.SfnAsyncClient |
| com.amazonaws.services.stepfunctions.AWSStepFunctionsClient | software.amazon.awssdk.services.sfn.SfnClient |
| com.amazonaws.services.storagegateway.AWSStorageGatewayAsyncClient | software.amazon.awssdk.services.storagegateway.StorageGatewayAsyncClient |
| com.amazonaws.services.storagegateway.AWSStorageGatewayClient | software.amazon.awssdk.services.storagegateway.StorageGatewayClient |
| com.amazonaws.services.support.AWSSupportAsyncClient | software.amazon.awssdk.services.support.SupportAsyncClient |
| com.amazonaws.services.support.AWSSupportClient | software.amazon.awssdk.services.support.SupportClient |
| com.amazonaws.services.transcribe.AmazonTranscribeAsyncClient | software.amazon.awssdk.services.transcribe.TranscribeAsyncClient |
| com.amazonaws.services.transcribe.AmazonTranscribeClient | software.amazon.awssdk.services.transcribe.TranscribeClient |
| com.amazonaws.services.translate.AmazonTranslateAsyncClient | software.amazon.awssdk.services.translate.TranslateAsyncClient |
| com.amazonaws.services.translate.AmazonTranslateClient | software.amazon.awssdk.services.translate.TranslateClient |
| com.amazonaws.services.waf.AWSWAFAsyncClient | software.amazon.awssdk.services.waf.WafAsyncClient |
| com.amazonaws.services.waf.AWSWAFClient | software.amazon.awssdk.services.waf.WafClient |
| com.amazonaws.services.waf.AWSWAFRegionalAsyncClient | software.amazon.awssdk.services.waf.regional.WafRegionalAsyncClient |
| com.amazonaws.services.waf.AWSWAFRegionalClient | software.amazon.awssdk.services.waf.regional.WafRegionalClient |
| com.amazonaws.services.workdocs.AmazonWorkDocsAsyncClient | software.amazon.awssdk.services.workdocs.WorkDocsAsyncClient |
| com.amazonaws.services.workdocs.AmazonWorkDocsClient | software.amazon.awssdk.services.workdocs.WorkDocsClient |
| com.amazonaws.services.workmail.AmazonWorkMailAsyncClient | software.amazon.awssdk.services.workmail.WorkMailAsyncClient |
| com.amazonaws.services.workmail.AmazonWorkMailClient | software.amazon.awssdk.services.workmail.WorkMailClient |
| com.amazonaws.services.workspaces.AmazonWorkspacesAsyncClient | software.amazon.awssdk.services.workspaces.WorkSpacesAsyncClient |
| com.amazonaws.services.workspaces.AmazonWorkspacesClient | software.amazon.awssdk.services.workspaces.WorkSpacesClient |
| com.amazonaws.services.xray.AWSXRayAsyncClient | software.amazon.awssdk.services.xray.XRayAsyncClient |
| com.amazonaws.services.xray.AWSXRayClient | software.amazon.awssdk.services.xray.XRayClient |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
