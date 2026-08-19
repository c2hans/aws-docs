---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-s3-client.html
---

# S3 client differences between version 1 and version 2 of the AWS SDK for Java
<a name="migration-s3-client"></a>

In this topic, the differences between the S3 clients in version 1 and version 2 of SDK for Java are organized by how the [migration tool](migration-tool.md) can automate the migration. The tool supports migration of most methods from V1 to V2, but some methods require manual migration. In additional to S3 client methods, some S3 V1 classes do not have a direct V2 equivalent requiring you to manually migrate them.

**Contents**
+ [Example V1 methods supported by the migration tool](#methods-tool-migration)
  + [`putObject`](#V1-V2-putobject)
  + [`getObject`](#V1-V2-getobject)
  + [`getObject` to a file](#V1-V2-getobject-to-file)
+ [V1 methods that require manual migration](#s3-methods-manual-migration)
  + [`getObject` using `S3ObjectId`](#V1s-getObject-using-V1s-S3ObjectId)
  + [`getETag` using `ObjectMetadata`](#V1s-ObjectMetadata-using-V1s-getETag)
  + [`listNextBatchOfObjects`](#V1-listNextBatchOfObjects)
  + [`listNextBatchOfVersions`](#V1-listNextBatchOfVersions)
  + [`selectObjectContent`](#V1-selectObjectContent)
  + [`setBucketAcl`](#V1-setBucketAcl)
  + [`setObjectAcl`](#V1-setObjectAcl)
  + [`initiateMultipartUpload`](#V1-initiateMultipartUpload)
    + [Example migration](#V1-initiateMultipartUpload-migration-ex)
    + [Implementation differences](#V1-initiateMultipartUpload-impl-diffs)
  + [`setRegion`](#V1-setRegion)
  + [`setS3ClientOptions(S3ClientOptions clientOptions)`](#V1-setS3ClientOptions)
  + [`setBucketLoggingConfiguration`](#V1-setBucketLoggingConfiguration)
  + [`setBucketLifecycleConfiguration`](#V1-setBucketLifecycleConfiguration)
  + [`setBucketTaggingConfiguration`](#V1-setBucketTaggingConfiguration)
+ [V1 classes that require manual migration](#s3-classes-manual-migration)
  + [`AccessControlList`](#V1-AccessControlList)
  + [`CannedAccessControlList`](#V1-CannedAccessControlList)
  + [`BucketNotificationConfiguration`](#V1-BucketNotificationConfiguration)
  + [`MultiFactorAuthentication`](#V1-MultifactorAuthentication)

## Example V1 methods supported by the migration tool
<a name="methods-tool-migration"></a>

The migration tool automatically migrates most methods from V1 to V2. The `putObject` and `getObject` methods are two examples.

### `putObject`
<a name="V1-V2-putobject"></a>

```
// SDK V1
s3Client.putObject("amzn-s3-demo-bucket", "my-key", "Hello World!");

// SDK V2
s3Client.putObject(req -> req
    .bucket("amzn-s3-demo-bucket")
    .key("my-key"),
    RequestBody.fromString("Hello World!"));
```

### `getObject`
<a name="V1-V2-getobject"></a>

```
// SDK V1
S3Object object = s3Client.getObject("amzn-s3-demo-bucket", "my-key");
InputStream content = object.getObjectContent();

// SDK V2
ResponseInputStream<GetObjectResponse> response = s3Client.getObject(req -> req
    .bucket("amzn-s3-demo-bucket")
    .key("my-key"));
```

### `getObject` to a file
<a name="V1-V2-getobject-to-file"></a>

```
// SDK V1
// V1 automatically creates parent directories if they don't exist.
ObjectMetadata metadata = s3Client.getObject(
    new GetObjectRequest("amzn-s3-demo-bucket", "my-key"),
    new File("/path/to/parent/dir/my-file.txt"));

// SDK V2
// V2 does NOT auto-create parent directories. Ensure they exist before calling getObject.
Files.createDirectories(Paths.get("/path/to/parent/dir"));
s3Client.getObject(
    req -> req.bucket("amzn-s3-demo-bucket").key("my-key"),
    ResponseTransformer.toFile(Paths.get("/path/to/parent/dir/my-file.txt")));
```

**Important**
Unlike SDK V1, SDK V2's `ResponseTransformer.toFile()` does not automatically create parent directories. If the parent directory does not exist, the SDK throws a `NoSuchFileException`. Call `Files.createDirectories()` before downloading if the parent directories might not exist.

## V1 methods that require manual migration
<a name="s3-methods-manual-migration"></a>

You need to manually migrate the following V1 S3 client methods. When you use the migration tool, you see a comment in the V2 output Java file that directs you to this topic.

### V1's `getObject` using V1's `S3ObjectId` to V2's `GetObjectRequest.builder()`
<a name="V1s-getObject-using-V1s-S3ObjectId"></a>

```
// SDK V1
AmazonS3 s3ClientV1 = AmazonS3ClientBuilder.standard()
        .withRegion(Regions.US_WEST_2)
        .build();

S3ObjectId s3ObjectId = new S3ObjectId(
    "amzn-s3-demo-bucket",
    "object-key",
    "abc123version"
);

GetObjectRequest getRequest= new GetObjectRequest(s3ObjectId);
S3Object s3ObjectVersioned = s3Client.getObject(getRequest);

// SDK V2
// V2 does not include a 'S3ObjectId' class. V2 uses the request builder pattern
// to supply the bucket, key, and version parameters.
S3Client s3Client = S3Client.builder()
    .region(Region.US_WEST_2)
    .build();

GetObjectRequest getRequest = GetObjectRequest.builder()
    .bucket("amzn-s3-demo-bucket")
    .key("object-key")
    .versionId("abc123version")
    .build();

ResponseInputStream<GetObjectResponse> response = s3Client.getObject(getRequest);
```

### V1's `getETag()` using V1's `ObjectMetadata` to V2's `GetObjectResponse.eTag()`
<a name="V1s-ObjectMetadata-using-V1s-getETag"></a>

```
// SDK V1
AmazonS3 s3ClientV1 = AmazonS3ClientBuilder.standard()
    .withRegion(Regions.US_WEST_2)
    .build();

S3Object object = s3ClientV1.getObject("amzn-s3-demo-bucket", "my-key");

// Double quotes are removed by the S3 client.
System.out.println(object.getObjectMetadata().getETag());

// SDK V2
S3Client s3ClientV2 = S3Client.builder()
        .region(Region.US_WEST_2)
        .build();

ResponseInputStream<GetObjectResponse> response = s3ClientV2.getObject(
        req -> req.bucket("amzn-s3-demo-bucket").key("my-key"));

// Double quotes are *NOT* removed. This is the unchanged ETag value as S3 sent it.
System.out.println(response.response().eTag());
```

### V1's `listNextBatchOfObjects` to V2's `listObjectsV2Paginator`
<a name="V1-listNextBatchOfObjects"></a>

```
// SDK V1
AmazonS3 s3ClientV1 = AmazonS3ClientBuilder.standard()
    .withRegion(Regions.US_WEST_2)
    .build();

ObjectListing objectListing = s3ClientV1.listObjects("bucket-name");
while (objectListing.isTruncated()) {
    objectListing = s3ClientV1.listNextBatchOfObjects(objectListing);
    for (S3ObjectSummary summary : objectListing.getObjectSummaries()) {
        System.out.println(summary.getKey());
    }
}

// SDK V2
S3Client s3ClientV2 = S3Client.builder()
    .region(Region.US_WEST_2)
    .build();

ListObjectsV2Request request = ListObjectsV2Request.builder()
    .bucket("bucket-name")
    .build();

// V2 returns a paginator.
ListObjectsV2Iterable responses = s3Client.listObjectsV2Paginator(request);

for (ListObjectsV2Response page : responses) {
    page.contents().forEach(content -> {
        System.out.println(content.key());
    });
}
```

### V1's `listNextBatchOfVersions` to V2's `listObjectVersionsPaginator`
<a name="V1-listNextBatchOfVersions"></a>

```
// SDK V1
AmazonS3 s3ClientV1 = AmazonS3ClientBuilder.standard()
    .withRegion(Regions.US_WEST_2)
    .build();

VersionListing versionListing = s3ClientV1.listVersions("bucket-name", "prefix");
while (versionListing.isTruncated()) {
    versionListing = s3ClientV1.listNextBatchOfVersions(versionListing);
    for (S3VersionSummary version : versionListing.getVersionSummaries()) {
        System.out.println(version.getKey() + " " + version.getVersionId());
    }
}

// SDK V2
S3Client s3ClientV2 = S3Client.builder()
    .region(Region.US_WEST_2)
    .build();

ListObjectVersionsRequest request = ListObjectVersionsRequest.builder()
    .bucket("bucket-name")
    .prefix("prefix")
    .build();

// V2 returns a paginator.
ListObjectVersionsIterable responses = s3ClientV2.listObjectVersionsPaginator(request);

for (ListObjectVersionsResponse page : responses) {
    page.versions().forEach(version -> {
        System.out.println(version.key() + " " + version.versionId());
    });
}
```

### `selectObjectContent`
<a name="V1-selectObjectContent"></a>

```
// SDK V1
AmazonS3 s3ClientV1 = AmazonS3ClientBuilder.standard()
    .withRegion(Regions.US_WEST_2)
    .build();

SelectObjectContentRequest request = new SelectObjectContentRequest()
    .withBucket("bucket-name")
    .withKey("object-key")
    .withExpression("select * from S3Object")
    .withExpressionType(ExpressionType.SQL)

SelectObjectContentResult result = s3ClientV1.selectObjectContent(request);
InputStream resultInputStream = result.getPayload().getRecordsInputStream();

// SDK V2
// In V2, 'selectObjectContent()' is available only on the S3AsyncClient.
// V2 handles responses using an event-based 'SelectObjectContentEventStream'.
S3AsyncClient s3ClientV2 = S3AsyncClient.builder()
    .region(Region.US_WEST_2)
    .build();

SelectObjectContentRequest request = SelectObjectContentRequest.builder()
    .bucket("bucket-name")
    .key("object-key")
    .expression("select * from S3Object")
    .expressionType(ExpressionType.SQL)
    .build();

SelectObjectContentResponseHandler handler = new SelectObjectContentResponseHandler() {
    // Implement the required abstract methods such as 'onEventStream()'.
};

CompletableFuture<Void> future = s3ClientV2.selectObjectContent(request, handler);
// The 'SelectObjectContentResponseHandler' implementation processes the results.
```

### V1's `setBucketAcl` to V2's `acl` method on `PutBucketAclRequest.builder()`
<a name="V1-setBucketAcl"></a>

```
// SDK V1
AmazonS3 s3ClientV1 = AmazonS3ClientBuilder.standard()
    .withRegion(Regions.US_WEST_2)
    .build();

AccessControlList acl = new AccessControlList();
acl.grantPermission(GroupGrantee.AllUsers, Permission.Read);
s3ClientV1.setBucketAcl("bucket-name", acl);

// SDK V2
S3Client s3ClientV2 = S3Client.builder()
    .region(Region.US_WEST_2)
    .build();

PutBucketAclRequest request = PutBucketAclRequest.builder()
    .bucket("bucket-name")
    .acl(BucketCannedACL.PRIVATE)
    .build();

s3ClientV2.putBucketAcl(request);
```

### V1's `setObjectAcl` to V2's `acl` method on `PutObjectAclRequest.builder()`
<a name="V1-setObjectAcl"></a>

```
// SDK V1
AmazonS3 s3ClientV1 = AmazonS3ClientBuilder.standard()
    .withRegion(Regions.US_WEST_2)
    .build();

AccessControlList acl = new AccessControlList();
acl.grantPermission(GroupGrantee.AllUsers, Permission.Read);
s3ClientV1.setObjectAcl("bucket-name", "object-key", acl);

// SDK V2
S3Client s3ClientV2 = S3Client.builder()
    .region(Region.US_WEST_2)
    .build();

PutObjectAclRequest request = PutObjectAclRequest.builder()
    .bucket("bucket-name")
    .key("object-key")
    .acl(ObjectCannedACL.PRIVATE)
    .build();

s3ClientV2.putObjectAcl(request);
```

### V1's `initiateMultipartUpload` to V2's `createMultipartUpload`
<a name="V1-initiateMultipartUpload"></a>

#### Example migration
<a name="V1-initiateMultipartUpload-migration-ex"></a>

```
// SDK V1
AmazonS3 s3ClientV1 = AmazonS3ClientBuilder.standard()
    .withRegion(Regions.US_WEST_2)
    .build();

ObjectMetadata metadata = new ObjectMetadata();
metadata.setContentType("application/zip");
metadata.addUserMetadata("mykey", "myvalue");

InitiateMultipartUploadRequest initRequest = new InitiateMultipartUploadRequest(
    "bucket-name",
    "object-key",
    metadata
);

InitiateMultipartUploadResult initResponse = s3ClientV1.initiateMultipartUpload(initRequest);
String uploadId = initResponse.getUploadId();

// SDK V2
// V1 uses ObjectMetadata methods, whereas V2 uses a simple Map.
S3Client s3ClientV2 = S3Client.builder()
    .region(Region.US_WEST_2)
    .build();

CreateMultipartUploadRequest createMultipartRequest = CreateMultipartUploadRequest.builder()
    .bucket("amzn-s3-demo-bucket")
    .key("object-key")
    .contentType("application/zip")
    .metadata(Collections.singletonMap("mykey", "myvalue"))
    .build();

CreateMultipartUploadResponse response = s3ClientV2.createMultipartUpload(createMultipartRequest);
String uploadId = response.uploadId();
```

#### Implementation differences
<a name="V1-initiateMultipartUpload-impl-diffs"></a>

The default `Content-Type` header value for the following methods differ as shown in the following table.

| SDK version | Method | Default `Content-Type` value |
| --- | --- | --- |
| version 1 | [initiateMultipartUpload](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/AmazonS3Client.html#initiateMultipartUpload-com.amazonaws.services.s3.model.InitiateMultipartUploadRequest-) | application/octet-stream |
| version 2 | [createMultipartUpload](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3AsyncClient.html#createMultipartUpload(software.amazon.awssdk.services.s3.model.CreateMultipartUploadRequest)) | binary/octet-stream |

### V1's `setRegion` to V2's `region` method on client builder
<a name="V1-setRegion"></a>

```
// SDK V1
AmazonS3 s3ClientV1 = AmazonS3ClientBuilder.standard().build();
s3ClientV1.setRegion(Region.getRegion(Regions.US_WEST_2));

// SDK V2
S3Client s3ClientV2 = S3Client.builder()
    .region(Region.US_WEST_2)
    .build();
```

### V1's `setS3ClientOptions(S3ClientOptions clientOptions)`
<a name="V1-setS3ClientOptions"></a>

Instead of using a single `S3ClientOptions` object with the `setS3ClientOptions` method, V2 provides methods on the client builder to set options.

### V1's `setBucketLoggingConfiguration` to V2's `putBucketLogging`
<a name="V1-setBucketLoggingConfiguration"></a>

```
// SDK V1
AmazonS3 s3ClientV1 = AmazonS3ClientBuilder.standard()
    .withRegion(Regions.US_WEST_2)
    .build();

BucketLoggingConfiguration loggingConfig = new BucketLoggingConfiguration();
loggingConfig.setDestinationBucketName("log-bucket");

SetBucketLoggingConfigurationRequest request = new SetBucketLoggingConfigurationRequest(
    "amzn-s3-demo-source-bucket",
    loggingConfig
);

s3ClientV1.setBucketLoggingConfiguration(request);

// SDK V2
// In V2, V1's 'BucketLoggingConfiguration' is replaced by 'BucketLoggingStatus'
// and 'LoggingEnabled'.
S3Client s3ClientV2 = S3Client.builder()
    .region(Region.US_WEST_2)
    .build();

LoggingEnabled loggingEnabled = LoggingEnabled.builder()
    .targetBucket("log-bucket")
    .build();

BucketLoggingStatus loggingStatus = BucketLoggingStatus.builder()
    .loggingEnabled(loggingEnabled)
    .build();

PutBucketLoggingRequest request = PutBucketLoggingRequest.builder()
    .bucket("amzn-s3-demo-source-bucket")
    .bucketLoggingStatus(loggingStatus)
    .build();

s3ClientV2.putBucketLogging(request);
```

### V1's `setBucketLifecycleConfiguration` to V2's `putBucketLifecycleConfiguration`
<a name="V1-setBucketLifecycleConfiguration"></a>

```
// SDK V1
BucketLifecycleConfiguration.Rule rule = new BucketLifecycleConfiguration.Rule()
    .withId("Archive and Delete Rule")
    .withPrefix("documents/")
    .withStatus(BucketLifecycleConfiguration.ENABLED)
    .withTransitions(Arrays.asList(
        new Transition()
            .withDays(30)
            .withStorageClass(StorageClass.StandardInfrequentAccess.toString()),
        new Transition()
            .withDays(90)
            .withStorageClass(StorageClass.Glacier.toString())
    ))
    .withExpirationInDays(365);

BucketLifecycleConfiguration configuration = new BucketLifecycleConfiguration()
    .withRules(Arrays.asList(rule));

s3ClientV1.setBucketLifecycleConfiguration("amzn-s3-demo-bucket", configuration);

// SDK V2
LifecycleRule rule = LifecycleRule.builder()
    .id("Archive and Delete Rule")
    .filter(LifecycleRuleFilter.builder()
        .prefix("documents/")
        .build())
    .status(ExpirationStatus.ENABLED)
    .transitions(Arrays.asList(
        Transition.builder()
            .days(30)
            .storageClass(TransitionStorageClass.STANDARD_IA)
            .build(),
        Transition.builder()
            .days(90)
            .storageClass(TransitionStorageClass.GLACIER)
            .build()
    ))
    .expiration(LifecycleExpiration.builder()
        .days(365)
        .build())
    .build();

PutBucketLifecycleConfigurationRequest request = PutBucketLifecycleConfigurationRequest.builder()
    .bucket("amzn-s3-demo-bucket")
    .lifecycleConfiguration(BucketLifecycleConfiguration.builder()
        .rules(rule)
        .build())
    .build();

s3ClientV2.putBucketLifecycleConfiguration(request);
```

### V1's `setBucketTaggingConfiguration` to V2's `putBucketTagging`
<a name="V1-setBucketTaggingConfiguration"></a>

```
// SDK V1
List<TagSet> tagsets = new ArrayList<>();
TagSet tagSet = new TagSet();
tagSet.setTag("key1", "value1");
tagSet.setTag("key2", "value2");
tagsets.add(tagSet);

BucketTaggingConfiguration bucketTaggingConfiguration = new BucketTaggingConfiguration();
bucketTaggingConfiguration.setTagSets(tagsets);

SetBucketTaggingConfigurationRequest request = new SetBucketTaggingConfigurationRequest(
    "amzn-s3-demo-bucket",
    bucketTaggingConfiguration
);

s3ClientV1.setBucketTaggingConfiguration(request);

// SDK V2
Tagging tagging = Tagging.builder()
    .tagSet(Arrays.asList(
        Tag.builder()
            .key("key1")
            .value("value1")
            .build(),
        Tag.builder()
            .key("key2")
            .value("value2")
            .build()
    ))
    .build();

PutBucketTaggingRequest request = PutBucketTaggingRequest.builder()
    .bucket("amzn-s3-demo-bucket")
    .tagging(tagging)
    .build();

s3ClientV2.putBucketTagging(request);
```

## V1 classes that require manual migration
<a name="s3-classes-manual-migration"></a>

### V1's `AccessControlList` to V2's `AccessControlPolicy`
<a name="V1-AccessControlList"></a>

```
// SDK V1
AccessControlList aclV1 = new AccessControlList();
aclV1.setOwner(new Owner("owner-id", "owner-name"));
aclV1.grantPermission(GroupGrantee.AllUsers, Permission.Read);

// SDK V2
// To migrate from V1 to V2, replace direct 'AccessControlList' modifications with an
// 'AccessControlPolicy.builder()' that contains both owner information and grants.
// Note that V2's approach requires building the complete permission set upfront rather than modifying permissions incrementally.
AccessControlPolicy acpV2 = AccessControlPolicy.builder()
    .owner(Owner.builder()
        .id("owner-id")
        .displayName("owner-name")
        .build())
    .grants(Arrays.asList(
         Grant.builder()
            .grantee(Grantee.builder()
                 .type(Type.GROUP)
                 .uri("http://acs.amazonaws.com/groups/global/AllUsers")
                 .build())
             .permission(Permission.READ)
             .build()
     ))
     .build();
```

### V1's `CannedAccessControlList` enum to V2's `BucketCannedACL` and `ObjectCannedACL` enums
<a name="V1-CannedAccessControlList"></a>

```
// SDK V1
// In V1, 'CannedAccessControlList' is an enumeration of predefined ACLs.
AmazonS3 s3ClientV1 = AmazonS3ClientBuilder.standard().build();

// Creating a bucket.
s3ClientV1.setBucketAcl("bucket-name", CannedAccessControlList.PublicRead);

// Creating an object.
PutObjectRequest putObjectRequest = new PutObjectRequest("bucket-name", "object-key", file)
    .withCannedAcl(CannedAccessControlList.PublicRead);
s3ClientV1.putObject(putObjectRequest);

// SDK V2
// V2 replaces V1's 'CannedAccessControlList' with 'BucketCannedACL' for buckets and 'ObjectCannedACL' for objects.
S3Client s3ClientV2 = S3Client.builder().build();

// Creating a bucket.
PutBucketAclRequest bucketRequest = PutBucketAclRequest.builder()
    .bucket("bucket-name")
    .acl(BucketCannedACL.PRIVATE)
    .build();
s3ClientV2.putBucketAcl(bucketRequest);

// Creating an object.
PutObjectRequest objectRequest = PutObjectRequest.builder()
    .bucket("bucket-name")
    .key("object-key")
    .acl(ObjectCannedACL.PUBLIC_READ)
    .build();
s3ClientV2.putObject(objectRequest, RequestBody.fromFile(file));
```

### V1's `BucketNotificationConfiguration` to V2's `NotificationConfiguration`
<a name="V1-BucketNotificationConfiguration"></a>

```
//SDK V1
BucketNotificationConfiguration notificationConfig = new BucketNotificationConfiguration();

// Adding configurations by name
notificationConfig.addConfiguration("lambdaConfig",
    new LambdaConfiguration("arn:aws:lambda:function", "s3:ObjectCreated:"));

notificationConfig.addConfiguration("topicConfig",
    new TopicConfiguration("arn:aws:sns:topic", "s3:ObjectRemoved:"));

notificationConfig.addConfiguration("queueConfig",
    new QueueConfiguration("arn:aws:sqs:queue", "s3:ObjectRestore:*"));

s3Client.setBucketNotificationConfiguration("bucket", notificationConfig);

// SDK V2
// In V2, V1's BucketNotificationConfiguration is renamed to NotificationConfiguration.
// V2 contains no common abstract class for LambdaFunction/Topic/Queue configurations.
NotificationConfiguration notificationConfig = NotificationConfiguration.builder()
    .lambdaFunctionConfigurations(
        LambdaFunctionConfiguration.builder()
            .lambdaFunctionArn("arn:aws:lambda:function")
            .events(Event.valueOf("s3:ObjectCreated:"))
            .build())
    .topicConfigurations(
        TopicConfiguration.builder()
            .topicArn("arn:aws:sns:topic")
            .events(Event.valueOf("s3:ObjectRemoved:"))
            .build())
    .queueConfigurations(
        QueueConfiguration.builder()
            .queueArn("arn:aws:sqs:queue")
            .events(Event.valueOf("s3:ObjectRestore:*"))
            .build())
    .build();

s3Client.putBucketNotificationConfiguration(req -> req
    .bucket("bucket")
    .notificationConfiguration(notificationConfig));
```

### V1's `MultiFactorAuthentication` to V2's `mfa` method on a request builder
<a name="V1-MultifactorAuthentication"></a>

```
// SDK V1
AmazonS3 s3ClientV1 = AmazonS3ClientBuilder.standard()
    .withRegion(Regions.US_WEST_2)
    .build();

BucketVersioningConfiguration versioningConfig = new BucketVersioningConfiguration()
    .withStatus(BucketVersioningConfiguration.ENABLED);

// Create an MFA configuration object.
MultiFactorAuthentication mfa = new MultiFactorAuthentication(
    "arn:aws:iam::1234567890:mfa/user",
    "123456"
);

// Create the request object.
SetBucketVersioningConfigurationRequest request = new SetBucketVersioningConfigurationRequest(
    "bucket-name",
    versioningConfig,
    mfa
);

// Send the request.
s3ClientV1.setBucketVersioningConfiguration(request);

// SDK V2
// V2 replaces V1's MultiFactorAuthentication POJO with parameters you set on the request builder.
S3Client s3ClientV2 = S3Client.builder()
    .region(Region.US_WEST_2)
    .build();

PutBucketVersioningRequest request = PutBucketVersioningRequest.builder()
    .bucket("bucket-name")
    .versioningConfiguration(VersioningConfiguration.builder()
        .status(BucketVersioningStatus.ENABLED)
        .build())
    .mfa("arn:aws:iam::1234567890:mfa/user 123456")  // Single method takes both MFA erial number and token.
    .build();

s3ClientV2.putBucketVersioning(request);
```
