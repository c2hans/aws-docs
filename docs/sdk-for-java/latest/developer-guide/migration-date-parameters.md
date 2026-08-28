---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-date-parameters.html
---

# Date parameter changes
<a name="migration-date-parameters"></a>

In version 1, many operations accepted `java.util.Date` objects for time-based parameters. In version 2, these operations use `java.time.Instant` objects instead.

You can convert `Date` parameters automatically using the [migration tool](migration-tool.md), or you can convert them manually by calling the `toInstant()` method on your `Date` object.

**Example - Generate a presigned URL with an expiration date in version 1**

```
// Generate a presigned URL that expires at a specific date
Date expiration = new Date(System.currentTimeMillis() + 3600000); // 1 hour from now
URL presignedUrl = s3Client.generatePresignedUrl(bucketName, keyName, expiration);
```

**Example - Generate a presigned URL with an expiration instant in version 2**

```
// Generate a presigned URL that expires at a specific instant
Date expiration = new Date(System.currentTimeMillis() + 3600000); // 1 hour from now
PresignedGetObjectRequest presignedRequest = presigner.presignGetObject(
    GetObjectPresignRequest.builder()
        .getObjectRequest(GetObjectRequest.builder()
            .bucket(bucketName)
            .key(keyName)
            .build())
        .signatureDuration(Duration.between(Instant.now(), expiration.toInstant()))
        .build());
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
