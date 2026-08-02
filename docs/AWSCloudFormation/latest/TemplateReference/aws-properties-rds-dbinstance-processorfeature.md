---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rds-dbinstance-processorfeature.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::DBInstance ProcessorFeature
<a name="aws-properties-rds-dbinstance-processorfeature"></a>

The `ProcessorFeature` property type specifies the processor features of a DB instance class.

## Syntax
<a name="aws-properties-rds-dbinstance-processorfeature-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rds-dbinstance-processorfeature-syntax.json"></a>

```
{
  "[Name](#cfn-rds-dbinstance-processorfeature-name)" : {{String}},
  "[Value](#cfn-rds-dbinstance-processorfeature-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-rds-dbinstance-processorfeature-syntax.yaml"></a>

```
  [Name](#cfn-rds-dbinstance-processorfeature-name): {{String}}
  [Value](#cfn-rds-dbinstance-processorfeature-value): {{String}}
```

## Properties
<a name="aws-properties-rds-dbinstance-processorfeature-properties"></a>

`Name`  <a name="cfn-rds-dbinstance-processorfeature-name"></a>
The name of the processor feature. Valid names are `coreCount` and `threadsPerCore`.
*Required*: No
*Type*: String
*Allowed values*: `coreCount | threadsPerCore`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-rds-dbinstance-processorfeature-value"></a>
The value of a processor feature.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-rds-dbinstance-processorfeature--examples"></a>

The following example specifies processor features of an Oracle DB instance class.

### Authentication details
<a name="aws-properties-rds-dbinstance-processorfeature--examples--Authentication_details"></a>

#### JSON
<a name="aws-properties-rds-dbinstance-processorfeature--examples--Authentication_details--json"></a>

```
"ProcessorFeatures":[
   {
      "Name": "threadsPerCore",
      "Value": "4"
   },
   {
      "Name": "coreCount",
      "Value": "4"
   }
]
```

#### YAML
<a name="aws-properties-rds-dbinstance-processorfeature--examples--Authentication_details--yaml"></a>

```
ProcessorFeatures:
  - Name: threadsPerCore
    Value: 4
  - Name: coreCount
    Value: 4
```
