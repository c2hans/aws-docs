---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessGrant.html
---

# CreateAccessGrant
<a name="API_control_CreateAccessGrant"></a>

Creates an access grant that gives a grantee access to your S3 data. The grantee can be an IAM user or role or a directory user, or group. Before you can create a grant, you must have an S3 Access Grants instance in the same Region as the S3 data. You can create an S3 Access Grants instance using the [CreateAccessGrantsInstance](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessGrantsInstance.html). You must also have registered at least one S3 data location in your S3 Access Grants instance using [CreateAccessGrantsLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessGrantsLocation.html).

Permissions
You must have the `s3:CreateAccessGrant` permission to use this operation.

Additional Permissions
For any directory identity - `sso:DescribeInstance` and `sso:DescribeApplication`
For directory users - `identitystore:DescribeUser`
For directory groups - `identitystore:DescribeGroup`

## Request Syntax
<a name="API_control_CreateAccessGrant_RequestSyntax"></a>

```
POST /v20180820/accessgrantsinstance/grant HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
<?xml version="1.0" encoding="UTF-8"?>
<CreateAccessGrantRequest xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <AccessGrantsLocationId>{{string}}</AccessGrantsLocationId>
   <AccessGrantsLocationConfiguration>
      <S3SubPrefix>{{string}}</S3SubPrefix>
   </AccessGrantsLocationConfiguration>
   <Grantee>
      <GranteeIdentifier>{{string}}</GranteeIdentifier>
      <GranteeType>{{string}}</GranteeType>
   </Grantee>
   <Permission>{{string}}</Permission>
   <ApplicationArn>{{string}}</ApplicationArn>
   <S3PrefixType>{{string}}</S3PrefixType>
   <Tags>
      <Tag>
         <Key>{{string}}</Key>
         <Value>{{string}}</Value>
      </Tag>
   </Tags>
</CreateAccessGrantRequest>
```

## URI Request Parameters
<a name="API_control_CreateAccessGrant_RequestParameters"></a>

The request uses the following URI parameters.

 ** [x-amz-account-id](#API_control_CreateAccessGrant_RequestSyntax) **   <a name="AmazonS3-control_CreateAccessGrant-request-header-AccountId"></a>
The AWS account ID of the S3 Access Grants instance.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_CreateAccessGrant_RequestBody"></a>

The request accepts the following data in XML format.

 ** [CreateAccessGrantRequest](#API_control_CreateAccessGrant_RequestSyntax) **   <a name="AmazonS3-control_CreateAccessGrant-request-CreateAccessGrantRequest"></a>
Root level tag for the CreateAccessGrantRequest parameters.
Required: Yes

 ** [AccessGrantsLocationConfiguration](#API_control_CreateAccessGrant_RequestSyntax) **   <a name="AmazonS3-control_CreateAccessGrant-request-AccessGrantsLocationConfiguration"></a>
The configuration options of the grant location. The grant location is the S3 path to the data to which you are granting access. It contains the `S3SubPrefix` field. The grant scope is the result of appending the subprefix to the location scope of the registered location.
Type: [AccessGrantsLocationConfiguration](API_control_AccessGrantsLocationConfiguration.md) data type
Required: No

 ** [AccessGrantsLocationId](#API_control_CreateAccessGrant_RequestSyntax) **   <a name="AmazonS3-control_CreateAccessGrant-request-AccessGrantsLocationId"></a>
The ID of the registered location to which you are granting access. S3 Access Grants assigns this ID when you register the location. S3 Access Grants assigns the ID `default` to the default location `s3://` and assigns an auto-generated ID to other locations that you register.
If you are passing the `default` location, you cannot create an access grant for the entire default location. You must also specify a bucket or a bucket and prefix in the `Subprefix` field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-]+`
Required: Yes

 ** [ApplicationArn](#API_control_CreateAccessGrant_RequestSyntax) **   <a name="AmazonS3-control_CreateAccessGrant-request-ApplicationArn"></a>
The Amazon Resource Name (ARN) of an AWS IAM Identity Center application associated with your Identity Center instance. If an application ARN is included in the request to create an access grant, the grantee can only access the S3 data through this application.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:[^:]+:sso::\d{12}:application/.*$`
Required: No

 ** [Grantee](#API_control_CreateAccessGrant_RequestSyntax) **   <a name="AmazonS3-control_CreateAccessGrant-request-Grantee"></a>
The user, group, or role to which you are granting access. You can grant access to an IAM user or role. If you have added your corporate directory to AWS IAM Identity Center and associated your Identity Center instance with your S3 Access Grants instance, the grantee can also be a corporate directory user or group.
Type: [Grantee](API_control_Grantee.md) data type
Required: Yes

 ** [Permission](#API_control_CreateAccessGrant_RequestSyntax) **   <a name="AmazonS3-control_CreateAccessGrant-request-Permission"></a>
The type of access that you are granting to your S3 data, which can be set to one of the following values:
+  `READ` – Grant read-only access to the S3 data.
+  `WRITE` – Grant write-only access to the S3 data.
+  `READWRITE` – Grant both read and write access to the S3 data.
Type: String
Valid Values: `READ | WRITE | READWRITE`
Required: Yes

 ** [S3PrefixType](#API_control_CreateAccessGrant_RequestSyntax) **   <a name="AmazonS3-control_CreateAccessGrant-request-S3PrefixType"></a>
The type of `S3SubPrefix`. The only possible value is `Object`. Pass this value if the access grant scope is an object. Do not pass this value if the access grant scope is a bucket or a bucket and a prefix.
Type: String
Valid Values: `Object`
Required: No

 ** [Tags](#API_control_CreateAccessGrant_RequestSyntax) **   <a name="AmazonS3-control_CreateAccessGrant-request-Tags"></a>
The AWS resource tags that you are adding to the access grant. Each tag is a label consisting of a user-defined key and value. Tags can help you manage, identify, organize, search for, and filter resources.
Type: Array of [Tag](API_control_Tag.md) data types
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_control_CreateAccessGrant_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<CreateAccessGrantResult>
   <CreatedAt>timestamp</CreatedAt>
   <AccessGrantId>string</AccessGrantId>
   <AccessGrantArn>string</AccessGrantArn>
   <Grantee>
      <GranteeIdentifier>string</GranteeIdentifier>
      <GranteeType>string</GranteeType>
   </Grantee>
   <AccessGrantsLocationId>string</AccessGrantsLocationId>
   <AccessGrantsLocationConfiguration>
      <S3SubPrefix>string</S3SubPrefix>
   </AccessGrantsLocationConfiguration>
   <Permission>string</Permission>
   <ApplicationArn>string</ApplicationArn>
   <GrantScope>string</GrantScope>
</CreateAccessGrantResult>
```

## Response Elements
<a name="API_control_CreateAccessGrant_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [CreateAccessGrantResult](#API_control_CreateAccessGrant_ResponseSyntax) **   <a name="AmazonS3-control_CreateAccessGrant-response-CreateAccessGrantResult"></a>
Root level tag for the CreateAccessGrantResult parameters.
Required: Yes

 ** [AccessGrantArn](#API_control_CreateAccessGrant_ResponseSyntax) **   <a name="AmazonS3-control_CreateAccessGrant-response-AccessGrantArn"></a>
The Amazon Resource Name (ARN) of the access grant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:access\-grants\/grant/[a-zA-Z0-9\-]+`

 ** [AccessGrantId](#API_control_CreateAccessGrant_ResponseSyntax) **   <a name="AmazonS3-control_CreateAccessGrant-response-AccessGrantId"></a>
The ID of the access grant. S3 Access Grants auto-generates this ID when you create the access grant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-]+`

 ** [AccessGrantsLocationConfiguration](#API_control_CreateAccessGrant_ResponseSyntax) **   <a name="AmazonS3-control_CreateAccessGrant-response-AccessGrantsLocationConfiguration"></a>
The configuration options of the grant location. The grant location is the S3 path to the data to which you are granting access.
Type: [AccessGrantsLocationConfiguration](API_control_AccessGrantsLocationConfiguration.md) data type

 ** [AccessGrantsLocationId](#API_control_CreateAccessGrant_ResponseSyntax) **   <a name="AmazonS3-control_CreateAccessGrant-response-AccessGrantsLocationId"></a>
The ID of the registered location to which you are granting access. S3 Access Grants assigns this ID when you register the location. S3 Access Grants assigns the ID `default` to the default location `s3://` and assigns an auto-generated ID to other locations that you register.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-]+`

 ** [ApplicationArn](#API_control_CreateAccessGrant_ResponseSyntax) **   <a name="AmazonS3-control_CreateAccessGrant-response-ApplicationArn"></a>
The Amazon Resource Name (ARN) of an AWS IAM Identity Center application associated with your Identity Center instance. If the grant includes an application ARN, the grantee can only access the S3 data through this application.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:[^:]+:sso::\d{12}:application/.*$`

 ** [CreatedAt](#API_control_CreateAccessGrant_ResponseSyntax) **   <a name="AmazonS3-control_CreateAccessGrant-response-CreatedAt"></a>
The date and time when you created the access grant.
Type: Timestamp

 ** [Grantee](#API_control_CreateAccessGrant_ResponseSyntax) **   <a name="AmazonS3-control_CreateAccessGrant-response-Grantee"></a>
The user, group, or role to which you are granting access. You can grant access to an IAM user or role. If you have added your corporate directory to AWS IAM Identity Center and associated your Identity Center instance with your S3 Access Grants instance, the grantee can also be a corporate directory user or group.
Type: [Grantee](API_control_Grantee.md) data type

 ** [GrantScope](#API_control_CreateAccessGrant_ResponseSyntax) **   <a name="AmazonS3-control_CreateAccessGrant-response-GrantScope"></a>
The S3 path of the data to which you are granting access. It is the result of appending the `Subprefix` to the location scope.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `^.+$`

 ** [Permission](#API_control_CreateAccessGrant_ResponseSyntax) **   <a name="AmazonS3-control_CreateAccessGrant-response-Permission"></a>
The type of access that you are granting to your S3 data, which can be set to one of the following values:
+  `READ` – Grant read-only access to the S3 data.
+  `WRITE` – Grant write-only access to the S3 data.
+  `READWRITE` – Grant both read and write access to the S3 data.
Type: String
Valid Values: `READ | WRITE | READWRITE`

## See Also
<a name="API_control_CreateAccessGrant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/CreateAccessGrant)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/CreateAccessGrant)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/CreateAccessGrant)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/CreateAccessGrant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/CreateAccessGrant)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/CreateAccessGrant)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/CreateAccessGrant)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/CreateAccessGrant)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/CreateAccessGrant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/CreateAccessGrant)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
