---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessGrant.html
---

# GetAccessGrant
<a name="API_control_GetAccessGrant"></a>

Get the details of an access grant from your S3 Access Grants instance.

Permissions
You must have the `s3:GetAccessGrant` permission to use this operation.

## Request Syntax
<a name="API_control_GetAccessGrant_RequestSyntax"></a>

```
GET /v20180820/accessgrantsinstance/grant/{{id}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_GetAccessGrant_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_control_GetAccessGrant_RequestSyntax) **   <a name="AmazonS3-control_GetAccessGrant-request-uri-uri-AccessGrantId"></a>
The ID of the access grant. S3 Access Grants auto-generates this ID when you create the access grant.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-]+`
Required: Yes

 ** [x-amz-account-id](#API_control_GetAccessGrant_RequestSyntax) **   <a name="AmazonS3-control_GetAccessGrant-request-header-AccountId"></a>
The AWS account ID of the S3 Access Grants instance.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_GetAccessGrant_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_GetAccessGrant_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetAccessGrantResult>
   <CreatedAt>timestamp</CreatedAt>
   <AccessGrantId>string</AccessGrantId>
   <AccessGrantArn>string</AccessGrantArn>
   <Grantee>
      <GranteeIdentifier>string</GranteeIdentifier>
      <GranteeType>string</GranteeType>
   </Grantee>
   <Permission>string</Permission>
   <AccessGrantsLocationId>string</AccessGrantsLocationId>
   <AccessGrantsLocationConfiguration>
      <S3SubPrefix>string</S3SubPrefix>
   </AccessGrantsLocationConfiguration>
   <GrantScope>string</GrantScope>
   <ApplicationArn>string</ApplicationArn>
</GetAccessGrantResult>
```

## Response Elements
<a name="API_control_GetAccessGrant_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetAccessGrantResult](#API_control_GetAccessGrant_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessGrant-response-GetAccessGrantResult"></a>
Root level tag for the GetAccessGrantResult parameters.
Required: Yes

 ** [AccessGrantArn](#API_control_GetAccessGrant_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessGrant-response-AccessGrantArn"></a>
The Amazon Resource Name (ARN) of the access grant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:access\-grants\/grant/[a-zA-Z0-9\-]+`

 ** [AccessGrantId](#API_control_GetAccessGrant_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessGrant-response-AccessGrantId"></a>
The ID of the access grant. S3 Access Grants auto-generates this ID when you create the access grant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-]+`

 ** [AccessGrantsLocationConfiguration](#API_control_GetAccessGrant_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessGrant-response-AccessGrantsLocationConfiguration"></a>
The configuration options of the grant location. The grant location is the S3 path to the data to which you are granting access.
Type: [AccessGrantsLocationConfiguration](API_control_AccessGrantsLocationConfiguration.md) data type

 ** [AccessGrantsLocationId](#API_control_GetAccessGrant_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessGrant-response-AccessGrantsLocationId"></a>
The ID of the registered location to which you are granting access. S3 Access Grants assigns this ID when you register the location. S3 Access Grants assigns the ID `default` to the default location `s3://` and assigns an auto-generated ID to other locations that you register.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-]+`

 ** [ApplicationArn](#API_control_GetAccessGrant_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessGrant-response-ApplicationArn"></a>
The Amazon Resource Name (ARN) of an AWS IAM Identity Center application associated with your Identity Center instance. If the grant includes an application ARN, the grantee can only access the S3 data through this application.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:[^:]+:sso::\d{12}:application/.*$`

 ** [CreatedAt](#API_control_GetAccessGrant_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessGrant-response-CreatedAt"></a>
The date and time when you created the access grant.
Type: Timestamp

 ** [Grantee](#API_control_GetAccessGrant_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessGrant-response-Grantee"></a>
The user, group, or role to which you are granting access. You can grant access to an IAM user or role. If you have added a corporate directory to AWS IAM Identity Center and associated this Identity Center instance with the S3 Access Grants instance, the grantee can also be a corporate directory user or group.
Type: [Grantee](API_control_Grantee.md) data type

 ** [GrantScope](#API_control_GetAccessGrant_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessGrant-response-GrantScope"></a>
The S3 path of the data to which you are granting access. It is the result of appending the `Subprefix` to the location scope.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `^.+$`

 ** [Permission](#API_control_GetAccessGrant_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessGrant-response-Permission"></a>
The type of permission that was granted in the access grant. Can be one of the following values:
+  `READ` – Grant read-only access to the S3 data.
+  `WRITE` – Grant write-only access to the S3 data.
+  `READWRITE` – Grant both read and write access to the S3 data.
Type: String
Valid Values: `READ | WRITE | READWRITE`

## See Also
<a name="API_control_GetAccessGrant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetAccessGrant)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/GetAccessGrant)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetAccessGrant)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetAccessGrant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetAccessGrant)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetAccessGrant)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetAccessGrant)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetAccessGrant)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetAccessGrant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetAccessGrant)
