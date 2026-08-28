---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshiftserverless-workgroup-configparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RedshiftServerless::Workgroup ConfigParameter
<a name="aws-properties-redshiftserverless-workgroup-configparameter"></a>

A array of parameters to set for more control over a serverless database.

## Syntax
<a name="aws-properties-redshiftserverless-workgroup-configparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshiftserverless-workgroup-configparameter-syntax.json"></a>

```
{
  "[ParameterKey](#cfn-redshiftserverless-workgroup-configparameter-parameterkey)" : {{String}},
  "[ParameterValue](#cfn-redshiftserverless-workgroup-configparameter-parametervalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-redshiftserverless-workgroup-configparameter-syntax.yaml"></a>

```
  [ParameterKey](#cfn-redshiftserverless-workgroup-configparameter-parameterkey): {{String}}
  [ParameterValue](#cfn-redshiftserverless-workgroup-configparameter-parametervalue): {{String}}
```

## Properties
<a name="aws-properties-redshiftserverless-workgroup-configparameter-properties"></a>

`ParameterKey`  <a name="cfn-redshiftserverless-workgroup-configparameter-parameterkey"></a>
The key of the parameter. The options are `auto_mv`, `datestyle`, `enable_case_sensitive_identifier`, `enable_user_activity_logging`, `query_group`, `search_path`, `require_ssl`, `use_fips_ssl`, and query monitoring metrics that let you define performance boundaries. For more information about query monitoring rules and available metrics, see [ Query monitoring metrics for Amazon Redshift Serverless ](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless).
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterValue`  <a name="cfn-redshiftserverless-workgroup-configparameter-parametervalue"></a>
The value of the parameter to set.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `15000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
