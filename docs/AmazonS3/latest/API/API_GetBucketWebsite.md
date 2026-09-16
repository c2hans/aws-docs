---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketWebsite.html
---

# GetBucketWebsite
<a name="API_GetBucketWebsite"></a>

**Note**
This operation is not supported for directory buckets.

Returns the website configuration for a bucket. To host website on Amazon S3, you can configure a bucket as website by adding a website configuration. For more information about hosting websites, see [Hosting Websites on Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html).

This GET action requires the `S3:GetBucketWebsite` permission. By default, only the bucket owner can read the bucket website configuration. However, bucket owners can allow other users to read the website configuration by writing a bucket policy granting them the `S3:GetBucketWebsite` permission.

The following operations are related to `GetBucketWebsite`:
+  [DeleteBucketWebsite](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketWebsite.html)
+  [PutBucketWebsite](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketWebsite.html)

**Important**
You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax
<a name="API_GetBucketWebsite_RequestSyntax"></a>

```
GET /?website HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
```

## URI Request Parameters
<a name="API_GetBucketWebsite_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Bucket](#API_GetBucketWebsite_RequestSyntax) **   <a name="AmazonS3-GetBucketWebsite-request-header-Bucket"></a>
The bucket name for which to get the website configuration.
Required: Yes

 ** [x-amz-expected-bucket-owner](#API_GetBucketWebsite_RequestSyntax) **   <a name="AmazonS3-GetBucketWebsite-request-header-ExpectedBucketOwner"></a>
The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Request Body
<a name="API_GetBucketWebsite_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetBucketWebsite_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<WebsiteConfiguration>
   <RedirectAllRequestsTo>
      <HostName>string</HostName>
      <Protocol>string</Protocol>
   </RedirectAllRequestsTo>
   <IndexDocument>
      <Suffix>string</Suffix>
   </IndexDocument>
   <ErrorDocument>
      <Key>string</Key>
   </ErrorDocument>
   <RoutingRules>
      <RoutingRule>
         <Condition>
            <HttpErrorCodeReturnedEquals>string</HttpErrorCodeReturnedEquals>
            <KeyPrefixEquals>string</KeyPrefixEquals>
         </Condition>
         <Redirect>
            <HostName>string</HostName>
            <HttpRedirectCode>string</HttpRedirectCode>
            <Protocol>string</Protocol>
            <ReplaceKeyPrefixWith>string</ReplaceKeyPrefixWith>
            <ReplaceKeyWith>string</ReplaceKeyWith>
         </Redirect>
      </RoutingRule>
   </RoutingRules>
</WebsiteConfiguration>
```

## Response Elements
<a name="API_GetBucketWebsite_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [WebsiteConfiguration](#API_GetBucketWebsite_ResponseSyntax) **   <a name="AmazonS3-GetBucketWebsite-response-GetBucketWebsiteOutput"></a>
Root level tag for the WebsiteConfiguration parameters.
Required: Yes

 ** [ErrorDocument](#API_GetBucketWebsite_ResponseSyntax) **   <a name="AmazonS3-GetBucketWebsite-response-ErrorDocument"></a>
The object key name of the website error document to use for 4XX class errors.
Type: [ErrorDocument](API_ErrorDocument.md) data type

 ** [IndexDocument](#API_GetBucketWebsite_ResponseSyntax) **   <a name="AmazonS3-GetBucketWebsite-response-IndexDocument"></a>
The name of the index document for the website (for example `index.html`).
Type: [IndexDocument](API_IndexDocument.md) data type

 ** [RedirectAllRequestsTo](#API_GetBucketWebsite_ResponseSyntax) **   <a name="AmazonS3-GetBucketWebsite-response-RedirectAllRequestsTo"></a>
Specifies the redirect behavior of all requests to a website endpoint of an Amazon S3 bucket.
Type: [RedirectAllRequestsTo](API_RedirectAllRequestsTo.md) data type

 ** [RoutingRules](#API_GetBucketWebsite_ResponseSyntax) **   <a name="AmazonS3-GetBucketWebsite-response-RoutingRules"></a>
Rules that define when a redirect is applied and the redirect behavior.
Type: Array of [RoutingRule](API_RoutingRule.md) data types

## Examples
<a name="API_GetBucketWebsite_Examples"></a>

### Sample Request
<a name="API_GetBucketWebsite_Example_1"></a>

This request retrieves website configuration on the specified bucket.

```
            GET ?website HTTP/1.1
            Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
            Date: Thu, 27 Jan 2011 00:49:20 GMT
            Authorization: AWS AKIAIOSFODNN7EXAMPLE:n0Nhek72Ufg/u7Sm5C1dqRLs8XX=
```

### Sample Response
<a name="API_GetBucketWebsite_Example_2"></a>

This example illustrates one usage of GetBucketWebsite.

```
         HTTP/1.1 200 OK
         x-amz-id-2: YgIPIfBiKa2bj0KMgUAdQkf3ShJTOOpXUueF6QKo
         x-amz-request-id: 3848CD259D811111
         Date: Thu, 27 Jan 2011 00:49:26 GMT
         Content-Length: 240
         Content-Type: application/xml
         Transfer-Encoding: chunked
         Server: AmazonS3

         <?xml version="1.0" encoding="UTF-8"?>
         <WebsiteConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
           <IndexDocument>
             <Suffix>index.html</Suffix>
           </IndexDocument>
          <ErrorDocument>
            <Key>404.html</Key>
          </ErrorDocument>
         </WebsiteConfiguration>
```

## See Also
<a name="API_GetBucketWebsite_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketWebsite)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/GetBucketWebsite)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketWebsite)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketWebsite)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketWebsite)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketWebsite)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketWebsite)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketWebsite)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketWebsite)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketWebsite)
