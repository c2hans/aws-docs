---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/batch_example_batch_Hello_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Hello AWS Batch
<a name="batch_example_batch_Hello_section"></a>

The following code examples show how to get started using AWS Batch.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/batch#code-examples).

```
import software.amazon.awssdk.core.client.config.ClientOverrideConfiguration;
import software.amazon.awssdk.core.retry.RetryPolicy;
import software.amazon.awssdk.http.async.SdkAsyncHttpClient;
import software.amazon.awssdk.http.nio.netty.NettyNioAsyncHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.batch.BatchAsyncClient;
import software.amazon.awssdk.services.batch.model.JobStatus;
import software.amazon.awssdk.services.batch.model.JobSummary;
import software.amazon.awssdk.services.batch.model.ListJobsRequest;
import software.amazon.awssdk.services.batch.paginators.ListJobsPublisher;
import java.time.Duration;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.CompletableFuture;

public class HelloBatch {
    private static BatchAsyncClient batchClient;

    public static void main(String[] args) {
        List<JobSummary> jobs = listJobs("my-job-queue");
        jobs.forEach(job ->
            System.out.printf("Job ID: %s, Job Name: %s, Job Status: %s%n",
                job.jobId(), job.jobName(), job.status())
        );
    }

    public static List<JobSummary> listJobs(String jobQueue) {
        if (jobQueue == null || jobQueue.isEmpty()) {
            throw new IllegalArgumentException("Job queue cannot be null or empty");
        }

        ListJobsRequest listJobsRequest = ListJobsRequest.builder()
            .jobQueue(jobQueue)
            .jobStatus(JobStatus.SUCCEEDED)
            .build();

        List<JobSummary> jobSummaries = new ArrayList<>();
        ListJobsPublisher listJobsPaginator = getAsyncClient().listJobsPaginator(listJobsRequest);
        CompletableFuture<Void> future = listJobsPaginator.subscribe(response -> {
            jobSummaries.addAll(response.jobSummaryList());
        });

        future.join();
        return jobSummaries;
    }

    private static BatchAsyncClient getAsyncClient() {
        SdkAsyncHttpClient httpClient = NettyNioAsyncHttpClient.builder()
            .maxConcurrency(100)  // Increase max concurrency to handle more simultaneous connections.
            .connectionTimeout(Duration.ofSeconds(60))  // Set the connection timeout.
            .readTimeout(Duration.ofSeconds(60))  // Set the read timeout.
            .writeTimeout(Duration.ofSeconds(60))  // Set the write timeout.
            .build();

        ClientOverrideConfiguration overrideConfig = ClientOverrideConfiguration.builder()
            .apiCallTimeout(Duration.ofMinutes(2))  // Set the overall API call timeout.
            .apiCallAttemptTimeout(Duration.ofSeconds(90))  // Set the individual call attempt timeout.
            .retryPolicy(RetryPolicy.builder()  // Add a retry policy to handle transient errors.
                .numRetries(3)  // Number of retry attempts.
                .build())
            .build();

        if (batchClient == null) {
            batchClient = BatchAsyncClient.builder()
                .region(Region.US_EAST_1)
                .httpClient(httpClient)
                .overrideConfiguration(overrideConfig)
                .build();
        }
        return batchClient;
    }
}
```
+  For API details, see [listJobsPaginator](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/listJobsPaginator) in *AWS SDK for Java 2.x API Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/batch#code-examples).

```
def hello_batch() -> None:
    """
    Lists compute environments using the AWS Batch service.
    """
    batch_client = boto3.client("batch")
    print("Hello, AWS Batch! Let's list your compute environments:\n")
    try:
        response = batch_client.describe_compute_environments()
        environments = response.get("computeEnvironments", [])
        if environments:
            print(f"Found {len(environments)} compute environment(s):")
            for env in environments:
                print(
                    f"  - Name: {env['computeEnvironmentName']} | "
                    f"Type: {env.get('type', 'N/A')} | "
                    f"State: {env.get('state', 'N/A')} | "
                    f"Status: {env.get('status', 'N/A')}"
                )
        else:
            print("No compute environments found in your account.")
    except ClientError as err:
        logger.error(
            "Error listing compute environments: %s",
            err.response["Error"]["Message"],
        )
        raise

    print("\nHello example complete.")
```
+  For API details, see [listJobsPaginator](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/listJobsPaginator) in *AWS SDK for Python (Boto3) API Reference*.

------
