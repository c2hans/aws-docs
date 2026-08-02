---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshiftserverless-namespace.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RedshiftServerless::Namespace
<a name="aws-resource-redshiftserverless-namespace"></a>

A collection of database objects and users.

## Syntax
<a name="aws-resource-redshiftserverless-namespace-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-redshiftserverless-namespace-syntax.json"></a>

```
{
  "Type" : "AWS::RedshiftServerless::Namespace",
  "Properties" : {
      "[AdminPasswordSecretKmsKeyId](#cfn-redshiftserverless-namespace-adminpasswordsecretkmskeyid)" : {{String}},
      "[AdminUsername](#cfn-redshiftserverless-namespace-adminusername)" : {{String}},
      "[AdminUserPassword](#cfn-redshiftserverless-namespace-adminuserpassword)" : {{String}},
      "[DbName](#cfn-redshiftserverless-namespace-dbname)" : {{String}},
      "[DefaultIamRoleArn](#cfn-redshiftserverless-namespace-defaultiamrolearn)" : {{String}},
      "[FinalSnapshotName](#cfn-redshiftserverless-namespace-finalsnapshotname)" : {{String}},
      "[FinalSnapshotRetentionPeriod](#cfn-redshiftserverless-namespace-finalsnapshotretentionperiod)" : {{Integer}},
      "[IamRoles](#cfn-redshiftserverless-namespace-iamroles)" : {{[ String, ... ]}},
      "[KmsKeyId](#cfn-redshiftserverless-namespace-kmskeyid)" : {{String}},
      "[LogExports](#cfn-redshiftserverless-namespace-logexports)" : {{[ String, ... ]}},
      "[ManageAdminPassword](#cfn-redshiftserverless-namespace-manageadminpassword)" : {{Boolean}},
      "[NamespaceName](#cfn-redshiftserverless-namespace-namespacename)" : {{String}},
      "[NamespaceResourcePolicy](#cfn-redshiftserverless-namespace-namespaceresourcepolicy)" : {{Json}},
      "[RedshiftIdcApplicationArn](#cfn-redshiftserverless-namespace-redshiftidcapplicationarn)" : {{String}},
      "[SnapshotCopyConfigurations](#cfn-redshiftserverless-namespace-snapshotcopyconfigurations)" : {{[ SnapshotCopyConfiguration, ... ]}},
      "[Tags](#cfn-redshiftserverless-namespace-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-redshiftserverless-namespace-syntax.yaml"></a>

```
Type: AWS::RedshiftServerless::Namespace
Properties:
  [AdminPasswordSecretKmsKeyId](#cfn-redshiftserverless-namespace-adminpasswordsecretkmskeyid): {{String}}
  [AdminUsername](#cfn-redshiftserverless-namespace-adminusername): {{String}}
  [AdminUserPassword](#cfn-redshiftserverless-namespace-adminuserpassword): {{String}}
  [DbName](#cfn-redshiftserverless-namespace-dbname): {{String}}
  [DefaultIamRoleArn](#cfn-redshiftserverless-namespace-defaultiamrolearn): {{String}}
  [FinalSnapshotName](#cfn-redshiftserverless-namespace-finalsnapshotname): {{String}}
  [FinalSnapshotRetentionPeriod](#cfn-redshiftserverless-namespace-finalsnapshotretentionperiod): {{Integer}}
  [IamRoles](#cfn-redshiftserverless-namespace-iamroles): {{
    - String}}
  [KmsKeyId](#cfn-redshiftserverless-namespace-kmskeyid): {{String}}
  [LogExports](#cfn-redshiftserverless-namespace-logexports): {{
    - String}}
  [ManageAdminPassword](#cfn-redshiftserverless-namespace-manageadminpassword): {{Boolean}}
  [NamespaceName](#cfn-redshiftserverless-namespace-namespacename): {{String}}
  [NamespaceResourcePolicy](#cfn-redshiftserverless-namespace-namespaceresourcepolicy): {{Json}}
  [RedshiftIdcApplicationArn](#cfn-redshiftserverless-namespace-redshiftidcapplicationarn): {{String}}
  [SnapshotCopyConfigurations](#cfn-redshiftserverless-namespace-snapshotcopyconfigurations): {{
    - SnapshotCopyConfiguration}}
  [Tags](#cfn-redshiftserverless-namespace-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-redshiftserverless-namespace-properties"></a>

`AdminPasswordSecretKmsKeyId`  <a name="cfn-redshiftserverless-namespace-adminpasswordsecretkmskeyid"></a>
The ID of the AWS Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret. You can only use this parameter if `ManageAdminPassword` is `true`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AdminUsername`  <a name="cfn-redshiftserverless-namespace-adminusername"></a>
The username of the administrator for the primary database created in the namespace.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z][a-zA-Z_0-9+.@-]*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AdminUserPassword`  <a name="cfn-redshiftserverless-namespace-adminuserpassword"></a>
The password of the administrator for the primary database created in the namespace.
*Required*: No
*Type*: String
*Pattern*: `^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\x00-\x20\x22\x27\x2f\x40\x5c\x7f-\uffff]+`
*Minimum*: `8`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DbName`  <a name="cfn-redshiftserverless-namespace-dbname"></a>
The name of the primary database created in the namespace.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z][a-zA-Z_0-9+.@-]*`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultIamRoleArn`  <a name="cfn-redshiftserverless-namespace-defaultiamrolearn"></a>
The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FinalSnapshotName`  <a name="cfn-redshiftserverless-namespace-finalsnapshotname"></a>
The name of the snapshot to be created before the namespace is deleted.
*Required*: No
*Type*: String
*Pattern*: `[a-z][a-z0-9]*(-[a-z0-9]+)*`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FinalSnapshotRetentionPeriod`  <a name="cfn-redshiftserverless-namespace-finalsnapshotretentionperiod"></a>
How long to retain the final snapshot.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IamRoles`  <a name="cfn-redshiftserverless-namespace-iamroles"></a>
A list of IAM roles to associate with the namespace.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyId`  <a name="cfn-redshiftserverless-namespace-kmskeyid"></a>
The ID of the AWS Key Management Service key used to encrypt your data.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogExports`  <a name="cfn-redshiftserverless-namespace-logexports"></a>
The types of logs the namespace can export. Available export types are `userlog`, `connectionlog`, and `useractivitylog`.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `16`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManageAdminPassword`  <a name="cfn-redshiftserverless-namespace-manageadminpassword"></a>
If true, Amazon Redshift uses AWS Secrets Manager to manage the namespace's admin credentials. You can't use `AdminUserPassword` if `ManageAdminPassword` is true. If `ManageAdminPassword` is `false` or not set, Amazon Redshift uses `AdminUserPassword` for the admin user account's password.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NamespaceName`  <a name="cfn-redshiftserverless-namespace-namespacename"></a>
The name of the namespace. Must be between 3-64 alphanumeric characters in lowercase, and it cannot be a reserved word. A list of reserved words can be found in [Reserved Words](https://docs.aws.amazon.com//redshift/latest/dg/r_pg_keywords.html) in the Amazon Redshift Database Developer Guide.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9-]+$`
*Minimum*: `3`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NamespaceResourcePolicy`  <a name="cfn-redshiftserverless-namespace-namespaceresourcepolicy"></a>
The resource policy that will be attached to the namespace.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RedshiftIdcApplicationArn`  <a name="cfn-redshiftserverless-namespace-redshiftidcapplicationarn"></a>
The ARN for the Redshift application that integrates with IAM Identity Center.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnapshotCopyConfigurations`  <a name="cfn-redshiftserverless-namespace-snapshotcopyconfigurations"></a>
Property description not available.
*Required*: No
*Type*: Array of [SnapshotCopyConfiguration](aws-properties-redshiftserverless-namespace-snapshotcopyconfiguration.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-redshiftserverless-namespace-tags"></a>
The map of the key-value pairs used to tag the namespace.
*Required*: No
*Type*: Array of [Tag](aws-properties-redshiftserverless-namespace-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-redshiftserverless-namespace-return-values"></a>

### Ref
<a name="aws-resource-redshiftserverless-namespace-return-values-ref"></a>

When the logical ID of this resource is provided to the Ref intrinsic function, Ref returns the NamespaceName, such as `sample-namespace.` For more information about using the Ref function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-redshiftserverless-namespace-return-values-fn--getatt"></a>

GetAtt returns a value for a specified attribute of this type. For more information, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html). The following are the available attributes and sample return values.

####
<a name="aws-resource-redshiftserverless-namespace-return-values-fn--getatt-fn--getatt"></a>

`Namespace.AdminUsername`  <a name="Namespace.AdminUsername-fn::getatt"></a>
The username of the administrator for the first database created in the namespace.

`Namespace.CreationDate`  <a name="Namespace.CreationDate-fn::getatt"></a>
The date of when the namespace was created.

`Namespace.DbName`  <a name="Namespace.DbName-fn::getatt"></a>
The name of the first database created in the namespace.

`Namespace.DefaultIamRoleArn`  <a name="Namespace.DefaultIamRoleArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.

`Namespace.IamRoles`  <a name="Namespace.IamRoles-fn::getatt"></a>
A list of IAM roles to associate with the namespace.

`Namespace.KmsKeyId`  <a name="Namespace.KmsKeyId-fn::getatt"></a>
The ID of the AWS Key Management Service key used to encrypt your data.

`Namespace.LogExports`  <a name="Namespace.LogExports-fn::getatt"></a>
The types of logs the namespace can export. Available export types are `User log`, `Connection log`, and `User activity log`.

`Namespace.NamespaceArn`  <a name="Namespace.NamespaceArn-fn::getatt"></a>
The Amazon Resource Name (ARN) associated with a namespace.

`Namespace.NamespaceId`  <a name="Namespace.NamespaceId-fn::getatt"></a>
The unique identifier of a namespace.

`Namespace.NamespaceName`  <a name="Namespace.NamespaceName-fn::getatt"></a>
The name of the namespace. Must be between 3-64 alphanumeric characters in lowercase, and it cannot be a reserved word. A list of reserved words can be found in [Reserved Words](https://docs.aws.amazon.com//redshift/latest/dg/r_pg_keywords.html) in the Amazon Redshift Database Developer Guide.

`Namespace.Status`  <a name="Namespace.Status-fn::getatt"></a>
The status of the namespace.
