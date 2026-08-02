---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloudformation_example_cloudformation_ContinueUpdateRollback_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ContinueUpdateRollback` with a CLI
<a name="cloudformation_example_cloudformation_ContinueUpdateRollback_section"></a>

The following code examples show how to use `ContinueUpdateRollback`.

------
#### [ CLI ]

**AWS CLI**
**To retry an update rollback**
The following `continue-update-rollback` example resumes a rollback operation from a previously failed stack update.

```
aws cloudformation continue-update-rollback \
    --stack-name {{my-stack}}
```
This command produces no output.
+  For API details, see [ContinueUpdateRollback](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/continue-update-rollback.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Continues rollback of the named stack, which should be in the state 'UPDATE\_ROLLBACK\_FAILED'. If the continued rollback is successful, the stack will enter state 'UPDATE\_ROLLBACK\_COMPLETE'.**

```
Resume-CFNUpdateRollback -StackName "myStack"
```
+  For API details, see [ContinueUpdateRollback](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Continues rollback of the named stack, which should be in the state 'UPDATE\_ROLLBACK\_FAILED'. If the continued rollback is successful, the stack will enter state 'UPDATE\_ROLLBACK\_COMPLETE'.**

```
Resume-CFNUpdateRollback -StackName "myStack"
```
+  For API details, see [ContinueUpdateRollback](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
