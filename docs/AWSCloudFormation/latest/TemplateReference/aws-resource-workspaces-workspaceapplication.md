---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-workspaces-workspaceapplication.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpaces::WorkSpaceApplication
<a name="aws-resource-workspaces-workspaceapplication"></a>

Describes the WorkSpace application.

## Syntax
<a name="aws-resource-workspaces-workspaceapplication-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-workspaces-workspaceapplication-syntax.json"></a>

```
{
  "Type" : "AWS::WorkSpaces::WorkSpaceApplication"
}
```

### YAML
<a name="aws-resource-workspaces-workspaceapplication-syntax.yaml"></a>

```
Type: AWS::WorkSpaces::WorkSpaceApplication
```

## Return values
<a name="aws-resource-workspaces-workspaceapplication-return-values"></a>

### Ref
<a name="aws-resource-workspaces-workspaceapplication-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-workspaces-workspaceapplication-return-values-fn--getatt"></a>

####
<a name="aws-resource-workspaces-workspaceapplication-return-values-fn--getatt-fn--getatt"></a>

`ApplicationId`  <a name="ApplicationId-fn::getatt"></a>
The identifier of the application.

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`Created`  <a name="Created-fn::getatt"></a>
The time the application is created.

`Description`  <a name="Description-fn::getatt"></a>
The description of the WorkSpace application.

`LicenseType`  <a name="LicenseType-fn::getatt"></a>
The license availability for the applications.

`Name`  <a name="Name-fn::getatt"></a>
The name of the WorkSpace application.

`Owner`  <a name="Owner-fn::getatt"></a>
The owner of the WorkSpace application.

`State`  <a name="State-fn::getatt"></a>
The status of WorkSpace application.

`SupportedComputeTypeNames`  <a name="SupportedComputeTypeNames-fn::getatt"></a>
The supported compute types of the WorkSpace application.

`SupportedOperatingSystemNames`  <a name="SupportedOperatingSystemNames-fn::getatt"></a>
The supported operating systems of the WorkSpace application.
