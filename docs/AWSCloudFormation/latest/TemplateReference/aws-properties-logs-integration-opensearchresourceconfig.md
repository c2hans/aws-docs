---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-integration-opensearchresourceconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Integration OpenSearchResourceConfig
<a name="aws-properties-logs-integration-opensearchresourceconfig"></a>

This structure contains configuration details about an integration between CloudWatch Logs and OpenSearch Service.

## Syntax
<a name="aws-properties-logs-integration-opensearchresourceconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-integration-opensearchresourceconfig-syntax.json"></a>

```
{
  "[ApplicationARN](#cfn-logs-integration-opensearchresourceconfig-applicationarn)" : {{String}},
  "[DashboardViewerPrincipals](#cfn-logs-integration-opensearchresourceconfig-dashboardviewerprincipals)" : {{[ String, ... ]}},
  "[DataSourceRoleArn](#cfn-logs-integration-opensearchresourceconfig-datasourcerolearn)" : {{String}},
  "[KmsKeyArn](#cfn-logs-integration-opensearchresourceconfig-kmskeyarn)" : {{String}},
  "[RetentionDays](#cfn-logs-integration-opensearchresourceconfig-retentiondays)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-logs-integration-opensearchresourceconfig-syntax.yaml"></a>

```
  [ApplicationARN](#cfn-logs-integration-opensearchresourceconfig-applicationarn): {{String}}
  [DashboardViewerPrincipals](#cfn-logs-integration-opensearchresourceconfig-dashboardviewerprincipals): {{
    - String}}
  [DataSourceRoleArn](#cfn-logs-integration-opensearchresourceconfig-datasourcerolearn): {{String}}
  [KmsKeyArn](#cfn-logs-integration-opensearchresourceconfig-kmskeyarn): {{String}}
  [RetentionDays](#cfn-logs-integration-opensearchresourceconfig-retentiondays): {{Integer}}
```

## Properties
<a name="aws-properties-logs-integration-opensearchresourceconfig-properties"></a>

`ApplicationARN`  <a name="cfn-logs-integration-opensearchresourceconfig-applicationarn"></a>
If you want to use an existing OpenSearch Service application for your integration with OpenSearch Service, specify it here. If you omit this, a new application will be created.
*Required*: No
*Type*: String
*Pattern*: `[\w#+=/:,.@-]*\*?`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DashboardViewerPrincipals`  <a name="cfn-logs-integration-opensearchresourceconfig-dashboardviewerprincipals"></a>
Specify the ARNs of IAM roles and IAM users who you want to grant permission to for viewing the dashboards.
In addition to specifying these users here, you must also grant them the **CloudWatchOpenSearchDashboardAccess** IAM policy. For more information, see [IAM policies for users](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/OpenSearch-Dashboards-UserRoles.html).
*Required*: Yes
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataSourceRoleArn`  <a name="cfn-logs-integration-opensearchresourceconfig-datasourcerolearn"></a>
Specify the ARN of an IAM role that CloudWatch Logs will use to create the integration. This role must have the permissions necessary to access the OpenSearch Service collection to be able to create the dashboards. For more information about the permissions needed, see [Permissions that the integration needs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/OpenSearch-Dashboards-CreateRole.html) in the CloudWatch Logs User Guide.
*Required*: Yes
*Type*: String
*Pattern*: `[\w#+=/:,.@-]*\*?`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyArn`  <a name="cfn-logs-integration-opensearchresourceconfig-kmskeyarn"></a>
To have the vended dashboard data encrypted with AWS KMS instead of the CloudWatch Logs default encryption method, specify the ARN of the AWS KMS key that you want to use.
*Required*: No
*Type*: String
*Pattern*: `[\w#+=/:,.@-]*\*?`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RetentionDays`  <a name="cfn-logs-integration-opensearchresourceconfig-retentiondays"></a>
Specify how many days that you want the data derived by OpenSearch Service to be retained in the index that the dashboard refers to. This also sets the maximum time period that you can choose when viewing data in the dashboard. Choosing a longer time frame will incur additional costs.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `3650`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
