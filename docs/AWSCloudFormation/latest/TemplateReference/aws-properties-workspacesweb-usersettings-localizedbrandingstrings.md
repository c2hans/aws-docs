---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspacesweb-usersettings-localizedbrandingstrings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpacesWeb::UserSettings LocalizedBrandingStrings
<a name="aws-properties-workspacesweb-usersettings-localizedbrandingstrings"></a>

Localized text strings for a specific language that customize the web portal.

## Syntax
<a name="aws-properties-workspacesweb-usersettings-localizedbrandingstrings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspacesweb-usersettings-localizedbrandingstrings-syntax.json"></a>

```
{
  "[BrowserTabTitle](#cfn-workspacesweb-usersettings-localizedbrandingstrings-browsertabtitle)" : {{String}},
  "[ContactButtonText](#cfn-workspacesweb-usersettings-localizedbrandingstrings-contactbuttontext)" : {{String}},
  "[ContactLink](#cfn-workspacesweb-usersettings-localizedbrandingstrings-contactlink)" : {{String}},
  "[LoadingText](#cfn-workspacesweb-usersettings-localizedbrandingstrings-loadingtext)" : {{String}},
  "[LoginButtonText](#cfn-workspacesweb-usersettings-localizedbrandingstrings-loginbuttontext)" : {{String}},
  "[LoginDescription](#cfn-workspacesweb-usersettings-localizedbrandingstrings-logindescription)" : {{String}},
  "[LoginTitle](#cfn-workspacesweb-usersettings-localizedbrandingstrings-logintitle)" : {{String}},
  "[WelcomeText](#cfn-workspacesweb-usersettings-localizedbrandingstrings-welcometext)" : {{String}}
}
```

### YAML
<a name="aws-properties-workspacesweb-usersettings-localizedbrandingstrings-syntax.yaml"></a>

```
  [BrowserTabTitle](#cfn-workspacesweb-usersettings-localizedbrandingstrings-browsertabtitle): {{String}}
  [ContactButtonText](#cfn-workspacesweb-usersettings-localizedbrandingstrings-contactbuttontext): {{String}}
  [ContactLink](#cfn-workspacesweb-usersettings-localizedbrandingstrings-contactlink): {{String}}
  [LoadingText](#cfn-workspacesweb-usersettings-localizedbrandingstrings-loadingtext): {{String}}
  [LoginButtonText](#cfn-workspacesweb-usersettings-localizedbrandingstrings-loginbuttontext): {{String}}
  [LoginDescription](#cfn-workspacesweb-usersettings-localizedbrandingstrings-logindescription): {{String}}
  [LoginTitle](#cfn-workspacesweb-usersettings-localizedbrandingstrings-logintitle): {{String}}
  [WelcomeText](#cfn-workspacesweb-usersettings-localizedbrandingstrings-welcometext): {{String}}
```

## Properties
<a name="aws-properties-workspacesweb-usersettings-localizedbrandingstrings-properties"></a>

`BrowserTabTitle`  <a name="cfn-workspacesweb-usersettings-localizedbrandingstrings-browsertabtitle"></a>
The text displayed in the browser tab title.
*Required*: Yes
*Type*: String
*Pattern*: `^[^<>&'`~\\]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContactButtonText`  <a name="cfn-workspacesweb-usersettings-localizedbrandingstrings-contactbuttontext"></a>
The text displayed on the contact button. This field is optional and defaults to "Contact us".
*Required*: No
*Type*: String
*Pattern*: `^[^<>&'`~\\]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContactLink`  <a name="cfn-workspacesweb-usersettings-localizedbrandingstrings-contactlink"></a>
A contact link URL. The URL must start with `https://` or `mailto:`. If not provided, the contact button will be hidden from the web portal screen.
*Required*: No
*Type*: String
*Pattern*: `^(https?://|mailto:).*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LoadingText`  <a name="cfn-workspacesweb-usersettings-localizedbrandingstrings-loadingtext"></a>
The text displayed during session loading. This field is optional and defaults to "Loading your session".
*Required*: No
*Type*: String
*Pattern*: `^[^<>&'`~\\]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LoginButtonText`  <a name="cfn-workspacesweb-usersettings-localizedbrandingstrings-loginbuttontext"></a>
The text displayed on the login button. This field is optional and defaults to "Sign In".
*Required*: No
*Type*: String
*Pattern*: `^[^<>&'`~\\]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LoginDescription`  <a name="cfn-workspacesweb-usersettings-localizedbrandingstrings-logindescription"></a>
The description text for the login section. This field is optional and defaults to "Sign in to your session".
*Required*: No
*Type*: String
*Pattern*: `^[^<>&'`~\\]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LoginTitle`  <a name="cfn-workspacesweb-usersettings-localizedbrandingstrings-logintitle"></a>
The title text for the login section. This field is optional and defaults to "Sign In".
*Required*: No
*Type*: String
*Pattern*: `^[^<>&'`~\\]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WelcomeText`  <a name="cfn-workspacesweb-usersettings-localizedbrandingstrings-welcometext"></a>
The welcome text displayed on the sign-in page.
*Required*: Yes
*Type*: String
*Pattern*: `^[^<>&'`~\\]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
