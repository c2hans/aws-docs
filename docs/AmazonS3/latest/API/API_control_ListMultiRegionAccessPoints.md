---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListMultiRegionAccessPoints.html
---

# ListMultiRegionAccessPoints
<a name="API_control_ListMultiRegionAccessPoints"></a>

**Note**
This operation is not supported by directory buckets.

Returns a list of the Multi-Region Access Points currently associated with the specified AWS account. Each call can return up to 100 Multi-Region Access Points, the maximum number of Multi-Region Access Points that can be associated with a single account.

This action will always be routed to the US West (Oregon) Region. For more information about the restrictions around working with Multi-Region Access Points, see [Multi-Region Access Point restrictions and limitations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointRestrictions.html) in the *Amazon S3 User Guide*.

The following actions are related to `ListMultiRegionAccessPoint`:
+  [CreateMultiRegionAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateMultiRegionAccessPoint.html)
+  [DeleteMultiRegionAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteMultiRegionAccessPoint.html)
+  [DescribeMultiRegionAccessPointOperation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeMultiRegionAccessPointOperation.html)
+  [GetMultiRegionAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPoint.html)

## Request Syntax
<a name="API_control_ListMultiRegionAccessPoints_RequestSyntax"></a>

```
GET /v20180820/mrap/instances?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_ListMultiRegionAccessPoints_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_control_ListMultiRegionAccessPoints_RequestSyntax) **   <a name="AmazonS3-control_ListMultiRegionAccessPoints-request-uri-querystring-MaxResults"></a>
Not currently used. Do not use this parameter.
Valid Range: Minimum value of 0. Maximum value of 1000.

 ** [nextToken](#API_control_ListMultiRegionAccessPoints_RequestSyntax) **   <a name="AmazonS3-control_ListMultiRegionAccessPoints-request-uri-querystring-NextToken"></a>
Not currently used. Do not use this parameter.
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [x-amz-account-id](#API_control_ListMultiRegionAccessPoints_RequestSyntax) **   <a name="AmazonS3-control_ListMultiRegionAccessPoints-request-header-AccountId"></a>
The AWS account ID for the owner of the Multi-Region Access Point.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_ListMultiRegionAccessPoints_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_ListMultiRegionAccessPoints_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListMultiRegionAccessPointsResult>
   <AccessPoints>
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
   </AccessPoints>
   <NextToken>string</NextToken>
</ListMultiRegionAccessPointsResult>
```

## Response Elements
<a name="API_control_ListMultiRegionAccessPoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListMultiRegionAccessPointsResult](#API_control_ListMultiRegionAccessPoints_ResponseSyntax) **   <a name="AmazonS3-control_ListMultiRegionAccessPoints-response-ListMultiRegionAccessPointsResult"></a>
Root level tag for the ListMultiRegionAccessPointsResult parameters.
Required: Yes

 ** [AccessPoints](#API_control_ListMultiRegionAccessPoints_ResponseSyntax) **   <a name="AmazonS3-control_ListMultiRegionAccessPoints-response-AccessPoints"></a>
The list of Multi-Region Access Points associated with the user.
Type: Array of [MultiRegionAccessPointReport](API_control_MultiRegionAccessPointReport.md) data types

 ** [NextToken](#API_control_ListMultiRegionAccessPoints_ResponseSyntax) **   <a name="AmazonS3-control_ListMultiRegionAccessPoints-response-NextToken"></a>
If the specified bucket has more Multi-Region Access Points than can be returned in one call to this action, this field contains a continuation token. You can use this token tin subsequent calls to this action to retrieve additional Multi-Region Access Points.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## See Also
<a name="API_control_ListMultiRegionAccessPoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/ListMultiRegionAccessPoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/ListMultiRegionAccessPoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListMultiRegionAccessPoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/ListMultiRegionAccessPoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListMultiRegionAccessPoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/ListMultiRegionAccessPoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/ListMultiRegionAccessPoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/ListMultiRegionAccessPoints)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/ListMultiRegionAccessPoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListMultiRegionAccessPoints)
