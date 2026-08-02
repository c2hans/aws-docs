---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-application.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Cluster Application
<a name="aws-properties-emr-cluster-application"></a>

`Application` is a property of `AWS::EMR::Cluster`. The `Application` property type defines the open-source big data applications for EMR to install and configure when a cluster is created.

With Amazon EMR release version 4.0 and later, the only accepted parameter is the application `Name`. To pass arguments to these applications, you use configuration classifications specified using JSON objects in a `Configuration` property. For more information, see [Configuring Applications](https://docs.aws.amazon.com//emr/latest/ReleaseGuide/emr-configure-apps.html).

With earlier Amazon EMR releases, the application is any AWS or third-party software that you can add to the cluster. You can specify the version of the application and arguments to pass to it. Amazon EMR accepts and forwards the argument list to the corresponding installation script as a bootstrap action argument.

## Syntax
<a name="aws-properties-emr-cluster-application-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-cluster-application-syntax.json"></a>

```
{
  "[AdditionalInfo](#cfn-emr-cluster-application-additionalinfo)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Args](#cfn-emr-cluster-application-args)" : {{[ String, ... ]}},
  "[Name](#cfn-emr-cluster-application-name)" : {{String}},
  "[Version](#cfn-emr-cluster-application-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-emr-cluster-application-syntax.yaml"></a>

```
  [AdditionalInfo](#cfn-emr-cluster-application-additionalinfo): {{
    {{Key}}: {{Value}}}}
  [Args](#cfn-emr-cluster-application-args): {{
    - String}}
  [Name](#cfn-emr-cluster-application-name): {{String}}
  [Version](#cfn-emr-cluster-application-version): {{String}}
```

## Properties
<a name="aws-properties-emr-cluster-application-properties"></a>

`AdditionalInfo`  <a name="cfn-emr-cluster-application-additionalinfo"></a>
This option is for advanced users only. This is meta information about clusters and applications that are used for testing and troubleshooting.
*Required*: No
*Type*: Object of String
*Pattern*: `[a-zA-Z0-9]+`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Args`  <a name="cfn-emr-cluster-application-args"></a>
Arguments for Amazon EMR to pass to the application.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-emr-cluster-application-name"></a>
The name of the application.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Version`  <a name="cfn-emr-cluster-application-version"></a>
The version of the application.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
