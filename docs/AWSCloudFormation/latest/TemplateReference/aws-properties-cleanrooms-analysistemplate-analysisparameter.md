---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-analysistemplate-analysisparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::AnalysisTemplate AnalysisParameter
<a name="aws-properties-cleanrooms-analysistemplate-analysisparameter"></a>

Optional. The member who can query can provide this placeholder for a literal data value in an analysis template.

## Syntax
<a name="aws-properties-cleanrooms-analysistemplate-analysisparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-analysistemplate-analysisparameter-syntax.json"></a>

```
{
  "[DefaultValue](#cfn-cleanrooms-analysistemplate-analysisparameter-defaultvalue)" : {{String}},
  "[Name](#cfn-cleanrooms-analysistemplate-analysisparameter-name)" : {{String}},
  "[Type](#cfn-cleanrooms-analysistemplate-analysisparameter-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanrooms-analysistemplate-analysisparameter-syntax.yaml"></a>

```
  [DefaultValue](#cfn-cleanrooms-analysistemplate-analysisparameter-defaultvalue): {{String}}
  [Name](#cfn-cleanrooms-analysistemplate-analysisparameter-name): {{String}}
  [Type](#cfn-cleanrooms-analysistemplate-analysisparameter-type): {{String}}
```

## Properties
<a name="aws-properties-cleanrooms-analysistemplate-analysisparameter-properties"></a>

`DefaultValue`  <a name="cfn-cleanrooms-analysistemplate-analysisparameter-defaultvalue"></a>
Optional. The default value that is applied in the analysis template. The member who can query can override this value in the query editor.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-cleanrooms-analysistemplate-analysisparameter-name"></a>
The name of the parameter. The name must use only alphanumeric or underscore (\_) characters.
*Required*: Yes
*Type*: String
*Pattern*: `[0-9a-zA-Z_]+`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-cleanrooms-analysistemplate-analysisparameter-type"></a>
The type of parameter.
*Required*: Yes
*Type*: String
*Allowed values*: `SMALLINT | INTEGER | BIGINT | DECIMAL | REAL | DOUBLE_PRECISION | BOOLEAN | CHAR | VARCHAR | DATE | TIMESTAMP | TIMESTAMPTZ | TIME | TIMETZ | VARBYTE | BINARY | BYTE | CHARACTER | DOUBLE | FLOAT | INT | LONG | NUMERIC | SHORT | STRING | TIMESTAMP_LTZ | TIMESTAMP_NTZ | TINYINT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
