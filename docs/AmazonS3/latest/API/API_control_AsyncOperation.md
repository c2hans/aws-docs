---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_AsyncOperation.html
---

# AsyncOperation
<a name="API_control_AsyncOperation"></a>

A container for the information about an asynchronous operation.

## Contents
<a name="API_control_AsyncOperation_Contents"></a>

 ** CreationTime **   <a name="AmazonS3-Type-control_AsyncOperation-CreationTime"></a>
The time that the request was sent to the service.
Type: Timestamp
Required: No

 ** Operation **   <a name="AmazonS3-Type-control_AsyncOperation-Operation"></a>
The specific operation for the asynchronous request.
Type: String
Valid Values: `CreateMultiRegionAccessPoint | DeleteMultiRegionAccessPoint | PutMultiRegionAccessPointPolicy`
Required: No

 ** RequestParameters **   <a name="AmazonS3-Type-control_AsyncOperation-RequestParameters"></a>
The parameters associated with the request.
Type: [AsyncRequestParameters](API_control_AsyncRequestParameters.md) data type
Required: No

 ** RequestStatus **   <a name="AmazonS3-Type-control_AsyncOperation-RequestStatus"></a>
The current status of the request.
Type: String
Required: No

 ** RequestTokenARN **   <a name="AmazonS3-Type-control_AsyncOperation-RequestTokenARN"></a>
The request token associated with the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:.+`
Required: No

 ** ResponseDetails **   <a name="AmazonS3-Type-control_AsyncOperation-ResponseDetails"></a>
The details of the response.
Type: [AsyncResponseDetails](API_control_AsyncResponseDetails.md) data type
Required: No

## See Also
<a name="API_control_AsyncOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/AsyncOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/AsyncOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/AsyncOperation)
