---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/example_cloudwatch-logs_CreateLogStream_section.html
---

# Use `CreateLogStream` with an AWS SDK or CLI
<a name="example_cloudwatch-logs_CreateLogStream_section"></a>

The following code examples show how to use `CreateLogStream`.

------
#### [ .NET ]

**SDK for .NET**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/CloudWatchLogs#code-examples).

```
    using System;
    using System.Threading.Tasks;
    using Amazon.CloudWatchLogs;
    using Amazon.CloudWatchLogs.Model;

    /// <summary>
    /// Shows how to create an Amazon CloudWatch Logs stream for a CloudWatch
    /// log group.
    /// </summary>
    public class CreateLogStream
    {
        public static async Task Main()
        {
            // This client object will be associated with the same AWS Region
            // as the default user on this system. If you need to use a
            // different AWS Region, pass it as a parameter to the client
            // constructor.
            var client = new AmazonCloudWatchLogsClient();
            string logGroupName = "cloudwatchlogs-example-loggroup";
            string logStreamName = "cloudwatchlogs-example-logstream";

            var request = new CreateLogStreamRequest
            {
                LogGroupName = logGroupName,
                LogStreamName = logStreamName,
            };

            var response = await client.CreateLogStreamAsync(request);

            if (response.HttpStatusCode == System.Net.HttpStatusCode.OK)
            {
                Console.WriteLine($"{logStreamName} successfully created for {logGroupName}.");
            }
            else
            {
                Console.WriteLine("Could not create stream.");
            }
        }
    }
```
+  For API details, see [CreateLogStream](https://docs.aws.amazon.com/goto/DotNetSDKV3/logs-2014-03-28/CreateLogStream) in *AWS SDK for .NET API Reference*.

------
#### [ CLI ]

**AWS CLI**
The following command creates a log stream named `20150601` in the log group `my-logs`:

```
aws logs create-log-stream --log-group-name {{my-logs}} --log-stream-name {{20150601}}
```
+  For API details, see [CreateLogStream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/create-log-stream.html) in *AWS CLI Command Reference*.

------

For a complete list of AWS SDK developer guides and code examples, see [Using CloudWatch Logs with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
