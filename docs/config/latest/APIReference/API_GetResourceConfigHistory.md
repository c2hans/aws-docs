---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_GetResourceConfigHistory.html
---

# GetResourceConfigHistory

**Important**
For accurate reporting on the compliance status, you must record the `AWS::Config::ResourceCompliance` resource type.
For more information, see [Recording AWS Resources](https://docs.aws.amazon.com/config/latest/developerguide/select-resources.html) in the * AWS Config Resources Developer Guide*.

Returns a list of configurations items (CIs) for the specified resource.

 **Contents**

The list contains details about each state of the resource during the specified time interval. If you specified a retention period to retain your CIs between a minimum of 30 days and a maximum of 7 years (2557 days), AWS Config returns the CIs for the specified retention period.

 **Pagination**

The response is paginated. By default, AWS Config returns a limit of 10 configuration items per page. You can customize this number with the `limit` parameter. The response includes a `nextToken` string. To get the next page of results, run the request again and specify the string for the `nextToken` parameter.

**Note**
Each call to the API is limited to span a duration of seven days. It is likely that the number of records returned is smaller than the specified `limit`. In such cases, you can make another call, using the `nextToken`.

## Request Syntax
<a name="API_GetResourceConfigHistory_RequestSyntax"></a>

```
{
   "chronologicalOrder": "{{string}}",
   "earlierTime": {{number}},
   "laterTime": {{number}},
   "limit": {{number}},
   "nextToken": "{{string}}",
   "resourceId": "{{string}}",
   "resourceType": "{{string}}"
}
```

## Request Parameters
<a name="API_GetResourceConfigHistory_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [chronologicalOrder](#API_GetResourceConfigHistory_RequestSyntax) **   <a name="config-GetResourceConfigHistory-request-chronologicalOrder"></a>
The chronological order for configuration items listed. By default, the results are listed in reverse chronological order.
Type: String
Valid Values: `Reverse | Forward`
Required: No

 ** [earlierTime](#API_GetResourceConfigHistory_RequestSyntax) **   <a name="config-GetResourceConfigHistory-request-earlierTime"></a>
The chronologically earliest time in the time range for which the history requested. If not specified, the action returns paginated results that contain configuration items that start when the first configuration item was recorded.
Type: Timestamp
Required: No

 ** [laterTime](#API_GetResourceConfigHistory_RequestSyntax) **   <a name="config-GetResourceConfigHistory-request-laterTime"></a>
The chronologically latest time in the time range for which the history requested. If not specified, current time is taken.
Type: Timestamp
Required: No

 ** [limit](#API_GetResourceConfigHistory_RequestSyntax) **   <a name="config-GetResourceConfigHistory-request-limit"></a>
The maximum number of configuration items returned on each page. The default is 10. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [nextToken](#API_GetResourceConfigHistory_RequestSyntax) **   <a name="config-GetResourceConfigHistory-request-nextToken"></a>
The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String
Required: No

 ** [resourceId](#API_GetResourceConfigHistory_RequestSyntax) **   <a name="config-GetResourceConfigHistory-request-resourceId"></a>
The ID of the resource (for example., `sg-xxxxxx`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 768.
Required: Yes

 ** [resourceType](#API_GetResourceConfigHistory_RequestSyntax) **   <a name="config-GetResourceConfigHistory-request-resourceType"></a>
The resource type.
Type: String
Valid Values: `AWS::EC2::CustomerGateway | AWS::EC2::EIP | AWS::EC2::Host | AWS::EC2::Instance | AWS::EC2::InternetGateway | AWS::EC2::NetworkAcl | AWS::EC2::NetworkInterface | AWS::EC2::RouteTable | AWS::EC2::SecurityGroup | AWS::EC2::Subnet | AWS::CloudTrail::Trail | AWS::EC2::Volume | AWS::EC2::VPC | AWS::EC2::VPNConnection | AWS::EC2::VPNGateway | AWS::EC2::RegisteredHAInstance | AWS::EC2::NatGateway | AWS::EC2::EgressOnlyInternetGateway | AWS::EC2::VPCEndpoint | AWS::EC2::VPCEndpointService | AWS::EC2::FlowLog | AWS::EC2::VPCPeeringConnection | AWS::Elasticsearch::Domain | AWS::IAM::Group | AWS::IAM::Policy | AWS::IAM::Role | AWS::IAM::User | AWS::ElasticLoadBalancingV2::LoadBalancer | AWS::ACM::Certificate | AWS::RDS::DBInstance | AWS::RDS::DBSubnetGroup | AWS::RDS::DBSecurityGroup | AWS::RDS::DBSnapshot | AWS::RDS::DBCluster | AWS::RDS::DBClusterSnapshot | AWS::RDS::EventSubscription | AWS::S3::Bucket | AWS::S3::AccountPublicAccessBlock | AWS::Redshift::Cluster | AWS::Redshift::ClusterSnapshot | AWS::Redshift::ClusterParameterGroup | AWS::Redshift::ClusterSecurityGroup | AWS::Redshift::ClusterSubnetGroup | AWS::Redshift::EventSubscription | AWS::SSM::ManagedInstanceInventory | AWS::CloudWatch::Alarm | AWS::CloudFormation::Stack | AWS::ElasticLoadBalancing::LoadBalancer | AWS::AutoScaling::AutoScalingGroup | AWS::AutoScaling::LaunchConfiguration | AWS::AutoScaling::ScalingPolicy | AWS::AutoScaling::ScheduledAction | AWS::DynamoDB::Table | AWS::CodeBuild::Project | AWS::WAF::RateBasedRule | AWS::WAF::Rule | AWS::WAF::RuleGroup | AWS::WAF::WebACL | AWS::WAFRegional::RateBasedRule | AWS::WAFRegional::Rule | AWS::WAFRegional::RuleGroup | AWS::WAFRegional::WebACL | AWS::CloudFront::Distribution | AWS::CloudFront::StreamingDistribution | AWS::Lambda::Function | AWS::NetworkFirewall::Firewall | AWS::NetworkFirewall::FirewallPolicy | AWS::NetworkFirewall::RuleGroup | AWS::ElasticBeanstalk::Application | AWS::ElasticBeanstalk::ApplicationVersion | AWS::ElasticBeanstalk::Environment | AWS::WAFv2::WebACL | AWS::WAFv2::RuleGroup | AWS::WAFv2::IPSet | AWS::WAFv2::RegexPatternSet | AWS::WAFv2::ManagedRuleSet | AWS::XRay::EncryptionConfig | AWS::SSM::AssociationCompliance | AWS::SSM::PatchCompliance | AWS::Shield::Protection | AWS::ShieldRegional::Protection | AWS::Config::ConformancePackCompliance | AWS::Config::ResourceCompliance | AWS::ApiGateway::Stage | AWS::ApiGateway::RestApi | AWS::ApiGatewayV2::Stage | AWS::ApiGatewayV2::Api | AWS::CodePipeline::Pipeline | AWS::ServiceCatalog::CloudFormationProvisionedProduct | AWS::ServiceCatalog::CloudFormationProduct | AWS::ServiceCatalog::Portfolio | AWS::SQS::Queue | AWS::KMS::Key | AWS::QLDB::Ledger | AWS::SecretsManager::Secret | AWS::SNS::Topic | AWS::SSM::FileData | AWS::Backup::BackupPlan | AWS::Backup::BackupSelection | AWS::Backup::BackupVault | AWS::Backup::RecoveryPoint | AWS::ECR::Repository | AWS::ECS::Cluster | AWS::ECS::Service | AWS::ECS::TaskDefinition | AWS::EFS::AccessPoint | AWS::EFS::FileSystem | AWS::EKS::Cluster | AWS::OpenSearch::Domain | AWS::EC2::TransitGateway | AWS::Kinesis::Stream | AWS::Kinesis::StreamConsumer | AWS::CodeDeploy::Application | AWS::CodeDeploy::DeploymentConfig | AWS::CodeDeploy::DeploymentGroup | AWS::EC2::LaunchTemplate | AWS::ECR::PublicRepository | AWS::GuardDuty::Detector | AWS::EMR::SecurityConfiguration | AWS::SageMaker::CodeRepository | AWS::Route53Resolver::ResolverEndpoint | AWS::Route53Resolver::ResolverRule | AWS::Route53Resolver::ResolverRuleAssociation | AWS::DMS::ReplicationSubnetGroup | AWS::DMS::EventSubscription | AWS::MSK::Cluster | AWS::StepFunctions::Activity | AWS::WorkSpaces::Workspace | AWS::WorkSpaces::ConnectionAlias | AWS::SageMaker::Model | AWS::ElasticLoadBalancingV2::Listener | AWS::StepFunctions::StateMachine | AWS::Batch::JobQueue | AWS::Batch::ComputeEnvironment | AWS::AccessAnalyzer::Analyzer | AWS::Athena::WorkGroup | AWS::Athena::DataCatalog | AWS::Detective::Graph | AWS::GlobalAccelerator::Accelerator | AWS::GlobalAccelerator::EndpointGroup | AWS::GlobalAccelerator::Listener | AWS::EC2::TransitGatewayAttachment | AWS::EC2::TransitGatewayRouteTable | AWS::DMS::Certificate | AWS::AppConfig::Application | AWS::AppSync::GraphQLApi | AWS::DataSync::LocationSMB | AWS::DataSync::LocationFSxLustre | AWS::DataSync::LocationS3 | AWS::DataSync::LocationEFS | AWS::DataSync::Task | AWS::DataSync::LocationNFS | AWS::EC2::NetworkInsightsAccessScopeAnalysis | AWS::EKS::FargateProfile | AWS::Glue::Job | AWS::GuardDuty::ThreatIntelSet | AWS::GuardDuty::IPSet | AWS::SageMaker::Workteam | AWS::SageMaker::NotebookInstanceLifecycleConfig | AWS::ServiceDiscovery::Service | AWS::ServiceDiscovery::PublicDnsNamespace | AWS::SES::ContactList | AWS::SES::ConfigurationSet | AWS::Route53::HostedZone | AWS::IoTEvents::Input | AWS::IoTEvents::DetectorModel | AWS::IoTEvents::AlarmModel | AWS::ServiceDiscovery::HttpNamespace | AWS::Events::EventBus | AWS::ImageBuilder::ContainerRecipe | AWS::ImageBuilder::DistributionConfiguration | AWS::ImageBuilder::InfrastructureConfiguration | AWS::DataSync::LocationObjectStorage | AWS::DataSync::LocationHDFS | AWS::Glue::Classifier | AWS::Route53RecoveryReadiness::Cell | AWS::Route53RecoveryReadiness::ReadinessCheck | AWS::ECR::RegistryPolicy | AWS::Backup::ReportPlan | AWS::Lightsail::Certificate | AWS::RUM::AppMonitor | AWS::Events::Endpoint | AWS::SES::ReceiptRuleSet | AWS::Events::Archive | AWS::Events::ApiDestination | AWS::Lightsail::Disk | AWS::FIS::ExperimentTemplate | AWS::DataSync::LocationFSxWindows | AWS::SES::ReceiptFilter | AWS::GuardDuty::Filter | AWS::SES::Template | AWS::AmazonMQ::Broker | AWS::AppConfig::Environment | AWS::AppConfig::ConfigurationProfile | AWS::Cloud9::EnvironmentEC2 | AWS::EventSchemas::Registry | AWS::EventSchemas::RegistryPolicy | AWS::EventSchemas::Discoverer | AWS::FraudDetector::Label | AWS::FraudDetector::EntityType | AWS::FraudDetector::Variable | AWS::FraudDetector::Outcome | AWS::IoT::Authorizer | AWS::IoT::SecurityProfile | AWS::IoT::RoleAlias | AWS::IoT::Dimension | AWS::IoTAnalytics::Datastore | AWS::Lightsail::Bucket | AWS::Lightsail::StaticIp | AWS::MediaPackage::PackagingGroup | AWS::Route53RecoveryReadiness::RecoveryGroup | AWS::ResilienceHub::ResiliencyPolicy | AWS::Transfer::Workflow | AWS::EKS::IdentityProviderConfig | AWS::EKS::Addon | AWS::Glue::MLTransform | AWS::IoT::Policy | AWS::IoT::MitigationAction | AWS::IoTTwinMaker::Workspace | AWS::IoTTwinMaker::Entity | AWS::IoTAnalytics::Dataset | AWS::IoTAnalytics::Pipeline | AWS::IoTAnalytics::Channel | AWS::IoTSiteWise::Dashboard | AWS::IoTSiteWise::Project | AWS::IoTSiteWise::Portal | AWS::IoTSiteWise::AssetModel | AWS::IVS::Channel | AWS::IVS::RecordingConfiguration | AWS::IVS::PlaybackKeyPair | AWS::KinesisAnalyticsV2::Application | AWS::RDS::GlobalCluster | AWS::S3::MultiRegionAccessPoint | AWS::DeviceFarm::TestGridProject | AWS::Budgets::BudgetsAction | AWS::Lex::Bot | AWS::CodeGuruReviewer::RepositoryAssociation | AWS::IoT::CustomMetric | AWS::Route53Resolver::FirewallDomainList | AWS::RoboMaker::RobotApplicationVersion | AWS::EC2::TrafficMirrorSession | AWS::IoTSiteWise::Gateway | AWS::Lex::BotAlias | AWS::LookoutMetrics::Alert | AWS::IoT::AccountAuditConfiguration | AWS::EC2::TrafficMirrorTarget | AWS::S3::StorageLens | AWS::IoT::ScheduledAudit | AWS::Events::Connection | AWS::EventSchemas::Schema | AWS::MediaPackage::PackagingConfiguration | AWS::KinesisVideo::SignalingChannel | AWS::AppStream::DirectoryConfig | AWS::LookoutVision::Project | AWS::Route53RecoveryControl::Cluster | AWS::Route53RecoveryControl::SafetyRule | AWS::Route53RecoveryControl::ControlPanel | AWS::Route53RecoveryControl::RoutingControl | AWS::Route53RecoveryReadiness::ResourceSet | AWS::RoboMaker::SimulationApplication | AWS::RoboMaker::RobotApplication | AWS::HealthLake::FHIRDatastore | AWS::Pinpoint::Segment | AWS::Pinpoint::ApplicationSettings | AWS::Events::Rule | AWS::EC2::DHCPOptions | AWS::EC2::NetworkInsightsPath | AWS::EC2::TrafficMirrorFilter | AWS::EC2::IPAM | AWS::IoTTwinMaker::Scene | AWS::NetworkManager::TransitGatewayRegistration | AWS::CustomerProfiles::Domain | AWS::AutoScaling::WarmPool | AWS::Connect::PhoneNumber | AWS::AppConfig::DeploymentStrategy | AWS::AppFlow::Flow | AWS::AuditManager::Assessment | AWS::CloudWatch::MetricStream | AWS::DeviceFarm::InstanceProfile | AWS::DeviceFarm::Project | AWS::EC2::EC2Fleet | AWS::EC2::SubnetRouteTableAssociation | AWS::ECR::PullThroughCacheRule | AWS::GroundStation::Config | AWS::ImageBuilder::ImagePipeline | AWS::IoT::FleetMetric | AWS::IoTWireless::ServiceProfile | AWS::NetworkManager::Device | AWS::NetworkManager::GlobalNetwork | AWS::NetworkManager::Link | AWS::NetworkManager::Site | AWS::Panorama::Package | AWS::Pinpoint::App | AWS::Redshift::ScheduledAction | AWS::Route53Resolver::FirewallRuleGroupAssociation | AWS::SageMaker::AppImageConfig | AWS::SageMaker::Image | AWS::ECS::TaskSet | AWS::Cassandra::Keyspace | AWS::Signer::SigningProfile | AWS::Amplify::App | AWS::AppMesh::VirtualNode | AWS::AppMesh::VirtualService | AWS::AppRunner::VpcConnector | AWS::AppStream::Application | AWS::CodeArtifact::Repository | AWS::EC2::PrefixList | AWS::EC2::SpotFleet | AWS::Evidently::Project | AWS::Forecast::Dataset | AWS::IAM::SAMLProvider | AWS::IAM::ServerCertificate | AWS::Pinpoint::Campaign | AWS::Pinpoint::InAppTemplate | AWS::SageMaker::Domain | AWS::Transfer::Agreement | AWS::Transfer::Connector | AWS::KinesisFirehose::DeliveryStream | AWS::Amplify::Branch | AWS::AppIntegrations::EventIntegration | AWS::AppMesh::Route | AWS::Athena::PreparedStatement | AWS::EC2::IPAMScope | AWS::Evidently::Launch | AWS::Forecast::DatasetGroup | AWS::GreengrassV2::ComponentVersion | AWS::GroundStation::MissionProfile | AWS::MediaConnect::FlowEntitlement | AWS::MediaConnect::FlowVpcInterface | AWS::MediaTailor::PlaybackConfiguration | AWS::MSK::Configuration | AWS::Personalize::Dataset | AWS::Personalize::Schema | AWS::Personalize::Solution | AWS::Pinpoint::EmailTemplate | AWS::Pinpoint::EventStream | AWS::ResilienceHub::App | AWS::ACMPCA::CertificateAuthority | AWS::AppConfig::HostedConfigurationVersion | AWS::AppMesh::VirtualGateway | AWS::AppMesh::VirtualRouter | AWS::AppRunner::Service | AWS::CustomerProfiles::ObjectType | AWS::DMS::Endpoint | AWS::EC2::CapacityReservation | AWS::EC2::ClientVpnEndpoint | AWS::Kendra::Index | AWS::KinesisVideo::Stream | AWS::Logs::Destination | AWS::Pinpoint::EmailChannel | AWS::S3::AccessPoint | AWS::NetworkManager::CustomerGatewayAssociation | AWS::NetworkManager::LinkAssociation | AWS::IoTWireless::MulticastGroup | AWS::Personalize::DatasetGroup | AWS::IoTTwinMaker::ComponentType | AWS::CodeBuild::ReportGroup | AWS::SageMaker::FeatureGroup | AWS::MSK::BatchScramSecret | AWS::AppStream::Stack | AWS::IoT::JobTemplate | AWS::IoTWireless::FuotaTask | AWS::IoT::ProvisioningTemplate | AWS::InspectorV2::Filter | AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation | AWS::ServiceDiscovery::Instance | AWS::Transfer::Certificate | AWS::MediaConnect::FlowSource | AWS::APS::RuleGroupsNamespace | AWS::CodeGuruProfiler::ProfilingGroup | AWS::Route53Resolver::ResolverQueryLoggingConfig | AWS::Batch::SchedulingPolicy | AWS::ACMPCA::CertificateAuthorityActivation | AWS::AppMesh::GatewayRoute | AWS::AppMesh::Mesh | AWS::Connect::Instance | AWS::Connect::QuickConnect | AWS::EC2::CarrierGateway | AWS::EC2::IPAMPool | AWS::EC2::TransitGatewayConnect | AWS::EC2::TransitGatewayMulticastDomain | AWS::ECS::CapacityProvider | AWS::IAM::InstanceProfile | AWS::IoT::CACertificate | AWS::IoTTwinMaker::SyncJob | AWS::KafkaConnect::Connector | AWS::Lambda::CodeSigningConfig | AWS::NetworkManager::ConnectPeer | AWS::ResourceExplorer2::Index | AWS::AppStream::Fleet | AWS::Cognito::UserPool | AWS::Cognito::UserPoolClient | AWS::Cognito::UserPoolGroup | AWS::EC2::NetworkInsightsAccessScope | AWS::EC2::NetworkInsightsAnalysis | AWS::Grafana::Workspace | AWS::GroundStation::DataflowEndpointGroup | AWS::ImageBuilder::ImageRecipe | AWS::KMS::Alias | AWS::M2::Environment | AWS::QuickSight::DataSource | AWS::QuickSight::Template | AWS::QuickSight::Theme | AWS::RDS::OptionGroup | AWS::Redshift::EndpointAccess | AWS::Route53Resolver::FirewallRuleGroup | AWS::SSM::Document | AWS::AppConfig::ExtensionAssociation | AWS::AppIntegrations::Application | AWS::AppSync::ApiCache | AWS::Bedrock::Guardrail | AWS::Bedrock::KnowledgeBase | AWS::Cognito::IdentityPool | AWS::Connect::Rule | AWS::Connect::User | AWS::EC2::ClientVpnTargetNetworkAssociation | AWS::EC2::EIPAssociation | AWS::EC2::IPAMResourceDiscovery | AWS::EC2::IPAMResourceDiscoveryAssociation | AWS::EC2::InstanceConnectEndpoint | AWS::EC2::SnapshotBlockPublicAccess | AWS::EC2::VPCBlockPublicAccessExclusion | AWS::EC2::VPCBlockPublicAccessOptions | AWS::EC2::VPCEndpointConnectionNotification | AWS::EC2::VPNConnectionRoute | AWS::Evidently::Segment | AWS::IAM::OIDCProvider | AWS::InspectorV2::Activation | AWS::MSK::ClusterPolicy | AWS::MSK::VpcConnection | AWS::MediaConnect::Gateway | AWS::MemoryDB::SubnetGroup | AWS::OpenSearchServerless::Collection | AWS::OpenSearchServerless::VpcEndpoint | AWS::Redshift::EndpointAuthorization | AWS::Route53Profiles::Profile | AWS::S3::StorageLensGroup | AWS::S3Express::BucketPolicy | AWS::S3Express::DirectoryBucket | AWS::SageMaker::InferenceExperiment | AWS::SecurityHub::Standard | AWS::Transfer::Profile | AWS::CloudFormation::StackSet | AWS::MediaPackageV2::Channel | AWS::S3::AccessGrantsLocation | AWS::S3::AccessGrant | AWS::S3::AccessGrantsInstance | AWS::EMRServerless::Application | AWS::Config::AggregationAuthorization | AWS::Bedrock::ApplicationInferenceProfile | AWS::ApiGatewayV2::Integration | AWS::SageMaker::MlflowTrackingServer | AWS::SageMaker::ModelBiasJobDefinition | AWS::SecretsManager::RotationSchedule | AWS::Deadline::QueueFleetAssociation | AWS::ECR::RepositoryCreationTemplate | AWS::CloudFormation::LambdaHook | AWS::EC2::SubnetNetworkAclAssociation | AWS::ApiGateway::UsagePlan | AWS::AppConfig::Extension | AWS::Deadline::Fleet | AWS::EMR::Studio | AWS::S3Tables::TableBucket | AWS::CloudFront::RealtimeLogConfig | AWS::BackupGateway::Hypervisor | AWS::BCMDataExports::Export | AWS::CloudFormation::GuardHook | AWS::CloudFront::PublicKey | AWS::CloudTrail::EventDataStore | AWS::EntityResolution::IdMappingWorkflow | AWS::EntityResolution::SchemaMapping | AWS::IoT::DomainConfiguration | AWS::PCAConnectorAD::DirectoryRegistration | AWS::RDS::Integration | AWS::Config::ConformancePack | AWS::RolesAnywhere::Profile | AWS::CodeArtifact::Domain | AWS::Backup::RestoreTestingPlan | AWS::Config::StoredQuery | AWS::SageMaker::DataQualityJobDefinition | AWS::SageMaker::ModelExplainabilityJobDefinition | AWS::SageMaker::ModelQualityJobDefinition | AWS::SageMaker::StudioLifecycleConfig | AWS::SES::DedicatedIpPool | AWS::SES::MailManagerTrafficPolicy | AWS::SSM::ResourceDataSync | AWS::BedrockAgentCore::Runtime | AWS::BedrockAgentCore::BrowserCustom | AWS::ElasticLoadBalancingV2::TargetGroup | AWS::EMRContainers::VirtualCluster | AWS::EntityResolution::MatchingWorkflow | AWS::IoTCoreDeviceAdvisor::SuiteDefinition | AWS::EC2::SecurityGroupVpcAssociation | AWS::EC2::VerifiedAccessInstance | AWS::KafkaConnect::CustomPlugin | AWS::NetworkManager::TransitGatewayPeering | AWS::OpenSearchServerless::SecurityConfig | AWS::Redshift::Integration | AWS::RolesAnywhere::TrustAnchor | AWS::Route53Profiles::ProfileAssociation | AWS::SSMIncidents::ResponsePlan | AWS::Transfer::Server | AWS::Glue::Database | AWS::Organizations::OrganizationalUnit | AWS::EC2::IPAMPoolCidr | AWS::EC2::VPCGatewayAttachment | AWS::Bedrock::Prompt | AWS::Comprehend::Flywheel | AWS::DataSync::Agent | AWS::MediaTailor::LiveSource | AWS::MSK::ServerlessCluster | AWS::IoTSiteWise::Asset | AWS::B2BI::Capability | AWS::CloudFront::KeyValueStore | AWS::Deadline::Monitor | AWS::GuardDuty::MalwareProtectionPlan | AWS::Location::APIKey | AWS::MediaPackageV2::OriginEndpoint | AWS::PCAConnectorAD::Connector | AWS::S3Tables::TableBucketPolicy | AWS::SecretsManager::ResourcePolicy | AWS::SSMContacts::Contact | AWS::IoT::ThingGroup | AWS::ImageBuilder::LifecyclePolicy | AWS::GameLift::Build | AWS::ECR::ReplicationConfiguration | AWS::EC2::SubnetCidrBlock | AWS::Connect::SecurityProfile | AWS::CleanRoomsML::TrainingDataset | AWS::AppStream::AppBlockBuilder | AWS::Route53::DNSSEC | AWS::SageMaker::UserProfile | AWS::ApiGateway::Method`
Required: Yes

## Response Syntax
<a name="API_GetResourceConfigHistory_ResponseSyntax"></a>

```
{
   "configurationItems": [
      {
         "accountId": "string",
         "arn": "string",
         "availabilityZone": "string",
         "awsRegion": "string",
         "configuration": "string",
         "configurationItemCaptureTime": number,
         "configurationItemDeliveryTime": number,
         "configurationItemMD5Hash": "string",
         "configurationItemStatus": "string",
         "configurationStateId": "string",
         "recordingFrequency": "string",
         "relatedEvents": [ "string" ],
         "relationships": [
            {
               "relationshipName": "string",
               "resourceId": "string",
               "resourceName": "string",
               "resourceType": "string"
            }
         ],
         "resourceCreationTime": number,
         "resourceId": "string",
         "resourceName": "string",
         "resourceType": "string",
         "supplementaryConfiguration": {
            "string" : "string"
         },
         "tags": {
            "string" : "string"
         },
         "version": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_GetResourceConfigHistory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configurationItems](#API_GetResourceConfigHistory_ResponseSyntax) **   <a name="config-GetResourceConfigHistory-response-configurationItems"></a>
An array of `ConfigurationItems` Objects. Contatins the configuration history for one or more resources.
Type: Array of [ConfigurationItem](API_ConfigurationItem.md) objects

 ** [nextToken](#API_GetResourceConfigHistory_ResponseSyntax) **   <a name="config-GetResourceConfigHistory-response-nextToken"></a>
The string that you use in a subsequent request to get the next page of results in a paginated response.
Type: String

## Errors
<a name="API_GetResourceConfigHistory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidLimitException **
The specified limit is outside the allowable range.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The specified next token is not valid. Specify the `nextToken` string that was returned in the previous response to get the next page of results.
HTTP Status Code: 400

 ** InvalidTimeRangeException **
The specified time range is not valid. The earlier time is not chronologically before the later time.
HTTP Status Code: 400

 ** NoAvailableConfigurationRecorderException **
There are no customer managed configuration recorders available to record your resources. Use the [PutConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigurationRecorder.html) operation to create the customer managed configuration recorder.
HTTP Status Code: 400

 ** ResourceNotDiscoveredException **
You have specified a resource that is either unknown or has not been discovered.
HTTP Status Code: 400

 ** ValidationException **
The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.
For [PutStoredQuery](https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html), one of the following errors:
+ There are missing required fields.
+ The input value fails the validation.
+ You are trying to create more than 300 queries.
For [DescribeConfigurationRecorders](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html) and [DescribeConfigurationRecorderStatus](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html), one of the following errors:
+ You have specified more than one configuration recorder.
+ You have provided a service principal for service-linked configuration recorder that is not valid.
For [AssociateResourceTypes](https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html) and [DisassociateResourceTypes](https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html), one of the following errors:
+ Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.
+ One or more of the specified resource types are already associated or disassociated with the configuration recorder.
+ For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.
For [DeleteServiceLinkedConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html), one of the following errors:
+ You have provided both `Arn` and `ServicePrincipal`. Only one of `Arn` or `ServicePrincipal` can be specified.
+ You have provided a service principal for service-linked configuration recorder that is not valid.
HTTP Status Code: 400

## Examples
<a name="API_GetResourceConfigHistory_Examples"></a>

### How to access the contents for configuration: Amazon S3 bucket
<a name="API_GetResourceConfigHistory_Example_1"></a>

This example illustrates one usage of GetResourceConfigHistory.

```pyton
import boto3
import json

def handle_configuration(configuration_item):
    """
    Example of handling the configuration field from get_resource_config_history
    """
    # The configuration is a JSON-encoded string
    raw_configuration = configuration_item['configuration']
    print(f"Raw configuration: {raw_configuration}")

    # Deserialize the configuration string to access its attributes
    configuration = json.loads(raw_configuration)

    # Now you can access configuration attributes
    bucket_name = configuration['name']
    owner_id = configuration['owner']['id']
    creation_date = configuration['creationDate']
    region = configuration['region']

    print(f"Bucket Name: {bucket_name}")
    print(f"Owner ID: {owner_id}")
    print(f"Creation Date: {creation_date}")
    print(f"Region: {region}")
```

### How to access the contents for supplementaryConfiguration: Amazon S3 bucket
<a name="API_GetResourceConfigHistory_Example_2"></a>

This example illustrates one usage of GetResourceConfigHistory.

```pyton
import boto3
import json

def handle_supplementary_configuration(configuration_item):
    """
    Example of handling the supplementaryConfiguration field from get_resource_config_history
    """
    supplementary_config = configuration_item['supplementaryConfiguration']

    # Handle ServerSideEncryptionConfiguration
    sse_config = json.loads(supplementary_config['ServerSideEncryptionConfiguration'])
    encryption_rules = sse_config['rules']

    # Handle AccessControlList (double-encoded)
    acl_string = supplementary_config['AccessControlList']
    acl = json.loads(json.loads(acl_string))  # Note: double json.loads for double-encoded strings

    # Handle BucketPolicy
    bucket_policy = json.loads(supplementary_config['BucketPolicy'])

    print("Encryption Rules:", encryption_rules)
    print("ACL Grant List:", acl['grantList'])
    print("Bucket Policy:", bucket_policy)

    # Handle other supplementary configurations
    public_access = json.loads(supplementary_config['PublicAccessBlockConfiguration'])
    print("Public Access Block Configuration:", public_access)
```

## See Also
<a name="API_GetResourceConfigHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/GetResourceConfigHistory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/GetResourceConfigHistory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/GetResourceConfigHistory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/GetResourceConfigHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/GetResourceConfigHistory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/GetResourceConfigHistory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/GetResourceConfigHistory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/GetResourceConfigHistory)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/GetResourceConfigHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/GetResourceConfigHistory)
