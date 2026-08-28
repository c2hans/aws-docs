---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-amplify-app.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Amplify::App
<a name="aws-resource-amplify-app"></a>

 The AWS::Amplify::App resource specifies Apps in Amplify Hosting. An App is a collection of branches.

## Syntax
<a name="aws-resource-amplify-app-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-amplify-app-syntax.json"></a>

```
{
  "Type" : "AWS::Amplify::App",
  "Properties" : {
      "[AccessToken](#cfn-amplify-app-accesstoken)" : {{String}},
      "[AutoBranchCreationConfig](#cfn-amplify-app-autobranchcreationconfig)" : {{AutoBranchCreationConfig}},
      "[BasicAuthConfig](#cfn-amplify-app-basicauthconfig)" : {{BasicAuthConfig}},
      "[BuildSpec](#cfn-amplify-app-buildspec)" : {{String}},
      "[CacheConfig](#cfn-amplify-app-cacheconfig)" : {{CacheConfig}},
      "[ComputeRoleArn](#cfn-amplify-app-computerolearn)" : {{String}},
      "[CustomHeaders](#cfn-amplify-app-customheaders)" : {{String}},
      "[CustomRules](#cfn-amplify-app-customrules)" : {{[ CustomRule, ... ]}},
      "[Description](#cfn-amplify-app-description)" : {{String}},
      "[EnableBranchAutoDeletion](#cfn-amplify-app-enablebranchautodeletion)" : {{Boolean}},
      "[EnvironmentVariables](#cfn-amplify-app-environmentvariables)" : {{[ EnvironmentVariable, ... ]}},
      "[IAMServiceRole](#cfn-amplify-app-iamservicerole)" : {{String}},
      "[JobConfig](#cfn-amplify-app-jobconfig)" : {{JobConfig}},
      "[Name](#cfn-amplify-app-name)" : {{String}},
      "[OauthToken](#cfn-amplify-app-oauthtoken)" : {{String}},
      "[Platform](#cfn-amplify-app-platform)" : {{String}},
      "[Repository](#cfn-amplify-app-repository)" : {{String}},
      "[Tags](#cfn-amplify-app-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-amplify-app-syntax.yaml"></a>

```
Type: AWS::Amplify::App
Properties:
  [AccessToken](#cfn-amplify-app-accesstoken): {{String}}
  [AutoBranchCreationConfig](#cfn-amplify-app-autobranchcreationconfig): {{
    AutoBranchCreationConfig}}
  [BasicAuthConfig](#cfn-amplify-app-basicauthconfig): {{
    BasicAuthConfig}}
  [BuildSpec](#cfn-amplify-app-buildspec): {{String}}
  [CacheConfig](#cfn-amplify-app-cacheconfig): {{
    CacheConfig}}
  [ComputeRoleArn](#cfn-amplify-app-computerolearn): {{String}}
  [CustomHeaders](#cfn-amplify-app-customheaders): {{String}}
  [CustomRules](#cfn-amplify-app-customrules): {{
    - CustomRule}}
  [Description](#cfn-amplify-app-description): {{String}}
  [EnableBranchAutoDeletion](#cfn-amplify-app-enablebranchautodeletion): {{Boolean}}
  [EnvironmentVariables](#cfn-amplify-app-environmentvariables): {{
    - EnvironmentVariable}}
  [IAMServiceRole](#cfn-amplify-app-iamservicerole): {{String}}
  [JobConfig](#cfn-amplify-app-jobconfig): {{
    JobConfig}}
  [Name](#cfn-amplify-app-name): {{String}}
  [OauthToken](#cfn-amplify-app-oauthtoken): {{String}}
  [Platform](#cfn-amplify-app-platform): {{String}}
  [Repository](#cfn-amplify-app-repository): {{String}}
  [Tags](#cfn-amplify-app-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-amplify-app-properties"></a>

`AccessToken`  <a name="cfn-amplify-app-accesstoken"></a>
The personal access token for a GitHub repository for an Amplify app. The personal access token is used to authorize access to a GitHub repository using the Amplify GitHub App. The token is not stored.
Use `AccessToken` for GitHub repositories only. To authorize access to a repository provider such as Bitbucket or CodeCommit, use `OauthToken`.
You must specify either `AccessToken` or `OauthToken` when you create a new app.
Existing Amplify apps deployed from a GitHub repository using OAuth continue to work with CI/CD. However, we strongly recommend that you migrate these apps to use the GitHub App. For more information, see [Migrating an existing OAuth app to the Amplify GitHub App](https://docs.aws.amazon.com/amplify/latest/userguide/setting-up-GitHub-access.html#migrating-to-github-app-auth) in the *Amplify User Guide* .
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AutoBranchCreationConfig`  <a name="cfn-amplify-app-autobranchcreationconfig"></a>
 Sets the configuration for your automatic branch creation.
*Required*: No
*Type*: [AutoBranchCreationConfig](aws-properties-amplify-app-autobranchcreationconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BasicAuthConfig`  <a name="cfn-amplify-app-basicauthconfig"></a>
The credentials for basic authorization for an Amplify app. You must base64-encode the authorization credentials and provide them in the format `user:password`.
*Required*: No
*Type*: [BasicAuthConfig](aws-properties-amplify-app-basicauthconfig.md)
*Pattern*: `(?s).*`
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BuildSpec`  <a name="cfn-amplify-app-buildspec"></a>
The build specification (build spec) for an Amplify app.
*Required*: No
*Type*: String
*Pattern*: `(?s).+`
*Minimum*: `1`
*Maximum*: `25000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CacheConfig`  <a name="cfn-amplify-app-cacheconfig"></a>
The cache configuration for the Amplify app. If you don't specify the cache configuration `type`, Amplify uses the default `AMPLIFY_MANAGED` setting.
*Required*: No
*Type*: [CacheConfig](aws-properties-amplify-app-cacheconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComputeRoleArn`  <a name="cfn-amplify-app-computerolearn"></a>
The Amazon Resource Name (ARN) of the IAM role for an SSR app. The Compute role allows the Amplify Hosting compute service to securely access specific AWS resources based on the role's permissions. For more information about the SSR Compute role, see [Adding an SSR Compute role](https://docs.aws.amazon.com/amplify/latest/userguide/amplify-SSR-compute-role.html) in the *Amplify User Guide*.
*Required*: No
*Type*: String
*Pattern*: `(?s).*`
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomHeaders`  <a name="cfn-amplify-app-customheaders"></a>
The custom HTTP headers for an Amplify app.
*Required*: No
*Type*: String
*Pattern*: `(?s).*`
*Minimum*: `0`
*Maximum*: `25000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomRules`  <a name="cfn-amplify-app-customrules"></a>
The custom rewrite and redirect rules for an Amplify app.
*Required*: No
*Type*: Array of [CustomRule](aws-properties-amplify-app-customrule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-amplify-app-description"></a>
The description of the Amplify app.
*Required*: No
*Type*: String
*Pattern*: `(?s).*`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableBranchAutoDeletion`  <a name="cfn-amplify-app-enablebranchautodeletion"></a>
Automatically disconnect a branch in Amplify Hosting when you delete a branch from your Git repository.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentVariables`  <a name="cfn-amplify-app-environmentvariables"></a>
The environment variables for the Amplify app.
For a list of the environment variables that are accessible to Amplify by default, see [Amplify Environment variables](https://docs.aws.amazon.com/amplify/latest/userguide/amplify-console-environment-variables.html) in the *Amplify Hosting User Guide*.
*Required*: No
*Type*: Array of [EnvironmentVariable](aws-properties-amplify-app-environmentvariable.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IAMServiceRole`  <a name="cfn-amplify-app-iamservicerole"></a>
AWS Identity and Access Management (IAM) service role for the Amazon Resource Name (ARN) of the Amplify app.
*Required*: No
*Type*: String
*Pattern*: `(?s).*`
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JobConfig`  <a name="cfn-amplify-app-jobconfig"></a>
The configuration details that apply to the jobs for an Amplify app.
*Required*: No
*Type*: [JobConfig](aws-properties-amplify-app-jobconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-amplify-app-name"></a>
The name of the Amplify app.
*Required*: Yes
*Type*: String
*Pattern*: `(?s).+`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OauthToken`  <a name="cfn-amplify-app-oauthtoken"></a>
The OAuth token for a third-party source control system for an Amplify app. The OAuth token is used to create a webhook and a read-only deploy key using SSH cloning. The OAuth token is not stored.
Use `OauthToken` for repository providers other than GitHub, such as Bitbucket or CodeCommit. To authorize access to GitHub as your repository provider, use `AccessToken`.
You must specify either `OauthToken` or `AccessToken` when you create a new app.
Existing Amplify apps deployed from a GitHub repository using OAuth continue to work with CI/CD. However, we strongly recommend that you migrate these apps to use the GitHub App. For more information, see [Migrating an existing OAuth app to the Amplify GitHub App](https://docs.aws.amazon.com/amplify/latest/userguide/setting-up-GitHub-access.html#migrating-to-github-app-auth) in the *Amplify User Guide* .
*Required*: No
*Type*: String
*Pattern*: `(?s).*`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Platform`  <a name="cfn-amplify-app-platform"></a>
The platform for the Amplify app. For a static app, set the platform type to `WEB`. For a dynamic server-side rendered (SSR) app, set the platform type to `WEB_COMPUTE`. For an app requiring Amplify Hosting's original SSR support only, set the platform type to `WEB_DYNAMIC`.
If you are deploying an SSG only app with Next.js version 14 or later, you must set the platform type to `WEB_COMPUTE` and set the artifacts `baseDirectory` to `.next` in the application's build settings. For an example of the build specification settings, see [Amplify build settings for a Next.js 14 SSG application](https://docs.aws.amazon.com/amplify/latest/userguide/deploy-nextjs-app.html#build-setting-detection-ssg-14) in the *Amplify Hosting User Guide*.
*Required*: No
*Type*: String
*Allowed values*: `WEB | WEB_DYNAMIC | WEB_COMPUTE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Repository`  <a name="cfn-amplify-app-repository"></a>
The Git repository for the Amplify app.
*Required*: No
*Type*: String
*Pattern*: `(?s).*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-amplify-app-tags"></a>
The tag for an Amplify app.
*Required*: No
*Type*: Array of [Tag](aws-properties-amplify-app-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-amplify-app-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-amplify-app-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-amplify-app-return-values-fn--getatt-fn--getatt"></a>

`AppId`  <a name="AppId-fn::getatt"></a>
Unique Id for the Amplify App.

`AppName`  <a name="AppName-fn::getatt"></a>
Name for the Amplify App.

`Arn`  <a name="Arn-fn::getatt"></a>
ARN for the Amplify App.

`DefaultDomain`  <a name="DefaultDomain-fn::getatt"></a>
Default domain for the Amplify App.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
