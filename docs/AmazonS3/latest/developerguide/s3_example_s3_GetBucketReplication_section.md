---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/developerguide/s3_example_s3_GetBucketReplication_section.html
---

# Use `GetBucketReplication` with an AWS SDK or CLI
<a name="s3_example_s3_GetBucketReplication_section"></a>

The following code examples show how to use `GetBucketReplication`.

------
#### [ CLI ]

**AWS CLI**
The following command retrieves the replication configuration for a bucket named `amzn-s3-demo-bucket`:

```
aws s3api get-bucket-replication --bucket {{amzn-s3-demo-bucket}}
```
Output:

```
{
    "ReplicationConfiguration": {
        "Rules": [
            {
                "Status": "Enabled",
                "Prefix": "",
                "Destination": {
                    "Bucket": "arn:aws:s3:::amzn-s3-demo-bucket-backup",
                    "StorageClass": "STANDARD"
                },
                "ID": "ZmUwNzE4ZmQ4tMjVhOS00MTlkLOGI4NDkzZTIWJjNTUtYTA1"
            }
        ],
        "Role": "arn:aws:iam::123456789012:role/s3-replication-role"
    }
}
```
+  For API details, see [GetBucketReplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-replication.html) in *AWS CLI Command Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3#code-examples).

```
    /**
     * Retrieves the replication details for the specified S3 bucket.
     *
     * @param s3Client           the S3 client used to interact with the S3 service
     * @param sourceBucketName   the name of the S3 bucket to retrieve the replication details for
     *
     * @throws S3Exception if there is an error retrieving the replication details
     */
    public static void getReplicationDetails(S3Client s3Client, String sourceBucketName) {
        GetBucketReplicationRequest getRequest = GetBucketReplicationRequest.builder()
            .bucket(sourceBucketName)
            .build();

        try {
            ReplicationConfiguration replicationConfig = s3Client.getBucketReplication(getRequest).replicationConfiguration();
            ReplicationRule rule = replicationConfig.rules().get(0);
            System.out.println("Retrieved destination bucket: " + rule.destination().bucket());
            System.out.println("Retrieved priority: " + rule.priority());
            System.out.println("Retrieved source-bucket replication rule status: " + rule.status());

        } catch (S3Exception e) {
            System.err.println("Failed to retrieve replication details: " + e.awsErrorDetails().errorMessage());
        }
    }
```
+  For API details, see [GetBucketReplication](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketReplication) in *AWS SDK for Java 2.x API Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Returns the replication configuration information set on the bucket named 'amzn-s3-demo-bucket'.**

```
Get-S3BucketReplication -BucketName amzn-s3-demo-bucket
```
+  For API details, see [GetBucketReplication](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Returns the replication configuration information set on the bucket named 'amzn-s3-demo-bucket'.**

```
Get-S3BucketReplication -BucketName amzn-s3-demo-bucket
```
+  For API details, see [GetBucketReplication](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

For a complete list of AWS SDK developer guides and code examples, see [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
