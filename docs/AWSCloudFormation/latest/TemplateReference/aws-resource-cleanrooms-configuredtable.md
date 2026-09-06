---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cleanrooms-configuredtable.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::ConfiguredTable
<a name="aws-resource-cleanrooms-configuredtable"></a>

Creates a new configured table resource.

## Syntax
<a name="aws-resource-cleanrooms-configuredtable-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cleanrooms-configuredtable-syntax.json"></a>

```
{
  "Type" : "AWS::CleanRooms::ConfiguredTable",
  "Properties" : {
      "[AllowedColumns](#cfn-cleanrooms-configuredtable-allowedcolumns)" : {{[ String, ... ]}},
      "[AnalysisMethod](#cfn-cleanrooms-configuredtable-analysismethod)" : {{String}},
      "[AnalysisRules](#cfn-cleanrooms-configuredtable-analysisrules)" : {{[ AnalysisRule, ... ]}},
      "[Description](#cfn-cleanrooms-configuredtable-description)" : {{String}},
      "[Name](#cfn-cleanrooms-configuredtable-name)" : {{String}},
      "[SelectedAnalysisMethods](#cfn-cleanrooms-configuredtable-selectedanalysismethods)" : {{[ String, ... ]}},
      "[TableReference](#cfn-cleanrooms-configuredtable-tablereference)" : {{TableReference}},
      "[Tags](#cfn-cleanrooms-configuredtable-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cleanrooms-configuredtable-syntax.yaml"></a>

```
Type: AWS::CleanRooms::ConfiguredTable
Properties:
  [AllowedColumns](#cfn-cleanrooms-configuredtable-allowedcolumns): {{
    - String}}
  [AnalysisMethod](#cfn-cleanrooms-configuredtable-analysismethod): {{String}}
  [AnalysisRules](#cfn-cleanrooms-configuredtable-analysisrules): {{
    - AnalysisRule}}
  [Description](#cfn-cleanrooms-configuredtable-description): {{String}}
  [Name](#cfn-cleanrooms-configuredtable-name): {{String}}
  [SelectedAnalysisMethods](#cfn-cleanrooms-configuredtable-selectedanalysismethods): {{
    - String}}
  [TableReference](#cfn-cleanrooms-configuredtable-tablereference): {{
    TableReference}}
  [Tags](#cfn-cleanrooms-configuredtable-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cleanrooms-configuredtable-properties"></a>

`AllowedColumns`  <a name="cfn-cleanrooms-configuredtable-allowedcolumns"></a>
The columns within the underlying AWS Glue table that can be used within collaborations.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `128 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AnalysisMethod`  <a name="cfn-cleanrooms-configuredtable-analysismethod"></a>
The analysis method for the configured table.
`DIRECT_QUERY` allows SQL queries to be run directly on this table.
`DIRECT_JOB` allows PySpark jobs to be run directly on this table.
`MULTIPLE` allows both SQL queries and PySpark jobs to be run directly on this table.
*Required*: Yes
*Type*: String
*Allowed values*: `DIRECT_QUERY | DIRECT_JOB | MULTIPLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AnalysisRules`  <a name="cfn-cleanrooms-configuredtable-analysisrules"></a>
The analysis rule that was created for the configured table.
*Required*: No
*Type*: Array of [AnalysisRule](aws-properties-cleanrooms-configuredtable-analysisrule.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-cleanrooms-configuredtable-description"></a>
A description for the configured table.
*Required*: No
*Type*: String
*Pattern*: `^[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*$`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-cleanrooms-configuredtable-name"></a>
A name for the configured table.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectedAnalysisMethods`  <a name="cfn-cleanrooms-configuredtable-selectedanalysismethods"></a>
 The selected analysis methods for the configured table.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableReference`  <a name="cfn-cleanrooms-configuredtable-tablereference"></a>
The table that this configured table represents.
*Required*: Yes
*Type*: [TableReference](aws-properties-cleanrooms-configuredtable-tablereference.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-cleanrooms-configuredtable-tags"></a>
An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-cleanrooms-configuredtable-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cleanrooms-configuredtable-return-values"></a>

### Ref
<a name="aws-resource-cleanrooms-configuredtable-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name. For example:

 `{"Ref": "MyConfiguredTable"}`

For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cleanrooms-configuredtable-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cleanrooms-configuredtable-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Returns the Amazon Resource Name (ARN) of the specified configured table.
Example: `arn:aws:cleanrooms:us-east-1:111122223333:configuredtable/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`

`ConfiguredTableIdentifier`  <a name="ConfiguredTableIdentifier-fn::getatt"></a>
Returns the unique identifier of the specified configured table.
Example: `a1b2c3d4-5678-90ab-cdef-EXAMPLE33333`

## Examples
<a name="aws-resource-cleanrooms-configuredtable--examples"></a>

### A configured table using a list analysis rule
<a name="aws-resource-cleanrooms-configuredtable--examples--A_configured_table_using_a_list_analysis_rule"></a>

The following is an example of a configured table with a list analysis rule applied.

#### JSON
<a name="aws-resource-cleanrooms-configuredtable--examples--A_configured_table_using_a_list_analysis_rule--json"></a>

```
"ListConfiguredTable": {
  {
    "Type" : "AWS::CleanRooms::ConfiguredTable",
    "Properties" : {
        "Name" : "List Table",
        "Description" : "Example configured table with list AR",
        "AllowedColumns" : ["column1", "column2", "column4"],
        "AnalysisMethod" : "DIRECT_QUERY",
        "AnalysisRules" : [
          "Type": "LIST",
          "Policy": {
            "V1": {
              "List": {
                "JoinColumns": [
                  "column1"
                ],
                "ListColumns": [
                  "column2"
                ]
              }
            }
          }
        ],
        "TableReference" : {
          "Glue": {
            "DatabaseName": "ExampleDB",
            "TableName": "ExampleTable"
          }
        }
      }
  }
}
```

#### YAML
<a name="aws-resource-cleanrooms-configuredtable--examples--A_configured_table_using_a_list_analysis_rule--yaml"></a>

```
ListConfiguredTable:
  Type: AWS::CleanRooms::ConfiguredTable
  Properties:
    Name: List Table
    Description: Example configured table with list AR
    AllowedColumns:
      - column1
      - column2
      - column4
    AnalysisMethod: DIRECT_QUERY
    AnalysisRules:
      - Type: LIST
        Policy:
          V1:
            List:
              JoinColumns:
                - column1
              ListColumns:
                - column2
    TableReference:
      Glue:
        DatabaseName: ExampleDB
        TableName: ExampleTable
```
