---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicyStatus.html
---

# GetAccessPointPolicyStatus
<a name="API_control_GetAccessPointPolicyStatus"></a>

**Note**
This operation is not supported by directory buckets.

Indicates whether the specified access point currently has a policy that allows public access. For more information about public access through access points, see [Managing Data Access with Amazon S3 access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html) in the *Amazon S3 User Guide*.

## Request Syntax
<a name="API_control_GetAccessPointPolicyStatus_RequestSyntax"></a>

```
GET /v20180820/accesspoint/{{name}}/policyStatus HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_GetAccessPointPolicyStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_control_GetAccessPointPolicyStatus_RequestSyntax) **   <a name="AmazonS3-control_GetAccessPointPolicyStatus-request-uri-uri-Name"></a>
The name of the access point whose policy status you want to retrieve.
Length Constraints: Minimum length of 3. Maximum length of 255.
Required: Yes

 ** [x-amz-account-id](#API_control_GetAccessPointPolicyStatus_RequestSyntax) **   <a name="AmazonS3-control_GetAccessPointPolicyStatus-request-header-AccountId"></a>
The account ID for the account that owns the specified access point.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_GetAccessPointPolicyStatus_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_GetAccessPointPolicyStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetAccessPointPolicyStatusResult>
   <PolicyStatus>
      <IsPublic>boolean</IsPublic>
   </PolicyStatus>
</GetAccessPointPolicyStatusResult>
```

## Response Elements
<a name="API_control_GetAccessPointPolicyStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetAccessPointPolicyStatusResult](#API_control_GetAccessPointPolicyStatus_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessPointPolicyStatus-response-GetAccessPointPolicyStatusResult"></a>
Root level tag for the GetAccessPointPolicyStatusResult parameters.
Required: Yes

 ** [PolicyStatus](#API_control_GetAccessPointPolicyStatus_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessPointPolicyStatus-response-PolicyStatus"></a>
Indicates the current policy status of the specified access point.
Type: [PolicyStatus](API_control_PolicyStatus.md) data type

## See Also
<a name="API_control_GetAccessPointPolicyStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetAccessPointPolicyStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/GetAccessPointPolicyStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetAccessPointPolicyStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetAccessPointPolicyStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetAccessPointPolicyStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetAccessPointPolicyStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetAccessPointPolicyStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetAccessPointPolicyStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetAccessPointPolicyStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetAccessPointPolicyStatus)
