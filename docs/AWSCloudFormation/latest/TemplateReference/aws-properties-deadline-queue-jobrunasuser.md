---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-queue-jobrunasuser.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Queue JobRunAsUser
<a name="aws-properties-deadline-queue-jobrunasuser"></a>

Identifies the user for a job.

## Syntax
<a name="aws-properties-deadline-queue-jobrunasuser-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-queue-jobrunasuser-syntax.json"></a>

```
{
  "[Posix](#cfn-deadline-queue-jobrunasuser-posix)" : {{PosixUser}},
  "[RunAs](#cfn-deadline-queue-jobrunasuser-runas)" : {{String}},
  "[Windows](#cfn-deadline-queue-jobrunasuser-windows)" : {{WindowsUser}}
}
```

### YAML
<a name="aws-properties-deadline-queue-jobrunasuser-syntax.yaml"></a>

```
  [Posix](#cfn-deadline-queue-jobrunasuser-posix): {{
    PosixUser}}
  [RunAs](#cfn-deadline-queue-jobrunasuser-runas): {{String}}
  [Windows](#cfn-deadline-queue-jobrunasuser-windows): {{
    WindowsUser}}
```

## Properties
<a name="aws-properties-deadline-queue-jobrunasuser-properties"></a>

`Posix`  <a name="cfn-deadline-queue-jobrunasuser-posix"></a>
The user and group that the jobs in the queue run as.
*Required*: No
*Type*: [PosixUser](aws-properties-deadline-queue-posixuser.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RunAs`  <a name="cfn-deadline-queue-jobrunasuser-runas"></a>
Specifies whether the job should run using the queue's system user or if the job should run using the worker agent system user.
*Required*: Yes
*Type*: String
*Allowed values*: `QUEUE_CONFIGURED_USER | WORKER_AGENT_USER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Windows`  <a name="cfn-deadline-queue-jobrunasuser-windows"></a>
Identifies a Microsoft Windows user.
*Required*: No
*Type*: [WindowsUser](aws-properties-deadline-queue-windowsuser.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
