---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/cli/cli-mon-set-alarm-state.html
---

# mon-set-alarm-state
<a name="cli-mon-set-alarm-state"></a>

## Description
<a name="w2aab9c55b3"></a>

Temporarily changes the alarm state of the specified alarm. On the next period, the alarm is set to its true state.

## Syntax
<a name="w2aab9c55b5"></a>

 ****mon-set-alarm-state** AlarmName --state-reason {{value}} --state-value {{value}} [--state-reason-data {{value}}] [Common Options] **

## Options
<a name="w2aab9c55b7"></a>

| Name | Description |
| --- | --- |
| `AlarmName` | The name of the alarm. You can also set this value using `--alarm-name`.<br />Type: Argument<br />Valid values: A UTF-8 string.<br />Default: n/a<br />Required: Yes |
| `--state-reason` `VALUE`  | The reason why this alarm was set to this state (human readable).<br />Type: String<br />Valid values: A UTF-8 string between 1 and 1023 characters.<br />Default: n/a<br />Required: Yes |
| `--state-reason-data` `VALUE`  | The reason why this alarm was set to this state. This data is intended to be machine-readable JSON.Type: String<br />Valid values: A valid machine-readable JSON string between 1 and 4000 characters.<br />Default: n/a<br />Required: No |
| `--state-value` ` VALUE`  | The state the alarm should be set to.<br />Type: Enumeration<br />Valid values: ALARM, OK or INSUFFICIENT\_DATA<br />Default: n/a<br />Required: Yes |

## Common options
<a name="w2aab9c55b9"></a>

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
<a name="w2aab9c55c11"></a>

This command temporarily changes an alarm's state and displays `OK-Set alarm state value` when the request is successful.

The Amazon CloudWatch CLI displays errors on stderr.

## Examples
<a name="w2aab9c55c13"></a>

### Example request
<a name="w2aab9c55c13b2"></a>

This example sets the state of the alarm named my-alarm to OK.

```
mon-set-alarm-state --alarm-name my-alarm --state OK
```

## Related topics
<a name="w2aab9c55c15"></a>

### Download
<a name="w2aab9c55c15b2"></a>
+ [Set up the command line interface](SetupCLI.md)

### Related action
<a name="w2aab9c55c15b4"></a>
+ [SetAlarmState](http://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_SetAlarmState.html)

### Related command
<a name="w2aab9c55c15b6"></a>
+  [mon-describe-alarms](cli-mon-describe-alarms.md)
