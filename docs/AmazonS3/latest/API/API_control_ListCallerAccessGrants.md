---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListCallerAccessGrants.html
---

# ListCallerAccessGrants
<a name="API_control_ListCallerAccessGrants"></a>

Use this API to list the access grants that grant the caller access to Amazon S3 data through S3 Access Grants. The caller (grantee) can be an AWS Identity and Access Management (IAM) identity or AWS Identity Center corporate directory identity. You must pass the AWS account of the S3 data owner (grantor) in the request. You can, optionally, narrow the results by `GrantScope`, using a fragment of the data's S3 path, and S3 Access Grants will return only the grants with a path that contains the path fragment. You can also pass the `AllowedByApplication` filter in the request, which returns only the grants authorized for applications, whether the application is the caller's Identity Center application or any other application (`ALL`). For more information, see [List the caller's access grants](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-list-grants.html) in the *Amazon S3 User Guide*.

Permissions
You must have the `s3:ListCallerAccessGrants` permission to use this operation.

## Request Syntax
<a name="API_control_ListCallerAccessGrants_RequestSyntax"></a>

```
GET /v20180820/accessgrantsinstance/caller/grants?allowedByApplication={{AllowedByApplication}}&grantscope={{GrantScope}}&maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_ListCallerAccessGrants_RequestParameters"></a>

The request uses the following URI parameters.

 ** [allowedByApplication](#API_control_ListCallerAccessGrants_RequestSyntax) **   <a name="AmazonS3-control_ListCallerAccessGrants-request-uri-querystring-AllowedByApplication"></a>
If this optional parameter is passed in the request, a filter is applied to the results. The results will include only the access grants for the caller's Identity Center application or for any other applications (`ALL`).

 ** [grantscope](#API_control_ListCallerAccessGrants_RequestSyntax) **   <a name="AmazonS3-control_ListCallerAccessGrants-request-uri-querystring-GrantScope"></a>
The S3 path of the data that you would like to access. Must start with `s3://`. You can optionally pass only the beginning characters of a path, and S3 Access Grants will search for all applicable grants for the path fragment.
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `^.+$`

 ** [maxResults](#API_control_ListCallerAccessGrants_RequestSyntax) **   <a name="AmazonS3-control_ListCallerAccessGrants-request-uri-querystring-MaxResults"></a>
The maximum number of access grants that you would like returned in the `List Caller Access Grants` response. If the results include the pagination token `NextToken`, make another call using the `NextToken` to determine if there are more results.
Valid Range: Minimum value of 0. Maximum value of 1000.

 ** [nextToken](#API_control_ListCallerAccessGrants_RequestSyntax) **   <a name="AmazonS3-control_ListCallerAccessGrants-request-uri-querystring-NextToken"></a>
A pagination token to request the next page of results. Pass this value into a subsequent `List Caller Access Grants` request in order to retrieve the next page of results.

 ** [x-amz-account-id](#API_control_ListCallerAccessGrants_RequestSyntax) **   <a name="AmazonS3-control_ListCallerAccessGrants-request-header-AccountId"></a>
The AWS account ID of the S3 Access Grants instance.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_ListCallerAccessGrants_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_ListCallerAccessGrants_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListCallerAccessGrantsResult>
   <NextToken>string</NextToken>
   <CallerAccessGrantsList>
      <AccessGrant>
         <ApplicationArn>string</ApplicationArn>
         <GrantScope>string</GrantScope>
         <Permission>string</Permission>
      </AccessGrant>
   </CallerAccessGrantsList>
</ListCallerAccessGrantsResult>
```

## Response Elements
<a name="API_control_ListCallerAccessGrants_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListCallerAccessGrantsResult](#API_control_ListCallerAccessGrants_ResponseSyntax) **   <a name="AmazonS3-control_ListCallerAccessGrants-response-ListCallerAccessGrantsResult"></a>
Root level tag for the ListCallerAccessGrantsResult parameters.
Required: Yes

 ** [CallerAccessGrantsList](#API_control_ListCallerAccessGrants_ResponseSyntax) **   <a name="AmazonS3-control_ListCallerAccessGrants-response-CallerAccessGrantsList"></a>
A list of the caller's access grants that were created using S3 Access Grants and that grant the caller access to the S3 data of the AWS account ID that was specified in the request.
Type: Array of [ListCallerAccessGrantsEntry](API_control_ListCallerAccessGrantsEntry.md) data types

 ** [NextToken](#API_control_ListCallerAccessGrants_ResponseSyntax) **   <a name="AmazonS3-control_ListCallerAccessGrants-response-NextToken"></a>
A pagination token that you can use to request the next page of results. Pass this value into a subsequent `List Caller Access Grants` request in order to retrieve the next page of results.
Type: String

## See Also
<a name="API_control_ListCallerAccessGrants_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/ListCallerAccessGrants)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/ListCallerAccessGrants)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListCallerAccessGrants)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/ListCallerAccessGrants)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListCallerAccessGrants)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/ListCallerAccessGrants)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/ListCallerAccessGrants)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/ListCallerAccessGrants)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/ListCallerAccessGrants)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListCallerAccessGrants)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
