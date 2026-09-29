---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshift-redshiftidcapplication.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Redshift::RedshiftIdcApplication
<a name="aws-resource-redshift-redshiftidcapplication"></a>

Contains properties for the Redshift IDC application.

## Syntax
<a name="aws-resource-redshift-redshiftidcapplication-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-redshift-redshiftidcapplication-syntax.json"></a>

```
{
  "Type" : "AWS::Redshift::RedshiftIdcApplication",
  "Properties" : {
      "[ApplicationType](#cfn-redshift-redshiftidcapplication-applicationtype)" : {{String}},
      "[AuthorizedTokenIssuerList](#cfn-redshift-redshiftidcapplication-authorizedtokenissuerlist)" : {{[ AuthorizedTokenIssuer, ... ]}},
      "[IamRoleArn](#cfn-redshift-redshiftidcapplication-iamrolearn)" : {{String}},
      "[IdcDisplayName](#cfn-redshift-redshiftidcapplication-idcdisplayname)" : {{String}},
      "[IdcInstanceArn](#cfn-redshift-redshiftidcapplication-idcinstancearn)" : {{String}},
      "[IdentityNamespace](#cfn-redshift-redshiftidcapplication-identitynamespace)" : {{String}},
      "[RedshiftIdcApplicationName](#cfn-redshift-redshiftidcapplication-redshiftidcapplicationname)" : {{String}},
      "[ServiceIntegrations](#cfn-redshift-redshiftidcapplication-serviceintegrations)" : {{[ ServiceIntegrationsUnion, ... ]}},
      "[SsoTagKeys](#cfn-redshift-redshiftidcapplication-ssotagkeys)" : {{[ String, ... ]}},
      "[Tags](#cfn-redshift-redshiftidcapplication-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-redshift-redshiftidcapplication-syntax.yaml"></a>

```
Type: AWS::Redshift::RedshiftIdcApplication
Properties:
  [ApplicationType](#cfn-redshift-redshiftidcapplication-applicationtype): {{String}}
  [AuthorizedTokenIssuerList](#cfn-redshift-redshiftidcapplication-authorizedtokenissuerlist): {{
    - AuthorizedTokenIssuer}}
  [IamRoleArn](#cfn-redshift-redshiftidcapplication-iamrolearn): {{String}}
  [IdcDisplayName](#cfn-redshift-redshiftidcapplication-idcdisplayname): {{String}}
  [IdcInstanceArn](#cfn-redshift-redshiftidcapplication-idcinstancearn): {{String}}
  [IdentityNamespace](#cfn-redshift-redshiftidcapplication-identitynamespace): {{String}}
  [RedshiftIdcApplicationName](#cfn-redshift-redshiftidcapplication-redshiftidcapplicationname): {{String}}
  [ServiceIntegrations](#cfn-redshift-redshiftidcapplication-serviceintegrations): {{
    - ServiceIntegrationsUnion}}
  [SsoTagKeys](#cfn-redshift-redshiftidcapplication-ssotagkeys): {{
    - String}}
  [Tags](#cfn-redshift-redshiftidcapplication-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-redshift-redshiftidcapplication-properties"></a>

`ApplicationType`  <a name="cfn-redshift-redshiftidcapplication-applicationtype"></a>
The type of application being created. Valid values are `None` or `Lakehouse`. Use `Lakehouse` to enable Amazon Redshift federated permissions on cluster.
*Required*: No
*Type*: String
*Allowed values*: `None | Lakehouse`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AuthorizedTokenIssuerList`  <a name="cfn-redshift-redshiftidcapplication-authorizedtokenissuerlist"></a>
The authorized token issuer list for the Amazon Redshift IAM Identity Center application.
*Required*: No
*Type*: Array of [AuthorizedTokenIssuer](aws-properties-redshift-redshiftidcapplication-authorizedtokenissuer.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IamRoleArn`  <a name="cfn-redshift-redshiftidcapplication-iamrolearn"></a>
The ARN for the Amazon Redshift IAM Identity Center application. It has the required permissions to be assumed and invoke the IDC Identity Center API.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z-]*:[a-zA-Z0-9-]+:[a-z0-9-]*:[0-9]*:.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdcDisplayName`  <a name="cfn-redshift-redshiftidcapplication-idcdisplayname"></a>
The display name for the Amazon Redshift IAM Identity Center application. It appears on the console.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w+=,.@-]+$`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdcInstanceArn`  <a name="cfn-redshift-redshiftidcapplication-idcinstancearn"></a>
The ARN for the IAM Identity Center instance that Redshift integrates with.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z-]*:[a-zA-Z0-9-]+:[a-z0-9-]*:[0-9]*:.+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IdentityNamespace`  <a name="cfn-redshift-redshiftidcapplication-identitynamespace"></a>
The identity namespace for the Amazon Redshift IAM Identity Center application. It determines which managed application verifies the connection token.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_+.#@$-]+$`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RedshiftIdcApplicationName`  <a name="cfn-redshift-redshiftidcapplication-redshiftidcapplicationname"></a>
The name of the Redshift application in IAM Identity Center.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z][a-z0-9]*(-[a-z0-9]+)*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServiceIntegrations`  <a name="cfn-redshift-redshiftidcapplication-serviceintegrations"></a>
A list of service integrations for the Redshift IAM Identity Center application.
*Required*: No
*Type*: Array of [ServiceIntegrationsUnion](aws-properties-redshift-redshiftidcapplication-serviceintegrationsunion.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SsoTagKeys`  <a name="cfn-redshift-redshiftidcapplication-ssotagkeys"></a>
A list of tags keys that Redshift Identity Center applications copy to IAM Identity Center. For each input key, the tag corresponding to the key-value pair is propagated.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-redshift-redshiftidcapplication-tags"></a>
A list of tags.
*Required*: No
*Type*: Array of [Tag](aws-properties-redshift-redshiftidcapplication-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-redshift-redshiftidcapplication-return-values"></a>

### Ref
<a name="aws-resource-redshift-redshiftidcapplication-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-redshift-redshiftidcapplication-return-values-fn--getatt"></a>

####
<a name="aws-resource-redshift-redshiftidcapplication-return-values-fn--getatt-fn--getatt"></a>

`IdcManagedApplicationArn`  <a name="IdcManagedApplicationArn-fn::getatt"></a>
The ARN for the Amazon Redshift IAM Identity Center application.

`IdcOnboardStatus`  <a name="IdcOnboardStatus-fn::getatt"></a>
The onboarding status for the Amazon Redshift IAM Identity Center application.

`RedshiftIdcApplicationArn`  <a name="RedshiftIdcApplicationArn-fn::getatt"></a>
The ARN for the Redshift application that integrates with IAM Identity Center.
