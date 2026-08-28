---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshiftserverless-workgroup-workgroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RedshiftServerless::Workgroup Workgroup
<a name="aws-properties-redshiftserverless-workgroup-workgroup"></a>

The collection of computing resources from which an endpoint is created.

## Syntax
<a name="aws-properties-redshiftserverless-workgroup-workgroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshiftserverless-workgroup-workgroup-syntax.json"></a>

```
{
  "[BaseCapacity](#cfn-redshiftserverless-workgroup-workgroup-basecapacity)" : {{Integer}},
  "[ConfigParameters](#cfn-redshiftserverless-workgroup-workgroup-configparameters)" : {{[ ConfigParameter, ... ]}},
  "[CreationDate](#cfn-redshiftserverless-workgroup-workgroup-creationdate)" : {{String}},
  "[Endpoint](#cfn-redshiftserverless-workgroup-workgroup-endpoint)" : {{Endpoint}},
  "[EnhancedVpcRouting](#cfn-redshiftserverless-workgroup-workgroup-enhancedvpcrouting)" : {{Boolean}},
  "[MaxCapacity](#cfn-redshiftserverless-workgroup-workgroup-maxcapacity)" : {{Integer}},
  "[NamespaceName](#cfn-redshiftserverless-workgroup-workgroup-namespacename)" : {{String}},
  "[PricePerformanceTarget](#cfn-redshiftserverless-workgroup-workgroup-priceperformancetarget)" : {{PerformanceTarget}},
  "[PubliclyAccessible](#cfn-redshiftserverless-workgroup-workgroup-publiclyaccessible)" : {{Boolean}},
  "[SecurityGroupIds](#cfn-redshiftserverless-workgroup-workgroup-securitygroupids)" : {{[ String, ... ]}},
  "[Status](#cfn-redshiftserverless-workgroup-workgroup-status)" : {{String}},
  "[SubnetIds](#cfn-redshiftserverless-workgroup-workgroup-subnetids)" : {{[ String, ... ]}},
  "[TrackName](#cfn-redshiftserverless-workgroup-workgroup-trackname)" : {{String}},
  "[WorkgroupArn](#cfn-redshiftserverless-workgroup-workgroup-workgrouparn)" : {{String}},
  "[WorkgroupId](#cfn-redshiftserverless-workgroup-workgroup-workgroupid)" : {{String}},
  "[WorkgroupName](#cfn-redshiftserverless-workgroup-workgroup-workgroupname)" : {{String}}
}
```

### YAML
<a name="aws-properties-redshiftserverless-workgroup-workgroup-syntax.yaml"></a>

```
  [BaseCapacity](#cfn-redshiftserverless-workgroup-workgroup-basecapacity): {{Integer}}
  [ConfigParameters](#cfn-redshiftserverless-workgroup-workgroup-configparameters): {{
    - ConfigParameter}}
  [CreationDate](#cfn-redshiftserverless-workgroup-workgroup-creationdate): {{String}}
  [Endpoint](#cfn-redshiftserverless-workgroup-workgroup-endpoint): {{
    Endpoint}}
  [EnhancedVpcRouting](#cfn-redshiftserverless-workgroup-workgroup-enhancedvpcrouting): {{Boolean}}
  [MaxCapacity](#cfn-redshiftserverless-workgroup-workgroup-maxcapacity): {{Integer}}
  [NamespaceName](#cfn-redshiftserverless-workgroup-workgroup-namespacename): {{String}}
  [PricePerformanceTarget](#cfn-redshiftserverless-workgroup-workgroup-priceperformancetarget): {{
    PerformanceTarget}}
  [PubliclyAccessible](#cfn-redshiftserverless-workgroup-workgroup-publiclyaccessible): {{Boolean}}
  [SecurityGroupIds](#cfn-redshiftserverless-workgroup-workgroup-securitygroupids): {{
    - String}}
  [Status](#cfn-redshiftserverless-workgroup-workgroup-status): {{String}}
  [SubnetIds](#cfn-redshiftserverless-workgroup-workgroup-subnetids): {{
    - String}}
  [TrackName](#cfn-redshiftserverless-workgroup-workgroup-trackname): {{String}}
  [WorkgroupArn](#cfn-redshiftserverless-workgroup-workgroup-workgrouparn): {{String}}
  [WorkgroupId](#cfn-redshiftserverless-workgroup-workgroup-workgroupid): {{String}}
  [WorkgroupName](#cfn-redshiftserverless-workgroup-workgroup-workgroupname): {{String}}
```

## Properties
<a name="aws-properties-redshiftserverless-workgroup-workgroup-properties"></a>

`BaseCapacity`  <a name="cfn-redshiftserverless-workgroup-workgroup-basecapacity"></a>
The base data warehouse capacity of the workgroup in Redshift Processing Units (RPUs).
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConfigParameters`  <a name="cfn-redshiftserverless-workgroup-workgroup-configparameters"></a>
An array of parameters to set for advanced control over a database. The options are `auto_mv`, `datestyle`, `enable_case_sensitive_identifier`, `enable_user_activity_logging`, `query_group`, `search_path`, `require_ssl`, `use_fips_ssl`, and either `wlm_json_configuration` or query monitoring metrics that let you define performance boundaries. You can either specify individual query monitoring metrics (such as `max_scan_row_count`, `max_query_execution_time`) or use `wlm_json_configuration` to define query queues with rules, but not both. If you're using `wlm_json_configuration`, the maximum size of `parameterValue` is 8000 characters. For more information about query monitoring rules and available metrics, see [ Query monitoring metrics for Amazon Redshift Serverless](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless).
*Required*: No
*Type*: Array of [ConfigParameter](aws-properties-redshiftserverless-workgroup-configparameter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreationDate`  <a name="cfn-redshiftserverless-workgroup-workgroup-creationdate"></a>
The creation date of the workgroup.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Endpoint`  <a name="cfn-redshiftserverless-workgroup-workgroup-endpoint"></a>
The endpoint that is created from the workgroup.
*Required*: No
*Type*: [Endpoint](aws-properties-redshiftserverless-workgroup-endpoint.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnhancedVpcRouting`  <a name="cfn-redshiftserverless-workgroup-workgroup-enhancedvpcrouting"></a>
The value that specifies whether to enable enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxCapacity`  <a name="cfn-redshiftserverless-workgroup-workgroup-maxcapacity"></a>
The maximum data-warehouse capacity Amazon Redshift Serverless uses to serve queries. The max capacity is specified in RPUs.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NamespaceName`  <a name="cfn-redshiftserverless-workgroup-workgroup-namespacename"></a>
The namespace the workgroup is associated with.
*Required*: No
*Type*: String
*Pattern*: `^[a-z0-9-]+$`
*Minimum*: `3`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PricePerformanceTarget`  <a name="cfn-redshiftserverless-workgroup-workgroup-priceperformancetarget"></a>
An object that represents the price performance target settings for the workgroup.
*Required*: No
*Type*: [PerformanceTarget](aws-properties-redshiftserverless-workgroup-performancetarget.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PubliclyAccessible`  <a name="cfn-redshiftserverless-workgroup-workgroup-publiclyaccessible"></a>
A value that specifies whether the workgroup can be accessible from a public network.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroupIds`  <a name="cfn-redshiftserverless-workgroup-workgroup-securitygroupids"></a>
An array of security group IDs to associate with the workgroup.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-redshiftserverless-workgroup-workgroup-status"></a>
The status of the workgroup.
*Required*: No
*Type*: String
*Allowed values*: `CREATING | AVAILABLE | MODIFYING | DELETING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetIds`  <a name="cfn-redshiftserverless-workgroup-workgroup-subnetids"></a>
An array of subnet IDs the workgroup is associated with.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrackName`  <a name="cfn-redshiftserverless-workgroup-workgroup-trackname"></a>
The name of the track for the workgroup.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkgroupArn`  <a name="cfn-redshiftserverless-workgroup-workgroup-workgrouparn"></a>
The Amazon Resource Name (ARN) that links to the workgroup.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkgroupId`  <a name="cfn-redshiftserverless-workgroup-workgroup-workgroupid"></a>
The unique identifier of the workgroup.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkgroupName`  <a name="cfn-redshiftserverless-workgroup-workgroup-workgroupname"></a>
The name of the workgroup.
*Required*: No
*Type*: String
*Pattern*: `^[a-z0-9-]*$`
*Minimum*: `3`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
