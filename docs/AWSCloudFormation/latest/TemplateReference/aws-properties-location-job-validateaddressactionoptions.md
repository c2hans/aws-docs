---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-location-job-validateaddressactionoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Location::Job ValidateAddressActionOptions
<a name="aws-properties-location-job-validateaddressactionoptions"></a>

Options specific to address validation jobs.

## Syntax
<a name="aws-properties-location-job-validateaddressactionoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-location-job-validateaddressactionoptions-syntax.json"></a>

```
{
  "[AdditionalFeatures](#cfn-location-job-validateaddressactionoptions-additionalfeatures)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-location-job-validateaddressactionoptions-syntax.yaml"></a>

```
  [AdditionalFeatures](#cfn-location-job-validateaddressactionoptions-additionalfeatures): {{
    - String}}
```

## Properties
<a name="aws-properties-location-job-validateaddressactionoptions-properties"></a>

`AdditionalFeatures`  <a name="cfn-location-job-validateaddressactionoptions-additionalfeatures"></a>
A list of optional additional parameters that can be requested for each result.
Values:
+ `Position` - Return the position coordinates of the address if available.
+ `CountrySpecificAttributes` - Return additional information about the address specific to the country of origin.
*Required*: No
*Type*: Array of String
*Allowed values*: `Position | CountrySpecificAttributes`
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
