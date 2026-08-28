---
source_url: https://docs.aws.amazon.com/snowball/latest/developer-guide/working-s3-snow-buckets-get-bucket-s3-snow.html
---

AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

# Getting a bucket with Amazon S3 compatible storage on Snowball Edge on a Snowball Edge
<a name="working-s3-snow-buckets-get-bucket-s3-snow"></a>

The following example gets an Amazon S3 compatible storage on Snowball Edge bucket using the AWS CLI. To use this command, replace each user input placeholder with your own information.

```
aws s3control get-bucket --account-id {{123456789012}} --bucket amzn-s3-demo-bucket --endpoint-url https://{{s3ctrlapi-endpoint-ip}} --profile {{your-profile}}
```

For more information about this command, see [get-bucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-bucket.html) in the AWS CLI Command Reference.

The following Amazon S3 compatible storage on Snowball Edge example gets a bucket using the SDK for Java. For more information, see [GetBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucket.html) in the [Amazon Simple Storage Service API Reference](https://docs.aws.amazon.com/AmazonS3/latest/API/).

```
import com.amazonaws.services.s3control.model.*;

public void getBucket(String bucketName) {

    GetBucketRequest reqGetBucket = new GetBucketRequest()
            .withBucket(bucketName)
            .withAccountId(AccountId);

    GetBucketResult respGetBucket = s3ControlClient.getBucket(reqGetBucket);
    System.out.printf("GetBucket Response: %s%n", respGetBucket.toString());
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball Edge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
