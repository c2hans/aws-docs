---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ListDiscoveredResources.html
---

# ListDiscoveredResources
<a name="API_ListDiscoveredResources"></a>

Returns a list of resource resource identifiers for the specified resource types for the resources of that type. A *resource identifier* includes the resource type, ID, and (if available) the custom resource name.

The results consist of resources that AWS Config has *discovered*, including those that AWS Config is not currently recording. You can narrow the results to include only resources that have specific resource IDs or a resource name.

**Note**
You can specify either resource IDs or a resource name, but not both, in the same request.

**Important**
 * CloudFormation stack recording behavior in AWS Config *
When a CloudFormation stack fails to create (for example, it enters the `ROLLBACK_FAILED` state), AWS Config does not record a configuration item (CI) for that stack. Configuration items are only recorded for stacks that reach the following states:
 `CREATE_COMPLETE`
 `UPDATE_COMPLETE`
 `UPDATE_ROLLBACK_COMPLETE`
 `UPDATE_ROLLBACK_FAILED`
 `DELETE_FAILED`
 `DELETE_COMPLETE`
Because no CI is created for a failed stack creation, you won't see configuration history for that stack in AWS Config, even after the stack is deleted. This helps make sure that AWS Config only tracks resources that were successfully provisioned.

## Request Syntax
<a name="API_ListDiscoveredResources_RequestSyntax"></a>

```
{
   "includeDeletedResources": {{boolean}},
   "limit": {{number}},
   "nextToken": "{{string}}",
   "resourceIds": [ "{{string}}" ],
   "resourceName": "{{string}}",
   "resourceType": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDiscoveredResources_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [includeDeletedResources](#API_ListDiscoveredResources_RequestSyntax) **   <a name="config-ListDiscoveredResources-request-includeDeletedResources"></a>
Specifies whether AWS Config includes deleted resources in the results. By default, deleted resources are not included.
Type: Boolean
Required: No

 ** [limit](#API_ListDiscoveredResources_RequestSyntax) **   <a name="config-ListDiscoveredResources-request-limit"></a>
The maximum number of resource identifiers returned on each page. The default is 100. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListDiscoveredResources_RequestSyntax) **   <a name="config-ListDiscoveredResources-request-nextToken"></a>
The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String
Required: No

 ** [resourceIds](#API_ListDiscoveredResources_RequestSyntax) **   <a name="config-ListDiscoveredResources-request-resourceIds"></a>
The IDs of only those resources that you want AWS Config to list in the response. If you do not specify this parameter, AWS Config lists all resources of the specified type that it has discovered. You can list a minimum of 1 resourceID and a maximum of 20 resourceIds.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 768.
Required: No

 ** [resourceName](#API_ListDiscoveredResources_RequestSyntax) **   <a name="config-ListDiscoveredResources-request-resourceName"></a>
The custom name of only those resources that you want AWS Config to list in the response. If you do not specify this parameter, AWS Config lists all resources of the specified type that it has discovered.
Type: String
Required: No

 ** [resourceType](#API_ListDiscoveredResources_RequestSyntax) **   <a name="config-ListDiscoveredResources-request-resourceType"></a>
The type of resources that you want AWS Config to list in the response.
Type: String
Valid Values: `AWS::AccessAnalyzer::Analyzer | AWS::ACM::Certificate | AWS::ACMPCA::CertificateAuthority | AWS::ACMPCA::CertificateAuthorityActivation | AWS::AmazonMQ::Broker | AWS::Amplify::App | AWS::Amplify::Branch | AWS::ApiGateway::ClientCertificate | AWS::ApiGateway::DomainName | AWS::ApiGateway::Method | AWS::ApiGateway::Resource | AWS::ApiGateway::RestApi | AWS::ApiGateway::Stage | AWS::ApiGateway::UsagePlan | AWS::ApiGatewayV2::Api | AWS::ApiGatewayV2::DomainName | AWS::ApiGatewayV2::Integration | AWS::ApiGatewayV2::Route | AWS::ApiGatewayV2::Stage | AWS::AppConfig::Application | AWS::AppConfig::ConfigurationProfile | AWS::AppConfig::DeploymentStrategy | AWS::AppConfig::Environment | AWS::AppConfig::Extension | AWS::AppConfig::ExtensionAssociation | AWS::AppConfig::HostedConfigurationVersion | AWS::AppFlow::Flow | AWS::AppIntegrations::Application | AWS::AppIntegrations::EventIntegration | AWS::AppMesh::GatewayRoute | AWS::AppMesh::Mesh | AWS::AppMesh::Route | AWS::AppMesh::VirtualGateway | AWS::AppMesh::VirtualNode | AWS::AppMesh::VirtualRouter | AWS::AppMesh::VirtualService | AWS::AppRunner::Service | AWS::AppRunner::VpcConnector | AWS::AppStream::AppBlockBuilder | AWS::AppStream::Application | AWS::AppStream::DirectoryConfig | AWS::AppStream::Fleet | AWS::AppStream::Stack | AWS::AppSync::ApiCache | AWS::AppSync::GraphQLApi | AWS::APS::RuleGroupsNamespace | AWS::Athena::DataCatalog | AWS::Athena::PreparedStatement | AWS::Athena::WorkGroup | AWS::AuditManager::Assessment | AWS::AutoScaling::AutoScalingGroup | AWS::AutoScaling::LaunchConfiguration | AWS::AutoScaling::ScalingPolicy | AWS::AutoScaling::ScheduledAction | AWS::AutoScaling::WarmPool | AWS::B2BI::Capability | AWS::Backup::BackupPlan | AWS::Backup::BackupSelection | AWS::Backup::BackupVault | AWS::Backup::RecoveryPoint | AWS::Backup::ReportPlan | AWS::Backup::RestoreTestingPlan | AWS::BackupGateway::Hypervisor | AWS::Batch::ComputeEnvironment | AWS::Batch::JobQueue | AWS::Batch::SchedulingPolicy | AWS::BCMDataExports::Export | AWS::Bedrock::ApplicationInferenceProfile | AWS::Bedrock::Guardrail | AWS::Bedrock::KnowledgeBase | AWS::Bedrock::Prompt | AWS::BedrockAgentCore::BrowserCustom | AWS::BedrockAgentCore::Runtime | AWS::Budgets::BudgetsAction | AWS::Cassandra::Keyspace | AWS::CleanRoomsML::TrainingDataset | AWS::Cloud9::EnvironmentEC2 | AWS::CloudFormation::GuardHook | AWS::CloudFormation::LambdaHook | AWS::CloudFormation::Stack | AWS::CloudFormation::StackSet | AWS::CloudFront::Distribution | AWS::CloudFront::KeyValueStore | AWS::CloudFront::PublicKey | AWS::CloudFront::RealtimeLogConfig | AWS::CloudFront::StreamingDistribution | AWS::CloudTrail::EventDataStore | AWS::CloudTrail::Trail | AWS::CloudWatch::Alarm | AWS::CloudWatch::MetricStream | AWS::CodeArtifact::Domain | AWS::CodeArtifact::Repository | AWS::CodeBuild::Project | AWS::CodeBuild::ReportGroup | AWS::CodeDeploy::Application | AWS::CodeDeploy::DeploymentConfig | AWS::CodeDeploy::DeploymentGroup | AWS::CodeGuruProfiler::ProfilingGroup | AWS::CodeGuruReviewer::RepositoryAssociation | AWS::CodePipeline::Pipeline | AWS::Cognito::IdentityPool | AWS::Cognito::UserPool | AWS::Cognito::UserPoolClient | AWS::Cognito::UserPoolGroup | AWS::Comprehend::Flywheel | AWS::Config::AggregationAuthorization | AWS::Config::ConfigurationRecorder | AWS::Config::ConformancePack | AWS::Config::ConformancePackCompliance | AWS::Config::ResourceCompliance | AWS::Config::StoredQuery | AWS::Connect::Instance | AWS::Connect::PhoneNumber | AWS::Connect::QuickConnect | AWS::Connect::Rule | AWS::Connect::SecurityProfile | AWS::Connect::User | AWS::CustomerProfiles::Domain | AWS::CustomerProfiles::ObjectType | AWS::DataSync::Agent | AWS::DataSync::LocationEFS | AWS::DataSync::LocationFSxLustre | AWS::DataSync::LocationFSxWindows | AWS::DataSync::LocationHDFS | AWS::DataSync::LocationNFS | AWS::DataSync::LocationObjectStorage | AWS::DataSync::LocationS3 | AWS::DataSync::LocationSMB | AWS::DataSync::Task | AWS::DAX::Cluster | AWS::DAX::ParameterGroup | AWS::DAX::SubnetGroup | AWS::Deadline::Fleet | AWS::Deadline::Monitor | AWS::Deadline::QueueFleetAssociation | AWS::Detective::Graph | AWS::DeviceFarm::InstanceProfile | AWS::DeviceFarm::Project | AWS::DeviceFarm::TestGridProject | AWS::DMS::Certificate | AWS::DMS::Endpoint | AWS::DMS::EventSubscription | AWS::DMS::ReplicationInstance | AWS::DMS::ReplicationSubnetGroup | AWS::DMS::ReplicationTask | AWS::DynamoDB::GlobalTable | AWS::DynamoDB::Table | AWS::EC2::CapacityReservation | AWS::EC2::CarrierGateway | AWS::EC2::ClientVpnAuthorizationRule | AWS::EC2::ClientVpnEndpoint | AWS::EC2::ClientVpnTargetNetworkAssociation | AWS::EC2::CustomerGateway | AWS::EC2::DHCPOptions | AWS::EC2::EC2Fleet | AWS::EC2::EgressOnlyInternetGateway | AWS::EC2::EIP | AWS::EC2::EIPAssociation | AWS::EC2::FlowLog | AWS::EC2::Host | AWS::EC2::Image | AWS::EC2::Instance | AWS::EC2::InstanceConnectEndpoint | AWS::EC2::InternetGateway | AWS::EC2::IPAM | AWS::EC2::IPAMPool | AWS::EC2::IPAMPoolCidr | AWS::EC2::IPAMResourceDiscovery | AWS::EC2::IPAMResourceDiscoveryAssociation | AWS::EC2::IPAMScope | AWS::EC2::LaunchTemplate | AWS::EC2::NatGateway | AWS::EC2::NetworkAcl | AWS::EC2::NetworkInsightsAccessScope | AWS::EC2::NetworkInsightsAccessScopeAnalysis | AWS::EC2::NetworkInsightsAnalysis | AWS::EC2::NetworkInsightsPath | AWS::EC2::NetworkInterface | AWS::EC2::PlacementGroup | AWS::EC2::PrefixList | AWS::EC2::RegisteredHAInstance | AWS::EC2::RouteTable | AWS::EC2::SecurityGroup | AWS::EC2::SecurityGroupVpcAssociation | AWS::EC2::SnapshotBlockPublicAccess | AWS::EC2::SpotFleet | AWS::EC2::Subnet | AWS::EC2::SubnetCidrBlock | AWS::EC2::SubnetNetworkAclAssociation | AWS::EC2::SubnetRouteTableAssociation | AWS::EC2::TrafficMirrorFilter | AWS::EC2::TrafficMirrorSession | AWS::EC2::TrafficMirrorTarget | AWS::EC2::TransitGateway | AWS::EC2::TransitGatewayAttachment | AWS::EC2::TransitGatewayConnect | AWS::EC2::TransitGatewayMulticastDomain | AWS::EC2::TransitGatewayRoute | AWS::EC2::TransitGatewayRouteTable | AWS::EC2::TransitGatewayRouteTableAssociation | AWS::EC2::TransitGatewayRouteTablePropagation | AWS::EC2::VerifiedAccessInstance | AWS::EC2::Volume | AWS::EC2::VPC | AWS::EC2::VPCBlockPublicAccessExclusion | AWS::EC2::VPCBlockPublicAccessOptions | AWS::EC2::VPCEndpoint | AWS::EC2::VPCEndpointConnectionNotification | AWS::EC2::VPCEndpointService | AWS::EC2::VPCGatewayAttachment | AWS::EC2::VPCPeeringConnection | AWS::EC2::VPNConnection | AWS::EC2::VPNConnectionRoute | AWS::EC2::VPNGateway | AWS::ECR::PublicRepository | AWS::ECR::PullThroughCacheRule | AWS::ECR::RegistryPolicy | AWS::ECR::ReplicationConfiguration | AWS::ECR::Repository | AWS::ECR::RepositoryCreationTemplate | AWS::ECS::CapacityProvider | AWS::ECS::Cluster | AWS::ECS::PrimaryTaskSet | AWS::ECS::Service | AWS::ECS::TaskDefinition | AWS::ECS::TaskSet | AWS::EFS::AccessPoint | AWS::EFS::FileSystem | AWS::EFS::MountTarget | AWS::EKS::Addon | AWS::EKS::Cluster | AWS::EKS::FargateProfile | AWS::EKS::IdentityProviderConfig | AWS::EKS::Nodegroup | AWS::ElastiCache::CacheCluster | AWS::ElastiCache::ParameterGroup | AWS::ElastiCache::ReplicationGroup | AWS::ElastiCache::SecurityGroupIngress | AWS::ElastiCache::SubnetGroup | AWS::ElasticBeanstalk::Application | AWS::ElasticBeanstalk::ApplicationVersion | AWS::ElasticBeanstalk::Environment | AWS::ElasticLoadBalancing::LoadBalancer | AWS::ElasticLoadBalancingV2::Listener | AWS::ElasticLoadBalancingV2::LoadBalancer | AWS::ElasticLoadBalancingV2::TargetGroup | AWS::Elasticsearch::Domain | AWS::EMR::Cluster | AWS::EMR::InstanceFleetConfig | AWS::EMR::InstanceGroupConfig | AWS::EMR::SecurityConfiguration | AWS::EMR::Step | AWS::EMR::Studio | AWS::EMRContainers::VirtualCluster | AWS::EMRServerless::Application | AWS::EntityResolution::IdMappingWorkflow | AWS::EntityResolution::MatchingWorkflow | AWS::EntityResolution::SchemaMapping | AWS::Events::ApiDestination | AWS::Events::Archive | AWS::Events::Connection | AWS::Events::Endpoint | AWS::Events::EventBus | AWS::Events::Rule | AWS::EventSchemas::Discoverer | AWS::EventSchemas::Registry | AWS::EventSchemas::RegistryPolicy | AWS::EventSchemas::Schema | AWS::Evidently::Launch | AWS::Evidently::Project | AWS::Evidently::Segment | AWS::FIS::ExperimentTemplate | AWS::Forecast::Dataset | AWS::Forecast::DatasetGroup | AWS::FraudDetector::EntityType | AWS::FraudDetector::Label | AWS::FraudDetector::Outcome | AWS::FraudDetector::Variable | AWS::GameLift::Build | AWS::GlobalAccelerator::Accelerator | AWS::GlobalAccelerator::EndpointGroup | AWS::GlobalAccelerator::Listener | AWS::Glue::Classifier | AWS::Glue::Database | AWS::Glue::DevEndpoint | AWS::Glue::Job | AWS::Glue::MLTransform | AWS::Grafana::Workspace | AWS::GreengrassV2::ComponentVersion | AWS::GroundStation::Config | AWS::GroundStation::DataflowEndpointGroup | AWS::GroundStation::MissionProfile | AWS::GuardDuty::Detector | AWS::GuardDuty::Filter | AWS::GuardDuty::IPSet | AWS::GuardDuty::MalwareProtectionPlan | AWS::GuardDuty::Master | AWS::GuardDuty::Member | AWS::GuardDuty::ThreatIntelSet | AWS::HealthLake::FHIRDatastore | AWS::IAM::Group | AWS::IAM::InstanceProfile | AWS::IAM::OIDCProvider | AWS::IAM::Policy | AWS::IAM::Role | AWS::IAM::SAMLProvider | AWS::IAM::ServerCertificate | AWS::IAM::User | AWS::ImageBuilder::ContainerRecipe | AWS::ImageBuilder::DistributionConfiguration | AWS::ImageBuilder::ImagePipeline | AWS::ImageBuilder::ImageRecipe | AWS::ImageBuilder::InfrastructureConfiguration | AWS::ImageBuilder::LifecyclePolicy | AWS::InspectorV2::Activation | AWS::InspectorV2::Filter | AWS::IoT::AccountAuditConfiguration | AWS::IoT::Authorizer | AWS::IoT::CACertificate | AWS::IoT::CustomMetric | AWS::IoT::Dimension | AWS::IoT::DomainConfiguration | AWS::IoT::FleetMetric | AWS::IoT::JobTemplate | AWS::IoT::MitigationAction | AWS::IoT::Policy | AWS::IoT::ProvisioningTemplate | AWS::IoT::RoleAlias | AWS::IoT::ScheduledAudit | AWS::IoT::SecurityProfile | AWS::IoT::ThingGroup | AWS::IoTAnalytics::Channel | AWS::IoTAnalytics::Dataset | AWS::IoTAnalytics::Datastore | AWS::IoTAnalytics::Pipeline | AWS::IoTCoreDeviceAdvisor::SuiteDefinition | AWS::IoTEvents::AlarmModel | AWS::IoTEvents::DetectorModel | AWS::IoTEvents::Input | AWS::IoTSiteWise::Asset | AWS::IoTSiteWise::AssetModel | AWS::IoTSiteWise::Dashboard | AWS::IoTSiteWise::Gateway | AWS::IoTSiteWise::Portal | AWS::IoTSiteWise::Project | AWS::IoTTwinMaker::ComponentType | AWS::IoTTwinMaker::Entity | AWS::IoTTwinMaker::Scene | AWS::IoTTwinMaker::SyncJob | AWS::IoTTwinMaker::Workspace | AWS::IoTWireless::FuotaTask | AWS::IoTWireless::MulticastGroup | AWS::IoTWireless::ServiceProfile | AWS::IVS::Channel | AWS::IVS::PlaybackKeyPair | AWS::IVS::RecordingConfiguration | AWS::KafkaConnect::Connector | AWS::KafkaConnect::CustomPlugin | AWS::Kendra::Index | AWS::Kinesis::Stream | AWS::Kinesis::StreamConsumer | AWS::KinesisAnalytics::Application | AWS::KinesisAnalytics::ApplicationOutput | AWS::KinesisAnalytics::ApplicationReferenceDataSource | AWS::KinesisAnalyticsV2::Application | AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption | AWS::KinesisAnalyticsV2::ApplicationOutput | AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource | AWS::KinesisFirehose::DeliveryStream | AWS::KinesisVideo::SignalingChannel | AWS::KinesisVideo::Stream | AWS::KMS::Alias | AWS::KMS::Key | AWS::Lambda::Alias | AWS::Lambda::CodeSigningConfig | AWS::Lambda::Function | AWS::Lex::Bot | AWS::Lex::BotAlias | AWS::LicenseManager::LicenseConfiguration | AWS::Lightsail::Bucket | AWS::Lightsail::Certificate | AWS::Lightsail::Disk | AWS::Lightsail::StaticIp | AWS::Location::APIKey | AWS::Logs::Destination | AWS::Logs::LogGroup | AWS::LookoutMetrics::Alert | AWS::LookoutVision::Project | AWS::M2::Environment | AWS::Macie::Session | AWS::MediaConnect::FlowEntitlement | AWS::MediaConnect::FlowSource | AWS::MediaConnect::FlowVpcInterface | AWS::MediaConnect::Gateway | AWS::MediaPackage::PackagingConfiguration | AWS::MediaPackage::PackagingGroup | AWS::MediaPackageV2::Channel | AWS::MediaPackageV2::OriginEndpoint | AWS::MediaTailor::LiveSource | AWS::MediaTailor::PlaybackConfiguration | AWS::MemoryDB::SubnetGroup | AWS::MobileHub::Project | AWS::MSK::BatchScramSecret | AWS::MSK::Cluster | AWS::MSK::ClusterPolicy | AWS::MSK::Configuration | AWS::MSK::ServerlessCluster | AWS::MSK::VpcConnection | AWS::Neptune::DBCluster | AWS::Neptune::DBClusterParameterGroup | AWS::Neptune::DBInstance | AWS::Neptune::DBParameterGroup | AWS::Neptune::DBSubnetGroup | AWS::NetworkFirewall::Firewall | AWS::NetworkFirewall::FirewallPolicy | AWS::NetworkFirewall::LoggingConfiguration | AWS::NetworkFirewall::RuleGroup | AWS::NetworkFirewall::TLSInspectionConfiguration | AWS::NetworkFirewall::VpcEndpointAssociation | AWS::NetworkFirewall::ProxyRuleGroup | AWS::NetworkFirewall::ProxyConfiguration | AWS::NetworkFirewall::Proxy | AWS::NetworkFirewall::ContainerAssociation | AWS::NetworkManager::ConnectPeer | AWS::NetworkManager::CustomerGatewayAssociation | AWS::NetworkManager::Device | AWS::NetworkManager::GlobalNetwork | AWS::NetworkManager::Link | AWS::NetworkManager::LinkAssociation | AWS::NetworkManager::Site | AWS::NetworkManager::TransitGatewayPeering | AWS::NetworkManager::TransitGatewayRegistration | AWS::OpenSearch::Domain | AWS::OpenSearchServerless::Collection | AWS::OpenSearchServerless::SecurityConfig | AWS::OpenSearchServerless::VpcEndpoint | AWS::OpsWorks::Layer | AWS::OpsWorks::Stack | AWS::Organizations::OrganizationalUnit | AWS::Panorama::Package | AWS::PCAConnectorAD::Connector | AWS::PCAConnectorAD::DirectoryRegistration | AWS::Personalize::Dataset | AWS::Personalize::DatasetGroup | AWS::Personalize::Schema | AWS::Personalize::Solution | AWS::Pinpoint::App | AWS::Pinpoint::ApplicationSettings | AWS::Pinpoint::Campaign | AWS::Pinpoint::EmailChannel | AWS::Pinpoint::EmailTemplate | AWS::Pinpoint::EventStream | AWS::Pinpoint::InAppTemplate | AWS::Pinpoint::Segment | AWS::QLDB::Ledger | AWS::QuickSight::DataSource | AWS::QuickSight::Template | AWS::QuickSight::Theme | AWS::RAM::ResourceShare | AWS::RDS::DBCluster | AWS::RDS::DBClusterParameterGroup | AWS::RDS::DBClusterSnapshot | AWS::RDS::DBInstance | AWS::RDS::DBOptionGroup | AWS::RDS::DBParameterGroup | AWS::RDS::DBSecurityGroup | AWS::RDS::DBSnapshot | AWS::RDS::DBSubnetGroup | AWS::RDS::EventSubscription | AWS::RDS::GlobalCluster | AWS::RDS::Integration | AWS::RDS::OptionGroup | AWS::Redshift::Cluster | AWS::Redshift::ClusterParameterGroup | AWS::Redshift::ClusterSecurityGroup | AWS::Redshift::ClusterSnapshot | AWS::Redshift::ClusterSubnetGroup | AWS::Redshift::EndpointAccess | AWS::Redshift::EndpointAuthorization | AWS::Redshift::EventSubscription | AWS::Redshift::Integration | AWS::Redshift::ScheduledAction | AWS::ResilienceHub::App | AWS::ResilienceHub::ResiliencyPolicy | AWS::ResourceExplorer2::Index | AWS::RoboMaker::RobotApplication | AWS::RoboMaker::RobotApplicationVersion | AWS::RoboMaker::SimulationApplication | AWS::RolesAnywhere::Profile | AWS::RolesAnywhere::TrustAnchor | AWS::Route53::DNSSEC | AWS::Route53::HealthCheck | AWS::Route53::HostedZone | AWS::Route53Profiles::Profile | AWS::Route53Profiles::ProfileAssociation | AWS::Route53RecoveryControl::Cluster | AWS::Route53RecoveryControl::ControlPanel | AWS::Route53RecoveryControl::RoutingControl | AWS::Route53RecoveryControl::SafetyRule | AWS::Route53RecoveryReadiness::Cell | AWS::Route53RecoveryReadiness::ReadinessCheck | AWS::Route53RecoveryReadiness::RecoveryGroup | AWS::Route53RecoveryReadiness::ResourceSet | AWS::Route53Resolver::FirewallDomainList | AWS::Route53Resolver::FirewallRuleGroup | AWS::Route53Resolver::FirewallRuleGroupAssociation | AWS::Route53Resolver::ResolverEndpoint | AWS::Route53Resolver::ResolverQueryLoggingConfig | AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation | AWS::Route53Resolver::ResolverRule | AWS::Route53Resolver::ResolverRuleAssociation | AWS::RUM::AppMonitor | AWS::S3::AccessGrant | AWS::S3::AccessGrantsInstance | AWS::S3::AccessGrantsLocation | AWS::S3::AccessPoint | AWS::S3::AccountPublicAccessBlock | AWS::S3::Bucket | AWS::S3::BucketPolicy | AWS::S3::MultiRegionAccessPoint | AWS::S3::StorageLens | AWS::S3::StorageLensGroup | AWS::S3Express::BucketPolicy | AWS::S3Express::DirectoryBucket | AWS::S3Tables::TableBucket | AWS::S3Tables::TableBucketPolicy | AWS::SageMaker::AppImageConfig | AWS::SageMaker::CodeRepository | AWS::SageMaker::DataQualityJobDefinition | AWS::SageMaker::Domain | AWS::SageMaker::Endpoint | AWS::SageMaker::EndpointConfig | AWS::SageMaker::FeatureGroup | AWS::SageMaker::Image | AWS::SageMaker::InferenceExperiment | AWS::SageMaker::MlflowTrackingServer | AWS::SageMaker::Model | AWS::SageMaker::ModelBiasJobDefinition | AWS::SageMaker::ModelExplainabilityJobDefinition | AWS::SageMaker::ModelQualityJobDefinition | AWS::SageMaker::MonitoringSchedule | AWS::SageMaker::NotebookInstance | AWS::SageMaker::NotebookInstanceLifecycleConfig | AWS::SageMaker::StudioLifecycleConfig | AWS::SageMaker::TrainingJob | AWS::SageMaker::UserProfile | AWS::SageMaker::Workteam | AWS::SecretsManager::ResourcePolicy | AWS::SecretsManager::RotationSchedule | AWS::SecretsManager::Secret | AWS::SecurityHub::Standard | AWS::ServiceCatalog::CloudFormationProduct | AWS::ServiceCatalog::CloudFormationProvisionedProduct | AWS::ServiceCatalog::Portfolio | AWS::ServiceDiscovery::HttpNamespace | AWS::ServiceDiscovery::Instance | AWS::ServiceDiscovery::PublicDnsNamespace | AWS::ServiceDiscovery::Service | AWS::SES::ConfigurationSet | AWS::SES::ContactList | AWS::SES::DedicatedIpPool | AWS::SES::MailManagerTrafficPolicy | AWS::SES::ReceiptFilter | AWS::SES::ReceiptRuleSet | AWS::SES::Template | AWS::Shield::Protection | AWS::ShieldRegional::Protection | AWS::Signer::SigningProfile | AWS::SNS::Subscription | AWS::SNS::Topic | AWS::SQS::Queue | AWS::SSM::AssociationCompliance | AWS::SSM::Document | AWS::SSM::FileData | AWS::SSM::ManagedInstanceInventory | AWS::SSM::PatchCompliance | AWS::SSM::ResourceDataSync | AWS::SSMContacts::Contact | AWS::SSMIncidents::ResponsePlan | AWS::SSO::InstanceAccessControlAttributeConfiguration | AWS::SSO::PermissionSet | AWS::StepFunctions::Activity | AWS::StepFunctions::StateMachine | AWS::Transfer::Agreement | AWS::Transfer::Certificate | AWS::Transfer::Connector | AWS::Transfer::Profile | AWS::Transfer::Server | AWS::Transfer::Workflow | AWS::VPCFirewall::Firewall | AWS::VPCFirewall::FirewallPolicy | AWS::VPCFirewall::RuleGroup | AWS::WAF::RateBasedRule | AWS::WAF::Rule | AWS::WAF::RuleGroup | AWS::WAF::WebACL | AWS::WAFRegional::RateBasedRule | AWS::WAFRegional::Rule | AWS::WAFRegional::RuleGroup | AWS::WAFRegional::WebACL | AWS::WAFv2::IPSet | AWS::WAFv2::ManagedRuleSet | AWS::WAFv2::RegexPatternSet | AWS::WAFv2::RuleGroup | AWS::WAFv2::WebACL | AWS::WorkSpaces::ConnectionAlias | AWS::WorkSpaces::Workspace | AWS::XRay::EncryptionConfig`
Required: Yes

## Response Syntax
<a name="API_ListDiscoveredResources_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "resourceIdentifiers": [
      {
         "resourceDeletionTime": number,
         "resourceId": "string",
         "resourceName": "string",
         "resourceType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListDiscoveredResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListDiscoveredResources_ResponseSyntax) **   <a name="config-ListDiscoveredResources-response-nextToken"></a>
The string that you use in a subsequent request to get the next page of results in a paginated response.
Type: String

 ** [resourceIdentifiers](#API_ListDiscoveredResources_ResponseSyntax) **   <a name="config-ListDiscoveredResources-response-resourceIdentifiers"></a>
The details that identify a resource that is discovered by AWS Config, including the resource type, ID, and (if available) the custom resource name.
Type: Array of [ResourceIdentifier](API_ResourceIdentifier.md) objects

## Errors
<a name="API_ListDiscoveredResources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidLimitException **
The specified limit is outside the allowable range.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The specified next token is not valid. Specify the `nextToken` string that was returned in the previous response to get the next page of results.
HTTP Status Code: 400

 ** NoAvailableConfigurationRecorderException **
There are no customer managed configuration recorders available to record your resources. Use the [PutConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigurationRecorder.html) operation to create the customer managed configuration recorder.
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

## See Also
<a name="API_ListDiscoveredResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/ListDiscoveredResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/ListDiscoveredResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ListDiscoveredResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/ListDiscoveredResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ListDiscoveredResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/ListDiscoveredResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/ListDiscoveredResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/ListDiscoveredResources)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/ListDiscoveredResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ListDiscoveredResources)
