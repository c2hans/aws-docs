---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchservice-domain-offpeakwindow.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchService::Domain OffPeakWindow
<a name="aws-properties-opensearchservice-domain-offpeakwindow"></a>

A custom 10-hour, low-traffic window during which OpenSearch Service can perform mandatory configuration changes on the domain. These actions can include scheduled service software updates and blue/green Auto-Tune enhancements. OpenSearch Service will schedule these actions during the window that you specify. If you don't specify a window start time, it defaults to 10:00 P.M. local time.

## Syntax
<a name="aws-properties-opensearchservice-domain-offpeakwindow-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchservice-domain-offpeakwindow-syntax.json"></a>

```
{
  "[WindowStartTime](#cfn-opensearchservice-domain-offpeakwindow-windowstarttime)" : {{WindowStartTime}}
}
```

### YAML
<a name="aws-properties-opensearchservice-domain-offpeakwindow-syntax.yaml"></a>

```
  [WindowStartTime](#cfn-opensearchservice-domain-offpeakwindow-windowstarttime): {{
    WindowStartTime}}
```

## Properties
<a name="aws-properties-opensearchservice-domain-offpeakwindow-properties"></a>

`WindowStartTime`  <a name="cfn-opensearchservice-domain-offpeakwindow-windowstarttime"></a>
The desired start time for an off-peak maintenance window.
*Required*: No
*Type*: [WindowStartTime](aws-properties-opensearchservice-domain-windowstarttime.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
