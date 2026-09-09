---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectLockConfiguration.html
---

# GetObjectLockConfiguration
<a name="API_GetObjectLockConfiguration"></a>

**Note**
This operation is not supported for directory buckets.

Gets the Object Lock configuration for a bucket. The rule specified in the Object Lock configuration will be applied by default to every new object placed in the specified bucket. For more information, see [Locking Objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html).

The following action is related to `GetObjectLockConfiguration`:
+  [GetObjectAttributes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAttributes.html)

**Important**
You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax
<a name="API_GetObjectLockConfiguration_RequestSyntax"></a>

```
GET /?object-lock HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
```

## URI Request Parameters
<a name="API_GetObjectLockConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Bucket](#API_GetObjectLockConfiguration_RequestSyntax) **   <a name="AmazonS3-GetObjectLockConfiguration-request-header-Bucket"></a>
The bucket whose Object Lock configuration you want to retrieve.
 **Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html) in the *Amazon S3 User Guide*.
Required: Yes

 ** [x-amz-expected-bucket-owner](#API_GetObjectLockConfiguration_RequestSyntax) **   <a name="AmazonS3-GetObjectLockConfiguration-request-header-ExpectedBucketOwner"></a>
The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Request Body
<a name="API_GetObjectLockConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetObjectLockConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ObjectLockConfiguration>
   <ObjectLockEnabled>string</ObjectLockEnabled>
   <Rule>
      <DefaultRetention>
         <Days>integer</Days>
         <DefaultEventHold>
            <Days>integer</Days>
            <Years>integer</Years>
         </DefaultEventHold>
         <Mode>string</Mode>
         <Years>integer</Years>
      </DefaultRetention>
   </Rule>
</ObjectLockConfiguration>
```

## Response Elements
<a name="API_GetObjectLockConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ObjectLockConfiguration](#API_GetObjectLockConfiguration_ResponseSyntax) **   <a name="AmazonS3-GetObjectLockConfiguration-response-ObjectLockConfiguration"></a>
Root level tag for the ObjectLockConfiguration parameters.
Required: Yes

 ** [ObjectLockEnabled](#API_GetObjectLockConfiguration_ResponseSyntax) **   <a name="AmazonS3-GetObjectLockConfiguration-response-ObjectLockEnabled"></a>
Indicates whether this bucket has an Object Lock configuration enabled. Enable `ObjectLockEnabled` when you apply `ObjectLockConfiguration` to a bucket.
Type: String
Valid Values: `Enabled`

 ** [Rule](#API_GetObjectLockConfiguration_ResponseSyntax) **   <a name="AmazonS3-GetObjectLockConfiguration-response-Rule"></a>
Specifies the Object Lock rule for the specified object. Enable the this rule when you apply `ObjectLockConfiguration` to a bucket. Bucket settings require both a mode and a period. The period can be either `Days` or `Years` but you must select one. You cannot specify `Days` and `Years` at the same time.
Type: [ObjectLockRule](API_ObjectLockRule.md) data type

## See Also
<a name="API_GetObjectLockConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetObjectLockConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/GetObjectLockConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetObjectLockConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetObjectLockConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetObjectLockConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetObjectLockConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetObjectLockConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetObjectLockConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetObjectLockConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetObjectLockConfiguration)
