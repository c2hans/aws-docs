---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codepipeline_example_codepipeline_ListPipelines_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListPipelines` with a CLI
<a name="codepipeline_example_codepipeline_ListPipelines_section"></a>

The following code examples show how to use `ListPipelines`.

------
#### [ CLI ]

**AWS CLI**
**To view a list of pipelines**
This example lists all AWS CodePipeline pipelines associated with the user's AWS account.
Command:

```
aws codepipeline list-pipelines
```
Output:

```
{
  "pipelines": [
      {
          "updated": 1439504274.641,
          "version": 1,
          "name": "MyFirstPipeline",
          "created": 1439504274.641
      },
      {
          "updated": 1436461837.992,
          "version": 2,
          "name": "MySecondPipeline",
          "created": 1436460801.381
      }
      ]
}
```
+  For API details, see [ListPipelines](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/list-pipelines.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example gets a list of available pipelines.**

```
Get-CPPipelineList
```
**Output:**

```
Created                  Name                Updated                  Version
-------                  ----                -------                  -------
8/13/2015 10:17:54 PM    CodePipelineDemo    8/13/2015 10:17:54 PM    3
7/8/2015 2:41:53 AM      MyFirstPipeline     7/22/2015 9:06:37 PM     7
```
+  For API details, see [ListPipelines](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example gets a list of available pipelines.**

```
Get-CPPipelineList
```
**Output:**

```
Created                  Name                Updated                  Version
-------                  ----                -------                  -------
8/13/2015 10:17:54 PM    CodePipelineDemo    8/13/2015 10:17:54 PM    3
7/8/2015 2:41:53 AM      MyFirstPipeline     7/22/2015 9:06:37 PM     7
```
+  For API details, see [ListPipelines](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
