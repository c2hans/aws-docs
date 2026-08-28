---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-gitlabdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service GitLabDetails
<a name="aws-properties-devopsagent-service-gitlabdetails"></a>

Configuration details for registering a GitLab service.

## Syntax
<a name="aws-properties-devopsagent-service-gitlabdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-gitlabdetails-syntax.json"></a>

```
{
  "[GroupId](#cfn-devopsagent-service-gitlabdetails-groupid)" : {{String}},
  "[TargetUrl](#cfn-devopsagent-service-gitlabdetails-targeturl)" : {{String}},
  "[TokenType](#cfn-devopsagent-service-gitlabdetails-tokentype)" : {{String}},
  "[TokenValue](#cfn-devopsagent-service-gitlabdetails-tokenvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-gitlabdetails-syntax.yaml"></a>

```
  [GroupId](#cfn-devopsagent-service-gitlabdetails-groupid): {{String}}
  [TargetUrl](#cfn-devopsagent-service-gitlabdetails-targeturl): {{String}}
  [TokenType](#cfn-devopsagent-service-gitlabdetails-tokentype): {{String}}
  [TokenValue](#cfn-devopsagent-service-gitlabdetails-tokenvalue): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-service-gitlabdetails-properties"></a>

`GroupId`  <a name="cfn-devopsagent-service-gitlabdetails-groupid"></a>
The GitLab group ID. Required when `TokenType` is `group`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetUrl`  <a name="cfn-devopsagent-service-gitlabdetails-targeturl"></a>
The GitLab instance URL. Must be an HTTPS URL.
*Required*: Yes
*Type*: String
*Pattern*: `^https://[a-zA-Z0-9]([a-zA-Z0-9.-]*[a-zA-Z0-9])?(?::[0-9]{1,5})?/?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TokenType`  <a name="cfn-devopsagent-service-gitlabdetails-tokentype"></a>
The type of GitLab access token.
*Allowed Values*: `personal` \| `group`
*Required*: Yes
*Type*: String
*Allowed values*: `personal | group`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TokenValue`  <a name="cfn-devopsagent-service-gitlabdetails-tokenvalue"></a>
The GitLab access token value. Must match the pattern `^glpat-[a-zA-Z0-9._-]+$`.
*Required*: Yes
*Type*: String
*Pattern*: `^glpat-[a-zA-Z0-9._-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
