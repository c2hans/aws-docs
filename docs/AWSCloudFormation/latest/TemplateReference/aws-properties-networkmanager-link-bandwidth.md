---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkmanager-link-bandwidth.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::Link Bandwidth
<a name="aws-properties-networkmanager-link-bandwidth"></a>

Describes bandwidth information.

## Syntax
<a name="aws-properties-networkmanager-link-bandwidth-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkmanager-link-bandwidth-syntax.json"></a>

```
{
  "[DownloadSpeed](#cfn-networkmanager-link-bandwidth-downloadspeed)" : {{Integer}},
  "[UploadSpeed](#cfn-networkmanager-link-bandwidth-uploadspeed)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-networkmanager-link-bandwidth-syntax.yaml"></a>

```
  [DownloadSpeed](#cfn-networkmanager-link-bandwidth-downloadspeed): {{Integer}}
  [UploadSpeed](#cfn-networkmanager-link-bandwidth-uploadspeed): {{Integer}}
```

## Properties
<a name="aws-properties-networkmanager-link-bandwidth-properties"></a>

`DownloadSpeed`  <a name="cfn-networkmanager-link-bandwidth-downloadspeed"></a>
Download speed in Mbps.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UploadSpeed`  <a name="cfn-networkmanager-link-bandwidth-uploadspeed"></a>
Upload speed in Mbps.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
