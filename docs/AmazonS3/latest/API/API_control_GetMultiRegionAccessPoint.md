---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPoint.html
---

# GetMultiRegionAccessPoint
<a name="API_control_GetMultiRegionAccessPoint"></a>

**Note**
This operation is not supported by directory buckets.

Returns configuration information about the specified Multi-Region Access Point.

This action will always be routed to the US West (Oregon) Region. For more information about the restrictions around working with Multi-Region Access Points, see [Multi-Region Access Point restrictions and limitations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointRestrictions.html) in the *Amazon S3 User Guide*.

The following actions are related to `GetMultiRegionAccessPoint`:
+  [CreateMultiRegionAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateMultiRegionAccessPoint.html)
+  [DeleteMultiRegionAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteMultiRegionAccessPoint.html)
+  [DescribeMultiRegionAccessPointOperation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeMultiRegionAccessPointOperation.html)
+  [ListMultiRegionAccessPoints](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListMultiRegionAccessPoints.html)

## Request Syntax
<a name="API_control_GetMultiRegionAccessPoint_RequestSyntax"></a>

```
GET /v20180820/mrap/instances/{{name+}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_GetMultiRegionAccessPoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_control_GetMultiRegionAccessPoint_RequestSyntax) **   <a name="AmazonS3-control_GetMultiRegionAccessPoint-request-uri-uri-Name"></a>
The name of the Multi-Region Access Point whose configuration information you want to receive. The name of the Multi-Region Access Point is different from the alias. For more information about the distinction between the name and the alias of an Multi-Region Access Point, see [Rules for naming Amazon S3 Multi-Region Access Points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/CreatingMultiRegionAccessPoints.html#multi-region-access-point-naming) in the *Amazon S3 User Guide*.
Length Constraints: Maximum length of 50.
Pattern: `^[a-z0-9][-a-z0-9]{1,48}[a-z0-9]$`
Required: Yes

 ** [x-amz-account-id](#API_control_GetMultiRegionAccessPoint_RequestSyntax) **   <a name="AmazonS3-control_GetMultiRegionAccessPoint-request-header-AccountId"></a>
The AWS account ID for the owner of the Multi-Region Access Point.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_GetMultiRegionAccessPoint_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_GetMultiRegionAccessPoint_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetMultiRegionAccessPointResult>
   <AccessPoint>
      <Alias>string</Alias>
      <CreatedAt>timestamp</CreatedAt>
      <Name>string</Name>
      <PublicAccessBlock>
         <BlockPublicAcls>boolean</BlockPublicAcls>
         <BlockPublicPolicy>boolean</BlockPublicPolicy>
         <IgnorePublicAcls>boolean</IgnorePublicAcls>
         <RestrictPublicBuckets>boolean</RestrictPublicBuckets>
      </PublicAccessBlock>
      <Regions>
         <Region>
            <Bucket>string</Bucket>
            <BucketAccountId>string</BucketAccountId>
            <Region>string</Region>
         </Region>
      </Regions>
      <Status>string</Status>
   </AccessPoint>
</GetMultiRegionAccessPointResult>
```

## Response Elements
<a name="API_control_GetMultiRegionAccessPoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetMultiRegionAccessPointResult](#API_control_GetMultiRegionAccessPoint_ResponseSyntax) **   <a name="AmazonS3-control_GetMultiRegionAccessPoint-response-GetMultiRegionAccessPointResult"></a>
Root level tag for the GetMultiRegionAccessPointResult parameters.
Required: Yes

 ** [AccessPoint](#API_control_GetMultiRegionAccessPoint_ResponseSyntax) **   <a name="AmazonS3-control_GetMultiRegionAccessPoint-response-AccessPoint"></a>
A container element containing the details of the requested Multi-Region Access Point.
Type: [MultiRegionAccessPointReport](API_control_MultiRegionAccessPointReport.md) data type

## See Also
<a name="API_control_GetMultiRegionAccessPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetMultiRegionAccessPoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/GetMultiRegionAccessPoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetMultiRegionAccessPoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetMultiRegionAccessPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetMultiRegionAccessPoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetMultiRegionAccessPoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetMultiRegionAccessPoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetMultiRegionAccessPoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetMultiRegionAccessPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetMultiRegionAccessPoint)
