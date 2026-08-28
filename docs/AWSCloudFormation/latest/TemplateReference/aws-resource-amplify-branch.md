---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-amplify-branch.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Amplify::Branch
<a name="aws-resource-amplify-branch"></a>

 The AWS::Amplify::Branch resource specifies a new branch within an app.

## Syntax
<a name="aws-resource-amplify-branch-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-amplify-branch-syntax.json"></a>

```
{
  "Type" : "AWS::Amplify::Branch",
  "Properties" : {
      "[AppId](#cfn-amplify-branch-appid)" : {{String}},
      "[Backend](#cfn-amplify-branch-backend)" : {{Backend}},
      "[BasicAuthConfig](#cfn-amplify-branch-basicauthconfig)" : {{BasicAuthConfig}},
      "[BranchName](#cfn-amplify-branch-branchname)" : {{String}},
      "[BuildSpec](#cfn-amplify-branch-buildspec)" : {{String}},
      "[ComputeRoleArn](#cfn-amplify-branch-computerolearn)" : {{String}},
      "[Description](#cfn-amplify-branch-description)" : {{String}},
      "[EnableAutoBuild](#cfn-amplify-branch-enableautobuild)" : {{Boolean}},
      "[EnablePerformanceMode](#cfn-amplify-branch-enableperformancemode)" : {{Boolean}},
      "[EnablePullRequestPreview](#cfn-amplify-branch-enablepullrequestpreview)" : {{Boolean}},
      "[EnableSkewProtection](#cfn-amplify-branch-enableskewprotection)" : {{Boolean}},
      "[EnvironmentVariables](#cfn-amplify-branch-environmentvariables)" : {{[ EnvironmentVariable, ... ]}},
      "[Framework](#cfn-amplify-branch-framework)" : {{String}},
      "[PullRequestEnvironmentName](#cfn-amplify-branch-pullrequestenvironmentname)" : {{String}},
      "[Stage](#cfn-amplify-branch-stage)" : {{String}},
      "[Tags](#cfn-amplify-branch-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-amplify-branch-syntax.yaml"></a>

```
Type: AWS::Amplify::Branch
Properties:
  [AppId](#cfn-amplify-branch-appid): {{String}}
  [Backend](#cfn-amplify-branch-backend): {{
    Backend}}
  [BasicAuthConfig](#cfn-amplify-branch-basicauthconfig): {{
    BasicAuthConfig}}
  [BranchName](#cfn-amplify-branch-branchname): {{String}}
  [BuildSpec](#cfn-amplify-branch-buildspec): {{String}}
  [ComputeRoleArn](#cfn-amplify-branch-computerolearn): {{String}}
  [Description](#cfn-amplify-branch-description): {{String}}
  [EnableAutoBuild](#cfn-amplify-branch-enableautobuild): {{Boolean}}
  [EnablePerformanceMode](#cfn-amplify-branch-enableperformancemode): {{Boolean}}
  [EnablePullRequestPreview](#cfn-amplify-branch-enablepullrequestpreview): {{Boolean}}
  [EnableSkewProtection](#cfn-amplify-branch-enableskewprotection): {{Boolean}}
  [EnvironmentVariables](#cfn-amplify-branch-environmentvariables): {{
    - EnvironmentVariable}}
  [Framework](#cfn-amplify-branch-framework): {{String}}
  [PullRequestEnvironmentName](#cfn-amplify-branch-pullrequestenvironmentname): {{String}}
  [Stage](#cfn-amplify-branch-stage): {{String}}
  [Tags](#cfn-amplify-branch-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-amplify-branch-properties"></a>

`AppId`  <a name="cfn-amplify-branch-appid"></a>
 The unique ID for an Amplify app.
*Required*: Yes
*Type*: String
*Pattern*: `d[a-z0-9]+`
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Backend`  <a name="cfn-amplify-branch-backend"></a>
The backend for a `Branch` of an Amplify app. Use for a backend created from an CloudFormation stack.
This field is available to Amplify Gen 2 apps only. When you deploy an application with Amplify Gen 2, you provision the app's backend infrastructure using Typescript code.
*Required*: No
*Type*: [Backend](aws-properties-amplify-branch-backend.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BasicAuthConfig`  <a name="cfn-amplify-branch-basicauthconfig"></a>
 The basic authorization credentials for a branch of an Amplify app. You must base64-encode the authorization credentials and provide them in the format `user:password`.
*Required*: No
*Type*: [BasicAuthConfig](aws-properties-amplify-branch-basicauthconfig.md)
*Pattern*: `(?s).*`
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BranchName`  <a name="cfn-amplify-branch-branchname"></a>
The name for the branch.
*Required*: Yes
*Type*: String
*Pattern*: `(?s).+`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BuildSpec`  <a name="cfn-amplify-branch-buildspec"></a>
 The build specification (build spec) for the branch.
*Required*: No
*Type*: String
*Pattern*: `(?s).+`
*Minimum*: `1`
*Maximum*: `25000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComputeRoleArn`  <a name="cfn-amplify-branch-computerolearn"></a>
The Amazon Resource Name (ARN) of the IAM role to assign to a branch of an SSR app. The SSR Compute role allows the Amplify Hosting compute service to securely access specific AWS resources based on the role's permissions. For more information about the SSR Compute role, see [Adding an SSR Compute role](https://docs.aws.amazon.com/amplify/latest/userguide/amplify-SSR-compute-role.html) in the *Amplify User Guide*.
*Required*: No
*Type*: String
*Pattern*: `(?s).*`
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-amplify-branch-description"></a>
 The description for the branch that is part of an Amplify app.
*Required*: No
*Type*: String
*Pattern*: `(?s).*`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableAutoBuild`  <a name="cfn-amplify-branch-enableautobuild"></a>
 Enables auto building for the branch.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnablePerformanceMode`  <a name="cfn-amplify-branch-enableperformancemode"></a>
Enables performance mode for the branch.
Performance mode optimizes for faster hosting performance by keeping content cached at the edge for a longer interval. When performance mode is enabled, hosting configuration or code changes can take up to 10 minutes to roll out.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnablePullRequestPreview`  <a name="cfn-amplify-branch-enablepullrequestpreview"></a>
Specifies whether Amplify Hosting creates a preview for each pull request that is made for this branch. If this property is enabled, Amplify deploys your app to a unique preview URL after each pull request is opened. Development and QA teams can use this preview to test the pull request before it's merged into a production or integration branch.
To provide backend support for your preview, Amplify automatically provisions a temporary backend environment that it deletes when the pull request is closed. If you want to specify a dedicated backend environment for your previews, use the `PullRequestEnvironmentName` property.
For more information, see [Web Previews](https://docs.aws.amazon.com/amplify/latest/userguide/pr-previews.html) in the *AWS Amplify Hosting User Guide*.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableSkewProtection`  <a name="cfn-amplify-branch-enableskewprotection"></a>
Specifies whether the skew protection feature is enabled for the branch.
Deployment skew protection is available to Amplify applications to eliminate version skew issues between client and servers in web applications. When you apply skew protection to a branch, you can ensure that your clients always interact with the correct version of server-side assets, regardless of when a deployment occurs. For more information about skew protection, see [Skew protection for Amplify deployments](https://docs.aws.amazon.com/amplify/latest/userguide/skew-protection.html) in the *Amplify User Guide*.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentVariables`  <a name="cfn-amplify-branch-environmentvariables"></a>
 The environment variables for the branch.
*Required*: No
*Type*: Array of [EnvironmentVariable](aws-properties-amplify-branch-environmentvariable.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Framework`  <a name="cfn-amplify-branch-framework"></a>
 The framework for the branch.
*Required*: No
*Type*: String
*Pattern*: `(?s).*`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PullRequestEnvironmentName`  <a name="cfn-amplify-branch-pullrequestenvironmentname"></a>
If pull request previews are enabled for this branch, you can use this property to specify a dedicated backend environment for your previews. For example, you could specify an environment named `prod`, `test`, or `dev` that you initialized with the Amplify CLI and mapped to this branch.
To enable pull request previews, set the `EnablePullRequestPreview` property to `true`.
If you don't specify an environment, Amplify Hosting provides backend support for each preview by automatically provisioning a temporary backend environment. Amplify Hosting deletes this environment when the pull request is closed.
For more information about creating backend environments, see [Feature Branch Deployments and Team Workflows](https://docs.aws.amazon.com/amplify/latest/userguide/multi-environments.html) in the *AWS Amplify Hosting User Guide*.
*Required*: No
*Type*: String
*Pattern*: `(?s).*`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Stage`  <a name="cfn-amplify-branch-stage"></a>
Describes the current stage for the branch.
*Required*: No
*Type*: String
*Allowed values*: `EXPERIMENTAL | BETA | PULL_REQUEST | PRODUCTION | DEVELOPMENT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-amplify-branch-tags"></a>
 The tag for the branch.
*Required*: No
*Type*: Array of [Tag](aws-properties-amplify-branch-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-amplify-branch-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-amplify-branch-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-amplify-branch-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
 ARN for a branch, part of an Amplify App.

`BranchName`  <a name="BranchName-fn::getatt"></a>
 Name for a branch, part of an Amplify App.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
