---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeMultiRegionAccessPointOperation.html
---

# DescribeMultiRegionAccessPointOperation
<a name="API_control_DescribeMultiRegionAccessPointOperation"></a>

**Note**
This operation is not supported by directory buckets.

Retrieves the status of an asynchronous request to manage a Multi-Region Access Point. For more information about managing Multi-Region Access Points and how asynchronous requests work, see [Using Multi-Region Access Points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MrapOperations.html) in the *Amazon S3 User Guide*.

The following actions are related to `GetMultiRegionAccessPoint`:
+  [CreateMultiRegionAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateMultiRegionAccessPoint.html)
+  [DeleteMultiRegionAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteMultiRegionAccessPoint.html)
+  [GetMultiRegionAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPoint.html)
+  [ListMultiRegionAccessPoints](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListMultiRegionAccessPoints.html)

## Request Syntax
<a name="API_control_DescribeMultiRegionAccessPointOperation_RequestSyntax"></a>

```
GET /v20180820/async-requests/mrap/{{request_token+}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_DescribeMultiRegionAccessPointOperation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [request\_token](#API_control_DescribeMultiRegionAccessPointOperation_RequestSyntax) **   <a name="AmazonS3-control_DescribeMultiRegionAccessPointOperation-request-uri-uri-RequestTokenARN"></a>
The request token associated with the request you want to know about. This request token is returned as part of the response when you make an asynchronous request. You provide this token to query about the status of the asynchronous action.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:.+`
Required: Yes

 ** [x-amz-account-id](#API_control_DescribeMultiRegionAccessPointOperation_RequestSyntax) **   <a name="AmazonS3-control_DescribeMultiRegionAccessPointOperation-request-header-AccountId"></a>
The AWS account ID for the owner of the Multi-Region Access Point.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_DescribeMultiRegionAccessPointOperation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_DescribeMultiRegionAccessPointOperation_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<DescribeMultiRegionAccessPointOperationResult>
   <AsyncOperation>
      <CreationTime>timestamp</CreationTime>
      <Operation>string</Operation>
      <RequestParameters>
         <CreateMultiRegionAccessPointRequest>
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
               </Region>
            </Regions>
         </CreateMultiRegionAccessPointRequest>
         <DeleteMultiRegionAccessPointRequest>
            <Name>string</Name>
         </DeleteMultiRegionAccessPointRequest>
         <PutMultiRegionAccessPointPolicyRequest>
            <Name>string</Name>
            <Policy>string</Policy>
         </PutMultiRegionAccessPointPolicyRequest>
      </RequestParameters>
      <RequestStatus>string</RequestStatus>
      <RequestTokenARN>string</RequestTokenARN>
      <ResponseDetails>
         <ErrorDetails>
            <Code>string</Code>
            <Message>string</Message>
            <RequestId>string</RequestId>
            <Resource>string</Resource>
         </ErrorDetails>
         <MultiRegionAccessPointDetails>
            <Regions>
               <Region>
                  <Name>string</Name>
                  <RequestStatus>string</RequestStatus>
               </Region>
            </Regions>
         </MultiRegionAccessPointDetails>
      </ResponseDetails>
   </AsyncOperation>
</DescribeMultiRegionAccessPointOperationResult>
```

## Response Elements
<a name="API_control_DescribeMultiRegionAccessPointOperation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [DescribeMultiRegionAccessPointOperationResult](#API_control_DescribeMultiRegionAccessPointOperation_ResponseSyntax) **   <a name="AmazonS3-control_DescribeMultiRegionAccessPointOperation-response-DescribeMultiRegionAccessPointOperationResult"></a>
Root level tag for the DescribeMultiRegionAccessPointOperationResult parameters.
Required: Yes

 ** [AsyncOperation](#API_control_DescribeMultiRegionAccessPointOperation_ResponseSyntax) **   <a name="AmazonS3-control_DescribeMultiRegionAccessPointOperation-response-AsyncOperation"></a>
A container element containing the details of the asynchronous operation.
Type: [AsyncOperation](API_control_AsyncOperation.md) data type

## See Also
<a name="API_control_DescribeMultiRegionAccessPointOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
