---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchservice-domain-identitycenteroptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchService::Domain IdentityCenterOptions
<a name="aws-properties-opensearchservice-domain-identitycenteroptions"></a>

Settings container for integrating IAM Identity Center with OpenSearch UI applications, which enables enabling secure user authentication and access control across multiple data sources. This setup supports single sign-on (SSO) through IAM Identity Center, allowing centralized user management.

## Syntax
<a name="aws-properties-opensearchservice-domain-identitycenteroptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchservice-domain-identitycenteroptions-syntax.json"></a>

```
{
  "[EnabledAPIAccess](#cfn-opensearchservice-domain-identitycenteroptions-enabledapiaccess)" : {{Boolean}},
  "[IdentityCenterApplicationARN](#cfn-opensearchservice-domain-identitycenteroptions-identitycenterapplicationarn)" : {{String}},
  "[IdentityCenterInstanceARN](#cfn-opensearchservice-domain-identitycenteroptions-identitycenterinstancearn)" : {{String}},
  "[IdentityStoreId](#cfn-opensearchservice-domain-identitycenteroptions-identitystoreid)" : {{String}},
  "[RolesKey](#cfn-opensearchservice-domain-identitycenteroptions-roleskey)" : {{String}},
  "[SubjectKey](#cfn-opensearchservice-domain-identitycenteroptions-subjectkey)" : {{String}}
}
```

### YAML
<a name="aws-properties-opensearchservice-domain-identitycenteroptions-syntax.yaml"></a>

```
  [EnabledAPIAccess](#cfn-opensearchservice-domain-identitycenteroptions-enabledapiaccess): {{Boolean}}
  [IdentityCenterApplicationARN](#cfn-opensearchservice-domain-identitycenteroptions-identitycenterapplicationarn): {{String}}
  [IdentityCenterInstanceARN](#cfn-opensearchservice-domain-identitycenteroptions-identitycenterinstancearn): {{String}}
  [IdentityStoreId](#cfn-opensearchservice-domain-identitycenteroptions-identitystoreid): {{String}}
  [RolesKey](#cfn-opensearchservice-domain-identitycenteroptions-roleskey): {{String}}
  [SubjectKey](#cfn-opensearchservice-domain-identitycenteroptions-subjectkey): {{String}}
```

## Properties
<a name="aws-properties-opensearchservice-domain-identitycenteroptions-properties"></a>

`EnabledAPIAccess`  <a name="cfn-opensearchservice-domain-identitycenteroptions-enabledapiaccess"></a>
Indicates whether IAM Identity Center is enabled for the application.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdentityCenterApplicationARN`  <a name="cfn-opensearchservice-domain-identitycenteroptions-identitycenterapplicationarn"></a>
The ARN of the IAM Identity Center application that integrates with Amazon OpenSearch Service.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-z\\-]*:[a-z]+:[a-z0-9\\-]*:[0-9]*:[a-z0-9\\-]+\/[a-z0-9\\-]+\/[a-z0-9\\-]+`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdentityCenterInstanceARN`  <a name="cfn-opensearchservice-domain-identitycenteroptions-identitycenterinstancearn"></a>
The Amazon Resource Name (ARN) of the IAM Identity Center instance.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-z\\-]*:[a-z]+:[a-z0-9\\-]*:[0-9]*:[a-z0-9\\-]+\/[a-z0-9\\-]+`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdentityStoreId`  <a name="cfn-opensearchservice-domain-identitycenteroptions-identitystoreid"></a>
The identifier of the IAM Identity Store.
*Required*: No
*Type*: String
*Pattern*: `^d-[0-9a-f]{10}$|^[0-9a-f]{8}\\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\\b[0-9a-f]{12}$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RolesKey`  <a name="cfn-opensearchservice-domain-identitycenteroptions-roleskey"></a>
Specifies the attribute that contains the backend role identifier (such as group name or group ID) in IAM Identity Center.
*Required*: No
*Type*: String
*Allowed values*: `GroupName | GroupId`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubjectKey`  <a name="cfn-opensearchservice-domain-identitycenteroptions-subjectkey"></a>
Specifies the attribute that contains the subject identifier (such as username, user ID, or email) in IAM Identity Center.
*Required*: No
*Type*: String
*Allowed values*: `UserName | UserId | Email`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
