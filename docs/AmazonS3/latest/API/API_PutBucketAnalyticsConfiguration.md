---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAnalyticsConfiguration.html
---

# PutBucketAnalyticsConfiguration
<a name="API_PutBucketAnalyticsConfiguration"></a>

**Note**
This operation is not supported for directory buckets.

Sets an analytics configuration for the bucket (specified by the analytics configuration ID). You can have up to 1,000 analytics configurations per bucket.

You can choose to have storage class analysis export analysis reports sent to a comma-separated values (CSV) flat file. See the `DataExport` request element. Reports are updated daily and are based on the object filters that you configure. When selecting data export, you specify a destination bucket and an optional destination prefix where the file is written. You can export the data to a destination bucket in a different account. However, the destination bucket must be in the same Region as the bucket that you are making the PUT analytics configuration to. For more information, see [Amazon S3 Analytics – Storage Class Analysis](https://docs.aws.amazon.com/AmazonS3/latest/dev/analytics-storage-class.html).

**Important**
You must create a bucket policy on the destination bucket where the exported file is written to grant permissions to Amazon S3 to write objects to the bucket. For an example policy, see [Granting Permissions for Amazon S3 Inventory and Storage Class Analysis](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html#example-bucket-policies-use-case-9).

To use this operation, you must have permissions to perform the `s3:PutAnalyticsConfiguration` action. The bucket owner has this permission by default. The bucket owner can grant this permission to others. For more information about permissions, see [Permissions Related to Bucket Subresource Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources) and [Managing Access Permissions to Your Amazon S3 Resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html).

 `PutBucketAnalyticsConfiguration` has the following special errors:
+
  +  *HTTP Error: HTTP 400 Bad Request*
  +  *Code: InvalidArgument*
  +  *Cause: Invalid argument.*
+
  +  *HTTP Error: HTTP 400 Bad Request*
  +  *Code: TooManyConfigurations*
  +  *Cause: You are attempting to create a new configuration but have already reached the 1,000-configuration limit.*
+
  +  *HTTP Error: HTTP 403 Forbidden*
  +  *Code: AccessDenied*
  +  *Cause: You are not the owner of the specified bucket, or you do not have the s3:PutAnalyticsConfiguration bucket permission to set the configuration on the bucket.*

The following operations are related to `PutBucketAnalyticsConfiguration`:
+  [GetBucketAnalyticsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAnalyticsConfiguration.html)
+  [DeleteBucketAnalyticsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketAnalyticsConfiguration.html)
+  [ListBucketAnalyticsConfigurations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBucketAnalyticsConfigurations.html)

**Important**
You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax
<a name="API_PutBucketAnalyticsConfiguration_RequestSyntax"></a>

```
PUT /?analytics&id={{Id}} HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
<?xml version="1.0" encoding="UTF-8"?>
<AnalyticsConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <Id>{{string}}</Id>
   <Filter>
      <And>
         <Prefix>{{string}}</Prefix>
         <Tag>
            <Key>{{string}}</Key>
            <Value>{{string}}</Value>
         </Tag>
         ...
      </And>
      <Prefix>{{string}}</Prefix>
      <Tag>
         <Key>{{string}}</Key>
         <Value>{{string}}</Value>
      </Tag>
   </Filter>
   <StorageClassAnalysis>
      <DataExport>
         <Destination>
            <S3BucketDestination>
               <Bucket>{{string}}</Bucket>
               <BucketAccountId>{{string}}</BucketAccountId>
               <Format>{{string}}</Format>
               <Prefix>{{string}}</Prefix>
            </S3BucketDestination>
         </Destination>
         <OutputSchemaVersion>{{string}}</OutputSchemaVersion>
      </DataExport>
   </StorageClassAnalysis>
</AnalyticsConfiguration>
```

## URI Request Parameters
<a name="API_PutBucketAnalyticsConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Bucket](#API_PutBucketAnalyticsConfiguration_RequestSyntax) **   <a name="AmazonS3-PutBucketAnalyticsConfiguration-request-header-Bucket"></a>
The name of the bucket to which an analytics configuration is stored.
Required: Yes

 ** [id](#API_PutBucketAnalyticsConfiguration_RequestSyntax) **   <a name="AmazonS3-PutBucketAnalyticsConfiguration-request-uri-querystring-Id"></a>
The ID that identifies the analytics configuration.
Required: Yes

 ** [x-amz-expected-bucket-owner](#API_PutBucketAnalyticsConfiguration_RequestSyntax) **   <a name="AmazonS3-PutBucketAnalyticsConfiguration-request-header-ExpectedBucketOwner"></a>
The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Request Body
<a name="API_PutBucketAnalyticsConfiguration_RequestBody"></a>

The request accepts the following data in XML format.

 ** [AnalyticsConfiguration](#API_PutBucketAnalyticsConfiguration_RequestSyntax) **   <a name="AmazonS3-PutBucketAnalyticsConfiguration-request-AnalyticsConfiguration"></a>
Root level tag for the AnalyticsConfiguration parameters.
Required: Yes

 ** [Filter](#API_PutBucketAnalyticsConfiguration_RequestSyntax) **   <a name="AmazonS3-PutBucketAnalyticsConfiguration-request-Filter"></a>
The filter used to describe a set of objects for analyses. A filter must have exactly one prefix, one tag, or one conjunction (AnalyticsAndOperator). If no filter is provided, all objects will be considered in any analysis.
Type: [AnalyticsFilter](API_AnalyticsFilter.md) data type
Required: No

 ** [Id](#API_PutBucketAnalyticsConfiguration_RequestSyntax) **   <a name="AmazonS3-PutBucketAnalyticsConfiguration-request-Id"></a>
The ID that identifies the analytics configuration.
Type: String
Required: Yes

 ** [StorageClassAnalysis](#API_PutBucketAnalyticsConfiguration_RequestSyntax) **   <a name="AmazonS3-PutBucketAnalyticsConfiguration-request-StorageClassAnalysis"></a>
 Contains data related to access patterns to be collected and made available to analyze the tradeoffs between different storage classes.
Type: [StorageClassAnalysis](API_StorageClassAnalysis.md) data type
Required: Yes

## Response Syntax
<a name="API_PutBucketAnalyticsConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutBucketAnalyticsConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Examples
<a name="API_PutBucketAnalyticsConfiguration_Examples"></a>

### Example 1: Creating an analytics configuration
<a name="API_PutBucketAnalyticsConfiguration_Example_1"></a>

The following PUT request for the bucket `examplebucket` creates a new or replaces an existing analytics configuration with the ID `report1`. The configuration is defined in the request body.

```
PUT /?analytics&id=report1 HTTP/1.1
Host: examplebucket.s3.<Region>.amazonaws.com
Date: Mon, 31 Oct 2016 12:00:00 GMT
Authorization: authorization string
Content-Length: length

<?xml version="1.0" encoding="UTF-8"?>
<AnalyticsConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <Id>report1</Id>
  <Filter>
    <And>
      <Prefix>images/</Prefix>
      <Tag>
        <Key>dog</Key>
        <Value>corgi</Value>
      </Tag>
    </And>
  </Filter>
  <StorageClassAnalysis>
    <DataExport>
      <OutputSchemaVersion>V_1</OutputSchemaVersion>
      <Destination>
        <S3BucketDestination>
          <Format>CSV</Format>
          <BucketAccountId>123456789012</BucketAccountId>
          <Bucket>arn:aws:s3:::destination-bucket</Bucket>
          <Prefix>destination-prefix</Prefix>
        </S3BucketDestination>
      </Destination>
    </DataExport>
  </StorageClassAnalysis>
</AnalyticsConfiguration>
```

### Sample Response
<a name="API_PutBucketAnalyticsConfiguration_Example_2"></a>

This example illustrates one usage of PutBucketAnalyticsConfiguration.

```
HTTP/1.1 200 OK
x-amz-id-2: YgIPIfBiKa2bj0KMg95r/0zo3emzU4dzsD4rcKCHQUAdQkf3ShJTOOpXUueF6QKo
x-amz-request-id: 236A8905248E5A01
Date: Mon, 31 Oct 2016 12:00:00 GMT
Content-Length: 0
Server: AmazonS3
```

## See Also
<a name="API_PutBucketAnalyticsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketAnalyticsConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/PutBucketAnalyticsConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketAnalyticsConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketAnalyticsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketAnalyticsConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketAnalyticsConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketAnalyticsConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketAnalyticsConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketAnalyticsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketAnalyticsConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
