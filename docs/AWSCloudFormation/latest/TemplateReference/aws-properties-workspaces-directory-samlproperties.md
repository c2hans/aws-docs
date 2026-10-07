---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspaces-directory-samlproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpaces::Directory SamlProperties
<a name="aws-properties-workspaces-directory-samlproperties"></a>

Describes the enablement status, user access URL, and relay state parameter name that are used for configuring federation with an SAML 2.0 identity provider.

## Syntax
<a name="aws-properties-workspaces-directory-samlproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspaces-directory-samlproperties-syntax.json"></a>

```
{
  "[RelayStateParameterName](#cfn-workspaces-directory-samlproperties-relaystateparametername)" : {{String}},
  "[Status](#cfn-workspaces-directory-samlproperties-status)" : {{String}},
  "[UserAccessUrl](#cfn-workspaces-directory-samlproperties-useraccessurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-workspaces-directory-samlproperties-syntax.yaml"></a>

```
  [RelayStateParameterName](#cfn-workspaces-directory-samlproperties-relaystateparametername): {{String}}
  [Status](#cfn-workspaces-directory-samlproperties-status): {{String}}
  [UserAccessUrl](#cfn-workspaces-directory-samlproperties-useraccessurl): {{String}}
```

## Properties
<a name="aws-properties-workspaces-directory-samlproperties-properties"></a>

`RelayStateParameterName`  <a name="cfn-workspaces-directory-samlproperties-relaystateparametername"></a>
The relay state parameter name supported by the SAML 2.0 identity provider (IdP). When the end user is redirected to the user access URL from the WorkSpaces client application, this relay state parameter name is appended as a query parameter to the URL along with the relay state endpoint to return the user to the client application session.
To use SAML 2.0 authentication with WorkSpaces, the IdP must support IdP-initiated deep linking for the relay state URL. Consult your IdP documentation for more information.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-workspaces-directory-samlproperties-status"></a>
Indicates the status of SAML 2.0 authentication. These statuses include the following.
+ If the setting is `DISABLED`, end users will be directed to login with their directory credentials.
+ If the setting is `ENABLED`, end users will be directed to login via the user access URL. Users attempting to connect to WorkSpaces from a client application that does not support SAML 2.0 authentication will not be able to connect.
+ If the setting is `ENABLED_WITH_DIRECTORY_LOGIN_FALLBACK`, end users will be directed to login via the user access URL on supported client applications, but will not prevent clients that do not support SAML 2.0 authentication from connecting as if SAML 2.0 authentication was disabled.
*Required*: No
*Type*: String
*Allowed values*: `DISABLED | ENABLED | ENABLED_WITH_DIRECTORY_LOGIN_FALLBACK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserAccessUrl`  <a name="cfn-workspaces-directory-samlproperties-useraccessurl"></a>
The SAML 2.0 identity provider (IdP) user access URL is the URL a user would navigate to in their web browser in order to federate from the IdP and directly access the application, without any SAML 2.0 service provider (SP) bindings.
*Required*: No
*Type*: String
*Pattern*: `^(http|https)\://\S+$`
*Minimum*: `8`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
