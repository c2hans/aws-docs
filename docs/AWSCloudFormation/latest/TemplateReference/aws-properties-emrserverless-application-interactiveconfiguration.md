---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrserverless-application-interactiveconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRServerless::Application InteractiveConfiguration
<a name="aws-properties-emrserverless-application-interactiveconfiguration"></a>

The configuration to use to enable the different types of interactive use cases in an application.

## Syntax
<a name="aws-properties-emrserverless-application-interactiveconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrserverless-application-interactiveconfiguration-syntax.json"></a>

```
{
  "[LivyEndpointEnabled](#cfn-emrserverless-application-interactiveconfiguration-livyendpointenabled)" : {{Boolean}},
  "[SessionEnabled](#cfn-emrserverless-application-interactiveconfiguration-sessionenabled)" : {{Boolean}},
  "[StudioEnabled](#cfn-emrserverless-application-interactiveconfiguration-studioenabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-emrserverless-application-interactiveconfiguration-syntax.yaml"></a>

```
  [LivyEndpointEnabled](#cfn-emrserverless-application-interactiveconfiguration-livyendpointenabled): {{Boolean}}
  [SessionEnabled](#cfn-emrserverless-application-interactiveconfiguration-sessionenabled): {{Boolean}}
  [StudioEnabled](#cfn-emrserverless-application-interactiveconfiguration-studioenabled): {{Boolean}}
```

## Properties
<a name="aws-properties-emrserverless-application-interactiveconfiguration-properties"></a>

`LivyEndpointEnabled`  <a name="cfn-emrserverless-application-interactiveconfiguration-livyendpointenabled"></a>
Enables an Apache Livy endpoint that you can connect to and run interactive jobs.
*Required*: No
*Type*: Boolean
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`SessionEnabled`  <a name="cfn-emrserverless-application-interactiveconfiguration-sessionenabled"></a>
Enables interactive sessions on the application. When set to `true`, you can start interactive sessions using the `StartSession` operation.
*Required*: No
*Type*: Boolean
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`StudioEnabled`  <a name="cfn-emrserverless-application-interactiveconfiguration-studioenabled"></a>
Enables you to connect an application to Amazon EMR Studio to run interactive workloads in a notebook.
*Required*: No
*Type*: Boolean
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
