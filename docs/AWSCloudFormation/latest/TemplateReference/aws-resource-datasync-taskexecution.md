---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datasync-taskexecution.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::TaskExecution
<a name="aws-resource-datasync-taskexecution"></a>

<a name="aws-resource-datasync-taskexecution-description"></a>The `AWS::DataSync::TaskExecution` resource Property description not available. for DataSync.

## Syntax
<a name="aws-resource-datasync-taskexecution-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-datasync-taskexecution-syntax.json"></a>

```
{
  "Type" : "AWS::DataSync::TaskExecution",
  "Properties" : {
      "[Tags](#cfn-datasync-taskexecution-tags)" : {{[ Tag, ... ]}},
      "[TaskArn](#cfn-datasync-taskexecution-taskarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-datasync-taskexecution-syntax.yaml"></a>

```
Type: AWS::DataSync::TaskExecution
Properties:
  [Tags](#cfn-datasync-taskexecution-tags): {{
    - Tag}}
  [TaskArn](#cfn-datasync-taskexecution-taskarn): {{String}}
```

## Properties
<a name="aws-resource-datasync-taskexecution-properties"></a>

`Tags`  <a name="cfn-datasync-taskexecution-tags"></a>
Specifies the tags that you want to apply to the Amazon Resource Name (ARN) representing the task execution.
*Tags* are key-value pairs that help you manage, filter, and search for your DataSync resources.
*Required*: No
*Type*: Array of [Tag](aws-properties-datasync-taskexecution-tag.md)
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TaskArn`  <a name="cfn-datasync-taskexecution-taskarn"></a>
Specifies the Amazon Resource Name (ARN) of the task that you want to start.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:task/task-[0-9a-f]{17}$`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-datasync-taskexecution-return-values"></a>

### Ref
<a name="aws-resource-datasync-taskexecution-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-datasync-taskexecution-return-values-fn--getatt"></a>

####
<a name="aws-resource-datasync-taskexecution-return-values-fn--getatt-fn--getatt"></a>

`BytesCompressed`  <a name="BytesCompressed-fn::getatt"></a>
The number of physical bytes that DataSync transfers over the network after compression (if compression is possible). This number is typically less than [BytesTransferred](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html#DataSync-DescribeTaskExecution-response-BytesTransferred) unless the data isn't compressible.

`BytesTransferred`  <a name="BytesTransferred-fn::getatt"></a>
The number of bytes that DataSync sends to the network before compression (if compression is possible). For the number of bytes transferred over the network, see [BytesCompressed](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html#DataSync-DescribeTaskExecution-response-BytesCompressed).

`BytesWritten`  <a name="BytesWritten-fn::getatt"></a>
The number of logical bytes that DataSync actually writes to the destination location.

`EstimatedBytesToTransfer`  <a name="EstimatedBytesToTransfer-fn::getatt"></a>
The number of logical bytes that DataSync expects to write to the destination location.

`EstimatedFilesToDelete`  <a name="EstimatedFilesToDelete-fn::getatt"></a>
The number of files, objects, and directories that DataSync expects to delete in your destination location. If you don't configure your task to [delete data in the destination that isn't in the source](https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html), the value is always `0`.
For [Enhanced mode tasks](https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html), this counter only includes files or objects. Directories are counted in [EstimatedFoldersToDelete](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html#DataSync-DescribeTaskExecution-response-EstimatedFoldersToDelete).

`EstimatedFilesToTransfer`  <a name="EstimatedFilesToTransfer-fn::getatt"></a>
The number of files, objects, and directories that DataSync expects to transfer over the network. This value is calculated while DataSync [prepares](https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses) the transfer.
How this gets calculated depends primarily on your task’s [transfer mode](https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-TransferMode) configuration:
+ If `TranserMode` is set to `CHANGED` - The calculation is based on comparing the content of the source and destination locations and determining the difference that needs to be transferred. The difference can include:
  + Anything that's added or modified at the source location.
  + Anything that's in both locations and modified at the destination after an initial transfer (unless [OverwriteMode](https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-OverwriteMode) is set to `NEVER`).
  + **(Basic task mode only)** The number of items that DataSync expects to delete (if [PreserveDeletedFiles](https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-PreserveDeletedFiles) is set to `REMOVE`).
+ If `TranserMode` is set to `ALL` - The calculation is based only on the items that DataSync finds at the source location.
For [Enhanced mode tasks](https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html), this counter only includes files or objects. Directories are counted in [EstimatedFoldersToTransfer](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html#DataSync-DescribeTaskExecution-response-EstimatedFoldersToTransfer).

`FilesDeleted`  <a name="FilesDeleted-fn::getatt"></a>
The number of files, objects, and directories that DataSync actually deletes in your destination location. If you don't configure your task to [delete data in the destination that isn't in the source](https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html), the value is always `0`.
For [Enhanced mode tasks](https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html), this counter only includes files or objects. Directories are counted in [FoldersDeleted](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html#DataSync-DescribeTaskExecution-response-FoldersDeleted).

`FilesPrepared`  <a name="FilesPrepared-fn::getatt"></a>
The number of files or objects that DataSync will attempt to transfer after comparing your source and destination locations.
Applies only to [Enhanced mode tasks](https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html).
This counter isn't applicable if you configure your task to [transfer all data](https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html#task-option-transfer-mode). In that scenario, DataSync copies everything from the source to the destination without comparing differences between the locations.

`FilesSkipped`  <a name="FilesSkipped-fn::getatt"></a>
The number of files, objects, and directories that DataSync skips during your transfer.
For [Enhanced mode tasks](https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html), this counter only includes files or objects. Directories are counted in [FoldersSkipped](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html#DataSync-DescribeTaskExecution-response-FoldersSkipped).

`FilesTransferred`  <a name="FilesTransferred-fn::getatt"></a>
The number of files, objects, and directories that DataSync actually transfers over the network. This value is updated periodically during your task execution when something is read from the source and sent over the network.
If DataSync fails to transfer something, this value can be less than `EstimatedFilesToTransfer`. In some cases, this value can also be greater than `EstimatedFilesToTransfer`. This element is implementation-specific for some location types, so don't use it as an exact indication of what's transferring or to monitor your task execution.
For [Enhanced mode tasks](https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html), this counter only includes files or objects. Directories are counted in [FoldersTransferred](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html#DataSync-DescribeTaskExecution-response-FoldersTransferred).

`FilesVerified`  <a name="FilesVerified-fn::getatt"></a>
The number of files, objects, and directories that DataSync verifies during your transfer.
When you configure your task to [verify only the data that's transferred](https://docs.aws.amazon.com/datasync/latest/userguide/configure-data-verification-options.html), DataSync doesn't verify directories in some situations or files that fail to transfer.
For [Enhanced mode tasks](https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html), this counter only includes files or objects. Directories are counted in [FoldersVerified](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html#DataSync-DescribeTaskExecution-response-FoldersVerified).

`StartTime`  <a name="StartTime-fn::getatt"></a>
The time that DataSync sends the request to start the task execution. For non-queued tasks, `LaunchTime` and `StartTime` are typically the same. For queued tasks, `LaunchTime` is typically later than `StartTime` because previously queued tasks must finish running before newer tasks can begin.

`Status`  <a name="Status-fn::getatt"></a>
The status of the task execution.
For detailed information about task execution statuses, see [Task execution statuses](https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses).

`TaskExecutionArn`  <a name="TaskExecutionArn-fn::getatt"></a>
The ARN of the task execution that you wanted information about. `TaskExecutionArn` is hierarchical and includes `TaskArn` for the task that was executed.
For example, a `TaskExecution` value with the ARN `arn:aws:datasync:us-east-1:111222333444:task/task-0208075f79cedf4a2/execution/exec-08ef1e88ec491019b` executed the task with the ARN `arn:aws:datasync:us-east-1:111222333444:task/task-0208075f79cedf4a2`.

`TaskMode`  <a name="TaskMode-fn::getatt"></a>
The task mode that you're using. For more information, see [Choosing a task mode for your data transfer](https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html).
