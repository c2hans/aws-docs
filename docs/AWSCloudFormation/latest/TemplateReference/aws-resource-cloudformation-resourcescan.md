---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-resourcescan.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::ResourceScan
<a name="aws-resource-cloudformation-resourcescan"></a>

<a name="aws-resource-cloudformation-resourcescan-description"></a>The `AWS::CloudFormation::ResourceScan` resource Property description not available. for CloudFormation.

## Syntax
<a name="aws-resource-cloudformation-resourcescan-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudformation-resourcescan-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFormation::ResourceScan",
  "Properties" : {
      "[ScanFilters](#cfn-cloudformation-resourcescan-scanfilters)" : {{[ ScanFilter, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cloudformation-resourcescan-syntax.yaml"></a>

```
Type: AWS::CloudFormation::ResourceScan
Properties:
  [ScanFilters](#cfn-cloudformation-resourcescan-scanfilters): {{
    - ScanFilter}}
```

## Properties
<a name="aws-resource-cloudformation-resourcescan-properties"></a>

`ScanFilters`  <a name="cfn-cloudformation-resourcescan-scanfilters"></a>
Property description not available.
*Required*: No
*Type*: Array of [ScanFilter](aws-properties-cloudformation-resourcescan-scanfilter.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-cloudformation-resourcescan-return-values"></a>

### Ref
<a name="aws-resource-cloudformation-resourcescan-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-cloudformation-resourcescan-return-values-fn--getatt"></a>

####
<a name="aws-resource-cloudformation-resourcescan-return-values-fn--getatt-fn--getatt"></a>

`PercentageCompleted`  <a name="PercentageCompleted-fn::getatt"></a>
The percentage of the resource scan that has been completed.

`ResourceScanId`  <a name="ResourceScanId-fn::getatt"></a>
The Amazon Resource Name (ARN) of the resource scan.

`ScanId`  <a name="ScanId-fn::getatt"></a>
Property description not available.

`StartTime`  <a name="StartTime-fn::getatt"></a>
The time that the resource scan was started.

`Status`  <a name="Status-fn::getatt"></a>
Status of the resource scan.
 **IN\_PROGRESS**
The resource scan is still in progress.
 **COMPLETE**
The resource scan is complete.
 **EXPIRED**
The resource scan has expired.
 **FAILED**
The resource scan has failed.
