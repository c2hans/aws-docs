---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-securityprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::SecurityProfile
<a name="aws-resource-connect-securityprofile"></a>

Creates a security profile.

For information about security profiles, see [Security Profiles](https://docs.aws.amazon.com/connect/latest/adminguide/connect-security-profiles.html) in the *Connect Customer Administrator Guide*. For a mapping of the API name and user interface name of the security profile permissions, see [List of security profile permissions](https://docs.aws.amazon.com/connect/latest/adminguide/security-profile-list.html).

## Syntax
<a name="aws-resource-connect-securityprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-securityprofile-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::SecurityProfile",
  "Properties" : {
      "[AllowedAccessControlHierarchyGroupId](#cfn-connect-securityprofile-allowedaccesscontrolhierarchygroupid)" : {{String}},
      "[AllowedAccessControlTags](#cfn-connect-securityprofile-allowedaccesscontroltags)" : {{[ Tag, ... ]}},
      "[AllowedFlowModules](#cfn-connect-securityprofile-allowedflowmodules)" : {{[ FlowModule, ... ]}},
      "[Applications](#cfn-connect-securityprofile-applications)" : {{[ Application, ... ]}},
      "[Description](#cfn-connect-securityprofile-description)" : {{String}},
      "[GranularAccessControlConfiguration](#cfn-connect-securityprofile-granularaccesscontrolconfiguration)" : {{GranularAccessControlConfiguration}},
      "[HierarchyRestrictedResources](#cfn-connect-securityprofile-hierarchyrestrictedresources)" : {{[ String, ... ]}},
      "[InstanceArn](#cfn-connect-securityprofile-instancearn)" : {{String}},
      "[Permissions](#cfn-connect-securityprofile-permissions)" : {{[ String, ... ]}},
      "[SecurityProfileName](#cfn-connect-securityprofile-securityprofilename)" : {{String}},
      "[TagRestrictedResources](#cfn-connect-securityprofile-tagrestrictedresources)" : {{[ String, ... ]}},
      "[Tags](#cfn-connect-securityprofile-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-connect-securityprofile-syntax.yaml"></a>

```
Type: AWS::Connect::SecurityProfile
Properties:
  [AllowedAccessControlHierarchyGroupId](#cfn-connect-securityprofile-allowedaccesscontrolhierarchygroupid): {{String}}
  [AllowedAccessControlTags](#cfn-connect-securityprofile-allowedaccesscontroltags): {{
    - Tag}}
  [AllowedFlowModules](#cfn-connect-securityprofile-allowedflowmodules): {{
    - FlowModule}}
  [Applications](#cfn-connect-securityprofile-applications): {{
    - Application}}
  [Description](#cfn-connect-securityprofile-description): {{String}}
  [GranularAccessControlConfiguration](#cfn-connect-securityprofile-granularaccesscontrolconfiguration): {{
    GranularAccessControlConfiguration}}
  [HierarchyRestrictedResources](#cfn-connect-securityprofile-hierarchyrestrictedresources): {{
    - String}}
  [InstanceArn](#cfn-connect-securityprofile-instancearn): {{String}}
  [Permissions](#cfn-connect-securityprofile-permissions): {{
    - String}}
  [SecurityProfileName](#cfn-connect-securityprofile-securityprofilename): {{String}}
  [TagRestrictedResources](#cfn-connect-securityprofile-tagrestrictedresources): {{
    - String}}
  [Tags](#cfn-connect-securityprofile-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-connect-securityprofile-properties"></a>

`AllowedAccessControlHierarchyGroupId`  <a name="cfn-connect-securityprofile-allowedaccesscontrolhierarchygroupid"></a>
The identifier of the hierarchy group that a security profile uses to restrict access to resources in Connect Customer.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]+$`
*Minimum*: `0`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedAccessControlTags`  <a name="cfn-connect-securityprofile-allowedaccesscontroltags"></a>
The list of tags that a security profile uses to restrict access to resources in Connect Customer.
*Required*: No
*Type*: Array of [Tag](aws-properties-connect-securityprofile-tag.md)
*Maximum*: `4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedFlowModules`  <a name="cfn-connect-securityprofile-allowedflowmodules"></a>
Property description not available.
*Required*: No
*Type*: Array of [FlowModule](aws-properties-connect-securityprofile-flowmodule.md)
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Applications`  <a name="cfn-connect-securityprofile-applications"></a>
Property description not available.
*Required*: No
*Type*: Array of [Application](aws-properties-connect-securityprofile-application.md)
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-connect-securityprofile-description"></a>
The description of the security profile.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `250`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GranularAccessControlConfiguration`  <a name="cfn-connect-securityprofile-granularaccesscontrolconfiguration"></a>
The granular access control configuration for the security profile, including data table permissions.
*Required*: No
*Type*: [GranularAccessControlConfiguration](aws-properties-connect-securityprofile-granularaccesscontrolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HierarchyRestrictedResources`  <a name="cfn-connect-securityprofile-hierarchyrestrictedresources"></a>
The list of resources that a security profile applies hierarchy restrictions to in Connect Customer. Following are acceptable ResourceNames: `User`.
*Required*: No
*Type*: Array of String
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceArn`  <a name="cfn-connect-securityprofile-instancearn"></a>
The identifier of the Connect Customer instance.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Permissions`  <a name="cfn-connect-securityprofile-permissions"></a>
Permissions assigned to the security profile. For a list of valid permissions, see [List of security profile permissions](https://docs.aws.amazon.com/connect/latest/adminguide/security-profile-list.html).
*Required*: No
*Type*: Array of String
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityProfileName`  <a name="cfn-connect-securityprofile-securityprofilename"></a>
The name for the security profile.
*Required*: Yes
*Type*: String
*Pattern*: `^[ a-zA-Z0-9_@-]+$`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TagRestrictedResources`  <a name="cfn-connect-securityprofile-tagrestrictedresources"></a>
The list of resources that a security profile applies tag restrictions to in Connect Customer.
*Required*: No
*Type*: Array of String
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-connect-securityprofile-tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
*Required*: No
*Type*: Array of [Tag](aws-properties-connect-securityprofile-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-connect-securityprofile-return-values"></a>

### Ref
<a name="aws-resource-connect-securityprofile-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the security profile. For example:

 `{ "Ref": "mySecurityProfileName" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-connect-securityprofile-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-connect-securityprofile-return-values-fn--getatt-fn--getatt"></a>

`LastModifiedRegion`  <a name="LastModifiedRegion-fn::getatt"></a>
The AWS Region where this resource was last modified.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The timestamp when this resource was last modified.

`SecurityProfileArn`  <a name="SecurityProfileArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the security profile.
