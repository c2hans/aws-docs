---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-processor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer Processor
<a name="aws-properties-logs-transformer-processor"></a>

This structure contains the information about one processor in a log transformer.

## Syntax
<a name="aws-properties-logs-transformer-processor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-processor-syntax.json"></a>

```
{
  "[AddKeys](#cfn-logs-transformer-processor-addkeys)" : {{AddKeys}},
  "[CopyValue](#cfn-logs-transformer-processor-copyvalue)" : {{CopyValue}},
  "[Csv](#cfn-logs-transformer-processor-csv)" : {{Csv}},
  "[DateTimeConverter](#cfn-logs-transformer-processor-datetimeconverter)" : {{DateTimeConverter}},
  "[DeleteKeys](#cfn-logs-transformer-processor-deletekeys)" : {{DeleteKeys}},
  "[Grok](#cfn-logs-transformer-processor-grok)" : {{Grok}},
  "[ListToMap](#cfn-logs-transformer-processor-listtomap)" : {{ListToMap}},
  "[LowerCaseString](#cfn-logs-transformer-processor-lowercasestring)" : {{LowerCaseString}},
  "[MoveKeys](#cfn-logs-transformer-processor-movekeys)" : {{MoveKeys}},
  "[ParseCloudfront](#cfn-logs-transformer-processor-parsecloudfront)" : {{ParseCloudfront}},
  "[ParseJSON](#cfn-logs-transformer-processor-parsejson)" : {{ParseJSON}},
  "[ParseKeyValue](#cfn-logs-transformer-processor-parsekeyvalue)" : {{ParseKeyValue}},
  "[ParsePostgres](#cfn-logs-transformer-processor-parsepostgres)" : {{ParsePostgres}},
  "[ParseRoute53](#cfn-logs-transformer-processor-parseroute53)" : {{ParseRoute53}},
  "[ParseToOCSF](#cfn-logs-transformer-processor-parsetoocsf)" : {{ParseToOCSF}},
  "[ParseVPC](#cfn-logs-transformer-processor-parsevpc)" : {{ParseVPC}},
  "[ParseWAF](#cfn-logs-transformer-processor-parsewaf)" : {{ParseWAF}},
  "[RenameKeys](#cfn-logs-transformer-processor-renamekeys)" : {{RenameKeys}},
  "[SplitString](#cfn-logs-transformer-processor-splitstring)" : {{SplitString}},
  "[SubstituteString](#cfn-logs-transformer-processor-substitutestring)" : {{SubstituteString}},
  "[TrimString](#cfn-logs-transformer-processor-trimstring)" : {{TrimString}},
  "[TypeConverter](#cfn-logs-transformer-processor-typeconverter)" : {{TypeConverter}},
  "[UpperCaseString](#cfn-logs-transformer-processor-uppercasestring)" : {{UpperCaseString}}
}
```

### YAML
<a name="aws-properties-logs-transformer-processor-syntax.yaml"></a>

```
  [AddKeys](#cfn-logs-transformer-processor-addkeys): {{
    AddKeys}}
  [CopyValue](#cfn-logs-transformer-processor-copyvalue): {{
    CopyValue}}
  [Csv](#cfn-logs-transformer-processor-csv): {{
    Csv}}
  [DateTimeConverter](#cfn-logs-transformer-processor-datetimeconverter): {{
    DateTimeConverter}}
  [DeleteKeys](#cfn-logs-transformer-processor-deletekeys): {{
    DeleteKeys}}
  [Grok](#cfn-logs-transformer-processor-grok): {{
    Grok}}
  [ListToMap](#cfn-logs-transformer-processor-listtomap): {{
    ListToMap}}
  [LowerCaseString](#cfn-logs-transformer-processor-lowercasestring): {{
    LowerCaseString}}
  [MoveKeys](#cfn-logs-transformer-processor-movekeys): {{
    MoveKeys}}
  [ParseCloudfront](#cfn-logs-transformer-processor-parsecloudfront): {{
    ParseCloudfront}}
  [ParseJSON](#cfn-logs-transformer-processor-parsejson): {{
    ParseJSON}}
  [ParseKeyValue](#cfn-logs-transformer-processor-parsekeyvalue): {{
    ParseKeyValue}}
  [ParsePostgres](#cfn-logs-transformer-processor-parsepostgres): {{
    ParsePostgres}}
  [ParseRoute53](#cfn-logs-transformer-processor-parseroute53): {{
    ParseRoute53}}
  [ParseToOCSF](#cfn-logs-transformer-processor-parsetoocsf): {{
    ParseToOCSF}}
  [ParseVPC](#cfn-logs-transformer-processor-parsevpc): {{
    ParseVPC}}
  [ParseWAF](#cfn-logs-transformer-processor-parsewaf): {{
    ParseWAF}}
  [RenameKeys](#cfn-logs-transformer-processor-renamekeys): {{
    RenameKeys}}
  [SplitString](#cfn-logs-transformer-processor-splitstring): {{
    SplitString}}
  [SubstituteString](#cfn-logs-transformer-processor-substitutestring): {{
    SubstituteString}}
  [TrimString](#cfn-logs-transformer-processor-trimstring): {{
    TrimString}}
  [TypeConverter](#cfn-logs-transformer-processor-typeconverter): {{
    TypeConverter}}
  [UpperCaseString](#cfn-logs-transformer-processor-uppercasestring): {{
    UpperCaseString}}
```

## Properties
<a name="aws-properties-logs-transformer-processor-properties"></a>

`AddKeys`  <a name="cfn-logs-transformer-processor-addkeys"></a>
Use this parameter to include the [ addKeys](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-addKeys) processor in your transformer.
*Required*: No
*Type*: [AddKeys](aws-properties-logs-transformer-addkeys.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CopyValue`  <a name="cfn-logs-transformer-processor-copyvalue"></a>
Use this parameter to include the [ copyValue](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-copyValue) processor in your transformer.
*Required*: No
*Type*: [CopyValue](aws-properties-logs-transformer-copyvalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Csv`  <a name="cfn-logs-transformer-processor-csv"></a>
Use this parameter to include the [ CSV](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-CSV) processor in your transformer.
*Required*: No
*Type*: [Csv](aws-properties-logs-transformer-csv.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DateTimeConverter`  <a name="cfn-logs-transformer-processor-datetimeconverter"></a>
Use this parameter to include the [ datetimeConverter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-datetimeConverter) processor in your transformer.
*Required*: No
*Type*: [DateTimeConverter](aws-properties-logs-transformer-datetimeconverter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeleteKeys`  <a name="cfn-logs-transformer-processor-deletekeys"></a>
Use this parameter to include the [ deleteKeys](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-deleteKeys) processor in your transformer.
*Required*: No
*Type*: [DeleteKeys](aws-properties-logs-transformer-deletekeys.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Grok`  <a name="cfn-logs-transformer-processor-grok"></a>
Use this parameter to include the [ grok](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-grok) processor in your transformer.
*Required*: No
*Type*: [Grok](aws-properties-logs-transformer-grok.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ListToMap`  <a name="cfn-logs-transformer-processor-listtomap"></a>
Use this parameter to include the [ listToMap](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-listToMap) processor in your transformer.
*Required*: No
*Type*: [ListToMap](aws-properties-logs-transformer-listtomap.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LowerCaseString`  <a name="cfn-logs-transformer-processor-lowercasestring"></a>
Use this parameter to include the [ lowerCaseString](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-lowerCaseString) processor in your transformer.
*Required*: No
*Type*: [LowerCaseString](aws-properties-logs-transformer-lowercasestring.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MoveKeys`  <a name="cfn-logs-transformer-processor-movekeys"></a>
Use this parameter to include the [ moveKeys](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-moveKeys) processor in your transformer.
*Required*: No
*Type*: [MoveKeys](aws-properties-logs-transformer-movekeys.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParseCloudfront`  <a name="cfn-logs-transformer-processor-parsecloudfront"></a>
Use this parameter to include the [ parseCloudfront](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-parseCloudfront) processor in your transformer.
If you use this processor, it must be the first processor in your transformer.
*Required*: No
*Type*: [ParseCloudfront](aws-properties-logs-transformer-parsecloudfront.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParseJSON`  <a name="cfn-logs-transformer-processor-parsejson"></a>
Use this parameter to include the [ parseJSON](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-parseJSON) processor in your transformer.
*Required*: No
*Type*: [ParseJSON](aws-properties-logs-transformer-parsejson.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParseKeyValue`  <a name="cfn-logs-transformer-processor-parsekeyvalue"></a>
Use this parameter to include the [ parseKeyValue](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-parseKeyValue) processor in your transformer.
*Required*: No
*Type*: [ParseKeyValue](aws-properties-logs-transformer-parsekeyvalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParsePostgres`  <a name="cfn-logs-transformer-processor-parsepostgres"></a>
Use this parameter to include the [ parsePostGres](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parsePostGres) processor in your transformer.
If you use this processor, it must be the first processor in your transformer.
*Required*: No
*Type*: [ParsePostgres](aws-properties-logs-transformer-parsepostgres.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParseRoute53`  <a name="cfn-logs-transformer-processor-parseroute53"></a>
Use this parameter to include the [ parseRoute53](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-parseRoute53) processor in your transformer.
If you use this processor, it must be the first processor in your transformer.
*Required*: No
*Type*: [ParseRoute53](aws-properties-logs-transformer-parseroute53.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParseToOCSF`  <a name="cfn-logs-transformer-processor-parsetoocsf"></a>
Use this parameter to convert logs into Open Cybersecurity Schema (OCSF) format.
*Required*: No
*Type*: [ParseToOCSF](aws-properties-logs-transformer-parsetoocsf.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParseVPC`  <a name="cfn-logs-transformer-processor-parsevpc"></a>
Use this parameter to include the [ parseVPC](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-parseVPC) processor in your transformer.
If you use this processor, it must be the first processor in your transformer.
*Required*: No
*Type*: [ParseVPC](aws-properties-logs-transformer-parsevpc.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParseWAF`  <a name="cfn-logs-transformer-processor-parsewaf"></a>
Use this parameter to include the [ parseWAF](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseWAF) processor in your transformer.
If you use this processor, it must be the first processor in your transformer.
*Required*: No
*Type*: [ParseWAF](aws-properties-logs-transformer-parsewaf.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RenameKeys`  <a name="cfn-logs-transformer-processor-renamekeys"></a>
Use this parameter to include the [ renameKeys](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-renameKeys) processor in your transformer.
*Required*: No
*Type*: [RenameKeys](aws-properties-logs-transformer-renamekeys.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SplitString`  <a name="cfn-logs-transformer-processor-splitstring"></a>
Use this parameter to include the [ splitString](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-splitString) processor in your transformer.
*Required*: No
*Type*: [SplitString](aws-properties-logs-transformer-splitstring.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubstituteString`  <a name="cfn-logs-transformer-processor-substitutestring"></a>
Use this parameter to include the [ substituteString](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-substituteString) processor in your transformer.
*Required*: No
*Type*: [SubstituteString](aws-properties-logs-transformer-substitutestring.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrimString`  <a name="cfn-logs-transformer-processor-trimstring"></a>
Use this parameter to include the [ trimString](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-trimString) processor in your transformer.
*Required*: No
*Type*: [TrimString](aws-properties-logs-transformer-trimstring.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TypeConverter`  <a name="cfn-logs-transformer-processor-typeconverter"></a>
Use this parameter to include the [ typeConverter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-typeConverter) processor in your transformer.
*Required*: No
*Type*: [TypeConverter](aws-properties-logs-transformer-typeconverter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpperCaseString`  <a name="cfn-logs-transformer-processor-uppercasestring"></a>
Use this parameter to include the [ upperCaseString](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-upperCaseString) processor in your transformer.
*Required*: No
*Type*: [UpperCaseString](aws-properties-logs-transformer-uppercasestring.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
