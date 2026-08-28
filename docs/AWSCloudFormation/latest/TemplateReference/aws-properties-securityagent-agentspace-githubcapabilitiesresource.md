---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityagent-agentspace-githubcapabilitiesresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityAgent::AgentSpace GitHubCapabilitiesResource
<a name="aws-properties-securityagent-agentspace-githubcapabilitiesresource"></a>

The capabilities enabled for a GitHub resource integration.

## Syntax
<a name="aws-properties-securityagent-agentspace-githubcapabilitiesresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityagent-agentspace-githubcapabilitiesresource-syntax.json"></a>

```
{
  "[LeaveComments](#cfn-securityagent-agentspace-githubcapabilitiesresource-leavecomments)" : {{Boolean}},
  "[RemediateCode](#cfn-securityagent-agentspace-githubcapabilitiesresource-remediatecode)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-securityagent-agentspace-githubcapabilitiesresource-syntax.yaml"></a>

```
  [LeaveComments](#cfn-securityagent-agentspace-githubcapabilitiesresource-leavecomments): {{Boolean}}
  [RemediateCode](#cfn-securityagent-agentspace-githubcapabilitiesresource-remediatecode): {{Boolean}}
```

## Properties
<a name="aws-properties-securityagent-agentspace-githubcapabilitiesresource-properties"></a>

`LeaveComments`  <a name="cfn-securityagent-agentspace-githubcapabilitiesresource-leavecomments"></a>
Indicates whether the integration can leave comments on pull requests.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RemediateCode`  <a name="cfn-securityagent-agentspace-githubcapabilitiesresource-remediatecode"></a>
Indicates whether the integration can create code remediation pull requests.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
