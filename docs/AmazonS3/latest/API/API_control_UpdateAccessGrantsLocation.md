---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateAccessGrantsLocation.html
---

# UpdateAccessGrantsLocation
<a name="API_control_UpdateAccessGrantsLocation"></a>

Updates the IAM role of a registered location in your S3 Access Grants instance.

Permissions
You must have the `s3:UpdateAccessGrantsLocation` permission to use this operation.

Additional Permissions
You must also have the following permission: `iam:PassRole`

## Request Syntax
<a name="API_control_UpdateAccessGrantsLocation_RequestSyntax"></a>

```
PUT /v20180820/accessgrantsinstance/location/{{id}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
<?xml version="1.0" encoding="UTF-8"?>
<UpdateAccessGrantsLocationRequest xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <IAMRoleArn>{{string}}</IAMRoleArn>
</UpdateAccessGrantsLocationRequest>
```

## URI Request Parameters
<a name="API_control_UpdateAccessGrantsLocation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_control_UpdateAccessGrantsLocation_RequestSyntax) **   <a name="AmazonS3-control_UpdateAccessGrantsLocation-request-uri-uri-AccessGrantsLocationId"></a>
The ID of the registered location that you are updating. S3 Access Grants assigns this ID when you register the location. S3 Access Grants assigns the ID `default` to the default location `s3://` and assigns an auto-generated ID to other locations that you register.
The ID of the registered location to which you are granting access. S3 Access Grants assigned this ID when you registered the location. S3 Access Grants assigns the ID `default` to the default location `s3://` and assigns an auto-generated ID to other locations that you register.
If you are passing the `default` location, you cannot create an access grant for the entire default location. You must also specify a bucket or a bucket and prefix in the `Subprefix` field.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-]+`
Required: Yes

 ** [x-amz-account-id](#API_control_UpdateAccessGrantsLocation_RequestSyntax) **   <a name="AmazonS3-control_UpdateAccessGrantsLocation-request-header-AccountId"></a>
The AWS account ID of the S3 Access Grants instance.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_UpdateAccessGrantsLocation_RequestBody"></a>

The request accepts the following data in XML format.

 ** [UpdateAccessGrantsLocationRequest](#API_control_UpdateAccessGrantsLocation_RequestSyntax) **   <a name="AmazonS3-control_UpdateAccessGrantsLocation-request-UpdateAccessGrantsLocationRequest"></a>
Root level tag for the UpdateAccessGrantsLocationRequest parameters.
Required: Yes

 ** [IAMRoleArn](#API_control_UpdateAccessGrantsLocation_RequestSyntax) **   <a name="AmazonS3-control_UpdateAccessGrantsLocation-request-IAMRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role for the registered location. S3 Access Grants assumes this role to manage access to the registered location.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[^:]+:iam::\d{12}:role/.*`
Required: Yes

## Response Syntax
<a name="API_control_UpdateAccessGrantsLocation_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<UpdateAccessGrantsLocationResult>
   <CreatedAt>timestamp</CreatedAt>
   <AccessGrantsLocationId>string</AccessGrantsLocationId>
   <AccessGrantsLocationArn>string</AccessGrantsLocationArn>
   <LocationScope>string</LocationScope>
   <IAMRoleArn>string</IAMRoleArn>
</UpdateAccessGrantsLocationResult>
```

## Response Elements
<a name="API_control_UpdateAccessGrantsLocation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [UpdateAccessGrantsLocationResult](#API_control_UpdateAccessGrantsLocation_ResponseSyntax) **   <a name="AmazonS3-control_UpdateAccessGrantsLocation-response-UpdateAccessGrantsLocationResult"></a>
Root level tag for the UpdateAccessGrantsLocationResult parameters.
Required: Yes

 ** [AccessGrantsLocationArn](#API_control_UpdateAccessGrantsLocation_ResponseSyntax) **   <a name="AmazonS3-control_UpdateAccessGrantsLocation-response-AccessGrantsLocationArn"></a>
The Amazon Resource Name (ARN) of the registered location that you are updating.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:access\-grants\/location/[a-zA-Z0-9\-]+`

 ** [AccessGrantsLocationId](#API_control_UpdateAccessGrantsLocation_ResponseSyntax) **   <a name="AmazonS3-control_UpdateAccessGrantsLocation-response-AccessGrantsLocationId"></a>
The ID of the registered location to which you are granting access. S3 Access Grants assigned this ID when you registered the location. S3 Access Grants assigns the ID `default` to the default location `s3://` and assigns an auto-generated ID to other locations that you register.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-]+`

 ** [CreatedAt](#API_control_UpdateAccessGrantsLocation_ResponseSyntax) **   <a name="AmazonS3-control_UpdateAccessGrantsLocation-response-CreatedAt"></a>
The date and time when you registered the location.
Type: Timestamp

 ** [IAMRoleArn](#API_control_UpdateAccessGrantsLocation_ResponseSyntax) **   <a name="AmazonS3-control_UpdateAccessGrantsLocation-response-IAMRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role of the registered location. S3 Access Grants assumes this role to manage access to the registered location.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[^:]+:iam::\d{12}:role/.*`

 ** [LocationScope](#API_control_UpdateAccessGrantsLocation_ResponseSyntax) **   <a name="AmazonS3-control_UpdateAccessGrantsLocation-response-LocationScope"></a>
The S3 URI path of the location that you are updating. You cannot update the scope of the registered location. The location scope can be the default S3 location `s3://`, the S3 path to a bucket `s3://<bucket>`, or the S3 path to a bucket and prefix `s3://<bucket>/<prefix>`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `^.+$`

## See Also
<a name="API_control_UpdateAccessGrantsLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/UpdateAccessGrantsLocation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/UpdateAccessGrantsLocation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/UpdateAccessGrantsLocation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/UpdateAccessGrantsLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/UpdateAccessGrantsLocation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/UpdateAccessGrantsLocation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/UpdateAccessGrantsLocation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/UpdateAccessGrantsLocation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/UpdateAccessGrantsLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/UpdateAccessGrantsLocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
