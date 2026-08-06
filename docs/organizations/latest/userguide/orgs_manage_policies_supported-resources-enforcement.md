---
source_url: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_supported-resources-enforcement.html
---

# Services and resource types that support enforcement
<a name="orgs_manage_policies_supported-resources-enforcement"></a>

The following services and resource types support enforcement with tag policies:

<table>
<thead>
  <tr><th>  </th><th>  </th><th>  </th><th colspan="2"> Basic Compliance Rules </th><th colspan="2"> Required Tag Keys </th></tr>
  <tr><th> Service </th><th> Tag Policies JSON syntax </th><th> CloudFormation Alias </th><th> Reporting Mode </th><th> Enforcement Mode </th><th> Reporting Mode </th><th> Enforce for IaC </th></tr>
</thead>
<tbody>
  <tr><td rowspan="4"> AWS Amplify UI Builder [amplifyuibuilder] </td><td> amplifyuibuilder:theme </td><td> +   `AWS::AmplifyUIBuilder::Theme`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> amplifyuibuilder:app/environment/components </td><td> +   `AWS::AmplifyUIBuilder::Component`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> amplifyuibuilder:component </td><td> +   `AWS::AmplifyUIBuilder::Component`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> amplifyuibuilder:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> AWS Amplify [amplify] </td><td> amplify:apps </td><td> +   `AWS::Amplify::App`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="8"> AWS App Mesh [appmesh] </td><td> appmesh:mesh </td><td> +   `AWS::AppMesh::Mesh`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> appmesh:mesh/virtualgateway/gatewayroute </td><td> +   `AWS::AppMesh::GatewayRoute`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> appmesh:mesh/virtualgateway </td><td> +   `AWS::AppMesh::VirtualGateway`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> appmesh:mesh/virtualnode </td><td> +   `AWS::AppMesh::VirtualNode`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> appmesh:mesh/virtualrouter/route </td><td> +   `AWS::AppMesh::Route`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> appmesh:mesh/virtualservice </td><td> +   `AWS::AppMesh::VirtualService`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> appmesh:mesh/virtualrouter </td><td> +   `AWS::AppMesh::VirtualRouter`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> appmesh:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="6"> AWS App Runner [apprunner] </td><td> apprunner:autoscalingconfiguration </td><td> +   `AWS::AppRunner::AutoScalingConfiguration`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> apprunner:service </td><td> +   `AWS::AppRunner::Service`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> apprunner:connection </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> apprunner:vpcingressconnection </td><td> +   `AWS::AppRunner::VpcIngressConnection`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> apprunner:observabilityconfiguration </td><td> +   `AWS::AppRunner::ObservabilityConfiguration`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> apprunner:vpcconnector </td><td> +   `AWS::AppRunner::VpcConnector`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="9"> AWS AppConfig [appconfig] </td><td> appconfig:application/environment </td><td> +   `AWS::AppConfig::Environment`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> appconfig:environment </td><td> +   `AWS::AppConfig::Environment`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> appconfig:configuration </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> appconfig:extension </td><td> +   `AWS::AppConfig::Extension`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> appconfig:application </td><td> +   `AWS::AppConfig::Application`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> appconfig:extensionassociation </td><td> +   `AWS::AppConfig::ExtensionAssociation`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> appconfig:application/configurationprofile </td><td> +   `AWS::AppConfig::ConfigurationProfile`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> appconfig:application/environment/deployment </td><td> +   `AWS::AppConfig::Deployment`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> appconfig:deploymentstrategy </td><td> +   `AWS::AppConfig::DeploymentStrategy`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="3"> AWS AppFabric [appfabric] </td><td> appfabric:appbundle/ingestion </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> appfabric:appbundle </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> appfabric:appbundle/appauthorization </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="3"> AWS AppSync [appsync] </td><td> appsync:domainnames </td><td> +   `AWS::AppSync::DomainName`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> appsync:apis </td><td> +   `AWS::AppSync::GraphQLApi`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> appsync:apis </td><td> +   `AWS::AppSync::Api`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> AWS Application Auto Scaling [application-autoscaling] </td><td> application-autoscaling:scalable-target </td><td> +   `AWS::ApplicationAutoScaling::ScalableTarget`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="10"> AWS Application Migration Service [mgn] </td><td> mgn:source-server </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> mgn:connector </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> mgn:application </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> mgn:wave </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> mgn:launch-configuration-template </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> mgn:replication-configuration-template </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> mgn:job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> mgn:import </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> mgn:vcenter-client </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> mgn:export </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="4"> AWS Audit Manager [auditmanager] </td><td> auditmanager:assessment </td><td> +   `AWS::AuditManager::Assessment`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> auditmanager:control </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> auditmanager:assessmentframework </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> auditmanager:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="4"> AWS B2B Data Interchange [b2bi] </td><td> b2bi:profile </td><td> +   `AWS::B2BI::Profile`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> b2bi:partnership </td><td> +   `AWS::B2BI::Partnership`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> b2bi:transformer </td><td> +   `AWS::B2BI::Transformer`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> b2bi:capability </td><td> +   `AWS::B2BI::Capability`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="4"> AWS Backup Gateway [backup-gateway] </td><td> backup-gateway:vm </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> backup-gateway:hypervisor </td><td> +   `AWS::BackupGateway::Hypervisor`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> backup-gateway:gateway </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> backup-gateway:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> AWS Backup [backup-search] </td><td> backup-search:search-export-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> backup-search:search-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="9"> AWS Backup [backup] </td><td> backup:legal-hold </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> backup:tiering-configuration </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> backup:report-plan </td><td> +   `AWS::Backup::ReportPlan`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> backup:backup-vault </td><td> +   `AWS::Backup::LogicallyAirGappedBackupVault`  <br />+   `AWS::Backup::BackupVault`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> backup:restore-testing-plan </td><td> +   `AWS::Backup::RestoreTestingPlan`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> backup:framework </td><td> +   `AWS::Backup::Framework`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> backup:backup-plan </td><td> +   `AWS::Backup::BackupPlan`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> backup:recovery-point </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> backup:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="9"> AWS Batch [batch] </td><td> batch:service-environment </td><td> +   `AWS::Batch::ServiceEnvironment`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> batch:job-definition </td><td> +   `AWS::Batch::JobDefinition`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> batch:scheduling-policy </td><td> +   `AWS::Batch::SchedulingPolicy`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> batch:consumable-resource </td><td> +   `AWS::Batch::ConsumableResource`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> batch:service-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> batch:compute-environment </td><td> +   `AWS::Batch::ComputeEnvironment`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> batch:job </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> batch:job-queue </td><td> +   `AWS::Batch::JobQueue`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> batch:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> AWS Billing And Cost Management Data Exports [bcm-data-exports] </td><td> bcm-data-exports:export </td><td> +   `AWS::BCMDataExports::Export`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="3"> AWS Billing And Cost Management Pricing Calculator [bcm-pricing-calculator] </td><td> bcm-pricing-calculator:workload-estimate </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bcm-pricing-calculator:bill-estimate </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bcm-pricing-calculator:bill-scenario </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="4"> AWS Billing Conductor [billingconductor] </td><td> billingconductor:billinggroup </td><td> +   `AWS::BillingConductor::BillingGroup`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> billingconductor:pricingplan </td><td> +   `AWS::BillingConductor::PricingPlan`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> billingconductor:customlineitem </td><td> +   `AWS::BillingConductor::CustomLineItem`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> billingconductor:pricingrule </td><td> +   `AWS::BillingConductor::PricingRule`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> AWS Billing [billing] </td><td> billing:billingview </td><td> +   `AWS::Billing::BillingView`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> AWS Budget Service [budgets] </td><td> budgets:budget </td><td> +   `AWS::Budgets::Budget`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> budgets:budget/action </td><td> +   `AWS::Budgets::BudgetsAction`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> AWS BugBust [bugbust] </td><td> bugbust:event </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> bugbust:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> AWS Certificate Manager [acm] </td><td> acm:certificate </td><td> +   `AWS::CertificateManager::Certificate`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> acm:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="4"> AWS Chatbot [chatbot] </td><td> chatbot:custom-action </td><td> +   `AWS::Chatbot::CustomAction`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> chatbot:chat-configuration/microsoft-teams-channel </td><td> +   `AWS::Chatbot::SlackChannelConfiguration`  <br />+   `AWS::Chatbot::MicrosoftTeamsChannelConfiguration`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> chatbot:chat-configuration/slack-channel </td><td> +   `AWS::Chatbot::SlackChannelConfiguration`  <br />+   `AWS::Chatbot::MicrosoftTeamsChannelConfiguration`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> chatbot:chat-configuration/chime-webhook </td><td> +   `AWS::Chatbot::SlackChannelConfiguration`  <br />+   `AWS::Chatbot::MicrosoftTeamsChannelConfiguration`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="11"> AWS Clean Rooms ML [cleanrooms-ml] </td><td> cleanrooms-ml:configured-model-algorithm </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> cleanrooms-ml:trained-model </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> cleanrooms-ml:membership/trained-model </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> cleanrooms-ml:configured-model-algorithm-association </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> cleanrooms-ml:membership/configured-model-algorithm-association </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> cleanrooms-ml:membership/trained-model-inference-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> cleanrooms-ml:trained-model-inference-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> cleanrooms-ml:audience-model </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> cleanrooms-ml:audience-generation-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> cleanrooms-ml:training-dataset </td><td> +   `AWS::CleanRoomsML::TrainingDataset`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> cleanrooms-ml:configured-audience-model </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="9"> AWS Clean Rooms [cleanrooms] </td><td> cleanrooms:collaboration </td><td> +   `AWS::CleanRooms::Collaboration`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> cleanrooms:membership/privacybudgettemplate </td><td> +   `AWS::CleanRooms::PrivacyBudgetTemplate`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> cleanrooms:membership/configuredtableassociation </td><td> +   `AWS::CleanRooms::ConfiguredTableAssociation`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> cleanrooms:configuredtable </td><td> +   `AWS::CleanRooms::ConfiguredTable`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> cleanrooms:membership/analysistemplate </td><td> +   `AWS::CleanRooms::AnalysisTemplate`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> cleanrooms:membership/configuredaudiencemodelassociation </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> cleanrooms:membership </td><td> +   `AWS::CleanRooms::Membership`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> cleanrooms:membership/idmappingtable </td><td> +   `AWS::CleanRooms::IdMappingTable`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> cleanrooms:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> AWS Cloud Map [servicediscovery] </td><td> servicediscovery:namespace </td><td> +   `AWS::ServiceDiscovery::HttpNamespace`  <br />+   `AWS::ServiceDiscovery::PrivateDnsNamespace`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> servicediscovery:service </td><td> +   `AWS::ServiceDiscovery::Service`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> AWS Cloud9 [cloud9] </td><td> cloud9:environment </td><td> +   `AWS::Cloud9::EnvironmentEC2`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> cloud9:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> AWS CloudFormation [cloudformation] </td><td> cloudformation:stack </td><td> +   `AWS::CloudFormation::Stack`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> cloudformation:stackset </td><td> +   `AWS::CloudFormation::StackSet`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> AWS CloudHSM [cloudhsm] </td><td> cloudhsm:backup </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> cloudhsm:cluster </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="5"> AWS CloudTrail [cloudtrail] </td><td> cloudtrail:channel </td><td> +   `AWS::CloudTrail::Channel`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> cloudtrail:eventdatastore </td><td> +   `AWS::CloudTrail::EventDataStore`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> cloudtrail:trail </td><td> +   `AWS::CloudTrail::Trail`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> cloudtrail:dashboard </td><td> +   `AWS::CloudTrail::Dashboard`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> cloudtrail:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> AWS CloudWatch RUM [rum] </td><td> rum:appmonitor </td><td> +   `AWS::RUM::AppMonitor`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="3"> AWS CodeArtifact [codeartifact] </td><td> codeartifact:repository </td><td> +   `AWS::CodeArtifact::Repository`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> codeartifact:domain </td><td> +   `AWS::CodeArtifact::Domain`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> codeartifact:package-group </td><td> +   `AWS::CodeArtifact::PackageGroup`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="4"> AWS CodeBuild [codebuild] </td><td> codebuild:project </td><td> +   `AWS::CodeBuild::Project`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> codebuild:fleet </td><td> +   `AWS::CodeBuild::Fleet`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> codebuild:report-group </td><td> +   `AWS::CodeBuild::ReportGroup`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> codebuild:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> AWS CodeCommit [codecommit] </td><td> codecommit:repository </td><td> +   `AWS::CodeCommit::Repository`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> codecommit:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="3"> AWS CodeConnections [codeconnections] </td><td> codeconnections:host </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> codeconnections:connection </td><td> +   `AWS::CodeConnections::Connection`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> codeconnections:repository-link </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="4"> AWS CodeDeploy [codedeploy] </td><td> codedeploy:deploymentconfig </td><td> +   `AWS::CodeDeploy::DeploymentConfig`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> codedeploy:application </td><td> +   `AWS::CodeDeploy::Application`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> codedeploy:deploymentgroup </td><td> +   `AWS::CodeDeploy::DeploymentGroup`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> codedeploy:instance </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="4"> AWS CodePipeline [codepipeline] </td><td> codepipeline:webhook </td><td> +   `AWS::CodePipeline::Webhook`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> codepipeline:pipeline </td><td> +   `AWS::CodePipeline::Pipeline`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> codepipeline:actiontype </td><td> +   `AWS::CodePipeline::CustomActionType`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> codepipeline:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="4"> AWS CodeStar Connections [codestar-connections] </td><td> codestar-connections:connection </td><td> +   `AWS::CodeStarConnections::Connection`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> codestar-connections:host </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> codestar-connections:repository-link </td><td> +   `AWS::CodeStarConnections::RepositoryLink`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> codestar-connections:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> AWS CodeStar Notifications [codestar-notifications] </td><td> codestar-notifications:notificationrule </td><td> +   `AWS::CodeStarNotifications::NotificationRule`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> AWS CodeStar [codestar] </td><td> codestar:project </td><td> +   `AWS::CodeStar::GitHubRepository`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="9"> AWS Config [config] </td><td> config:aggregation-authorization </td><td> +   `AWS::Config::AggregationAuthorization`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> config:organization-config-rule </td><td> +   `AWS::Config::OrganizationConfigRule`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> config:organization-conformance-pack </td><td> +   `AWS::Config::OrganizationConformancePack`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> config:config-rule </td><td> +   `AWS::Config::ConfigRule`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> config:configuration-recorder </td><td> +   `AWS::Config::ConfigurationRecorder`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> config:stored-query </td><td> +   `AWS::Config::StoredQuery`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> config:config-aggregator </td><td> +   `AWS::Config::ConfigurationAggregator`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> config:conformance-pack </td><td> +   `AWS::Config::ConformancePack`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> config:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="3"> AWS Control Tower [controltower] </td><td> controltower:landingzone </td><td> +   `AWS::ControlTower::LandingZone`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> controltower:enabledcontrol </td><td> +   `AWS::ControlTower::EnabledControl`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> controltower:enabledbaseline </td><td> +   `AWS::ControlTower::EnabledBaseline`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="3"> AWS Cost Explorer Service [ce] </td><td> ce:anomalysubscription </td><td> +   `AWS::CE::AnomalySubscription`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ce:costcategory </td><td> +   `AWS::CE::CostCategory`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ce:anomalymonitor </td><td> +   `AWS::CE::AnomalyMonitor`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> AWS Cost and Usage Report [cur] </td><td> cur:definition </td><td> +   `AWS::CUR::ReportDefinition`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="5"> AWS Data Exchange [dataexchange] </td><td> dataexchange:entitled-revisions </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> dataexchange:event-actions </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> dataexchange:entitled-data-sets </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> dataexchange:data-grants </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> dataexchange:data-sets </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> AWS Data Pipeline [datapipeline] </td><td> datapipeline:pipeline </td><td> +   `AWS::DataPipeline::Pipeline`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="6"> AWS DataSync [datasync] </td><td> datasync:location </td><td> +   `AWS::DataSync::LocationEFS`  <br />+   `AWS::DataSync::LocationS3`  <br />+   `AWS::DataSync::LocationFSxLustre`  <br />+   `AWS::DataSync::LocationNFS`  <br />+   `AWS::DataSync::LocationFSxONTAP`  <br />+   `AWS::DataSync::LocationObjectStorage`  <br />+   `AWS::DataSync::LocationFSxOpenZFS`  <br />+   `AWS::DataSync::LocationSMB`  <br />+   `AWS::DataSync::LocationFSxWindows`  <br />+   `AWS::DataSync::LocationAzureBlob`  <br />+   `AWS::DataSync::LocationHDFS`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> datasync:task </td><td> +   `AWS::DataSync::Task`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> datasync:task/execution </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> datasync:agent </td><td> +   `AWS::DataSync::Agent`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> datasync:system/job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> datasync:system </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="13"> AWS Database Migration Service [dms] </td><td> dms:assessment-run </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> dms:subgrp </td><td> +   `AWS::DMS::ReplicationSubnetGroup`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> dms:es </td><td> +   `AWS::DMS::EventSubscription`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> dms:replication-config </td><td> +   `AWS::DMS::ReplicationConfig`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> dms:cert </td><td> +   `AWS::DMS::Certificate`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> dms:rep </td><td> +   `AWS::DMS::ReplicationInstance`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> dms:instance-profile </td><td> +   `AWS::DMS::InstanceProfile`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> dms:task </td><td> +   `AWS::DMS::ReplicationTask`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> dms:endpoint </td><td> +   `AWS::DMS::Endpoint`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> dms:data-migration </td><td> +   `AWS::DMS::DataMigration`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> dms:data-provider </td><td> +   `AWS::DMS::DataProvider`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> dms:migration-project </td><td> +   `AWS::DMS::MigrationProject`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> dms:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="3"> AWS Deadline Cloud [deadline] </td><td> deadline:license-endpoint </td><td> +   `AWS::Deadline::LicenseEndpoint`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> deadline:farm </td><td> +   `AWS::Deadline::Farm`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> deadline:monitor </td><td> +   `AWS::Deadline::Monitor`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> AWS DeepComposer [deepcomposer] </td><td> deepcomposer:composition </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> deepcomposer:model </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="6"> AWS DeepRacer [deepracer] </td><td> deepracer:leaderboard\_evaluation\_job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> deepracer:leaderboard </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> deepracer:model </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> deepracer:training\_job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> deepracer:evaluation\_job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> deepracer:car </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="11"> AWS Device Farm [devicefarm] </td><td> devicefarm:device </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> devicefarm:testgrid-project </td><td> +   `AWS::DeviceFarm::TestGridProject`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> devicefarm:deviceinstance </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> devicefarm:devicepool </td><td> +   `AWS::DeviceFarm::DevicePool`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> devicefarm:project </td><td> +   `AWS::DeviceFarm::Project`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> devicefarm:testgrid-session </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> devicefarm:session </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> devicefarm:instanceprofile </td><td> +   `AWS::DeviceFarm::InstanceProfile`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> devicefarm:networkprofile </td><td> +   `AWS::DeviceFarm::NetworkProfile`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> devicefarm:vpceconfiguration </td><td> +   `AWS::DeviceFarm::VPCEConfiguration`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> devicefarm:run </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="3"> AWS Diode Messaging [diode-messaging] </td><td> diode-messaging:responding-flow </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> diode-messaging:mapping </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> diode-messaging:requesting-flow </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> AWS Diode [diode] </td><td> diode:transfer </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> diode:account-mapping </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="5"> AWS Direct Connect [directconnect] </td><td> directconnect:dxvif </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> directconnect:dxlag </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> directconnect:dxcon </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> directconnect:dx-gateway </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> directconnect:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> AWS Directory Service [ds] </td><td> ds:directory </td><td> +   `AWS::DirectoryService::MicrosoftAD`  <br />+   `AWS::DirectoryService::SimpleAD`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="6"> AWS Elastic Beanstalk [elasticbeanstalk] </td><td> elasticbeanstalk:platform </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> elasticbeanstalk:configurationtemplate </td><td> +   `AWS::ElasticBeanstalk::ConfigurationTemplate`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> elasticbeanstalk:application </td><td> +   `AWS::ElasticBeanstalk::Application`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> elasticbeanstalk:environment </td><td> +   `AWS::ElasticBeanstalk::Environment`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> elasticbeanstalk:applicationversion </td><td> +   `AWS::ElasticBeanstalk::ApplicationVersion`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> elasticbeanstalk:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="6"> AWS Elastic Disaster Recovery [drs] </td><td> drs:job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> drs:source-network </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> drs:replication-configuration-template </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> drs:source-server </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> drs:launch-configuration-template </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> drs:recovery-instance </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="6"> AWS Elastic Load Balancing [elasticloadbalancing] </td><td> elasticloadbalancing:loadbalancer </td><td> +   `AWS::ElasticLoadBalancingV2::LoadBalancer`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> elasticloadbalancing:targetgroup </td><td> +   `AWS::ElasticLoadBalancingV2::TargetGroup`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> elasticloadbalancing:loadbalancer </td><td> +   `AWS::ElasticLoadBalancing::LoadBalancer`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> elasticloadbalancing:listener </td><td> +   `AWS::ElasticLoadBalancingV2::Listener`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> elasticloadbalancing:truststore </td><td> +   `AWS::ElasticLoadBalancingV2::TrustStore`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> elasticloadbalancing:listener-rule </td><td> +   `AWS::ElasticLoadBalancingV2::ListenerRule`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> AWS Elemental Appliances and Software [elemental-appliances-software] </td><td> elemental-appliances-software:quote </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="8"> AWS Elemental MediaConnect [mediaconnect] </td><td> mediaconnect:routeroutput </td><td> +   `AWS::MediaConnect::RouterOutput`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> mediaconnect:source </td><td> +   `AWS::MediaConnect::FlowSource`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> mediaconnect:output </td><td> +   `AWS::MediaConnect::FlowOutput`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> mediaconnect:entitlement </td><td> +   `AWS::MediaConnect::FlowEntitlement`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> mediaconnect:flow </td><td> +   `AWS::MediaConnect::Flow`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> mediaconnect:routernetworkinterface </td><td> +   `AWS::MediaConnect::RouterNetworkInterface`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> mediaconnect:flow/vpcinterface </td><td> +   `AWS::MediaConnect::FlowVpcInterface`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> mediaconnect:routerinput </td><td> +   `AWS::MediaConnect::RouterInput`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="4"> AWS Elemental MediaConvert [mediaconvert] </td><td> mediaconvert:queues </td><td> +   `AWS::MediaConvert::Queue`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> mediaconvert:presets </td><td> +   `AWS::MediaConvert::Preset`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> mediaconvert:jobtemplates </td><td> +   `AWS::MediaConvert::JobTemplate`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> mediaconvert:jobs </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="15"> AWS Elemental MediaLive [medialive] </td><td> medialive:node </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> medialive:sdisource </td><td> +   `AWS::MediaLive::SdiSource`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> medialive:reservation </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> medialive:signal-map </td><td> +   `AWS::MediaLive::SignalMap`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> medialive:network </td><td> +   `AWS::MediaLive::Network`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> medialive:cloudwatch-alarm-template </td><td> +   `AWS::MediaLive::CloudWatchAlarmTemplate`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> medialive:eventbridge-rule-template </td><td> +   `AWS::MediaLive::EventBridgeRuleTemplate`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> medialive:multiplex </td><td> +   `AWS::MediaLive::Multiplex`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> medialive:cloudwatch-alarm-template-group </td><td> +   `AWS::MediaLive::CloudWatchAlarmTemplateGroup`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> medialive:eventbridge-rule-template-group </td><td> +   `AWS::MediaLive::EventBridgeRuleTemplateGroup`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> medialive:channel </td><td> +   `AWS::MediaLive::Channel`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> medialive:channelplacementgroup </td><td> +   `AWS::MediaLive::ChannelPlacementGroup`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> medialive:inputsecuritygroup </td><td> +   `AWS::MediaLive::InputSecurityGroup`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> medialive:input </td><td> +   `AWS::MediaLive::Input`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> medialive:inputdevice </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="5"> AWS Elemental MediaPackage V2 [mediapackagev2] </td><td> mediapackagev2:channelGroup/channel/originEndpoint </td><td> +   `AWS::MediaPackageV2::OriginEndpoint`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> mediapackagev2:channelgroup/channel/originendpoint </td><td> +   `AWS::MediaPackageV2::OriginEndpoint`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> mediapackagev2:channelgroup </td><td> +   `AWS::MediaPackageV2::ChannelGroup`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> mediapackagev2:channelGroup/channel </td><td> +   `AWS::MediaPackageV2::Channel`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> mediapackagev2:channelgroup/channel </td><td> +   `AWS::MediaPackageV2::Channel`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="3"> AWS Elemental MediaPackage [mediapackage-vod] </td><td> mediapackage-vod:packaging-configurations </td><td> +   `AWS::MediaPackage::PackagingConfiguration`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> mediapackage-vod:assets </td><td> +   `AWS::MediaPackage::Asset`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> mediapackage-vod:packaging-groups </td><td> +   `AWS::MediaPackage::PackagingGroup`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> AWS Elemental MediaPackage [mediapackage] </td><td> mediapackage:channels </td><td> +   `AWS::MediaPackage::Channel`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> mediapackage:origin\_endpoints </td><td> +   `AWS::MediaPackage::OriginEndpoint`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="4"> AWS Elemental MediaStore [mediastore] </td><td> mediastore:folder </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> mediastore:container </td><td> +   `AWS::MediaStore::Container`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> mediastore:object </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> mediastore:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="5"> AWS Elemental MediaTailor [mediatailor] </td><td> mediatailor:playbackconfiguration </td><td> +   `AWS::MediaTailor::PlaybackConfiguration`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> mediatailor:sourcelocation </td><td> +   `AWS::MediaTailor::SourceLocation`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> mediatailor:livesource </td><td> +   `AWS::MediaTailor::LiveSource`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> mediatailor:vodsource </td><td> +   `AWS::MediaTailor::VodSource`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> mediatailor:channel </td><td> +   `AWS::MediaTailor::Channel`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> AWS Elemental Support Cases [elemental-support-cases] </td><td> elemental-support-cases:case </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> AWS End User Messaging Social [social-messaging] </td><td> social-messaging:waba </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> social-messaging:phone-number-id </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="5"> AWS Entity Resolution [entityresolution] </td><td> entityresolution:schemamapping </td><td> +   `AWS::EntityResolution::SchemaMapping`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> entityresolution:matchingworkflow </td><td> +   `AWS::EntityResolution::MatchingWorkflow`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> entityresolution:idnamespace </td><td> +   `AWS::EntityResolution::IdNamespace`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> entityresolution:idmappingworkflow </td><td> +   `AWS::EntityResolution::IdMappingWorkflow`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> entityresolution:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="3"> AWS Fault Injection Service [fis] </td><td> fis:action </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> fis:experiment-template </td><td> +   `AWS::FIS::ExperimentTemplate`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> fis:experiment </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="4"> AWS Firewall Manager [fms] </td><td> fms:applications-list </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> fms:protocols-list </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> fms:policy </td><td> +   `AWS::FMS::Policy`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> fms:resource-set </td><td> +   `AWS::FMS::ResourceSet`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> AWS Global Accelerator [globalaccelerator] </td><td> globalaccelerator:accelerator </td><td> +   `AWS::GlobalAccelerator::Accelerator`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> globalaccelerator:attachment </td><td> +   `AWS::GlobalAccelerator::CrossAccountAttachment`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="6"> AWS Glue DataBrew [databrew] </td><td> databrew:job </td><td> +   `AWS::DataBrew::Job`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> databrew:recipe </td><td> +   `AWS::DataBrew::Recipe`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> databrew:schedule </td><td> +   `AWS::DataBrew::Schedule`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> databrew:project </td><td> +   `AWS::DataBrew::Project`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> databrew:ruleset </td><td> +   `AWS::DataBrew::Ruleset`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> databrew:dataset </td><td> +   `AWS::DataBrew::Dataset`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="19"> AWS Glue [glue] </td><td> glue:workflow </td><td> +   `AWS::Glue::Workflow`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> glue:integrationresourceproperty </td><td> +   `AWS::Glue::IntegrationResourceProperty`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> glue:integration </td><td> +   `AWS::Glue::Integration`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> glue:blueprint </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> glue:completion </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> glue:usageprofile </td><td> +   `AWS::Glue::UsageProfile`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> glue:job </td><td> +   `AWS::Glue::Job`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> glue:session </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> glue:trigger </td><td> +   `AWS::Glue::Trigger`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> glue:catalog </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> glue:devendpoint </td><td> +   `AWS::Glue::DevEndpoint`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> glue:dataqualityruleset </td><td> +   `AWS::Glue::DataQualityRuleset`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> glue:mltransform </td><td> +   `AWS::Glue::MLTransform`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> glue:connection </td><td> +   `AWS::Glue::Connection`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> glue:crawler </td><td> +   `AWS::Glue::Crawler`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> glue:registry </td><td> +   `AWS::Glue::Registry`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> glue:schema </td><td> +   `AWS::Glue::Schema`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> glue:customentitytype </td><td> +   `AWS::Glue::CustomEntityType`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> glue:database </td><td> +   `AWS::Glue::Database`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="6"> AWS Ground Station [groundstation] </td><td> groundstation:contact </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> groundstation:mission-profile </td><td> +   `AWS::GroundStation::MissionProfile`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> groundstation:ephemeris </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> groundstation:satellite </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> groundstation:config </td><td> +   `AWS::GroundStation::Config`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> groundstation:dataflow-endpoint-group </td><td> +   `AWS::GroundStation::DataflowEndpointGroup`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> AWS HealthImaging [medical-imaging] </td><td> medical-imaging:datastore </td><td> +   `AWS::HealthImaging::Datastore`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> medical-imaging:datastore/imageset </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> AWS HealthLake [healthlake] </td><td> healthlake:datastore </td><td> +   `AWS::HealthLake::FHIRDatastore`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> healthlake:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="13"> AWS HealthOmics [omics] </td><td> omics:annotationstore </td><td> +   `AWS::Omics::AnnotationStore`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> omics:sequencestore/readset </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> omics:referencestore/reference </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> omics:run </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> omics:runcache </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> omics:sequencestore </td><td> +   `AWS::Omics::SequenceStore`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> omics:variantstore </td><td> +   `AWS::Omics::VariantStore`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> omics:rungroup </td><td> +   `AWS::Omics::RunGroup`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> omics:workflow </td><td> +   `AWS::Omics::Workflow`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> omics:referencestore </td><td> +   `AWS::Omics::ReferenceStore`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> omics:annotationstore/version </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> omics:workflow/version </td><td> +   `AWS::Omics::WorkflowVersion`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> omics:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> AWS IAM Access Analyzer [access-analyzer] </td><td> access-analyzer:analyzer </td><td> +   `AWS::AccessAnalyzer::Analyzer`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="4"> AWS IAM Identity Center [sso] </td><td> sso:permissionset </td><td> +   `AWS::SSO::PermissionSet`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sso:application </td><td> +   `AWS::SSO::Application`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sso:instance </td><td> +   `AWS::SSO::Instance`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sso:trustedtokenissuer </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="9"> AWS Identity and Access Management (IAM) [iam] </td><td> iam:mfa </td><td> +   `AWS::IAM::VirtualMFADevice`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iam:server-certificate </td><td> +   `AWS::IAM::ServerCertificate`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iam:saml-provider </td><td> +   `AWS::IAM::SAMLProvider`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iam:oidc-provider </td><td> +   `AWS::IAM::OIDCProvider`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iam:policy </td><td> +   `AWS::IAM::ManagedPolicy`  <br />+   `AWS::IAM::Policy`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> iam:role </td><td> +   `AWS::IAM::Role`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iam:user </td><td> +   `AWS::IAM::User`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iam:instance-profile </td><td> +   `AWS::IAM::InstanceProfile`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iam:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="4"> AWS Identity and Access Management Roles Anywhere [nile] </td><td> nile:trust-anchor </td><td> +   `AWS::RolesAnywhere::TrustAnchor`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> nile:crl </td><td> +   `AWS::RolesAnywhere::CRL`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> nile:subject </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> nile:profile </td><td> +   `AWS::RolesAnywhere::Profile`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> AWS Invoicing Service [invoicing] </td><td> invoicing:procurement-portal-preference </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> invoicing:invoice-unit </td><td> +   `AWS::Invoicing::InvoiceUnit`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="5"> AWS IoT Analytics [iotanalytics] </td><td> iotanalytics:channel </td><td> +   `AWS::IoTAnalytics::Channel`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> iotanalytics:dataset </td><td> +   `AWS::IoTAnalytics::Dataset`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> iotanalytics:datastore </td><td> +   `AWS::IoTAnalytics::Datastore`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> iotanalytics:pipeline </td><td> +   `AWS::IoTAnalytics::Pipeline`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> iotanalytics:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> AWS IoT Core Device Advisor [iotdeviceadvisor] </td><td> iotdeviceadvisor:suiterun </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> iotdeviceadvisor:suitedefinition </td><td> +   `AWS::IoTCoreDeviceAdvisor::SuiteDefinition`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="4"> AWS IoT Events [iotevents] </td><td> iotevents:detectormodel </td><td> +   `AWS::IoTEvents::DetectorModel`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> iotevents:input </td><td> +   `AWS::IoTEvents::Input`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> iotevents:alarmmodel </td><td> +   `AWS::IoTEvents::AlarmModel`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> iotevents:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> AWS IoT Fleet Hub for Device Management [iotfleethub] </td><td> iotfleethub:application </td><td> +   `AWS::IoTFleetHub::Application`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iotfleethub:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="7"> AWS IoT FleetWise [iotfleetwise] </td><td> iotfleetwise:model-manifest </td><td> +   `AWS::IoTFleetWise::ModelManifest`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iotfleetwise:vehicle </td><td> +   `AWS::IoTFleetWise::Vehicle`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iotfleetwise:decoder-manifest </td><td> +   `AWS::IoTFleetWise::DecoderManifest`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iotfleetwise:state-template </td><td> +   `AWS::IoTFleetWise::StateTemplate`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> iotfleetwise:fleet </td><td> +   `AWS::IoTFleetWise::Fleet`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iotfleetwise:signal-catalog </td><td> +   `AWS::IoTFleetWise::SignalCatalog`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iotfleetwise:campaign </td><td> +   `AWS::IoTFleetWise::Campaign`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="14"> AWS IoT Greengrass [greengrass] </td><td> greengrass:coresdefinition </td><td> +   `AWS::Greengrass::CoreDefinition`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> greengrass:components:versions </td><td> +   `AWS::GreengrassV2::ComponentVersion`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> greengrass:devicesdefinition </td><td> +   `AWS::Greengrass::DeviceDefinition`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> greengrass:connectorsdefinition </td><td> +   `AWS::Greengrass::ConnectorDefinition`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> greengrass:deployments </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> greengrass:functionsdefinition </td><td> +   `AWS::Greengrass::FunctionDefinition`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> greengrass:bulk </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> greengrass:resourcesdefinition </td><td> +   `AWS::Greengrass::ResourceDefinition`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> greengrass:components </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> greengrass:groups </td><td> +   `AWS::Greengrass::Group`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> greengrass:loggersdefinition </td><td> +   `AWS::Greengrass::LoggerDefinition`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> greengrass:coredevices </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> greengrass:subscriptionsdefinition </td><td> +   `AWS::Greengrass::SubscriptionDefinition`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> greengrass:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="6"> AWS IoT Managed Integrations [iotmanagedintegrations] </td><td> iotmanagedintegrations:ota-task </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> iotmanagedintegrations:managed-thing </td><td> +   `AWS::IoTManagedIntegrations::ManagedThing`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> iotmanagedintegrations:cloud-connector </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> iotmanagedintegrations:account-association </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> iotmanagedintegrations:provisioning-profile </td><td> +   `AWS::IoTManagedIntegrations::ProvisioningProfile`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> iotmanagedintegrations:credential-locker </td><td> +   `AWS::IoTManagedIntegrations::CredentialLocker`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="11"> AWS IoT SiteWise [iotsitewise] </td><td> iotsitewise:portal </td><td> +   `AWS::IoTSiteWise::Portal`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iotsitewise:dashboard </td><td> +   `AWS::IoTSiteWise::Dashboard`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iotsitewise:project </td><td> +   `AWS::IoTSiteWise::Project`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iotsitewise:asset </td><td> +   `AWS::IoTSiteWise::Asset`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iotsitewise:dataset </td><td> +   `AWS::IoTSiteWise::Dataset`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iotsitewise:time-series </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> iotsitewise:computation-model </td><td> +   `AWS::IoTSiteWise::ComputationModel`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> iotsitewise:asset-model </td><td> +   `AWS::IoTSiteWise::AssetModel`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iotsitewise:gateway </td><td> +   `AWS::IoTSiteWise::Gateway`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iotsitewise:access-policy </td><td> +   `AWS::IoTSiteWise::AccessPolicy`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iotsitewise:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="5"> AWS IoT TwinMaker [iotdigitaltwin] </td><td> iotdigitaltwin:workspace </td><td> +   `AWS::IoTTwinMaker::Workspace`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> iotdigitaltwin:workspace/component-type </td><td> +   `AWS::IoTTwinMaker::ComponentType`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> iotdigitaltwin:workspace/scene </td><td> +   `AWS::IoTTwinMaker::Scene`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> iotdigitaltwin:workspace/sync-job </td><td> +   `AWS::IoTTwinMaker::SyncJob`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> iotdigitaltwin:entity </td><td> +   `AWS::IoTTwinMaker::Entity`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="11"> AWS IoT Wireless [iotwireless] </td><td> iotwireless:sidewalkaccount </td><td> +   `AWS::IoTWireless::PartnerAccount`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iotwireless:networkanalyzerconfiguration </td><td> +   `AWS::IoTWireless::NetworkAnalyzerConfiguration`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iotwireless:serviceprofile </td><td> +   `AWS::IoTWireless::ServiceProfile`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iotwireless:multicastgroup </td><td> +   `AWS::IoTWireless::MulticastGroup`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iotwireless:wirelessgateway </td><td> +   `AWS::IoTWireless::WirelessGateway`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iotwireless:wirelessdevice </td><td> +   `AWS::IoTWireless::WirelessDevice`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iotwireless:destination </td><td> +   `AWS::IoTWireless::Destination`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iotwireless:fuotatask </td><td> +   `AWS::IoTWireless::FuotaTask`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iotwireless:importtask </td><td> +   `AWS::IoTWireless::WirelessDeviceImportTask`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iotwireless:wirelessgatewaytaskdefinition </td><td> +   `AWS::IoTWireless::TaskDefinition`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iotwireless:deviceprofile </td><td> +   `AWS::IoTWireless::DeviceProfile`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="25"> AWS IoT [iot] </td><td> iot:package </td><td> +   `AWS::IoT::SoftwarePackage`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iot:authorizer </td><td> +   `AWS::IoT::Authorizer`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iot:package/version </td><td> +   `AWS::IoT::SoftwarePackageVersion`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> iot:fleetmetric </td><td> +   `AWS::IoT::FleetMetric`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iot:jobtemplate </td><td> +   `AWS::IoT::JobTemplate`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iot:billinggroup </td><td> +   `AWS::IoT::BillingGroup`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iot:provisioningtemplate </td><td> +   `AWS::IoT::ProvisioningTemplate`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iot:thingtype </td><td> +   `AWS::IoT::ThingType`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iot:thinggroup </td><td> +   `AWS::IoT::ThingGroup`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iot:certificateprovider </td><td> +   `AWS::IoT::CertificateProvider`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iot:rolealias </td><td> +   `AWS::IoT::RoleAlias`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iot:cacert </td><td> +   `AWS::IoT::CACertificate`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iot:custommetric </td><td> +   `AWS::IoT::CustomMetric`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iot:domainconfiguration </td><td> +   `AWS::IoT::DomainConfiguration`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> iot:policy </td><td> +   `AWS::IoT::Policy`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iot:mitigationaction </td><td> +   `AWS::IoT::MitigationAction`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iot:securityprofile </td><td> +   `AWS::IoT::SecurityProfile`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iot:rule </td><td> +   `AWS::IoT::TopicRule`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iot:scheduledaudit </td><td> +   `AWS::IoT::ScheduledAudit`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> iot:tunnel </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> iot:stream </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> iot:job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> iot:otaupdate </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> iot:command </td><td> +   `AWS::IoT::Command`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> iot:dimension </td><td> +   `AWS::IoT::Dimension`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> AWS Key Management Service [kms] </td><td> kms:key </td><td> +   `AWS::KMS::Key`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> kms:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="7"> AWS Lambda [lambda] </td><td> lambda:layer/version </td><td> +   `AWS::Lambda::LayerVersion`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> lambda:layerversion </td><td> +   `AWS::Lambda::LayerVersion`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> lambda:layer </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> lambda:function </td><td> +   `AWS::Lambda::Function`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> lambda:event-source-mapping </td><td> +   `AWS::Lambda::EventSourceMapping`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> lambda:code-signing-config </td><td> +   `AWS::Lambda::CodeSigningConfig`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> lambda:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> AWS Launch Wizard [launchwizard] </td><td> launchwizard:deployment </td><td> +   `AWS::LaunchWizard::Deployment`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> AWS License Manager Linux Subscriptions Manager [license-manager-linux-subscriptions] </td><td> license-manager-linux-subscriptions:subscription-provider </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="4"> AWS License Manager User Subscriptions [license-manager-user-subscriptions] </td><td> license-manager-user-subscriptions:product-subscription </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> license-manager-user-subscriptions:identity-provider </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> license-manager-user-subscriptions:instance-user </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> license-manager-user-subscriptions:license-server-endpoint </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="6"> AWS License Manager [license-manager] </td><td> license-manager:license-asset-group </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> license-manager:license </td><td> +   `AWS::LicenseManager::License`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> license-manager:license-asset-ruleset </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> license-manager:license-configuration </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> license-manager:report-generator </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> license-manager:grant </td><td> +   `AWS::LicenseManager::Grant`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> AWS MWAA Serverless [airflow-serverless] </td><td> airflow-serverless:workflow </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="4"> AWS Mainframe Modernization Application Testing [apptest] </td><td> apptest:testsuite </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> apptest:testconfiguration </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> apptest:testcase </td><td> +   `AWS::AppTest::TestCase`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> apptest:testrun </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> AWS Mainframe Modernization Service [m2] </td><td> m2:app </td><td> +   `AWS::M2::Application`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> m2:env </td><td> +   `AWS::M2::Environment`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> AWS Marketplace Vendor Insights [vendor-insights] </td><td> vendor-insights:security-profile </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> vendor-insights:data-source </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> AWS Marketplace [aws-marketplace] </td><td> aws-marketplace:deploymentparameter </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> aws-marketplace:changeset </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> AWS Migration Hub Orchestrator [migrationhub-orchestrator] </td><td> migrationhub-orchestrator:workflow </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> migrationhub-orchestrator:template </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="4"> AWS Migration Hub Refactor Spaces [refactor-spaces] </td><td> refactor-spaces:environment/application </td><td> +   `AWS::RefactorSpaces::Application`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> refactor-spaces:environment/application/service </td><td> +   `AWS::RefactorSpaces::Service`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> refactor-spaces:environment </td><td> +   `AWS::RefactorSpaces::Environment`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> refactor-spaces:environment/application/route </td><td> +   `AWS::RefactorSpaces::Route`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="6"> AWS Network Firewall [network-firewall] </td><td> network-firewall:stateless-rulegroup </td><td> +   `AWS::NetworkFirewall::RuleGroup`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> network-firewall:vpc-endpoint-association </td><td> +   `AWS::NetworkFirewall::VpcEndpointAssociation`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> network-firewall:firewall </td><td> +   `AWS::NetworkFirewall::Firewall`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> network-firewall:stateful-rulegroup </td><td> +   `AWS::NetworkFirewall::RuleGroup`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> network-firewall:firewall-policy </td><td> +   `AWS::NetworkFirewall::FirewallPolicy`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> network-firewall:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="9"> AWS Network Manager [networkmanager] </td><td> networkmanager:peering </td><td> +   `AWS::NetworkManager::TransitGatewayPeering`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> networkmanager:global-network </td><td> +   `AWS::NetworkManager::GlobalNetwork`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> networkmanager:link </td><td> +   `AWS::NetworkManager::Link`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> networkmanager:core-network </td><td> +   `AWS::NetworkManager::CoreNetwork`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> networkmanager:device </td><td> +   `AWS::NetworkManager::Device`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> networkmanager:connect-peer </td><td> +   `AWS::NetworkManager::ConnectPeer`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> networkmanager:attachment </td><td> +   `AWS::NetworkManager::VpcAttachment`  <br />+   `AWS::NetworkManager::ConnectAttachment`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> networkmanager:site </td><td> +   `AWS::NetworkManager::Site`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> networkmanager:connection </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> AWS OpsWorks Configuration Management [opsworks-cm] </td><td> opsworks-cm:server </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> opsworks-cm:backup </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="3"> AWS OpsWorks [opsworks] </td><td> opsworks:instance </td><td> +   `AWS::OpsWorks::Instance`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> opsworks:stack </td><td> +   `AWS::OpsWorks::Stack`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> opsworks:layer </td><td> +   `AWS::OpsWorks::Layer`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="6"> AWS Organizations [organizations] </td><td> organizations:account </td><td> +   `AWS::Organizations::Account`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> organizations:ou </td><td> +   `AWS::Organizations::OrganizationalUnit`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> organizations:resourcepolicy </td><td> +   `AWS::Organizations::ResourcePolicy`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> organizations:root </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> organizations:policy </td><td> +   `AWS::Organizations::Policy`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> organizations:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> AWS Outposts [outposts] </td><td> outposts:site </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> outposts:outpost </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="3"> AWS Panorama [panorama] </td><td> panorama:package </td><td> +   `AWS::Panorama::Package`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> panorama:applicationinstance </td><td> +   `AWS::Panorama::ApplicationInstance`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> panorama:device </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="3"> AWS Parallel Computing Service [pcs] </td><td> pcs:cluster </td><td> +   `AWS::PCS::Cluster`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> pcs:queue </td><td> +   `AWS::PCS::Queue`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> pcs:computenodegroup </td><td> +   `AWS::PCS::ComputeNodeGroup`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="3"> AWS Partner Central Selling [partnercentral] </td><td> partnercentral:opportunity </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> partnercentral:engagement-by-accepting-invitation-task </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> partnercentral:engagement-from-opportunity-task </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> AWS Payment Cryptography [payment-cryptography] </td><td> payment-cryptography:key </td><td> +   `AWS::PaymentCryptography::Key`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> AWS Payments [payments] </td><td> payments:payment-instrument </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> AWS Performance Insights [pi] </td><td> pi:perf-reports </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="3"> AWS Private CA Connector for Active Directory [pca-connector-ad] </td><td> pca-connector-ad:connector </td><td> +   `AWS::PCAConnectorAD::Connector`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> pca-connector-ad:connector/template </td><td> +   `AWS::PCAConnectorAD::Template`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> pca-connector-ad:directory-registration </td><td> +   `AWS::PCAConnectorAD::DirectoryRegistration`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> AWS Private CA Connector for SCEP [pca-connector-scep] </td><td> pca-connector-scep:connector </td><td> +   `AWS::PCAConnectorSCEP::Connector`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> AWS Private Certificate Authority [acm-pca] </td><td> acm-pca:certificate-authority </td><td> +   `AWS::ACMPCA::CertificateAuthority`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> acm-pca:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="9"> AWS Proton [proton] </td><td> proton:environment-template </td><td> +   `AWS::Proton::EnvironmentTemplate`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> proton:environment </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> proton:service/service-instance </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> proton:repository </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> proton:component </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> proton:environment-account-connection </td><td> +   `AWS::Proton::EnvironmentAccountConnection`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> proton:service </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> proton:deployment </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> proton:service-template </td><td> +   `AWS::Proton::ServiceTemplate`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> AWS Purchase Orders Console [purchase-orders] </td><td> purchase-orders:purchase-order </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> AWS RTB Fabric [rtbfabric] </td><td> rtbfabric:requestergateway </td><td> +   `AWS::RTBFabric::RequesterGateway`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> rtbfabric:respondergateway </td><td> +   `AWS::RTBFabric::ResponderGateway`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> AWS Recycle Bin [rbin] </td><td> rbin:rule </td><td> +   `AWS::Rbin::Rule`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> rbin:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="4"> AWS Resilience Hub [resiliencehub] </td><td> resiliencehub:app-assessment </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> resiliencehub:resiliency-policy </td><td> +   `AWS::ResilienceHub::ResiliencyPolicy`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> resiliencehub:recommendation-template </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> resiliencehub:app </td><td> +   `AWS::ResilienceHub::App`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="4"> AWS Resource Access Manager (RAM) [ram] </td><td> ram:resource-share </td><td> +   `AWS::RAM::ResourceShare`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ram:resourceshareinvitation </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ram:permission </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ram:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> AWS Resource Groups [resource-groups] </td><td> resource-groups:group </td><td> +   `AWS::ResourceGroups::Group`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> resource-groups:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="12"> AWS RoboMaker [robomaker] </td><td> robomaker:world-generation-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> robomaker:world-generation-jobs </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> robomaker:simulation-job-batch </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> robomaker:simulation-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> robomaker:world-template </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> robomaker:robot </td><td> +   `AWS::RoboMaker::Robot`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> robomaker:world-export-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> robomaker:simulation-application </td><td> +   `AWS::RoboMaker::SimulationApplication`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> robomaker:deployment-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> robomaker:robot-application </td><td> +   `AWS::RoboMaker::RobotApplication`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> robomaker:deployment-fleet </td><td> +   `AWS::RoboMaker::Fleet`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> robomaker:world </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="4"> AWS SQL Workbench [sqlworkbench] </td><td> sqlworkbench:query </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sqlworkbench:notebook </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sqlworkbench:chart </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sqlworkbench:connection </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> AWS Savings Plans [savingsplans] </td><td> savingsplans:savingsplan </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> AWS Secrets Manager [secretsmanager] </td><td> secretsmanager:secret </td><td> +   `AWS::SecretsManager::Secret`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> secretsmanager:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="8"> AWS Security Hub [securityhub] </td><td> securityhub:connectorv2 </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> securityhub:automation-rulev2 </td><td> +   `AWS::SecurityHub::AutomationRuleV2`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> securityhub:automation-rule </td><td> +   `AWS::SecurityHub::AutomationRule`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> securityhub:aggregatorv2 </td><td> +   `AWS::SecurityHub::AggregatorV2`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> securityhub:hubv2 </td><td> +   `AWS::SecurityHub::HubV2`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> securityhub:product-subscription </td><td> +   `AWS::SecurityHub::ProductSubscription`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> securityhub:hub </td><td> +   `AWS::SecurityHub::Hub`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> securityhub:configuration-policy </td><td> +   `AWS::SecurityHub::ConfigurationPolicy`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="6"> AWS Service - Oracle Database@AWS [odb] </td><td> odb:cloud-vm-cluster </td><td> +   `AWS::ODB::CloudVmCluster`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> odb:cloud-exadata-infrastructure </td><td> +   `AWS::ODB::CloudExadataInfrastructure`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> odb:db-node </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> odb:cloud-autonomous-vm-cluster </td><td> +   `AWS::ODB::CloudAutonomousVmCluster`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> odb:odb-peering-connection </td><td> +   `AWS::ODB::OdbPeeringConnection`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> odb:odb-network </td><td> +   `AWS::ODB::OdbNetwork`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="3"> AWS Service Catalog [catalog] </td><td> catalog:portfolio </td><td> +   `AWS::ServiceCatalog::Portfolio`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> catalog:product </td><td> +   `AWS::ServiceCatalog::CloudFormationProvisionedProduct`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> catalog:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="3"> AWS Service Catalog [servicecatalog] </td><td> servicecatalog:attribute-groups </td><td> +   `AWS::ServiceCatalogAppRegistry::AttributeGroup`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> servicecatalog:applications </td><td> +   `AWS::ServiceCatalogAppRegistry::Application`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> servicecatalog:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> AWS Shield [shield] </td><td> shield:protection </td><td> +   `AWS::Shield::Protection`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> shield:protection-group </td><td> +   `AWS::Shield::ProtectionGroup`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> AWS Signer [signer] </td><td> signer:signing-profiles </td><td> +   `AWS::Signer::SigningProfile`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> AWS SimSpace Weaver [simspaceweaver] </td><td> simspaceweaver:simulation </td><td> +   `AWS::SimSpaceWeaver::Simulation`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> AWS Snow Device Management [snow-device-management] </td><td> snow-device-management:task </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> snow-device-management:managed-device </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="4"> AWS Step Functions [states] </td><td> states:execution </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> states:activity </td><td> +   `AWS::StepFunctions::Activity`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> states:statemachine </td><td> +   `AWS::StepFunctions::StateMachine`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> states:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="6"> AWS Storage Gateway [storagegateway] </td><td> storagegateway:tapepool </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> storagegateway:fs-association </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> storagegateway:tape </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> storagegateway:gateway </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> storagegateway:gateway/volume </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> storagegateway:share </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> AWS Supply Chain [scn] </td><td> scn:instance </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> scn:billofmaterialsimportjob </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="3"> AWS Systems Manager Incident Manager Contacts [ssm-contacts] </td><td> ssm-contacts:contact </td><td> +   `AWS::SSMContacts::Contact`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> ssm-contacts:rotation </td><td> +   `AWS::SSMContacts::Rotation`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ssm-contacts:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="3"> AWS Systems Manager Incident Manager [ssm-incidents] </td><td> ssm-incidents:incident-record </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ssm-incidents:replication-set </td><td> +   `AWS::SSMIncidents::ReplicationSet`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ssm-incidents:response-plan </td><td> +   `AWS::SSMIncidents::ResponsePlan`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> AWS Systems Manager Quick Setup [ssm-quicksetup] </td><td> ssm-quicksetup:configuration-manager </td><td> +   `AWS::SSMQuickSetup::ConfigurationManager`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="12"> AWS Systems Manager [ssm] </td><td> ssm:managed-instance </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> ssm:document </td><td> +   `AWS::SSM::Document`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ssm:automation-definition </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ssm:parameter </td><td> +   `AWS::SSM::Parameter`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ssm:automation-execution </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> ssm:opsitem </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> ssm:patchbaseline </td><td> +   `AWS::SSM::PatchBaseline`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ssm:session </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> ssm:association </td><td> +   `AWS::SSM::Association`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ssm:maintenancewindow </td><td> +   `AWS::SSM::MaintenanceWindow`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ssm:opsmetadata </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ssm:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> AWS Systems Manager for SAP [ssm-sap] </td><td> ssm-sap:hana/db </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ssm-sap:hana </td><td> +   `AWS::SystemsManagerSAP::Application`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="5"> AWS Telco Network Builder [tnb] </td><td> tnb:network-instance </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> tnb:function-instance </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> tnb:function-package </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> tnb:network-package </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> tnb:network-operation </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="10"> AWS Transfer Family [transfer] </td><td> transfer:connector </td><td> +   `AWS::Transfer::Connector`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> transfer:user </td><td> +   `AWS::Transfer::User`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> transfer:workflow </td><td> +   `AWS::Transfer::Workflow`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> transfer:webapp </td><td> +   `AWS::Transfer::WebApp`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> transfer:agreement </td><td> +   `AWS::Transfer::Agreement`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> transfer:host-key </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> transfer:server </td><td> +   `AWS::Transfer::Server`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> transfer:certificate </td><td> +   `AWS::Transfer::Certificate`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> transfer:profile </td><td> +   `AWS::Transfer::Profile`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> transfer:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> AWS Transform [transform] </td><td> transform:connector </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> AWS User Notifications Contacts [notifications-contacts] </td><td> notifications-contacts:emailcontact </td><td> +   `AWS::NotificationsContacts::EmailContact`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> AWS User Notifications [notifications] </td><td> notifications:configuration </td><td> +   `AWS::Notifications::NotificationConfiguration`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="4"> AWS WAF Regional [waf-regional] </td><td> waf-regional:rule </td><td> +   `AWS::WAFRegional::Rule`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> waf-regional:rulegroup </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> waf-regional:ratebasedrule </td><td> +   `AWS::WAFRegional::RateBasedRule`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> waf-regional:webacl </td><td> +   `AWS::WAFRegional::WebACL`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="4"> AWS WAF [waf] </td><td> waf:rulegroup </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> waf:webacl </td><td> +   `AWS::WAF::WebACL`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> waf:ratebasedrule </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> waf:rule </td><td> +   `AWS::WAF::Rule`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="5"> AWS Well-Architected Tool [wellarchitected] </td><td> wellarchitected:lens </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> wellarchitected:review-template </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> wellarchitected:workload </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> wellarchitected:profile </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> wellarchitected:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> AWS Wickr [wickr] </td><td> wickr:network </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> wickr:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> AWS WorkSpaces Managed Instances [workspaces-instances] </td><td> workspaces-instances:workspaceinstance </td><td> +   `AWS::WorkspacesInstances::WorkspaceInstance`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> AWS X-Ray [xray] </td><td> xray:sampling-rule </td><td> +   `AWS::XRay::SamplingRule`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> xray:group </td><td> +   `AWS::XRay::Group`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> AWS rePost Private [repostspace] </td><td> repostspace:space </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="5"> AWS service providing managed private networks [private-networks] </td><td> private-networks:network-site </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> private-networks:order </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> private-networks:network </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> private-networks:network-resource </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> private-networks:device-identifier </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="11"> Alexa for Business [a4b] </td><td> a4b:profile </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> a4b:address-book </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> a4b:network-profile </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> a4b:user </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> a4b:conference-provider </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> a4b:skill-group </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> a4b:room </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> a4b:gateway-group </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> a4b:schedule </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> a4b:contact </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> a4b:device </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> Amazon AI Operations [aiops] </td><td> aiops:investigation-group </td><td> +   `AWS::AIOps::InvestigationGroup`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="8"> Amazon API Gateway Management [apigateway] </td><td> apigateway:usageplans </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> apigateway:apikeys </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> apigateway:clientcertificates </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> apigateway:restapis </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> apigateway:domainnames </td><td> +   `AWS::ApiGateway::DomainNameV2`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> apigateway:domainnameaccessassociations </td><td> +   `AWS::ApiGateway::DomainNameAccessAssociation`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> apigateway:vpclinks </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> apigateway:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> Amazon ARC Region switch [arc-region-switch] </td><td> arc-region-switch:plan </td><td> +   `AWS::ARCRegionSwitch::Plan`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> Amazon AppFlow [appflow] </td><td> appflow:connector </td><td> +   `AWS::AppFlow::Connector`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> appflow:flow </td><td> +   `AWS::AppFlow::Flow`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="6"> Amazon AppIntegrations [app-integrations] </td><td> app-integrations:application-association </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> app-integrations:data-integration </td><td> +   `AWS::AppIntegrations::DataIntegration`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> app-integrations:event-integration </td><td> +   `AWS::AppIntegrations::EventIntegration`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> app-integrations:data-integration-association </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> app-integrations:application </td><td> +   `AWS::AppIntegrations::Application`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> app-integrations:event-integration-association </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="7"> Amazon AppStream 2.0 [appstream] </td><td> appstream:image </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> appstream:app-block </td><td> +   `AWS::AppStream::AppBlock`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> appstream:stack </td><td> +   `AWS::AppStream::Stack`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> appstream:app-block-builder </td><td> +   `AWS::AppStream::AppBlockBuilder`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> appstream:fleet </td><td> +   `AWS::AppStream::Fleet`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> appstream:image-builder </td><td> +   `AWS::AppStream::ImageBuilder`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> appstream:application </td><td> +   `AWS::AppStream::Application`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="4"> Amazon Athena [athena] </td><td> athena:datacatalog </td><td> +   `AWS::Athena::DataCatalog`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> athena:capacity-reservation </td><td> +   `AWS::Athena::CapacityReservation`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> athena:workgroup </td><td> +   `AWS::Athena::WorkGroup`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> athena:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> Amazon Aurora DSQL [dsql] </td><td> dsql:cluster </td><td> +   `AWS::DSQL::Cluster`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="9"> Amazon Bedrock [bedrock-agentcore] </td><td> bedrock-agentcore:workload-identity </td><td> +   `AWS::BedrockAgentCore::WorkloadIdentity`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bedrock-agentcore:code-interpreter-custom </td><td> +   `AWS::BedrockAgentCore::CodeInterpreterCustom`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bedrock-agentcore:gateway </td><td> +   `AWS::BedrockAgentCore::Gateway`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bedrock-agentcore:token-vault </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bedrock-agentcore:memory </td><td> +   `AWS::BedrockAgentCore::Memory`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bedrock-agentcore:workload-identity-directory </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bedrock-agentcore:runtime </td><td> +   `AWS::BedrockAgentCore::Runtime`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bedrock-agentcore:browser-custom </td><td> +   `AWS::BedrockAgentCore::BrowserCustom`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bedrock-agentcore:runtime-endpoint </td><td> +   `AWS::BedrockAgentCore::RuntimeEndpoint`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="30"> Amazon Bedrock [bedrock] </td><td> bedrock:model-copy-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bedrock:custom-model-deployment </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bedrock:prompt-router </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bedrock:agent-alias </td><td> +   `AWS::Bedrock::AgentAlias`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> bedrock:blueprint </td><td> +   `AWS::Bedrock::Blueprint`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> bedrock:model-customization-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bedrock:model-import-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bedrock:data-automation-invocation </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bedrock:data-automation-invocation-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bedrock:automated-reasoning-policy </td><td> +   `AWS::Bedrock::AutomatedReasoningPolicy`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bedrock:model-evaluation-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bedrock:session </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bedrock:prompt </td><td> +   `AWS::Bedrock::Prompt`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> bedrock:guardrail </td><td> +   `AWS::Bedrock::Guardrail`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> bedrock:async-invoke </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bedrock:flow/alias </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bedrock:prompt-version </td><td> +   `AWS::Bedrock::PromptVersion`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bedrock:data-automation-project </td><td> +   `AWS::Bedrock::DataAutomationProject`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> bedrock:provisioned-model </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bedrock:provisioned-model-v2 </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bedrock:application-inference-profile </td><td> +   `AWS::Bedrock::ApplicationInferenceProfile`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> bedrock:imported-model </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bedrock:flow </td><td> +   `AWS::Bedrock::Flow`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> bedrock:flow/alias </td><td> +   `AWS::Bedrock::FlowAlias`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bedrock:flow-alias </td><td> +   `AWS::Bedrock::FlowAlias`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bedrock:knowledge-base </td><td> +   `AWS::Bedrock::KnowledgeBase`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> bedrock:agent </td><td> +   `AWS::Bedrock::Agent`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> bedrock:model-invocation-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bedrock:custom-model </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> bedrock:evaluation-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="3"> Amazon Braket [braket] </td><td> braket:quantum-task </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> braket:job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> braket:spending-limit </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="14"> Amazon Chime [chime] </td><td> chime:meeting </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> chime:sip-media-application </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> chime:sma </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> chime:app-instance/bot </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> chime:voice-profile-domain </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> chime:app-instance/channel </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> chime:app-instance/user </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> chime:media-pipeline-kinesis-video-stream-pool </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> chime:app-instance </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> chime:media-pipeline </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> chime:voice-connector </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> chime:vc </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> chime:media-insights-pipeline-configuration </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> chime:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> Amazon Cloud Directory [clouddirectory] </td><td> clouddirectory:directory </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="11"> Amazon CloudFront [cloudfront] </td><td> cloudfront:vpcorigin </td><td> +   `AWS::CloudFront::VpcOrigin`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> cloudfront:connection-function </td><td> +   `AWS::CloudFront::ConnectionFunction`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> cloudfront:distribution-tenant </td><td> +   `AWS::CloudFront::DistributionTenant`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> cloudfront:distribution </td><td> +   `AWS::CloudFront::Distribution`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> cloudfront:anycast-ip-list </td><td> +   `AWS::CloudFront::AnycastIpList`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> cloudfront:key-value-store </td><td> +   `AWS::CloudFront::KeyValueStore`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> cloudfront:keyvaluestore </td><td> +   `AWS::CloudFront::KeyValueStore`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> cloudfront:streaming-distribution </td><td> +   `AWS::CloudFront::StreamingDistribution`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> cloudfront:trust-store </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> cloudfront:connection-group </td><td> +   `AWS::CloudFront::ConnectionGroup`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> cloudfront:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> Amazon CloudSearch [cloudsearch] </td><td> cloudsearch:domain </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> Amazon CloudWatch Application Insights [applicationinsights] </td><td> applicationinsights:application </td><td> +   `AWS::ApplicationInsights::Application`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> Amazon CloudWatch Application Signals [application-signals] </td><td> application-signals:slo </td><td> +   `AWS::ApplicationSignals::ServiceLevelObjective`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="6"> Amazon CloudWatch Evidently [evidently] </td><td> evidently:segment </td><td> +   `AWS::Evidently::Segment`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> evidently:project/launch </td><td> +   `AWS::Evidently::Launch`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> evidently:project </td><td> +   `AWS::Evidently::Project`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> evidently:project/feature </td><td> +   `AWS::Evidently::Feature`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> evidently:experiment </td><td> +   `AWS::Evidently::Experiment`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> evidently:project/experiment </td><td> +   `AWS::Evidently::Experiment`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> Amazon CloudWatch Internet Monitor [internetmonitor] </td><td> internetmonitor:monitor </td><td> +   `AWS::InternetMonitor::Monitor`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> internetmonitor:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="7"> Amazon CloudWatch Logs [logs] </td><td> logs:log-group </td><td> +   `AWS::Logs::LogGroup`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> logs:delivery-destination </td><td> +   `AWS::Logs::DeliveryDestination`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> logs:scheduled-query </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> logs:destination </td><td> +   `AWS::Logs::Destination`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> logs:delivery-source </td><td> +   `AWS::Logs::DeliverySource`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> logs:anomaly-detector </td><td> +   `AWS::Logs::LogAnomalyDetector`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> logs:delivery </td><td> +   `AWS::Logs::Delivery`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> Amazon CloudWatch Network Synthetic Monitor [networkmonitor] </td><td> networkmonitor:monitor </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> networkmonitor:probe </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="3"> Amazon CloudWatch Observability Access Manager [oam] </td><td> oam:link </td><td> +   `AWS::Oam::Link`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> oam:sink </td><td> +   `AWS::Oam::Sink`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> oam:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="5"> Amazon CloudWatch Observability Admin Service [observabilityadmin] </td><td> observabilityadmin:organization-telemetry-rule </td><td> +   `AWS::ObservabilityAdmin::OrganizationTelemetryRule`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> observabilityadmin:s3tableintegration </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> observabilityadmin:telemetry-rule </td><td> +   `AWS::ObservabilityAdmin::TelemetryRule`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> observabilityadmin:telemetry-pipeline </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> observabilityadmin:organization-centralization-rule </td><td> +   `AWS::ObservabilityAdmin::OrganizationCentralizationRule`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> Amazon CloudWatch Synthetics [synthetics] </td><td> synthetics:group </td><td> +   `AWS::Synthetics::Group`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> synthetics:canary </td><td> +   `AWS::Synthetics::Canary`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="5"> Amazon CloudWatch [cloudwatch] </td><td> cloudwatch:metric-stream </td><td> +   `AWS::CloudWatch::MetricStream`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> cloudwatch:slo </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> cloudwatch:insight-rule </td><td> +   `AWS::CloudWatch::InsightRule`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> cloudwatch:alarm </td><td> +   `AWS::CloudWatch::Alarm`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> cloudwatch:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="4"> Amazon CodeCatalyst [codecatalyst] </td><td> codecatalyst:identity-center-applications </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> codecatalyst:space </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> codecatalyst:connections </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> codecatalyst:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> Amazon CodeGuru Profiler [codeguru-profiler] </td><td> codeguru-profiler:profilinggroup </td><td> +   `AWS::CodeGuruProfiler::ProfilingGroup`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="3"> Amazon CodeGuru Reviewer [codeguru-reviewer] </td><td> codeguru-reviewer:association </td><td> +   `AWS::CodeGuruReviewer::RepositoryAssociation`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> codeguru-reviewer:codereview </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> codeguru-reviewer:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> Amazon CodeGuru Security [codeguru-security] </td><td> codeguru-security:scans </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> codeguru-security:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> Amazon CodeWhisperer [codewhisperer] </td><td> codewhisperer:profile </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> codewhisperer:customization </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> Amazon Cognito Identity [cognito-identity] </td><td> cognito-identity:identitypool </td><td> +   `AWS::Cognito::IdentityPool`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> cognito-identity:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> Amazon Cognito Identity [cognito-idp] </td><td> cognito-idp:userpool </td><td> +   `AWS::Cognito::UserPool`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> cognito-idp:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="16"> Amazon Comprehend [comprehend] </td><td> comprehend:targeted-sentiment-detection-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> comprehend:entity-recognizer-endpoint </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> comprehend:sentiment-detection-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> comprehend:flywheel </td><td> +   `AWS::Comprehend::Flywheel`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> comprehend:document-classifier-endpoint </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> comprehend:entity-recognizer </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> comprehend:topics-detection-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> comprehend:events-detection-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> comprehend:document-classifier </td><td> +   `AWS::Comprehend::DocumentClassifier`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> comprehend:key-phrases-detection-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> comprehend:document-classification-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> comprehend:entities-detection-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> comprehend:dominant-language-detection-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> comprehend:flywheel/dataset </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> comprehend:pii-entities-detection-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> comprehend:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="7"> Amazon Connect Cases [cases] </td><td> cases:related-item </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> cases:domain/case/related-item </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> cases:layout </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> cases:field </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> cases:template </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> cases:domain/case </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> cases:domain </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="4"> Amazon Connect Customer Profiles [profile] </td><td> profile:domains/object-types </td><td> +   `AWS::CustomerProfiles::ObjectType`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> profile:domains/domain-object-types </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> profile:domains </td><td> +   `AWS::CustomerProfiles::Domain`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> profile:domains/integrations </td><td> +   `AWS::CustomerProfiles::Integration`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> Amazon Connect Outbound Campaigns [connect-campaigns] </td><td> connect-campaigns:campaign </td><td> +   `AWS::ConnectCampaigns::Campaign`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> Amazon Connect Voice ID [voiceid] </td><td> voiceid:domain </td><td> +   `AWS::VoiceID::Domain`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="27"> Amazon Connect [connect] </td><td> connect:instance/evaluation-form </td><td> +   `AWS::Connect::EvaluationForm`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> connect:instance/agent-state </td><td> +   `AWS::Connect::AgentStatus`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> connect:wildcardagentstatus </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> connect:instance/transfer-destination </td><td> +   `AWS::Connect::QuickConnect`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> connect:instance/use-case </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> connect:wildcardquickconnect </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> connect:instance/task-template </td><td> +   `AWS::Connect::TaskTemplate`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> connect:instance/agent </td><td> +   `AWS::Connect::User`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> connect:traffic-distribution-group </td><td> +   `AWS::Connect::TrafficDistributionGroup`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> connect:instance/flow-module </td><td> +   `AWS::Connect::ContactFlowModule`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> connect:phone-number </td><td> +   `AWS::Connect::PhoneNumber`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> connect:instance/agent-group </td><td> +   `AWS::Connect::UserHierarchyGroup`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> connect:instance/operating-hours </td><td> +   `AWS::Connect::HoursOfOperation`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> connect:instance/security-profile </td><td> +   `AWS::Connect::SecurityProfile`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> connect:wildcardcontactflow </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> connect:instance/queue </td><td> +   `AWS::Connect::Queue`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> connect:instance/contact-evaluation </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> connect:instance/rule </td><td> +   `AWS::Connect::Rule`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> connect:instance/integration-association </td><td> +   `AWS::Connect::IntegrationAssociation`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> connect:instance/contact-flow </td><td> +   `AWS::Connect::ContactFlow`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> connect:instance/vocabulary </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> connect:instance </td><td> +   `AWS::Connect::Instance`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> connect:instance/routing-profile </td><td> +   `AWS::Connect::RoutingProfile`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> connect:wildcardqueue </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> connect:contact </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> connect:instance/prompt </td><td> +   `AWS::Connect::Prompt`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> connect:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> Amazon Data Lifecycle Manager [dlm] </td><td> dlm:policy </td><td> +   `AWS::DLM::LifecyclePolicy`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> dlm:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> Amazon DataZone [datazone] </td><td> datazone:domain </td><td> +   `AWS::DataZone::Domain`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> Amazon Detective [detective] </td><td> detective:graph </td><td> +   `AWS::Detective::Graph`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="3"> Amazon DocumentDB Elastic Clusters [docdb-elastic] </td><td> docdb-elastic:cluster </td><td> +   `AWS::DocDBElastic::Cluster`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> docdb-elastic:cluster-pg </td><td> +   `AWS::DocDBElastic::Cluster`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> docdb-elastic:cluster-snapshot </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> Amazon DynamoDB Accelerator (DAX) [dax] </td><td> dax:cache </td><td> +   `AWS::DAX::Cluster`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="5"> Amazon DynamoDB [dynamodb] </td><td> dynamodb:globaltable </td><td> +   `AWS::DynamoDB::GlobalTable`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> dynamodb:table </td><td> +   `AWS::DynamoDB::Table`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> dynamodb:index </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> dynamodb:table/stream </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> dynamodb:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> Amazon EC2 Auto Scaling [autoscaling] </td><td> autoscaling:autoscalinggroup </td><td> +   `AWS::AutoScaling::AutoScalingGroup`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="9"> Amazon EC2 Image Builder [imagebuilder] </td><td> imagebuilder:infrastructure-configuration </td><td> +   `AWS::ImageBuilder::InfrastructureConfiguration`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> imagebuilder:image-recipe </td><td> +   `AWS::ImageBuilder::ImageRecipe`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> imagebuilder:container-recipe </td><td> +   `AWS::ImageBuilder::ContainerRecipe`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> imagebuilder:image </td><td> +   `AWS::ImageBuilder::Image`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> imagebuilder:workflow </td><td> +   `AWS::ImageBuilder::Workflow`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> imagebuilder:component </td><td> +   `AWS::ImageBuilder::Component`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> imagebuilder:lifecycle-policy </td><td> +   `AWS::ImageBuilder::LifecyclePolicy`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> imagebuilder:distribution-configuration </td><td> +   `AWS::ImageBuilder::DistributionConfiguration`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> imagebuilder:image-pipeline </td><td> +   `AWS::ImageBuilder::ImagePipeline`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="93"> Amazon EC2 [ec2] </td><td> ec2:image-usage-report </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:ipam-external-resource-verification-token </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:security-group </td><td> +   `AWS::EC2::SecurityGroup`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:traffic-mirror-session </td><td> +   `AWS::EC2::TrafficMirrorSession`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:ipam-pool </td><td> +   `AWS::EC2::IPAMPool`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:security-group-rule </td><td> +   `AWS::EC2::SecurityGroupIngress`  <br />+   `AWS::EC2::SecurityGroupEgress`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:local-gateway-virtual-interface-group </td><td> +   `AWS::EC2::LocalGatewayVirtualInterfaceGroup`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:natgateway </td><td> +   `AWS::EC2::NatGateway`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:import-snapshot-task </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:internet-gateway </td><td> +   `AWS::EC2::InternetGateway`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:transit-gateway </td><td> +   `AWS::EC2::TransitGateway`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:dhcp-options </td><td> +   `AWS::EC2::DHCPOptions`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:image </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:network-insights-access-scope-analysis </td><td> +   `AWS::EC2::NetworkInsightsAccessScopeAnalysis`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:ipv4pool-ec2 </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:transit-gateway-policy-table </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:transit-gateway-attachment </td><td> +   `AWS::EC2::TransitGatewayVpcAttachment`  <br />+   `AWS::EC2::TransitGatewayAttachment`  <br />+   `AWS::EC2::TransitGatewayPeeringAttachment`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:volume </td><td> +   `AWS::EC2::Volume`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:import-image-task </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:subnet </td><td> +   `AWS::EC2::Subnet`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:vpc </td><td> +   `AWS::EC2::VPC`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:vpc-endpoint-service-permission </td><td> +   `AWS::EC2::VPCEndpointServicePermissions`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:capacity-reservation </td><td> +   `AWS::EC2::CapacityReservation`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:network-acl </td><td> +   `AWS::EC2::NetworkAcl`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:verified-access-trust-provider </td><td> +   `AWS::EC2::VerifiedAccessTrustProvider`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:vpn-gateway </td><td> +   `AWS::EC2::VPNGateway`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:carrier-gateway </td><td> +   `AWS::EC2::CarrierGateway`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:elastic-gpu </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:elasticgpu </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:local-gateway-route-table </td><td> +   `AWS::EC2::LocalGatewayRouteTable`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:network-insights-access-scope </td><td> +   `AWS::EC2::NetworkInsightsAccessScope`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:transit-gateway-connect-peer </td><td> +   `AWS::EC2::TransitGatewayConnectPeer`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:verified-access-group </td><td> +   `AWS::EC2::VerifiedAccessGroup`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:traffic-mirror-target </td><td> +   `AWS::EC2::TrafficMirrorTarget`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:coip-pool </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:fleet </td><td> +   `AWS::EC2::EC2Fleet`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:local-gateway-route-table-virtual-interface-group-association </td><td> +   `AWS::EC2::LocalGatewayRouteTableVirtualInterfaceGroupAssociation`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:transit-gateway-multicast-domain </td><td> +   `AWS::EC2::TransitGatewayMulticastDomain`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:network-interface </td><td> +   `AWS::EC2::NetworkInterface`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:capacity-manager-data-export </td><td> +   `AWS::EC2::CapacityManagerDataExport`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:client-vpn-endpoint </td><td> +   `AWS::EC2::ClientVpnEndpoint`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:spot-instances-request </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:network-insights-path </td><td> +   `AWS::EC2::NetworkInsightsPath`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:instance-connect-endpoint </td><td> +   `AWS::EC2::InstanceConnectEndpoint`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:traffic-mirror-filter-rule </td><td> +   `AWS::EC2::TrafficMirrorFilterRule`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:local-gateway-virtual-interface </td><td> +   `AWS::EC2::LocalGatewayVirtualInterface`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:vpc-peering-connection </td><td> +   `AWS::EC2::VPCPeeringConnection`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:snapshot </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:customer-gateway </td><td> +   `AWS::EC2::CustomerGateway`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:capacity-block </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:verified-access-endpoint </td><td> +   `AWS::EC2::VerifiedAccessEndpoint`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:vpn-connection </td><td> +   `AWS::EC2::VPNConnection`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:ipam-scope </td><td> +   `AWS::EC2::IPAMScope`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:host-reservation </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:replace-root-volume-task </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:instance </td><td> +   `AWS::EC2::Instance`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:fpga-image </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:route-server-endpoint </td><td> +   `AWS::EC2::RouteServerEndpoint`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:key-pair </td><td> +   `AWS::EC2::KeyPair`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:vpc-endpoint-connection </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:dedicated-host </td><td> +   `AWS::EC2::Host`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:local-gateway-route-table-vpc-association </td><td> +   `AWS::EC2::LocalGatewayRouteTableVPCAssociation`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:vpc-endpoint-service </td><td> +   `AWS::EC2::VPCEndpointService`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:egress-only-internet-gateway </td><td> +   `AWS::EC2::EgressOnlyInternetGateway`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:ipam-resource-discovery </td><td> +   `AWS::EC2::IPAMResourceDiscovery`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:mac-modification-task </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:network-insights-analysis </td><td> +   `AWS::EC2::NetworkInsightsAnalysis`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:placement-group </td><td> +   `AWS::EC2::PlacementGroup`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:instance-event-window </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:ipv6pool-ec2 </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:prefix-list </td><td> +   `AWS::EC2::PrefixList`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:vpc-endpoint </td><td> +   `AWS::EC2::VPCEndpoint`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:elastic-ip </td><td> +   `AWS::EC2::EIP`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:export-instance-task </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:reserved-instances </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:export-image-task </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:subnet-cidr-reservation </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:vpc-flow-log </td><td> +   `AWS::EC2::FlowLog`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:capacity-reservation-fleet </td><td> +   `AWS::EC2::CapacityReservationFleet`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:ipam-resource-discovery-association </td><td> +   `AWS::EC2::IPAMResourceDiscoveryAssociation`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:transit-gateway-route-table-announcement </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:traffic-mirror-filter </td><td> +   `AWS::EC2::TrafficMirrorFilter`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:outpost-lag </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:local-gateway </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:launch-template </td><td> +   `AWS::EC2::LaunchTemplate`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:vpc-block-public-access-exclusion </td><td> +   `AWS::EC2::VPCBlockPublicAccessExclusion`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:route-table </td><td> +   `AWS::EC2::RouteTable`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:ipam </td><td> +   `AWS::EC2::IPAM`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:declarative-policies-report </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ec2:verified-access-instance </td><td> +   `AWS::EC2::VerifiedAccessInstance`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:transit-gateway-route-table </td><td> +   `AWS::EC2::TransitGatewayRouteTable`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:spot-fleet-request </td><td> +   `AWS::EC2::SpotFleet`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ec2:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> Amazon EMR Serverless [emr-serverless] </td><td> emr-serverless:jobruns </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> emr-serverless:applications </td><td> +   `AWS::EMRServerless::Application`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="5"> Amazon EMR on EKS (EMR Containers) [emr-containers] </td><td> emr-containers:virtualclusters/jobruns </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> emr-containers:virtualclusters/endpoints </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> emr-containers:securityconfigurations </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> emr-containers:jobtemplates </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> emr-containers:virtualclusters </td><td> +   `AWS::EMRContainers::VirtualCluster`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="12"> Amazon ElastiCache [elasticache] </td><td> elasticache:securitygroup </td><td> +   `AWS::ElastiCache::SecurityGroup`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> elasticache:parametergroup </td><td> +   `AWS::ElastiCache::ParameterGroup`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> elasticache:usergroup </td><td> +   `AWS::ElastiCache::UserGroup`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> elasticache:snapshot </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> elasticache:subnetgroup </td><td> +   `AWS::ElastiCache::SubnetGroup`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> elasticache:cluster </td><td> +   `AWS::ElastiCache::CacheCluster`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> elasticache:reserved-instance </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> elasticache:serverlesscache </td><td> +   `AWS::ElastiCache::ServerlessCache`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> elasticache:replicationgroup </td><td> +   `AWS::ElastiCache::ReplicationGroup`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> elasticache:serverlesscachesnapshot </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> elasticache:user </td><td> +   `AWS::ElastiCache::User`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> elasticache:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> Amazon Elastic Container Registry [ecr-public] </td><td> ecr-public:repository </td><td> +   `AWS::ECR::PublicRepository`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> Amazon Elastic Container Registry [ecr] </td><td> ecr:repository </td><td> +   `AWS::ECR::Repository`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ecr:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="10"> Amazon Elastic Container Service [ecs] </td><td> ecs:task </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ecs:capacity-provider </td><td> +   `AWS::ECS::CapacityProvider`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ecs:service-revision </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ecs:service </td><td> +   `AWS::ECS::Service`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ecs:cluster </td><td> +   `AWS::ECS::Cluster`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ecs:service-deployment </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ecs:task-definition </td><td> +   `AWS::ECS::TaskDefinition`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ecs:container-instance </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ecs:task-set </td><td> +   `AWS::ECS::TaskSet`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ecs:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="3"> Amazon Elastic File System [elasticfilesystem] </td><td> elasticfilesystem:file-system </td><td> +   `AWS::EFS::FileSystem`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> elasticfilesystem:access-point </td><td> +   `AWS::EFS::AccessPoint`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> elasticfilesystem:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> Amazon Elastic Inference [amazonelasticinference] </td><td> amazonelasticinference:accelerator </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="10"> Amazon Elastic Kubernetes Service [eks] </td><td> eks:cluster </td><td> +   `AWS::EKS::Cluster`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> eks:access-entry </td><td> +   `AWS::EKS::AccessEntry`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> eks:addon </td><td> +   `AWS::EKS::Addon`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> eks:podidentityassociation </td><td> +   `AWS::EKS::PodIdentityAssociation`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> eks:dashboard </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> eks:eks-anywhere-subscription </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> eks:identityproviderconfig </td><td> +   `AWS::EKS::IdentityProviderConfig`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> eks:nodegroup </td><td> +   `AWS::EKS::Nodegroup`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> eks:fargateprofile </td><td> +   `AWS::EKS::FargateProfile`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> eks:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="5"> Amazon Elastic MapReduce [elasticmapreduce] </td><td> elasticmapreduce:cluster </td><td> +   `AWS::EMR::Cluster`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> elasticmapreduce:editor </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> elasticmapreduce:notebook-execution </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> elasticmapreduce:studio </td><td> +   `AWS::EMR::Studio`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> elasticmapreduce:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> Amazon Elastic VMware Service [evs] </td><td> evs:environment </td><td> +   `AWS::EVS::Environment`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> Amazon EventBridge Pipes [pipes] </td><td> pipes:pipe </td><td> +   `AWS::Pipes::Pipe`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> pipes:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> Amazon EventBridge Scheduler [scheduler] </td><td> scheduler:schedule-group </td><td> +   `AWS::Scheduler::ScheduleGroup`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> scheduler:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="3"> Amazon EventBridge Schemas [schemas] </td><td> schemas:discoverer </td><td> +   `AWS::EventSchemas::Discoverer`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> schemas:registry </td><td> +   `AWS::EventSchemas::Registry`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> schemas:schema </td><td> +   `AWS::EventSchemas::Schema`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="3"> Amazon EventBridge [events] </td><td> events:event-bus </td><td> +   `AWS::Events::EventBus`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> events:rule </td><td> +   `AWS::Events::Rule`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> events:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="9"> Amazon FSx [fsx] </td><td> fsx:backup </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> fsx:storage-virtual-machine </td><td> +   `AWS::FSx::StorageVirtualMachine`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> fsx:snapshot </td><td> +   `AWS::FSx::Snapshot`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> fsx:file-system </td><td> +   `AWS::FSx::FileSystem`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> fsx:association </td><td> +   `AWS::FSx::DataRepositoryAssociation`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> fsx:file-cache </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> fsx:volume </td><td> +   `AWS::FSx::Volume`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> fsx:task </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> fsx:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="8"> Amazon FinSpace [finspace] </td><td> finspace:kxenvironment/kxdatabase/kxdataview </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> finspace:kxenvironment/kxuser </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> finspace:environment </td><td> +   `AWS::FinSpace::Environment`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> finspace:kxenvironment/kxdatabase </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> finspace:kxenvironment/kxvolume </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> finspace:kxenvironment </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> finspace:kxenvironment/kxscalinggroup </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> finspace:kxenvironment/kxcluster </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="14"> Amazon Forecast [forecast] </td><td> forecast:dataset-import-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> forecast:predictor-backtest-export-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> forecast:forecast-endpoint </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> forecast:dataset-group </td><td> +   `AWS::Forecast::DatasetGroup`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> forecast:what-if-forecast-export </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> forecast:monitor </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> forecast:forecast-export-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> forecast:dataset </td><td> +   `AWS::Forecast::Dataset`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> forecast:what-if-forecast </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> forecast:predictor </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> forecast:what-if-analysis </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> forecast:explainability </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> forecast:explainability-export </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> forecast:forecast </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="15"> Amazon Fraud Detector [frauddetector] </td><td> frauddetector:detector </td><td> +   `AWS::FraudDetector::Detector`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> frauddetector:detector-version </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> frauddetector:batch-prediction </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> frauddetector:label </td><td> +   `AWS::FraudDetector::Label`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> frauddetector:event-type </td><td> +   `AWS::FraudDetector::EventType`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> frauddetector:external-model </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> frauddetector:batch-import </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> frauddetector:entity-type </td><td> +   `AWS::FraudDetector::EntityType`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> frauddetector:outcome </td><td> +   `AWS::FraudDetector::Outcome`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> frauddetector:model-version </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> frauddetector:list </td><td> +   `AWS::FraudDetector::List`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> frauddetector:rule </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> frauddetector:variable </td><td> +   `AWS::FraudDetector::Variable`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> frauddetector:model </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> frauddetector:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> Amazon FreeRTOS [freertos] </td><td> freertos:subscription </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> freertos:configuration </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="11"> Amazon GameLift Servers [gamelift] </td><td> gamelift:script </td><td> +   `AWS::GameLift::Script`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> gamelift:build </td><td> +   `AWS::GameLift::Build`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> gamelift:containergroupdefinition </td><td> +   `AWS::GameLift::ContainerGroupDefinition`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> gamelift:gamesessionqueue </td><td> +   `AWS::GameLift::GameSessionQueue`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> gamelift:fleet </td><td> +   `AWS::GameLift::Fleet`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> gamelift:matchmakingruleset </td><td> +   `AWS::GameLift::MatchmakingRuleSet`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> gamelift:location </td><td> +   `AWS::GameLift::Location`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> gamelift:alias </td><td> +   `AWS::GameLift::Alias`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> gamelift:gameservergroup </td><td> +   `AWS::GameLift::GameServerGroup`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> gamelift:containerfleet </td><td> +   `AWS::GameLift::ContainerFleet`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> gamelift:matchmakingconfiguration </td><td> +   `AWS::GameLift::MatchmakingConfiguration`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> Amazon GameLift Streams [gameliftstreams] </td><td> gameliftstreams:application </td><td> +   `AWS::GameLiftStreams::Application`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> gameliftstreams:streamgroup </td><td> +   `AWS::GameLiftStreams::StreamGroup`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> Amazon GuardDuty [AWS] </td><td> AWS::GuardDuty::PublishingDestination </td><td> +   `AWS::GuardDuty::PublishingDestination`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="5"> Amazon GuardDuty [guardduty] </td><td> guardduty:malware-protection-plan </td><td> +   `AWS::GuardDuty::MalwareProtectionPlan`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> guardduty:detector </td><td> +   `AWS::GuardDuty::Detector`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> guardduty:detector/ipset </td><td> +   `AWS::GuardDuty::IPSet`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> guardduty:detector/threatintelset </td><td> +   `AWS::GuardDuty::ThreatIntelSet`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> guardduty:detector/filter </td><td> +   `AWS::GuardDuty::Filter`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="4"> Amazon Honeycode [honeycode] </td><td> honeycode:screen-automation </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> honeycode:workbook </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> honeycode:table </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> honeycode:screen </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="6"> Amazon Inspector [inspector2] </td><td> inspector2:codescan-configuration </td><td> +   `AWS::InspectorV2::CisScanConfiguration`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> inspector2:cis-configuration </td><td> +   `AWS::InspectorV2::CisScanConfiguration`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> inspector2:filter </td><td> +   `AWS::InspectorV2::Filter`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> inspector2:codesecurity-integration </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> inspector2:codesecurity-configuration </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> inspector2:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="13"> Amazon Interactive Video Service [ivs] </td><td> ivs:public-key </td><td> +   `AWS::IVS::PublicKey`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ivs:ingest-configuration </td><td> +   `AWS::IVS::IngestConfiguration`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ivs:recording-configuration </td><td> +   `AWS::IVS::RecordingConfiguration`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ivs:transcode-configuration </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ivs:chat-room </td><td> +   `AWS::IVSChat::Room`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ivs:playback-restriction-policy </td><td> +   `AWS::IVS::PlaybackRestrictionPolicy`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ivs:channel </td><td> +   `AWS::IVS::Channel`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ivs:playback-key </td><td> +   `AWS::IVS::PlaybackKeyPair`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ivs:stream-key </td><td> +   `AWS::IVS::StreamKey`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ivs:composition </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ivs:stage </td><td> +   `AWS::IVS::Stage`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ivs:storage-configuration </td><td> +   `AWS::IVS::StorageConfiguration`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ivs:encoder-configuration </td><td> +   `AWS::IVS::EncoderConfiguration`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> Amazon Kendra Intelligent Ranking [kendra-ranking] </td><td> kendra-ranking:rescore-execution-plan </td><td> +   `AWS::KendraRanking::ExecutionPlan`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="5"> Amazon Kendra [kendra] </td><td> kendra:index </td><td> +   `AWS::Kendra::Index`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> kendra:index/thesaurus </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> kendra:index/query-suggestions-block-list </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> kendra:index/data-source </td><td> +   `AWS::Kendra::DataSource`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> kendra:index/featured-results-set </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> Amazon Keyspaces (for Apache Cassandra) [cassandra] </td><td> cassandra:keyspace </td><td> +   `AWS::Cassandra::Keyspace`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> cassandra:table </td><td> +   `AWS::Cassandra::Table`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="3"> Amazon Kinesis Analytics [kinesisanalytics] </td><td> kinesisanalytics:application </td><td> +   `AWS::KinesisAnalytics::Application`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> kinesisanalytics:application </td><td> +   `AWS::KinesisAnalyticsV2::Application`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> kinesisanalytics:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> Amazon Kinesis Data Streams [kinesis] </td><td> kinesis:stream </td><td> +   `AWS::Kinesis::Stream`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> kinesis:stream/consumer </td><td> +   `AWS::Kinesis::StreamConsumer`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> Amazon Kinesis Firehose [firehose] </td><td> firehose:deliverystream </td><td> +   `AWS::KinesisFirehose::DeliveryStream`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> firehose:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> Amazon Kinesis Video Streams [kinesisvideo] </td><td> kinesisvideo:stream </td><td> +   `AWS::KinesisVideo::Stream`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> kinesisvideo:channel </td><td> +   `AWS::KinesisVideo::SignalingChannel`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="4"> Amazon Lex [lex] </td><td> lex:bot-channel </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> lex:test-set </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> lex:bot-alias </td><td> +   `AWS::Lex::BotAlias`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> lex:bot </td><td> +   `AWS::Lex::Bot`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="14"> Amazon Lightsail [lightsail] </td><td> lightsail:keypair </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> lightsail:distribution </td><td> +   `AWS::Lightsail::Distribution`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> lightsail:containerservice </td><td> +   `AWS::Lightsail::Container`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> lightsail:disksnapshot </td><td> +   `AWS::Lightsail::DiskSnapshot`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> lightsail:relationaldatabase </td><td> +   `AWS::Lightsail::Database`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> lightsail:certificate </td><td> +   `AWS::Lightsail::Certificate`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> lightsail:bucket </td><td> +   `AWS::Lightsail::Bucket`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> lightsail:instance </td><td> +   `AWS::Lightsail::Instance`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> lightsail:disk </td><td> +   `AWS::Lightsail::Disk`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> lightsail:loadbalancer </td><td> +   `AWS::Lightsail::LoadBalancer`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> lightsail:domain </td><td> +   `AWS::Lightsail::Domain`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> lightsail:instancesnapshot </td><td> +   `AWS::Lightsail::InstanceSnapshot`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> lightsail:relationaldatabasesnapshot </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> lightsail:staticip </td><td> +   `AWS::Lightsail::StaticIp`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="6"> Amazon Location [geo] </td><td> geo:geofence-collection </td><td> +   `AWS::Location::GeofenceCollection`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> geo:tracker </td><td> +   `AWS::Location::Tracker`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> geo:api-key </td><td> +   `AWS::Location::APIKey`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> geo:place-index </td><td> +   `AWS::Location::PlaceIndex`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> geo:route-calculator </td><td> +   `AWS::Location::RouteCalculator`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> geo:map </td><td> +   `AWS::Location::Map`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="4"> Amazon Lookout for Equipment [lookoutequipment] </td><td> lookoutequipment:dataset </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> lookoutequipment:label-group </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> lookoutequipment:inference-scheduler </td><td> +   `AWS::LookoutEquipment::InferenceScheduler`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> lookoutequipment:model </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="3"> Amazon Lookout for Metrics [lookoutmetrics] </td><td> lookoutmetrics:metricset </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> lookoutmetrics:anomalydetector </td><td> +   `AWS::LookoutMetrics::AnomalyDetector`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> lookoutmetrics:alert </td><td> +   `AWS::LookoutMetrics::Alert`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> Amazon Lookout for Vision [lookoutvision] </td><td> lookoutvision:model </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="3"> Amazon MQ [mq] </td><td> mq:configuration </td><td> +   `AWS::AmazonMQ::Configuration`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> mq:broker </td><td> +   `AWS::AmazonMQ::Broker`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> mq:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="4"> Amazon Machine Learning [machinelearning] </td><td> machinelearning:evaluation </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> machinelearning:mlmodel </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> machinelearning:batchprediction </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> machinelearning:datasource </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> Amazon Macie [macie2] </td><td> macie2:classification-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> macie2:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="5"> Amazon Macie [macie] </td><td> macie:allow-list </td><td> +   `AWS::Macie::AllowList`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> macie:member </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> macie:findings-filter </td><td> +   `AWS::Macie::FindingsFilter`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> macie:classification-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> macie:custom-data-identifier </td><td> +   `AWS::Macie::CustomDataIdentifier`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="6"> Amazon Managed Blockchain [managedblockchain] </td><td> managedblockchain:proposals </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> managedblockchain:members </td><td> +   `AWS::ManagedBlockchain::Member`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> managedblockchain:accessors </td><td> +   `AWS::ManagedBlockchain::Accessor`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> managedblockchain:networks </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> managedblockchain:nodes </td><td> +   `AWS::ManagedBlockchain::Node`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> managedblockchain:invitations </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> Amazon Managed Grafana [grafana] </td><td> grafana:workspaces </td><td> +   `AWS::Grafana::Workspace`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="4"> Amazon Managed Service for Prometheus [aps] </td><td> aps:scraper </td><td> +   `AWS::APS::Scraper`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> aps:anomalydetector </td><td> +   `AWS::APS::AnomalyDetector`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> aps:workspace </td><td> +   `AWS::APS::Workspace`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> aps:rulegroupsnamespace </td><td> +   `AWS::APS::RuleGroupsNamespace`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="3"> Amazon Managed Streaming for Apache Kafka [kafka] </td><td> kafka:vpc-connection </td><td> +   `AWS::MSK::VpcConnection`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> kafka:cluster </td><td> +   `AWS::MSK::Cluster`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> kafka:replicator </td><td> +   `AWS::MSK::Replicator`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="3"> Amazon Managed Streaming for Kafka Connect [kafkaconnect] </td><td> kafkaconnect:worker-configuration </td><td> +   `AWS::KafkaConnect::WorkerConfiguration`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> kafkaconnect:connector </td><td> +   `AWS::KafkaConnect::Connector`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> kafkaconnect:custom-plugin </td><td> +   `AWS::KafkaConnect::CustomPlugin`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> Amazon Managed Workflows for Apache Airflow [airflow] </td><td> airflow:environment </td><td> +   `AWS::MWAA::Environment`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="8"> Amazon MemoryDB [memorydb] </td><td> memorydb:cluster </td><td> +   `AWS::MemoryDB::Cluster`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> memorydb:acl </td><td> +   `AWS::MemoryDB::ACL`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> memorydb:subnetgroup </td><td> +   `AWS::MemoryDB::SubnetGroup`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> memorydb:reservednode </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> memorydb:multiregioncluster </td><td> +   `AWS::MemoryDB::MultiRegionCluster`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> memorydb:user </td><td> +   `AWS::MemoryDB::User`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> memorydb:parametergroup </td><td> +   `AWS::MemoryDB::ParameterGroup`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> memorydb:snapshot </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="6"> Amazon Nimble Studio [nimble] </td><td> nimble:studio </td><td> +   `AWS::NimbleStudio::Studio`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> nimble:launch-profile </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> nimble:streaming-session </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> nimble:streaming-session-backup </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> nimble:streaming-image </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> nimble:studio-component </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="3"> Amazon One Enterprise [one] </td><td> one:site </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> one:device-instance </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> one:device-configuration-template </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> Amazon OpenSearch Ingestion [osis] </td><td> osis:pipeline </td><td> +   `AWS::OSIS::Pipeline`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="3"> Amazon OpenSearch Serverless [aoss] </td><td> aoss:collection </td><td> +   `AWS::OpenSearchServerless::Collection`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> aoss:collection-group </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> aoss:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> Amazon OpenSearch [es] </td><td> es:domain </td><td> +   `AWS::Elasticsearch::Domain`  <br />+   `AWS::OpenSearchService::Domain`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> es:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> Amazon OpenSearch [opensearch] </td><td> opensearch:datasource </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="12"> Amazon Personalize [personalize] </td><td> personalize:data-deletion-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> personalize:dataset-group </td><td> +   `AWS::Personalize::DatasetGroup`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> personalize:batch-segment-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> personalize:campaign </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> personalize:recommender </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> personalize:batch-inference-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> personalize:event-tracker </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> personalize:dataset-import-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> personalize:dataset </td><td> +   `AWS::Personalize::Dataset`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> personalize:solution </td><td> +   `AWS::Personalize::Solution`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> personalize:filter </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> personalize:dataset-export-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="7"> Amazon Pinpoint SMS and Voice Service [sms-voice] </td><td> sms-voice:sender-id </td><td> +   `AWS::SMSVOICE::SenderId`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> sms-voice:protect-configuration </td><td> +   `AWS::SMSVOICE::ProtectConfiguration`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sms-voice:opt-out-list </td><td> +   `AWS::SMSVOICE::OptOutList`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> sms-voice:phone-number </td><td> +   `AWS::SMSVOICE::PhoneNumber`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> sms-voice:pool </td><td> +   `AWS::SMSVOICE::Pool`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> sms-voice:configuration-set </td><td> +   `AWS::SMSVOICE::ConfigurationSet`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> sms-voice:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> Amazon Pinpoint [mobiletargeting] </td><td> mobiletargeting:templates </td><td> +   `AWS::Pinpoint::SmsTemplate`  <br />+   `AWS::Pinpoint::PushTemplate`  <br />+   `AWS::Pinpoint::InAppTemplate`  <br />+   `AWS::Pinpoint::EmailTemplate`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> mobiletargeting:apps </td><td> +   `AWS::Pinpoint::App`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> Amazon Q Business Q Apps [qapps] </td><td> qapps:application/qapp/session </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> qapps:application/qapp </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="6"> Amazon Q Business [qbusiness] </td><td> qbusiness:application/plugin </td><td> +   `AWS::QBusiness::Plugin`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> qbusiness:application/retriever </td><td> +   `AWS::QBusiness::Retriever`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> qbusiness:application/index/data-source </td><td> +   `AWS::QBusiness::DataSource`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> qbusiness:application </td><td> +   `AWS::QBusiness::Application`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> qbusiness:application/web-experience </td><td> +   `AWS::QBusiness::WebExperience`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> qbusiness:application/index </td><td> +   `AWS::QBusiness::Index`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="12"> Amazon Q in Connect [wisdom] </td><td> wisdom:content-association </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> wisdom:content </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> wisdom:assistant </td><td> +   `AWS::Wisdom::Assistant`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> wisdom:quick-response </td><td> +   `AWS::Wisdom::QuickResponse`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> wisdom:ai-agent </td><td> +   `AWS::Wisdom::AIAgent`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> wisdom:message-template </td><td> +   `AWS::Wisdom::MessageTemplate`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> wisdom:knowledge-base </td><td> +   `AWS::Wisdom::KnowledgeBase`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> wisdom:session </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> wisdom:ai-prompt </td><td> +   `AWS::Wisdom::AIPrompt`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> wisdom:ai-guardrail </td><td> +   `AWS::Wisdom::AIGuardrail`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> wisdom:association </td><td> +   `AWS::Wisdom::AssistantAssociation`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> wisdom:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="3"> Amazon QLDB [qldb] </td><td> qldb:ledger </td><td> +   `AWS::QLDB::Ledger`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> qldb:stream </td><td> +   `AWS::QLDB::Stream`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> qldb:ledger/table </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="17"> Amazon QuickSight [quicksight] </td><td> quicksight:vpcconnection </td><td> +   `AWS::QuickSight::VPCConnection`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> quicksight:analysis </td><td> +   `AWS::QuickSight::Analysis`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> quicksight:folder </td><td> +   `AWS::QuickSight::Folder`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> quicksight:custompermissions </td><td> +   `AWS::QuickSight::CustomPermissions`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> quicksight:brand </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> quicksight:user </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> quicksight:datasource </td><td> +   `AWS::QuickSight::DataSource`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> quicksight:template </td><td> +   `AWS::QuickSight::Template`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> quicksight:topic </td><td> +   `AWS::QuickSight::Topic`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> quicksight:email-customization-template </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> quicksight:theme </td><td> +   `AWS::QuickSight::Theme`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> quicksight:customization </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> quicksight:flow </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> quicksight:action-connector </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> quicksight:namespace </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> quicksight:dataset </td><td> +   `AWS::QuickSight::DataSet`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> quicksight:dashboard </td><td> +   `AWS::QuickSight::Dashboard`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="3"> Amazon RDS [neptune-graph] </td><td> neptune-graph:export-task </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> neptune-graph:graph </td><td> +   `AWS::NeptuneGraph::Graph`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> neptune-graph:graph-snapshot </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="33"> Amazon RDS [rds] </td><td> rds:cluster-snapshot </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> rds:db </td><td> +   `AWS::DocDB::DBInstance`  <br />+   `AWS::RDS::DBInstance`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> rds:globalcluster </td><td> +   `AWS::RDS::GlobalCluster`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> rds:global-cluster </td><td> +   `AWS::RDS::GlobalCluster`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> rds:subgrp </td><td> +   `AWS::RDS::DBSubnetGroup`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> rds:cluster-auto-backup </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> rds:deployment </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> rds:pg </td><td> +   `AWS::Neptune::DBParameterGroup`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> rds:cluster-pg </td><td> +   `AWS::Neptune::DBClusterParameterGroup`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> rds:snapshot-tenant-database </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> rds:es </td><td> +   `AWS::DocDB::EventSubscription`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> rds:pg </td><td> +   `AWS::RDS::DBParameterGroup`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> rds:target-group </td><td> +   `AWS::RDS::DBProxyTargetGroup`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> rds:cluster </td><td> +   `AWS::DocDB::DBCluster`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> rds:snapshot </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> rds:db-proxy </td><td> +   `AWS::RDS::DBProxy`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> rds:es </td><td> +   `AWS::RDS::EventSubscription`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> rds:cluster-endpoint </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> rds:integration </td><td> +   `AWS::RDS::Integration`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> rds:ri </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> rds:auto-backup </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> rds:secgrp </td><td> +   `AWS::RDS::DBSecurityGroup`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> rds:cev </td><td> +   `AWS::RDS::CustomDBEngineVersion`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> rds:db-proxy-endpoint </td><td> +   `AWS::RDS::DBProxyEndpoint`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> rds:cluster-pg </td><td> +   `AWS::RDS::DBClusterParameterGroup`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> rds:optgrp </td><td> +   `AWS::RDS::OptionGroup`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> rds:og </td><td> +   `AWS::RDS::OptionGroup`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> rds:db </td><td> +   `AWS::Neptune::DBInstance`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> rds:subgrp </td><td> +   `AWS::DocDB::DBSubnetGroup`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> rds:tenant-database </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> rds:subgrp </td><td> +   `AWS::Neptune::DBSubnetGroup`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> rds:cluster-pg </td><td> +   `AWS::DocDB::DBClusterParameterGroup`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> rds:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="5"> Amazon Redshift Serverless [redshift-serverless] </td><td> redshift-serverless:recoverypoint </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> redshift-serverless:workgroup </td><td> +   `AWS::RedshiftServerless::Workgroup`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> redshift-serverless:namespace </td><td> +   `AWS::RedshiftServerless::Namespace`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> redshift-serverless:snapshot </td><td> +   `AWS::RedshiftServerless::Snapshot`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> redshift-serverless:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="17"> Amazon Redshift [redshift] </td><td> redshift:eventsubscription </td><td> +   `AWS::Redshift::EventSubscription`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> redshift:hsmconfiguration </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> redshift:subnetgroup </td><td> +   `AWS::Redshift::ClusterSubnetGroup`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> redshift:snapshotcopygrant </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> redshift:qev2idcapplication </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> redshift:securitygroupingress </td><td> +   `AWS::Redshift::ClusterSecurityGroupIngress`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> redshift:namespace </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> redshift:snapshotschedule </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> redshift:securitygroup </td><td> +   `AWS::Redshift::ClusterSecurityGroup`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> redshift:hsmclientcertificate </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> redshift:redshiftidcapplication </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> redshift:cluster </td><td> +   `AWS::Redshift::Cluster`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> redshift:snapshot </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> redshift:usagelimit </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> redshift:integration </td><td> +   `AWS::Redshift::Integration`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> redshift:parametergroup </td><td> +   `AWS::Redshift::ClusterParameterGroup`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> redshift:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="4"> Amazon Rekognition [rekognition] </td><td> rekognition:project/version </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> rekognition:project </td><td> +   `AWS::Rekognition::Project`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> rekognition:collection </td><td> +   `AWS::Rekognition::Collection`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> rekognition:streamprocessor </td><td> +   `AWS::Rekognition::StreamProcessor`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> Amazon Route 53 Profiles [route53profiles] </td><td> route53profiles:profile-association </td><td> +   `AWS::Route53Profiles::ProfileAssociation`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> route53profiles:profile </td><td> +   `AWS::Route53Profiles::Profile`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="3"> Amazon Route 53 Recovery Controls [route53-recovery-control] </td><td> route53-recovery-control:controlpanel/safetyrule </td><td> +   `AWS::Route53RecoveryControl::SafetyRule`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> route53-recovery-control:cluster </td><td> +   `AWS::Route53RecoveryControl::Cluster`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> route53-recovery-control:controlpanel </td><td> +   `AWS::Route53RecoveryControl::ControlPanel`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="4"> Amazon Route 53 Recovery Readiness [route53-recovery-readiness] </td><td> route53-recovery-readiness:recovery-group </td><td> +   `AWS::Route53RecoveryReadiness::RecoveryGroup`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> route53-recovery-readiness:readiness-check </td><td> +   `AWS::Route53RecoveryReadiness::ReadinessCheck`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> route53-recovery-readiness:cell </td><td> +   `AWS::Route53RecoveryReadiness::Cell`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> route53-recovery-readiness:resource-set </td><td> +   `AWS::Route53RecoveryReadiness::ResourceSet`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="8"> Amazon Route 53 Resolver [route53resolver] </td><td> route53resolver:resolver-rule </td><td> +   `AWS::Route53Resolver::ResolverRule`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> route53resolver:firewall-domain-list </td><td> +   `AWS::Route53Resolver::FirewallDomainList`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> route53resolver:resolver-endpoint </td><td> +   `AWS::Route53Resolver::ResolverEndpoint`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> route53resolver:resolver-query-log-config </td><td> +   `AWS::Route53Resolver::ResolverQueryLoggingConfig`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> route53resolver:firewall-rule-group </td><td> +   `AWS::Route53Resolver::FirewallRuleGroup`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> route53resolver:firewall-rule-group-association </td><td> +   `AWS::Route53Resolver::FirewallRuleGroupAssociation`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> route53resolver:outpost-resolver </td><td> +   `AWS::Route53Resolver::OutpostResolver`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> route53resolver:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="4"> Amazon Route 53 [route53] </td><td> route53:healthcheck </td><td> +   `AWS::Route53::HealthCheck`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> route53:domain </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> route53:hostedzone </td><td> +   `AWS::Route53::HostedZone`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> route53:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> Amazon S3 Express [s3express] </td><td> s3express:accesspoint </td><td> +   `AWS::S3Express::AccessPoint`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> s3express:bucket </td><td> +   `AWS::S3Express::DirectoryBucket`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> Amazon S3 Glacier [glacier] </td><td> glacier:vaults </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> Amazon S3 Tables [s3tables] </td><td> s3tables:TableBucket </td><td> +   `AWS::S3Tables::TableBucket`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> s3tables:table </td><td> +   `AWS::S3Tables::Table`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> Amazon S3 Vectors [s3vectors] </td><td> s3vectors:index </td><td> +   `AWS::S3Vectors::Index`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> s3vectors:vectorbucket </td><td> +   `AWS::S3Vectors::VectorBucket`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="10"> Amazon S3 [s3] </td><td> s3:accessgrantsinstance </td><td> +   `AWS::S3::AccessGrantsInstance`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> s3:bucket </td><td> +   `AWS::S3::Bucket`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> s3:job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> s3:access-grants </td><td> +   `AWS::S3::AccessGrant`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> s3:storage-lens </td><td> +   `AWS::S3::StorageLens`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> s3:access-grants/location </td><td> +   `AWS::S3::AccessGrantsLocation`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> s3:accessgrantslocation </td><td> +   `AWS::S3::AccessGrantsLocation`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> s3:storage-lens-group </td><td> +   `AWS::S3::StorageLensGroup`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> s3:accesspoint </td><td> +   `AWS::S3::AccessPoint`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> s3:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="10"> Amazon SES [ses] </td><td> ses:identity </td><td> +   `AWS::SES::EmailIdentity`  <br />+   `AWS::PinpointEmail::Identity`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ses:dedicated-ip-pool </td><td> +   `AWS::SES::DedicatedIpPool`  <br />+   `AWS::PinpointEmail::DedicatedIpPool`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ses:contact-list </td><td> +   `AWS::SES::ContactList`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ses:mailmanager-ingress-point </td><td> +   `AWS::SES::MailManagerIngressPoint`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ses:configuration-set </td><td> +   `AWS::SES::ConfigurationSet`  <br />+   `AWS::PinpointEmail::ConfigurationSet`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ses:mailmanager-address-list </td><td> +   `AWS::SES::MailManagerAddressList`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ses:multi-region-endpoint </td><td> +   `AWS::SES::MultiRegionEndpoint`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> ses:mailmanager-archive </td><td> +   `AWS::SES::MailManagerArchive`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ses:mailmanager-traffic-policy </td><td> +   `AWS::SES::MailManagerTrafficPolicy`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> ses:mailmanager-rule-set </td><td> +   `AWS::SES::MailManagerRuleSet`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> Amazon SNS [sns] </td><td> sns:topic </td><td> +   `AWS::SNS::Topic`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sns:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> Amazon SQS [sqs] </td><td> sqs:queue </td><td> +   `AWS::SQS::Queue`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sqs:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="64"> Amazon SageMaker [sagemaker] </td><td> sagemaker:image </td><td> +   `AWS::SageMaker::Image`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:model-quality-job-definition </td><td> +   `AWS::SageMaker::ModelQualityJobDefinition`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:monitoring-schedule </td><td> +   `AWS::SageMaker::MonitoringSchedule`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:transform-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:code-repository </td><td> +   `AWS::SageMaker::CodeRepository`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:imageversion </td><td> +   `AWS::SageMaker::ImageVersion`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:experiment </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:action </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:hyper-parameter-tuning-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:model-bias-job-definition </td><td> +   `AWS::SageMaker::ModelBiasJobDefinition`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:app-image-config </td><td> +   `AWS::SageMaker::AppImageConfig`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:model </td><td> +   `AWS::SageMaker::Model`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:training-plan </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:workforce </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:model-explainability-job-definition </td><td> +   `AWS::SageMaker::ModelExplainabilityJobDefinition`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:model-card </td><td> +   `AWS::SageMaker::ModelCard`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:model-card-export-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:notebook-instance-lifecycle-config </td><td> +   `AWS::SageMaker::NotebookInstanceLifecycleConfig`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:notebook-instance </td><td> +   `AWS::SageMaker::NotebookInstance`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:compilation-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:model-package </td><td> +   `AWS::SageMaker::ModelPackage`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:data-quality-job-definition </td><td> +   `AWS::SageMaker::DataQualityJobDefinition`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:user-profile </td><td> +   `AWS::SageMaker::UserProfile`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:domain </td><td> +   `AWS::SageMaker::Domain`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:mlflow-tracking-server </td><td> +   `AWS::SageMaker::MlflowTrackingServer`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:edge-packaging-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:cluster </td><td> +   `AWS::SageMaker::Cluster`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:device </td><td> +   `AWS::SageMaker::Device`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:feature-group </td><td> +   `AWS::SageMaker::FeatureGroup`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:artifact </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:studio-lifecycle-config </td><td> +   `AWS::SageMaker::StudioLifecycleConfig`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:cluster-scheduler-config </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:automl-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:app </td><td> +   `AWS::SageMaker::App`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:space </td><td> +   `AWS::SageMaker::Space`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:inference-component </td><td> +   `AWS::SageMaker::InferenceComponent`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:endpoint </td><td> +   `AWS::SageMaker::Endpoint`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:workteam </td><td> +   `AWS::SageMaker::Workteam`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:inference-experiment </td><td> +   `AWS::SageMaker::InferenceExperiment`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:optimization-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:algorithm </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:pipeline/execution </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:pipeline-execution </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:project </td><td> +   `AWS::SageMaker::Project`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:model-package-group </td><td> +   `AWS::SageMaker::ModelPackageGroup`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:labeling-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:edge-deployment </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:training-job </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:compute-quota </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:reserved-capacity </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:context </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:partner-app </td><td> +   `AWS::SageMaker::PartnerApp`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:experiment-trial </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:hub </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:flow-definition </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:pipeline </td><td> +   `AWS::SageMaker::Pipeline`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:lineage-group </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:inference-recommendations-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:device-fleet </td><td> +   `AWS::SageMaker::DeviceFleet`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:hub-content </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:experiment-trial-component </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker:endpoint-config </td><td> +   `AWS::SageMaker::EndpointConfig`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:processing-job </td><td> +   `AWS::SageMaker::ProcessingJob`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> sagemaker:human-task-ui </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="3"> Amazon SageMaker geospatial capabilities [sagemaker-geospatial] </td><td> sagemaker-geospatial:raster-data-collection </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker-geospatial:earth-observation-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> sagemaker-geospatial:vector-enrichment-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="3"> Amazon Security Lake [securitylake] </td><td> securitylake:data-lake </td><td> +   `AWS::SecurityLake::DataLake`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> securitylake:subscriber </td><td> +   `AWS::SecurityLake::Subscriber`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> securitylake:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> Amazon Simple Workflow Service [swf] </td><td> swf:domain </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> Amazon Textract [textract] </td><td> textract:adapters </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> textract:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> Amazon Timestream InfluxDB [timestream-influxdb] </td><td> timestream-influxdb:db-instance </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="3"> Amazon Timestream [timestream] </td><td> timestream:database </td><td> +   `AWS::Timestream::Database`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> timestream:database/table </td><td> +   `AWS::Timestream::Table`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> timestream:scheduled-query </td><td> +   `AWS::Timestream::ScheduledQuery`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="7"> Amazon Transcribe [transcribe] </td><td> transcribe:vocabulary-filter </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> transcribe:vocabulary </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> transcribe:transcription-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> transcribe:medical-transcription-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> transcribe:medical-vocabulary </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> transcribe:medical-scribe-job </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> transcribe:language-model </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> Amazon Translate [translate] </td><td> translate:parallel-data </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> translate:terminology </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="13"> Amazon VPC Lattice [vpc-lattice] </td><td> vpc-lattice:service/listener/rule </td><td> +   `AWS::VpcLattice::Rule`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> vpc-lattice:servicenetworkserviceassociation </td><td> +   `AWS::VpcLattice::ServiceNetworkServiceAssociation`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> vpc-lattice:service/listener </td><td> +   `AWS::VpcLattice::Listener`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> vpc-lattice:accesslogsubscription </td><td> +   `AWS::VpcLattice::AccessLogSubscription`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> vpc-lattice:servicenetworkresourceassociation </td><td> +   `AWS::VpcLattice::ServiceNetworkResourceAssociation`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> vpc-lattice:domainverification </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> vpc-lattice:resourceendpointassociation </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> vpc-lattice:servicenetworkvpcassociation </td><td> +   `AWS::VpcLattice::ServiceNetworkVpcAssociation`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> vpc-lattice:service </td><td> +   `AWS::VpcLattice::Service`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> vpc-lattice:servicenetwork </td><td> +   `AWS::VpcLattice::ServiceNetwork`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> vpc-lattice:resourceconfiguration </td><td> +   `AWS::VpcLattice::ResourceConfiguration`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> vpc-lattice:targetgroup </td><td> +   `AWS::VpcLattice::TargetGroup`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> vpc-lattice:resourcegateway </td><td> +   `AWS::VpcLattice::ResourceGateway`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> Amazon Verified Permissions [verifiedpermissions] </td><td> verifiedpermissions:policy-store </td><td> +   `AWS::VerifiedPermissions::PolicyStore`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> Amazon WorkLink [worklink] </td><td> worklink:fleet </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> Amazon WorkMail [workmail] </td><td> workmail:organization </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="10"> Amazon WorkSpaces Secure Browser [workspaces-web] </td><td> workspaces-web:portal </td><td> +   `AWS::WorkSpacesWeb::Portal`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> workspaces-web:ipaccesssettings </td><td> +   `AWS::WorkSpacesWeb::IpAccessSettings`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> workspaces-web:useraccessloggingsettings </td><td> +   `AWS::WorkSpacesWeb::UserAccessLoggingSettings`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> workspaces-web:dataprotectionsettings </td><td> +   `AWS::WorkSpacesWeb::DataProtectionSettings`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> workspaces-web:sessionlogger </td><td> +   `AWS::WorkSpacesWeb::SessionLogger`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> workspaces-web:usersettings </td><td> +   `AWS::WorkSpacesWeb::UserSettings`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> workspaces-web:browsersettings </td><td> +   `AWS::WorkSpacesWeb::BrowserSettings`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> workspaces-web:identityprovider </td><td> +   `AWS::WorkSpacesWeb::IdentityProvider`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> workspaces-web:networksettings </td><td> +   `AWS::WorkSpacesWeb::NetworkSettings`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> workspaces-web:truststore </td><td> +   `AWS::WorkSpacesWeb::TrustStore`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> Amazon WorkSpaces Secure Browser [workspacesweb] </td><td> workspacesweb:identityprovider </td><td> +   `AWS::WorkSpacesWeb::IdentityProvider`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="5"> Amazon WorkSpaces Thin Client [thinclient] </td><td> thinclient:environment </td><td> +   `AWS::WorkSpacesThinClient::Environment`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> thinclient:environments </td><td> +   `AWS::WorkSpacesThinClient::Environment`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> thinclient:device </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> thinclient:devices </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> thinclient:softwareset </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="8"> Amazon WorkSpaces [workspaces] </td><td> workspaces:directory </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> workspaces:workspace </td><td> +   `AWS::WorkSpaces::Workspace`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> workspaces:workspacebundle </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> workspaces:workspaceimage </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> workspaces:connectionalias </td><td> +   `AWS::WorkSpaces::ConnectionAlias`   </td><td> Yes </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> workspaces:workspacespool </td><td> +   `AWS::WorkSpaces::WorkspacesPool`   </td><td> Yes </td><td> No </td><td> Yes </td><td> Yes </td></tr>
  <tr><td> workspaces:workspaceipgroup </td><td> +   `N/A`   </td><td> Yes </td><td> Yes </td><td> No </td><td> No </td></tr>
  <tr><td> workspaces:ALL\_SUPPORTED </td><td> +   `N/A`   </td><td> No </td><td> Yes </td><td> Yes </td><td> Yes </td></tr>
  <tr><td rowspan="2"> Deprecated - AWS IoT 1-Click [iot1click] </td><td> iot1click:devices </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> iot1click:projects </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> Deprecated AWS IoT RoboRunner [iotroborunner] </td><td> iotroborunner:site </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> iotroborunner:site/worker-fleet </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td rowspan="2"> Multi-party approval [mpa] </td><td> mpa:approval-team </td><td> +   `AWS::MPA::ApprovalTeam`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> mpa:identity-source </td><td> +   `AWS::MPA::IdentitySource`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> Service Quotas [servicequotas] </td><td> servicequotas:quota </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
  <tr><td> route53globalresolver [route53globalresolver] </td><td> route53globalresolver:firewall-domain-list </td><td> +   `N/A`   </td><td> Yes </td><td> No </td><td> No </td><td> No </td></tr>
</tbody>
</table>

+ See [Terraform documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/guides/tag-policy-compliance) for resource type support in Terraform AWS Provider.
+ See [Pulumi documentation](https://www.pulumi.com/docs/insights/policy/integrations/aws-organizations-tag-policies/#aws-provider-types) for resource type support in Pulumi Cloud.
