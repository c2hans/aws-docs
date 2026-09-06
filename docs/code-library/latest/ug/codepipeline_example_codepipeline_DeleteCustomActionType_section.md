---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codepipeline_example_codepipeline_DeleteCustomActionType_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteCustomActionType` with a CLI
<a name="codepipeline_example_codepipeline_DeleteCustomActionType_section"></a>

The following code examples show how to use `DeleteCustomActionType`.

------
#### [ CLI ]

**AWS CLI**
**To delete a custom action**
This example deletes a custom action in AWS CodePipeline by using an already-created JSON file (here named DeleteMyCustomAction.json) that contains the action type, provider name, and version number of the action to be deleted. Use the list-action-types command to view the correct values for category, version, and provider.
Command:

```
aws codepipeline delete-custom-action-type --cli-input-json {{file://DeleteMyCustomAction.json}}
```
JSON file sample contents:

```
{
  "category": "Build",
  "version": "1",
  "provider": "MyJenkinsProviderName"
}
```
Output:

```
None.
```
+  For API details, see [DeleteCustomActionType](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/delete-custom-action-type.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example deletes the specified custom action. The command will prompt for confirmation before proceeding. Add the -Force parameter to delete the custom action without a prompt.**

```
Remove-CPCustomActionType -Category Build -Provider MyBuildProviderName -Version 1
```
+  For API details, see [DeleteCustomActionType](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example deletes the specified custom action. The command will prompt for confirmation before proceeding. Add the -Force parameter to delete the custom action without a prompt.**

```
Remove-CPCustomActionType -Category Build -Provider MyBuildProviderName -Version 1
```
+  For API details, see [DeleteCustomActionType](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
