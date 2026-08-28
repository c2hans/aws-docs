---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-serialization-changes.html
---

# Serialization differences between 1.x and 2.x of the AWS SDK for Java
<a name="migration-serialization-changes"></a>

## List objects to request parameters difference
<a name="serialization-diffs-list-obj-to-req-param"></a>

The SDK for Java v1.x and v2.x differ in how they serialize List objects to request parameters.

The SDK for Java 1.x does not serialize an empty list, whereas the SDK for Java 2.x serializes an empty list as an empty parameter.

For example, consider a service with a `SampleOperation` that takes a `SampleRequest`. The `SampleRequest` accepts two parameters—a String type `str1` and List type `listParam`—as shown in the following examples.

**Example of `SampleOperation` in 1.x**

```
SampleRequest v1Request = new SampleRequest()
    .withStr1("TestName");

sampleServiceV1Client.sampleOperation(v1Request);
```
Wire-level logging shows that the `listParam` parameter is not serialized.

```
Action=SampleOperation&Version=2011-01-01&str1=TestName
```

**Example of `SampleOperation` in 2.x**

```
sampleServiceV2Client.sampleOperation(b -> b
    .str1("TestName"));
```
Wire-level logging shows that the `listParam` parameter is serialized with no value.

```
Action=SampleOperation&Version=2011-01-01&str1=TestName&listParam=
```

## POJOs in V1 compared to builders in V2
<a name="serialization-json-objects"></a>

Because the V1 SDK for Java uses mutable POJO classes, serialization and deserialization libraries—such as [Jackson](https://github.com/FasterXML/jackson-docs)—can use model objects directly.

The V2 SDK for Java, by contrast, uses immutable model objects. You must use an intermediate builder to perform de/serialization.

The following example shows the differences between de/serializing a `headBucket` API call with V1 and V2 using a Jackson `ObjectMapper`.

```
    public void sendRequest() throws IOException {
        final String bucketName = "amzn-s3-demo-bucket";
        final ObjectMapper mapper = new ObjectMapper();

        // V1 uses POJOs to serialize and deserialize.
        final AmazonS3 v1S3Client = AmazonS3ClientBuilder.defaultClient();
        HeadBucketResult resultV1 = v1S3Client.headBucket(
            new HeadBucketRequest(bucketName));

        String v1Serialized = mapper.writeValueAsString(resultV1);

        HeadBucketResult deserializedV1 = mapper.readValue(v1Serialized, HeadBucketResult.class);

        // V2 uses builders to serialize and deserialize.
        S3Client v2S3Client = S3Client.create();
        HeadBucketResponse v2Response = v2S3Client.headBucket(
            b -> b.bucket(bucketName));

        String v2Serialized = mapper.writeValueAsString(
            v2Response.toBuilder());

        HeadBucketResponse v2Deserialized = mapper.readValue(
            v2Serialized, HeadBucketResponse.serializableBuilderClass())
            .build();
    }
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
