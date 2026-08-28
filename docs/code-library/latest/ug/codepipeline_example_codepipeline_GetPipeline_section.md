---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codepipeline_example_codepipeline_GetPipeline_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetPipeline` with a CLI
<a name="codepipeline_example_codepipeline_GetPipeline_section"></a>

The following code examples show how to use `GetPipeline`.

------
#### [ CLI ]

**AWS CLI**
**To view the structure of a pipeline**
This example returns the structure of a pipeline named MyFirstPipeline.
Command:

```
aws codepipeline get-pipeline --name {{MyFirstPipeline}}
```
Output:

```
{
  "pipeline": {
      "roleArn": "arn:aws:iam::111111111111:role/AWS-CodePipeline-Service",
      "stages": [
          {
              "name": "Source",
              "actions": [
                  {
                      "inputArtifacts": [],
                      "name": "Source",
                      "actionTypeId": {
                          "category": "Source",
                          "owner": "AWS",
                          "version": "1",
                          "provider": "S3"
                      },
                      "outputArtifacts": [
                          {
                              "name": "MyApp"
                          }
                      ],
                      "configuration": {
                          "S3Bucket": "awscodepipeline-demo-bucket",
                          "S3ObjectKey": "aws-codepipeline-s3-aws-codedeploy_linux.zip"
                      },
                      "runOrder": 1
                  }
              ]
          },
          {
              "name": "Beta",
              "actions": [
                  {
                      "inputArtifacts": [
                          {
                              "name": "MyApp"
                          }
                      ],
                      "name": "CodePipelineDemoFleet",
                      "actionTypeId": {
                          "category": "Deploy",
                          "owner": "AWS",
                          "version": "1",
                          "provider": "CodeDeploy"
                      },
                      "outputArtifacts": [],
                      "configuration": {
                          "ApplicationName": "CodePipelineDemoApplication",
                          "DeploymentGroupName": "CodePipelineDemoFleet"
                      },
                      "runOrder": 1
                  }
              ]
          }
      ],
      "artifactStore": {
          "type": "S3",
          "location": "codepipeline-us-east-1-11EXAMPLE11"
      },
      "name": "MyFirstPipeline",
      "version": 1
  }
}
```
+  For API details, see [GetPipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/get-pipeline.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example gets general information about the specified pipeline.**

```
Get-CPPipeline -Name CodePipelineDemo -Version 1
```
**Output:**

```
ArtifactStore : Amazon.CodePipeline.Model.ArtifactStore
Name          : CodePipelineDemo
RoleArn       : arn:aws:iam::80398EXAMPLE:role/CodePipelineServiceRole
Stages        : {Source, Build, Beta, TestStage}
Version       : 1
```
**Example 2: This example gets detailed information about the specified pipeline.**

```
$pipeline = Get-CPPipeline -Name CodePipelineDemo
Write-Output ("Name = " + $pipeline.Name)
Write-Output ("RoleArn = " + $pipeline.RoleArn)
Write-Output ("Version = " + $pipeline.Version)
Write-Output ("ArtifactStore:")
Write-Output ("  Location = " + $pipeline.ArtifactStore.Location)
Write-Output ("  Type = " + $pipeline.ArtifactStore.Type.Value)
Write-Output ("Stages:")
ForEach ($stage in $pipeline.Stages) {
  Write-Output ("  Name = " + $stage.Name)
  Write-Output ("    Actions:")
  ForEach ($action in $stage.Actions) {
    Write-Output ("      Name = " + $action.Name)
	Write-Output ("        Category = " + $action.ActionTypeId.Category)
	Write-Output ("        Owner = " + $action.ActionTypeId.Owner)
	Write-Output ("        Provider = " + $action.ActionTypeId.Provider)
	Write-Output ("        Version = " + $action.ActionTypeId.Version)
	Write-Output ("        Configuration:")
	ForEach ($key in $action.Configuration.Keys) {
	  $value = $action.Configuration.$key
	  Write-Output ("          " + $key + " = " + $value)
	}
	Write-Output ("        InputArtifacts:")
	ForEach ($ia in $action.InputArtifacts) {
	  Write-Output ("          " + $ia.Name)
	}
	ForEach ($oa in $action.OutputArtifacts) {
	  Write-Output ("          " + $oa.Name)
	}
	Write-Output ("        RunOrder = " + $action.RunOrder)
  }
}
```
**Output:**

```
Name = CodePipelineDemo
RoleArn = arn:aws:iam::80398EXAMPLE:role/CodePipelineServiceRole
Version = 3
ArtifactStore:
  Location = amzn-s3-demo-bucket
  Type = S3
Stages:
  Name = Source
    Actions:
      Name = Source
        Category = Source
        Owner = ThirdParty
        Provider = GitHub
        Version = 1
        Configuration:
          Branch = master
          OAuthToken = ****
          Owner = my-user-name
          Repo = MyRepoName
        InputArtifacts:
          MyApp
        RunOrder = 1
  Name = Build
    Actions:
      Name = Build
        Category = Build
        Owner = Custom
        Provider = MyCustomProviderName
        Version = 1
        Configuration:
          ProjectName = MyProjectName
        InputArtifacts:
          MyApp
          MyAppBuild
        RunOrder = 1
  Name = Beta
    Actions:
      Name = CodePipelineDemoFleet
        Category = Deploy
        Owner = AWS
        Provider = CodeDeploy
        Version = 1
        Configuration:
          ApplicationName = CodePipelineDemoApplication
          DeploymentGroupName = CodePipelineDemoFleet
        InputArtifacts:
          MyAppBuild
        RunOrder = 1
  Name = TestStage
    Actions:
      Name = MyJenkinsTestAction
        Category = Test
        Owner = Custom
        Provider = MyCustomTestProvider
        Version = 1
        Configuration:
          ProjectName = MyJenkinsProjectName
        InputArtifacts:
          MyAppBuild
        RunOrder = 1
```
+  For API details, see [GetPipeline](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example gets general information about the specified pipeline.**

```
Get-CPPipeline -Name CodePipelineDemo -Version 1
```
**Output:**

```
ArtifactStore : Amazon.CodePipeline.Model.ArtifactStore
Name          : CodePipelineDemo
RoleArn       : arn:aws:iam::80398EXAMPLE:role/CodePipelineServiceRole
Stages        : {Source, Build, Beta, TestStage}
Version       : 1
```
**Example 2: This example gets detailed information about the specified pipeline.**

```
$pipeline = Get-CPPipeline -Name CodePipelineDemo
Write-Output ("Name = " + $pipeline.Name)
Write-Output ("RoleArn = " + $pipeline.RoleArn)
Write-Output ("Version = " + $pipeline.Version)
Write-Output ("ArtifactStore:")
Write-Output ("  Location = " + $pipeline.ArtifactStore.Location)
Write-Output ("  Type = " + $pipeline.ArtifactStore.Type.Value)
Write-Output ("Stages:")
ForEach ($stage in $pipeline.Stages) {
  Write-Output ("  Name = " + $stage.Name)
  Write-Output ("    Actions:")
  ForEach ($action in $stage.Actions) {
    Write-Output ("      Name = " + $action.Name)
	Write-Output ("        Category = " + $action.ActionTypeId.Category)
	Write-Output ("        Owner = " + $action.ActionTypeId.Owner)
	Write-Output ("        Provider = " + $action.ActionTypeId.Provider)
	Write-Output ("        Version = " + $action.ActionTypeId.Version)
	Write-Output ("        Configuration:")
	ForEach ($key in $action.Configuration.Keys) {
	  $value = $action.Configuration.$key
	  Write-Output ("          " + $key + " = " + $value)
	}
	Write-Output ("        InputArtifacts:")
	ForEach ($ia in $action.InputArtifacts) {
	  Write-Output ("          " + $ia.Name)
	}
	ForEach ($oa in $action.OutputArtifacts) {
	  Write-Output ("          " + $oa.Name)
	}
	Write-Output ("        RunOrder = " + $action.RunOrder)
  }
}
```
**Output:**

```
Name = CodePipelineDemo
RoleArn = arn:aws:iam::80398EXAMPLE:role/CodePipelineServiceRole
Version = 3
ArtifactStore:
  Location = amzn-s3-demo-bucket
  Type = S3
Stages:
  Name = Source
    Actions:
      Name = Source
        Category = Source
        Owner = ThirdParty
        Provider = GitHub
        Version = 1
        Configuration:
          Branch = master
          OAuthToken = ****
          Owner = my-user-name
          Repo = MyRepoName
        InputArtifacts:
          MyApp
        RunOrder = 1
  Name = Build
    Actions:
      Name = Build
        Category = Build
        Owner = Custom
        Provider = MyCustomProviderName
        Version = 1
        Configuration:
          ProjectName = MyProjectName
        InputArtifacts:
          MyApp
          MyAppBuild
        RunOrder = 1
  Name = Beta
    Actions:
      Name = CodePipelineDemoFleet
        Category = Deploy
        Owner = AWS
        Provider = CodeDeploy
        Version = 1
        Configuration:
          ApplicationName = CodePipelineDemoApplication
          DeploymentGroupName = CodePipelineDemoFleet
        InputArtifacts:
          MyAppBuild
        RunOrder = 1
  Name = TestStage
    Actions:
      Name = MyJenkinsTestAction
        Category = Test
        Owner = Custom
        Provider = MyCustomTestProvider
        Version = 1
        Configuration:
          ProjectName = MyJenkinsProjectName
        InputArtifacts:
          MyAppBuild
        RunOrder = 1
```
+  For API details, see [GetPipeline](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
