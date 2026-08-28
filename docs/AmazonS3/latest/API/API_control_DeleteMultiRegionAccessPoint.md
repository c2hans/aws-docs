---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteMultiRegionAccessPoint.html
---

# DeleteMultiRegionAccessPoint
<a name="API_control_DeleteMultiRegionAccessPoint"></a>

**Note**
This operation is not supported by directory buckets.

Deletes a Multi-Region Access Point. This action does not delete the buckets associated with the Multi-Region Access Point, only the Multi-Region Access Point itself.

This action will always be routed to the US West (Oregon) Region. For more information about the restrictions around working with Multi-Region Access Points, see [Multi-Region Access Point restrictions and limitations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointRestrictions.html) in the *Amazon S3 User Guide*.

This request is asynchronous, meaning that you might receive a response before the command has completed. When this request provides a response, it provides a token that you can use to monitor the status of the request with `DescribeMultiRegionAccessPointOperation`.

The following actions are related to `DeleteMultiRegionAccessPoint`:
+  [CreateMultiRegionAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateMultiRegionAccessPoint.html)
+  [DescribeMultiRegionAccessPointOperation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeMultiRegionAccessPointOperation.html)
+  [GetMultiRegionAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPoint.html)
+  [ListMultiRegionAccessPoints](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListMultiRegionAccessPoints.html)

## Request Syntax
<a name="API_control_DeleteMultiRegionAccessPoint_RequestSyntax"></a>

```
POST /v20180820/async-requests/mrap/delete HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
<?xml version="1.0" encoding="UTF-8"?>
<DeleteMultiRegionAccessPointRequest xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <ClientToken>{{string}}</ClientToken>
   <Details>
      <Name>{{string}}</Name>
   </Details>
</DeleteMultiRegionAccessPointRequest>
```

## URI Request Parameters
<a name="API_control_DeleteMultiRegionAccessPoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [x-amz-account-id](#API_control_DeleteMultiRegionAccessPoint_RequestSyntax) **   <a name="AmazonS3-control_DeleteMultiRegionAccessPoint-request-header-AccountId"></a>
The AWS account ID for the owner of the Multi-Region Access Point.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_DeleteMultiRegionAccessPoint_RequestBody"></a>

The request accepts the following data in XML format.

 ** [DeleteMultiRegionAccessPointRequest](#API_control_DeleteMultiRegionAccessPoint_RequestSyntax) **   <a name="AmazonS3-control_DeleteMultiRegionAccessPoint-request-DeleteMultiRegionAccessPointRequest"></a>
Root level tag for the DeleteMultiRegionAccessPointRequest parameters.
Required: Yes

 ** [ClientToken](#API_control_DeleteMultiRegionAccessPoint_RequestSyntax) **   <a name="AmazonS3-control_DeleteMultiRegionAccessPoint-request-ClientToken"></a>
An idempotency token used to identify the request and guarantee that requests are unique.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `\S+`
Required: Yes

 ** [Details](#API_control_DeleteMultiRegionAccessPoint_RequestSyntax) **   <a name="AmazonS3-control_DeleteMultiRegionAccessPoint-request-Details"></a>
A container element containing details about the Multi-Region Access Point.
Type: [DeleteMultiRegionAccessPointInput](API_control_DeleteMultiRegionAccessPointInput.md) data type
Required: Yes

## Response Syntax
<a name="API_control_DeleteMultiRegionAccessPoint_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<DeleteMultiRegionAccessPointResult>
   <RequestTokenARN>string</RequestTokenARN>
</DeleteMultiRegionAccessPointResult>
```

## Response Elements
<a name="API_control_DeleteMultiRegionAccessPoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [DeleteMultiRegionAccessPointResult](#API_control_DeleteMultiRegionAccessPoint_ResponseSyntax) **   <a name="AmazonS3-control_DeleteMultiRegionAccessPoint-response-DeleteMultiRegionAccessPointResult"></a>
Root level tag for the DeleteMultiRegionAccessPointResult parameters.
Required: Yes

 ** [RequestTokenARN](#API_control_DeleteMultiRegionAccessPoint_ResponseSyntax) **   <a name="AmazonS3-control_DeleteMultiRegionAccessPoint-response-RequestTokenARN"></a>
The request token associated with the request. You can use this token with [DescribeMultiRegionAccessPointOperation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeMultiRegionAccessPointOperation.html) to determine the status of asynchronous requests.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:.+`

## See Also
<a name="API_control_DeleteMultiRegionAccessPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/DeleteMultiRegionAccessPoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/DeleteMultiRegionAccessPoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DeleteMultiRegionAccessPoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/DeleteMultiRegionAccessPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DeleteMultiRegionAccessPoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/DeleteMultiRegionAccessPoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/DeleteMultiRegionAccessPoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/DeleteMultiRegionAccessPoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/DeleteMultiRegionAccessPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DeleteMultiRegionAccessPoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
