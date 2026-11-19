---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigurationItem.html
---

# ConfigurationItem

A list that contains detailed configurations of a specified resource.

## Contents
<a name="API_ConfigurationItem_Contents"></a>

 ** accountId **   <a name="config-Type-ConfigurationItem-accountId"></a>
The 12-digit AWS account ID associated with the resource.
Type: String
Pattern: `\d{12}`
Required: No

 ** arn **   <a name="config-Type-ConfigurationItem-arn"></a>
Amazon Resource Name (ARN) associated with the resource.
Type: String
Required: No

 ** availabilityZone **   <a name="config-Type-ConfigurationItem-availabilityZone"></a>
The Availability Zone associated with the resource.
Type: String
Required: No

 ** awsRegion **   <a name="config-Type-ConfigurationItem-awsRegion"></a>
The region where the resource resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** configuration **   <a name="config-Type-ConfigurationItem-configuration"></a>
A JSON-encoded string that contains the contents for the resource configuration. This string needs to be deserialized using `json.loads()` before you can access the contents.
Type: String
Required: No

 ** configurationItemCaptureTime **   <a name="config-Type-ConfigurationItem-configurationItemCaptureTime"></a>
The time when the recording of configuration changes was initiated for the resource.
Type: Timestamp
Required: No

 ** configurationItemDeliveryTime **   <a name="config-Type-ConfigurationItem-configurationItemDeliveryTime"></a>
The time when configuration changes for the resource were delivered.
This field is optional and is not guaranteed to be present in a configuration item (CI). If you are using daily recording, this field will be populated. However, if you are using continuous recording, this field will be omitted since the delivery time is instantaneous as the CI is available right away.
For more information on daily recording and continuous recording, see [Recording Frequency](https://docs.aws.amazon.com/config/latest/developerguide/select-resources.html#select-resources-recording-frequency) in the * AWS Config Developer Guide*.
Type: Timestamp
Required: No

 ** configurationItemMD5Hash **   <a name="config-Type-ConfigurationItem-configurationItemMD5Hash"></a>
Unique MD5 hash that represents the configuration item's state.
You can use MD5 hash to compare the states of two or more configuration items that are associated with the same resource.
Type: String
Required: No

 ** configurationItemStatus **   <a name="config-Type-ConfigurationItem-configurationItemStatus"></a>
The configuration item status. Valid values include:
+ OK – The resource configuration has been updated
+ ResourceDiscovered – The resource was newly discovered
+ ResourceNotRecorded – The resource was discovered but its configuration was not recorded since the recorder doesn't record resources of this type
+ ResourceDeleted – The resource was deleted
+ ResourceDeletedNotRecorded – The resource was deleted but its configuration was not recorded since the recorder doesn't record resources of this type
Type: String
Valid Values: `OK | ResourceDiscovered | ResourceNotRecorded | ResourceDeleted | ResourceDeletedNotRecorded`
Required: No

 ** configurationStateId **   <a name="config-Type-ConfigurationItem-configurationStateId"></a>
An identifier that indicates the ordering of the configuration items of a resource.
Type: String
Required: No

 ** recordingFrequency **   <a name="config-Type-ConfigurationItem-recordingFrequency"></a>
The recording frequency that AWS Config uses to record configuration changes for the resource.
This field only appears in the API response when `DAILY` recording is enabled for a resource type. If this field is not present, `CONTINUOUS` recording is enabled for that resource type. For more information on daily recording and continuous recording, see [Recording Frequency](https://docs.aws.amazon.com/config/latest/developerguide/select-resources.html#select-resources-recording-frequency) in the * AWS Config Developer Guide*.
Type: String
Valid Values: `CONTINUOUS | DAILY`
Required: No

 ** relatedEvents **   <a name="config-Type-ConfigurationItem-relatedEvents"></a>
A list of CloudTrail event IDs.
A populated field indicates that the current configuration was initiated by the events recorded in the CloudTrail log. For more information about CloudTrail, see [What Is AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/what_is_cloud_trail_top_level.html).
An empty field indicates that the current configuration was not initiated by any event. As of Version 1.3, the relatedEvents field is empty. You can access the [LookupEvents API](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_LookupEvents.html) in the * AWS CloudTrail API Reference* to retrieve the events for the resource.
Type: Array of strings
Required: No

 ** relationships **   <a name="config-Type-ConfigurationItem-relationships"></a>
A list of related AWS resources.
Type: Array of [Relationship](API_Relationship.md) objects
Required: No

 ** resourceCreationTime **   <a name="config-Type-ConfigurationItem-resourceCreationTime"></a>
The time stamp when the resource was created.
Type: Timestamp
Required: No

 ** resourceId **   <a name="config-Type-ConfigurationItem-resourceId"></a>
The ID of the resource (for example, `sg-xxxxxx`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 768.
Required: No

 ** resourceName **   <a name="config-Type-ConfigurationItem-resourceName"></a>
The custom name of the resource, if available.
Type: String
Required: No

 ** resourceType **   <a name="config-Type-ConfigurationItem-resourceType"></a>
The type of AWS resource.
Type: String
Valid Values: `AWS::EC2::CustomerGateway | AWS::EC2::EIP | AWS::EC2::Host | AWS::EC2::Instance | AWS::EC2::InternetGateway | AWS::EC2::NetworkAcl | AWS::EC2::NetworkInterface | AWS::EC2::RouteTable | AWS::EC2::SecurityGroup | AWS::EC2::Subnet | AWS::CloudTrail::Trail | AWS::EC2::Volume | AWS::EC2::VPC | AWS::EC2::VPNConnection | AWS::EC2::VPNGateway | AWS::EC2::RegisteredHAInstance | AWS::EC2::NatGateway | AWS::EC2::EgressOnlyInternetGateway | AWS::EC2::VPCEndpoint | AWS::EC2::VPCEndpointService | AWS::EC2::FlowLog | AWS::EC2::VPCPeeringConnection | AWS::Elasticsearch::Domain | AWS::IAM::Group | AWS::IAM::Policy | AWS::IAM::Role | AWS::IAM::User | AWS::ElasticLoadBalancingV2::LoadBalancer | AWS::ACM::Certificate | AWS::RDS::DBInstance | AWS::RDS::DBSubnetGroup | AWS::RDS::DBSecurityGroup | AWS::RDS::DBSnapshot | AWS::RDS::DBCluster | AWS::RDS::DBClusterSnapshot | AWS::RDS::EventSubscription | AWS::S3::Bucket | AWS::S3::AccountPublicAccessBlock | AWS::Redshift::Cluster | AWS::Redshift::ClusterSnapshot | AWS::Redshift::ClusterParameterGroup | AWS::Redshift::ClusterSecurityGroup | AWS::Redshift::ClusterSubnetGroup | AWS::Redshift::EventSubscription | AWS::SSM::ManagedInstanceInventory | AWS::CloudWatch::Alarm | AWS::CloudFormation::Stack | AWS::ElasticLoadBalancing::LoadBalancer | AWS::AutoScaling::AutoScalingGroup | AWS::AutoScaling::LaunchConfiguration | AWS::AutoScaling::ScalingPolicy | AWS::AutoScaling::ScheduledAction | AWS::DynamoDB::Table | AWS::CodeBuild::Project | AWS::WAF::RateBasedRule | AWS::WAF::Rule | AWS::WAF::RuleGroup | AWS::WAF::WebACL | AWS::WAFRegional::RateBasedRule | AWS::WAFRegional::Rule | AWS::WAFRegional::RuleGroup | AWS::WAFRegional::WebACL | AWS::CloudFront::Distribution | AWS::CloudFront::StreamingDistribution | AWS::Lambda::Function | AWS::NetworkFirewall::Firewall | AWS::NetworkFirewall::FirewallPolicy | AWS::NetworkFirewall::RuleGroup | AWS::ElasticBeanstalk::Application | AWS::ElasticBeanstalk::ApplicationVersion | AWS::ElasticBeanstalk::Environment | AWS::WAFv2::WebACL | AWS::WAFv2::RuleGroup | AWS::WAFv2::IPSet | AWS::WAFv2::RegexPatternSet | AWS::WAFv2::ManagedRuleSet | AWS::XRay::EncryptionConfig | AWS::SSM::AssociationCompliance | AWS::SSM::PatchCompliance | AWS::Shield::Protection | AWS::ShieldRegional::Protection | AWS::Config::ConformancePackCompliance | AWS::Config::ResourceCompliance | AWS::ApiGateway::Stage | AWS::ApiGateway::RestApi | AWS::ApiGatewayV2::Stage | AWS::ApiGatewayV2::Api | AWS::CodePipeline::Pipeline | AWS::ServiceCatalog::CloudFormationProvisionedProduct | AWS::ServiceCatalog::CloudFormationProduct | AWS::ServiceCatalog::Portfolio | AWS::SQS::Queue | AWS::KMS::Key | AWS::QLDB::Ledger | AWS::SecretsManager::Secret | AWS::SNS::Topic | AWS::SSM::FileData | AWS::Backup::BackupPlan | AWS::Backup::BackupSelection | AWS::Backup::BackupVault | AWS::Backup::RecoveryPoint | AWS::ECR::Repository | AWS::ECS::Cluster | AWS::ECS::Service | AWS::ECS::TaskDefinition | AWS::EFS::AccessPoint | AWS::EFS::FileSystem | AWS::EKS::Cluster | AWS::OpenSearch::Domain | AWS::EC2::TransitGateway | AWS::Kinesis::Stream | AWS::Kinesis::StreamConsumer | AWS::CodeDeploy::Application | AWS::CodeDeploy::DeploymentConfig | AWS::CodeDeploy::DeploymentGroup | AWS::EC2::LaunchTemplate | AWS::ECR::PublicRepository | AWS::GuardDuty::Detector | AWS::EMR::SecurityConfiguration | AWS::SageMaker::CodeRepository | AWS::Route53Resolver::ResolverEndpoint | AWS::Route53Resolver::ResolverRule | AWS::Route53Resolver::ResolverRuleAssociation | AWS::DMS::ReplicationSubnetGroup | AWS::DMS::EventSubscription | AWS::MSK::Cluster | AWS::StepFunctions::Activity | AWS::WorkSpaces::Workspace | AWS::WorkSpaces::ConnectionAlias | AWS::SageMaker::Model | AWS::ElasticLoadBalancingV2::Listener | AWS::StepFunctions::StateMachine | AWS::Batch::JobQueue | AWS::Batch::ComputeEnvironment | AWS::AccessAnalyzer::Analyzer | AWS::Athena::WorkGroup | AWS::Athena::DataCatalog | AWS::Detective::Graph | AWS::GlobalAccelerator::Accelerator | AWS::GlobalAccelerator::EndpointGroup | AWS::GlobalAccelerator::Listener | AWS::EC2::TransitGatewayAttachment | AWS::EC2::TransitGatewayRouteTable | AWS::DMS::Certificate | AWS::AppConfig::Application | AWS::AppSync::GraphQLApi | AWS::DataSync::LocationSMB | AWS::DataSync::LocationFSxLustre | AWS::DataSync::LocationS3 | AWS::DataSync::LocationEFS | AWS::DataSync::Task | AWS::DataSync::LocationNFS | AWS::EC2::NetworkInsightsAccessScopeAnalysis | AWS::EKS::FargateProfile | AWS::Glue::Job | AWS::GuardDuty::ThreatIntelSet | AWS::GuardDuty::IPSet | AWS::SageMaker::Workteam | AWS::SageMaker::NotebookInstanceLifecycleConfig | AWS::ServiceDiscovery::Service | AWS::ServiceDiscovery::PublicDnsNamespace | AWS::SES::ContactList | AWS::SES::ConfigurationSet | AWS::Route53::HostedZone | AWS::IoTEvents::Input | AWS::IoTEvents::DetectorModel | AWS::IoTEvents::AlarmModel | AWS::ServiceDiscovery::HttpNamespace | AWS::Events::EventBus | AWS::ImageBuilder::ContainerRecipe | AWS::ImageBuilder::DistributionConfiguration | AWS::ImageBuilder::InfrastructureConfiguration | AWS::DataSync::LocationObjectStorage | AWS::DataSync::LocationHDFS | AWS::Glue::Classifier | AWS::Route53RecoveryReadiness::Cell | AWS::Route53RecoveryReadiness::ReadinessCheck | AWS::ECR::RegistryPolicy | AWS::Backup::ReportPlan | AWS::Lightsail::Certificate | AWS::RUM::AppMonitor | AWS::Events::Endpoint | AWS::SES::ReceiptRuleSet | AWS::Events::Archive | AWS::Events::ApiDestination | AWS::Lightsail::Disk | AWS::FIS::ExperimentTemplate | AWS::DataSync::LocationFSxWindows | AWS::SES::ReceiptFilter | AWS::GuardDuty::Filter | AWS::SES::Template | AWS::AmazonMQ::Broker | AWS::AppConfig::Environment | AWS::AppConfig::ConfigurationProfile | AWS::Cloud9::EnvironmentEC2 | AWS::EventSchemas::Registry | AWS::EventSchemas::RegistryPolicy | AWS::EventSchemas::Discoverer | AWS::FraudDetector::Label | AWS::FraudDetector::EntityType | AWS::FraudDetector::Variable | AWS::FraudDetector::Outcome | AWS::IoT::Authorizer | AWS::IoT::SecurityProfile | AWS::IoT::RoleAlias | AWS::IoT::Dimension | AWS::IoTAnalytics::Datastore | AWS::Lightsail::Bucket | AWS::Lightsail::StaticIp | AWS::MediaPackage::PackagingGroup | AWS::Route53RecoveryReadiness::RecoveryGroup | AWS::ResilienceHub::ResiliencyPolicy | AWS::Transfer::Workflow | AWS::EKS::IdentityProviderConfig | AWS::EKS::Addon | AWS::Glue::MLTransform | AWS::IoT::Policy | AWS::IoT::MitigationAction | AWS::IoTTwinMaker::Workspace | AWS::IoTTwinMaker::Entity | AWS::IoTAnalytics::Dataset | AWS::IoTAnalytics::Pipeline | AWS::IoTAnalytics::Channel | AWS::IoTSiteWise::Dashboard | AWS::IoTSiteWise::Project | AWS::IoTSiteWise::Portal | AWS::IoTSiteWise::AssetModel | AWS::IVS::Channel | AWS::IVS::RecordingConfiguration | AWS::IVS::PlaybackKeyPair | AWS::KinesisAnalyticsV2::Application | AWS::RDS::GlobalCluster | AWS::S3::MultiRegionAccessPoint | AWS::DeviceFarm::TestGridProject | AWS::Budgets::BudgetsAction | AWS::Lex::Bot | AWS::CodeGuruReviewer::RepositoryAssociation | AWS::IoT::CustomMetric | AWS::Route53Resolver::FirewallDomainList | AWS::RoboMaker::RobotApplicationVersion | AWS::EC2::TrafficMirrorSession | AWS::IoTSiteWise::Gateway | AWS::Lex::BotAlias | AWS::LookoutMetrics::Alert | AWS::IoT::AccountAuditConfiguration | AWS::EC2::TrafficMirrorTarget | AWS::S3::StorageLens | AWS::IoT::ScheduledAudit | AWS::Events::Connection | AWS::EventSchemas::Schema | AWS::MediaPackage::PackagingConfiguration | AWS::KinesisVideo::SignalingChannel | AWS::AppStream::DirectoryConfig | AWS::LookoutVision::Project | AWS::Route53RecoveryControl::Cluster | AWS::Route53RecoveryControl::SafetyRule | AWS::Route53RecoveryControl::ControlPanel | AWS::Route53RecoveryControl::RoutingControl | AWS::Route53RecoveryReadiness::ResourceSet | AWS::RoboMaker::SimulationApplication | AWS::RoboMaker::RobotApplication | AWS::HealthLake::FHIRDatastore | AWS::Pinpoint::Segment | AWS::Pinpoint::ApplicationSettings | AWS::Events::Rule | AWS::EC2::DHCPOptions | AWS::EC2::NetworkInsightsPath | AWS::EC2::TrafficMirrorFilter | AWS::EC2::IPAM | AWS::IoTTwinMaker::Scene | AWS::NetworkManager::TransitGatewayRegistration | AWS::CustomerProfiles::Domain | AWS::AutoScaling::WarmPool | AWS::Connect::PhoneNumber | AWS::AppConfig::DeploymentStrategy | AWS::AppFlow::Flow | AWS::AuditManager::Assessment | AWS::CloudWatch::MetricStream | AWS::DeviceFarm::InstanceProfile | AWS::DeviceFarm::Project | AWS::EC2::EC2Fleet | AWS::EC2::SubnetRouteTableAssociation | AWS::ECR::PullThroughCacheRule | AWS::GroundStation::Config | AWS::ImageBuilder::ImagePipeline | AWS::IoT::FleetMetric | AWS::IoTWireless::ServiceProfile | AWS::NetworkManager::Device | AWS::NetworkManager::GlobalNetwork | AWS::NetworkManager::Link | AWS::NetworkManager::Site | AWS::Panorama::Package | AWS::Pinpoint::App | AWS::Redshift::ScheduledAction | AWS::Route53Resolver::FirewallRuleGroupAssociation | AWS::SageMaker::AppImageConfig | AWS::SageMaker::Image | AWS::ECS::TaskSet | AWS::Cassandra::Keyspace | AWS::Signer::SigningProfile | AWS::Amplify::App | AWS::AppMesh::VirtualNode | AWS::AppMesh::VirtualService | AWS::AppRunner::VpcConnector | AWS::AppStream::Application | AWS::CodeArtifact::Repository | AWS::EC2::PrefixList | AWS::EC2::SpotFleet | AWS::Evidently::Project | AWS::Forecast::Dataset | AWS::IAM::SAMLProvider | AWS::IAM::ServerCertificate | AWS::Pinpoint::Campaign | AWS::Pinpoint::InAppTemplate | AWS::SageMaker::Domain | AWS::Transfer::Agreement | AWS::Transfer::Connector | AWS::KinesisFirehose::DeliveryStream | AWS::Amplify::Branch | AWS::AppIntegrations::EventIntegration | AWS::AppMesh::Route | AWS::Athena::PreparedStatement | AWS::EC2::IPAMScope | AWS::Evidently::Launch | AWS::Forecast::DatasetGroup | AWS::GreengrassV2::ComponentVersion | AWS::GroundStation::MissionProfile | AWS::MediaConnect::FlowEntitlement | AWS::MediaConnect::FlowVpcInterface | AWS::MediaTailor::PlaybackConfiguration | AWS::MSK::Configuration | AWS::Personalize::Dataset | AWS::Personalize::Schema | AWS::Personalize::Solution | AWS::Pinpoint::EmailTemplate | AWS::Pinpoint::EventStream | AWS::ResilienceHub::App | AWS::ACMPCA::CertificateAuthority | AWS::AppConfig::HostedConfigurationVersion | AWS::AppMesh::VirtualGateway | AWS::AppMesh::VirtualRouter | AWS::AppRunner::Service | AWS::CustomerProfiles::ObjectType | AWS::DMS::Endpoint | AWS::EC2::CapacityReservation | AWS::EC2::ClientVpnEndpoint | AWS::Kendra::Index | AWS::KinesisVideo::Stream | AWS::Logs::Destination | AWS::Pinpoint::EmailChannel | AWS::S3::AccessPoint | AWS::NetworkManager::CustomerGatewayAssociation | AWS::NetworkManager::LinkAssociation | AWS::IoTWireless::MulticastGroup | AWS::Personalize::DatasetGroup | AWS::IoTTwinMaker::ComponentType | AWS::CodeBuild::ReportGroup | AWS::SageMaker::FeatureGroup | AWS::MSK::BatchScramSecret | AWS::AppStream::Stack | AWS::IoT::JobTemplate | AWS::IoTWireless::FuotaTask | AWS::IoT::ProvisioningTemplate | AWS::InspectorV2::Filter | AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation | AWS::ServiceDiscovery::Instance | AWS::Transfer::Certificate | AWS::MediaConnect::FlowSource | AWS::APS::RuleGroupsNamespace | AWS::CodeGuruProfiler::ProfilingGroup | AWS::Route53Resolver::ResolverQueryLoggingConfig | AWS::Batch::SchedulingPolicy | AWS::ACMPCA::CertificateAuthorityActivation | AWS::AppMesh::GatewayRoute | AWS::AppMesh::Mesh | AWS::Connect::Instance | AWS::Connect::QuickConnect | AWS::EC2::CarrierGateway | AWS::EC2::IPAMPool | AWS::EC2::TransitGatewayConnect | AWS::EC2::TransitGatewayMulticastDomain | AWS::ECS::CapacityProvider | AWS::IAM::InstanceProfile | AWS::IoT::CACertificate | AWS::IoTTwinMaker::SyncJob | AWS::KafkaConnect::Connector | AWS::Lambda::CodeSigningConfig | AWS::NetworkManager::ConnectPeer | AWS::ResourceExplorer2::Index | AWS::AppStream::Fleet | AWS::Cognito::UserPool | AWS::Cognito::UserPoolClient | AWS::Cognito::UserPoolGroup | AWS::EC2::NetworkInsightsAccessScope | AWS::EC2::NetworkInsightsAnalysis | AWS::Grafana::Workspace | AWS::GroundStation::DataflowEndpointGroup | AWS::ImageBuilder::ImageRecipe | AWS::KMS::Alias | AWS::M2::Environment | AWS::QuickSight::DataSource | AWS::QuickSight::Template | AWS::QuickSight::Theme | AWS::RDS::OptionGroup | AWS::Redshift::EndpointAccess | AWS::Route53Resolver::FirewallRuleGroup | AWS::SSM::Document | AWS::AppConfig::ExtensionAssociation | AWS::AppIntegrations::Application | AWS::AppSync::ApiCache | AWS::Bedrock::Guardrail | AWS::Bedrock::KnowledgeBase | AWS::Cognito::IdentityPool | AWS::Connect::Rule | AWS::Connect::User | AWS::EC2::ClientVpnTargetNetworkAssociation | AWS::EC2::EIPAssociation | AWS::EC2::IPAMResourceDiscovery | AWS::EC2::IPAMResourceDiscoveryAssociation | AWS::EC2::InstanceConnectEndpoint | AWS::EC2::SnapshotBlockPublicAccess | AWS::EC2::VPCBlockPublicAccessExclusion | AWS::EC2::VPCBlockPublicAccessOptions | AWS::EC2::VPCEndpointConnectionNotification | AWS::EC2::VPNConnectionRoute | AWS::Evidently::Segment | AWS::IAM::OIDCProvider | AWS::InspectorV2::Activation | AWS::MSK::ClusterPolicy | AWS::MSK::VpcConnection | AWS::MediaConnect::Gateway | AWS::MemoryDB::SubnetGroup | AWS::OpenSearchServerless::Collection | AWS::OpenSearchServerless::VpcEndpoint | AWS::Redshift::EndpointAuthorization | AWS::Route53Profiles::Profile | AWS::S3::StorageLensGroup | AWS::S3Express::BucketPolicy | AWS::S3Express::DirectoryBucket | AWS::SageMaker::InferenceExperiment | AWS::SecurityHub::Standard | AWS::Transfer::Profile | AWS::CloudFormation::StackSet | AWS::MediaPackageV2::Channel | AWS::S3::AccessGrantsLocation | AWS::S3::AccessGrant | AWS::S3::AccessGrantsInstance | AWS::EMRServerless::Application | AWS::Config::AggregationAuthorization | AWS::Bedrock::ApplicationInferenceProfile | AWS::ApiGatewayV2::Integration | AWS::SageMaker::MlflowTrackingServer | AWS::SageMaker::ModelBiasJobDefinition | AWS::SecretsManager::RotationSchedule | AWS::Deadline::QueueFleetAssociation | AWS::ECR::RepositoryCreationTemplate | AWS::CloudFormation::LambdaHook | AWS::EC2::SubnetNetworkAclAssociation | AWS::ApiGateway::UsagePlan | AWS::AppConfig::Extension | AWS::Deadline::Fleet | AWS::EMR::Studio | AWS::S3Tables::TableBucket | AWS::CloudFront::RealtimeLogConfig | AWS::BackupGateway::Hypervisor | AWS::BCMDataExports::Export | AWS::CloudFormation::GuardHook | AWS::CloudFront::PublicKey | AWS::CloudTrail::EventDataStore | AWS::EntityResolution::IdMappingWorkflow | AWS::EntityResolution::SchemaMapping | AWS::IoT::DomainConfiguration | AWS::PCAConnectorAD::DirectoryRegistration | AWS::RDS::Integration | AWS::Config::ConformancePack | AWS::RolesAnywhere::Profile | AWS::CodeArtifact::Domain | AWS::Backup::RestoreTestingPlan | AWS::Config::StoredQuery | AWS::SageMaker::DataQualityJobDefinition | AWS::SageMaker::ModelExplainabilityJobDefinition | AWS::SageMaker::ModelQualityJobDefinition | AWS::SageMaker::StudioLifecycleConfig | AWS::SES::DedicatedIpPool | AWS::SES::MailManagerTrafficPolicy | AWS::SSM::ResourceDataSync | AWS::BedrockAgentCore::Runtime | AWS::BedrockAgentCore::BrowserCustom | AWS::ElasticLoadBalancingV2::TargetGroup | AWS::EMRContainers::VirtualCluster | AWS::EntityResolution::MatchingWorkflow | AWS::IoTCoreDeviceAdvisor::SuiteDefinition | AWS::EC2::SecurityGroupVpcAssociation | AWS::EC2::VerifiedAccessInstance | AWS::KafkaConnect::CustomPlugin | AWS::NetworkManager::TransitGatewayPeering | AWS::OpenSearchServerless::SecurityConfig | AWS::Redshift::Integration | AWS::RolesAnywhere::TrustAnchor | AWS::Route53Profiles::ProfileAssociation | AWS::SSMIncidents::ResponsePlan | AWS::Transfer::Server | AWS::Glue::Database | AWS::Organizations::OrganizationalUnit | AWS::EC2::IPAMPoolCidr | AWS::EC2::VPCGatewayAttachment | AWS::Bedrock::Prompt | AWS::Comprehend::Flywheel | AWS::DataSync::Agent | AWS::MediaTailor::LiveSource | AWS::MSK::ServerlessCluster | AWS::IoTSiteWise::Asset | AWS::B2BI::Capability | AWS::CloudFront::KeyValueStore | AWS::Deadline::Monitor | AWS::GuardDuty::MalwareProtectionPlan | AWS::Location::APIKey | AWS::MediaPackageV2::OriginEndpoint | AWS::PCAConnectorAD::Connector | AWS::S3Tables::TableBucketPolicy | AWS::SecretsManager::ResourcePolicy | AWS::SSMContacts::Contact | AWS::IoT::ThingGroup | AWS::ImageBuilder::LifecyclePolicy | AWS::GameLift::Build | AWS::ECR::ReplicationConfiguration | AWS::EC2::SubnetCidrBlock | AWS::Connect::SecurityProfile | AWS::CleanRoomsML::TrainingDataset | AWS::AppStream::AppBlockBuilder | AWS::Route53::DNSSEC | AWS::SageMaker::UserProfile | AWS::ApiGateway::Method`
Required: No

 ** supplementaryConfiguration **   <a name="config-Type-ConfigurationItem-supplementaryConfiguration"></a>
A string to string map that contains additional contents for the resource configuration.AWS Config returns this field for certain resource types to supplement the information returned for the `configuration` field.
This string to string map needs to be deserialized using `json.loads()` before you can accessing the contents.
Type: String to string map
Required: No

 ** tags **   <a name="config-Type-ConfigurationItem-tags"></a>
A mapping of key value tags associated with the resource.
Type: String to string map
Required: No

 ** version **   <a name="config-Type-ConfigurationItem-version"></a>
The version number of the resource configuration.
Type: String
Required: No

## See Also
<a name="API_ConfigurationItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ConfigurationItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ConfigurationItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ConfigurationItem)
