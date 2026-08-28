---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspacesweb-usersettings-cookiesynchronizationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpacesWeb::UserSettings CookieSynchronizationConfiguration
<a name="aws-properties-workspacesweb-usersettings-cookiesynchronizationconfiguration"></a>

The configuration that specifies which cookies should be synchronized from the end user's local browser to the remote browser.

## Syntax
<a name="aws-properties-workspacesweb-usersettings-cookiesynchronizationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspacesweb-usersettings-cookiesynchronizationconfiguration-syntax.json"></a>

```
{
  "[Allowlist](#cfn-workspacesweb-usersettings-cookiesynchronizationconfiguration-allowlist)" : {{[ CookieSpecification, ... ]}},
  "[Blocklist](#cfn-workspacesweb-usersettings-cookiesynchronizationconfiguration-blocklist)" : {{[ CookieSpecification, ... ]}}
}
```

### YAML
<a name="aws-properties-workspacesweb-usersettings-cookiesynchronizationconfiguration-syntax.yaml"></a>

```
  [Allowlist](#cfn-workspacesweb-usersettings-cookiesynchronizationconfiguration-allowlist): {{
    - CookieSpecification}}
  [Blocklist](#cfn-workspacesweb-usersettings-cookiesynchronizationconfiguration-blocklist): {{
    - CookieSpecification}}
```

## Properties
<a name="aws-properties-workspacesweb-usersettings-cookiesynchronizationconfiguration-properties"></a>

`Allowlist`  <a name="cfn-workspacesweb-usersettings-cookiesynchronizationconfiguration-allowlist"></a>
The list of cookie specifications that are allowed to be synchronized to the remote browser.
*Required*: Yes
*Type*: Array of [CookieSpecification](aws-properties-workspacesweb-usersettings-cookiespecification.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Blocklist`  <a name="cfn-workspacesweb-usersettings-cookiesynchronizationconfiguration-blocklist"></a>
The list of cookie specifications that are blocked from being synchronized to the remote browser.
*Required*: No
*Type*: Array of [CookieSpecification](aws-properties-workspacesweb-usersettings-cookiespecification.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
