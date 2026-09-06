---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessGrants.html
---

# ListAccessGrants
<a name="API_control_ListAccessGrants"></a>

Returns the list of access grants in your S3 Access Grants instance.

Permissions
You must have the `s3:ListAccessGrants` permission to use this operation.

## Request Syntax
<a name="API_control_ListAccessGrants_RequestSyntax"></a>

```
GET /v20180820/accessgrantsinstance/grants?application_arn={{ApplicationArn}}&granteeidentifier={{GranteeIdentifier}}&granteetype={{GranteeType}}&grantscope={{GrantScope}}&maxResults={{MaxResults}}&nextToken={{NextToken}}&permission={{Permission}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_ListAccessGrants_RequestParameters"></a>

The request uses the following URI parameters.

 ** [application\_arn](#API_control_ListAccessGrants_RequestSyntax) **   <a name="AmazonS3-control_ListAccessGrants-request-uri-querystring-ApplicationArn"></a>
The Amazon Resource Name (ARN) of an AWS IAM Identity Center application associated with your Identity Center instance. If the grant includes an application ARN, the grantee can only access the S3 data through this application.
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:[^:]+:sso::\d{12}:application/.*$`

 ** [granteeidentifier](#API_control_ListAccessGrants_RequestSyntax) **   <a name="AmazonS3-control_ListAccessGrants-request-uri-querystring-GranteeIdentifier"></a>
The unique identifer of the `Grantee`. If the grantee type is `IAM`, the identifier is the IAM Amazon Resource Name (ARN) of the user or role. If the grantee type is a directory user or group, the identifier is 128-bit universally unique identifier (UUID) in the format `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`. You can obtain this UUID from your AWS IAM Identity Center instance.

 ** [granteetype](#API_control_ListAccessGrants_RequestSyntax) **   <a name="AmazonS3-control_ListAccessGrants-request-uri-querystring-GranteeType"></a>
The type of the grantee to which access has been granted. It can be one of the following values:
+  `IAM` - An IAM user or role.
+  `DIRECTORY_USER` - Your corporate directory user. You can use this option if you have added your corporate identity directory to IAM Identity Center and associated the IAM Identity Center instance with your S3 Access Grants instance.
+  `DIRECTORY_GROUP` - Your corporate directory group. You can use this option if you have added your corporate identity directory to IAM Identity Center and associated the IAM Identity Center instance with your S3 Access Grants instance.
Valid Values: `DIRECTORY_USER | DIRECTORY_GROUP | IAM`

 ** [grantscope](#API_control_ListAccessGrants_RequestSyntax) **   <a name="AmazonS3-control_ListAccessGrants-request-uri-querystring-GrantScope"></a>
The S3 path of the data to which you are granting access. It is the result of appending the `Subprefix` to the location scope.
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `^.+$`

 ** [maxResults](#API_control_ListAccessGrants_RequestSyntax) **   <a name="AmazonS3-control_ListAccessGrants-request-uri-querystring-MaxResults"></a>
The maximum number of access grants that you would like returned in the `List Access Grants` response. If the results include the pagination token `NextToken`, make another call using the `NextToken` to determine if there are more results.
Valid Range: Minimum value of 0. Maximum value of 1000.

 ** [nextToken](#API_control_ListAccessGrants_RequestSyntax) **   <a name="AmazonS3-control_ListAccessGrants-request-uri-querystring-NextToken"></a>
A pagination token to request the next page of results. Pass this value into a subsequent `List Access Grants` request in order to retrieve the next page of results.

 ** [permission](#API_control_ListAccessGrants_RequestSyntax) **   <a name="AmazonS3-control_ListAccessGrants-request-uri-querystring-Permission"></a>
The type of permission granted to your S3 data, which can be set to one of the following values:
+  `READ` – Grant read-only access to the S3 data.
+  `WRITE` – Grant write-only access to the S3 data.
+  `READWRITE` – Grant both read and write access to the S3 data.
Valid Values: `READ | WRITE | READWRITE`

 ** [x-amz-account-id](#API_control_ListAccessGrants_RequestSyntax) **   <a name="AmazonS3-control_ListAccessGrants-request-header-AccountId"></a>
The AWS account ID of the S3 Access Grants instance.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_ListAccessGrants_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_ListAccessGrants_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListAccessGrantsResult>
   <NextToken>string</NextToken>
   <AccessGrantsList>
      <AccessGrant>
         <AccessGrantArn>string</AccessGrantArn>
         <AccessGrantId>string</AccessGrantId>
         <AccessGrantsLocationConfiguration>
            <S3SubPrefix>string</S3SubPrefix>
         </AccessGrantsLocationConfiguration>
         <AccessGrantsLocationId>string</AccessGrantsLocationId>
         <ApplicationArn>string</ApplicationArn>
         <CreatedAt>timestamp</CreatedAt>
         <Grantee>
            <GranteeIdentifier>string</GranteeIdentifier>
            <GranteeType>string</GranteeType>
         </Grantee>
         <GrantScope>string</GrantScope>
         <Permission>string</Permission>
      </AccessGrant>
   </AccessGrantsList>
</ListAccessGrantsResult>
```

## Response Elements
<a name="API_control_ListAccessGrants_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListAccessGrantsResult](#API_control_ListAccessGrants_ResponseSyntax) **   <a name="AmazonS3-control_ListAccessGrants-response-ListAccessGrantsResult"></a>
Root level tag for the ListAccessGrantsResult parameters.
Required: Yes

 ** [AccessGrantsList](#API_control_ListAccessGrants_ResponseSyntax) **   <a name="AmazonS3-control_ListAccessGrants-response-AccessGrantsList"></a>
A container for a list of grants in an S3 Access Grants instance.
Type: Array of [ListAccessGrantEntry](API_control_ListAccessGrantEntry.md) data types

 ** [NextToken](#API_control_ListAccessGrants_ResponseSyntax) **   <a name="AmazonS3-control_ListAccessGrants-response-NextToken"></a>
A pagination token to request the next page of results. Pass this value into a subsequent `List Access Grants` request in order to retrieve the next page of results.
Type: String

## See Also
<a name="API_control_ListAccessGrants_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/ListAccessGrants)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/ListAccessGrants)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListAccessGrants)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/ListAccessGrants)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListAccessGrants)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/ListAccessGrants)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/ListAccessGrants)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/ListAccessGrants)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/ListAccessGrants)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListAccessGrants)
