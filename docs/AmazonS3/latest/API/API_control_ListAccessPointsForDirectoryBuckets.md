---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPointsForDirectoryBuckets.html
---

# ListAccessPointsForDirectoryBuckets
<a name="API_control_ListAccessPointsForDirectoryBuckets"></a>

Returns a list of the access points that are owned by the AWS account and that are associated with the specified directory bucket.

To list access points for general purpose buckets, see [ListAccesspoints](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPoints.html).

To use this operation, you must have the permission to perform the `s3express:ListAccessPointsForDirectoryBuckets` action.

For information about REST API errors, see [REST error responses](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#RESTErrorResponses).

## Request Syntax
<a name="API_control_ListAccessPointsForDirectoryBuckets_RequestSyntax"></a>

```
GET /v20180820/accesspointfordirectory?directoryBucket={{DirectoryBucket}}&maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_ListAccessPointsForDirectoryBuckets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [directoryBucket](#API_control_ListAccessPointsForDirectoryBuckets_RequestSyntax) **   <a name="AmazonS3-control_ListAccessPointsForDirectoryBuckets-request-uri-querystring-DirectoryBucket"></a>
The name of the directory bucket associated with the access points you want to list.
Length Constraints: Minimum length of 3. Maximum length of 255.

 ** [maxResults](#API_control_ListAccessPointsForDirectoryBuckets_RequestSyntax) **   <a name="AmazonS3-control_ListAccessPointsForDirectoryBuckets-request-uri-querystring-MaxResults"></a>
The maximum number of access points that you would like returned in the `ListAccessPointsForDirectoryBuckets` response. If the directory bucket is associated with more than this number of access points, the results include the pagination token `NextToken`. Make another call using the `NextToken` to retrieve more results.
Valid Range: Minimum value of 0. Maximum value of 1000.

 ** [nextToken](#API_control_ListAccessPointsForDirectoryBuckets_RequestSyntax) **   <a name="AmazonS3-control_ListAccessPointsForDirectoryBuckets-request-uri-querystring-NextToken"></a>
 If `NextToken` is returned, there are more access points available than requested in the `maxResults` value. The value of `NextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours.
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [x-amz-account-id](#API_control_ListAccessPointsForDirectoryBuckets_RequestSyntax) **   <a name="AmazonS3-control_ListAccessPointsForDirectoryBuckets-request-header-AccountId"></a>
The AWS account ID that owns the access points.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_ListAccessPointsForDirectoryBuckets_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_ListAccessPointsForDirectoryBuckets_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListAccessPointsForDirectoryBucketsResult>
   <AccessPointList>
      <AccessPoint>
         <AccessPointArn>string</AccessPointArn>
         <Alias>string</Alias>
         <Bucket>string</Bucket>
         <BucketAccountId>string</BucketAccountId>
         <DataSourceId>string</DataSourceId>
         <DataSourceType>string</DataSourceType>
         <Name>string</Name>
         <NetworkOrigin>string</NetworkOrigin>
         <VpcConfiguration>
            <VpcId>string</VpcId>
         </VpcConfiguration>
      </AccessPoint>
   </AccessPointList>
   <NextToken>string</NextToken>
</ListAccessPointsForDirectoryBucketsResult>
```

## Response Elements
<a name="API_control_ListAccessPointsForDirectoryBuckets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListAccessPointsForDirectoryBucketsResult](#API_control_ListAccessPointsForDirectoryBuckets_ResponseSyntax) **   <a name="AmazonS3-control_ListAccessPointsForDirectoryBuckets-response-ListAccessPointsForDirectoryBucketsResult"></a>
Root level tag for the ListAccessPointsForDirectoryBucketsResult parameters.
Required: Yes

 ** [AccessPointList](#API_control_ListAccessPointsForDirectoryBuckets_ResponseSyntax) **   <a name="AmazonS3-control_ListAccessPointsForDirectoryBuckets-response-AccessPointList"></a>
Contains identification and configuration information for one or more access points associated with the directory bucket.
Type: Array of [AccessPoint](API_control_AccessPoint.md) data types

 ** [NextToken](#API_control_ListAccessPointsForDirectoryBuckets_ResponseSyntax) **   <a name="AmazonS3-control_ListAccessPointsForDirectoryBuckets-response-NextToken"></a>
 If `NextToken` is returned, there are more access points available than requested in the `maxResults` value. The value of `NextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## See Also
<a name="API_control_ListAccessPointsForDirectoryBuckets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
