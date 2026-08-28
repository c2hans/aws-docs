---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-HeadObjectExamples.html
---

# Retrieving object metadata from directory buckets
<a name="directory-buckets-objects-HeadObjectExamples"></a>

The following AWS SDK and AWS CLI examples show how to use the `HeadObject` and `GetObjectAttributes` API operation to retrieve metadata from an object in an Amazon S3 directory bucket without returning the object itself.

## Using the AWS SDKs
<a name="directory-bucket-copy-sdks"></a>

------
#### [ SDK for Java 2.x ]

**Example**

```
public static void headObject(S3Client s3Client, String bucketName, String objectKey) {
     try {
         HeadObjectRequest headObjectRequest = HeadObjectRequest
                 .builder()
                 .bucket(bucketName)
                 .key(objectKey)
                 .build();
         HeadObjectResponse response = s3Client.headObject(headObjectRequest);
         System.out.format("Amazon S3 object: \"%s\" found in bucket: \"%s\" with ETag: \"%s\"", objectKey, bucketName, response.eTag());
     }
     catch (S3Exception e) {
         System.err.println(e.awsErrorDetails().errorMessage());
```

------

## Using the AWS CLI
<a name="directory-head-object-cli"></a>

The following `head-object` example command shows how you can use the AWS CLI to retrieve metadata from an object. To run this command, replace the `{{user input placeholders}}` with your own information.

```
aws s3api head-object --bucket {{bucket-base-name}}--{{zone-id}}--x-s3 --key {{KEY_NAME}}
```

For more information, see [head-object](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/head-object.html) in the *AWS CLI Command Reference*.

The following `get-object-attributes` example command shows how you can use the AWS CLI to retrieve metadata from an object. To run this command, replace the `{{user input placeholders}}` with your own information.

```
aws s3api get-object-attributes --bucket {{bucket-base-name}}--{{zone-id}}--x-s3 --key {{KEY_NAME}} --object-attributes "StorageClass" "ETag" "ObjectSize"
```

For more information, see [get-object-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object-attributes.html) in the *AWS CLI Command Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
