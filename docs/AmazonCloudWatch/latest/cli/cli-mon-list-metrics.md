---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/cli/cli-mon-list-metrics.html
---

# mon-list-metrics
<a name="cli-mon-list-metrics"></a>

## Description
<a name="w2aab9c43b3"></a>

Lists the names, namespaces, and dimensions of the metrics associated with your AWS account. You can filter metrics using any combination of metric name, namespace, or dimensions. If you do not specify a filter, all possible matches for the attribute are returned.

**Note**
The mon-list-metrics command can take up to fifteen minutes to report new metric names, namespaces, and dimensions added by calls to `mon-put-data`. The data points put by `mon-put-data`, or other methods will be available by `mon-get-statistics` in less than five minutes.

## Syntax
<a name="w2aab9c43b5"></a>

 ****mon-list-metrics** [--dimensions "key1={{value1}},key2={{value2}}..."] [--metric-name {{value}}] [--namespace {{value}}] [Common Options] **

## Options
<a name="w2aab9c43b7"></a>

| Name | Description |
| --- | --- |
| -d, --dimensions `"key1=value1,key2=value2..."`  | The dimensions of the metric to retrieve. You can specify dimensions two ways and the formats can be combined or used interchangeably:+ One option per dimension: --dimensions "key1=value1" --dimensions "key2=value2"<br />+ All in one option: --dimensions "key1=value1,key2=value2"<br />If no dimensions are specified, no filtering of dimensions will be done. Any other requested filters will still be applied. To be included in the result a metric must contain all specified dimensions, although the metric may contain additional dimensions beyond the requested metrics.<br />Type: Map<br />Valid values: A string of the format name=value, where the key is the name of the dimension, and the value is the dimension's value. The dimension names, and values must be an ANSI string between 1 and 250 characters long. A maximum of 10 dimensions are allowed.<br />Default: n/a<br />Required: No |
| `-m, --metric-name` `VALUE`  | The name of the metric. To be included in the results, the metric name must match the requested metric name exactly. If no metric name is specified no filtering is done. Any other requested filters are applied.<br />Type: Simple<br />Valid values: Any valid metric name between 1 and 250 characters in length.<br />Default: n/a<br />Required: No |
| `-n, --namespace` ` VALUE`  | The namespace to use to filter metrics. For more information about namespaces, see [AWS Namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html).<br />Type: String<br />Valid values: A valid namespace between 1 and 250 characters in length.<br />Default: n/a<br />Required: No |

## Common options
<a name="w2aab9c43b9"></a>

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
<a name="w2aab9c43c11"></a>

This command returns a table that contains the following:
+ Metric Name - The name of the metric attached to this metric.
+ Namespace - The namespace associated with this metric.
+ Dimensions - The dimension names and values associated with this metric.

The Amazon CloudWatch CLI displays errors on stderr.

## Examples
<a name="w2aab9c43c13"></a>

### Example request
<a name="w2aab9c43c13b2"></a>

This example returns a list of all your metrics.

```
mon-list-metrics
```

This is an example of an output of a call to 'mon-list-metrics'.

```
Metric Name                 Namespace  Dimensions
CPUUtilization               AWS/EC2    {InstanceId=i-e7e48a8e}
CPUUtilization               AWS/EC2    {InstanceId=i-231d744a}
CPUUtilization               AWS/EC2    {InstanceId=i-22016e4b}
CPUUtilization               AWS/EC2    {InstanceId=i-b0345cd9}
CPUUtilization               AWS/EC2    {InstanceId=i-539dff3a}
CPUUtilization               AWS/EC2    {InstanceId=i-af3544c6}
CPUUtilization               AWS/EC2    {InstanceId=i-d4f29ebd}
CPUUtilization               AWS/EC2    {ImageId=ami-de4daab7}
...
```

### Example request
<a name="w2aab9c43c13b4"></a>

This example lists your metrics with the specified name.

```
mon-list-metrics --metric-name RequestCount
```

### Example request
<a name="w2aab9c43c13b6"></a>

This example lists your metrics that belong to the specified namespace.

```
mon-list-metrics --namespace MyService
```

### Example request
<a name="w2aab9c43c13b8"></a>

This example lists your metrics with the specified dimension names and values.

```
mon-list-metrics --dimensions "User=SomeUser,Stack=Test"
```

## Related topics
<a name="w2aab9c43c15"></a>

### Download
<a name="w2aab9c43c15b2"></a>
+ [Set up the command line interface](SetupCLI.md)

### Related action
<a name="w2aab9c43c15b4"></a>
+ [ListMetrics](http://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html)

### Related command
<a name="w2aab9c43c15b6"></a>
+  [mon-describe-alarms](cli-mon-describe-alarms.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
