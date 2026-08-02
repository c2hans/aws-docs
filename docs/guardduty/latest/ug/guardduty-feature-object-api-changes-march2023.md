---
source_url: https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-feature-object-api-changes-march2023.html
---

# GuardDuty API changes in March 2023
<a name="guardduty-feature-object-api-changes-march2023"></a>

The GuardDuty APIs configure protection features that don't belong to the list of [GuardDuty foundational data sources](guardduty_data-sources.md). A feature object contains feature details, such as feature name and status, and may contain additional configuration for some of the protection plans. This migration affects the following APIs in the *Amazon GuardDuty API Reference*:
+ [CreateDetector](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateDetector.html)
+ [GetDetector](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetDetector.html)
+ [UpdateDetector](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateDetector.html)
+ [GetMemberDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetMemberDetectors.html)
+ [UpdateMemberDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateMemberDetectors.html)
+ [DescribeOrganizationConfiguration](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DescribeOrganizationConfiguration.html)
+ [UpdateOrganizationConfiguration](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateOrganizationConfiguration.html)
+ [GetRemainingFreeTrialDays](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetRemainingFreeTrialDays.html)
+ [GetUsageStatistics](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetUsageStatistics.html)

## Features compared to data sources
<a name="comparison-datasources-features-activation"></a>

Historically, all GuardDuty features were passed through a `dataSources` object in the API. From March 2023, GuardDuty prefers `features` object instead of the `dataSources` object in the API. All earlier data sources have corresponding features, but newer features may not have corresponding data sources.

The following list shows the comparison between `dataSources` and `features` object when passed through an API:
+ The `dataSources` object contains objects for each protection type and its status. The `features` object is a list of available features that correspond to each protection type within GuardDuty.

  Starting March 2023, feature activation will be the only way to configure new GuardDuty features in your AWS environment.
+ The `dataSources` schema in the API request or response is the same in each AWS Region where GuardDuty is available. However, every feature may not be available in each Region. Therefore, the available feature names may differ based on the Region.

## Understanding how APIs with features work
<a name="understanding-how-feature-activation-works"></a>

The GuardDuty APIs will continue to return a `dataSources` object as applicable, and they will also return a `features` object containing the same information in a different format. GuardDuty features launched before March 2023 will be available through `dataSources` object and `features` object. GuardDuty launched features since March 2023 will only be available through the `features` object. You can't create or update a detector, or describe your AWS Organizations using both `dataSources` and `features` object notation in the same API request. To enable GuardDuty protection types, you will need to migrate your existing data sources to the `features` object by using the same APIs that now include the `features` object too.

**Note**
GuardDuty will not add new data source after this modification.

GuardDuty has deprecated the use of data sources that are associated with the protection plans. However, it still supports the [GuardDuty foundational data sources](guardduty_data-sources.md). The GuardDuty best practices recommend using features for enabling or editing the configuration for any protection plan in your account.

## Incorporating feature changes in APIs
<a name="features-activation-incorporating-changes"></a>
+ If you manage GuardDuty configurations through APIs, SDKs, or CloudFormation template, and want to enable potential new GuardDuty features, you will need to modify your code and template, respectively. For more information, see the updated APIs in the *[Amazon GuardDuty API Reference](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Operations.html)*.
+ For GuardDuty features configured prior to this upgrade, you can continue using the APIs, SDKs, or CloudFormation template. However, we recommend that you switch to using `feature` object.

  All the data sources have an equivalent feature object. For more information, see [Mapping `dataSources` to `features`](#guardduty-feature-enablement-datasource-relation).
+ Presently, `additionalConfiguration` in the `features` object is only available for certain protection types.
  + For such protection types, if your feature's `AdditionalConfiguration` `status` is set to `ENABLED` but your feature's configuration `status` is not set to `ENABLED`, GuardDuty will not take any action in this case.
  + The following APIs get impacted by this:
    + [UpdateDetector](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateDetector.html)
    + [UpdateMemberDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateMemberDetectors.html)
    + [UpdateOrganizationConfiguration](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateOrganizationConfiguration.html)

## Mapping `dataSources` to `features`
<a name="guardduty-feature-enablement-datasource-relation"></a>

The following table shows the mapping of protection types, `dataSources`, and `features`.

<table>
<thead>
  <tr><th>GuardDuty protection type</th><th>Data source name\*</th><th>Feature name</th></tr>
</thead>
<tbody>
  <tr><td>[VPC Flow Logs](guardduty_data-sources.md#guardduty_vpc)</td><td>`flowLogs` (read only; can't be modified)</td><td>`FLOW_LOGS` (read only; can't be modified)</td></tr>
  <tr><td>[Route53 Resolver DNS query logs](guardduty_data-sources.md#guardduty_dns)</td><td>`dnsLogs` (read only; can't be modified)</td><td>`DNS_LOGS` (read only; can't be modified)</td></tr>
  <tr><td>[CloudTrail events](guardduty_data-sources.md#guardduty_controlplane)</td><td>`cloudTrail` (read only; can't be modified)</td><td>`CLOUD_TRAIL` (read only; can't be modified)</td></tr>
  <tr><td>[S3](s3-protection.md)</td><td>`s3Logs`</td><td>`S3_DATA_EVENTS`</td></tr>
  <tr><td>[EKS Protection](kubernetes-protection.md)</td><td>`kubernetes.auditlogs`</td><td>`EKS_AUDIT_LOGS`</td></tr>
  <tr><td>[Malware Protection for EC2](malware-protection.md)</td><td>`malwareProtection.scanEc2InstanceWithFindings.ebsVolumes`</td><td>`EBS_MALWARE_PROTECTION`</td></tr>
  <tr><td>[RDS Login events](rds-protection.md)</td><td rowspan="7">GuardDuty provides only feature activation support for these protection types.</td><td>`RDS_LOGIN_EVENTS`</td></tr>
  <tr><td>EKS Runtime Monitoring</td><td>`EKS_RUNTIME_MONITORING`</td></tr>
  <tr><td>[Runtime Monitoring](runtime-monitoring.md)</td><td>`RUNTIME_MONITORING`</td></tr>
  <tr><td>GuardDuty security agent for Amazon EKS clusters</td><td>`EKS_RUNTIME_MONITORING.additionalConfiguration.EKS_ADDON_MANAGEMENT`<br />`RUNTIME_MONITORING.additionalConfiguration.EKS_ADDON_MANAGEMENT`</td></tr>
  <tr><td>GuardDuty security agent for Amazon ECS-Fargate clusters</td><td>`RUNTIME_MONITORING.additionalConfiguration.ECS_FARGATE_AGENT_MANAGEMENT`</td></tr>
  <tr><td>GuardDuty security agent for Amazon EC2 instances</td><td>`RUNTIME_MONITORING.additionalConfiguration.EC2_AGENT_MANAGEMENT`</td></tr>
  <tr><td>[Lambda Protection](lambda-protection.md)</td><td>`LAMBDA_NETWORK_LOGS`</td></tr>
</tbody>
</table>

\*GetUsageStatistics uses its own `dataSource` names. For more information, see [Monitoring GuardDuty Usage and Estimating Costs](monitoring_costs.md) or [https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetUsageStatistics.html](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetUsageStatistics.html).
