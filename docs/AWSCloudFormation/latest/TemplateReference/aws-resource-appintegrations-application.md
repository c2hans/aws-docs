---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appintegrations-application.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppIntegrations::Application
<a name="aws-resource-appintegrations-application"></a>

Creates and persists an Application resource.

## Syntax
<a name="aws-resource-appintegrations-application-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-appintegrations-application-syntax.json"></a>

```
{
  "Type" : "AWS::AppIntegrations::Application",
  "Properties" : {
      "[ApplicationConfig](#cfn-appintegrations-application-applicationconfig)" : {{ApplicationConfig}},
      "[ApplicationSourceConfig](#cfn-appintegrations-application-applicationsourceconfig)" : {{ApplicationSourceConfig}},
      "[ApplicationType](#cfn-appintegrations-application-applicationtype)" : {{String}},
      "[Description](#cfn-appintegrations-application-description)" : {{String}},
      "[IframeConfig](#cfn-appintegrations-application-iframeconfig)" : {{IframeConfig}},
      "[InitializationTimeout](#cfn-appintegrations-application-initializationtimeout)" : {{Integer}},
      "[IsService](#cfn-appintegrations-application-isservice)" : {{Boolean}},
      "[Name](#cfn-appintegrations-application-name)" : {{String}},
      "[Namespace](#cfn-appintegrations-application-namespace)" : {{String}},
      "[Permissions](#cfn-appintegrations-application-permissions)" : {{[ String, ... ]}},
      "[Tags](#cfn-appintegrations-application-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-appintegrations-application-syntax.yaml"></a>

```
Type: AWS::AppIntegrations::Application
Properties:
  [ApplicationConfig](#cfn-appintegrations-application-applicationconfig): {{
    ApplicationConfig}}
  [ApplicationSourceConfig](#cfn-appintegrations-application-applicationsourceconfig): {{
    ApplicationSourceConfig}}
  [ApplicationType](#cfn-appintegrations-application-applicationtype): {{String}}
  [Description](#cfn-appintegrations-application-description): {{String}}
  [IframeConfig](#cfn-appintegrations-application-iframeconfig): {{
    IframeConfig}}
  [InitializationTimeout](#cfn-appintegrations-application-initializationtimeout): {{Integer}}
  [IsService](#cfn-appintegrations-application-isservice): {{Boolean}}
  [Name](#cfn-appintegrations-application-name): {{String}}
  [Namespace](#cfn-appintegrations-application-namespace): {{String}}
  [Permissions](#cfn-appintegrations-application-permissions): {{
    - String}}
  [Tags](#cfn-appintegrations-application-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-appintegrations-application-properties"></a>

`ApplicationConfig`  <a name="cfn-appintegrations-application-applicationconfig"></a>
Property description not available.
*Required*: No
*Type*: [ApplicationConfig](aws-properties-appintegrations-application-applicationconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicationSourceConfig`  <a name="cfn-appintegrations-application-applicationsourceconfig"></a>
The configuration for where the application should be loaded from.
*Required*: Yes
*Type*: [ApplicationSourceConfig](aws-properties-appintegrations-application-applicationsourceconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicationType`  <a name="cfn-appintegrations-application-applicationtype"></a>
The type of application.
*Required*: No
*Type*: String
*Allowed values*: `STANDARD | SERVICE | MCP_SERVER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-appintegrations-application-description"></a>
The description of the application.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IframeConfig`  <a name="cfn-appintegrations-application-iframeconfig"></a>
Property description not available.
*Required*: No
*Type*: [IframeConfig](aws-properties-appintegrations-application-iframeconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InitializationTimeout`  <a name="cfn-appintegrations-application-initializationtimeout"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsService`  <a name="cfn-appintegrations-application-isservice"></a>
Indicates whether the application is a service.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-appintegrations-application-name"></a>
The name of the application.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\/\._ \-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Namespace`  <a name="cfn-appintegrations-application-namespace"></a>
The namespace of the application.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9/\._\-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Permissions`  <a name="cfn-appintegrations-application-permissions"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `150`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-appintegrations-application-tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
*Required*: No
*Type*: Array of [Tag](aws-properties-appintegrations-application-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-appintegrations-application-return-values"></a>

### Ref
<a name="aws-resource-appintegrations-application-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-appintegrations-application-return-values-fn--getatt"></a>

####
<a name="aws-resource-appintegrations-application-return-values-fn--getatt-fn--getatt"></a>

`ApplicationArn`  <a name="ApplicationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the Application.

`Id`  <a name="Id-fn::getatt"></a>
A unique identifier for the Application.
