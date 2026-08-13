---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-location-job-jobactionoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Location::Job JobActionOptions
<a name="aws-properties-location-job-jobactionoptions"></a>

Additional options for configuring job action parameters.

## Syntax
<a name="aws-properties-location-job-jobactionoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-location-job-jobactionoptions-syntax.json"></a>

```
{
  "[ValidateAddress](#cfn-location-job-jobactionoptions-validateaddress)" : {{ValidateAddressActionOptions}}
}
```

### YAML
<a name="aws-properties-location-job-jobactionoptions-syntax.yaml"></a>

```
  [ValidateAddress](#cfn-location-job-jobactionoptions-validateaddress): {{
    ValidateAddressActionOptions}}
```

## Properties
<a name="aws-properties-location-job-jobactionoptions-properties"></a>

`ValidateAddress`  <a name="cfn-location-job-jobactionoptions-validateaddress"></a>
Options specific to address validation jobs.
*Required*: No
*Type*: [ValidateAddressActionOptions](aws-properties-location-job-validateaddressactionoptions.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
