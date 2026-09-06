---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutMultiRegionAccessPointPolicy.html
---

# PutMultiRegionAccessPointPolicy
<a name="API_control_PutMultiRegionAccessPointPolicy"></a>

**Note**
This operation is not supported by directory buckets.

Associates an access control policy with the specified Multi-Region Access Point. Each Multi-Region Access Point can have only one policy, so a request made to this action replaces any existing policy that is associated with the specified Multi-Region Access Point.

This action will always be routed to the US West (Oregon) Region. For more information about the restrictions around working with Multi-Region Access Points, see [Multi-Region Access Point restrictions and limitations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointRestrictions.html) in the *Amazon S3 User Guide*.

The following actions are related to `PutMultiRegionAccessPointPolicy`:
+  [GetMultiRegionAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPointPolicy.html)
+  [GetMultiRegionAccessPointPolicyStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPointPolicyStatus.html)

## Request Syntax
<a name="API_control_PutMultiRegionAccessPointPolicy_RequestSyntax"></a>

```
POST /v20180820/async-requests/mrap/put-policy HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
<?xml version="1.0" encoding="UTF-8"?>
<PutMultiRegionAccessPointPolicyRequest xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <ClientToken>{{string}}</ClientToken>
   <Details>
      <Name>{{string}}</Name>
      <Policy>{{string}}</Policy>
   </Details>
</PutMultiRegionAccessPointPolicyRequest>
```

## URI Request Parameters
<a name="API_control_PutMultiRegionAccessPointPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [x-amz-account-id](#API_control_PutMultiRegionAccessPointPolicy_RequestSyntax) **   <a name="AmazonS3-control_PutMultiRegionAccessPointPolicy-request-header-AccountId"></a>
The AWS account ID for the owner of the Multi-Region Access Point.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_PutMultiRegionAccessPointPolicy_RequestBody"></a>

The request accepts the following data in XML format.

 ** [PutMultiRegionAccessPointPolicyRequest](#API_control_PutMultiRegionAccessPointPolicy_RequestSyntax) **   <a name="AmazonS3-control_PutMultiRegionAccessPointPolicy-request-PutMultiRegionAccessPointPolicyRequest"></a>
Root level tag for the PutMultiRegionAccessPointPolicyRequest parameters.
Required: Yes

 ** [ClientToken](#API_control_PutMultiRegionAccessPointPolicy_RequestSyntax) **   <a name="AmazonS3-control_PutMultiRegionAccessPointPolicy-request-ClientToken"></a>
An idempotency token used to identify the request and guarantee that requests are unique.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `\S+`
Required: Yes

 ** [Details](#API_control_PutMultiRegionAccessPointPolicy_RequestSyntax) **   <a name="AmazonS3-control_PutMultiRegionAccessPointPolicy-request-Details"></a>
A container element containing the details of the policy for the Multi-Region Access Point.
Type: [PutMultiRegionAccessPointPolicyInput](API_control_PutMultiRegionAccessPointPolicyInput.md) data type
Required: Yes

## Response Syntax
<a name="API_control_PutMultiRegionAccessPointPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<PutMultiRegionAccessPointPolicyResult>
   <RequestTokenARN>string</RequestTokenARN>
</PutMultiRegionAccessPointPolicyResult>
```

## Response Elements
<a name="API_control_PutMultiRegionAccessPointPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [PutMultiRegionAccessPointPolicyResult](#API_control_PutMultiRegionAccessPointPolicy_ResponseSyntax) **   <a name="AmazonS3-control_PutMultiRegionAccessPointPolicy-response-PutMultiRegionAccessPointPolicyResult"></a>
Root level tag for the PutMultiRegionAccessPointPolicyResult parameters.
Required: Yes

 ** [RequestTokenARN](#API_control_PutMultiRegionAccessPointPolicy_ResponseSyntax) **   <a name="AmazonS3-control_PutMultiRegionAccessPointPolicy-response-RequestTokenARN"></a>
The request token associated with the request. You can use this token with [DescribeMultiRegionAccessPointOperation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeMultiRegionAccessPointOperation.html) to determine the status of asynchronous requests.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:.+`

## See Also
<a name="API_control_PutMultiRegionAccessPointPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/PutMultiRegionAccessPointPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/PutMultiRegionAccessPointPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutMultiRegionAccessPointPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/PutMultiRegionAccessPointPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutMultiRegionAccessPointPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/PutMultiRegionAccessPointPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/PutMultiRegionAccessPointPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/PutMultiRegionAccessPointPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutMultiRegionAccessPointPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutMultiRegionAccessPointPolicy)
