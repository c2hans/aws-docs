---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/waiters.html
---

# Waiters
<a name="waiters"></a>

Waiters are a client-side abstraction used to poll a resource until a desired state is reached, or until it is determined that the resource will not enter the desired state. This is a common task when working with services that are eventually consistent, like Amazon Simple Storage Service (Amazon S3), or services that asynchronously create resources, like Amazon EC2.

Writing logic to continuously poll the status of a resource can be cumbersome and error-prone. The goal of waiters is to move this responsibility out of customer code and into the AWS SDK for Kotlin, which has in-depth knowledge of the timing aspects for the AWS operation.

**Note**
The following examples use Amazon S3. However, the concepts are the same for any AWS service that has one or more waiters defined. All extensions are defined in the `aws.sdk.kotlin.services.<service>.waiters` package (such as `aws.sdk.kotlin.services.dynamodb.waiters`). They also follow a standard naming convention (`waitUntil<Condition>`).

The following code example shows the use of a waiter function that allows you to avoid writing polling logic.

 **Imports**

```
import aws.sdk.kotlin.services.s3.S3Client
import aws.sdk.kotlin.services.s3.waiters.waitUntilBucketExists
```

 **Code**

```
val s3 = S3Client.fromEnvironment()

// This initiates creating an S3 bucket and potentially returns before the bucket exists.
s3.createBucket { bucket = "amzn-s3-demo-bucket" }

// When this function returns, the bucket either exists or an exception
// is thrown.
s3.waitUntilBucketExists { bucket = "amzn-s3-demo-bucket" }

// The bucket now exists.
```

**Note**
Each wait method returns an `Outcome` instance that can be used to get at the final response that corresponds to reaching the desired condition. An outcome also contains additional details like the number of attempts made to reach the desired state.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Kotlin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-kotlin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
