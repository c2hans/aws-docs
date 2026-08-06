---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/cli/cli-mon-put-metric-alarm.html
---

# mon-put-metric-alarm
<a name="cli-mon-put-metric-alarm"></a>

## Description
<a name="w2aab9c51b3"></a>

Creates or updates an alarm and associates it with the specified CloudWatch metric. You can also use this command to associate one or more Amazon Simple Notification Service (Amazon SNS) resources with an alarm.

When this operation creates an alarm, the alarm state is immediately set to INSUFFICIENT\_DATA. The alarm is evaluated and its StateValue is set appropriately. Any actions associated with the StateValue is then executed.

**Note**
When updating an existing alarm, StateValue is left unchanged.

## Syntax
<a name="w2aab9c51b5"></a>

 ****mon-put-metric-alarm** AlarmName --comparison-operator {{value}} --evaluation-periods {{value}} --metric-name {{value}} --namespace {{value}} --period {{value}} [--statistic {{value}}] [--extendedstatistic {{value}}] --threshold {{value}} [--actions-enabled {{value}}] [--alarm-actions {{value}}[,{{value}}...] ] [--alarm-description {{value}}] [--dimensions "key1={{value1}},key2={{value2}}..."] [--ok-actions {{value}}[,{{value}}...] ] [--unit {{value}}] [--insufficient-data-actions {{value}}[,{{value}}...]] [Common Options] **

## Options
<a name="w2aab9c51b7"></a>

| Name | Description |
| --- | --- |
| `AlarmName` ``  | The name of the alarm to update or create. The name must be unique within your AWS account. You can also set this value using `--alarm-name`.<br />Type: Argument<br />Valid values: A UTF-8 string.<br />Default: n/a<br />Required: Yes |
| `--actions-enabled` `VALUE`  | Indicates whether actions should be executed when the alarm changes state. <br />Type: Boolean<br />Valid values: True or False<br />Default: True<br />Required: No |
| `--alarm-actions` `VALUE1,VALUE2,VALUE3... `  | The actions (up to five) to execute when this alarm transitions into an ALARM state from any other state. Each action is specified as an Amazon Resource Name (ARN). Using alarm actions, you can publish to an Amazon SNS topic, activate an Amazon EC2 Auto Scaling policy, or stop, terminate, or recover an Amazon EC2 instance.If you are using an AWS Identity and Access Management (IAM) account to create or modify an alarm, you must have the following Amazon EC2 permissions:  `ec2:DescribeInstanceStatus` and `ec2:DescribeInstances` for all alarms on Amazon EC2 instance status metrics. `ec2:StopInstances` for alarms with stop actions. `ec2:TerminateInstances` for alarms with terminate actions. `ec2:DescribeInstanceRecoveryAttribute`, and `ec2:RecoverInstances` for alarms with recover actions.  <br />If you have read/write permissions for Amazon CloudWatch but not for Amazon EC2, you can still create an alarm but the stop or terminate actions won’t be performed on the Amazon EC2 instance. However, if you are later granted permission to use the associated Amazon EC2 APIs, the alarm actions you created earlier will be performed. For more information about IAM permissions, see [Permissions and Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/PermissionsAndPolicies.html) in *IAM User Guide*. <br />If you are using an IAM role (for example, an Amazon EC2 instance profile), you cannot stop or terminate the instance using alarm actions. However, you can still see the alarm state and perform any other actions such as Amazon SNS notifications or Amazon EC2 Auto Scaling policies. <br />If you are using temporary security credentials granted using the AWS Security Token Service (AWS STS), you cannot stop or terminate an Amazon EC2 instance using alarm actions. <br />Type: String<br />Valid values: An ARN for an Amazon SNS topic, an Auto Scaling policy, or an ARN to stop, terminate, or recover an Amazon EC2 instance.<br />Default: n/a<br />Required: No |
| `--alarm-description` `VALUE`  | The description of the alarm.<br />Type: String<br />Valid values: Any Unicode string between 1 and 255 characters in length.<br />Default: n/a<br />Required: No |
| `--comparison-operator` `VALUE`  | The comparison operator used to compare a data point to the threshold.<br />Type: Enumeration<br />Valid values: one of GreaterThanOrEqualToThreshold, GreaterThanThreshold, LessThanThreshold, or LessThanOrEqualToThreshold<br />Default: n/a<br />Required: Yes |
| `--dimensions` `"key1=value1,key2=value2..."`  | The dimensions of the metric to create that you want to create an alarm for. You can specify dimensions two ways and the formats can be combined or used interchangeably:+ One option per dimension: --dimensions "key1=value1" --dimensions "key2=value2"<br />+ All in one option: --dimensions "key1=value1,key2=value2"<br />Type: Map<br />Valid values: A string of the format name=value, where the key is the name of the dimension, and the value is the dimension's value. The dimension names, and values must be an ANSI string between 1 and 250 characters long. A maximum of 10 dimensions are allowed.<br />Default: n/a<br />Required: No |
| `--evaluation-periods` `VALUE`  | The number of consecutive periods for which the value of the metric is compared to the threshold to determine alarm status.<br />Type: Integer<br />Valid values: A number greater than zero.<br />Default: n/a<br />Required: Yes |
| `--metric-name` `VALUE`  | The name of the metric on which to alarm.<br />Type: Argument<br />Valid values: An ANSI string between 1 and 250 characters in length.<br />Default: n/a<br />Required: Yes |
| `--namespace` `VALUE`  | The namespace of the metric on which to alarm. For more information about namespaces, see [AWS Namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html).<br />Type: String<br />Valid values: An ANSI string between 1 and 250 characters in length.<br />Default: n/a<br />Required: Yes |
| `--ok-actions` `VALUE1,VALUE2,VALUE3...`  | The actions (up to five) to execute when this alarm transitions into an OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).<br />Type: String<br />Valid values: A valid ARN identifier.<br />Default: n/a<br />Required: No |
| `--period` `VALUE`  | The period of metric on which to alarm (in seconds).<br />Type: Argument<br />Valid values: A number, in seconds that is a multiple of 60 seconds.<br />Default: n/a<br />Required: Yes |
| `--statistic` `VALUE`  | The statistic of the metric on which to alarm.<br />Type: Enumeration<br />Valid values: SampleCount, Average, Sum, Minimum, or Maximum<br />Default: n/a<br />Required: You must specify --statistic or --extendedstatistic. |
| `--extendedstatistic` `VALUE`  | The percentile statistic of the metric on which to alarm.<br />Type: String<br />Valid values: Any percentile, with up to two decimal places (for example, p95.45).<br />Default: n/a<br />Required: You must specify --statistic or --extendedstatistic. |
|  `--threshold` `VALUE`  | The threshold that data points are compared with to determine the alarm state.<br />Type: Double<br />Valid values: A double value. All values must be a number between 1E-130 and 1E130.<br />Default: n/a<br />Required: Yes |
| `--unit` `VALUE`  | The unit of the metric on which to alarm.<br />Type: Enumeration<br />Valid values: One of the following:+  Seconds <br />+  Microseconds <br />+  Milliseconds <br />+  Bytes <br />+  Kilobytes <br />+  Megabytes <br />+  Gigabytes <br />+  Terabytes <br />+  Bits <br />+  Kilobits <br />+  Megabits <br />+  Gigabits <br />+  Terabits <br />+  Percent <br />+  Count <br />+  Bytes/Second <br />+  Kilobytes/Second <br />+  Megabytes/Second <br />+  Gigabytes/Second <br />+  Terabytes/Second <br />+  Bits/Second <br />+  Kilobits/Second <br />+  Megabits/Second <br />+  Gigabits/Second <br />+  Terabits/Second <br />+  Count/Second <br />+  None <br />Default: n/a<br />Required: No |
| `--insufficient-data-actions` `VALUE1,VALUE2,VALUE3...`  | The actions (up to five) to execute when this alarm transitions into an INSUFFICIENT\_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).<br />Type: String<br />Valid values: A valid ARN identifier.<br />Default: n/a<br />Required: No |

## Common options
<a name="w2aab9c51b9"></a>

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
<a name="w2aab9c51c11"></a>

This command creates or updates an alarm associated with the specified metric.

The Amazon CloudWatch CLI displays errors on stderr.

## Examples
<a name="w2aab9c51c13"></a>

### Example request
<a name="w2aab9c51c13b2"></a>

This example creates an alarm that publishes a message to a topic when CPU utilization of an EC2 instances exceeds 90 percent for three consecutive one minute periods.

```
mon-put-metric-alarm --alarm-name my-alarm --alarm-description "some desc" \
--metric-name CPUUtilization --namespace AWS/EC2 --statistic Average  --period 60 --threshold 90 \
--comparison-operator GreaterThanThreshold  --dimensions InstanceId=i-abcdef --evaluation-periods 3  \
--unit Percent --alarm-actions arn:aws:sns:us-east-1:1234567890:my-topic
```

## Related topics
<a name="w2aab9c51c15"></a>

### Download
<a name="w2aab9c51c15b2"></a>
+ [Set up the command line interface](SetupCLI.md)

### Related action
<a name="w2aab9c51c15b4"></a>
+ [PutMetricAlarm](http://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html)

### Related command
<a name="w2aab9c51c15b6"></a>
+  [mon-put-data](cli-mon-put-data.md)
