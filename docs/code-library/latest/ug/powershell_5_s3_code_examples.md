---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/powershell_5_s3_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon S3 examples using Tools for PowerShell V5
<a name="powershell_5_s3_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with Amazon S3.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Copy-S3Object`
<a name="s3_CopyObject_powershell_5_topic"></a>

The following code example shows how to use `Copy-S3Object`.

**Tools for PowerShell V5**
**Example 1: This command copies the object "sample.txt" from bucket "test-files" to the same bucket but with a new key of "sample-copy.txt".**

```
Copy-S3Object -BucketName amzn-s3-demo-bucket -Key sample.txt -DestinationKey sample-copy.txt
```
**Example 2: This command copies the object "sample.txt" from bucket "test-files" to the bucket "backup-files" with a key of "sample-copy.txt".**

```
Copy-S3Object -BucketName amzn-s3-demo-source-bucket -Key sample.txt -DestinationKey sample-copy.txt -DestinationBucket amzn-s3-demo-destination-bucket
```
**Example 3: This command downloads the object "sample.txt" from bucket "test-files" to a local file with name "local-sample.txt".**

```
Copy-S3Object -BucketName amzn-s3-demo-bucket -Key sample.txt -LocalFile local-sample.txt
```
**Example 4: Downloads the single object to the specified file. The downloaded file will be found at c:\\downloads\\data\\archive.zip**

```
Copy-S3Object -BucketName amzn-s3-demo-bucket -Key data/archive.zip -LocalFolder c:\downloads
```
**Example 5: Downloads all objects that match the specified key prefix to the local folder. The relative key hierarchy will be preserved as subfolders in the overall download location.**

```
Copy-S3Object -BucketName amzn-s3-demo-bucket -KeyPrefix data -LocalFolder c:\downloads
```
**Example 6: Downloads a single object to a local file using multipart parallel download for improved performance on large files.**

```
Copy-S3Object -BucketName amzn-s3-demo-bucket -Key sample.txt -LocalFile local-sample.txt -UseMultipartDownload
```
**Example 7: Downloads a large object using RANGE mode with a custom 64MB part size. RANGE mode uses HTTP byte-range requests and works for all objects regardless of how they were uploaded.**

```
Copy-S3Object -BucketName amzn-s3-demo-bucket -Key large-file.zip -LocalFile local-large-file.zip -UseMultipartDownload -MultipartDownloadType RANGE -PartSize 64MB
```
**Example 8: Downloads all objects matching the key prefix to a local folder using multipart download with concurrent file downloads.**

```
Copy-S3Object -BucketName amzn-s3-demo-bucket -KeyPrefix data/ -LocalFolder C:\local-data -UseMultipartDownload -DownloadFilesConcurrently
```
**Example 9: Downloads a single object using multipart download with 20 concurrent connections for maximum throughput on high-bandwidth networks.**

```
Copy-S3Object -BucketName amzn-s3-demo-bucket -Key large-file.zip -LocalFile local-large-file.zip -UseMultipartDownload -ConcurrentServiceRequest 20
```
**Example 10: Downloads all objects matching the key prefix to a local folder using multipart download, continuing past individual file failures instead of aborting.**

```
Copy-S3Object -BucketName amzn-s3-demo-bucket -KeyPrefix data/ -LocalFolder C:\local-data -UseMultipartDownload -FailurePolicy ContinueOnFailure
```
+  For API details, see [CopyObject](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Dismount-S3PSDrive`
<a name="s3_DismountS3PSDrive_powershell_5_topic"></a>

The following code example shows how to use `Dismount-S3PSDrive`.

**Tools for PowerShell V5**
**Example 1: Changes to a location outside the S3 drive, then removes the drive.**

```
Set-Location $HOME
Dismount-S3PSDrive -Name S3
```
+  For API details, see [Dismount-S3PSDrive](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3Bucket`
<a name="s3_ListBuckets_powershell_5_topic"></a>

The following code example shows how to use `Get-S3Bucket`.

**Tools for PowerShell V5**
**Example 1: This command returns all S3 buckets.**

```
Get-S3Bucket
```
**Example 2: This command returns bucket named "test-files"**

```
Get-S3Bucket -BucketName amzn-s3-demo-bucket
```
+  For API details, see [ListBuckets](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3BucketACL`
<a name="s3_GetBucketAcl_powershell_5_topic"></a>

The following code example shows how to use `Get-S3BucketACL`.

**Tools for PowerShell V5**
**Example 1: The command gets the details of the object owner of the S3 object.**

```
(Get-S3BucketACL -BucketName 'amzn-s3-demo-bucket' -Select *).Owner
```
**Output:**

```
DisplayName Id
----------- --
testusername      9988776a6554433d22f1100112e334acb45566778899009e9887bd7f66c5f544
```
+  For API details, see [GetBucketAcl](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3BucketAccelerateConfiguration`
<a name="s3_GetBucketAccelerateConfiguration_powershell_5_topic"></a>

The following code example shows how to use `Get-S3BucketAccelerateConfiguration`.

**Tools for PowerShell V5**
**Example 1: This command returns the value Enabled, if the transfer acceleration settings is enabled for the bucket specified.**

```
Get-S3BucketAccelerateConfiguration -BucketName 'amzn-s3-demo-bucket'
```
**Output:**

```
Value
-----
Enabled
```
+  For API details, see [GetBucketAccelerateConfiguration](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3BucketAnalyticsConfiguration`
<a name="s3_GetBucketAnalyticsConfiguration_powershell_5_topic"></a>

The following code example shows how to use `Get-S3BucketAnalyticsConfiguration`.

**Tools for PowerShell V5**
**Example 1: This command returns the details of the analytics filter with the name 'testfilter' in the given S3 bucket.**

```
Get-S3BucketAnalyticsConfiguration -BucketName 'amzn-s3-demo-bucket' -AnalyticsId 'testfilter'
```
+  For API details, see [GetBucketAnalyticsConfiguration](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3BucketAnalyticsConfigurationList`
<a name="s3_ListBucketAnalyticsConfigurations_powershell_5_topic"></a>

The following code example shows how to use `Get-S3BucketAnalyticsConfigurationList`.

**Tools for PowerShell V5**
**Example 1: This command returns the first 100 analytics configurations of the given S3 bucket.**

```
Get-S3BucketAnalyticsConfigurationList -BucketName 'amzn-s3-demo-bucket'
```
+  For API details, see [ListBucketAnalyticsConfigurations](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3BucketEncryption`
<a name="s3_GetBucketEncryption_powershell_5_topic"></a>

The following code example shows how to use `Get-S3BucketEncryption`.

**Tools for PowerShell V5**
**Example 1: This command returns all the server side encryption rules associated with the given bucket.**

```
Get-S3BucketEncryption -BucketName 'amzn-s3-demo-bucket'
```
+  For API details, see [GetBucketEncryption](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3BucketInventoryConfiguration`
<a name="s3_GetBucketInventoryConfiguration_powershell_5_topic"></a>

The following code example shows how to use `Get-S3BucketInventoryConfiguration`.

**Tools for PowerShell V5**
**Example 1: This command returns the details of the inventory named 'testinventory' for the given S3 bucket.**

```
Get-S3BucketInventoryConfiguration -BucketName 'amzn-s3-demo-bucket' -InventoryId 'testinventory'
```
+  For API details, see [GetBucketInventoryConfiguration](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3BucketInventoryConfigurationList`
<a name="s3_ListBucketInventoryConfigurations_powershell_5_topic"></a>

The following code example shows how to use `Get-S3BucketInventoryConfigurationList`.

**Tools for PowerShell V5**
**Example 1: This command returns the first 100 inventory configurations of the given S3 bucket.**

```
Get-S3BucketInventoryConfigurationList -BucketName 'amzn-s3-demo-bucket'
```
+  For API details, see [ListBucketInventoryConfigurations](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3BucketLocation`
<a name="s3_GetBucketLocation_powershell_5_topic"></a>

The following code example shows how to use `Get-S3BucketLocation`.

**Tools for PowerShell V5**
**Example 1: This command returns the location constraint for the bucket 'amzn-s3-demo-bucket', if a constraint exists.**

```
Get-S3BucketLocation -BucketName 'amzn-s3-demo-bucket'
```
**Output:**

```
Value
-----
ap-south-1
```
+  For API details, see [GetBucketLocation](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3BucketLogging`
<a name="s3_GetBucketLogging_powershell_5_topic"></a>

The following code example shows how to use `Get-S3BucketLogging`.

**Tools for PowerShell V5**
**Example 1: This command returns the logging status for the specified bucket.**

```
Get-S3BucketLogging -BucketName 'amzn-s3-demo-bucket'
```
**Output:**

```
TargetBucketName   Grants TargetPrefix
----------------   ------ ------------
testbucket1        {}     testprefix
```
+  For API details, see [GetBucketLogging](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3BucketMetricsConfiguration`
<a name="s3_GetBucketMetricsConfiguration_powershell_5_topic"></a>

The following code example shows how to use `Get-S3BucketMetricsConfiguration`.

**Tools for PowerShell V5**
**Example 1: This command returns the details about the metrics filter named 'testfilter' for the given S3 bucket.**

```
Get-S3BucketMetricsConfiguration -BucketName 'amzn-s3-demo-bucket' -MetricsId 'testfilter'
```
+  For API details, see [GetBucketMetricsConfiguration](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3BucketNotification`
<a name="s3_GetBucketNotification_powershell_5_topic"></a>

The following code example shows how to use `Get-S3BucketNotification`.

**Tools for PowerShell V5**
**Example 1: This example retrieves notification configuration of the given bucket**

```
Get-S3BucketNotification -BucketName amzn-s3-demo-bucket | select -ExpandProperty TopicConfigurations
```
**Output:**

```
Id   Topic
--   -----
mimo arn:aws:sns:eu-west-1:123456789012:topic-1
```
+  For API details, see [GetBucketNotification](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3BucketPolicy`
<a name="s3_GetBucketPolicy_powershell_5_topic"></a>

The following code example shows how to use `Get-S3BucketPolicy`.

**Tools for PowerShell V5**
**Example 1: This command outputs the bucket policy associated with the given S3 bucket.**

```
Get-S3BucketPolicy -BucketName 'amzn-s3-demo-bucket'
```
+  For API details, see [GetBucketPolicy](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3BucketPolicyStatus`
<a name="s3_GetBucketPolicyStatus_powershell_5_topic"></a>

The following code example shows how to use `Get-S3BucketPolicyStatus`.

**Tools for PowerShell V5**
**Example 1: This command returns policy status for the given S3 bucket, indicating whether the bucket is public.**

```
Get-S3BucketPolicyStatus -BucketName 'amzn-s3-demo-bucket'
```
+  For API details, see [GetBucketPolicyStatus](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3BucketReplication`
<a name="s3_GetBucketReplication_powershell_5_topic"></a>

The following code example shows how to use `Get-S3BucketReplication`.

**Tools for PowerShell V5**
**Example 1: Returns the replication configuration information set on the bucket named 'amzn-s3-demo-bucket'.**

```
Get-S3BucketReplication -BucketName amzn-s3-demo-bucket
```
+  For API details, see [GetBucketReplication](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3BucketRequestPayment`
<a name="s3_GetBucketRequestPayment_powershell_5_topic"></a>

The following code example shows how to use `Get-S3BucketRequestPayment`.

**Tools for PowerShell V5**
**Example 1: Returns the request payment configuration for the bucket named 'amzn-s3-demo-bucket'. By default, the bucket owner pays for downloads from the bucket.**

```
Get-S3BucketRequestPayment -BucketName amzn-s3-demo-bucket
```
+  For API details, see [GetBucketRequestPayment](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3BucketTagging`
<a name="s3_GetBucketTagging_powershell_5_topic"></a>

The following code example shows how to use `Get-S3BucketTagging`.

**Tools for PowerShell V5**
**Example 1: This command returns all the tags associated with the given bucket.**

```
Get-S3BucketTagging -BucketName 'amzn-s3-demo-bucket'
```
+  For API details, see [GetBucketTagging](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3BucketVersioning`
<a name="s3_GetBucketVersioning_powershell_5_topic"></a>

The following code example shows how to use `Get-S3BucketVersioning`.

**Tools for PowerShell V5**
**Example 1: This command returns the status of versioning with respect to the given bucket.**

```
Get-S3BucketVersioning -BucketName 'amzn-s3-demo-bucket'
```
+  For API details, see [GetBucketVersioning](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3BucketWebsite`
<a name="s3_GetBucketWebsite_powershell_5_topic"></a>

The following code example shows how to use `Get-S3BucketWebsite`.

**Tools for PowerShell V5**
**Example 1: This command returns the details of the static website configurations of the given S3 bucket.**

```
Get-S3BucketWebsite -BucketName 'amzn-s3-demo-bucket'
```
+  For API details, see [GetBucketWebsite](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3CORSConfiguration`
<a name="s3_GetCORSConfiguration_powershell_5_topic"></a>

The following code example shows how to use `Get-S3CORSConfiguration`.

**Tools for PowerShell V5**
**Example 1: This command returns an object that contains all the CORS configuration rules corresponding to the given S3 Bucket.**

```
Get-S3CORSConfiguration -BucketName 'amzn-s3-demo-bucket' -Select Configuration.Rules
```
**Output:**

```
AllowedMethods : {PUT, POST, DELETE}
AllowedOrigins : {http://www.example1.com}
Id             :
ExposeHeaders  : {}
MaxAgeSeconds  : 0
AllowedHeaders : {*}

AllowedMethods : {PUT, POST, DELETE}
AllowedOrigins : {http://www.example2.com}
Id             :
ExposeHeaders  : {}
MaxAgeSeconds  : 0
AllowedHeaders : {*}

AllowedMethods : {GET}
AllowedOrigins : {*}
Id             :
ExposeHeaders  : {}
MaxAgeSeconds  : 0
AllowedHeaders : {}
```
+  For API details, see [GetCORSConfiguration](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3HeadBucket`
<a name="s3_HeadBucket_powershell_5_topic"></a>

The following code example shows how to use `Get-S3HeadBucket`.

**Tools for PowerShell V5**
**Example 1: This command returns the output with HTTP status code 200 OK for existing bucket when user has permission to access it. BucketArn parameter is only supported for S3 directory buckets.**

```
Get-S3HeadBucket -BucketName amzn-s3-demo-bucket
```
**Output:**

```
AccessPointAlias   : False
BucketArn          :
BucketLocationName :
BucketLocationType :
BucketRegion       : us-east-2
ResponseMetadata   : Amazon.Runtime.ResponseMetadata
ContentLength      : 0
HttpStatusCode     : OK
```
**Example 2: This command throws error with HTTP status code NotFound for non-existent bucket.**

```
Get-S3HeadBucket -BucketName amzn-s3-non-existing-bucket
```
**Output:**

```
Get-S3HeadBucket: Error making request with Error Code NotFound and Http Status Code NotFound. No further error information was returned by the service.
```
**Example 3: This command throws error with HTTP status code Forbidden for existing bucket where user does not have permission to access it.**

```
Get-S3HeadBucket -BucketName amzn-s3-no-access-bucket
```
**Output:**

```
Get-S3HeadBucket: Error making request with Error Code Forbidden and Http Status Code Forbidden. No further error information was returned by the service.
```
+  For API details, see [HeadBucket](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3LifecycleConfiguration`
<a name="s3_GetLifecycleConfiguration_powershell_5_topic"></a>

The following code example shows how to use `Get-S3LifecycleConfiguration`.

**Tools for PowerShell V5**
**Example 1: This example retrieves lifecycle configuration for the bucket.**

```
Get-S3LifecycleConfiguration -BucketName amzn-s3-demo-bucket
```
**Output:**

```
Rules
-----
{Remove-in-150-days, Archive-to-Glacier-in-30-days}
```
+  For API details, see [GetLifecycleConfiguration](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3Object`
<a name="s3_ListObjects_powershell_5_topic"></a>

The following code example shows how to use `Get-S3Object`.

**Tools for PowerShell V5**
**Example 1: This command retrieves the information about all of the items in the bucket "test-files".**

```
Get-S3Object -BucketName amzn-s3-demo-bucket
```
**Example 2: This command retrieves the information about the item "sample.txt" from bucket "test-files".**

```
Get-S3Object -BucketName amzn-s3-demo-bucket -Key sample.txt
```
**Example 3: This command retrieves the information about all items with the prefix "sample" from bucket "test-files".**

```
Get-S3Object -BucketName amzn-s3-demo-bucket -KeyPrefix sample
```
+  For API details, see [ListObjects](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3ObjectACL`
<a name="s3_GetObjectAcl_powershell_5_topic"></a>

The following code example shows how to use `Get-S3ObjectACL`.

**Tools for PowerShell V5**
**Example 1: The command gets the details of the object owner of the S3 object.**

```
(Get-S3ObjectACL -BucketName 'amzn-s3-demo-bucket' -key 'initialize.ps1' -Select *).Owner
```
**Output:**

```
DisplayName Id
----------- --
testusername      9988776a6554433d22f1100112e334acb45566778899009e9887bd7f66c5f544
```
+  For API details, see [GetObjectAcl](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3ObjectLockConfiguration`
<a name="s3_GetObjectLockConfiguration_powershell_5_topic"></a>

The following code example shows how to use `Get-S3ObjectLockConfiguration`.

**Tools for PowerShell V5**
**Example 1: This command returns the value 'Enabled' if Object lock configuration is enabled for the given S3 bucket.**

```
Get-S3ObjectLockConfiguration -BucketName 'amzn-s3-demo-bucket' -Select ObjectLockConfiguration.ObjectLockEnabled
```
**Output:**

```
Value
-----
Enabled
```
+  For API details, see [GetObjectLockConfiguration](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3ObjectMetadata`
<a name="s3_GetObjectMetadata_powershell_5_topic"></a>

The following code example shows how to use `Get-S3ObjectMetadata`.

**Tools for PowerShell V5**
**Example 1: This command returns the metadata of the object with key 'ListTrusts.txt' in the given S3 bucket.**

```
Get-S3ObjectMetadata -BucketName 'amzn-s3-demo-bucket' -Key 'ListTrusts.txt'
```
**Output:**

```
Headers                                       : Amazon.S3.Model.HeadersCollection
Metadata                                      : Amazon.S3.Model.MetadataCollection
DeleteMarker                                  :
AcceptRanges                                  : bytes
ContentRange                                  :
Expiration                                    :
RestoreExpiration                             :
RestoreInProgress                             : False
LastModified                                  : 01/01/2020 08:02:05
ETag                                          : "d000011112a222e333e3bb4ee5d43d21"
MissingMeta                                   : 0
VersionId                                     : null
Expires                                       : 01/01/0001 00:00:00
WebsiteRedirectLocation                       :
ServerSideEncryptionMethod                    : AES256
ServerSideEncryptionCustomerMethod            :
ServerSideEncryptionKeyManagementServiceKeyId :
ReplicationStatus                             :
PartsCount                                    :
ObjectLockLegalHoldStatus                     :
ObjectLockMode                                :
ObjectLockRetainUntilDate                     : 01/01/0001 00:00:00
StorageClass                                  :
RequestCharged                                :
```
+  For API details, see [GetObjectMetadata](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3ObjectRetention`
<a name="s3_GetObjectRetention_powershell_5_topic"></a>

The following code example shows how to use `Get-S3ObjectRetention`.

**Tools for PowerShell V5**
**Example 1: The command returns the mode and date till the object would be retained.**

```
Get-S3ObjectRetention -BucketName 'amzn-s3-demo-bucket' -Key 'testfile.txt'
```
+  For API details, see [GetObjectRetention](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3ObjectTagSet`
<a name="s3_GetObjectTagging_powershell_5_topic"></a>

The following code example shows how to use `Get-S3ObjectTagSet`.

**Tools for PowerShell V5**
**Example 1: The sample returns the tags associated with the object present on the given S3 bucket.**

```
Get-S3ObjectTagSet -Key 'testfile.txt' -BucketName 'amzn-s3-demo-bucket'
```
**Output:**

```
Key  Value
---  -----
test value
```
+  For API details, see [GetObjectTagging](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3PreSignedURL`
<a name="s3_GetPreSignedURL_powershell_5_topic"></a>

The following code example shows how to use `Get-S3PreSignedURL`.

**Tools for PowerShell V5**
**Example 1: The command returns pre-signed URL for a specified key and an expiration date.**

```
Get-S3PreSignedURL -BucketName 'amzn-s3-demo-bucket' -Key 'testkey' -Expires '2023-11-16'
```
**Example 2: The command returns pre-signed URL for a Directory Bucket with specified key and an expiration date.**

```
[Amazon.AWSConfigsS3]::UseSignatureVersion4 = $true
      Get-S3PreSignedURL -BucketName amzn-s3-demo-bucket--usw2-az1--x-s3 -Key 'testkey' -Expire '2023-11-17'
```
+  For API details, see [GetPreSignedURL](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3PublicAccessBlock`
<a name="s3_GetPublicAccessBlock_powershell_5_topic"></a>

The following code example shows how to use `Get-S3PublicAccessBlock`.

**Tools for PowerShell V5**
**Example 1: The command returns the public access block configuration of the given S3 bucket.**

```
Get-S3PublicAccessBlock -BucketName 'amzn-s3-demo-bucket'
```
+  For API details, see [GetPublicAccessBlock](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-S3Version`
<a name="s3_ListVersions_powershell_5_topic"></a>

The following code example shows how to use `Get-S3Version`.

**Tools for PowerShell V5**
**Example 1: This command returns the metadata about all of the versions of objects in the given S3 bucket.**

```
Get-S3Version -BucketName 'amzn-s3-demo-bucket'
```
**Output:**

```
IsTruncated         : False
KeyMarker           :
VersionIdMarker     :
NextKeyMarker       :
NextVersionIdMarker :
Versions            : {EC2.txt, EC2MicrosoftWindowsGuide.txt, ListDirectories.json, ListTrusts.json}
Name                : amzn-s3-demo-bucket
Prefix              :
MaxKeys             : 1000
CommonPrefixes      : {}
Delimiter           :
```
+  For API details, see [ListVersions](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Mount-S3PSDrive`
<a name="s3_MountS3PSDrive_powershell_5_topic"></a>

The following code example shows how to use `Mount-S3PSDrive`.

**Tools for PowerShell V5**
**Example 1: Mounts an account-root S3 drive named S3 using the default credential and Region resolution. The cmdlet does not change the current location. Get-PSDrive shows the mounted drive, and Get-ChildItem lists the buckets available to the resolved credentials.**

```
Mount-S3PSDrive -Name S3
Get-PSDrive -Name S3
Get-ChildItem -Path S3:\
```
**Example 2: Mounts a drive scoped to a bucket prefix and sets the Region used by the drive. Set-Location enters the drive explicitly because mounting does not change the current location.**

```
Mount-S3PSDrive -Name ProjectData -Root 'amzn-s3-demo-bucket/projects/2026' -Region us-west-2
Set-Location ProjectData:\
```
**Example 3: Mounts an account-root drive using credentials from a named profile.**

```
Mount-S3PSDrive -Name Archive -ProfileName my-profile -Region us-east-1
```
+  For API details, see [Mount-S3PSDrive](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-S3Bucket`
<a name="s3_PutBucket_powershell_5_topic"></a>

The following code example shows how to use `New-S3Bucket`.

**Tools for PowerShell V5**
**Example 1: This command creates a new private bucket named "sample-bucket".**

```
New-S3Bucket -BucketName amzn-s3-demo-bucket
```
**Example 2: This command creates a new bucket named "sample-bucket" with read-write permissions.**

```
New-S3Bucket -BucketName amzn-s3-demo-bucket -PublicReadWrite
```
**Example 3: This command creates a new bucket named "sample-bucket" with read-only permissions.**

```
New-S3Bucket -BucketName amzn-s3-demo-bucket -PublicReadOnly
```
**Example 4: This command creates a new Directory bucket named "amzn-s3-demo-bucket--use1-az5--x-s3" with PutBucketConfiguration.**

```
$bucketConfiguration = @{
      BucketInfo = @{
          DataRedundancy = 'SingleAvailabilityZone'
          Type = 'Directory'
      }
      Location = @{
          Name = 'usw2-az1'
          Type = 'AvailabilityZone'
      }
    }
New-S3Bucket -BucketName amzn-s3-demo-bucket--usw2-az1--x-s3 -BucketConfiguration $bucketConfiguration -Region us-west-2
```
+  For API details, see [PutBucket](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Read-S3Object`
<a name="s3_GetObject_powershell_5_topic"></a>

The following code example shows how to use `Read-S3Object`.

**Tools for PowerShell V5**
**Example 1: This command retrieves item "sample.txt" from bucket "amzn-s3-demo-bucket" and saves it to a file named "local-sample.txt" in the current location. The file "local-sample.txt" does not have to exist before this command is called.**

```
Read-S3Object -BucketName amzn-s3-demo-bucket -Key sample.txt -File local-sample.txt
```
**Example 2: This command retrieves virtual directory "DIR" from bucket "amzn-s3-demo-bucket" and saves it to a folder named "Local-DIR" in the current location. The folder "Local-DIR" does not have to exist before this command is called.**

```
Read-S3Object -BucketName amzn-s3-demo-bucket -KeyPrefix DIR -Folder Local-DIR
```
**Example 3: Downloads all objects with keys ending in '.json' from buckets with 'config' in the bucket name to files in the specified folder. The object keys are used to set the filenames.**

```
Get-S3Bucket | ? { $_.BucketName -like '*config*' } | Get-S3Object | ? { $_.Key -like '*.json' } | Read-S3Object -Folder C:\ConfigObjects
```
**Example 4: Downloads a single object using multipart parallel download for improved performance on large files.**

```
Read-S3Object -BucketName amzn-s3-demo-bucket -Key sample.txt -File local-sample.txt -UseMultipartDownload
```
**Example 5: Downloads a large object using RANGE mode with a custom 64MB part size. RANGE mode uses HTTP byte-range requests and works for all objects regardless of how they were uploaded.**

```
Read-S3Object -BucketName amzn-s3-demo-bucket -Key large-file.zip -File local-large-file.zip -UseMultipartDownload -MultipartDownloadType RANGE -PartSize 64MB
```
**Example 6: Downloads all objects with the key prefix "data/" to a local folder using multipart download with concurrent file downloads.**

```
Read-S3Object -BucketName amzn-s3-demo-bucket -KeyPrefix data/ -Folder C:\local-data -UseMultipartDownload -DownloadFilesConcurrently
```
**Example 7: Downloads a single object using multipart download with 20 concurrent connections for maximum throughput on high-bandwidth networks.**

```
Read-S3Object -BucketName amzn-s3-demo-bucket -Key large-file.zip -File local-large-file.zip -UseMultipartDownload -ConcurrentServiceRequest 20
```
**Example 8: Downloads all objects with the key prefix "data/" to a local folder using multipart download, continuing past individual file failures instead of aborting.**

```
Read-S3Object -BucketName amzn-s3-demo-bucket -KeyPrefix data/ -Folder C:\local-data -UseMultipartDownload -FailurePolicy ContinueOnFailure
```
+  For API details, see [GetObject](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-S3Bucket`
<a name="s3_DeleteBucket_powershell_5_topic"></a>

The following code example shows how to use `Remove-S3Bucket`.

**Tools for PowerShell V5**
**Example 1: This command removes all objects and object versions from the bucket 'test-files' and then deletes the bucket. The command will prompt for confirmation before proceeding. Add the -Force switch to suppress confirmation. Note that buckets that are not empty cannot be deleted.**

```
Remove-S3Bucket -BucketName amzn-s3-demo-bucket -DeleteBucketContent
```
+  For API details, see [DeleteBucket](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-S3BucketAnalyticsConfiguration`
<a name="s3_DeleteBucketAnalyticsConfiguration_powershell_5_topic"></a>

The following code example shows how to use `Remove-S3BucketAnalyticsConfiguration`.

**Tools for PowerShell V5**
**Example 1: The command removes the analytics filter with name 'testfilter' in the given S3 bucket.**

```
Remove-S3BucketAnalyticsConfiguration -BucketName 'amzn-s3-demo-bucket' -AnalyticsId 'testfilter'
```
+  For API details, see [DeleteBucketAnalyticsConfiguration](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-S3BucketEncryption`
<a name="s3_DeleteBucketEncryption_powershell_5_topic"></a>

The following code example shows how to use `Remove-S3BucketEncryption`.

**Tools for PowerShell V5**
**Example 1: This disables the encryption enabled for the S3 bucket provided.**

```
Remove-S3BucketEncryption -BucketName 'amzn-s3-demo-bucket'
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-S3BucketEncryption (DeleteBucketEncryption)" on target "s3casetestbucket".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```
+  For API details, see [DeleteBucketEncryption](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-S3BucketInventoryConfiguration`
<a name="s3_DeleteBucketInventoryConfiguration_powershell_5_topic"></a>

The following code example shows how to use `Remove-S3BucketInventoryConfiguration`.

**Tools for PowerShell V5**
**Example 1: This command removes the invventory named 'testInventoryName' corresponding to the given S3 bucket.**

```
Remove-S3BucketInventoryConfiguration -BucketName 'amzn-s3-demo-bucket' -InventoryId 'testInventoryName'
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-S3BucketInventoryConfiguration (DeleteBucketInventoryConfiguration)" on target "amzn-s3-demo-bucket".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```
+  For API details, see [DeleteBucketInventoryConfiguration](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-S3BucketMetricsConfiguration`
<a name="s3_DeleteBucketMetricsConfiguration_powershell_5_topic"></a>

The following code example shows how to use `Remove-S3BucketMetricsConfiguration`.

**Tools for PowerShell V5**
**Example 1: The command removes the metrics filter with name 'testmetrics' in the given S3 bucket.**

```
Remove-S3BucketMetricsConfiguration -BucketName 'amzn-s3-demo-bucket' -MetricsId 'testmetrics'
```
+  For API details, see [DeleteBucketMetricsConfiguration](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-S3BucketPolicy`
<a name="s3_DeleteBucketPolicy_powershell_5_topic"></a>

The following code example shows how to use `Remove-S3BucketPolicy`.

**Tools for PowerShell V5**
**Example 1: The command removes the bucket policy associated with the given S3 bucket.**

```
Remove-S3BucketPolicy -BucketName 'amzn-s3-demo-bucket'
```
+  For API details, see [DeleteBucketPolicy](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-S3BucketReplication`
<a name="s3_DeleteBucketReplication_powershell_5_topic"></a>

The following code example shows how to use `Remove-S3BucketReplication`.

**Tools for PowerShell V5**
**Example 1: Deletes the replication configuration associated with the bucket named 'amzn-s3-demo-bucket'. Note that this operation requires permission for the s3:DeleteReplicationConfiguration action. You will be prompted for confirmation before the operation proceeds - to suppress confirmation, use the -Force switch.**

```
Remove-S3BucketReplication -BucketName amzn-s3-demo-bucket
```
+  For API details, see [DeleteBucketReplication](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-S3BucketTagging`
<a name="s3_DeleteBucketTagging_powershell_5_topic"></a>

The following code example shows how to use `Remove-S3BucketTagging`.

**Tools for PowerShell V5**
**Example 1: This command removes all the tags associated with the given S3 bucket.**

```
Remove-S3BucketTagging -BucketName 'amzn-s3-demo-bucket'
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-S3BucketTagging (DeleteBucketTagging)" on target "amzn-s3-demo-bucket".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```
+  For API details, see [DeleteBucketTagging](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-S3BucketWebsite`
<a name="s3_DeleteBucketWebsite_powershell_5_topic"></a>

The following code example shows how to use `Remove-S3BucketWebsite`.

**Tools for PowerShell V5**
**Example 1: This command disables the static website hosting property of the given S3 bucket.**

```
Remove-S3BucketWebsite -BucketName 'amzn-s3-demo-bucket'
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-S3BucketWebsite (DeleteBucketWebsite)" on target "amzn-s3-demo-bucket".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```
+  For API details, see [DeleteBucketWebsite](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-S3CORSConfiguration`
<a name="s3_DeleteCORSConfiguration_powershell_5_topic"></a>

The following code example shows how to use `Remove-S3CORSConfiguration`.

**Tools for PowerShell V5**
**Example 1: This command removes the CORS configuration for the given S3 bucket.**

```
Remove-S3CORSConfiguration -BucketName 'amzn-s3-demo-bucket'
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-S3CORSConfiguration (DeleteCORSConfiguration)" on target "amzn-s3-demo-bucket".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```
+  For API details, see [DeleteCORSConfiguration](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-S3LifecycleConfiguration`
<a name="s3_DeleteLifecycleConfiguration_powershell_5_topic"></a>

The following code example shows how to use `Remove-S3LifecycleConfiguration`.

**Tools for PowerShell V5**
**Example 1: The command removes all the lifecycle rules for the given S3 bucket.**

```
Remove-S3LifecycleConfiguration -BucketName 'amzn-s3-demo-bucket'
```
+  For API details, see [DeleteLifecycleConfiguration](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-S3MultipartUpload`
<a name="s3_AbortMultipartUpload_powershell_5_topic"></a>

The following code example shows how to use `Remove-S3MultipartUpload`.

**Tools for PowerShell V5**
**Example 1: This command aborts multipart uploads created earlier than 5 days ago.**

```
Remove-S3MultipartUpload -BucketName amzn-s3-demo-bucket -DaysBefore 5
```
**Example 2: This command aborts multipart uploads created earlier than January 2nd, 2014.**

```
Remove-S3MultipartUpload -BucketName amzn-s3-demo-bucket -InitiatedDate "Thursday, January 02, 2014"
```
**Example 3: This command aborts multipart uploads created earlier than January 2nd, 2014, 10:45:37.**

```
Remove-S3MultipartUpload -BucketName amzn-s3-demo-bucket -InitiatedDate "2014/01/02 10:45:37"
```
+  For API details, see [AbortMultipartUpload](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-S3Object`
<a name="s3_DeleteObjects_powershell_5_topic"></a>

The following code example shows how to use `Remove-S3Object`.

**Tools for PowerShell V5**
**Example 1: This command removes the object "sample.txt" from bucket "test-files". You are prompted for confirmation before the command executes; to suppress the prompt use the -Force switch.**

```
Remove-S3Object -BucketName amzn-s3-demo-bucket -Key sample.txt
```
**Example 2: This command removes the specified version of object "sample.txt" from bucket "test-files", assuming the bucket has been configured to enable object versions.**

```
Remove-S3Object -BucketName amzn-s3-demo-bucket -Key sample.txt -VersionId HLbxnx6V9omT6AQYVpks8mmFKQcejpqt
```
**Example 3: This command removes objects "sample1.txt", "sample2.txt" and "sample3.txt" from bucket "test-files" as a single batch operation. The service response will list all keys processed, regardless of the success or error status of the deletion. To obtain only errors for keys that were not able to be processed by the service add the -ReportErrorsOnly parameter (this parameter can also be specified with the alias -Quiet.**

```
Remove-S3Object -BucketName amzn-s3-demo-bucket -KeyCollection @( "sample1.txt", "sample2.txt", "sample3.txt" )
```
**Example 4: This example uses an inline expression with the -KeyCollection parameter to obtain the keys of the objects to delete. Get-S3Object returns a collection of Amazon.S3.Model.S3Object instances, each of which has a Key member of type string identifying the object.**

```
Remove-S3Object -bucketname "amzn-s3-demo-bucket" -KeyCollection (Get-S3Object "test-files" -KeyPrefix "prefix/subprefix" | select -ExpandProperty Key)
```
**Example 5: This example obtains all objects that have a key prefix "prefix/subprefix" in the bucket and deletes them. Note that the incoming objects are processed one at a time. For large collections consider passing the collection to the cmdlet's -InputObject (alias -S3ObjectCollection) parameter to enable the deletion to occur as a batch with a single call to the service.**

```
Get-S3Object -BucketName "amzn-s3-demo-bucket" -KeyPrefix "prefix/subprefix" | Remove-S3Object -Force
```
**Example 6: This example pipes a collection of Amazon.S3.Model.S3ObjectVersion instances that represent delete markers to the cmdlet for deletion. Note that the incoming objects are processed one at a time. For large collections consider passing the collection to the cmdlet's -InputObject (alias -S3ObjectCollection) parameter to enable the deletion to occur as a batch with a single call to the service.**

```
(Get-S3Version -BucketName "amzn-s3-demo-bucket").Versions | Where {$_.IsDeleteMarker -eq "True"} | Remove-S3Object -Force
```
**Example 7: This script shows how to perform a batch delete of a set of objects (in this case delete markers) by constructing an array of objects to be used with the -KeyAndVersionCollection parameter.**

```
$keyVersions = @()
$markers = (Get-S3Version -BucketName $BucketName).Versions | Where {$_.IsDeleteMarker -eq "True"}
foreach ($marker in $markers) { $keyVersions += @{ Key = $marker.Key; VersionId = $marker.VersionId } }
Remove-S3Object -BucketName $BucketName -KeyAndVersionCollection $keyVersions -Force
```
+  For API details, see [DeleteObjects](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-S3ObjectTagSet`
<a name="s3_DeleteObjectTagging_powershell_5_topic"></a>

The following code example shows how to use `Remove-S3ObjectTagSet`.

**Tools for PowerShell V5**
**Example 1: This command removes all the tags associated with the object with key 'testfile.txt' in the given S3 Bucket.**

```
Remove-S3ObjectTagSet -Key 'testfile.txt' -BucketName 'amzn-s3-demo-bucket' -Select '^Key'
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-S3ObjectTagSet (DeleteObjectTagging)" on target "testfile.txt".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
testfile.txt
```
+  For API details, see [DeleteObjectTagging](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-S3PublicAccessBlock`
<a name="s3_DeletePublicAccessBlock_powershell_5_topic"></a>

The following code example shows how to use `Remove-S3PublicAccessBlock`.

**Tools for PowerShell V5**
**Example 1: This command turns off the block public access setting for the given bucket.**

```
Remove-S3PublicAccessBlock -BucketName 'amzn-s3-demo-bucket' -Force -Select '^BucketName'
```
**Output:**

```
amzn-s3-demo-bucket
```
+  For API details, see [DeletePublicAccessBlock](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Set-S3BucketEncryption`
<a name="s3_PutBucketEncryption_powershell_5_topic"></a>

The following code example shows how to use `Set-S3BucketEncryption`.

**Tools for PowerShell V5**
**Example 1: This command enables default AES256 server side encryption with Amazon S3 Managed Keys(SSE-S3) on the given bucket. **

```
$Encryptionconfig = @{ServerSideEncryptionByDefault = @{ServerSideEncryptionAlgorithm = "AES256"}}
Set-S3BucketEncryption -BucketName 'amzn-s3-demo-bucket' -ServerSideEncryptionConfiguration_ServerSideEncryptionRule $Encryptionconfig
```
+  For API details, see [PutBucketEncryption](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Test-S3Bucket`
<a name="s3_Test-S3Bucket_powershell_5_topic"></a>

The following code example shows how to use `Test-S3Bucket`.

**Tools for PowerShell V5**
**Example 1: This command returns True if the bucket exists, False otherwise. The command returns True even if the bucket does not belong to the user.**

```
Test-S3Bucket -BucketName amzn-s3-demo-bucket
```
+  For API details, see [Test-S3Bucket](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Write-S3BucketAccelerateConfiguration`
<a name="s3_PutBucketAccelerateConfiguration_powershell_5_topic"></a>

The following code example shows how to use `Write-S3BucketAccelerateConfiguration`.

**Tools for PowerShell V5**
**Example 1: This command enables the transfer acceleration for the given S3 bucket.**

```
$statusVal = New-Object Amazon.S3.BucketAccelerateStatus('Enabled')
Write-S3BucketAccelerateConfiguration -BucketName 'amzn-s3-demo-bucket' -AccelerateConfiguration_Status $statusVal
```
+  For API details, see [PutBucketAccelerateConfiguration](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Write-S3BucketNotification`
<a name="s3_PutBucketNotification_powershell_5_topic"></a>

The following code example shows how to use `Write-S3BucketNotification`.

**Tools for PowerShell V5**
**Example 1: This example configures the SNS topic configuration for the S3 event ObjectRemovedDelete and enables notification for the given s3 bucket**

```
$topic =  [Amazon.S3.Model.TopicConfiguration] @{
  Id = "delete-event"
  Topic = "arn:aws:sns:eu-west-1:123456789012:topic-1"
  Event = [Amazon.S3.EventType]::ObjectRemovedDelete
}

Write-S3BucketNotification -BucketName amzn-s3-demo-bucket -TopicConfiguration $topic
```
**Example 2: This example enables notifications of ObjectCreatedAll for the given bucket sending it to Lambda function.**

```
$lambdaConfig = [Amazon.S3.Model.LambdaFunctionConfiguration] @{
  Events = "s3:ObjectCreated:*"
  FunctionArn = "arn:aws:lambda:eu-west-1:123456789012:function:rdplock"
  Id = "ObjectCreated-Lambda"
  Filter = @{
    S3KeyFilter = @{
      FilterRules = @(
        @{Name="Prefix";Value="dada"}
        @{Name="Suffix";Value=".pem"}
      )
    }
  }
}

Write-S3BucketNotification -BucketName amzn-s3-demo-bucket -LambdaFunctionConfiguration $lambdaConfig
```
**Example 3: This example creates 2 different Lambda configuration on the basis of different key-suffix and configured both in a single command. **

```
#Lambda Config 1

$firstLambdaConfig = [Amazon.S3.Model.LambdaFunctionConfiguration] @{
  Events = "s3:ObjectCreated:*"
  FunctionArn = "arn:aws:lambda:eu-west-1:123456789012:function:verifynet"
  Id = "ObjectCreated-dada-ps1"
  Filter = @{
    S3KeyFilter = @{
      FilterRules = @(
        @{Name="Prefix";Value="dada"}
        @{Name="Suffix";Value=".ps1"}
      )
    }
  }
}

#Lambda Config 2

$secondlambdaConfig = [Amazon.S3.Model.LambdaFunctionConfiguration] @{
  Events = [Amazon.S3.EventType]::ObjectCreatedAll
  FunctionArn = "arn:aws:lambda:eu-west-1:123456789012:function:verifyssm"
  Id = "ObjectCreated-dada-json"
  Filter = @{
    S3KeyFilter = @{
      FilterRules = @(
        @{Name="Prefix";Value="dada"}
        @{Name="Suffix";Value=".json"}
      )
    }
  }
}

Write-S3BucketNotification -BucketName amzn-s3-demo-bucket -LambdaFunctionConfiguration $firstLambdaConfig,$secondlambdaConfig
```
+  For API details, see [PutBucketNotification](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Write-S3BucketReplication`
<a name="s3_PutBucketReplication_powershell_5_topic"></a>

The following code example shows how to use `Write-S3BucketReplication`.

**Tools for PowerShell V5**
**Example 1: This example sets a replication configuration with a single rule enabling replication to the 'amzn-s3-demo-bucket' bucket any new objects created with the key name prefix "TaxDocs" in the bucket 'amzn-s3-demo-bucket'.**

```
$rule1 = New-Object Amazon.S3.Model.ReplicationRule
$rule1.ID = "Rule-1"
$rule1.Status = "Enabled"
$rule1.Prefix = "TaxDocs"
$rule1.Destination = @{ BucketArn = "arn:aws:s3:::amzn-s3-demo-destination-bucket" }

$params = @{
    BucketName = "amzn-s3-demo-bucket"
    Configuration_Role = "arn:aws:iam::35667example:role/CrossRegionReplicationRoleForS3"
    Configuration_Rule = $rule1
}

Write-S3BucketReplication @params
```
**Example 2: This example sets a replication configuration with multiple rules enabling replication to the 'amzn-s3-demo-bucket' bucket any new objects created with either the key name prefix "TaxDocs" or "OtherDocs". The key prefixes must not overlap.**

```
$rule1 = New-Object Amazon.S3.Model.ReplicationRule
$rule1.ID = "Rule-1"
$rule1.Status = "Enabled"
$rule1.Prefix = "TaxDocs"
$rule1.Destination = @{ BucketArn = "arn:aws:s3:::amzn-s3-demo-destination-bucket" }

$rule2 = New-Object Amazon.S3.Model.ReplicationRule
$rule2.ID = "Rule-2"
$rule2.Status = "Enabled"
$rule2.Prefix = "OtherDocs"
$rule2.Destination = @{ BucketArn = "arn:aws:s3:::amzn-s3-demo-destination-bucket" }

$params = @{
    BucketName = "amzn-s3-demo-bucket"
    Configuration_Role = "arn:aws:iam::35667example:role/CrossRegionReplicationRoleForS3"
    Configuration_Rule = $rule1,$rule2
}

Write-S3BucketReplication @params
```
**Example 3: This example updates the replication configuration on the specified bucket to disable the rule controlling replication of objects with the key name prefix "TaxDocs" to the bucket 'amzn-s3-demo-bucket'.**

```
$rule1 = New-Object Amazon.S3.Model.ReplicationRule
$rule1.ID = "Rule-1"
$rule1.Status = "Disabled"
$rule1.Prefix = "TaxDocs"
$rule1.Destination = @{ BucketArn = "arn:aws:s3:::amzn-s3-demo-destination-bucket" }

$params = @{
    BucketName = "amzn-s3-demo-bucket"
    Configuration_Role = "arn:aws:iam::35667example:role/CrossRegionReplicationRoleForS3"
    Configuration_Rule = $rule1
}

Write-S3BucketReplication @params
```
+  For API details, see [PutBucketReplication](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Write-S3BucketRequestPayment`
<a name="s3_PutBucketRequestPayment_powershell_5_topic"></a>

The following code example shows how to use `Write-S3BucketRequestPayment`.

**Tools for PowerShell V5**
**Example 1: Updates the request payment configuration for the bucket named 'amzn-s3-demo-bucket' so that the person requesting downloads from the bucket will be charged for the download. By default the bucket owner pays for downloads. To set the request payment back to the default use 'BucketOwner' for the RequestPaymentConfiguration\_Payer parameter.**

```
Write-S3BucketRequestPayment -BucketName amzn-s3-demo-bucket -RequestPaymentConfiguration_Payer Requester
```
+  For API details, see [PutBucketRequestPayment](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Write-S3BucketTagging`
<a name="s3_PutBucketTagging_powershell_5_topic"></a>

The following code example shows how to use `Write-S3BucketTagging`.

**Tools for PowerShell V5**
**Example 1: This command applies two tags to a bucket named `cloudtrail-test-2018`: a tag with a key of Stage and a value of Test, and a tag with a key of Environment and a value of Alpha. To verify that the tags were added to the bucket, run `Get-S3BucketTagging -BucketName bucket_name`. The results should show the tags that you applied to the bucket in the first command. Note that `Write-S3BucketTagging` overwrites the entire existing tag set on a bucket. To add or delete individual tags, run the Resource Groups and Tagging API cmdlets, `Add-RGTResourceTag` and `Remove-RGTResourceTag`. Alternatively, use Tag Editor in the AWS Management Console to manage S3 bucket tags.**

```
Write-S3BucketTagging -BucketName amzn-s3-demo-bucket -TagSet @( @{ Key="Stage"; Value="Test" }, @{ Key="Environment"; Value="Alpha" } )
```
**Example 2: This command pipes a bucket named `cloudtrail-test-2018` into the `Write-S3BucketTagging` cmdlet. It applies tags Stage:Production and Department:Finance to the bucket. Note that `Write-S3BucketTagging` overwrites the entire existing tag set on a bucket.**

```
Get-S3Bucket -BucketName amzn-s3-demo-bucket | Write-S3BucketTagging -TagSet @( @{ Key="Stage"; Value="Production" }, @{ Key="Department"; Value="Finance" } )
```
+  For API details, see [PutBucketTagging](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Write-S3BucketVersioning`
<a name="s3_PutBucketVersioning_powershell_5_topic"></a>

The following code example shows how to use `Write-S3BucketVersioning`.

**Tools for PowerShell V5**
**Example 1: The command enables versioning for the given S3 bucket.**

```
Write-S3BucketVersioning -BucketName 'amzn-s3-demo-bucket' -VersioningConfig_Status Enabled
```
+  For API details, see [PutBucketVersioning](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Write-S3BucketWebsite`
<a name="s3_PutBucketWebsite_powershell_5_topic"></a>

The following code example shows how to use `Write-S3BucketWebsite`.

**Tools for PowerShell V5**
**Example 1: The command enables website hosting for the given bucket with the index document as 'index.html' and error document as 'error.html'.**

```
Write-S3BucketWebsite -BucketName 'amzn-s3-demo-bucket' -WebsiteConfiguration_IndexDocumentSuffix 'index.html' -WebsiteConfiguration_ErrorDocument 'error.html'
```
+  For API details, see [PutBucketWebsite](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Write-S3LifecycleConfiguration`
<a name="s3_PutLifecycleConfiguration_powershell_5_topic"></a>

The following code example shows how to use `Write-S3LifecycleConfiguration`.

**Tools for PowerShell V5**
**Example 1: This example writes / replaces the configuration provided in the $NewRule. This configuration is making sure to limit the scope objects with given prefix and tag values.**

```
$NewRule = [Amazon.S3.Model.LifecycleRule] @{
		Expiration =  @{
			Days=  50
		}
		Id =  "Test-From-Write-cmdlet-1"
		Filter=  @{
			LifecycleFilterPredicate =  [Amazon.S3.Model.LifecycleAndOperator]@{
				Operands=  @(
					[Amazon.S3.Model.LifecyclePrefixPredicate] @{
						"Prefix" =  "py"
					},
					[Amazon.S3.Model.LifecycleTagPredicate] @{
						"Tag"=  @{
							"Key" =  "non-use"
							"Value" = "yes"
						}
					}
				)
			}
		}
		"Status"= 'Enabled'
		NoncurrentVersionExpiration = @{
			NoncurrentDays = 75
		}
	}

	Write-S3LifecycleConfiguration -BucketName amzn-s3-demo-bucket -Configuration_Rule $NewRule
```
**Example 2: This example sets multiple rules with filtering. $ArchiveRule sets the objects to archive in 30 days to Glacier and 120 to DeepArchive. $ExpireRule expires both current and previous versions in 150 days for objects with 'py' prefix and tag:key 'archieved' set to 'yes'.**

```
$ExpireRule = [Amazon.S3.Model.LifecycleRule] @{
		Expiration =  @{
			Days=  150
		}
		Id =  "Remove-in-150-days"
		Filter=  @{
			LifecycleFilterPredicate =  [Amazon.S3.Model.LifecycleAndOperator]@{
				Operands=  @(
					[Amazon.S3.Model.LifecyclePrefixPredicate] @{
						"Prefix" =  "py"
					},
					[Amazon.S3.Model.LifecycleTagPredicate] @{
						"Tag"=  @{
							"Key" =  "archived"
							"Value" = "yes"
						}
					}
				)
			}
		}
		Status= 'Enabled'
		NoncurrentVersionExpiration = @{
			NoncurrentDays = 150
		}
	}

	$ArchiveRule = [Amazon.S3.Model.LifecycleRule] @{
		Expiration =  $null
		Id =  "Archive-to-Glacier-in-30-days"
		Filter=  @{
			LifecycleFilterPredicate =  [Amazon.S3.Model.LifecycleAndOperator]@{
				Operands= @(
					[Amazon.S3.Model.LifecyclePrefixPredicate] @{
						"Prefix" =  "py"
					},
					[Amazon.S3.Model.LifecycleTagPredicate] @{
						"Tag"=  @{
							"Key" =  "reviewed"
							"Value" = "yes"
						}
					}
				)
			}
		}
		Status = 'Enabled'
		NoncurrentVersionExpiration = @{
			NoncurrentDays = 75
		}
		Transitions = @(
			@{
				Days = 30
				"StorageClass"= 'Glacier'
			},
			@{
				Days = 120
				"StorageClass"= [Amazon.S3.S3StorageClass]::DeepArchive
			}
		)
	}

	Write-S3LifecycleConfiguration -BucketName amzn-s3-demo-bucket -Configuration_Rule $ExpireRule,$ArchiveRule
```
+  For API details, see [PutLifecycleConfiguration](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Write-S3Object`
<a name="s3_PutObject_powershell_5_topic"></a>

The following code example shows how to use `Write-S3Object`.

**Tools for PowerShell V5**
**Example 1: This command uploads the single file "local-sample.txt" to Amazon S3, creating an object with key "sample.txt" in bucket "test-files".**

```
Write-S3Object -BucketName amzn-s3-demo-bucket -Key "sample.txt" -File .\local-sample.txt
```
**Example 2: This command uploads the single file "sample.txt" to Amazon S3, creating an object with key "sample.txt" in bucket "test-files". If the -Key parameter is not supplied, the filename is used as the S3 object key.**

```
Write-S3Object -BucketName amzn-s3-demo-bucket -File .\sample.txt
```
**Example 3: This command uploads the single file "local-sample.txt" to Amazon S3, creating an object with key "prefix/to/sample.txt" in bucket "test-files".**

```
Write-S3Object -BucketName amzn-s3-demo-bucket -Key "prefix/to/sample.txt" -File .\local-sample.txt
```
**Example 4: This command uploads all files in the subdirectory "Scripts" to the bucket "test-files" and applies the common key prefix "SampleScripts" to each object. Each uploaded file will have a key of "SampleScripts/filename" where 'filename' varies.**

```
Write-S3Object -BucketName amzn-s3-demo-bucket -Folder .\Scripts -KeyPrefix SampleScripts\
```
**Example 5: This command uploads all \*.ps1 files in the local director "Scripts" to bucket "test-files" and applies the common key prefix "SampleScripts" to each object. Each uploaded file will have a key of "SampleScripts/filename.ps1" where 'filename' varies.**

```
Write-S3Object -BucketName amzn-s3-demo-bucket -Folder .\Scripts -KeyPrefix SampleScripts\ -SearchPattern *.ps1
```
**Example 6: This command creates a new S3 object containing the specified content string with key 'sample.txt'.**

```
Write-S3Object -BucketName amzn-s3-demo-bucket -Key "sample.txt" -Content "object contents"
```
**Example 7: This command uploads the specified file (the filename is used as the key) and applies the specified tags to the new object.**

```
Write-S3Object -BucketName amzn-s3-demo-bucket -File "sample.txt" -TagSet @{Key="key1";Value="value1"},@{Key="key2";Value="value2"}
```
**Example 8: This command recursively uploads the specified folder and applies the specified tags to all the new objects.**

```
Write-S3Object -BucketName amzn-s3-demo-bucket -Folder . -KeyPrefix "TaggedFiles" -Recurse -TagSet @{Key="key1";Value="value1"},@{Key="key2";Value="value2"}
```
+  For API details, see [PutObject](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Write-S3ObjectRetention`
<a name="s3_PutObjectRetention_powershell_5_topic"></a>

The following code example shows how to use `Write-S3ObjectRetention`.

**Tools for PowerShell V5**
**Example 1: The command enables governance retention mode untill the date '31st Dec 2019 00:00:00' for 'testfile.txt' object in the given S3 bucket.**

```
Write-S3ObjectRetention -BucketName 'amzn-s3-demo-bucket' -Key 'testfile.txt' -Retention_Mode GOVERNANCE -Retention_RetainUntilDate "2019-12-31T00:00:00"
```
+  For API details, see [PutObjectRetention](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.
