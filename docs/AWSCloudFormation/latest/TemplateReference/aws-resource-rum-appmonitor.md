---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rum-appmonitor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RUM::AppMonitor
<a name="aws-resource-rum-appmonitor"></a>

Creates a CloudWatch RUM app monitor, which you can use to collect telemetry data from your application and send it to CloudWatch RUM. The data includes performance and reliability information such as page load time, client-side errors, and user behavior.

After you create an app monitor, sign in to the CloudWatch RUM console to get the JavaScript code snippet to add to your web application. For more information, see [How do I find a code snippet that I've already generated?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-find-code-snippet.html)

## Syntax
<a name="aws-resource-rum-appmonitor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-rum-appmonitor-syntax.json"></a>

```
{
  "Type" : "AWS::RUM::AppMonitor",
  "Properties" : {
      "[AppMonitorConfiguration](#cfn-rum-appmonitor-appmonitorconfiguration)" : {{AppMonitorConfiguration}},
      "[CustomEvents](#cfn-rum-appmonitor-customevents)" : {{CustomEvents}},
      "[CwLogEnabled](#cfn-rum-appmonitor-cwlogenabled)" : {{Boolean}},
      "[DeobfuscationConfiguration](#cfn-rum-appmonitor-deobfuscationconfiguration)" : {{DeobfuscationConfiguration}},
      "[Domain](#cfn-rum-appmonitor-domain)" : {{String}},
      "[DomainList](#cfn-rum-appmonitor-domainlist)" : {{[ String, ... ]}},
      "[Name](#cfn-rum-appmonitor-name)" : {{String}},
      "[Platform](#cfn-rum-appmonitor-platform)" : {{String}},
      "[ResourcePolicy](#cfn-rum-appmonitor-resourcepolicy)" : {{ResourcePolicy}},
      "[Tags](#cfn-rum-appmonitor-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-rum-appmonitor-syntax.yaml"></a>

```
Type: AWS::RUM::AppMonitor
Properties:
  [AppMonitorConfiguration](#cfn-rum-appmonitor-appmonitorconfiguration): {{
    AppMonitorConfiguration}}
  [CustomEvents](#cfn-rum-appmonitor-customevents): {{
    CustomEvents}}
  [CwLogEnabled](#cfn-rum-appmonitor-cwlogenabled): {{Boolean}}
  [DeobfuscationConfiguration](#cfn-rum-appmonitor-deobfuscationconfiguration): {{
    DeobfuscationConfiguration}}
  [Domain](#cfn-rum-appmonitor-domain): {{String}}
  [DomainList](#cfn-rum-appmonitor-domainlist): {{
    - String}}
  [Name](#cfn-rum-appmonitor-name): {{String}}
  [Platform](#cfn-rum-appmonitor-platform): {{String}}
  [ResourcePolicy](#cfn-rum-appmonitor-resourcepolicy): {{
    ResourcePolicy}}
  [Tags](#cfn-rum-appmonitor-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-rum-appmonitor-properties"></a>

`AppMonitorConfiguration`  <a name="cfn-rum-appmonitor-appmonitorconfiguration"></a>
A structure that contains much of the configuration data for the app monitor. If you are using Amazon Cognito for authorization, you must include this structure in your request, and it must include the ID of the Amazon Cognito identity pool to use for authorization. If you don't include `AppMonitorConfiguration`, you must set up your own authorization method. For more information, see [Authorize your application to send data to AWS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-get-started-authorization.html).
If you omit this argument, the sample rate used for CloudWatch RUM is set to 10% of the user sessions.
*Required*: No
*Type*: [AppMonitorConfiguration](aws-properties-rum-appmonitor-appmonitorconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomEvents`  <a name="cfn-rum-appmonitor-customevents"></a>
Specifies whether this app monitor allows the web client to define and send custom events. If you omit this parameter, custom events are `DISABLED`.
*Required*: No
*Type*: [CustomEvents](aws-properties-rum-appmonitor-customevents.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CwLogEnabled`  <a name="cfn-rum-appmonitor-cwlogenabled"></a>
Data collected by CloudWatch RUM is kept by RUM for 30 days and then deleted. This parameter specifies whether CloudWatch RUM sends a copy of this telemetry data to Amazon CloudWatch Logs in your account. This enables you to keep the telemetry data for more than 30 days, but it does incur Amazon CloudWatch Logs charges.
If you omit this parameter, the default is `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeobfuscationConfiguration`  <a name="cfn-rum-appmonitor-deobfuscationconfiguration"></a>
 A structure that contains the configuration for how an app monitor can deobfuscate stack traces.
*Required*: No
*Type*: [DeobfuscationConfiguration](aws-properties-rum-appmonitor-deobfuscationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Domain`  <a name="cfn-rum-appmonitor-domain"></a>
The top-level internet domain name for which your application has administrative authority. This parameter or the `DomainList` parameter is required.
*Required*: No
*Type*: String
*Pattern*: `^(localhost)$|^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$|(?=^[a-zA-Z0-9\.\*-]{4,253}$)(?!.*\.-)(?!.*-\.)(?!.*\.\.)(?!.*[^\.]{64,})^(\*\.)?(?![-\.\*])[^\*]{1,}\.(\*|(?!.*--)(?=.*[a-zA-Z])[^\*]{1,}[^\*-])$`
*Minimum*: `1`
*Maximum*: `253`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainList`  <a name="cfn-rum-appmonitor-domainlist"></a>
 List the domain names for which your application has administrative authority. This parameter or the `Domain` parameter is required.
You can have a minimum of 1 and a maximum of 5 `Domain` under `DomainList`. Each `Domain` must be a minimum length of 1 and a maximum of 253 characters.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `253 | 5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-rum-appmonitor-name"></a>
A name for the app monitor. This parameter is required.
*Required*: Yes
*Type*: String
*Pattern*: `[\.\-_/#A-Za-z0-9]+`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Platform`  <a name="cfn-rum-appmonitor-platform"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `Web | Android | iOS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourcePolicy`  <a name="cfn-rum-appmonitor-resourcepolicy"></a>
Use this structure to assign a resource-based policy to a CloudWatch RUM app monitor to control access to it. Each app monitor can have one resource-based policy. The maximum size of the policy is 4 KB. To learn more about using resource policies with RUM, see [Using resource-based policies with CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-resource-policies.html).
*Required*: No
*Type*: [ResourcePolicy](aws-properties-rum-appmonitor-resourcepolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-rum-appmonitor-tags"></a>
Assigns one or more tags (key-value pairs) to the app monitor.
Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.
Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters.
You can associate as many as 50 tags with an app monitor.
For more information, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-rum-appmonitor-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-rum-appmonitor-return-values"></a>

### Ref
<a name="aws-resource-rum-appmonitor-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the app monitor.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-rum-appmonitor-return-values-fn--getatt"></a>

####
<a name="aws-resource-rum-appmonitor-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
The ID of the app monitor, such as `123456ab-1234-4ca9-9d2f-a1b2c3456789`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
