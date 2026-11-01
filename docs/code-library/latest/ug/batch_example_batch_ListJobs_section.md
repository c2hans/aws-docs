---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/batch_example_batch_ListJobs_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListJobs` with an AWS SDK or CLI
<a name="batch_example_batch_ListJobs_section"></a>

The following code examples show how to use `ListJobs`.

------
#### [ CLI ]

**AWS CLI**
**Example 1: To list running jobs**
The following `list-jobs` example lists the running jobs in the HighPriority job queue.

```
aws batch list-jobs \
    --job-queue {{HighPriority}}
```
Output:

```
{
    "jobSummaryList": [
        {
            "jobName": "example",
            "jobId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
        }
    ]
}
```
For more information, see [Job states](https://docs.aws.amazon.com/batch/latest/userguide/job_states.html) in the *AWS Batch User Guide*.
**Example 2: To list submitted jobs**
The following `list-jobs` example lists jobs in the HighPriority job queue that are in the SUBMITTED job status.

```
aws batch list-jobs \
    --job-queue {{HighPriority}} \
    --job-status {{SUBMITTED}}
```
Output:

```
{
    "jobSummaryList": [
        {
            "jobName": "example",
            "jobId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
        }
    ]
}
```
For more information, see [Job states](https://docs.aws.amazon.com/batch/latest/userguide/job_states.html) in the *AWS Batch User Guide*.
+  For API details, see [ListJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/list-jobs.html) in *AWS CLI Command Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/batch#code-examples).

```
    def list_jobs(self, job_queue: str, job_status: str = "SUCCEEDED") -> list:
        """
        Lists jobs in a job queue with a specific status.

        :param job_queue: The job queue name or ARN.
        :param job_status: The job status to filter by (default SUCCEEDED).
        :return: A list of job summary dictionaries.
        """
        try:
            paginator = self.batch_client.get_paginator("list_jobs")
            job_summaries = []
            for page in paginator.paginate(jobQueue=job_queue, jobStatus=job_status):
                job_summaries.extend(page.get("jobSummaryList", []))
            logger.info(
                "Listed %d %s job(s) in queue %s.",
                len(job_summaries),
                job_status,
                job_queue,
            )
            return job_summaries
        except ClientError as err:
            logger.error(
                "Error listing jobs in queue %s: %s",
                job_queue,
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [ListJobs](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/ListJobs) in *AWS SDK for Python (Boto3) API Reference*.

------
