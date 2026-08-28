---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketLifecycleConfiguration.html
---

# PutBucketLifecycleConfiguration
<a name="API_control_PutBucketLifecycleConfiguration"></a>

**Note**
This action puts a lifecycle configuration to an Amazon S3 on Outposts bucket. To put a lifecycle configuration to an S3 bucket, see [PutBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html) in the *Amazon S3 API Reference*.

Creates a new lifecycle configuration for the S3 on Outposts bucket or replaces an existing lifecycle configuration. Outposts buckets only support lifecycle configurations that delete/expire objects after a certain period of time and abort incomplete multipart uploads.

All Amazon S3 on Outposts REST API requests for this action require an additional parameter of `x-amz-outpost-id` to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of `s3-control`. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the `x-amz-outpost-id` derived by using the access point ARN, see the [Examples](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketLifecycleConfiguration.html#API_control_PutBucketLifecycleConfiguration_Examples) section.

The following actions are related to `PutBucketLifecycleConfiguration`:
+  [GetBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketLifecycleConfiguration.html)
+  [DeleteBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketLifecycleConfiguration.html)

## Request Syntax
<a name="API_control_PutBucketLifecycleConfiguration_RequestSyntax"></a>

```
PUT /v20180820/bucket/{{name}}/lifecycleconfiguration HTTP/1.1
Host: {{Bucket}}.s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
<?xml version="1.0" encoding="UTF-8"?>
<LifecycleConfiguration xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <Rules>
      <Rule>
         <AbortIncompleteMultipartUpload>
            <DaysAfterInitiation>{{integer}}</DaysAfterInitiation>
         </AbortIncompleteMultipartUpload>
         <Expiration>
            <Date>{{timestamp}}</Date>
            <Days>{{integer}}</Days>
            <ExpiredObjectDeleteMarker>{{boolean}}</ExpiredObjectDeleteMarker>
         </Expiration>
         <Filter>
            <And>
               <ObjectSizeGreaterThan>{{long}}</ObjectSizeGreaterThan>
               <ObjectSizeLessThan>{{long}}</ObjectSizeLessThan>
               <Prefix>{{string}}</Prefix>
               <Tags>
                  <S3Tag>
                     <Key>{{string}}</Key>
                     <Value>{{string}}</Value>
                  </S3Tag>
               </Tags>
            </And>
            <ObjectSizeGreaterThan>{{long}}</ObjectSizeGreaterThan>
            <ObjectSizeLessThan>{{long}}</ObjectSizeLessThan>
            <Prefix>{{string}}</Prefix>
            <Tag>
               <Key>{{string}}</Key>
               <Value>{{string}}</Value>
            </Tag>
         </Filter>
         <ID>{{string}}</ID>
         <NoncurrentVersionExpiration>
            <NewerNoncurrentVersions>{{integer}}</NewerNoncurrentVersions>
            <NoncurrentDays>{{integer}}</NoncurrentDays>
         </NoncurrentVersionExpiration>
         <NoncurrentVersionTransitions>
            <NoncurrentVersionTransition>
               <NoncurrentDays>{{integer}}</NoncurrentDays>
               <StorageClass>{{string}}</StorageClass>
            </NoncurrentVersionTransition>
         </NoncurrentVersionTransitions>
         <Status>{{string}}</Status>
         <Transitions>
            <Transition>
               <Date>{{timestamp}}</Date>
               <Days>{{integer}}</Days>
               <StorageClass>{{string}}</StorageClass>
            </Transition>
         </Transitions>
      </Rule>
   </Rules>
</LifecycleConfiguration>
```

## URI Request Parameters
<a name="API_control_PutBucketLifecycleConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_control_PutBucketLifecycleConfiguration_RequestSyntax) **   <a name="AmazonS3-control_PutBucketLifecycleConfiguration-request-header-Bucket"></a>
The name of the bucket for which to set the configuration.
Length Constraints: Minimum length of 3. Maximum length of 255.
Required: Yes

 ** [x-amz-account-id](#API_control_PutBucketLifecycleConfiguration_RequestSyntax) **   <a name="AmazonS3-control_PutBucketLifecycleConfiguration-request-header-AccountId"></a>
The AWS account ID of the Outposts bucket.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_PutBucketLifecycleConfiguration_RequestBody"></a>

The request accepts the following data in XML format.

 ** [LifecycleConfiguration](#API_control_PutBucketLifecycleConfiguration_RequestSyntax) **   <a name="AmazonS3-control_PutBucketLifecycleConfiguration-request-LifecycleConfiguration"></a>
Root level tag for the LifecycleConfiguration parameters.
Required: Yes

 ** [Rules](#API_control_PutBucketLifecycleConfiguration_RequestSyntax) **   <a name="AmazonS3-control_PutBucketLifecycleConfiguration-request-Rules"></a>
A lifecycle rule for individual objects in an Outposts bucket.
Type: Array of [LifecycleRule](API_control_LifecycleRule.md) data types
Required: No

## Response Syntax
<a name="API_control_PutBucketLifecycleConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_control_PutBucketLifecycleConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Examples
<a name="API_control_PutBucketLifecycleConfiguration_Examples"></a>

### Sample PutBucketLifecycleConfiguration request on an Amazon S3 on Outposts bucket
<a name="API_control_PutBucketLifecycleConfiguration_Example_1"></a>

This request puts a lifecycle configuration on an Outposts bucket named `example-outpost-bucket`.

```
            PUT /v20180820/bucket/example-outpost-bucket/lifecycleconfiguration HTTP/1.1
            Host:s3-outposts.<Region>.amazonaws.com
            x-amz-account-id: example-account-id
            x-amz-outpost-id: op-01ac5d28a6a232904
            Content-Length: 0
            Date: Wed, 01 Mar  2006 12:00:00 GMT
            Content-MD5: q6yJDlIkcBaGGfb3QLY69A==
            Authorization: authorization string
            Content-Length: 214

            <LifecycleConfiguration>
              <Rule>
                <ID>id2</ID>
                <Filter>
                   <Prefix>logs/</Prefix>
                </Filter>
                <Status>Enabled</Status>
                <Expiration>
                  <Days>365</Days>
                </Expiration>
              </Rule>
            </LifecycleConfiguration>
```

## See Also
<a name="API_control_PutBucketLifecycleConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/PutBucketLifecycleConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/PutBucketLifecycleConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutBucketLifecycleConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/PutBucketLifecycleConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutBucketLifecycleConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/PutBucketLifecycleConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/PutBucketLifecycleConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/PutBucketLifecycleConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutBucketLifecycleConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutBucketLifecycleConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
