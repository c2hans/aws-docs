---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-securityprofile-application.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::SecurityProfile Application
<a name="aws-properties-connect-securityprofile-application"></a>

This API is in preview release for Connect Customer and is subject to change.

A third-party application's metadata.

## Syntax
<a name="aws-properties-connect-securityprofile-application-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-securityprofile-application-syntax.json"></a>

```
{
  "[ApplicationPermissions](#cfn-connect-securityprofile-application-applicationpermissions)" : {{[ String, ... ]}},
  "[Namespace](#cfn-connect-securityprofile-application-namespace)" : {{String}},
  "[Type](#cfn-connect-securityprofile-application-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-securityprofile-application-syntax.yaml"></a>

```
  [ApplicationPermissions](#cfn-connect-securityprofile-application-applicationpermissions): {{
    - String}}
  [Namespace](#cfn-connect-securityprofile-application-namespace): {{String}}
  [Type](#cfn-connect-securityprofile-application-type): {{String}}
```

## Properties
<a name="aws-properties-connect-securityprofile-application-properties"></a>

`ApplicationPermissions`  <a name="cfn-connect-securityprofile-application-applicationpermissions"></a>
The permissions that the agent is granted on the application. For third-party applications, only the `ACCESS` permission is supported. For MCP Servers, the permissions are tool Identifiers accepted by MCP Server.
*Required*: No
*Type*: Array of String
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Namespace`  <a name="cfn-connect-securityprofile-application-namespace"></a>
Namespace of the application that you want to give access to.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-connect-securityprofile-application-type"></a>
 Type of Application.
*Required*: No
*Type*: String
*Allowed values*: `MCP | THIRD_PARTY_APPLICATION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
