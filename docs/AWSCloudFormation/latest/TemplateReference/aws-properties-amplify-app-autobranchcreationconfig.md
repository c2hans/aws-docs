---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplify-app-autobranchcreationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Amplify::App AutoBranchCreationConfig
<a name="aws-properties-amplify-app-autobranchcreationconfig"></a>

 Use the AutoBranchCreationConfig property type to automatically create branches that match a certain pattern.

## Syntax
<a name="aws-properties-amplify-app-autobranchcreationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplify-app-autobranchcreationconfig-syntax.json"></a>

```
{
  "[AutoBranchCreationPatterns](#cfn-amplify-app-autobranchcreationconfig-autobranchcreationpatterns)" : {{[ String, ... ]}},
  "[BasicAuthConfig](#cfn-amplify-app-autobranchcreationconfig-basicauthconfig)" : {{BasicAuthConfig}},
  "[BuildSpec](#cfn-amplify-app-autobranchcreationconfig-buildspec)" : {{String}},
  "[EnableAutoBranchCreation](#cfn-amplify-app-autobranchcreationconfig-enableautobranchcreation)" : {{Boolean}},
  "[EnableAutoBuild](#cfn-amplify-app-autobranchcreationconfig-enableautobuild)" : {{Boolean}},
  "[EnablePerformanceMode](#cfn-amplify-app-autobranchcreationconfig-enableperformancemode)" : {{Boolean}},
  "[EnablePullRequestPreview](#cfn-amplify-app-autobranchcreationconfig-enablepullrequestpreview)" : {{Boolean}},
  "[EnvironmentVariables](#cfn-amplify-app-autobranchcreationconfig-environmentvariables)" : {{[ EnvironmentVariable, ... ]}},
  "[Framework](#cfn-amplify-app-autobranchcreationconfig-framework)" : {{String}},
  "[PullRequestEnvironmentName](#cfn-amplify-app-autobranchcreationconfig-pullrequestenvironmentname)" : {{String}},
  "[Stage](#cfn-amplify-app-autobranchcreationconfig-stage)" : {{String}}
}
```

### YAML
<a name="aws-properties-amplify-app-autobranchcreationconfig-syntax.yaml"></a>

```
  [AutoBranchCreationPatterns](#cfn-amplify-app-autobranchcreationconfig-autobranchcreationpatterns): {{
    - String}}
  [BasicAuthConfig](#cfn-amplify-app-autobranchcreationconfig-basicauthconfig): {{
    BasicAuthConfig}}
  [BuildSpec](#cfn-amplify-app-autobranchcreationconfig-buildspec): {{String}}
  [EnableAutoBranchCreation](#cfn-amplify-app-autobranchcreationconfig-enableautobranchcreation): {{Boolean}}
  [EnableAutoBuild](#cfn-amplify-app-autobranchcreationconfig-enableautobuild): {{Boolean}}
  [EnablePerformanceMode](#cfn-amplify-app-autobranchcreationconfig-enableperformancemode): {{Boolean}}
  [EnablePullRequestPreview](#cfn-amplify-app-autobranchcreationconfig-enablepullrequestpreview): {{Boolean}}
  [EnvironmentVariables](#cfn-amplify-app-autobranchcreationconfig-environmentvariables): {{
    - EnvironmentVariable}}
  [Framework](#cfn-amplify-app-autobranchcreationconfig-framework): {{String}}
  [PullRequestEnvironmentName](#cfn-amplify-app-autobranchcreationconfig-pullrequestenvironmentname): {{String}}
  [Stage](#cfn-amplify-app-autobranchcreationconfig-stage): {{String}}
```

## Properties
<a name="aws-properties-amplify-app-autobranchcreationconfig-properties"></a>

`AutoBranchCreationPatterns`  <a name="cfn-amplify-app-autobranchcreationconfig-autobranchcreationpatterns"></a>
Automated branch creation glob patterns for the Amplify app.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BasicAuthConfig`  <a name="cfn-amplify-app-autobranchcreationconfig-basicauthconfig"></a>
Sets password protection for your auto created branch.
*Required*: No
*Type*: [BasicAuthConfig](aws-properties-amplify-app-basicauthconfig.md)
*Pattern*: `(?s).*`
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BuildSpec`  <a name="cfn-amplify-app-autobranchcreationconfig-buildspec"></a>
 The build specification (build spec) for the autocreated branch.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `25000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableAutoBranchCreation`  <a name="cfn-amplify-app-autobranchcreationconfig-enableautobranchcreation"></a>
Enables automated branch creation for the Amplify app.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableAutoBuild`  <a name="cfn-amplify-app-autobranchcreationconfig-enableautobuild"></a>
Enables auto building for the auto created branch.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnablePerformanceMode`  <a name="cfn-amplify-app-autobranchcreationconfig-enableperformancemode"></a>
Enables performance mode for the branch.
Performance mode optimizes for faster hosting performance by keeping content cached at the edge for a longer interval. When performance mode is enabled, hosting configuration or code changes can take up to 10 minutes to roll out.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnablePullRequestPreview`  <a name="cfn-amplify-app-autobranchcreationconfig-enablepullrequestpreview"></a>
Sets whether pull request previews are enabled for each branch that Amplify Hosting automatically creates for your app. Amplify creates previews by deploying your app to a unique URL whenever a pull request is opened for the branch. Development and QA teams can use this preview to test the pull request before it's merged into a production or integration branch.
To provide backend support for your preview, Amplify Hosting automatically provisions a temporary backend environment that it deletes when the pull request is closed. If you want to specify a dedicated backend environment for your previews, use the `PullRequestEnvironmentName` property.
For more information, see [Web Previews](https://docs.aws.amazon.com/amplify/latest/userguide/pr-previews.html) in the *AWS Amplify Hosting User Guide*.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentVariables`  <a name="cfn-amplify-app-autobranchcreationconfig-environmentvariables"></a>
The environment variables for the autocreated branch.
*Required*: No
*Type*: Array of [EnvironmentVariable](aws-properties-amplify-app-environmentvariable.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Framework`  <a name="cfn-amplify-app-autobranchcreationconfig-framework"></a>
The framework for the autocreated branch.
*Required*: No
*Type*: String
*Pattern*: `(?s).*`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PullRequestEnvironmentName`  <a name="cfn-amplify-app-autobranchcreationconfig-pullrequestenvironmentname"></a>
If pull request previews are enabled, you can use this property to specify a dedicated backend environment for your previews. For example, you could specify an environment named `prod`, `test`, or `dev` that you initialized with the Amplify CLI.
To enable pull request previews, set the `EnablePullRequestPreview` property to `true`.
If you don't specify an environment, Amplify Hosting provides backend support for each preview by automatically provisioning a temporary backend environment. Amplify deletes this environment when the pull request is closed.
For more information about creating backend environments, see [Feature Branch Deployments and Team Workflows](https://docs.aws.amazon.com/amplify/latest/userguide/multi-environments.html) in the *AWS Amplify Hosting User Guide*.
*Required*: No
*Type*: String
*Pattern*: `(?s).*`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Stage`  <a name="cfn-amplify-app-autobranchcreationconfig-stage"></a>
Stage for the auto created branch.
*Required*: No
*Type*: String
*Allowed values*: `EXPERIMENTAL | BETA | PULL_REQUEST | PRODUCTION | DEVELOPMENT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
