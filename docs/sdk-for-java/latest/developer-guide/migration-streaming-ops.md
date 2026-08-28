---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-streaming-ops.html
---

# Streaming operation differences between 1.x and 2.x of the AWS SDK for Java
<a name="migration-streaming-ops"></a>

Streaming operations, such as Amazon S3 `getObject` and `putObject` methods, support non-blocking I/O in version 2.x of the SDK. As a result, the request and response model objects no longer take an `InputStream` as a parameter. Instead, for synchronous requests the request object accepts `RequestBody`, which is a stream of bytes. The asynchronous equivalent accepts an `AsyncRequestBody`.

**Example of Amazon S3 `putObject` operation in 1.x**

```
s3client.putObject(BUCKET, KEY, new File(file_path));
```

**Example of Amazon S3 `putObject` operation in 2.x**

```
s3client.putObject(PutObjectRequest.builder()
                                 .bucket(BUCKET)
                                 .key(KEY)
                                 .build(),
                 RequestBody.of(Paths.get("myfile.in")));
```

A streaming response object accepts a `ResponseTransformer` for synchronous clients and a `AsyncResponseTransformer` for asynchronous clients in V2.

**Example of Amazon S3 `getObject` operation in 1.x**

```
S3Object o = s3.getObject(bucket, key);
S3ObjectInputStream s3is = o.getObjectContent();
FileOutputStream fos = new FileOutputStream(new File(key));
```

**Example of Amazon S3 `getObject` operation in 2.x**

```
s3client.getObject(GetObjectRequest.builder().bucket(bucket).key(key).build(),
		ResponseTransformer.toFile(Paths.get("key")));
```

In the SDK for Java 2.x, streaming response operations have an `AsBytes` method to load the response into memory and simplify common type conversions in-memory.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
