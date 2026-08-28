---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPointRoutes.html
---

# GetMultiRegionAccessPointRoutes
<a name="API_control_GetMultiRegionAccessPointRoutes"></a>

**Note**
This operation is not supported by directory buckets.

Returns the routing configuration for a Multi-Region Access Point, indicating which Regions are active or passive.

To obtain routing control changes and failover requests, use the Amazon S3 failover control infrastructure endpoints in these five AWS Regions:
+  `us-east-1`
+  `us-west-2`
+  `ap-southeast-2`
+  `ap-northeast-1`
+  `eu-west-1`

## Request Syntax
<a name="API_control_GetMultiRegionAccessPointRoutes_RequestSyntax"></a>

```
GET /v20180820/mrap/instances/{{mrap+}}/routes HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_GetMultiRegionAccessPointRoutes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [mrap](#API_control_GetMultiRegionAccessPointRoutes_RequestSyntax) **   <a name="AmazonS3-control_GetMultiRegionAccessPointRoutes-request-uri-uri-Mrap"></a>
The Multi-Region Access Point ARN.
Length Constraints: Maximum length of 200.
Pattern: `^[a-zA-Z0-9\:.-]{3,200}$`
Required: Yes

 ** [x-amz-account-id](#API_control_GetMultiRegionAccessPointRoutes_RequestSyntax) **   <a name="AmazonS3-control_GetMultiRegionAccessPointRoutes-request-header-AccountId"></a>
The AWS account ID for the owner of the Multi-Region Access Point.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_GetMultiRegionAccessPointRoutes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_GetMultiRegionAccessPointRoutes_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetMultiRegionAccessPointRoutesResult>
   <Mrap>string</Mrap>
   <Routes>
      <Route>
         <Bucket>string</Bucket>
         <Region>string</Region>
         <TrafficDialPercentage>integer</TrafficDialPercentage>
      </Route>
   </Routes>
</GetMultiRegionAccessPointRoutesResult>
```

## Response Elements
<a name="API_control_GetMultiRegionAccessPointRoutes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetMultiRegionAccessPointRoutesResult](#API_control_GetMultiRegionAccessPointRoutes_ResponseSyntax) **   <a name="AmazonS3-control_GetMultiRegionAccessPointRoutes-response-GetMultiRegionAccessPointRoutesResult"></a>
Root level tag for the GetMultiRegionAccessPointRoutesResult parameters.
Required: Yes

 ** [Mrap](#API_control_GetMultiRegionAccessPointRoutes_ResponseSyntax) **   <a name="AmazonS3-control_GetMultiRegionAccessPointRoutes-response-Mrap"></a>
The Multi-Region Access Point ARN.
Type: String
Length Constraints: Maximum length of 200.
Pattern: `^[a-zA-Z0-9\:.-]{3,200}$`

 ** [Routes](#API_control_GetMultiRegionAccessPointRoutes_ResponseSyntax) **   <a name="AmazonS3-control_GetMultiRegionAccessPointRoutes-response-Routes"></a>
The different routes that make up the route configuration. Active routes return a value of `100`, and passive routes return a value of `0`.
Type: Array of [MultiRegionAccessPointRoute](API_control_MultiRegionAccessPointRoute.md) data types

## See Also
<a name="API_control_GetMultiRegionAccessPointRoutes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetMultiRegionAccessPointRoutes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/GetMultiRegionAccessPointRoutes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetMultiRegionAccessPointRoutes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetMultiRegionAccessPointRoutes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetMultiRegionAccessPointRoutes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetMultiRegionAccessPointRoutes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetMultiRegionAccessPointRoutes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetMultiRegionAccessPointRoutes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetMultiRegionAccessPointRoutes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetMultiRegionAccessPointRoutes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
