---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/cli/cli-mon-put-data.html
---

# mon-put-data
<a name="cli-mon-put-data"></a>

## Description
<a name="w2aab9c47b3"></a>

Adds metric data points to the specified metric. This call will put time-series data, for either the raw value or valid statistic values of a given metric name. It supports the input of a single data point at a time.

**Note**
When you create a new metric using the `mon-put-data` command, it can take up to two minutes before you can retrieve statistics on the new metric using the `mon-get-stats` command. However, it can take up to fifteen minutes before the new metric appears in the list of metrics retrieved using the `mon-list-metrics` command.

## Syntax
<a name="w2aab9c47b5"></a>

 ****mon-put-data** --metric-name {{value}}[--namespace {{value}} [--dimensions "key1={{value1}},key2={{value2}}..."] [--statisticValues "key1={{value1}},key2={{value2}}..."] [--timestamp {{value}}] [--unit {{value}}] [--value {{value}}] [Common Options] **

## Options
<a name="w2aab9c47b7"></a>

| Name | Description |
| --- | --- |
| -d, --dimensions "key1=value1,key2=value2..." ``  | The dimensions that uniquely identify the metric data. You can specify dimensions two ways and the formats can be combined or used interchangeably:+ One option per dimension: --dimensions "key1=value1" --dimensions "key2=value2"<br />+ All in one option: --dimensions "key1=value1,key2=value2"<br />Type: Map<br />Valid values: A string of the format name=value, where the key is the name of the dimension, and the value is the dimension's value. The dimension names, and values must be an ANSI string between 1 and 250 characters long. A maximum of 10 dimensions are allowed.<br />Default: n/a<br />Required: No |
| `-m, --metric-name` `VALUE1,VALUE2,VALUE3...`  | The name of the metric.<br />Type: String<br />Valid values: Any valid metric name between 1 and 250 characters.<br />Default: n/a<br />Required: Yes |
| `n, --namespace` `VALUE`  | The namespace of the metric. For more information about namespaces, see [AWS Namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html).<br />Type: String<br />Valid values: An ANSI string between 1 and 250 characters in length.<br />Default: n/a<br />Required: Yes |
| `-s, --statistic` `Values "key1=value1,key2=value2..."`  | The statistics to store for the specified timestamp and metric. This option is exclusive with `--value`. At least one of `--statisticValue` or `--value` must be specified.<br />Type: Map<br />Valid values: A string containing all double values for all statistic names: SampleCount, Sum, Maximum, and Minimum. All these values must be a value between 1E-130 and 1E130.<br />Default: n/a<br />Required: Yes |
| `-t, --timestamp` `VALUE`  | The timestamp of the data point or observation for the metric to record. Timestamps are specified using ISO8601 combined format. For example the date and time July 30th, 2013 at 12:30:00 PST would be represented as 2013-07-30T12:30:00-07:00, or in UTC: 2013-07-30T19:30:00Z.<br />Type: Simple<br />Valid values: A valid timestamp represented in ISO8601 format with time zone offset, or UTC indicator.<br />Default: The current UTC time.<br />Required: No |
| `-u, --unit` `VALUE`  | The unit for the metric.<br />Type: Enumeration<br />Valid values: One of the following:+  Seconds <br />+  Microseconds <br />+  Milliseconds <br />+  Bytes <br />+  Kilobytes <br />+  Megabytes <br />+  Gigabytes <br />+  Terabytes <br />+  Bits <br />+  Kilobits <br />+  Megabits <br />+  Gigabits <br />+  Terabits <br />+  Percent <br />+  Count <br />+  Bytes/Second <br />+  Kilobytes/Second <br />+  Megabytes/Second <br />+  Gigabytes/Second <br />+  Terabytes/Second <br />+  Bits/Second <br />+  Kilobits/Second <br />+  Megabits/Second <br />+  Gigabits/Second <br />+  Terabits/Second <br />+  Count/Second <br />+  None <br />Default: n/a<br />Required: No |
| `-v, --value` `VALUE`  | A single value to be recorded. The value is translated to a statistic set of the form: SampleCount=1, Sum=VALUE, Minimum=VALUE, Maximum=VALUE. This option is exclusive of `--statisticValues`.<br />Type: Simple<br />Valid values: All values must be a number between 1E-130 and 1E130.<br />Default: n/a<br />Required: Yes |

## Common options
<a name="w2aab9c47b9"></a>

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
<a name="w2aab9c47c11"></a>

This command adds metric data points to a metric.

The Amazon CloudWatch CLI displays errors on stderr.

## Examples
<a name="w2aab9c47c13"></a>

### Example request
<a name="w2aab9c47c13b2"></a>

This example puts statistic data for `RequestCount` in the `MyService` namespace. The metric contains no dimensions and so represents the overall RequestCount across the entire service. The measurement is a pre-aggregated statisticValue representing five earlier measurements whose maximum was 70, whose minimum was 30, and whose sum was 250.

```
mon-put-data --metric-name RequestCount --namespace "MyService" --timestamp 2013-11-25T00:00:00.000Z --statisticValues "Sum=250,Minimum=30,Maximum=70,SampleCount=5"
```

### Example request
<a name="w2aab9c47c13b4"></a>

This example puts user-specific `RequestCount` test data in the `MyService` namespace. The user and stack name are stored as dimensions in order to distinguish this metric from the service-wide metric in the example above.

```
mon-put-data --metric-name RequestCount --namespace "MyService" --dimensions "User=SomeUser,Stack=Test" --timestamp 2013-11-25T00:00:00.000Z --value 50
```

## Related topics
<a name="w2aab9c47c15"></a>

### Download
<a name="w2aab9c47c15b2"></a>
+ [Set up the command line interface](SetupCLI.md)

### Related action
<a name="w2aab9c47c15b4"></a>
+ [PutMetricData](http://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricData.html)

### Related command
<a name="w2aab9c47c15b6"></a>
+  [mon-put-metric-alarm](cli-mon-put-metric-alarm.md)
