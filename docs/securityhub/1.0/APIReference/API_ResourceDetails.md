---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ResourceDetails.html
---

# ResourceDetails
<a name="API_ResourceDetails"></a>

Additional details about a resource related to a finding.

To provide the details, use the object that corresponds to the resource type. For example, if the resource type is `AwsEc2Instance`, then you use the `AwsEc2Instance` object to provide the details.

If the type-specific object does not contain all of the fields you want to populate, then you use the `Other` object to populate those additional fields.

You also use the `Other` object to populate the details when the selected type does not have a corresponding object.

## Contents
<a name="API_ResourceDetails_Contents"></a>

 ** AwsAmazonMqBroker **   <a name="securityhub-Type-ResourceDetails-AwsAmazonMqBroker"></a>
 Provides details about AWS AppSync message broker. A message broker allows software applications and components to communicate using various programming languages, operating systems, and formal messaging protocols.
Type: [AwsAmazonMqBrokerDetails](API_AwsAmazonMqBrokerDetails.md) object
Required: No

 ** AwsApiGatewayRestApi **   <a name="securityhub-Type-ResourceDetails-AwsApiGatewayRestApi"></a>
Provides information about a REST API in version 1 of Amazon API Gateway.
Type: [AwsApiGatewayRestApiDetails](API_AwsApiGatewayRestApiDetails.md) object
Required: No

 ** AwsApiGatewayStage **   <a name="securityhub-Type-ResourceDetails-AwsApiGatewayStage"></a>
Provides information about a version 1 Amazon API Gateway stage.
Type: [AwsApiGatewayStageDetails](API_AwsApiGatewayStageDetails.md) object
Required: No

 ** AwsApiGatewayV2Api **   <a name="securityhub-Type-ResourceDetails-AwsApiGatewayV2Api"></a>
Provides information about a version 2 API in Amazon API Gateway.
Type: [AwsApiGatewayV2ApiDetails](API_AwsApiGatewayV2ApiDetails.md) object
Required: No

 ** AwsApiGatewayV2Stage **   <a name="securityhub-Type-ResourceDetails-AwsApiGatewayV2Stage"></a>
Provides information about a version 2 stage for Amazon API Gateway.
Type: [AwsApiGatewayV2StageDetails](API_AwsApiGatewayV2StageDetails.md) object
Required: No

 ** AwsAppSyncGraphQlApi **   <a name="securityhub-Type-ResourceDetails-AwsAppSyncGraphQlApi"></a>
 Provides details about an AWS AppSync Graph QL API, which lets you query multiple databases, microservices, and APIs from a single GraphQL endpoint.
Type: [AwsAppSyncGraphQlApiDetails](API_AwsAppSyncGraphQlApiDetails.md) object
Required: No

 ** AwsAthenaWorkGroup **   <a name="securityhub-Type-ResourceDetails-AwsAthenaWorkGroup"></a>
 Provides information about an Amazon Athena workgroup. A workgroup helps you separate users, teams, applications, or workloads. It also helps you set limits on data processing and track costs.
Type: [AwsAthenaWorkGroupDetails](API_AwsAthenaWorkGroupDetails.md) object
Required: No

 ** AwsAutoScalingAutoScalingGroup **   <a name="securityhub-Type-ResourceDetails-AwsAutoScalingAutoScalingGroup"></a>
Details for an autoscaling group.
Type: [AwsAutoScalingAutoScalingGroupDetails](API_AwsAutoScalingAutoScalingGroupDetails.md) object
Required: No

 ** AwsAutoScalingLaunchConfiguration **   <a name="securityhub-Type-ResourceDetails-AwsAutoScalingLaunchConfiguration"></a>
Provides details about a launch configuration.
Type: [AwsAutoScalingLaunchConfigurationDetails](API_AwsAutoScalingLaunchConfigurationDetails.md) object
Required: No

 ** AwsBackupBackupPlan **   <a name="securityhub-Type-ResourceDetails-AwsBackupBackupPlan"></a>
Provides details about an AWS Backup backup plan.
Type: [AwsBackupBackupPlanDetails](API_AwsBackupBackupPlanDetails.md) object
Required: No

 ** AwsBackupBackupVault **   <a name="securityhub-Type-ResourceDetails-AwsBackupBackupVault"></a>
Provides details about an AWS Backup backup vault.
Type: [AwsBackupBackupVaultDetails](API_AwsBackupBackupVaultDetails.md) object
Required: No

 ** AwsBackupRecoveryPoint **   <a name="securityhub-Type-ResourceDetails-AwsBackupRecoveryPoint"></a>
Provides details about an AWS Backup backup, or recovery point.
Type: [AwsBackupRecoveryPointDetails](API_AwsBackupRecoveryPointDetails.md) object
Required: No

 ** AwsCertificateManagerCertificate **   <a name="securityhub-Type-ResourceDetails-AwsCertificateManagerCertificate"></a>
Provides details about an AWS Certificate Manager certificate.
Type: [AwsCertificateManagerCertificateDetails](API_AwsCertificateManagerCertificateDetails.md) object
Required: No

 ** AwsCloudFormationStack **   <a name="securityhub-Type-ResourceDetails-AwsCloudFormationStack"></a>
Details about an CloudFormation stack. A stack is a collection of AWS resources that you can manage as a single unit.
Type: [AwsCloudFormationStackDetails](API_AwsCloudFormationStackDetails.md) object
Required: No

 ** AwsCloudFrontDistribution **   <a name="securityhub-Type-ResourceDetails-AwsCloudFrontDistribution"></a>
Details about a CloudFront distribution.
Type: [AwsCloudFrontDistributionDetails](API_AwsCloudFrontDistributionDetails.md) object
Required: No

 ** AwsCloudTrailTrail **   <a name="securityhub-Type-ResourceDetails-AwsCloudTrailTrail"></a>
Provides details about a CloudTrail trail.
Type: [AwsCloudTrailTrailDetails](API_AwsCloudTrailTrailDetails.md) object
Required: No

 ** AwsCloudWatchAlarm **   <a name="securityhub-Type-ResourceDetails-AwsCloudWatchAlarm"></a>
Details about an Amazon CloudWatch alarm. An alarm allows you to monitor and receive alerts about your AWS resources and applications across multiple Regions.
Type: [AwsCloudWatchAlarmDetails](API_AwsCloudWatchAlarmDetails.md) object
Required: No

 ** AwsCodeBuildProject **   <a name="securityhub-Type-ResourceDetails-AwsCodeBuildProject"></a>
Details for an AWS CodeBuild project.
Type: [AwsCodeBuildProjectDetails](API_AwsCodeBuildProjectDetails.md) object
Required: No

 ** AwsDmsEndpoint **   <a name="securityhub-Type-ResourceDetails-AwsDmsEndpoint"></a>
 Provides details about an AWS Database Migration Service (AWS DMS) endpoint. An endpoint provides connection, data store type, and location information about your data store.
Type: [AwsDmsEndpointDetails](API_AwsDmsEndpointDetails.md) object
Required: No

 ** AwsDmsReplicationInstance **   <a name="securityhub-Type-ResourceDetails-AwsDmsReplicationInstance"></a>
 Provides details about an AWS DMS replication instance. DMS uses a replication instance to connect to your source data store, read the source data, and format the data for consumption by the target data store.
Type: [AwsDmsReplicationInstanceDetails](API_AwsDmsReplicationInstanceDetails.md) object
Required: No

 ** AwsDmsReplicationTask **   <a name="securityhub-Type-ResourceDetails-AwsDmsReplicationTask"></a>
 Provides details about an AWS DMS replication task. A replication task moves a set of data from the source endpoint to the target endpoint.
Type: [AwsDmsReplicationTaskDetails](API_AwsDmsReplicationTaskDetails.md) object
Required: No

 ** AwsDynamoDbTable **   <a name="securityhub-Type-ResourceDetails-AwsDynamoDbTable"></a>
Details about a DynamoDB table.
Type: [AwsDynamoDbTableDetails](API_AwsDynamoDbTableDetails.md) object
Required: No

 ** AwsEc2ClientVpnEndpoint **   <a name="securityhub-Type-ResourceDetails-AwsEc2ClientVpnEndpoint"></a>
 Provides details about an AWS Client VPN endpoint. A Client VPN endpoint is the resource that you create and configure to enable and manage client VPN sessions. It's the termination point for all client VPN sessions.
Type: [AwsEc2ClientVpnEndpointDetails](API_AwsEc2ClientVpnEndpointDetails.md) object
Required: No

 ** AwsEc2Eip **   <a name="securityhub-Type-ResourceDetails-AwsEc2Eip"></a>
Details about an Elastic IP address.
Type: [AwsEc2EipDetails](API_AwsEc2EipDetails.md) object
Required: No

 ** AwsEc2Instance **   <a name="securityhub-Type-ResourceDetails-AwsEc2Instance"></a>
Details about an EC2 instance related to a finding.
Type: [AwsEc2InstanceDetails](API_AwsEc2InstanceDetails.md) object
Required: No

 ** AwsEc2LaunchTemplate **   <a name="securityhub-Type-ResourceDetails-AwsEc2LaunchTemplate"></a>
 Specifies the properties for creating an Amazon Elastic Compute Cloud (Amazon EC2) launch template.
Type: [AwsEc2LaunchTemplateDetails](API_AwsEc2LaunchTemplateDetails.md) object
Required: No

 ** AwsEc2NetworkAcl **   <a name="securityhub-Type-ResourceDetails-AwsEc2NetworkAcl"></a>
Details about an EC2 network access control list (ACL).
Type: [AwsEc2NetworkAclDetails](API_AwsEc2NetworkAclDetails.md) object
Required: No

 ** AwsEc2NetworkInterface **   <a name="securityhub-Type-ResourceDetails-AwsEc2NetworkInterface"></a>
Details for an EC2 network interface.
Type: [AwsEc2NetworkInterfaceDetails](API_AwsEc2NetworkInterfaceDetails.md) object
Required: No

 ** AwsEc2RouteTable **   <a name="securityhub-Type-ResourceDetails-AwsEc2RouteTable"></a>
 Provides details about a route table. A route table contains a set of rules, called routes, that determine where to direct network traffic from your subnet or gateway.
Type: [AwsEc2RouteTableDetails](API_AwsEc2RouteTableDetails.md) object
Required: No

 ** AwsEc2SecurityGroup **   <a name="securityhub-Type-ResourceDetails-AwsEc2SecurityGroup"></a>
Details for an EC2 security group.
Type: [AwsEc2SecurityGroupDetails](API_AwsEc2SecurityGroupDetails.md) object
Required: No

 ** AwsEc2Subnet **   <a name="securityhub-Type-ResourceDetails-AwsEc2Subnet"></a>
Details about a subnet in Amazon EC2.
Type: [AwsEc2SubnetDetails](API_AwsEc2SubnetDetails.md) object
Required: No

 ** AwsEc2TransitGateway **   <a name="securityhub-Type-ResourceDetails-AwsEc2TransitGateway"></a>
Details about an Amazon EC2 transit gateway that interconnects your virtual private clouds (VPC) and on-premises networks.
Type: [AwsEc2TransitGatewayDetails](API_AwsEc2TransitGatewayDetails.md) object
Required: No

 ** AwsEc2Volume **   <a name="securityhub-Type-ResourceDetails-AwsEc2Volume"></a>
Details for an Amazon EC2 volume.
Type: [AwsEc2VolumeDetails](API_AwsEc2VolumeDetails.md) object
Required: No

 ** AwsEc2Vpc **   <a name="securityhub-Type-ResourceDetails-AwsEc2Vpc"></a>
Details for an Amazon EC2 VPC.
Type: [AwsEc2VpcDetails](API_AwsEc2VpcDetails.md) object
Required: No

 ** AwsEc2VpcEndpointService **   <a name="securityhub-Type-ResourceDetails-AwsEc2VpcEndpointService"></a>
Details about the service configuration for a VPC endpoint service.
Type: [AwsEc2VpcEndpointServiceDetails](API_AwsEc2VpcEndpointServiceDetails.md) object
Required: No

 ** AwsEc2VpcPeeringConnection **   <a name="securityhub-Type-ResourceDetails-AwsEc2VpcPeeringConnection"></a>
Details about an Amazon EC2 VPC peering connection. A VPC peering connection is a networking connection between two VPCs that enables you to route traffic between them privately.
Type: [AwsEc2VpcPeeringConnectionDetails](API_AwsEc2VpcPeeringConnectionDetails.md) object
Required: No

 ** AwsEc2VpnConnection **   <a name="securityhub-Type-ResourceDetails-AwsEc2VpnConnection"></a>
Details about an Amazon EC2 VPN connection.
Type: [AwsEc2VpnConnectionDetails](API_AwsEc2VpnConnectionDetails.md) object
Required: No

 ** AwsEcrContainerImage **   <a name="securityhub-Type-ResourceDetails-AwsEcrContainerImage"></a>
Information about an Amazon ECR image.
Type: [AwsEcrContainerImageDetails](API_AwsEcrContainerImageDetails.md) object
Required: No

 ** AwsEcrRepository **   <a name="securityhub-Type-ResourceDetails-AwsEcrRepository"></a>
Information about an Amazon Elastic Container Registry repository.
Type: [AwsEcrRepositoryDetails](API_AwsEcrRepositoryDetails.md) object
Required: No

 ** AwsEcsCluster **   <a name="securityhub-Type-ResourceDetails-AwsEcsCluster"></a>
Details about an Amazon ECS cluster.
Type: [AwsEcsClusterDetails](API_AwsEcsClusterDetails.md) object
Required: No

 ** AwsEcsContainer **   <a name="securityhub-Type-ResourceDetails-AwsEcsContainer"></a>
Provides information about a Docker container that's part of a task.
Type: [AwsEcsContainerDetails](API_AwsEcsContainerDetails.md) object
Required: No

 ** AwsEcsService **   <a name="securityhub-Type-ResourceDetails-AwsEcsService"></a>
Details about a service within an ECS cluster.
Type: [AwsEcsServiceDetails](API_AwsEcsServiceDetails.md) object
Required: No

 ** AwsEcsTask **   <a name="securityhub-Type-ResourceDetails-AwsEcsTask"></a>
Details about a task in a cluster.
Type: [AwsEcsTaskDetails](API_AwsEcsTaskDetails.md) object
Required: No

 ** AwsEcsTaskDefinition **   <a name="securityhub-Type-ResourceDetails-AwsEcsTaskDefinition"></a>
Details about a task definition. A task definition describes the container and volume definitions of an Amazon Elastic Container Service task.
Type: [AwsEcsTaskDefinitionDetails](API_AwsEcsTaskDefinitionDetails.md) object
Required: No

 ** AwsEfsAccessPoint **   <a name="securityhub-Type-ResourceDetails-AwsEfsAccessPoint"></a>
Details about an Amazon EFS access point. An access point is an application-specific view into an EFS file system that applies an operating system user and group, and a file system path, to any file system request made through the access point.
Type: [AwsEfsAccessPointDetails](API_AwsEfsAccessPointDetails.md) object
Required: No

 ** AwsEksCluster **   <a name="securityhub-Type-ResourceDetails-AwsEksCluster"></a>
Details about an Amazon EKS cluster.
Type: [AwsEksClusterDetails](API_AwsEksClusterDetails.md) object
Required: No

 ** AwsElasticBeanstalkEnvironment **   <a name="securityhub-Type-ResourceDetails-AwsElasticBeanstalkEnvironment"></a>
Details about an Elastic Beanstalk environment.
Type: [AwsElasticBeanstalkEnvironmentDetails](API_AwsElasticBeanstalkEnvironmentDetails.md) object
Required: No

 ** AwsElasticsearchDomain **   <a name="securityhub-Type-ResourceDetails-AwsElasticsearchDomain"></a>
Details for an Elasticsearch domain.
Type: [AwsElasticsearchDomainDetails](API_AwsElasticsearchDomainDetails.md) object
Required: No

 ** AwsElbLoadBalancer **   <a name="securityhub-Type-ResourceDetails-AwsElbLoadBalancer"></a>
Contains details about a Classic Load Balancer.
Type: [AwsElbLoadBalancerDetails](API_AwsElbLoadBalancerDetails.md) object
Required: No

 ** AwsElbv2LoadBalancer **   <a name="securityhub-Type-ResourceDetails-AwsElbv2LoadBalancer"></a>
Details about a load balancer.
Type: [AwsElbv2LoadBalancerDetails](API_AwsElbv2LoadBalancerDetails.md) object
Required: No

 ** AwsEventSchemasRegistry **   <a name="securityhub-Type-ResourceDetails-AwsEventSchemasRegistry"></a>
 A schema defines the structure of events that are sent to Amazon EventBridge. Schema registries are containers for schemas. They collect and organize schemas so that your schemas are in logical groups.
Type: [AwsEventSchemasRegistryDetails](API_AwsEventSchemasRegistryDetails.md) object
Required: No

 ** AwsEventsEndpoint **   <a name="securityhub-Type-ResourceDetails-AwsEventsEndpoint"></a>
 Provides details about an Amazon EventBridge global endpoint. The endpoint can improve your application’s availability by making it Regional-fault tolerant.
Type: [AwsEventsEndpointDetails](API_AwsEventsEndpointDetails.md) object
Required: No

 ** AwsEventsEventbus **   <a name="securityhub-Type-ResourceDetails-AwsEventsEventbus"></a>
 Provides details about Amazon EventBridge event bus for an endpoint. An event bus is a router that receives events and delivers them to zero or more destinations, or targets.
Type: [AwsEventsEventbusDetails](API_AwsEventsEventbusDetails.md) object
Required: No

 ** AwsGuardDutyDetector **   <a name="securityhub-Type-ResourceDetails-AwsGuardDutyDetector"></a>
 Provides details about an Amazon GuardDuty detector. A detector is an object that represents the GuardDuty service. A detector is required for GuardDuty to become operational.
Type: [AwsGuardDutyDetectorDetails](API_AwsGuardDutyDetectorDetails.md) object
Required: No

 ** AwsIamAccessKey **   <a name="securityhub-Type-ResourceDetails-AwsIamAccessKey"></a>
Details about an IAM access key related to a finding.
Type: [AwsIamAccessKeyDetails](API_AwsIamAccessKeyDetails.md) object
Required: No

 ** AwsIamGroup **   <a name="securityhub-Type-ResourceDetails-AwsIamGroup"></a>
Contains details about an IAM group.
Type: [AwsIamGroupDetails](API_AwsIamGroupDetails.md) object
Required: No

 ** AwsIamPolicy **   <a name="securityhub-Type-ResourceDetails-AwsIamPolicy"></a>
Details about an IAM permissions policy.
Type: [AwsIamPolicyDetails](API_AwsIamPolicyDetails.md) object
Required: No

 ** AwsIamRole **   <a name="securityhub-Type-ResourceDetails-AwsIamRole"></a>
Details about an IAM role.
Type: [AwsIamRoleDetails](API_AwsIamRoleDetails.md) object
Required: No

 ** AwsIamUser **   <a name="securityhub-Type-ResourceDetails-AwsIamUser"></a>
Details about an IAM user.
Type: [AwsIamUserDetails](API_AwsIamUserDetails.md) object
Required: No

 ** AwsKinesisStream **   <a name="securityhub-Type-ResourceDetails-AwsKinesisStream"></a>
Details about an Amazon Kinesis data stream.
Type: [AwsKinesisStreamDetails](API_AwsKinesisStreamDetails.md) object
Required: No

 ** AwsKmsKey **   <a name="securityhub-Type-ResourceDetails-AwsKmsKey"></a>
Details about an AWS KMS key.
Type: [AwsKmsKeyDetails](API_AwsKmsKeyDetails.md) object
Required: No

 ** AwsLambdaFunction **   <a name="securityhub-Type-ResourceDetails-AwsLambdaFunction"></a>
Details about a Lambda function.
Type: [AwsLambdaFunctionDetails](API_AwsLambdaFunctionDetails.md) object
Required: No

 ** AwsLambdaLayerVersion **   <a name="securityhub-Type-ResourceDetails-AwsLambdaLayerVersion"></a>
Details for a Lambda layer version.
Type: [AwsLambdaLayerVersionDetails](API_AwsLambdaLayerVersionDetails.md) object
Required: No

 ** AwsMskCluster **   <a name="securityhub-Type-ResourceDetails-AwsMskCluster"></a>
 Provides details about an Amazon Managed Streaming for Apache Kafka (Amazon MSK) cluster.
Type: [AwsMskClusterDetails](API_AwsMskClusterDetails.md) object
Required: No

 ** AwsNetworkFirewallFirewall **   <a name="securityhub-Type-ResourceDetails-AwsNetworkFirewallFirewall"></a>
Details about an AWS Network Firewall firewall.
Type: [AwsNetworkFirewallFirewallDetails](API_AwsNetworkFirewallFirewallDetails.md) object
Required: No

 ** AwsNetworkFirewallFirewallPolicy **   <a name="securityhub-Type-ResourceDetails-AwsNetworkFirewallFirewallPolicy"></a>
Details about an AWS Network Firewall firewall policy.
Type: [AwsNetworkFirewallFirewallPolicyDetails](API_AwsNetworkFirewallFirewallPolicyDetails.md) object
Required: No

 ** AwsNetworkFirewallRuleGroup **   <a name="securityhub-Type-ResourceDetails-AwsNetworkFirewallRuleGroup"></a>
Details about an AWS Network Firewall rule group.
Type: [AwsNetworkFirewallRuleGroupDetails](API_AwsNetworkFirewallRuleGroupDetails.md) object
Required: No

 ** AwsOpenSearchServiceDomain **   <a name="securityhub-Type-ResourceDetails-AwsOpenSearchServiceDomain"></a>
Details about an Amazon OpenSearch Service domain.
Type: [AwsOpenSearchServiceDomainDetails](API_AwsOpenSearchServiceDomainDetails.md) object
Required: No

 ** AwsRdsDbCluster **   <a name="securityhub-Type-ResourceDetails-AwsRdsDbCluster"></a>
Details about an Amazon RDS database cluster.
Type: [AwsRdsDbClusterDetails](API_AwsRdsDbClusterDetails.md) object
Required: No

 ** AwsRdsDbClusterSnapshot **   <a name="securityhub-Type-ResourceDetails-AwsRdsDbClusterSnapshot"></a>
Details about an Amazon RDS database cluster snapshot.
Type: [AwsRdsDbClusterSnapshotDetails](API_AwsRdsDbClusterSnapshotDetails.md) object
Required: No

 ** AwsRdsDbInstance **   <a name="securityhub-Type-ResourceDetails-AwsRdsDbInstance"></a>
Details about an Amazon RDS database instance.
Type: [AwsRdsDbInstanceDetails](API_AwsRdsDbInstanceDetails.md) object
Required: No

 ** AwsRdsDbSecurityGroup **   <a name="securityhub-Type-ResourceDetails-AwsRdsDbSecurityGroup"></a>
Details about an Amazon RDS DB security group.
Type: [AwsRdsDbSecurityGroupDetails](API_AwsRdsDbSecurityGroupDetails.md) object
Required: No

 ** AwsRdsDbSnapshot **   <a name="securityhub-Type-ResourceDetails-AwsRdsDbSnapshot"></a>
Details about an Amazon RDS database snapshot.
Type: [AwsRdsDbSnapshotDetails](API_AwsRdsDbSnapshotDetails.md) object
Required: No

 ** AwsRdsEventSubscription **   <a name="securityhub-Type-ResourceDetails-AwsRdsEventSubscription"></a>
Details about an RDS event notification subscription.
Type: [AwsRdsEventSubscriptionDetails](API_AwsRdsEventSubscriptionDetails.md) object
Required: No

 ** AwsRedshiftCluster **   <a name="securityhub-Type-ResourceDetails-AwsRedshiftCluster"></a>
Contains details about an Amazon Redshift cluster.
Type: [AwsRedshiftClusterDetails](API_AwsRedshiftClusterDetails.md) object
Required: No

 ** AwsRoute53HostedZone **   <a name="securityhub-Type-ResourceDetails-AwsRoute53HostedZone"></a>
 Provides details about an Amazon Route 53 hosted zone, including the four name servers assigned to the hosted zone. A hosted zone represents a collection of records that can be managed together, belonging to a single parent domain name.
Type: [AwsRoute53HostedZoneDetails](API_AwsRoute53HostedZoneDetails.md) object
Required: No

 ** AwsS3AccessPoint **   <a name="securityhub-Type-ResourceDetails-AwsS3AccessPoint"></a>
 Provides details about an Amazon Simple Storage Service (Amazon S3) access point. S3 access points are named network endpoints that are attached to S3 buckets that you can use to perform S3 object operations.
Type: [AwsS3AccessPointDetails](API_AwsS3AccessPointDetails.md) object
Required: No

 ** AwsS3AccountPublicAccessBlock **   <a name="securityhub-Type-ResourceDetails-AwsS3AccountPublicAccessBlock"></a>
Details about the Amazon S3 Public Access Block configuration for an account.
Type: [AwsS3AccountPublicAccessBlockDetails](API_AwsS3AccountPublicAccessBlockDetails.md) object
Required: No

 ** AwsS3Bucket **   <a name="securityhub-Type-ResourceDetails-AwsS3Bucket"></a>
Details about an S3 bucket related to a finding.
Type: [AwsS3BucketDetails](API_AwsS3BucketDetails.md) object
Required: No

 ** AwsS3Object **   <a name="securityhub-Type-ResourceDetails-AwsS3Object"></a>
Details about an S3 object related to a finding.
Type: [AwsS3ObjectDetails](API_AwsS3ObjectDetails.md) object
Required: No

 ** AwsSageMakerNotebookInstance **   <a name="securityhub-Type-ResourceDetails-AwsSageMakerNotebookInstance"></a>
 Provides details about an Amazon SageMaker AI notebook instance.
Type: [AwsSageMakerNotebookInstanceDetails](API_AwsSageMakerNotebookInstanceDetails.md) object
Required: No

 ** AwsSecretsManagerSecret **   <a name="securityhub-Type-ResourceDetails-AwsSecretsManagerSecret"></a>
Details about a Secrets Manager secret.
Type: [AwsSecretsManagerSecretDetails](API_AwsSecretsManagerSecretDetails.md) object
Required: No

 ** AwsSnsTopic **   <a name="securityhub-Type-ResourceDetails-AwsSnsTopic"></a>
Details about an SNS topic.
Type: [AwsSnsTopicDetails](API_AwsSnsTopicDetails.md) object
Required: No

 ** AwsSqsQueue **   <a name="securityhub-Type-ResourceDetails-AwsSqsQueue"></a>
Details about an SQS queue.
Type: [AwsSqsQueueDetails](API_AwsSqsQueueDetails.md) object
Required: No

 ** AwsSsmPatchCompliance **   <a name="securityhub-Type-ResourceDetails-AwsSsmPatchCompliance"></a>
Provides information about the state of a patch on an instance based on the patch baseline that was used to patch the instance.
Type: [AwsSsmPatchComplianceDetails](API_AwsSsmPatchComplianceDetails.md) object
Required: No

 ** AwsStepFunctionStateMachine **   <a name="securityhub-Type-ResourceDetails-AwsStepFunctionStateMachine"></a>
 Provides details about an AWS Step Functions state machine, which is a workflow consisting of a series of event-driven steps.
Type: [AwsStepFunctionStateMachineDetails](API_AwsStepFunctionStateMachineDetails.md) object
Required: No

 ** AwsWafRateBasedRule **   <a name="securityhub-Type-ResourceDetails-AwsWafRateBasedRule"></a>
Details about a rate-based rule for global resources.
Type: [AwsWafRateBasedRuleDetails](API_AwsWafRateBasedRuleDetails.md) object
Required: No

 ** AwsWafRegionalRateBasedRule **   <a name="securityhub-Type-ResourceDetails-AwsWafRegionalRateBasedRule"></a>
Details about a rate-based rule for Regional resources.
Type: [AwsWafRegionalRateBasedRuleDetails](API_AwsWafRegionalRateBasedRuleDetails.md) object
Required: No

 ** AwsWafRegionalRule **   <a name="securityhub-Type-ResourceDetails-AwsWafRegionalRule"></a>
Details about an AWS WAF rule for Regional resources.
Type: [AwsWafRegionalRuleDetails](API_AwsWafRegionalRuleDetails.md) object
Required: No

 ** AwsWafRegionalRuleGroup **   <a name="securityhub-Type-ResourceDetails-AwsWafRegionalRuleGroup"></a>
Details about an AWS WAF rule group for Regional resources.
Type: [AwsWafRegionalRuleGroupDetails](API_AwsWafRegionalRuleGroupDetails.md) object
Required: No

 ** AwsWafRegionalWebAcl **   <a name="securityhub-Type-ResourceDetails-AwsWafRegionalWebAcl"></a>
Details about an AWS WAF web access control list (web ACL) for Regional resources.
Type: [AwsWafRegionalWebAclDetails](API_AwsWafRegionalWebAclDetails.md) object
Required: No

 ** AwsWafRule **   <a name="securityhub-Type-ResourceDetails-AwsWafRule"></a>
Details about an AWS WAF rule for global resources.
Type: [AwsWafRuleDetails](API_AwsWafRuleDetails.md) object
Required: No

 ** AwsWafRuleGroup **   <a name="securityhub-Type-ResourceDetails-AwsWafRuleGroup"></a>
Details about an AWS WAF rule group for global resources.
Type: [AwsWafRuleGroupDetails](API_AwsWafRuleGroupDetails.md) object
Required: No

 ** AwsWafv2RuleGroup **   <a name="securityhub-Type-ResourceDetails-AwsWafv2RuleGroup"></a>
 Details about an AWS WAFv2 rule group.
Type: [AwsWafv2RuleGroupDetails](API_AwsWafv2RuleGroupDetails.md) object
Required: No

 ** AwsWafv2WebAcl **   <a name="securityhub-Type-ResourceDetails-AwsWafv2WebAcl"></a>
 Details about an AWS WAFv2 web Access Control List (ACL).
Type: [AwsWafv2WebAclDetails](API_AwsWafv2WebAclDetails.md) object
Required: No

 ** AwsWafWebAcl **   <a name="securityhub-Type-ResourceDetails-AwsWafWebAcl"></a>
Details for an AWS WAF web ACL.
Type: [AwsWafWebAclDetails](API_AwsWafWebAclDetails.md) object
Required: No

 ** AwsXrayEncryptionConfig **   <a name="securityhub-Type-ResourceDetails-AwsXrayEncryptionConfig"></a>
Information about the encryption configuration for AWS X-Ray.
Type: [AwsXrayEncryptionConfigDetails](API_AwsXrayEncryptionConfigDetails.md) object
Required: No

 ** AzureResource **   <a name="securityhub-Type-ResourceDetails-AzureResource"></a>
Details about an Azure resource that is related to a finding.
Type: JSON value
Required: No

 ** CodeRepository **   <a name="securityhub-Type-ResourceDetails-CodeRepository"></a>
 Details about an external code repository with which you can connect your AWS resources. The connection is established through Amazon Inspector.
Type: [CodeRepositoryDetails](API_CodeRepositoryDetails.md) object
Required: No

 ** Container **   <a name="securityhub-Type-ResourceDetails-Container"></a>
Details about a container resource related to a finding.
Type: [ContainerDetails](API_ContainerDetails.md) object
Required: No

 ** Other **   <a name="securityhub-Type-ResourceDetails-Other"></a>
Details about a resource that are not available in a type-specific details object. Use the `Other` object in the following cases.
+ The type-specific object does not contain all of the fields that you want to populate. In this case, first use the type-specific object to populate those fields. Use the `Other` object to populate the fields that are missing from the type-specific object.
+ The resource type does not have a corresponding object. This includes resources for which the type is `Other`.
Type: String to string map
Key Pattern: `.*\S.*`
Value Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_ResourceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ResourceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ResourceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ResourceDetails)
