---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cleanrooms-analysistemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::AnalysisTemplate
<a name="aws-resource-cleanrooms-analysistemplate"></a>

Creates a new analysis template.

## Syntax
<a name="aws-resource-cleanrooms-analysistemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cleanrooms-analysistemplate-syntax.json"></a>

```
{
  "Type" : "AWS::CleanRooms::AnalysisTemplate",
  "Properties" : {
      "[AnalysisParameters](#cfn-cleanrooms-analysistemplate-analysisparameters)" : {{[ AnalysisParameter, ... ]}},
      "[Description](#cfn-cleanrooms-analysistemplate-description)" : {{String}},
      "[ErrorMessageConfiguration](#cfn-cleanrooms-analysistemplate-errormessageconfiguration)" : {{ErrorMessageConfiguration}},
      "[Format](#cfn-cleanrooms-analysistemplate-format)" : {{String}},
      "[MembershipIdentifier](#cfn-cleanrooms-analysistemplate-membershipidentifier)" : {{String}},
      "[Name](#cfn-cleanrooms-analysistemplate-name)" : {{String}},
      "[Schema](#cfn-cleanrooms-analysistemplate-schema)" : {{AnalysisSchema}},
      "[Source](#cfn-cleanrooms-analysistemplate-source)" : {{AnalysisSource}},
      "[SourceMetadata](#cfn-cleanrooms-analysistemplate-sourcemetadata)" : {{AnalysisSourceMetadata}},
      "[SyntheticDataParameters](#cfn-cleanrooms-analysistemplate-syntheticdataparameters)" : {{SyntheticDataParameters}},
      "[Tags](#cfn-cleanrooms-analysistemplate-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cleanrooms-analysistemplate-syntax.yaml"></a>

```
Type: AWS::CleanRooms::AnalysisTemplate
Properties:
  [AnalysisParameters](#cfn-cleanrooms-analysistemplate-analysisparameters): {{
    - AnalysisParameter}}
  [Description](#cfn-cleanrooms-analysistemplate-description): {{String}}
  [ErrorMessageConfiguration](#cfn-cleanrooms-analysistemplate-errormessageconfiguration): {{
    ErrorMessageConfiguration}}
  [Format](#cfn-cleanrooms-analysistemplate-format): {{String}}
  [MembershipIdentifier](#cfn-cleanrooms-analysistemplate-membershipidentifier): {{String}}
  [Name](#cfn-cleanrooms-analysistemplate-name): {{String}}
  [Schema](#cfn-cleanrooms-analysistemplate-schema): {{
    AnalysisSchema}}
  [Source](#cfn-cleanrooms-analysistemplate-source): {{
    AnalysisSource}}
  [SourceMetadata](#cfn-cleanrooms-analysistemplate-sourcemetadata): {{
    AnalysisSourceMetadata}}
  [SyntheticDataParameters](#cfn-cleanrooms-analysistemplate-syntheticdataparameters): {{
    SyntheticDataParameters}}
  [Tags](#cfn-cleanrooms-analysistemplate-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cleanrooms-analysistemplate-properties"></a>

`AnalysisParameters`  <a name="cfn-cleanrooms-analysistemplate-analysisparameters"></a>
The parameters of the analysis template.
*Required*: No
*Type*: Array of [AnalysisParameter](aws-properties-cleanrooms-analysistemplate-analysisparameter.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-cleanrooms-analysistemplate-description"></a>
The description of the analysis template.
*Required*: No
*Type*: String
*Pattern*: `^[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*$`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ErrorMessageConfiguration`  <a name="cfn-cleanrooms-analysistemplate-errormessageconfiguration"></a>
The configuration that specifies the level of detail in error messages returned by analyses using this template. When set to `DETAILED`, error messages include more information to help troubleshoot issues with PySpark jobs. Detailed error messages may expose underlying data, including sensitive information. Recommended for faster troubleshooting in development and testing environments.
*Required*: No
*Type*: [ErrorMessageConfiguration](aws-properties-cleanrooms-analysistemplate-errormessageconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Format`  <a name="cfn-cleanrooms-analysistemplate-format"></a>
The format of the analysis template.
*Required*: Yes
*Type*: String
*Allowed values*: `SQL | PYSPARK_1_0`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MembershipIdentifier`  <a name="cfn-cleanrooms-analysistemplate-membershipidentifier"></a>
The identifier for a membership resource.
*Required*: Yes
*Type*: String
*Pattern*: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-cleanrooms-analysistemplate-name"></a>
The name of the analysis template.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?$`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Schema`  <a name="cfn-cleanrooms-analysistemplate-schema"></a>
The entire schema object.
*Required*: No
*Type*: [AnalysisSchema](aws-properties-cleanrooms-analysistemplate-analysisschema.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Source`  <a name="cfn-cleanrooms-analysistemplate-source"></a>
The source of the analysis template.
*Required*: Yes
*Type*: [AnalysisSource](aws-properties-cleanrooms-analysistemplate-analysissource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceMetadata`  <a name="cfn-cleanrooms-analysistemplate-sourcemetadata"></a>
 The source metadata for the analysis template.
*Required*: No
*Type*: [AnalysisSourceMetadata](aws-properties-cleanrooms-analysistemplate-analysissourcemetadata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SyntheticDataParameters`  <a name="cfn-cleanrooms-analysistemplate-syntheticdataparameters"></a>
The parameters used to generate synthetic data for this analysis template.
*Required*: No
*Type*: [SyntheticDataParameters](aws-properties-cleanrooms-analysistemplate-syntheticdataparameters.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cleanrooms-analysistemplate-tags"></a>
An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-cleanrooms-analysistemplate-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cleanrooms-analysistemplate-return-values"></a>

### Ref
<a name="aws-resource-cleanrooms-analysistemplate-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `AnalysisTemplateIdentifier`, such as `a1b2c3d4-5678-90ab-cdef-EXAMPLE2222`. For example:

 `{ "Ref": "myAnalysisTemplate" }`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cleanrooms-analysistemplate-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cleanrooms-analysistemplate-return-values-fn--getatt-fn--getatt"></a>

`AnalysisTemplateIdentifier`  <a name="AnalysisTemplateIdentifier-fn::getatt"></a>
Returns the identifier for the analysis template.
Example: `a1b2c3d4-5678-90ab-cdef-EXAMPLE2222`

`Arn`  <a name="Arn-fn::getatt"></a>
Returns the Amazon Resource Name (ARN) of the analysis template.
Example: `arn:aws:cleanrooms:us-east-1:111122223333:membership/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/analysistemplates/a1b2c3d4-5678-90ab-cdef-EXAMPLE2222`

`CollaborationArn`  <a name="CollaborationArn-fn::getatt"></a>
Returns the unique ARN for the analysis template’s associated collaboration.
Example: `arn:aws:cleanrooms:us-east-1:111122223333:collaboration/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333`

`CollaborationIdentifier`  <a name="CollaborationIdentifier-fn::getatt"></a>
Returns the unique ID for the associated collaboration of the analysis template.
Example: `a1b2c3d4-5678-90ab-cdef-EXAMPLE33333`

`MembershipArn`  <a name="MembershipArn-fn::getatt"></a>
Returns the Amazon Resource Name (ARN) of the member who created the analysis template.
Example: `arn:aws:cleanrooms:us-east-1:111122223333:membership/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`

## Examples
<a name="aws-resource-cleanrooms-analysistemplate--examples"></a>

### Create an analysis template
<a name="aws-resource-cleanrooms-analysistemplate--examples--Create_an_analysis_template"></a>

The following example creates an analysis template.

#### JSON
<a name="aws-resource-cleanrooms-analysistemplate--examples--Create_an_analysis_template--json"></a>

```
{
    "ExampleAnalysisTemplate": {
        "Type": "AWS::CleanRooms::AnalysisTemplate",
        "Properties": {
            "MembershipIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE1111",
            "Name": "exampleAnalysisTemplate",
            "Description": "example description",
            "Source": {
                "Text": "SELECT * FROM cta1 WHERE cta1.column1 > :Param1 AND cta1.column2 like :Param2"
            },
            "Format": "SQL",
            "AnalysisParameters": [
                {
                    "Name": "Param1",
                    "Type": "SMALLINT",
                    "DefaultValue": 1
                },
                {
                    "Name": "Param2",
                    "Type": "CHAR"
                }
            ],
            "Tags": [
                {
                    "Key": "Hello",
                    "Value": "World"
                }
            ]
        }
    }
}
```

#### YAML
<a name="aws-resource-cleanrooms-analysistemplate--examples--Create_an_analysis_template--yaml"></a>

```
ExampleAnalysisTemplate:
    Type: 'AWS::CleanRooms::AnalysisTemplate'
    Properties:
      MembershipIdentifier: a1b2c3d4-5678-90ab-cdef-EXAMPLE1111
      Name: exampleAnalysisTemplate
      Description: example description
      Source:
        Text: SELECT * FROM cta1 WHERE cta1.column1 > :Param1 AND cta1.column2 like :Param2
      Format: SQL
      AnalysisParameters:
        - Name: Param1
          Type: SMALLINT
          DefaultValue: 1
        - Name: Param2
          Type: CHAR
      Tags:
        - Key: Hello
          Value: World
```
