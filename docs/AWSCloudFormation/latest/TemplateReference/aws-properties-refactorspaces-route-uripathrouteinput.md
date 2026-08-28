---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-refactorspaces-route-uripathrouteinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RefactorSpaces::Route UriPathRouteInput
<a name="aws-properties-refactorspaces-route-uripathrouteinput"></a>

The configuration for the URI path route type.

## Syntax
<a name="aws-properties-refactorspaces-route-uripathrouteinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-refactorspaces-route-uripathrouteinput-syntax.json"></a>

```
{
  "[ActivationState](#cfn-refactorspaces-route-uripathrouteinput-activationstate)" : {{String}},
  "[AppendSourcePath](#cfn-refactorspaces-route-uripathrouteinput-appendsourcepath)" : {{Boolean}},
  "[IncludeChildPaths](#cfn-refactorspaces-route-uripathrouteinput-includechildpaths)" : {{Boolean}},
  "[Methods](#cfn-refactorspaces-route-uripathrouteinput-methods)" : {{[ String, ... ]}},
  "[SourcePath](#cfn-refactorspaces-route-uripathrouteinput-sourcepath)" : {{String}}
}
```

### YAML
<a name="aws-properties-refactorspaces-route-uripathrouteinput-syntax.yaml"></a>

```
  [ActivationState](#cfn-refactorspaces-route-uripathrouteinput-activationstate): {{String}}
  [AppendSourcePath](#cfn-refactorspaces-route-uripathrouteinput-appendsourcepath): {{Boolean}}
  [IncludeChildPaths](#cfn-refactorspaces-route-uripathrouteinput-includechildpaths): {{Boolean}}
  [Methods](#cfn-refactorspaces-route-uripathrouteinput-methods): {{
    - String}}
  [SourcePath](#cfn-refactorspaces-route-uripathrouteinput-sourcepath): {{String}}
```

## Properties
<a name="aws-properties-refactorspaces-route-uripathrouteinput-properties"></a>

`ActivationState`  <a name="cfn-refactorspaces-route-uripathrouteinput-activationstate"></a>
If set to `ACTIVE`, traffic is forwarded to this route’s service after the route is created.
*Required*: Yes
*Type*: String
*Allowed values*: `INACTIVE | ACTIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AppendSourcePath`  <a name="cfn-refactorspaces-route-uripathrouteinput-appendsourcepath"></a>
If set to `true`, this option appends the source path to the service URL endpoint.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IncludeChildPaths`  <a name="cfn-refactorspaces-route-uripathrouteinput-includechildpaths"></a>
Indicates whether to match all subpaths of the given source path. If this value is `false`, requests must match the source path exactly before they are forwarded to this route's service.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Methods`  <a name="cfn-refactorspaces-route-uripathrouteinput-methods"></a>
A list of HTTP methods to match. An empty list matches all values. If a method is present, only HTTP requests using that method are forwarded to this route’s service.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourcePath`  <a name="cfn-refactorspaces-route-uripathrouteinput-sourcepath"></a>
This is the path that Refactor Spaces uses to match traffic. Paths must start with `/` and are relative to the base of the application. To use path parameters in the source path, add a variable in curly braces. For example, the resource path {user} represents a path parameter called 'user'.
*Required*: No
*Type*: String
*Pattern*: `^(/([a-zA-Z0-9._:-]+|\{[a-zA-Z0-9._:-]+\}))+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
