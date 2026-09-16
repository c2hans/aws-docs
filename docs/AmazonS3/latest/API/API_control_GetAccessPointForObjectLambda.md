---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointForObjectLambda.html
---

# GetAccessPointForObjectLambda
<a name="API_control_GetAccessPointForObjectLambda"></a>

**Note**
This operation is not supported by directory buckets.

Returns configuration information about the specified Object Lambda Access Point

The following actions are related to `GetAccessPointForObjectLambda`:
+  [CreateAccessPointForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPointForObjectLambda.html)
+  [DeleteAccessPointForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointForObjectLambda.html)
+  [ListAccessPointsForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPointsForObjectLambda.html)

## Request Syntax
<a name="API_control_GetAccessPointForObjectLambda_RequestSyntax"></a>

```
GET /v20180820/accesspointforobjectlambda/{{name}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_GetAccessPointForObjectLambda_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_control_GetAccessPointForObjectLambda_RequestSyntax) **   <a name="AmazonS3-control_GetAccessPointForObjectLambda-request-uri-uri-Name"></a>
The name of the Object Lambda Access Point.
Length Constraints: Minimum length of 3. Maximum length of 45.
Pattern: `^[a-z0-9]([a-z0-9\-]*[a-z0-9])?$`
Required: Yes

 ** [x-amz-account-id](#API_control_GetAccessPointForObjectLambda_RequestSyntax) **   <a name="AmazonS3-control_GetAccessPointForObjectLambda-request-header-AccountId"></a>
The account ID for the account that owns the specified Object Lambda Access Point.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_GetAccessPointForObjectLambda_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_GetAccessPointForObjectLambda_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetAccessPointForObjectLambdaResult>
   <Name>string</Name>
   <PublicAccessBlockConfiguration>
      <BlockPublicAcls>boolean</BlockPublicAcls>
      <BlockPublicPolicy>boolean</BlockPublicPolicy>
      <IgnorePublicAcls>boolean</IgnorePublicAcls>
      <RestrictPublicBuckets>boolean</RestrictPublicBuckets>
   </PublicAccessBlockConfiguration>
   <CreationDate>timestamp</CreationDate>
   <Alias>
      <Status>string</Status>
      <Value>string</Value>
   </Alias>
</GetAccessPointForObjectLambdaResult>
```

## Response Elements
<a name="API_control_GetAccessPointForObjectLambda_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetAccessPointForObjectLambdaResult](#API_control_GetAccessPointForObjectLambda_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessPointForObjectLambda-response-GetAccessPointForObjectLambdaResult"></a>
Root level tag for the GetAccessPointForObjectLambdaResult parameters.
Required: Yes

 ** [Alias](#API_control_GetAccessPointForObjectLambda_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessPointForObjectLambda-response-Alias"></a>
The alias of the Object Lambda Access Point.
Type: [ObjectLambdaAccessPointAlias](API_control_ObjectLambdaAccessPointAlias.md) data type

 ** [CreationDate](#API_control_GetAccessPointForObjectLambda_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessPointForObjectLambda-response-CreationDate"></a>
The date and time when the specified Object Lambda Access Point was created.
Type: Timestamp

 ** [Name](#API_control_GetAccessPointForObjectLambda_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessPointForObjectLambda-response-Name"></a>
The name of the Object Lambda Access Point.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 45.
Pattern: `^[a-z0-9]([a-z0-9\-]*[a-z0-9])?$`

 ** [PublicAccessBlockConfiguration](#API_control_GetAccessPointForObjectLambda_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessPointForObjectLambda-response-PublicAccessBlockConfiguration"></a>
Configuration to block all public access. This setting is turned on and can not be edited.
Type: [PublicAccessBlockConfiguration](API_control_PublicAccessBlockConfiguration.md) data type

## See Also
<a name="API_control_GetAccessPointForObjectLambda_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetAccessPointForObjectLambda)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/GetAccessPointForObjectLambda)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetAccessPointForObjectLambda)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetAccessPointForObjectLambda)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetAccessPointForObjectLambda)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetAccessPointForObjectLambda)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetAccessPointForObjectLambda)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetAccessPointForObjectLambda)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetAccessPointForObjectLambda)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetAccessPointForObjectLambda)
