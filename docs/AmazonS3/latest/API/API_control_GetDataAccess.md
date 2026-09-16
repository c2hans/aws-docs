---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetDataAccess.html
---

# GetDataAccess
<a name="API_control_GetDataAccess"></a>

Returns a temporary access credential from S3 Access Grants to the grantee or client application. The [temporary credential](https://docs.aws.amazon.com/STS/latest/APIReference/API_Credentials.html) is an AWS STS token that grants them access to the S3 data.

Permissions
You must have the `s3:GetDataAccess` permission to use this operation.

Additional Permissions
The IAM role that S3 Access Grants assumes must have the following permissions specified in the trust policy when registering the location: `sts:AssumeRole`, for directory users or groups `sts:SetContext`, and for IAM users or roles `sts:SetSourceIdentity`.

## Request Syntax
<a name="API_control_GetDataAccess_RequestSyntax"></a>

```
GET /v20180820/accessgrantsinstance/dataaccess?auditContext={{AuditContext}}&durationSeconds={{DurationSeconds}}&permission={{Permission}}&privilege={{Privilege}}&target={{Target}}&targetType={{TargetType}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_GetDataAccess_RequestParameters"></a>

The request uses the following URI parameters.

 ** [auditContext](#API_control_GetDataAccess_RequestSyntax) **   <a name="AmazonS3-control_GetDataAccess-request-uri-querystring-AuditContext"></a>
The context to identify the job or query associated with the credential request. This information will be displayed in CloudTrail log in your account.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [durationSeconds](#API_control_GetDataAccess_RequestSyntax) **   <a name="AmazonS3-control_GetDataAccess-request-uri-querystring-DurationSeconds"></a>
The session duration, in seconds, of the temporary access credential that S3 Access Grants vends to the grantee or client application. The default value is 1 hour, but the grantee can specify a range from 900 seconds (15 minutes) up to 43200 seconds (12 hours). If the grantee requests a value higher than this maximum, the operation fails.
Valid Range: Minimum value of 900. Maximum value of 43200.

 ** [permission](#API_control_GetDataAccess_RequestSyntax) **   <a name="AmazonS3-control_GetDataAccess-request-uri-querystring-Permission"></a>
The type of permission granted to your S3 data, which can be set to one of the following values:
+  `READ` – Grant read-only access to the S3 data.
+  `WRITE` – Grant write-only access to the S3 data.
+  `READWRITE` – Grant both read and write access to the S3 data.
Valid Values: `READ | WRITE | READWRITE`
Required: Yes

 ** [privilege](#API_control_GetDataAccess_RequestSyntax) **   <a name="AmazonS3-control_GetDataAccess-request-uri-querystring-Privilege"></a>
The scope of the temporary access credential that S3 Access Grants vends to the grantee or client application.
+  `Default` – The scope of the returned temporary access token is the scope of the grant that is closest to the target scope.
+  `Minimal` – The scope of the returned temporary access token is the same as the requested target scope as long as the requested scope is the same as or a subset of the grant scope.
Valid Values: `Minimal | Default`

 ** [target](#API_control_GetDataAccess_RequestSyntax) **   <a name="AmazonS3-control_GetDataAccess-request-uri-querystring-Target"></a>
The S3 URI path of the data to which you are requesting temporary access credentials. If the requesting account has an access grant for this data, S3 Access Grants vends temporary access credentials in the response.
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `^.+$`
Required: Yes

 ** [targetType](#API_control_GetDataAccess_RequestSyntax) **   <a name="AmazonS3-control_GetDataAccess-request-uri-querystring-TargetType"></a>
The type of `Target`. The only possible value is `Object`. Pass this value if the target data that you would like to access is a path to an object. Do not pass this value if the target data is a bucket or a bucket and a prefix.
Valid Values: `Object`

 ** [x-amz-account-id](#API_control_GetDataAccess_RequestSyntax) **   <a name="AmazonS3-control_GetDataAccess-request-header-AccountId"></a>
The AWS account ID of the S3 Access Grants instance.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_GetDataAccess_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_GetDataAccess_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetDataAccessResult>
   <Credentials>
      <AccessKeyId>string</AccessKeyId>
      <Expiration>timestamp</Expiration>
      <SecretAccessKey>string</SecretAccessKey>
      <SessionToken>string</SessionToken>
   </Credentials>
   <MatchedGrantTarget>string</MatchedGrantTarget>
   <Grantee>
      <GranteeIdentifier>string</GranteeIdentifier>
      <GranteeType>string</GranteeType>
   </Grantee>
</GetDataAccessResult>
```

## Response Elements
<a name="API_control_GetDataAccess_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetDataAccessResult](#API_control_GetDataAccess_ResponseSyntax) **   <a name="AmazonS3-control_GetDataAccess-response-GetDataAccessResult"></a>
Root level tag for the GetDataAccessResult parameters.
Required: Yes

 ** [Credentials](#API_control_GetDataAccess_ResponseSyntax) **   <a name="AmazonS3-control_GetDataAccess-response-Credentials"></a>
The temporary credential token that S3 Access Grants vends.
Type: [Credentials](API_control_Credentials.md) data type

 ** [Grantee](#API_control_GetDataAccess_ResponseSyntax) **   <a name="AmazonS3-control_GetDataAccess-response-Grantee"></a>
The user, group, or role that was granted access to the S3 location scope. For directory identities, this API also returns the grants of the IAM role used for the identity-aware request. For more information on identity-aware sessions, see [Granting permissions to use identity-aware console sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_sts-setcontext.html).
Type: [Grantee](API_control_Grantee.md) data type

 ** [MatchedGrantTarget](#API_control_GetDataAccess_ResponseSyntax) **   <a name="AmazonS3-control_GetDataAccess-response-MatchedGrantTarget"></a>
The S3 URI path of the data to which you are being granted temporary access credentials.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `^.+$`

## See Also
<a name="API_control_GetDataAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetDataAccess)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/GetDataAccess)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetDataAccess)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetDataAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetDataAccess)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetDataAccess)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetDataAccess)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetDataAccess)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetDataAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetDataAccess)
