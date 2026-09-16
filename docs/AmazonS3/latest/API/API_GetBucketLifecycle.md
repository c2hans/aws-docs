---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycle.html
---

# GetBucketLifecycle
<a name="API_GetBucketLifecycle"></a>

**Important**
For an updated version of this API, see [GetBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.html). If you configured a bucket lifecycle using the `filter` element, you should see the updated version of this topic. This topic is provided for backward compatibility.

**Note**
This operation is not supported for directory buckets.

Returns the lifecycle configuration information set on the bucket. For information about lifecycle configuration, see [Object Lifecycle Management](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html).

 To use this operation, you must have permission to perform the `s3:GetLifecycleConfiguration` action. The bucket owner has this permission by default. The bucket owner can grant this permission to others. For more information about permissions, see [Permissions Related to Bucket Subresource Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources) and [Managing Access Permissions to Your Amazon S3 Resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html).

 `GetBucketLifecycle` has the following special error:
+ Error code: `NoSuchLifecycleConfiguration`
  + Description: The lifecycle configuration does not exist.
  + HTTP Status Code: 404 Not Found
  + SOAP Fault Code Prefix: Client

The following operations are related to `GetBucketLifecycle`:
+  [GetBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.html)
+  [PutBucketLifecycle](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycle.html)
+  [DeleteBucketLifecycle](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketLifecycle.html)

**Important**
You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax
<a name="API_GetBucketLifecycle_RequestSyntax"></a>

```
GET /?lifecycle HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
```

## URI Request Parameters
<a name="API_GetBucketLifecycle_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Bucket](#API_GetBucketLifecycle_RequestSyntax) **   <a name="AmazonS3-GetBucketLifecycle-request-header-Bucket"></a>
The name of the bucket for which to get the lifecycle information.
Required: Yes

 ** [x-amz-expected-bucket-owner](#API_GetBucketLifecycle_RequestSyntax) **   <a name="AmazonS3-GetBucketLifecycle-request-header-ExpectedBucketOwner"></a>
The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Request Body
<a name="API_GetBucketLifecycle_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetBucketLifecycle_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<LifecycleConfiguration>
   <Rule>
      <AbortIncompleteMultipartUpload>
         <DaysAfterInitiation>integer</DaysAfterInitiation>
      </AbortIncompleteMultipartUpload>
      <Expiration>
         <Date>timestamp</Date>
         <Days>integer</Days>
         <ExpiredObjectDeleteMarker>boolean</ExpiredObjectDeleteMarker>
      </Expiration>
      <ID>string</ID>
      <NoncurrentVersionExpiration>
         <NewerNoncurrentVersions>integer</NewerNoncurrentVersions>
         <NoncurrentDays>integer</NoncurrentDays>
      </NoncurrentVersionExpiration>
      <NoncurrentVersionTransition>
         <NewerNoncurrentVersions>integer</NewerNoncurrentVersions>
         <NoncurrentDays>integer</NoncurrentDays>
         <StorageClass>string</StorageClass>
      </NoncurrentVersionTransition>
      <Prefix>string</Prefix>
      <Status>string</Status>
      <Transition>
         <Date>timestamp</Date>
         <Days>integer</Days>
         <StorageClass>string</StorageClass>
      </Transition>
   </Rule>
   ...
</LifecycleConfiguration>
```

## Response Elements
<a name="API_GetBucketLifecycle_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [LifecycleConfiguration](#API_GetBucketLifecycle_ResponseSyntax) **   <a name="AmazonS3-GetBucketLifecycle-response-GetBucketLifecycleOutput"></a>
Root level tag for the LifecycleConfiguration parameters.
Required: Yes

 ** [Rule](#API_GetBucketLifecycle_ResponseSyntax) **   <a name="AmazonS3-GetBucketLifecycle-response-Rules"></a>
Container for a lifecycle rule.
Type: Array of [Rule](API_Rule.md) data types

## Examples
<a name="API_GetBucketLifecycle_Examples"></a>

### Sample Request: Retrieve a lifecycle subresource
<a name="API_GetBucketLifecycle_Example_1"></a>

This example is a GET request to retrieve the lifecycle subresource from the specified bucket, and an example response with the returned lifecycle configuration.

```
            GET /?lifecycle HTTP/1.1
            Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
            x-amz-date: Thu, 15 Nov 2012 00:17:21 GMT
            Authorization: signatureValue
```

### Sample Response
<a name="API_GetBucketLifecycle_Example_2"></a>

This example illustrates one usage of GetBucketLifecycle.

```
            HTTP/1.1 200 OK
            x-amz-id-2: ITnGT1y4RyTmXa3rPi4hklTXouTf0hccUjo0iCPjz6FnfIutBj3M7fPGlWO2SEWp
            x-amz-request-id: 51991C342C575321
            Date: Thu, 15 Nov 2012 00:17:23 GMT
            Server: AmazonS3
            Content-Length: 358

            <?xml version="1.0" encoding="UTF-8"?>
            <LifecycleConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
               <Rule>
                    <ID>Archive and then delete rule</ID>
                    <Prefix>projectdocs/</Prefix>
                   <Status>Enabled</Status>
                  <Transition>
                       <Days>30</Days>
                       <StorageClass>STANDARD_IA</StorageClass>
                  </Transition>
                  <Transition>
                     <Days>365</Days>
                      <StorageClass>GLACIER</StorageClass>
                   </Transition>
                   <Expiration>
                      <Days>3650</Days>
                   </Expiration>
               </Rule>
            </LifecycleConfiguration>
```

## See Also
<a name="API_GetBucketLifecycle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketLifecycle)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/GetBucketLifecycle)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketLifecycle)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketLifecycle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketLifecycle)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketLifecycle)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketLifecycle)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketLifecycle)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketLifecycle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketLifecycle)
