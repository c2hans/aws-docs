---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/cli/cli-mon-describe-alarms-for-metric.html
---

# mon-describe-alarms-for-metric
<a name="cli-mon-describe-alarms-for-metric"></a>

## Description
<a name="w2aab9c27b3"></a>

Gets information about the alarms associated with the specified metric.

## Syntax
<a name="w2aab9c27b5"></a>

 ****mon-describe-alarms-for-metric** --metric-name {{value}} --namespace {{value}} [--dimensions "key1={{value1}},key2={{value2}}..."] [--period {{value}}] [--statistic {{value}}] [--extendedstatistic {{value}}] [--unit {{value}}] [Common Options] **

## Options
<a name="w2aab9c27b7"></a>

| Name | Description |
| --- | --- |
| `--dimensions` `- "key1=value1,key2=value2...`  | The dimensions associated with the metric. You can specify dimensions two ways and the formats can be combined or used interchangeably:+ One option per dimension: --dimensions "key1=value1" --dimensions "key2=value2"<br />+ All in one option: --dimensions "key1=value1,key2=value2"<br />Type: Map<br />Valid values: A string of the format name=value, where the key is the name of the dimension, and the value is the dimension's value. The dimension names, and values must be an ANSI string between 1 and 250 characters long. A maximum of 10 dimensions are allowed.<br />Default: n/a<br />Required: No |
| `--metric-name` `VALUE`  | The name of the metric whose associated alarms you want to search for.<br />Type: Argument<br />Valid values: A valid metric name between 1 and 255 characters in length.<br />Default: n/a<br />Required: Yes |
| `--namespace` `VALUE`  | The namespace of the metric associated with the alarm. For more information about namespaces, see [AWS Namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html).<br />Type: String<br />Valid values: A valid namespace between 1 and 250 characters in length.<br />Default: n/a<br />Required: Yes |
| `--period` `VALUE`  | The period to filter the alarms by. Only alarms that evaluate metrics at this period will be included in the results. If this isn't specified alarms on any period will be included .<br />Type: Argument<br />Valid values: A number, in seconds that is a multiple of 60 seconds.<br />Default: n/a<br />Required: No |
| `--statistic` `VALUE`  | The statistic to filter alarms by. Only alarms on the specified statistic will be included. If this parameter isn't specified, alarms on any statistic are included.<br />Type: Enumeration<br />Valid values: SampleCount, Average, Sum, Minimum or Maximum<br />Default: n/a<br />Required: No |
| `--extendedstatistic` `VALUE`  | The percentile statistic to filter alarms by. Only alarms on the specified statistic are included. If this parameter isn't specified, alarms on any statistic are included.<br />Type: String<br />Valid values: Any percentile, with up to two decimal places (for example, p95.45).<br />Default: n/a<br />Required: No |
| `--unit` `VALUE`  | The unit to filter the alarms by. Only alarms on the specified statistics will be included. If this isn't specified than alarms on any units will be included. If the alarm doesn't have a unit specified than the only way to search for the alarm is to omit this option.<br />Type: Enumeration<br />Valid values: One of the following:+  Seconds <br />+  Microseconds <br />+  Milliseconds <br />+  Bytes <br />+  Kilobytes <br />+  Megabytes <br />+  Gigabytes <br />+  Terabytes <br />+  Bits <br />+  Kilobits <br />+  Megabits <br />+  Gigabits <br />+  Terabits <br />+  Percent <br />+  Count <br />+  Bytes/Second <br />+  Kilobytes/Second <br />+  Megabytes/Second <br />+  Gigabytes/Second <br />+  Terabytes/Second <br />+  Bits/Second <br />+  Kilobits/Second <br />+  Megabits/Second <br />+  Gigabits/Second <br />+  Terabits/Second <br />+  Count/Second <br />+  None <br />Default: n/a<br />Required: No |

## Common options
<a name="w2aab9c27b9"></a>

| Name | Description |
| --- | --- |
| `--aws-credential-file` `VALUE`  | The location of the file with your AWS credentials. You can set this value using the environment variable `AWS_CREDENTIAL_FILE`. If you define the environment variable or you provide the path to the credential file, the file must exist or the request fails. All CloudWatch requests must be signed using your access key ID and secret access key.<br />Type: String<br />Valid values: A valid path to a file containing your access key ID and secret access key.<br />Default: Uses the environment variable `AWS_CREDENTIAL_FILE`, if set. |
| `-C, --ec2-cert-file-path` `VALUE`  | The location of your EC2 certificate file for signing requests. You can use the environment variable `EC2_CERT` to specify this value.<br />Type: String<br />Valid values: A valid file path to the PEM file provided by Amazon EC2 or AWS Identity and Access Management.<br />Default: Uses the environment variable `EC2_CERT`, if set. |
|  `--connection-timeout` `VALUE`  | The connection timeout value, in seconds.<br />Type: Integer<br />Valid values: Any positive number.<br />Default: 30 |
|  `--delimiter` `VALUE`  | The delimiter to use when displaying delimited (long) results.<br />Type: String<br />Valid values: Any string.<br />Default: Comma (,) |
|  `--headers` ``  | If you are displaying tabular or delimited results, include the column headers. If you are showing XML results, return the HTTP headers from the service request, if applicable.<br />Type: Flag<br />Valid values: When present, shows headers.<br />Default: The `--headers` option is off by default. |
|  `-I, --access-key-id` `VALUE`  | The access key ID that will be used, in conjunction with the secret key, to sign the request. This must be used in conjunction with --secret-key, otherwise the option is ignored. All requests to CloudWatch must be signed, otherwise the request is rejected.<br />Type: String<br />Valid values: A valid access key ID.<br />Default: None |
|  `-K, --ec2-private-key-file-path` `VALUE`  | The private key that will be used to sign the request. Using public/private keys causes the CLI to use SOAP. The request is signed with a public certificate and private key. This parameter must be used in conjunction with `EC2_CERT`, otherwise the value is ignored. The value of the environment variable `EC2_PRIVATE_KEY` will be used if it is set, and this option is not specified. This option is ignored if the environment variable `AWS_CREDENTIAL_FILE` is set, or `--aws-credentials-file` is used. All requests to CloudWatch must be signed, otherwise the request is rejected.<br />Type: String<br />Valid values: The path to a valid ASN.1 private key.<br />Default: None |
|  `--region` `VALUE`  | The region requests are directed to. You can use the environment variable `EC2_REGION` to specify the value. The region is used to create the URL used to call CloudWatch, and must be a valid Amazon Web Services (AWS) region.<br />Type: String<br />Valid values: Any AWS region, for example, us-east-1.<br />Default: us-east-1, unless the `EC2_REGION` environment variable is set. |
|  `S, --secret-key` `VALUE`  | The secret access key that will be used to sign the request, in conjunction with an access key ID. This parameter must be used in conjunction with `--access-key-id`, otherwise this option is ignored.<br />Type: String<br />Valid values: Your access key ID.<br />Default: None |
|  `--show-empty-fields` ``  | Shows empty fields using (nil) as a placeholder to indicate that this data was not requested.<br />Type: Flag<br />Valid values: None<br />Default: Empty fields are not shown by default. |
|  `--show-request` ``  | Displays the URL the CLI uses to call AWS.<br />Type: Flag<br />Valid values: None<br />Default: false |
|  `--show-table, --show-long, --show-xml, --quiet` ``  | Specifies how the results are displayed: in a table, delimited (long), XML, or no output (quiet). The `--show-table` display shows a subset of the data in fixed column-width form; `--show-long` shows all of the returned values delimited by a character; `--show-xml` is the raw return from the service; and `--quiet` suppresses all standard output. All options are mutually exclusive, with the priority `--show-table`, `--show-long`, `--show-xml`, and `--quiet`.<br />Type: Flag<br />Valid values: None<br />Default: `--show-table` |
|  `-U, --url` `VALUE`  | The URL used to contact CloudWatch. You can set this value using the environment variable `AWS_CLOUDWATCH_URL`. This value is used in conjunction with `--region` to create the expected URL. This option overrides the URL for the service call.<br />Type: String<br />Valid values: A valid HTTP or HTTPS URL.<br />Default: Uses the value specified in `AWS_CLOUDWATCH_URL`, if set. |

## Output
<a name="w2aab9c27c11"></a>

This command returns a table that contains the following:
+ ALARM - Alarm name.
+ DESCRIPTION - The alarm description. This column appears only in the --show-long view.
+ STATE - The alarm state.
+ STATE\_REASON - A human-readable reason for state. This column appears only in the --show-long view.
+ STATE\_REASON\_DATA - A machine-readable reason for state (JSON format). This column appears only in the --show-long view.
+ ENABLED - Enables or disables actions. This column appears only in the --show-long view.
+ OK\_ACTIONS - The action to execute on OK status. This column appears only in the --show-long view.
+ ALARM\_ACTIONS - The action to execute on ALARM status.
+ INSUFFICIENT\_DATA\_ACTIONS - The action to execute on INSUFFICIENT\_DATA status. This column appears only in the --show-long view.
+ NAMESPACE - A namespace for the metric.
+ METRIC\_NAME - The name of the metric.
+ DIMENSIONS - The metric dimensions. This column appears only in the --show-long view.
+ PERIOD - The period.
+ STATISTIC - The statistic (Average, Minimum, Maximum, Sum, SampleCount).
+ EXTENDEDSTATISTIC - The percentile statistic.
+ UNIT - The unit. This column appears only in the --show-long view.
+ EVAL\_PERIODS - The number of periods to evaluate the metric.
+ COMPARISON - The comparison operator.
+ THRESHOLD - The threshold.

The Amazon CloudWatch CLI displays errors on stderr.

## Examples
<a name="w2aab9c27c13"></a>

### Example request
<a name="w2aab9c27c13b2"></a>

This example describes an alarm for a given metric.

```
mon-describe-alarms-for-metric--metric-name CPUUtilization --namespace AWS/EC2  --dimensions InstanceId=i-abcdef
```

This is an example output of this command.

```
ALARM    STATE ALARM_ACTIONS  NAMESPACE  METRIC_NAME    PERIOD  STATISTIC  EVAL_PERIODS  COMPARISON            THRESHOLD
my-alarm1  OK    arn:aws:sns:.. AWS/EC2    CPUUtilization 60      Average    3             GreaterThanThreshold  100.0
my-alarm2  OK    arn:aws:sns:.. AWS/EC2    CPUUtilization 60      Average    5             GreaterThanThreshold  80.0
```

## Related topics
<a name="w2aab9c27c15"></a>

### Download
<a name="w2aab9c27c15b2"></a>
+ [Set up the command line interface](SetupCLI.md)

### Related action
<a name="w2aab9c27c15b4"></a>
+ [DescribeAlarmForMetric](http://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarmsForMetric.html)

### Related commands
<a name="w2aab9c27c15b6"></a>
+  [mon-describe-alarm-history](cli-mon-describe-alarm-history.md)
+  [mon-describe-alarms](cli-mon-describe-alarms.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
