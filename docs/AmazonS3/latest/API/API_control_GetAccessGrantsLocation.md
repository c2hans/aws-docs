---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessGrantsLocation.html
---

# GetAccessGrantsLocation
<a name="API_control_GetAccessGrantsLocation"></a>

Retrieves the details of a particular location registered in your S3 Access Grants instance.

Permissions
You must have the `s3:GetAccessGrantsLocation` permission to use this operation.

## Request Syntax
<a name="API_control_GetAccessGrantsLocation_RequestSyntax"></a>

```
GET /v20180820/accessgrantsinstance/location/{{id}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_GetAccessGrantsLocation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_control_GetAccessGrantsLocation_RequestSyntax) **   <a name="AmazonS3-control_GetAccessGrantsLocation-request-uri-uri-AccessGrantsLocationId"></a>
The ID of the registered location that you are retrieving. S3 Access Grants assigns this ID when you register the location. S3 Access Grants assigns the ID `default` to the default location `s3://` and assigns an auto-generated ID to other locations that you register.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-]+`
Required: Yes

 ** [x-amz-account-id](#API_control_GetAccessGrantsLocation_RequestSyntax) **   <a name="AmazonS3-control_GetAccessGrantsLocation-request-header-AccountId"></a>
The AWS account ID of the S3 Access Grants instance.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_GetAccessGrantsLocation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_GetAccessGrantsLocation_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetAccessGrantsLocationResult>
   <CreatedAt>timestamp</CreatedAt>
   <AccessGrantsLocationId>string</AccessGrantsLocationId>
   <AccessGrantsLocationArn>string</AccessGrantsLocationArn>
   <LocationScope>string</LocationScope>
   <IAMRoleArn>string</IAMRoleArn>
</GetAccessGrantsLocationResult>
```

## Response Elements
<a name="API_control_GetAccessGrantsLocation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetAccessGrantsLocationResult](#API_control_GetAccessGrantsLocation_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessGrantsLocation-response-GetAccessGrantsLocationResult"></a>
Root level tag for the GetAccessGrantsLocationResult parameters.
Required: Yes

 ** [AccessGrantsLocationArn](#API_control_GetAccessGrantsLocation_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessGrantsLocation-response-AccessGrantsLocationArn"></a>
The Amazon Resource Name (ARN) of the registered location.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:access\-grants\/location/[a-zA-Z0-9\-]+`

 ** [AccessGrantsLocationId](#API_control_GetAccessGrantsLocation_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessGrantsLocation-response-AccessGrantsLocationId"></a>
The ID of the registered location to which you are granting access. S3 Access Grants assigns this ID when you register the location. S3 Access Grants assigns the ID `default` to the default location `s3://` and assigns an auto-generated ID to other locations that you register.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-]+`

 ** [CreatedAt](#API_control_GetAccessGrantsLocation_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessGrantsLocation-response-CreatedAt"></a>
The date and time when you registered the location.
Type: Timestamp

 ** [IAMRoleArn](#API_control_GetAccessGrantsLocation_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessGrantsLocation-response-IAMRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role for the registered location. S3 Access Grants assumes this role to manage access to the registered location.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[^:]+:iam::\d{12}:role/.*`

 ** [LocationScope](#API_control_GetAccessGrantsLocation_ResponseSyntax) **   <a name="AmazonS3-control_GetAccessGrantsLocation-response-LocationScope"></a>
The S3 URI path to the registered location. The location scope can be the default S3 location `s3://`, the S3 path to a bucket, or the S3 path to a bucket and prefix. A prefix in S3 is a string of characters at the beginning of an object key name used to organize the objects that you store in your S3 buckets. For example, object key names that start with the `engineering/` prefix or object key names that start with the `marketing/campaigns/` prefix.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `^.+$`

## See Also
<a name="API_control_GetAccessGrantsLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetAccessGrantsLocation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/GetAccessGrantsLocation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetAccessGrantsLocation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetAccessGrantsLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetAccessGrantsLocation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetAccessGrantsLocation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetAccessGrantsLocation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetAccessGrantsLocation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetAccessGrantsLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetAccessGrantsLocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
