---
source_url: https://docs.aws.amazon.com/codepipeline/latest/userguide/structure-configuration-examples.html
---

# Valid configuration parameters for each provider type
<a name="structure-configuration-examples"></a>

This section lists valid `configuration` parameters for each action provider.

Every action must have a valid action configuration, which depends on the provider type for that action. The following table lists the required action configuration elements for each valid provider type:

**Action configuration properties for provider types**

<table>
<thead>
  <tr><th>Name of provider</th><th>Provider name in action type</th><th>Configuration properties</th><th>Required/Optional</th></tr>
</thead>
<tbody>
  <tr><td>Amazon S3 (Deploy action provider)</td><td colspan="3">For more information, including examples related to Amazon S3 Deploy action parameters, see [Amazon S3 deploy action reference](action-reference-S3Deploy.md).</td></tr>
  <tr><td>Amazon S3 (Source action provider)</td><td colspan="3">For more information, including examples related to Amazon S3 source action parameters, see [Amazon S3 source action reference](action-reference-S3.md).</td></tr>
  <tr><td>Amazon ECR</td><td colspan="3">For more information, including examples related to Amazon ECR parameters, see [Amazon ECR source action reference](action-reference-ECR.md).</td></tr>
  <tr><td>CodeCommit</td><td colspan="3">For more information, including examples related to CodeCommit parameters, see [CodeCommit source action reference](action-reference-CodeCommit.md).</td></tr>
  <tr><td>CodeStarSourceConnection action for Bitbucket, GitHub (via GitHub app), GHES, and GitLab</td><td colspan="3">For more information, including examples of the action configuration, see [Configuration parameters](action-reference-CodestarConnectionSource.md#action-reference-CodestarConnectionSource-config).</td></tr>
  <tr><td>GitHub (via OAuth app)</td><td colspan="3">For more information, including examples related to GitHub parameters, see [GitHub (via OAuth app) source action reference](appendix-github-oauth.md#action-reference-GitHub). This is the Version 1 GitHub action.</td></tr>
  <tr><td>AWS CloudFormation</td><td colspan="3">For more information, including examples related to AWS CloudFormation parameters, see [CloudFormation deploy action reference](action-reference-CloudFormation.md).</td></tr>
  <tr><td>CodeBuild</td><td colspan="3">For more description and examples related to CodeBuild parameters, see [AWS CodeBuild build and test action reference](action-reference-CodeBuild.md).</td></tr>
  <tr><td>CodeDeploy</td><td colspan="3">For more description and examples related to CodeDeploy parameters, see [AWS CodeDeploy deploy action reference](action-reference-CodeDeploy.md).</td></tr>
  <tr><td>AWS Device Farm</td><td colspan="3">For more description and examples related to AWS Device Farm parameters, see [AWS Device Farm test action reference](action-reference-DeviceFarm.md).</td></tr>
  <tr><td rowspan="2">AWS Elastic Beanstalk</td><td rowspan="2">ElasticBeanstalk</td><td>ApplicationName </td><td>Required</td></tr>
  <tr><td>EnvironmentName</td><td>Required</td></tr>
  <tr><td>AWS Lambda</td><td colspan="3">For more information, including examples related to AWS Lambda parameters, see [AWS Lambda invoke action reference](action-reference-Lambda.md).</td></tr>
  <tr><td rowspan="3">AWS OpsWorks Stacks</td><td rowspan="3">OpsWorks</td><td>Stack </td><td>Required</td></tr>
  <tr><td>Layer</td><td>Optional</td></tr>
  <tr><td>App</td><td>Required</td></tr>
  <tr><td>Amazon ECS</td><td colspan="3">For more description and examples related to Amazon ECS parameters, see [Amazon Elastic Container Service deploy action reference](action-reference-ECS.md).</td></tr>
  <tr><td>Amazon ECS and CodeDeploy(Blue/Green)</td><td colspan="3">For more description and examples related to Amazon ECS and CodeDeploy blue/green parameters, see [Amazon Elastic Container Service and CodeDeploy blue-green deploy action reference](action-reference-ECSbluegreen.md).</td></tr>
  <tr><td rowspan="5">Service Catalog</td><td rowspan="5">ServiceCatalog</td><td>TemplateFilePath</td><td>Required</td></tr>
  <tr><td>ProductVersionName</td><td>Required</td></tr>
  <tr><td>ProductType</td><td>Required</td></tr>
  <tr><td>ProductVersionDescription</td><td>Optional</td></tr>
  <tr><td>ProductId</td><td>Required</td></tr>
  <tr><td rowspan="4">Alexa Skills Kit</td><td rowspan="4">AlexaSkillsKit</td><td>ClientId</td><td>Required</td></tr>
  <tr><td>ClientSecret</td><td>Required</td></tr>
  <tr><td>RefreshToken</td><td>Required</td></tr>
  <tr><td>SkillId</td><td>Required</td></tr>
  <tr><td>Jenkins</td><td>The name of the action you provided in the CodePipeline Plugin for Jenkins (for example, {{MyJenkinsProviderName}})</td><td>ProjectName</td><td>Required</td></tr>
  <tr><td rowspan="3">Manual Approval</td><td rowspan="3">Manual</td><td>CustomData</td><td>Optional</td></tr>
  <tr><td>ExternalEntityLink</td><td>Optional</td></tr>
  <tr><td>NotificationArn</td><td>Optional</td></tr>
</tbody>
</table>

The following example shows a valid configuration for a deploy action that uses Alexa Skills Kit:

```
"configuration": {
  "ClientId": "amzn1.application-oa2-client.aadEXAMPLE",
  "ClientSecret": "****",
  "RefreshToken": "****",
  "SkillId": "amzn1.ask.skill.22649d8f-0451-4b4b-9ed9-bfb6cEXAMPLE"
}
```

The following example shows a valid configuration for a manual approval:

```
"configuration": {
  "CustomData": "Comments on the manual approval",
  "ExternalEntityLink": "http://my-url.com",
  "NotificationArn": "arn:aws:sns:us-west-2:12345EXAMPLE:Notification"
}
```
