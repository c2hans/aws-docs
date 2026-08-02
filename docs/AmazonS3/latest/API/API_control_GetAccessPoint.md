---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html
---

# GetAccessPoint
<a name="API_control_GetAccessPoint"></a>

Returns configuration information about the specified access point.

All Amazon S3 on Outposts REST API requests for this action require an additional parameter of `x-amz-outpost-id` to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of `s3-control`. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the `x-amz-outpost-id` derived by using the access point ARN, see the [Examples](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html#API_control_GetAccessPoint_Examples) section.

The following actions are related to `GetAccessPoint`:
+  [CreateAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html)
+  [DeleteAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPoint.html)
+  [ListAccessPoints](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPoints.html)

## Request Syntax
<a name="API_control_GetAccessPoint_RequestSyntax"></a>

```
GET /v20180820/accesspoint/{{name}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_GetAccessPoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_control_GetAccessPoint_RequestSyntax) **   <a name="AmazonS3-control_GetAccessPoint-request-uri-uri-Name"></a>
The name of the access point whose configuration information you want to retrieve.
For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.
For using this parameter with S3 on Outposts with the AWS SDK and CLI, you must specify the ARN of the access point accessed in the format `arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/accesspoint/<my-accesspoint-name>`. For example, to access the access point `reports-ap` through Outpost `my-outpost` owned by account `123456789012` in Region `us-west-2`, use the URL encoding of `arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/accesspoint/reports-ap`. The value must be URL encoded.
Length Constraints: Minimum length of 3. Maximum length of 255.
Required: Yes

 ** [x-amz-account-id](#API_control_GetAccessPoint_RequestSyntax) **   <a name="AmazonS3-control_GetAccessPoint-request-header-AccountId"></a>
The AWS account ID for the account that owns the specified access point.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_GetAccessPoint_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_GetAccessPoint_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetAccessPointResult>
   <Name>string</Name>
   <Bucket>string</Bucket>
   <NetworkOrigin>string</NetworkOrigin>
   <VpcConfiguration>
      <VpcId>string</VpcId>
   </VpcConfiguration>
   <PublicAccessBlockConfiguration>
      <BlockPublicAcls>boolean</BlockPublicAcls>
      <BlockPublicPolicy>boolean</BlockPublicPolicy>
      <IgnorePublicAcls>boolean</IgnorePublicAcls>
      <RestrictPublicBuckets>boolean</RestrictPublicBuckets>
   </PublicAccessBlockConfiguration>
   <CreationDate>timestamp</CreationDate>
   <Alias>string</Alias>
   <AccessPointArn>string</AccessPointArn>
   <Endpoints>
      <entry>
         <key>string</key>
         <value>string</value>
      </entry>
   </Endpoints>
   <BucketAccountId>string</BucketAccountId>
   <DataSourceId>string</DataSourceId>
   <DataSourceType>string</DataSourceType>
</GetAccessPointResult>
```

## Response Elements
<a name="API_control_GetAccessPoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetAccessPointResult](#API_control_GetAccessPoint_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessPoint-response-GetAccessPointResult"></a>
Root level tag for the GetAccessPointResult parameters.
Required: Yes

 ** [AccessPointArn](#API_control_GetAccessPoint_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessPoint-response-AccessPointArn"></a>
The ARN of the access point.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 128.

 ** [Alias](#API_control_GetAccessPoint_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessPoint-response-Alias"></a>
The name or alias of the access point.
Type: String
Length Constraints: Maximum length of 63.
Pattern: `^[0-9a-z\\-]{63}`

 ** [Bucket](#API_control_GetAccessPoint_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessPoint-response-Bucket"></a>
The name of the bucket associated with the specified access point.
Type: String
Length Constraints: Maximum length of 255.

 ** [BucketAccountId](#API_control_GetAccessPoint_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessPoint-response-BucketAccountId"></a>
The AWS account ID associated with the S3 bucket associated with this access point.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`

 ** [CreationDate](#API_control_GetAccessPoint_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessPoint-response-CreationDate"></a>
The date and time when the specified access point was created.
Type: Timestamp

 ** [DataSourceId](#API_control_GetAccessPoint_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessPoint-response-DataSourceId"></a>
The unique identifier for the data source of the access point.
Type: String
Length Constraints: Maximum length of 191.

 ** [DataSourceType](#API_control_GetAccessPoint_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessPoint-response-DataSourceType"></a>
The type of the data source that the access point is attached to.
Type: String

 ** [Endpoints](#API_control_GetAccessPoint_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessPoint-response-Endpoints"></a>
The VPC endpoint for the access point.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Value Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [Name](#API_control_GetAccessPoint_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessPoint-response-Name"></a>
The name of the specified access point.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.

 ** [NetworkOrigin](#API_control_GetAccessPoint_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessPoint-response-NetworkOrigin"></a>
Indicates whether this access point allows access from the public internet. If `VpcConfiguration` is specified for this access point, then `NetworkOrigin` is `VPC`, and the access point doesn't allow access from the public internet. Otherwise, `NetworkOrigin` is `Internet`, and the access point allows access from the public internet, subject to the access point and bucket access policies.
This will always be true for an Amazon S3 on Outposts access point
Type: String
Valid Values: `Internet | VPC`

 ** [PublicAccessBlockConfiguration](#API_control_GetAccessPoint_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessPoint-response-PublicAccessBlockConfiguration"></a>
The `PublicAccessBlock` configuration that you want to apply to this Amazon S3 account. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see [The Meaning of "Public"](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status) in the *Amazon S3 User Guide*.
This data type is not supported for Amazon S3 on Outposts.
Type: [PublicAccessBlockConfiguration](API_control_PublicAccessBlockConfiguration.md) data type

 ** [VpcConfiguration](#API_control_GetAccessPoint_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessPoint-response-VpcConfiguration"></a>
Contains the virtual private cloud (VPC) configuration for the specified access point.
This element is empty if this access point is an Amazon S3 on Outposts access point that is used by other AWS services.
Type: [VpcConfiguration](API_control_VpcConfiguration.md) data type

## Examples
<a name="API_control_GetAccessPoint_Examples"></a>

### Sample request syntax for getting an Amazon S3 on Outposts access point
<a name="API_control_GetAccessPoint_Example_1"></a>

The following request returns the access point of the specified S3 on Outposts access point.

```
           GET /v20180820/accesspoint/example-access-point HTTP/1.1
           Host: s3-outposts.<Region>.amazonaws.com
           Date: Wed, 28 Oct 2020 22:32:00 GMT
           Authorization: authorization string
           x-amz-account-id: example-account-id
           x-amz-outpost-id: op-01ac5d28a6a232904
```

## See Also
<a name="API_control_GetAccessPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetAccessPoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/GetAccessPoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetAccessPoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetAccessPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetAccessPoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetAccessPoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetAccessPoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetAccessPoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetAccessPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetAccessPoint)
