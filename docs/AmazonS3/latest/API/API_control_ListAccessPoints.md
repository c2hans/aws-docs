---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPoints.html
---

# ListAccessPoints
<a name="API_control_ListAccessPoints"></a>

**Note**
This operation is not supported by directory buckets.

Returns a list of the access points. You can retrieve up to 1,000 access points per call. If the call returns more than 1,000 access points (or the number specified in `maxResults`, whichever is less), the response will include a continuation token that you can use to list the additional access points.

Returns only access points attached to S3 buckets by default. To return all access points specify `DataSourceType` as `ALL`.

All Amazon S3 on Outposts REST API requests for this action require an additional parameter of `x-amz-outpost-id` to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of `s3-control`. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the `x-amz-outpost-id` derived by using the access point ARN, see the [Examples](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html#API_control_GetAccessPoint_Examples) section.

The following actions are related to `ListAccessPoints`:
+  [CreateAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html)
+  [DeleteAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPoint.html)
+  [GetAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html)

## Request Syntax
<a name="API_control_ListAccessPoints_RequestSyntax"></a>

```
GET /v20180820/accesspoint?bucket={{Bucket}}&dataSourceId={{DataSourceId}}&dataSourceType={{DataSourceType}}&maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_ListAccessPoints_RequestParameters"></a>

The request uses the following URI parameters.

 ** [bucket](#API_control_ListAccessPoints_RequestSyntax) **   <a name="AmazonS3-control_ListAccessPoints-request-uri-querystring-Bucket"></a>
The name of the bucket whose associated access points you want to list.
For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.
For using this parameter with S3 on Outposts with the AWS SDK and CLI, you must specify the ARN of the bucket accessed in the format `arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name>`. For example, to access the bucket `reports` through Outpost `my-outpost` owned by account `123456789012` in Region `us-west-2`, use the URL encoding of `arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports`. The value must be URL encoded.
Length Constraints: Minimum length of 3. Maximum length of 255.

 ** [dataSourceId](#API_control_ListAccessPoints_RequestSyntax) **   <a name="AmazonS3-control_ListAccessPoints-request-uri-querystring-DataSourceId"></a>
The unique identifier for the data source of the access point.
Length Constraints: Maximum length of 191.

 ** [dataSourceType](#API_control_ListAccessPoints_RequestSyntax) **   <a name="AmazonS3-control_ListAccessPoints-request-uri-querystring-DataSourceType"></a>
The type of the data source that the access point is attached to. Returns only access points attached to S3 buckets by default. To return all access points specify `DataSourceType` as `ALL`.

 ** [maxResults](#API_control_ListAccessPoints_RequestSyntax) **   <a name="AmazonS3-control_ListAccessPoints-request-uri-querystring-MaxResults"></a>
The maximum number of access points that you want to include in the list. If the specified bucket has more than this number of access points, then the response will include a continuation token in the `NextToken` field that you can use to retrieve the next page of access points.
Valid Range: Minimum value of 0. Maximum value of 1000.

 ** [nextToken](#API_control_ListAccessPoints_RequestSyntax) **   <a name="AmazonS3-control_ListAccessPoints-request-uri-querystring-NextToken"></a>
A continuation token. If a previous call to `ListAccessPoints` returned a continuation token in the `NextToken` field, then providing that value here causes Amazon S3 to retrieve the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [x-amz-account-id](#API_control_ListAccessPoints_RequestSyntax) **   <a name="AmazonS3-control_ListAccessPoints-request-header-AccountId"></a>
The AWS account ID for the account that owns the specified access points.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_ListAccessPoints_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_ListAccessPoints_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListAccessPointsResult>
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
</ListAccessPointsResult>
```

## Response Elements
<a name="API_control_ListAccessPoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListAccessPointsResult](#API_control_ListAccessPoints_ResponseSyntax) **   <a name="AmazonS3-control_ListAccessPoints-response-ListAccessPointsResult"></a>
Root level tag for the ListAccessPointsResult parameters.
Required: Yes

 ** [AccessPointList](#API_control_ListAccessPoints_ResponseSyntax) **   <a name="AmazonS3-control_ListAccessPoints-response-AccessPointList"></a>
Contains identification and configuration information for one or more access points associated with the specified bucket.
Type: Array of [AccessPoint](API_control_AccessPoint.md) data types

 ** [NextToken](#API_control_ListAccessPoints_ResponseSyntax) **   <a name="AmazonS3-control_ListAccessPoints-response-NextToken"></a>
If the specified bucket has more access points than can be returned in one call to this API, this field contains a continuation token that you can provide in subsequent calls to this API to retrieve additional access points.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Examples
<a name="API_control_ListAccessPoints_Examples"></a>

### Sample request syntax for ListAccessPoints for Amazon S3 on Outposts
<a name="API_control_ListAccessPoints_Example_1"></a>

The following request returns a list access points of the specified Amazon S3 on Outposts bucket `example-outpost-bucket`.

```
           GET /v20180820/accesspoint?Bucket=example-outpost-bucket&MaxResults=MaxResults&NextToken=NextToken HTTP/1.1
           Host: s3-outposts.<Region>.amazonaws.com
           Date: Wed, 28 Oct 2020 22:32:00 GMT
           Authorization: authorization string
           x-amz-account-id: example-account-id
           x-amz-outpost-id: op-01ac5d28a6a232904
```

## See Also
<a name="API_control_ListAccessPoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/ListAccessPoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/ListAccessPoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListAccessPoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/ListAccessPoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListAccessPoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/ListAccessPoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/ListAccessPoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/ListAccessPoints)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/ListAccessPoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListAccessPoints)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
