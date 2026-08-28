---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-oam-link-linkfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Oam::Link LinkFilter
<a name="aws-properties-oam-link-linkfilter"></a>

When used in `MetricConfiguration` this field specifies which metric namespaces are to be shared with the monitoring account

When used in `LogGroupConfiguration` this field specifies which log groups are to share their log events with the monitoring account. Use the term `LogGroupName` and one or more of the following operands.

## Syntax
<a name="aws-properties-oam-link-linkfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-oam-link-linkfilter-syntax.json"></a>

```
{
  "[Filter](#cfn-oam-link-linkfilter-filter)" : {{String}}
}
```

### YAML
<a name="aws-properties-oam-link-linkfilter-syntax.yaml"></a>

```
  [Filter](#cfn-oam-link-linkfilter-filter): {{String}}
```

## Properties
<a name="aws-properties-oam-link-linkfilter-properties"></a>

`Filter`  <a name="cfn-oam-link-linkfilter-filter"></a>
When used in `MetricConfiguration` this field specifies which metric namespaces are to be shared with the monitoring account
When used in `LogGroupConfiguration` this field specifies which log groups are to share their log events with the monitoring account. Use the term `LogGroupName` and one or more of the following operands.
Use single quotation marks (') around log group names and metric namespaces.
The matching of log group names and metric namespaces is case sensitive. Each filter has a limit of five conditional operands. Conditional operands are `AND` and `OR`.
+ `=` and `!=`
+  `AND`
+  `OR`
+ `LIKE` and `NOT LIKE`. These can be used only as prefix searches. Include a `%` at the end of the string that you want to search for and include.
+ `IN` and `NOT IN`, using parentheses `( )`
Examples:
+ `Namespace NOT LIKE 'AWS/%'` includes only namespaces that don't start with `AWS/`, such as custom namespaces.
+ `Namespace IN ('AWS/EC2', 'AWS/ELB', 'AWS/S3')` includes only the metrics in the EC2, Elastic Load Balancing, and Amazon S3 namespaces.
+ `Namespace = 'AWS/EC2' OR Namespace NOT LIKE 'AWS/%'` includes only the EC2 namespace and your custom namespaces.
+ `LogGroupName IN ('This-Log-Group', 'Other-Log-Group')` includes only the log groups with names `This-Log-Group` and `Other-Log-Group`.
+ `LogGroupName NOT IN ('Private-Log-Group', 'Private-Log-Group-2')` includes all log groups except the log groups with names `Private-Log-Group` and `Private-Log-Group-2`.
+ `LogGroupName LIKE 'aws/lambda/%' OR LogGroupName LIKE 'AWSLogs%'` includes all log groups that have names that start with `aws/lambda/` or `AWSLogs`.
If you are updating a link that uses filters, you can specify `*` as the only value for the `filter` parameter to delete the filter and share all log groups with the monitoring account.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
