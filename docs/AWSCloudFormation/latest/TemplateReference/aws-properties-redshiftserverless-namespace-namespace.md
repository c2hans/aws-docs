---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshiftserverless-namespace-namespace.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RedshiftServerless::Namespace Namespace
<a name="aws-properties-redshiftserverless-namespace-namespace"></a>

A collection of database objects and users.

## Syntax
<a name="aws-properties-redshiftserverless-namespace-namespace-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshiftserverless-namespace-namespace-syntax.json"></a>

```
{
  "[AdminPasswordSecretArn](#cfn-redshiftserverless-namespace-namespace-adminpasswordsecretarn)" : {{String}},
  "[AdminPasswordSecretKmsKeyId](#cfn-redshiftserverless-namespace-namespace-adminpasswordsecretkmskeyid)" : {{String}},
  "[AdminUsername](#cfn-redshiftserverless-namespace-namespace-adminusername)" : {{String}},
  "[CreationDate](#cfn-redshiftserverless-namespace-namespace-creationdate)" : {{String}},
  "[DbName](#cfn-redshiftserverless-namespace-namespace-dbname)" : {{String}},
  "[DefaultIamRoleArn](#cfn-redshiftserverless-namespace-namespace-defaultiamrolearn)" : {{String}},
  "[IamRoles](#cfn-redshiftserverless-namespace-namespace-iamroles)" : {{[ String, ... ]}},
  "[KmsKeyId](#cfn-redshiftserverless-namespace-namespace-kmskeyid)" : {{String}},
  "[LogExports](#cfn-redshiftserverless-namespace-namespace-logexports)" : {{[ String, ... ]}},
  "[NamespaceArn](#cfn-redshiftserverless-namespace-namespace-namespacearn)" : {{String}},
  "[NamespaceId](#cfn-redshiftserverless-namespace-namespace-namespaceid)" : {{String}},
  "[NamespaceName](#cfn-redshiftserverless-namespace-namespace-namespacename)" : {{String}},
  "[Status](#cfn-redshiftserverless-namespace-namespace-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-redshiftserverless-namespace-namespace-syntax.yaml"></a>

```
  [AdminPasswordSecretArn](#cfn-redshiftserverless-namespace-namespace-adminpasswordsecretarn): {{String}}
  [AdminPasswordSecretKmsKeyId](#cfn-redshiftserverless-namespace-namespace-adminpasswordsecretkmskeyid): {{String}}
  [AdminUsername](#cfn-redshiftserverless-namespace-namespace-adminusername): {{String}}
  [CreationDate](#cfn-redshiftserverless-namespace-namespace-creationdate): {{String}}
  [DbName](#cfn-redshiftserverless-namespace-namespace-dbname): {{String}}
  [DefaultIamRoleArn](#cfn-redshiftserverless-namespace-namespace-defaultiamrolearn): {{String}}
  [IamRoles](#cfn-redshiftserverless-namespace-namespace-iamroles): {{
    - String}}
  [KmsKeyId](#cfn-redshiftserverless-namespace-namespace-kmskeyid): {{String}}
  [LogExports](#cfn-redshiftserverless-namespace-namespace-logexports): {{
    - String}}
  [NamespaceArn](#cfn-redshiftserverless-namespace-namespace-namespacearn): {{String}}
  [NamespaceId](#cfn-redshiftserverless-namespace-namespace-namespaceid): {{String}}
  [NamespaceName](#cfn-redshiftserverless-namespace-namespace-namespacename): {{String}}
  [Status](#cfn-redshiftserverless-namespace-namespace-status): {{String}}
```

## Properties
<a name="aws-properties-redshiftserverless-namespace-namespace-properties"></a>

`AdminPasswordSecretArn`  <a name="cfn-redshiftserverless-namespace-namespace-adminpasswordsecretarn"></a>
The Amazon Resource Name (ARN) for the namespace's admin user credentials secret.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AdminPasswordSecretKmsKeyId`  <a name="cfn-redshiftserverless-namespace-namespace-adminpasswordsecretkmskeyid"></a>
The ID of the AWS Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AdminUsername`  <a name="cfn-redshiftserverless-namespace-namespace-adminusername"></a>
The username of the administrator for the first database created in the namespace.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreationDate`  <a name="cfn-redshiftserverless-namespace-namespace-creationdate"></a>
The date of when the namespace was created.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DbName`  <a name="cfn-redshiftserverless-namespace-namespace-dbname"></a>
The name of the first database created in the namespace.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z][a-zA-Z_0-9+.@-]*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultIamRoleArn`  <a name="cfn-redshiftserverless-namespace-namespace-defaultiamrolearn"></a>
The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IamRoles`  <a name="cfn-redshiftserverless-namespace-namespace-iamroles"></a>
A list of IAM roles to associate with the namespace.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyId`  <a name="cfn-redshiftserverless-namespace-namespace-kmskeyid"></a>
The ID of the AWS Key Management Service key used to encrypt your data.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogExports`  <a name="cfn-redshiftserverless-namespace-namespace-logexports"></a>
The types of logs the namespace can export. Available export types are User log, Connection log, and User activity log.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `16`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NamespaceArn`  <a name="cfn-redshiftserverless-namespace-namespace-namespacearn"></a>
The Amazon Resource Name (ARN) associated with a namespace.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NamespaceId`  <a name="cfn-redshiftserverless-namespace-namespace-namespaceid"></a>
The unique identifier of a namespace.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NamespaceName`  <a name="cfn-redshiftserverless-namespace-namespace-namespacename"></a>
The name of the namespace. Must be between 3-64 alphanumeric characters in lowercase, and it cannot be a reserved word. A list of reserved words can be found in [Reserved Words](https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html) in the Amazon Redshift Database Developer Guide.
*Required*: No
*Type*: String
*Pattern*: `^[a-z0-9-]+$`
*Minimum*: `3`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-redshiftserverless-namespace-namespace-status"></a>
The status of the namespace.
*Required*: No
*Type*: String
*Allowed values*: `AVAILABLE | MODIFYING | DELETING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
