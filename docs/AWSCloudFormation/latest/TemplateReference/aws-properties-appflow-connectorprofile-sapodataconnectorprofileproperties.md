---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-connectorprofile-sapodataconnectorprofileproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::ConnectorProfile SAPODataConnectorProfileProperties
<a name="aws-properties-appflow-connectorprofile-sapodataconnectorprofileproperties"></a>

 The connector-specific profile properties required when using SAPOData.

## Syntax
<a name="aws-properties-appflow-connectorprofile-sapodataconnectorprofileproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-connectorprofile-sapodataconnectorprofileproperties-syntax.json"></a>

```
{
  "[ApplicationHostUrl](#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-applicationhosturl)" : {{String}},
  "[ApplicationServicePath](#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-applicationservicepath)" : {{String}},
  "[ClientNumber](#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-clientnumber)" : {{String}},
  "[DisableSSO](#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-disablesso)" : {{Boolean}},
  "[LogonLanguage](#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-logonlanguage)" : {{String}},
  "[OAuthProperties](#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-oauthproperties)" : {{OAuthProperties}},
  "[PortNumber](#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-portnumber)" : {{Integer}},
  "[PrivateLinkServiceName](#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-privatelinkservicename)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-connectorprofile-sapodataconnectorprofileproperties-syntax.yaml"></a>

```
  [ApplicationHostUrl](#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-applicationhosturl): {{String}}
  [ApplicationServicePath](#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-applicationservicepath): {{String}}
  [ClientNumber](#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-clientnumber): {{String}}
  [DisableSSO](#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-disablesso): {{Boolean}}
  [LogonLanguage](#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-logonlanguage): {{String}}
  [OAuthProperties](#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-oauthproperties): {{
    OAuthProperties}}
  [PortNumber](#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-portnumber): {{Integer}}
  [PrivateLinkServiceName](#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-privatelinkservicename): {{String}}
```

## Properties
<a name="aws-properties-appflow-connectorprofile-sapodataconnectorprofileproperties-properties"></a>

`ApplicationHostUrl`  <a name="cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-applicationhosturl"></a>
 The location of the SAPOData resource.
*Required*: No
*Type*: String
*Pattern*: `^(https?)://[-a-zA-Z0-9+&amp;@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&amp;@#/%=~_|]`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicationServicePath`  <a name="cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-applicationservicepath"></a>
 The application path to catalog service.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientNumber`  <a name="cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-clientnumber"></a>
 The client number for the client creating the connection.
*Required*: No
*Type*: String
*Pattern*: `^\d{3}$`
*Minimum*: `3`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisableSSO`  <a name="cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-disablesso"></a>
If you set this parameter to `true`, Amazon AppFlow bypasses the single sign-on (SSO) settings in your SAP account when it accesses your SAP OData instance.
Whether you need this option depends on the types of credentials that you applied to your SAP OData connection profile. If your profile uses basic authentication credentials, SAP SSO can prevent Amazon AppFlow from connecting to your account with your username and password. In this case, bypassing SSO makes it possible for Amazon AppFlow to connect successfully. However, if your profile uses OAuth credentials, this parameter has no affect.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogonLanguage`  <a name="cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-logonlanguage"></a>
 The logon language of SAPOData instance.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_]*$`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OAuthProperties`  <a name="cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-oauthproperties"></a>
 The SAPOData OAuth properties required for OAuth type authentication.
*Required*: No
*Type*: [OAuthProperties](aws-properties-appflow-connectorprofile-oauthproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PortNumber`  <a name="cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-portnumber"></a>
 The port number of the SAPOData instance.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateLinkServiceName`  <a name="cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-privatelinkservicename"></a>
 The SAPOData Private Link service name to be used for private data transfers.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
