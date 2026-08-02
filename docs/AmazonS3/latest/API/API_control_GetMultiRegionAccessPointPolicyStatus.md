---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPointPolicyStatus.html
---

# GetMultiRegionAccessPointPolicyStatus
<a name="API_control_GetMultiRegionAccessPointPolicyStatus"></a>

**Note**
This operation is not supported by directory buckets.

Indicates whether the specified Multi-Region Access Point has an access control policy that allows public access.

This action will always be routed to the US West (Oregon) Region. For more information about the restrictions around working with Multi-Region Access Points, see [Multi-Region Access Point restrictions and limitations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointRestrictions.html) in the *Amazon S3 User Guide*.

The following actions are related to `GetMultiRegionAccessPointPolicyStatus`:
+  [GetMultiRegionAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPointPolicy.html)
+  [PutMultiRegionAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutMultiRegionAccessPointPolicy.html)

## Request Syntax
<a name="API_control_GetMultiRegionAccessPointPolicyStatus_RequestSyntax"></a>

```
GET /v20180820/mrap/instances/{{name+}}/policystatus HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_GetMultiRegionAccessPointPolicyStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_control_GetMultiRegionAccessPointPolicyStatus_RequestSyntax) **   <a name="AmazonS3-control_GetMultiRegionAccessPointPolicyStatus-request-uri-uri-Name"></a>
Specifies the Multi-Region Access Point. The name of the Multi-Region Access Point is different from the alias. For more information about the distinction between the name and the alias of an Multi-Region Access Point, see [Rules for naming Amazon S3 Multi-Region Access Points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/CreatingMultiRegionAccessPoints.html#multi-region-access-point-naming) in the *Amazon S3 User Guide*.
Length Constraints: Maximum length of 50.
Pattern: `^[a-z0-9][-a-z0-9]{1,48}[a-z0-9]$`
Required: Yes

 ** [x-amz-account-id](#API_control_GetMultiRegionAccessPointPolicyStatus_RequestSyntax) **   <a name="AmazonS3-control_GetMultiRegionAccessPointPolicyStatus-request-header-AccountId"></a>
The AWS account ID for the owner of the Multi-Region Access Point.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_GetMultiRegionAccessPointPolicyStatus_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_GetMultiRegionAccessPointPolicyStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetMultiRegionAccessPointPolicyStatusResult>
   <Established>
      <IsPublic>boolean</IsPublic>
   </Established>
</GetMultiRegionAccessPointPolicyStatusResult>
```

## Response Elements
<a name="API_control_GetMultiRegionAccessPointPolicyStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetMultiRegionAccessPointPolicyStatusResult](#API_control_GetMultiRegionAccessPointPolicyStatus_ResponseSyntax) **   <a name="AmazonS3-control_GetMultiRegionAccessPointPolicyStatus-response-GetMultiRegionAccessPointPolicyStatusResult"></a>
Root level tag for the GetMultiRegionAccessPointPolicyStatusResult parameters.
Required: Yes

 ** [Established](#API_control_GetMultiRegionAccessPointPolicyStatus_ResponseSyntax) **   <a name="AmazonS3-control_GetMultiRegionAccessPointPolicyStatus-response-Established"></a>
Indicates whether this access point policy is public. For more information about how Amazon S3 evaluates policies to determine whether they are public, see [The Meaning of "Public"](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status) in the *Amazon S3 User Guide*.
Type: [PolicyStatus](API_control_PolicyStatus.md) data type

## See Also
<a name="API_control_GetMultiRegionAccessPointPolicyStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus)
