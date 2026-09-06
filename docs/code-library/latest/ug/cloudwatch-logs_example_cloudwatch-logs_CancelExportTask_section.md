---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloudwatch-logs_example_cloudwatch-logs_CancelExportTask_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CancelExportTask` with an AWS SDK
<a name="cloudwatch-logs_example_cloudwatch-logs_CancelExportTask_section"></a>

The following code example shows how to use `CancelExportTask`.

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
    /// Shows how to cancel an Amazon CloudWatch Logs export task.
    /// </summary>
    public class CancelExportTask
    {
        public static async Task Main()
        {
            // This client object will be associated with the same AWS Region
            // as the default user on this system. If you need to use a
            // different AWS Region, pass it as a parameter to the client
            // constructor.
            var client = new AmazonCloudWatchLogsClient();
            string taskId = "exampleTaskId";

            var request = new CancelExportTaskRequest
            {
                TaskId = taskId,
            };

            var response = await client.CancelExportTaskAsync(request);

            if (response.HttpStatusCode == System.Net.HttpStatusCode.OK)
            {
                Console.WriteLine($"{taskId} successfully canceled.");
            }
            else
            {
                Console.WriteLine($"{taskId} could not be canceled.");
            }
        }
    }
```
+  For API details, see [CancelExportTask](https://docs.aws.amazon.com/goto/DotNetSDKV3/logs-2014-03-28/CancelExportTask) in *AWS SDK for .NET API Reference*.

------
