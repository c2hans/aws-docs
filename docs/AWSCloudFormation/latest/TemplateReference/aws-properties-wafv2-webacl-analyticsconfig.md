---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-analyticsconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL AnalyticsConfig

Specifies the security analytics configuration for the web ACL. Security analytics shows the web ACL's request log data from multiple AWS Regions in a single dashboard in the AWS WAF console.

When you enable security analytics, you authorize AWS to transfer and store full request logs outside the AWS Region where the web ACL is hosted. For regional web ACLs, security analytics is disabled by default when you omit this configuration. For web ACLs that protect CloudFront distributions (global web ACLs), security analytics is enabled by default. For more information, see [Enabling security analytics for a protection pack (web ACL)](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-security-analytics-enabling.html) in the *AWS WAF Developer Guide*.

## Syntax
<a name="aws-properties-wafv2-webacl-analyticsconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-analyticsconfig-syntax.json"></a>

```json
{
  "[Mode](#cfn-wafv2-webacl-analyticsconfig-mode)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-analyticsconfig-syntax.yaml"></a>

```yaml
  [Mode](#cfn-wafv2-webacl-analyticsconfig-mode): {{String}}
```

## Properties
<a name="aws-properties-wafv2-webacl-analyticsconfig-properties"></a>

`Mode`  <a name="cfn-wafv2-webacl-analyticsconfig-mode"></a>
The security analytics mode for the web ACL. Valid values:
+ `CROSS_REGION` - Enables security analytics. AWS WAF transfers and stores the web ACL's request logs outside the AWS Region where the web ACL is hosted, for aggregation and processing.
+ `DISABLED` - Disables security analytics. AWS WAF stops transferring the web ACL's request logs.
*Required*: Yes
*Type*: String
*Allowed values*: `CROSS_REGION | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
