---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/cli/cli-mon-cmd.html
---

# mon-cmd
<a name="cli-mon-cmd"></a>

## Description
<a name="w2aab9c11b3"></a>

Lists all the other CloudWatch commands. For help on a specific command, use the following command:

```
commandname --help
```

## Syntax
<a name="w2aab9c11b5"></a>

 ****mon-cmd****

## Output
<a name="w2aab9c11b7"></a>

This command lists all of the Amazon CloudWatch commands in a table.

The Amazon CloudWatch CLI displays errors on stderr.

## Examples
<a name="w2aab9c11b9"></a>

### Example Request
<a name="w2aab9c11b9b2"></a>

This example lists all of the Amazon CloudWatch commands.

```
mon-cmd

Command Name                       Description
------------                       -----------
help
mon-delete-alarms                  Delete alarms.
mon-describe-alarm-history         Show the history of alarm transitions and actions taken.
mon-describe-alarms                List alarms and show detailed alarm configuration.
mon-describe-alarms-for-metric     Show alarms for a given metric.
mon-disable-alarm-actions          Disable all actions for a given alarm.
mon-enable-alarm-actions           Enable all actions for a given alarm.
mon-get-stats                      Get metric statistics.
mon-list-metrics                   List user's metrics.
mon-put-data                       Put metric data.
mon-put-metric-alarm               Create a new alarm or update an existing one.
mon-set-alarm-state                Manually set the state of an alarm.
mon-version                        Prints the version of the CLI tool and API.

For help on a specific command, type '<commandname> --help'
```

## Related Topics
<a name="w2aab9c11c11"></a>

### Download
<a name="w2aab9c11c11b2"></a>
+ [Set up the command line interface](SetupCLI.md)

### Related Command
<a name="w2aab9c11c11b4"></a>
+  [mon-version](cli-mon-version.md)
