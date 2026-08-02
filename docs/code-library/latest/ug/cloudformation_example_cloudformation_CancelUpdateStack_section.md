---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloudformation_example_cloudformation_CancelUpdateStack_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CancelUpdateStack` with a CLI
<a name="cloudformation_example_cloudformation_CancelUpdateStack_section"></a>

The following code examples show how to use `CancelUpdateStack`.

------
#### [ CLI ]

**AWS CLI**
**To cancel a stack update that is in progress**
The following `cancel-update-stack` command cancels a stack update on the `myteststack` stack:

```
aws cloudformation cancel-update-stack --stack-name {{myteststack}}
```
+  For API details, see [CancelUpdateStack](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/cancel-update-stack.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Cancels an update on the specified stack.**

```
Stop-CFNUpdateStack -StackName "myStack"
```
+  For API details, see [CancelUpdateStack](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Cancels an update on the specified stack.**

```
Stop-CFNUpdateStack -StackName "myStack"
```
+  For API details, see [CancelUpdateStack](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
