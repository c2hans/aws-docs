---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/powershell/v5/userguide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# Migrating from AWS Tools for PowerShell version 4 to version 5
<a name="migrating-v5"></a>

AWS Tools for PowerShell version 5 (V5) has breaking changes, which could cause your existing scripts to stop working. This topic describes the breaking changes in V5 and possible work that you might need to do to migrate your environment or code from V4.

For additional information about noteworthy changes in the AWS Tools for PowerShell also see the following resources:
+ The blog post [AWS Tools for PowerShell V5 now Generally Available](https://aws.amazon.com/blogs/developer/aws-tools-for-powershell-v5-now-generally-available/).
+ The [V5 Development Tracker issue in GitHub](https://github.com/aws/aws-tools-for-powershell/issues/357). In addition to the list of breaking changes, be sure to look at the details of each preview.
+ The blog post [Preview 1 of AWS Tools for PowerShell V5](https://aws.amazon.com/blogs/developer/preview-1-of-aws-tools-for-powershell-v5/)

**Note**
Since the AWS Tools for PowerShell rely on the AWS SDK for .NET, some of the changes related to V4 of the SDK might also affect V5 of the Tools for PowerShell. To see what has changed for V4 of the AWS SDK for .NET, see the [migration information](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html) in the [AWS SDK for .NET Developer Guide](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/).

## Minimum PowerShell version
<a name="migrating-v5-min-ps-ver"></a>

For the legacy, Windows-specific, single, large-module version of the AWS Tools for PowerShell, called *AWSPowerShell*, the module's minimum supported PowerShell version has been updated to 5.1. This is to match the AWS SDK for .NET new minimum version of .NET Framework 4.7.2.

For more information about the legacy AWSPowerShell module, see [Installing on Windows](pstools-getting-set-up-windows.md).

## Install or update `AWS.Tools` V4
<a name="migrating-v5-install-v4"></a>

When installing or updating the modularized version of the AWS Tools for PowerShell, called `AWS.Tools`, the `Install-AWSToolsModule` and `Update-AWSToolsModule` cmdlets will naturally use version 5 of `AWS.Tools` by default. If for some reason you need to install or update version 4 of `AWS.Tools` instead, you can do so by using the following commands, respectively:

```
Install-AWSToolsModule -MaximumVersion '4.9.999'
Update-AWSToolsModule -MaximumVersion '4.9.999'
```

For additional information about installing and updating the Tools for PowerShell, see [Get started](pstools-getting-set-up.md)

## Cancel cmdlet execution with CTRL\+C
<a name="migrating-v5-ctrl-c"></a>

Version 5 of the AWS Tools for PowerShell allows you to cancel cmdlet execution by using a keyboard shortcut such as CTRL\+C.

## Nullable value types
<a name="migrating-v5-value-types"></a>

The types adopted from the AWS SDK for .NET have been updated to use the SDK's new nullable changes. For example, properties of type `int` have been changed to `Nullable[int]`. This change doesn't affect how input parameter values are specified for AWS cmdlets because those value type parameters were already modeled as nullable. However, nullable types for cmdlet output is a breaking change because properties within the cmdlet output will contain `$null` instead of the various default values for types.

The following example demonstrates the behavior in V4 of the Tools for PowerShell. In this example, the `MissingMeta` property is set to 0 because that is the default value of type `int`.

```
# In V4
PS > Get-S3ObjectMetadata -BucketName {{amzn-s3-demo-bucket}}  -Key '{{test}}' |
>> Select LastModified, MissingMeta, ObjectLockRetainUntilDate, BucketKeyEnabled

LastModified          MissingMeta ObjectLockRetainUntilDate BucketKeyEnabled
------------          ----------- ------------------------- ----------------
8/29/2023 10:20:44 PM           0 1/1/0001 12:00:00 AM
```

The following example demonstrates the behavior in V5 of the Tools for PowerShell. In this example, the `MissingMeta` property is set to `$null`.

```
# In V5
PS > Get-S3ObjectMetadata -BucketName {{amzn-s3-demo-bucket}} -Key '{{test}}' |
>> Select LastModified, MissingMeta, ObjectLockRetainUntilDate, BucketKeyEnabled

LastModified          MissingMeta ObjectLockRetainUntilDate BucketKeyEnabled
------------          ----------- ------------------------- ----------------
8/29/2023 10:20:44 PM
```

In most cases, no code change is necessary because PowerShell has implicit conversion from nullable value types to non-nullable value types. However, this is a breaking change for comparison-logic code that checks explicitly for a default value of a nullable value type. Comparison logic that checks for the default value of a non-nullable type must be modified to check for `$null`.

For some of these types, the following examples show how to update code written for V4 that checks if nothing was returned:

```
#Type int:
# In V4, if you were checking whether an int is 0...
if($s3Metadata.MissingMeta -eq 0){}

# In V5, check if the int is null instead:
if($s3Metadata.MissingMeta -eq $null) {}

# Type datetime:
# In V4, if you were checking whether a datetime is '0001-01-01'...
if($s3Metadata.ObjectLockRetainUntilDate -eq '0001-01-01'){}

# In V5, check if the datetime is null instead:
if($s3Metadata.ObjectLockRetainUntilDate -eq $null){}

# Type boolean:
# In V4, if you were checking whether a boolean is $false...
if($s3Metadata.BucketKeyEnabled -eq $false){}

# In V5, check if the boolean is null instead:
if($s3Metadata.BucketKeyEnabled -eq $null)
```

Since the AWS Tools for PowerShell rely on the AWS SDK for .NET, it might be useful to examine how similar changes affected version 4 of the SDK. To find this information, see the [Value types](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html#net-dg-v4-value-types) migration content in the [AWS SDK for .NET Developer Guide](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/).

## Collections
<a name="migrating-v5-collections"></a>

Some cmdlet output has been changed to return `$null` instead of empty collections of type `List` or `Dictionary`. For additional information, including how to revert to legacy behavior, see the migration content for [Collections](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html#net-dg-v4-collections) in the [AWS SDK for .NET Developer Guide](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/).

## DateTime versus UTC DateTime
<a name="migrating-v5-utc-datetime"></a>

Some V4 cmdlets define DateTime parameters that are obsolete, as well as alternative UTC DateTime parameters. These obsolete DateTime parameters have been removed from the V5 cmdlets, and the name of the UTC DateTime parameters have been changed to the original name of the non-UTC DateTime parameters.

The following are some examples of cmdlets for which this change has been implemented.
+ `Get-ASScheduledAction` ([V4 cmdlet](https://docs.aws.amazon.com/powershell/v4/reference/items/Get-ASScheduledAction.html) and [V5 cmdlet](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-ASScheduledAction.html)):
  + The `StartTime` parameter has been removed, and the name of the `UtcStartTime` parameter has been changed to "StartTime".
  + The `EndTime` parameter has been removed, and the name of the `UtcEndTime` parameter has been changed to "EndTime".
+ `Copy-S3Object` ([V4 cmdlet](https://docs.aws.amazon.com/powershell/v4/reference/items/Copy-S3Object.html) and [V5 cmdlet](https://docs.aws.amazon.com/powershell/v5/reference/items/Copy-S3Object.html)):
  + The `ModifiedSinceDate` parameter has been removed, and the name of the `UtcModifiedSinceDate` parameter has been changed to "ModifiedSinceDate".
  + The `UnmodifiedSinceDate` parameter has been removed, and the name of the `UtcUnmodifiedSinceDate` parameter has been changed to "UnmodifiedSinceDate".

The following is a complete list of the cmdlets that are affected by this change.

### Open to view items
<a name="w2aac19b9c23c11b1"></a>
+ [Get-ASScheduledAction](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-ASScheduledAction.html)
+ [Write-ASScheduledUpdateGroupAction](https://docs.aws.amazon.com/powershell/v5/reference/items/Write-ASScheduledUpdateGroupAction.html)
+ [Get-CWAlarmHistory](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-CWAlarmHistory.html)
+ [Get-CWMetricData](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-CWMetricData.html)
+ [Get-CWMetricStatistic](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-CWMetricStatistic.html) (alias Get-CWMetricStatistics)
+ [New-EC2Fleet](https://docs.aws.amazon.com/powershell/v5/reference/items/New-EC2Fleet.html)
+ [Get-EC2FleetHistory](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-EC2FleetHistory.html)
+ [Get-EC2ScheduledInstance](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-EC2ScheduledInstance.html)
+ [Get-EC2ScheduledInstanceAvailability](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-EC2ScheduledInstanceAvailability.html)
+ [Get-EC2SpotFleetRequestHistory](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-EC2SpotFleetRequestHistory.html)
+ [Get-EC2SpotPriceHistory](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-EC2SpotPriceHistory.html)
+ [Import-EC2Image](https://docs.aws.amazon.com/powershell/v5/reference/items/Import-EC2Image.html)
+ [Import-EC2Snapshot](https://docs.aws.amazon.com/powershell/v5/reference/items/Import-EC2Snapshot.html)
+ [Request-EC2SpotFleet](https://docs.aws.amazon.com/powershell/v5/reference/items/Request-EC2SpotFleet.html)
+ [Request-EC2SpotInstance](https://docs.aws.amazon.com/powershell/v5/reference/items/Request-EC2SpotInstance.html)
+ [Send-EC2InstanceStatus](https://docs.aws.amazon.com/powershell/v5/reference/items/Send-EC2InstanceStatus.html)
+ [Get-ECEvent](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-ECEvent.html)
+ [Get-EBEnvironment](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-EBEnvironment.html)
+ [Get-EBEvent](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-EBEvent.html)
+ [Get-IOTTaskList](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-IOTTaskList.html)
+ [Get-IOTViolationEventList](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-IOTViolationEventList.html)
+ [Get-RDSEvent](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-RDSEvent.html)
+ [Reset-RDSDBCluster](https://docs.aws.amazon.com/powershell/v5/reference/items/Reset-RDSDBCluster.html)
+ [Restore-RDSDBClusterToPointInTime](https://docs.aws.amazon.com/powershell/v5/reference/items/Restore-RDSDBClusterToPointInTime.html)
+ [Restore-RDSDBInstanceToPointInTime](https://docs.aws.amazon.com/powershell/v5/reference/items/Restore-RDSDBInstanceToPointInTime.html)
+ [Get-RSClusterSnapshot](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-RSClusterSnapshot.html) (alias Get-RSClusterSnapshots)
+ [Get-RSEvent](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-RSEvent.html) (alias Get-RSEvents)
+ [Copy-S3Object](https://docs.aws.amazon.com/powershell/v5/reference/items/Copy-S3Object.html)
+ [Read-S3Object](https://docs.aws.amazon.com/powershell/v5/reference/items/Read-S3Object.html)
+ [Get-S3ObjectMetadata](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-S3ObjectMetadata.html)
+ [Send-SESBounce](https://docs.aws.amazon.com/powershell/v5/reference/items/Send-SESBounce.html)
+ [Get-WDActivity](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-WDActivity.html)

## Pipelining and `$AWSHistory`
<a name="migrating-v5-awshistory"></a>

In versions of the AWS Tools for PowerShell prior to V4, a session variable called `$AWSHistory` was introduced that maintains a record of AWS cmdlet invocations and the service responses that were received for each invocation.

In V4 of the Tools for PowerShell, this session variable was deprecated in favor of the `-Select *` parameter and argument, which can be used to return the entire service response. The `-Select *` parameter is described in [Pipelining, output, and iteration](pstools-pipelines.md).

In V5 of the Tools for PowerShell, the `$AWSHistory` session variable has been removed completely. As a consequence, the `Clear-AWSHistory` and `Set-AWSHistoryConfiguration` cmdlets have also been removed.

## The `-PassThru` parameter
<a name="migrating-v5-passthru"></a>

The `-PassThru` parameter has been removed. When a cmdlet doesn't return any output by default, users can request a returned parameter value by using `-Select ^ParameterName`. For additional details and examples, see the blog post [Preview 1 of AWS Tools for PowerShell V5](https://aws.amazon.com/blogs/developer/preview-1-of-aws-tools-for-powershell-v5/).

## Some DynamoDB cmdlets moved and renamed
<a name="migrating-v5-DynamoDB-cmdlets"></a>

The `Get-DDBStream` and `Get-DDBStreamList` cmdlets have been moved from the DynamoDBV2 module to a new module called DynamoDBStreams. They have also been renamed to [Get-DDBSStream](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-DDBSStream.html) and [Get-DDBSStreamList](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-DDBSStreamList.html), respectively.

## Logging of sensitive information
<a name="migrating-v5-logging"></a>

Logging behavior has been changed so that potentially sensitive information is less likely to be included in cmdlet output, especially in CI/CD situations. For more information and instructions about how to revert to V4 behavior, see [Logging of sensitive information](additional-security-considerations.md#add-sec-cons-sensitive-logs).

## Credential and profile resolution
<a name="migrating-v5-profile-cred-res"></a>

The AWS Tools for PowerShell have been updated to use certain environment variables when resolving credentials for a cmdlet: `AWS_PROFILE`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN`. In addition, there have been some changes in the resolution order for credentials and profiles. For more information, see [Credential and profile resolution](creds-assign.md).

## Credential error message
<a name="migrating-v5-creds-error-msg"></a>

The error message that the AWS Tools for PowerShell returns if it can't obtain appropriate credentials has changed.

In v4 of the tools, the message was similar to the following:

```
Get-SFNExecutionList -Region us-west-2
Get-SFNExecutionList: No credentials specified or obtained from persisted/shell defaults.
```

In V5 of the tools, the message is similar to the following instead:

```
Get-SFNExecutionList -Region us-west-2
Get-SFNExecutionList: Failed to resolve AWS credentials. The credential providers used to search for credentials returned the following errors:
... <list of specific exceptions>
```

## Consistent auto-iteration
<a name="migrating-v5-auto-iter"></a>

All paginated cmdlets have been updated to auto-iterate all data by default. You can revert this behavior by using the [Set-AWSAutoIterationMode](https://docs.aws.amazon.com/powershell/v5/reference/items/Set-AWSAutoIterationMode.html) cmdlet. If you run `Set-AWSAutoIterationMode -IterationMode v4`, operations that auto-iterated in v4 will still auto-iterate, but the rest will revert to manual iteration. To determine what mode auto-iteration is set to, use the [Get-AWSAutoIterationMode](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-AWSAutoIterationMode.html) cmdlet.

To see an example of a cmdlet that has been updated in this way, see the `Get-CWLLogEvent` cmdlet ([V4 cmdlet](https://docs.aws.amazon.com/powershell/v4/reference/index.html?page=Get-CWLLogEvent.html&tocid=Get-CWLLogEvent) and [V5 cmdlet](https://docs.aws.amazon.com/powershell/v5/reference/index.html?page=Get-CWLLogEvent.html&tocid=Get-CWLLogEvent)).

For details about auto-iteration, see [Iteration through paged data](pstools-pipelines.md#pstools-iteration).

## S3 cmdlets deprecated and replaced
<a name="migrating-v5-s3-cmdlets"></a>

For Amazon S3, the [Get-S3ACL](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-S3ACL.html) and [Set-S3ACL](https://docs.aws.amazon.com/powershell/v5/reference/items/Set-S3ACL.html) cmdlets have been deprecated. Use the following new cmdlets instead: [Get-S3BucketACL](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-S3BucketACL.html), [Set-S3BucketACL](https://docs.aws.amazon.com/powershell/v5/reference/items/Set-S3BucketACL.html), [Get-S3ObjectACL](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-S3ObjectACL.html), [Set-S3ObjectACL](https://docs.aws.amazon.com/powershell/v5/reference/items/Set-S3ObjectACL.html).

## Cleaning and trimming S3 key parameters
<a name="migrating-v5-s3-param-trim"></a>

Certain Amazon S3 cmdlets accept parameters named `Key` and `KeyPrefix`. V4 of the AWS Tools for PowerShell would clean and trim these parameters in the following ways: remove leading spaces, forward slashes ("/"), and backslashes ("\\"), convert all other backslashes to forward slashes, and remove trailing spaces. In V5 of the Tools for PowerShell, this is no longer the default behavior. You can revert to this behavior by specifying the `-EnableLegacyKeyCleaning` parameter.

This information applies to the following cmdlets:
+ [Copy-S3Object](https://docs.aws.amazon.com/powershell/v5/reference/items/Copy-S3Object.html)
+ [Get-S3Object](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-S3Object.html)
+ [Get-S3ObjectV2](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-S3ObjectV2.html)
+ [Read-S3Object](https://docs.aws.amazon.com/powershell/v5/reference/items/Read-S3Object.html)
+ [Remove-S3Object](https://docs.aws.amazon.com/powershell/v5/reference/items/Remove-S3Object.html)
+ [Set-S3ACL](https://docs.aws.amazon.com/powershell/v5/reference/items/Set-S3ACL.html)
+ [Write-S3Object](https://docs.aws.amazon.com/powershell/v5/reference/items/Write-S3Object.html)

## Interactive session capabilities
<a name="migrating-v5-interactive-session"></a>

Interactive session capabilities have been added to the [Start-SSMSession](https://docs.aws.amazon.com/powershell/v5/reference/items/Start-SSMSession.html) cmdlet, which aligns with the AWS CLI behavior. For example:

```
Start-SSMSession -Target 'i-1234567890abcdef0'
```

If you need legacy behavior, include the `-DisablePluginInvocation` parameter in the `Start-SSMSession` command.

## CloudWatch alarms
<a name="migrating-v5-Get-CWAlarm"></a>

The [Get-CWAlarm](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-CWAlarm.html) cmdlet has been updated to return both metric and composite Amazon CloudWatch alarms by default. To limit the output to either metric or composite alarms, you must specify the `-AlarmType` parameter: `Get-CWAlarm -AlarmType 'MetricAlarms'` or `Get-CWAlarm -AlarmType 'CompositeAlarms'`, respectively.

## `LitJson`
<a name="migrating-v5-LitJson"></a>

The AWS Tools for PowerShell have been updated to use `System.Text.Json` instead of `LitJson` for serialization. `LitJson` has been removed from V5 of the tools.

## The `LoggedAt` output property
<a name="migrating-v5-loggedat"></a>

The `LoggedAt` output property has been removed. In V4 of the tools, this property was returned by default on some cmdlets (for example `Get-SSMCommandInvocationDetail` and `Invoke-LMFunction`).

If you need to replicate the information that was provided by the `LoggedAt` output property, you can include something similar to the following in your scripts:

```
$loggedAt = (Get-Date).ToUniversalTime().ToString('s')
```

## Programming elements that were removed
<a name="migrating-v5-removed"></a>

A number of programming elements have been removed from V5 of the Tools for PowerShell. These are listed below, if not already covered previously, along with potential steps that you can take to accommodate their removal, if any.
+ The `Invoke-LMFunctionAsync` cmdlet.
+ The `Get-EC2ImageByName` cmdlet. Use the [Get-SSMLatestEC2Image](https://docs.aws.amazon.com/powershell/v5/reference/items/Get-SSMLatestEC2Image.html) cmdlet instead.
+ The `CalculateContentMD5Header` parameter from the [Write-S3Object](https://docs.aws.amazon.com/powershell/v5/reference/items/Write-S3Object.html) cmdlet.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Tools for PowerShell. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query powershell` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
