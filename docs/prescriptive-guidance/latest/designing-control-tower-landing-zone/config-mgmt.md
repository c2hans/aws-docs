---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-control-tower-landing-zone/config-mgmt.html
---

# Managing the configuration of AWS resources
<a name="config-mgmt"></a>

The [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) service enables you to assess, audit, and evaluate the configurations of your AWS resources. It provides a detailed view of how your resources are configured, shows how they relate to one another, and tracks how these configurations change over time. It's similar to a configuration management database that continuously monitors and records your AWS resource configurations, making it easier to audit resource compliance, analyze security postures, and troubleshoot configuration changes across your AWS environment. This service helps you maintain security and governance by tracking resource inventory, configuration history, and configuration change notifications to enable security and regulatory compliance.

## Track resource configuration changes
<a name="track-changes"></a>

AWS Control Tower enables [AWS Config configuration recorders](https://docs.aws.amazon.com/config/latest/developerguide/stop-start-recorder.html) in all enrolled accounts to track resource configuration changes. For landing zone versions 3.0 and later, global resources (such as IAM users, groups, roles, and customer-managed policies) are recorded only in the home Region. For landing zone versions earlier than 3.0, these global resources are recorded in all enabled Regions. Each AWS Config recorder is set up with a [delivery channel](https://docs.aws.amazon.com/config/latest/developerguide/manage-delivery-channel.html) that sends all configuration changes to a centralized Amazon S3 bucket in the Log Archive account. This provides comprehensive tracking of resource configuration changes across the organization. For more information about how AWS Control Tower monitors resource changes with AWS Config, see [Monitor resource changes with AWS Config](https://docs.aws.amazon.com/controltower/latest/userguide/monitoring-with-config.html) in the AWS Control Tower documentation.

AWS Config configuration recorders are enabled by default by AWS Control Tower and set to continuous recording for all relevant AWS resource types in enrolled accounts. If you are concerned about the [costs incurred by ](https://aws.amazon.com/config/pricing/)AWS Config, you might want to [manage these costs](https://docs.aws.amazon.com/controltower/latest/userguide/config-costs.html). For information about a solution that you can deploy in your landing zone without causing AWS Control Tower drift, see the AWS blog post [Customize AWS Config resource tracking in AWS Control Tower environment](https://aws.amazon.com/blogs/mt/customize-aws-config-resource-tracking-in-aws-control-tower-environment/).

## View configuration and compliance data
<a name="view-data"></a>

[AWS Config aggregators](https://docs.aws.amazon.com/config/latest/developerguide/aggregate-data.html) provide a centralized way to view configuration and compliance data from multiple AWS accounts and Regions. They act as a central collector that consolidates AWS Config data across your organization and makes it easier to monitor resource configurations and compliance at scale. This capability is particularly valuable for enterprises that manage multiple AWS accounts, because it enables centralized auditing, governance, and compliance monitoring across their entire AWS footprint. An AWS Control Tower setup with landing zone versions earlier than 4.0 creates two AWS Config aggregators to help manage and monitor your multi-account environment:
+ **Organization-level aggregator** (`aws-controltower-ConfigAggregatorForOrganizations`) is created in the management account of your AWS organization. Its primary purpose is to aggregate AWS Config data from all accounts in your organization, even if those accounts aren't enrolled in AWS Control Tower. AWS Config isn't enabled in the management account by default, so you can't see this aggregator in the AWS Config console. To view the aggregator in the management account, use the AWS CLI command:

  ```
   aws configservice describe-configuration-aggregators
  ```
+ **Security aggregator** (`aws-controltower-GuardRailsComplianceAggregator`) is created in the Audit account of your AWS Control Tower environment. Its primary purpose is to monitor compliance with AWS Control Tower guardrails. It aggregates the relevant AWS Config data from all accounts that are enrolled in AWS Control Tower.

These aggregators are supported in landing zone 3.3 and previous versions. In landing zone version 4.0, AWS Control Tower has migrated to a service-linked configuration aggregator (SLCA).

When you migrate to landing zone version 4.0 with AWS Config integration enabled, you will see the following changes:
+ The existing Audit account is registered as a delegated admin for AWS Config.
+ The SLCA is deployed into the AWS Config integration account. (This is the AWS Config central aggregator account for new customers and the Audit account for existing customers.) The SLCA can aggregate data from any AWS Config recorder in an organization, including accounts that aren't managed by AWS Control Tower.
+ Existing aggregators are deleted. The organization-level aggregator in the management account (`aws-controltower-ConfigAggregatorForOrganizations`) and the security aggregator in the Audit account (`aws-controltower-GuardRailsComplianceAggregator`) are deleted as part of the migration.
+ The following controls that are associated with the deleted aggregators are automatically removed.
  + [Disallow Changes to Tags Created by AWS Control Tower for AWS Config Resources](https://docs.aws.amazon.com/controltower/latest/controlreference/mandatory-controls.html#cloudwatch-disallow-config-changes)
  + [Disallow Deletion of AWS Config Aggregation Authorizations Created by AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/controlreference/mandatory-controls.html#config-aggregation-authorization-policy)
  + [Disallow Changes to AWS Config Rules Set Up by AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/controlreference/mandatory-controls.html#config-rule-disallow-changes)

Additionally, because AWS Config rules and the configuration aggregator are service-linked resources, service control policy (SCP) protection is longer required.
