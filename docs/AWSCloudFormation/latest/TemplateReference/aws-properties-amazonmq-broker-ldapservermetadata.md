---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amazonmq-broker-ldapservermetadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmazonMQ::Broker LdapServerMetadata
<a name="aws-properties-amazonmq-broker-ldapservermetadata"></a>

Optional. The metadata of the LDAP server used to authenticate and authorize connections to the broker. Does not apply to RabbitMQ brokers.

## Syntax
<a name="aws-properties-amazonmq-broker-ldapservermetadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amazonmq-broker-ldapservermetadata-syntax.json"></a>

```
{
  "[Hosts](#cfn-amazonmq-broker-ldapservermetadata-hosts)" : {{[ String, ... ]}},
  "[RoleBase](#cfn-amazonmq-broker-ldapservermetadata-rolebase)" : {{String}},
  "[RoleName](#cfn-amazonmq-broker-ldapservermetadata-rolename)" : {{String}},
  "[RoleSearchMatching](#cfn-amazonmq-broker-ldapservermetadata-rolesearchmatching)" : {{String}},
  "[RoleSearchSubtree](#cfn-amazonmq-broker-ldapservermetadata-rolesearchsubtree)" : {{Boolean}},
  "[ServiceAccountPassword](#cfn-amazonmq-broker-ldapservermetadata-serviceaccountpassword)" : {{String}},
  "[ServiceAccountUsername](#cfn-amazonmq-broker-ldapservermetadata-serviceaccountusername)" : {{String}},
  "[UserBase](#cfn-amazonmq-broker-ldapservermetadata-userbase)" : {{String}},
  "[UserRoleName](#cfn-amazonmq-broker-ldapservermetadata-userrolename)" : {{String}},
  "[UserSearchMatching](#cfn-amazonmq-broker-ldapservermetadata-usersearchmatching)" : {{String}},
  "[UserSearchSubtree](#cfn-amazonmq-broker-ldapservermetadata-usersearchsubtree)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-amazonmq-broker-ldapservermetadata-syntax.yaml"></a>

```
  [Hosts](#cfn-amazonmq-broker-ldapservermetadata-hosts): {{
    - String}}
  [RoleBase](#cfn-amazonmq-broker-ldapservermetadata-rolebase): {{String}}
  [RoleName](#cfn-amazonmq-broker-ldapservermetadata-rolename): {{String}}
  [RoleSearchMatching](#cfn-amazonmq-broker-ldapservermetadata-rolesearchmatching): {{String}}
  [RoleSearchSubtree](#cfn-amazonmq-broker-ldapservermetadata-rolesearchsubtree): {{Boolean}}
  [ServiceAccountPassword](#cfn-amazonmq-broker-ldapservermetadata-serviceaccountpassword): {{String}}
  [ServiceAccountUsername](#cfn-amazonmq-broker-ldapservermetadata-serviceaccountusername): {{String}}
  [UserBase](#cfn-amazonmq-broker-ldapservermetadata-userbase): {{String}}
  [UserRoleName](#cfn-amazonmq-broker-ldapservermetadata-userrolename): {{String}}
  [UserSearchMatching](#cfn-amazonmq-broker-ldapservermetadata-usersearchmatching): {{String}}
  [UserSearchSubtree](#cfn-amazonmq-broker-ldapservermetadata-usersearchsubtree): {{Boolean}}
```

## Properties
<a name="aws-properties-amazonmq-broker-ldapservermetadata-properties"></a>

`Hosts`  <a name="cfn-amazonmq-broker-ldapservermetadata-hosts"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleBase`  <a name="cfn-amazonmq-broker-ldapservermetadata-rolebase"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleName`  <a name="cfn-amazonmq-broker-ldapservermetadata-rolename"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleSearchMatching`  <a name="cfn-amazonmq-broker-ldapservermetadata-rolesearchmatching"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleSearchSubtree`  <a name="cfn-amazonmq-broker-ldapservermetadata-rolesearchsubtree"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceAccountPassword`  <a name="cfn-amazonmq-broker-ldapservermetadata-serviceaccountpassword"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceAccountUsername`  <a name="cfn-amazonmq-broker-ldapservermetadata-serviceaccountusername"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserBase`  <a name="cfn-amazonmq-broker-ldapservermetadata-userbase"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserRoleName`  <a name="cfn-amazonmq-broker-ldapservermetadata-userrolename"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserSearchMatching`  <a name="cfn-amazonmq-broker-ldapservermetadata-usersearchmatching"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserSearchSubtree`  <a name="cfn-amazonmq-broker-ldapservermetadata-usersearchsubtree"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
