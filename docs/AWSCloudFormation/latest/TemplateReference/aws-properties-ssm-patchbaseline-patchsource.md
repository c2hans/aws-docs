---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssm-patchbaseline-patchsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::PatchBaseline PatchSource
<a name="aws-properties-ssm-patchbaseline-patchsource"></a>

`PatchSource` is the property type for the `Sources` resource of the [AWS::SSM::PatchBaseline](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html) resource.

The AWS CloudFormation`AWS::SSM::PatchSource` resource is used to provide information about the patches to use to update target instances, including target operating systems and source repository. Applies to Linux managed nodes only.

## Syntax
<a name="aws-properties-ssm-patchbaseline-patchsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssm-patchbaseline-patchsource-syntax.json"></a>

```
{
  "[Configuration](#cfn-ssm-patchbaseline-patchsource-configuration)" : {{String}},
  "[Name](#cfn-ssm-patchbaseline-patchsource-name)" : {{String}},
  "[Products](#cfn-ssm-patchbaseline-patchsource-products)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ssm-patchbaseline-patchsource-syntax.yaml"></a>

```
  [Configuration](#cfn-ssm-patchbaseline-patchsource-configuration): {{String}}
  [Name](#cfn-ssm-patchbaseline-patchsource-name): {{String}}
  [Products](#cfn-ssm-patchbaseline-patchsource-products): {{
    - String}}
```

## Properties
<a name="aws-properties-ssm-patchbaseline-patchsource-properties"></a>

`Configuration`  <a name="cfn-ssm-patchbaseline-patchsource-configuration"></a>
The value of the repo configuration.
 **Example for yum repositories**
 `[main]`
 `name=MyCustomRepository`
 `baseurl=https://my-custom-repository`
 `enabled=1`
For information about other options available for your yum repository configuration, see [dnf.conf(5)](https://man7.org/linux/man-pages/man5/dnf.conf.5.html) on the *man7.org* website.
 **Examples for Ubuntu Server and Debian Server**
 `deb http://security.ubuntu.com/ubuntu jammy main`
 `deb https://site.example.com/debian distribution component1 component2 component3`
Repo information for Ubuntu Server repositories must be specifed in a single line. For more examples and information, see [jammy (5) sources.list.5.gz](https://manpages.ubuntu.com/manpages/jammy/man5/sources.list.5.html) on the *Ubuntu Server Manuals* website and [sources.list format](https://wiki.debian.org/SourcesList#sources.list_format) on the *Debian Wiki*.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-ssm-patchbaseline-patchsource-name"></a>
The name specified to identify the patch source.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-.]{3,50}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Products`  <a name="cfn-ssm-patchbaseline-patchsource-products"></a>
The specific operating system versions a patch repository applies to, such as "Ubuntu16.04", "RedhatEnterpriseLinux7.2" or "Suse12.7". For lists of supported product values, see [PatchFilter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchFilter.html) in the *AWS Systems Manager API Reference*.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `128 | 20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
