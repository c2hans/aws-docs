---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/cli/cli-mon-enable-alarm-actions.html
---

# mon-enable-alarm-actions
<a name="cli-mon-enable-alarm-actions"></a>

## Description
<a name="w2aab9c35b3"></a>

Enables all actions for the specified alarms.

## Syntax
<a name="w2aab9c35b5"></a>

 ****mon-enable-alarm-actions** [AlarmNames [{{AlarmNames}} ...]] [Common Options] **

## Options
<a name="w2aab9c35b7"></a>

| Name | Description |
| --- | --- |
| `AlarmNames` `AlarmNames`  | The names of the alarms. You can also set this value using `--alarm-name`.<br />Type: Argument<br />Valid values: A valid list of alarm names.<br />Default: n/a<br />Required: Yes |

## Common options
<a name="w2aab9c35b9"></a>

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
<a name="w2aab9c35c11"></a>

This command enables alarm actions for the specified alarms.

The Amazon CloudWatch CLI displays errors on stderr.

## Examples
<a name="w2aab9c35c13"></a>

### Example request
<a name="w2aab9c35c13b2"></a>

This example enables all actions for the alarm named my-alarm.

```
1. mon-enable-alarm-actions --alarm-name my-alarm
```

## Related topics
<a name="w2aab9c35c15"></a>

### Download
<a name="w2aab9c35c15b2"></a>
+ [Set up the command line interface](SetupCLI.md)

### Related action
<a name="w2aab9c35c15b4"></a>
+ [EnableAlarmActions](http://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_EnableAlarmActions.html)

### Related commands
<a name="w2aab9c35c15b6"></a>
+  [mon-disable-alarm-actions](cli-mon-disable-alarm-actions.md)
+  [mon-delete-alarms](cli-mon-delete-alarms.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
