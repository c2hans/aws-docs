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
The following command creates a log group named `my-logs`:

```
aws logs create-log-group --log-group-name {{my-logs}}
```
+  For API details, see [CreateLogGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/create-log-group.html) in *AWS CLI Command Reference*.

### `create-log-stream`
<a name="cloudwatch-logs_CreateLogStream_cli_2_topic"></a>

The following code example shows how to use `create-log-stream`.

**AWS CLI**
The following command creates a log stream named `20150601` in the log group `my-logs`:

```
aws logs create-log-stream --log-group-name {{my-logs}} --log-stream-name {{20150601}}
```
+  For API details, see [CreateLogStream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/create-log-stream.html) in *AWS CLI Command Reference*.

### `delete-log-group`
<a name="cloudwatch-logs_DeleteLogGroup_cli_2_topic"></a>

The following code example shows how to use `delete-log-group`.

**AWS CLI**
The following command deletes a log group named `my-logs`:

```
aws logs delete-log-group --log-group-name {{my-logs}}
```
+  For API details, see [DeleteLogGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/delete-log-group.html) in *AWS CLI Command Reference*.

### `delete-log-stream`
<a name="cloudwatch-logs_DeleteLogStream_cli_2_topic"></a>

The following code example shows how to use `delete-log-stream`.

**AWS CLI**
The following command deletes a log stream named `20150531` from a log group named `my-logs`:

```
aws logs delete-log-stream --log-group-name {{my-logs}} --log-stream-name {{20150531}}
```
+  For API details, see [DeleteLogStream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/delete-log-stream.html) in *AWS CLI Command Reference*.

### `delete-retention-policy`
<a name="cloudwatch-logs_DeleteRetentionPolicy_cli_2_topic"></a>

The following code example shows how to use `delete-retention-policy`.

**AWS CLI**
The following command removes the retention policy that has previously been applied to a log group named `my-logs`:

```
aws logs delete-retention-policy --log-group-name {{my-logs}}
```
+  For API details, see [DeleteRetentionPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/delete-retention-policy.html) in *AWS CLI Command Reference*.

### `describe-log-groups`
<a name="cloudwatch-logs_DescribeLogGroups_cli_2_topic"></a>

The following code example shows how to use `describe-log-groups`.

**AWS CLI**
The following command describes a log group named `my-logs`:

```
aws logs describe-log-groups --log-group-name-prefix {{my-logs}}
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
+  For API details, see [DescribeLogGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-log-groups.html) in *AWS CLI Command Reference*.

### `describe-log-streams`
<a name="cloudwatch-logs_DescribeLogStreams_cli_2_topic"></a>

The following code example shows how to use `describe-log-streams`.

**AWS CLI**
The following command shows all log streams starting with the prefix `2015` in the log group `my-logs`:

```
aws logs describe-log-streams --log-group-name {{my-logs}} --log-stream-name-prefix {{2015}}
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
+  For API details, see [DescribeLogStreams](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-log-streams.html) in *AWS CLI Command Reference*.

### `get-log-events`
<a name="cloudwatch-logs_GetLogEvents_cli_2_topic"></a>

The following code example shows how to use `get-log-events`.

**AWS CLI**
The following command retrieves log events from a log stream named `20150601` in the log group `my-logs`:

```
aws logs get-log-events --log-group-name {{my-logs}} --log-stream-name {{20150601}}
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
+  For API details, see [GetLogEvents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/get-log-events.html) in *AWS CLI Command Reference*.

### `put-log-events`
<a name="cloudwatch-logs_PutLogEvents_cli_2_topic"></a>

The following code example shows how to use `put-log-events`.

**AWS CLI**
The following command puts log events to a log stream named `20150601` in the log group `my-logs`:

```
aws logs put-log-events --log-group-name {{my-logs}} --log-stream-name {{20150601}} --log-events {{file://events}}
```
Output:

```
{
    "nextSequenceToken": "49542672486831074009579604567656788214806863282469607346"
}
```
The above example reads a JSON array of events from a file named `events` in the current directory:

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
Each subsequent call requires the next sequence token provided by the previous call to be specified with the sequence token option:

```
aws logs put-log-events --log-group-name {{my-logs}} --log-stream-name {{20150601}} --log-events {{file://events2}} --sequence-token {{"49542672486831074009579604567656788214806863282469607346"}}
```
Output:

```
{
    "nextSequenceToken": "49542672486831074009579604567900991230369019956308219826"
}
```
+  For API details, see [PutLogEvents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/put-log-events.html) in *AWS CLI Command Reference*.

### `put-retention-policy`
<a name="cloudwatch-logs_PutRetentionPolicy_cli_2_topic"></a>

The following code example shows how to use `put-retention-policy`.

**AWS CLI**
The following command adds a 5 day retention policy to a log group named `my-logs`:

```
aws logs put-retention-policy --log-group-name {{my-logs}} --retention-in-days {{5}}
```
+  For API details, see [PutRetentionPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/put-retention-policy.html) in *AWS CLI Command Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
