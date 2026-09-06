---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-partnerapp-partnerappmaintenanceconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::PartnerApp PartnerAppMaintenanceConfig
<a name="aws-properties-sagemaker-partnerapp-partnerappmaintenanceconfig"></a>

A collection of settings that specify the maintenance schedule for the PartnerApp.

## Syntax
<a name="aws-properties-sagemaker-partnerapp-partnerappmaintenanceconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-partnerapp-partnerappmaintenanceconfig-syntax.json"></a>

```
{
  "[MaintenanceWindowStart](#cfn-sagemaker-partnerapp-partnerappmaintenanceconfig-maintenancewindowstart)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-partnerapp-partnerappmaintenanceconfig-syntax.yaml"></a>

```
  [MaintenanceWindowStart](#cfn-sagemaker-partnerapp-partnerappmaintenanceconfig-maintenancewindowstart): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-partnerapp-partnerappmaintenanceconfig-properties"></a>

`MaintenanceWindowStart`  <a name="cfn-sagemaker-partnerapp-partnerappmaintenanceconfig-maintenancewindowstart"></a>
The maintenance window start day and time for the PartnerApp.
*Required*: Yes
*Type*: String
*Pattern*: `(Mon|Tue|Wed|Thu|Fri|Sat|Sun):([01]\d|2[0-3]):([0-5]\d)`
*Maximum*: `9`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
