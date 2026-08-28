---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-athena-namedquery.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Athena::NamedQuery
<a name="aws-resource-athena-namedquery"></a>

The `AWS::Athena::NamedQuery` resource specifies an Amazon Athena saved query, where `QueryString` contains the SQL query statements that make up the query.

## Syntax
<a name="aws-resource-athena-namedquery-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-athena-namedquery-syntax.json"></a>

```
{
  "Type" : "AWS::Athena::NamedQuery",
  "Properties" : {
      "[Database](#cfn-athena-namedquery-database)" : {{String}},
      "[Description](#cfn-athena-namedquery-description)" : {{String}},
      "[Name](#cfn-athena-namedquery-name)" : {{String}},
      "[QueryString](#cfn-athena-namedquery-querystring)" : {{String}},
      "[WorkGroup](#cfn-athena-namedquery-workgroup)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-athena-namedquery-syntax.yaml"></a>

```
Type: AWS::Athena::NamedQuery
Properties:
  [Database](#cfn-athena-namedquery-database): {{String}}
  [Description](#cfn-athena-namedquery-description): {{String}}
  [Name](#cfn-athena-namedquery-name): {{String}}
  [QueryString](#cfn-athena-namedquery-querystring): {{
    String}}
  [WorkGroup](#cfn-athena-namedquery-workgroup): {{String}}
```

## Properties
<a name="aws-resource-athena-namedquery-properties"></a>

`Database`  <a name="cfn-athena-namedquery-database"></a>
The database to which the query belongs.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-athena-namedquery-description"></a>
The query description.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-athena-namedquery-name"></a>
The query name.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`QueryString`  <a name="cfn-athena-namedquery-querystring"></a>
The SQL statements that make up the query.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `262144`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WorkGroup`  <a name="cfn-athena-namedquery-workgroup"></a>
The name of the workgroup that contains the named query.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-athena-namedquery-return-values"></a>

### Ref
<a name="aws-resource-athena-namedquery-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-athena-namedquery-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-athena-namedquery-return-values-fn--getatt-fn--getatt"></a>

`NamedQueryId`  <a name="NamedQueryId-fn::getatt"></a>
The unique ID of the query.

## Examples
<a name="aws-resource-athena-namedquery--examples"></a>

### Create a named query
<a name="aws-resource-athena-namedquery--examples--Create_a_named_query"></a>

The following example creates a named query.

#### JSON
<a name="aws-resource-athena-namedquery--examples--Create_a_named_query--json"></a>

```
{
    "Resources": {
        "AthenaNamedQuery": {
            "Type": "AWS::Athena::NamedQuery",
            "Properties": {
                "Database": "swfmetadata",
                "Description": "A query that selects all aggregated data",
                "Name": "MostExpensiveWorkflow",
                "QueryString": "SELECT workflowname, AVG(activitytaskstarted) AS AverageWorkflow FROM swfmetadata WHERE year='17' AND GROUP BY workflowname ORDER BY AverageWorkflow DESC LIMIT 10"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-athena-namedquery--examples--Create_a_named_query--yaml"></a>

```
Resources:
  AthenaNamedQuery:
    Type: AWS::Athena::NamedQuery
    Properties:
      Database: "swfmetadata"
      Description: "A query that selects all aggregated data"
      Name: "MostExpensiveWorkflow"
      QueryString: >
                    SELECT workflowname, AVG(activitytaskstarted) AS AverageWorkflow
                    FROM swfmetadata
                    WHERE year='17' AND GROUP BY workflowname
                    ORDER BY AverageWorkflow DESC LIMIT 10
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
