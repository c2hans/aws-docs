---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/batch_example_batch_DescribeJobs_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeJobs` with an AWS SDK or CLI
<a name="batch_example_batch_DescribeJobs_section"></a>

The following code examples show how to use `DescribeJobs`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Learn the basics](batch_example_batch_Scenario_section.md)
+  [Getting started with batch processing and serverless containers](batch_example_fargate_GettingStarted_section.md)

------
#### [ CLI ]

**AWS CLI**
**To describe a job**
The following `describe-jobs` example describes a job with the specified job ID.

```
aws batch describe-jobs \
    --jobs {{bcf0b186-a532-4122-842e-2ccab8d54efb}}
```
Output:

```
{
    "jobs": [
        {
            "status": "SUBMITTED",
            "container": {
                "mountPoints": [],
                "image": "busybox",
                "environment": [],
                "vcpus": 1,
                "command": [
                    "sleep",
                    "60"
                ],
                "volumes": [],
                "memory": 128,
                "ulimits": []
            },
            "parameters": {},
            "jobDefinition": "arn:aws:batch:us-east-1:012345678910:job-definition/sleep60:1",
            "jobQueue": "arn:aws:batch:us-east-1:012345678910:job-queue/HighPriority",
            "jobId": "bcf0b186-a532-4122-842e-2ccab8d54efb",
            "dependsOn": [],
            "jobName": "example",
            "createdAt": 1480483387803
        }
    ]
}
```
+  For API details, see [DescribeJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/describe-jobs.html) in *AWS CLI Command Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/batch#code-examples).

```
    /**
     * Asynchronously retrieves the status of a specific job.
     *
     * @param jobId the ID of the job to retrieve the status for
     * @return a CompletableFuture that completes with the job status
     */
    public CompletableFuture<String> describeJobAsync(String jobId) {
        DescribeJobsRequest describeJobsRequest = DescribeJobsRequest.builder()
            .jobs(jobId)
            .build();

        CompletableFuture<DescribeJobsResponse> responseFuture = getAsyncClient().describeJobs(describeJobsRequest);
        return responseFuture.whenComplete((response, ex) -> {
            if (ex != null) {
                throw new RuntimeException("Unexpected error occurred: " + ex.getMessage(), ex);
            }
        }).thenApply(response -> response.jobs().get(0).status().toString());
    }
```
+  For API details, see [DescribeJobs](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/DescribeJobs) in *AWS SDK for Java 2.x API Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/batch#code-examples).

```
    def describe_jobs(self, job_ids: list) -> list:
        """
        Describes one or more jobs.

        :param job_ids: A list of job IDs to describe.
        :return: A list of job detail dictionaries.
        """
        try:
            response = self.batch_client.describe_jobs(jobs=job_ids)
            jobs = response.get("jobs", [])
            logger.info("Described %d job(s).", len(jobs))
            return jobs
        except ClientError as err:
            logger.error(
                "Error describing jobs: %s",
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [DescribeJobs](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/DescribeJobs) in *AWS SDK for Python (Boto3) API Reference*.

------
