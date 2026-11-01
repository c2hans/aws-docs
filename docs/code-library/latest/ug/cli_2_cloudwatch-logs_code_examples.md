---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_cloudwatch-logs_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# CloudWatch Logs examples using AWS CLI
<a name="cli_2_cloudwatch-logs_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with CloudWatch Logs.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `create-log-group`
<a name="cloudwatch-logs_CreateLogGroup_cli_2_topic"></a>

The following code example shows how to use `create-log-group`.

**AWS CLI**
**To create a log group**
The following `create-log-group` example creates a log group named `my-logs`.

```
aws logs create-log-group \
    --log-group-name {{my-logs}}
```
This command produces no output.
For more information, see [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) in the *Amazon CloudWatch Logs User Guide*.
+  For API details, see [CreateLogGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/create-log-group.html) in *AWS CLI Command Reference*.

### `create-log-stream`
<a name="cloudwatch-logs_CreateLogStream_cli_2_topic"></a>

The following code example shows how to use `create-log-stream`.

**AWS CLI**
**To create a log stream**
The following `create-log-stream` example creates a log stream named `20150601` in the log group `my-logs`.

```
aws logs create-log-stream \
    --log-group-name {{my-logs}} \
    --log-stream-name {{20150601}}
```
This command produces no output.
For more information, see [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) in the *Amazon CloudWatch Logs User Guide*.
+  For API details, see [CreateLogStream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/create-log-stream.html) in *AWS CLI Command Reference*.

### `delete-log-group`
<a name="cloudwatch-logs_DeleteLogGroup_cli_2_topic"></a>

The following code example shows how to use `delete-log-group`.

**AWS CLI**
**To delete a log group**
The following `delete-log-group` example deletes a log group named `my-logs`.

```
aws logs delete-log-group \
    --log-group-name {{my-logs}}
```
This command produces no output.
For more information, see [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) in the *Amazon CloudWatch Logs User Guide*.
+  For API details, see [DeleteLogGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/delete-log-group.html) in *AWS CLI Command Reference*.

### `delete-log-stream`
<a name="cloudwatch-logs_DeleteLogStream_cli_2_topic"></a>

The following code example shows how to use `delete-log-stream`.

**AWS CLI**
**To delete a log stream**
The following `delete-log-stream` example deletes a log stream named `20150531` from a log group named `my-logs`.

```
aws logs delete-log-stream \
    --log-group-name {{my-logs}} \
    --log-stream-name {{20150531}}
```
This command produces no output.
For more information, see [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) in the *Amazon CloudWatch Logs User Guide*.
+  For API details, see [DeleteLogStream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/delete-log-stream.html) in *AWS CLI Command Reference*.

### `delete-retention-policy`
<a name="cloudwatch-logs_DeleteRetentionPolicy_cli_2_topic"></a>

The following code example shows how to use `delete-retention-policy`.

**AWS CLI**
**To delete the retention policy of a log group**
The following `delete-retention-policy` example removes the retention policy that has previously been applied to a log group named `my-logs`.

```
aws logs delete-retention-policy \
    --log-group-name {{my-logs}}
```
This command produces no output.
For more information, see [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) in the *Amazon CloudWatch Logs User Guide*.
+  For API details, see [DeleteRetentionPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/delete-retention-policy.html) in *AWS CLI Command Reference*.

### `describe-log-groups`
<a name="cloudwatch-logs_DescribeLogGroups_cli_2_topic"></a>

The following code example shows how to use `describe-log-groups`.

**AWS CLI**
**To describe a log group**
The following `describe-log-groups` example describes a log group named `my-logs`.

```
aws logs describe-log-groups \
    --log-group-name-prefix {{my-logs}}
```
Output:

```
{
    "logGroups": [
        {
            "storedBytes": 0,
            "metricFilterCount": 0,
            "creationTime": 1433189500783,
            "logGroupName": "my-logs",
            "retentionInDays": 5,
            "arn": "arn:aws:logs:us-west-2:0123456789012:log-group:my-logs:*"
        }
    ]
}
```
For more information, see [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) in the *Amazon CloudWatch Logs User Guide*.
+  For API details, see [DescribeLogGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-log-groups.html) in *AWS CLI Command Reference*.

### `describe-log-streams`
<a name="cloudwatch-logs_DescribeLogStreams_cli_2_topic"></a>

The following code example shows how to use `describe-log-streams`.

**AWS CLI**
**To describe the log streams in a log group**
The following `describe-log-streams` example shows all log streams starting with the prefix `2015` in the log group `my-logs`.

```
aws logs describe-log-streams \
    --log-group-name {{my-logs}} \
    --log-stream-name-prefix {{2015}}
```
Output:

```
{
    "logStreams": [
        {
            "creationTime": 1433189871774,
            "arn": "arn:aws:logs:us-west-2:0123456789012:log-group:my-logs:log-stream:20150531",
            "logStreamName": "20150531",
            "storedBytes": 0
        },
        {
            "creationTime": 1433189873898,
            "arn": "arn:aws:logs:us-west-2:0123456789012:log-group:my-logs:log-stream:20150601",
            "logStreamName": "20150601",
            "storedBytes": 0
        }
    ]
}
```
For more information, see [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) in the *Amazon CloudWatch Logs User Guide*.
+  For API details, see [DescribeLogStreams](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-log-streams.html) in *AWS CLI Command Reference*.

### `get-log-events`
<a name="cloudwatch-logs_GetLogEvents_cli_2_topic"></a>

The following code example shows how to use `get-log-events`.

**AWS CLI**
**To get log events from a log stream**
The following `get-log-events` example retrieves log events from a log stream named `20150601` in the log group `my-logs`.

```
aws logs get-log-events \
    --log-group-name {{my-logs}} \
    --log-stream-name {{20150601}}
```
Output:

```
{
    "nextForwardToken": "f/31961209122447488583055879464742346735121166569214640130",
    "events": [
        {
            "ingestionTime": 1433190494190,
            "timestamp": 1433190184356,
            "message": "Example Event 1"
        },
        {
            "ingestionTime": 1433190516679,
            "timestamp": 1433190184356,
            "message": "Example Event 1"
        },
        {
            "ingestionTime": 1433190494190,
            "timestamp": 1433190184358,
            "message": "Example Event 2"
        }
    ],
    "nextBackwardToken": "b/31961209122358285602261756944988674324553373268216709120"
}
```
For more information, see [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#ViewingLogData) in the *Amazon CloudWatch Logs User Guide*.
+  For API details, see [GetLogEvents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/get-log-events.html) in *AWS CLI Command Reference*.

### `put-log-events`
<a name="cloudwatch-logs_PutLogEvents_cli_2_topic"></a>

The following code example shows how to use `put-log-events`.

**AWS CLI**
**To put log events into a log stream**
The following `put-log-events` example puts log events to a log stream named `20150601` in the log group `my-logs`. The command reads a JSON array of events from a file named `events` in the current directory.

```
aws logs put-log-events \
    --log-group-name {{my-logs}} \
    --log-stream-name {{20150601}} \
    --log-events {{file://events}}
```
Contents of `events`:

```
[
    {
        "timestamp": 1433190184356,
        "message": "Example Event 1"
    },
    {
        "timestamp": 1433190184358,
        "message": "Example Event 2"
    },
    {
        "timestamp": 1433190184360,
        "message": "Example Event 3"
    }
]
```
Output:

```
{
    "nextSequenceToken": "49542672486831074009579604567656788214806863282469607346"
}
```
Each subsequent call requires the next sequence token provided by the previous call to be specified with the sequence token option.

```
aws logs put-log-events \
    --log-group-name {{my-logs}} \
    --log-stream-name {{20150601}} \
    --log-events {{file://events2}} \
    --sequence-token {{"49542672486831074009579604567656788214806863282469607346"}}
```
Contents of `events2`:

```
[
    {
        "timestamp": 1433190184362,
        "message": "Example Event 4"
    },
    {
        "timestamp": 1433190184364,
        "message": "Example Event 5"
    }
]
```
Output:

```
{
    "nextSequenceToken": "49542672486831074009579604567900991230369019956308219826"
}
```
For more information, see [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) in the *Amazon CloudWatch Logs User Guide*.
+  For API details, see [PutLogEvents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/put-log-events.html) in *AWS CLI Command Reference*.

### `put-retention-policy`
<a name="cloudwatch-logs_PutRetentionPolicy_cli_2_topic"></a>

The following code example shows how to use `put-retention-policy`.

**AWS CLI**
**To set the retention policy of a log group**
The following `put-retention-policy` example adds a 5 day retention policy to a log group named `my-logs`.

```
aws logs put-retention-policy \
    --log-group-name {{my-logs}} \
    --retention-in-days {{5}}
```
This command produces no output.
For more information, see [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) in the *Amazon CloudWatch Logs User Guide*.
+  For API details, see [PutRetentionPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/put-retention-policy.html) in *AWS CLI Command Reference*.

### `start-live-tail`
<a name="cloudwatch-logs_StartLiveTail_cli_2_topic"></a>

The following code example shows how to use `start-live-tail`.

**AWS CLI**
**To start a Live Tail session on a log group**
The following `start-live-tail` example starts a Live Tail session on a log group named `my-logs`.

```
aws logs start-live-tail \
    --log-group-identifiers {{arn:aws:logs:us-west-2:123456789012:log-group:my-logs}}
```
Output:

```
INFO Processing request a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
INFO Request a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 completed in 120 ms
```
The following command starts a Live Tail session on a log group named `my-logs` in interactive mode.

```
aws logs start-live-tail \
    --log-group-identifiers {{arn:aws:logs:us-west-2:123456789012:log-group:my-logs}} \
    --mode {{interactive}}
```
This command produces no output. It displays an interactive Live Tail session in the terminal.
In interactive mode you can highlight as many as five terms in the tailed logs. The severity codes are highlighted by default. Press `h` to enter the highlight mode and then type in the terms to be highlighted, one at a time, and press enter. Press `c` to clear the highlighted term(s). Press `t` to toggle formatting between JSON/Plain text. Press `Esc` to exit the Live Tail session. Press `up` / `down` keys to scroll up or down between log events, use `Ctrl + u` / `Ctrl + d` to scroll faster. Press `q` to scroll to latest log events.
For more information, see [Troubleshoot with CloudWatch Logs Live Tail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_LiveTail.html) in the *Amazon CloudWatch Logs User Guide*.
+  For API details, see [StartLiveTail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/start-live-tail.html) in *AWS CLI Command Reference*.
