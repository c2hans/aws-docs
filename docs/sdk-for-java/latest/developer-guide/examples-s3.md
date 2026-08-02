---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-s3.html
---

# Work with Amazon S3
<a name="examples-s3"></a>

This section provides background information for working with Amazon S3 by using the AWS SDK for Java 2.x. This section compliments the [Amazon S3 Java v2 examples](java_s3_code_examples.md) presented in the *Code examples* section of this guide.

## S3 clients in the AWS SDK for Java 2.x
<a name="s3-clients"></a>

The AWS SDK for Java 2.x provides different types of S3 clients. The following table shows the differences and can help you decide what is best for your use cases.

**Different flavors of Amazon S3 clients**

| S3 Client | Short description | When to use | Limitation/drawback |
| --- | --- | --- | --- |
| **AWS CRT-based S3 client**<br />Interface: [S3AsyncClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3AsyncClient.html)<br />Builder: [S3CrtAsyncClientBuilder](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3AsyncClient.html) | [See the AWS documentation website for more details](http://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-s3.html)See [Use a performant S3 client: AWS CRT-based S3 client](crt-based-s3-client.md). |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-s3.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-s3.html)  |
| **Java-based S3 async client *with* multipart enabled**<br />Interface: [S3AsyncClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3AsyncClient.html)<br />Builder: [S3AsyncClientBuilder](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3AsyncClientBuilder.html) | [See the AWS documentation website for more details](http://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-s3.html)See [Configure the Java-based S3 async client to use parallel transfers](s3-async-client-multipart.md). |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-s3.html)  | Less performant than the AWS CRT-based S3 client. |
| **Java-based S3 async client *without* multipart enabled**<br />Interface: [S3AsyncClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3AsyncClient.html)<br />Builder: [S3AsyncClientBuilder](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3AsyncClientBuilder.html) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-s3.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-s3.html)  | No performance optimization. |
| **Java-based S3 sync client**<br />Interface: [S3Client](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3Client.html)<br />Builder: [S3ClientBuilder](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3ClientBuilder.html) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-s3.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-s3.html)  | No performance optimization. |

**Note**
From version 2.18.x and onward, the AWS SDK for Java 2.x uses [virtual hosted-style addressing](https://docs.aws.amazon.com/AmazonS3/latest/userguide/VirtualHosting.html#virtual-hosted-style-access) when including an endpoint override. This applies as long as the bucket name is a valid DNS label.
Call the [https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3BaseClientBuilder.html#forcePathStyle(java.lang.Boolean](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3BaseClientBuilder.html#forcePathStyle(java.lang.Boolean) method with `true` in your client builder to force the client to use path-style addressing for buckets.
The following example shows a service client configured with an endpoint override and using path-style addressing.

```
S3Client client = S3Client.builder()
                          .region(Region.US_WEST_2)
                          .endpointOverride(URI.create("https://s3.us-west-2.amazonaws.com"))
                          .forcePathStyle(true)
                          .build();
```

**Topics**
+ [S3 clients in the SDK](#s3-clients)
+ [Uploading streams to S3](best-practices-s3-uploads.md)
+ [Pre-signed URLs](examples-s3-presign.md)
+ [Cross-Region access](s3-cross-region.md)
+ [Data integrity protection with checksums](s3-checksums.md)
+ [Use a performant S3 client](crt-based-s3-client.md)
+ [Configure parallel transfer support](s3-async-client-multipart.md)
+ [Transfer files and directories](transfer-manager.md)
+ [S3 Event Notifications](examples-s3-event-notifications.md)
