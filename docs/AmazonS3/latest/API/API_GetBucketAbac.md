---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAbac.html
---

# GetBucketAbac
<a name="API_GetBucketAbac"></a>

Returns the attribute-based access control (ABAC) property of the general purpose bucket. If ABAC is enabled on your bucket, you can use tags on the bucket for access control. For more information, see [Enabling ABAC in general purpose buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/buckets-tagging-enable-abac.html).

## Request Syntax
<a name="API_GetBucketAbac_RequestSyntax"></a>

```
GET /?abac HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
```

## URI Request Parameters
<a name="API_GetBucketAbac_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Bucket](#API_GetBucketAbac_RequestSyntax) **   <a name="AmazonS3-GetBucketAbac-request-header-Bucket"></a>
The name of the general purpose bucket.
Required: Yes

 ** [x-amz-expected-bucket-owner](#API_GetBucketAbac_RequestSyntax) **   <a name="AmazonS3-GetBucketAbac-request-header-ExpectedBucketOwner"></a>
The AWS account ID of the general purpose bucket's owner.

## Request Body
<a name="API_GetBucketAbac_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetBucketAbac_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<AbacStatus>
   <Status>string</Status>
</AbacStatus>
```

## Response Elements
<a name="API_GetBucketAbac_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [AbacStatus](#API_GetBucketAbac_ResponseSyntax) **   <a name="AmazonS3-GetBucketAbac-response-AbacStatus"></a>
Root level tag for the AbacStatus parameters.
Required: Yes

 ** [Status](#API_GetBucketAbac_ResponseSyntax) **   <a name="AmazonS3-GetBucketAbac-response-Status"></a>
The ABAC status of the general purpose bucket.
Type: String
Valid Values: `Enabled | Disabled`

## See Also
<a name="API_GetBucketAbac_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketAbac)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/GetBucketAbac)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketAbac)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketAbac)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketAbac)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketAbac)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketAbac)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketAbac)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketAbac)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketAbac)
