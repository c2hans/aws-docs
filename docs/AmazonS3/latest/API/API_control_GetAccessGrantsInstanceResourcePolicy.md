---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessGrantsInstanceResourcePolicy.html
---

# GetAccessGrantsInstanceResourcePolicy
<a name="API_control_GetAccessGrantsInstanceResourcePolicy"></a>

Returns the resource policy of the S3 Access Grants instance.

Permissions
You must have the `s3:GetAccessGrantsInstanceResourcePolicy` permission to use this operation.

## Request Syntax
<a name="API_control_GetAccessGrantsInstanceResourcePolicy_RequestSyntax"></a>

```
GET /v20180820/accessgrantsinstance/resourcepolicy HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_GetAccessGrantsInstanceResourcePolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [x-amz-account-id](#API_control_GetAccessGrantsInstanceResourcePolicy_RequestSyntax) **   <a name="AmazonS3-control_GetAccessGrantsInstanceResourcePolicy-request-header-AccountId"></a>
The AWS account ID of the S3 Access Grants instance.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_GetAccessGrantsInstanceResourcePolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_GetAccessGrantsInstanceResourcePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetAccessGrantsInstanceResourcePolicyResult>
   <Policy>string</Policy>
   <Organization>string</Organization>
   <CreatedAt>timestamp</CreatedAt>
</GetAccessGrantsInstanceResourcePolicyResult>
```

## Response Elements
<a name="API_control_GetAccessGrantsInstanceResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetAccessGrantsInstanceResourcePolicyResult](#API_control_GetAccessGrantsInstanceResourcePolicy_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessGrantsInstanceResourcePolicy-response-GetAccessGrantsInstanceResourcePolicyResult"></a>
Root level tag for the GetAccessGrantsInstanceResourcePolicyResult parameters.
Required: Yes

 ** [CreatedAt](#API_control_GetAccessGrantsInstanceResourcePolicy_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessGrantsInstanceResourcePolicy-response-CreatedAt"></a>
The date and time when you created the S3 Access Grants instance resource policy.
Type: Timestamp

 ** [Organization](#API_control_GetAccessGrantsInstanceResourcePolicy_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessGrantsInstanceResourcePolicy-response-Organization"></a>
The Organization of the resource policy of the S3 Access Grants instance.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 34.
Pattern: `^o-[a-z0-9]{10,32}$`

 ** [Policy](#API_control_GetAccessGrantsInstanceResourcePolicy_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessGrantsInstanceResourcePolicy-response-Policy"></a>
The resource policy of the S3 Access Grants instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 350000.

## See Also
<a name="API_control_GetAccessGrantsInstanceResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetAccessGrantsInstanceResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/GetAccessGrantsInstanceResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetAccessGrantsInstanceResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetAccessGrantsInstanceResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetAccessGrantsInstanceResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetAccessGrantsInstanceResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetAccessGrantsInstanceResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetAccessGrantsInstanceResourcePolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetAccessGrantsInstanceResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetAccessGrantsInstanceResourcePolicy)
