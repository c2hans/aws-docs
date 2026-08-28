---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html
---

# CreateAccessPoint
<a name="API_control_CreateAccessPoint"></a>

Creates an access point and associates it to a specified bucket. For more information, see [Managing access to shared datasets with access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html) or [Managing access to shared datasets in directory buckets with access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets.html) in the *Amazon S3 User Guide*.

To create an access point and attach it to a volume on an Amazon FSx file system, see [CreateAndAttachS3AccessPoint](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateAndAttachS3AccessPoint.html) in the *Amazon FSx API Reference*.

**Note**
S3 on Outposts only supports VPC-style access points.
For more information, see [ Accessing Amazon S3 on Outposts using virtual private cloud (VPC) only access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html) in the *Amazon S3 User Guide*.

All Amazon S3 on Outposts REST API requests for this action require an additional parameter of `x-amz-outpost-id` to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of `s3-control`. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the `x-amz-outpost-id` derived by using the access point ARN, see the [Examples](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html#API_control_CreateAccessPoint_Examples) section.

The following actions are related to `CreateAccessPoint`:
+  [GetAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html)
+  [DeleteAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPoint.html)
+  [ListAccessPoints](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPoints.html)
+  [ListAccessPointsForDirectoryBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPointsForDirectoryBuckets.html)

## Request Syntax
<a name="API_control_CreateAccessPoint_RequestSyntax"></a>

```
PUT /v20180820/accesspoint/{{name}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
<?xml version="1.0" encoding="UTF-8"?>
<CreateAccessPointRequest xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <Bucket>{{string}}</Bucket>
   <VpcConfiguration>
      <VpcId>{{string}}</VpcId>
   </VpcConfiguration>
   <PublicAccessBlockConfiguration>
      <BlockPublicAcls>{{boolean}}</BlockPublicAcls>
      <BlockPublicPolicy>{{boolean}}</BlockPublicPolicy>
      <IgnorePublicAcls>{{boolean}}</IgnorePublicAcls>
      <RestrictPublicBuckets>{{boolean}}</RestrictPublicBuckets>
   </PublicAccessBlockConfiguration>
   <BucketAccountId>{{string}}</BucketAccountId>
   <Scope>
      <Permissions>
         <Permission>{{string}}</Permission>
      </Permissions>
      <Prefixes>
         <Prefix>{{string}}</Prefix>
      </Prefixes>
   </Scope>
   <Tags>
      <Tag>
         <Key>{{string}}</Key>
         <Value>{{string}}</Value>
      </Tag>
   </Tags>
</CreateAccessPointRequest>
```

## URI Request Parameters
<a name="API_control_CreateAccessPoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_control_CreateAccessPoint_RequestSyntax) **   <a name="AmazonS3-control_CreateAccessPoint-request-uri-uri-Name"></a>
The name you want to assign to this access point.
For directory buckets, the access point name must consist of a base name that you provide and suffix that includes the `ZoneID` (AWS Availability Zone or Local Zone) of your bucket location, followed by `--xa-s3`. For more information, see [Managing access to shared datasets in directory buckets with access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets.html) in the *Amazon S3 User Guide*.
Length Constraints: Minimum length of 3. Maximum length of 255.
Required: Yes

 ** [x-amz-account-id](#API_control_CreateAccessPoint_RequestSyntax) **   <a name="AmazonS3-control_CreateAccessPoint-request-header-AccountId"></a>
The AWS account ID for the account that owns the specified access point.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_CreateAccessPoint_RequestBody"></a>

The request accepts the following data in XML format.

 ** [CreateAccessPointRequest](#API_control_CreateAccessPoint_RequestSyntax) **   <a name="AmazonS3-control_CreateAccessPoint-request-CreateAccessPointRequest"></a>
Root level tag for the CreateAccessPointRequest parameters.
Required: Yes

 ** [Bucket](#API_control_CreateAccessPoint_RequestSyntax) **   <a name="AmazonS3-control_CreateAccessPoint-request-Bucket"></a>
The name of the bucket that you want to associate this access point with.
For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.
For using this parameter with S3 on Outposts with the AWS SDK and CLI, you must specify the ARN of the bucket accessed in the format `arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name>`. For example, to access the bucket `reports` through Outpost `my-outpost` owned by account `123456789012` in Region `us-west-2`, use the URL encoding of `arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports`. The value must be URL encoded.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Required: Yes

 ** [BucketAccountId](#API_control_CreateAccessPoint_RequestSyntax) **   <a name="AmazonS3-control_CreateAccessPoint-request-BucketAccountId"></a>
The AWS account ID associated with the S3 bucket associated with this access point.
For same account access point when your bucket and access point belong to the same account owner, the `BucketAccountId` is not required. For cross-account access point when your bucket and access point are not in the same account, the `BucketAccountId` is required.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: No

 ** [PublicAccessBlockConfiguration](#API_control_CreateAccessPoint_RequestSyntax) **   <a name="AmazonS3-control_CreateAccessPoint-request-PublicAccessBlockConfiguration"></a>
 The `PublicAccessBlock` configuration that you want to apply to the access point.
Type: [PublicAccessBlockConfiguration](API_control_PublicAccessBlockConfiguration.md) data type
Required: No

 ** [Scope](#API_control_CreateAccessPoint_RequestSyntax) **   <a name="AmazonS3-control_CreateAccessPoint-request-Scope"></a>
For directory buckets, you can filter access control to specific prefixes, API operations, or a combination of both. For more information, see [Managing access to shared datasets in directory buckets with access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets.html) in the *Amazon S3 User Guide*.
Scope is only supported for access points attached to directory buckets.
Type: [Scope](API_control_Scope.md) data type
Required: No

 ** [Tags](#API_control_CreateAccessPoint_RequestSyntax) **   <a name="AmazonS3-control_CreateAccessPoint-request-Tags"></a>
An array of tags that you can apply to an access point. Tags are key-value pairs of metadata used to control access to your access points. For more information about tags, see [Using tags with Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html). For information about tagging access points, see [Using tags for attribute-based access control (ABAC)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#using-tags-for-abac).
Type: Array of [Tag](API_control_Tag.md) data types
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [VpcConfiguration](#API_control_CreateAccessPoint_RequestSyntax) **   <a name="AmazonS3-control_CreateAccessPoint-request-VpcConfiguration"></a>
If you include this field, Amazon S3 restricts access to this access point to requests from the specified virtual private cloud (VPC).
This is required for creating an access point for Amazon S3 on Outposts buckets.
Type: [VpcConfiguration](API_control_VpcConfiguration.md) data type
Required: No

## Response Syntax
<a name="API_control_CreateAccessPoint_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<CreateAccessPointResult>
   <AccessPointArn>string</AccessPointArn>
   <Alias>string</Alias>
</CreateAccessPointResult>
```

## Response Elements
<a name="API_control_CreateAccessPoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [CreateAccessPointResult](#API_control_CreateAccessPoint_ResponseSyntax) **   <a name="AmazonS3-control_CreateAccessPoint-response-CreateAccessPointResult"></a>
Root level tag for the CreateAccessPointResult parameters.
Required: Yes

 ** [AccessPointArn](#API_control_CreateAccessPoint_ResponseSyntax) **   <a name="AmazonS3-control_CreateAccessPoint-response-AccessPointArn"></a>
The ARN of the access point.
This is only supported by Amazon S3 on Outposts.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 128.

 ** [Alias](#API_control_CreateAccessPoint_ResponseSyntax) **   <a name="AmazonS3-control_CreateAccessPoint-response-Alias"></a>
The name or alias of the access point.
Type: String
Length Constraints: Maximum length of 63.
Pattern: `^[0-9a-z\\-]{63}`

## Examples
<a name="API_control_CreateAccessPoint_Examples"></a>

### Sample request for creating an access point for an Amazon S3 on Outposts bucket
<a name="API_control_CreateAccessPoint_Example_1"></a>

This request creates an access point for S3 on Outposts bucket.

```
            PUT /v20180820/accesspoint/example-access-point HTTP/1.1
            Host:s3-outposts.<Region>.amazonaws.com
            x-amz-account-id: example-account-id
            x-amz-outpost-id: op-01ac5d28a6a232904
            <?xml version="1.0" encoding="UTF-8"?>
               <CreateAccessPointRequest xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
                  <Bucket>example-outpost-bucket </Bucket>
               </CreateAccessPointRequest>
```

## See Also
<a name="API_control_CreateAccessPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/CreateAccessPoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/CreateAccessPoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/CreateAccessPoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/CreateAccessPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/CreateAccessPoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/CreateAccessPoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/CreateAccessPoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/CreateAccessPoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/CreateAccessPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/CreateAccessPoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
