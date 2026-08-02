---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/cli/cli-mon-describe-alarms.html
---

# mon-describe-alarms
<a name="cli-mon-describe-alarms"></a>

## Description
<a name="w2aab9c23b3"></a>

Gets information on the specified alarms. If you don't specify an alarm name, this command returns information about all of your alarms. You can retrieve alarms by using only the alarm name prefix, the alarm state, or an action prefix.

## Syntax
<a name="w2aab9c23b5"></a>

 ****mon-describe-alarms** [AlarmNames [{{AlarmNames}} ...]] [--action-prefix {{value}}] [--alarm-name-prefix {{value}}] [--state-value {{value}}] [Common Options]**

## Options
<a name="w2aab9c23b7"></a>

| Name | Description |
| --- | --- |
| `AlarmNames` `AlarmNames` | The names of the alarms. You can also set this value using `--alarm-name`. You can specify this option multiple times.<br />Type: Argument<br />Valid values: An existing alarm name, otherwise no response is returned.<br />Default: n/a, displays all alarms by default.<br />Required: No |
|  `--action-prefix` `VALUE`  | Prefix of action names.<br />Type: Argument<br />Valid values: The prefix of an existing action name, in ARN format.<br />Default: n/a, display the first action by default.<br />Required: No |
|  `--alarm-name-prefix` `VALUE`  | Prefix of alarm names.<br />Type: Argument<br />Valid values: The prefix of an existing alarm name.<br />Default: n/a<br />Required: No |
|  `--state-value` `VALUE`  | The state of the alarm.<br />Type: Enumeration<br />Valid values: OK, ALARM, or INSUFFICIENT\_DATA<br />Default: All alarm states.<br />Required: No |

## Common options
<a name="w2aab9c23b9"></a>

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
<a name="w2aab9c23c11"></a>

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
<a name="w2aab9c23c13"></a>

### Example request
<a name="w2aab9c23c13b2"></a>

This example describes all of your alarms whose name starts with my-alarm.

```
mon-describe-alarms --alarm-name-prefix my-alarm --headers
```

This is an example output of this command.

```
ALARM      STATE ALARM_ACTIONS  NAMESPACE  METRIC_NAME    PERIOD  STATISTIC  EVAL_PERIODS  COMPARISON            THRESHOLD
my-alarm1  OK    arn:aws:sns:.. AWS/EC2    CPUUtilization 60      Average    3             GreaterThanThreshold  100.0
my-alarm2  OK    arn:aws:sns:.. AWS/EC2    CPUUtilization 60      Average    5
GreaterThanThreshold  80o.0
```

## Related topics
<a name="w2aab9c23c15"></a>

### Download
<a name="w2aab9c23c15b2"></a>
+ [Set up the command line interface](SetupCLI.md)

### Related action
<a name="w2aab9c23c15b4"></a>
+ [DescribeAlarms](http://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarms.html)

### Related commands
<a name="w2aab9c23c15b6"></a>
+  [mon-describe-alarm-history](cli-mon-describe-alarm-history.md)
+  [mon-describe-alarms-for-metric](cli-mon-describe-alarms-for-metric.md)
