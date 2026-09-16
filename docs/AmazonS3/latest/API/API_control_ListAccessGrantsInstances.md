---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessGrantsInstances.html
---

# ListAccessGrantsInstances
<a name="API_control_ListAccessGrantsInstances"></a>

Returns a list of S3 Access Grants instances. An S3 Access Grants instance serves as a logical grouping for your individual access grants. You can only have one S3 Access Grants instance per Region per account.

Permissions
You must have the `s3:ListAccessGrantsInstances` permission to use this operation.

## Request Syntax
<a name="API_control_ListAccessGrantsInstances_RequestSyntax"></a>

```
GET /v20180820/accessgrantsinstances?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_ListAccessGrantsInstances_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_control_ListAccessGrantsInstances_RequestSyntax) **   <a name="AmazonS3-control_ListAccessGrantsInstances-request-uri-querystring-MaxResults"></a>
The maximum number of access grants that you would like returned in the `List Access Grants` response. If the results include the pagination token `NextToken`, make another call using the `NextToken` to determine if there are more results.
Valid Range: Minimum value of 0. Maximum value of 1000.

 ** [nextToken](#API_control_ListAccessGrantsInstances_RequestSyntax) **   <a name="AmazonS3-control_ListAccessGrantsInstances-request-uri-querystring-NextToken"></a>
A pagination token to request the next page of results. Pass this value into a subsequent `List Access Grants Instances` request in order to retrieve the next page of results.

 ** [x-amz-account-id](#API_control_ListAccessGrantsInstances_RequestSyntax) **   <a name="AmazonS3-control_ListAccessGrantsInstances-request-header-AccountId"></a>
The AWS account ID of the S3 Access Grants instance.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_ListAccessGrantsInstances_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_ListAccessGrantsInstances_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListAccessGrantsInstancesResult>
   <NextToken>string</NextToken>
   <AccessGrantsInstancesList>
      <AccessGrantsInstance>
         <AccessGrantsInstanceArn>string</AccessGrantsInstanceArn>
         <AccessGrantsInstanceId>string</AccessGrantsInstanceId>
         <CreatedAt>timestamp</CreatedAt>
         <IdentityCenterApplicationArn>string</IdentityCenterApplicationArn>
         <IdentityCenterArn>string</IdentityCenterArn>
         <IdentityCenterInstanceArn>string</IdentityCenterInstanceArn>
      </AccessGrantsInstance>
   </AccessGrantsInstancesList>
</ListAccessGrantsInstancesResult>
```

## Response Elements
<a name="API_control_ListAccessGrantsInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListAccessGrantsInstancesResult](#API_control_ListAccessGrantsInstances_ResponseSyntax) **   <a name="AmazonS3-control_ListAccessGrantsInstances-response-ListAccessGrantsInstancesResult"></a>
Root level tag for the ListAccessGrantsInstancesResult parameters.
Required: Yes

 ** [AccessGrantsInstancesList](#API_control_ListAccessGrantsInstances_ResponseSyntax) **   <a name="AmazonS3-control_ListAccessGrantsInstances-response-AccessGrantsInstancesList"></a>
A container for a list of S3 Access Grants instances.
Type: Array of [ListAccessGrantsInstanceEntry](API_control_ListAccessGrantsInstanceEntry.md) data types

 ** [NextToken](#API_control_ListAccessGrantsInstances_ResponseSyntax) **   <a name="AmazonS3-control_ListAccessGrantsInstances-response-NextToken"></a>
A pagination token to request the next page of results. Pass this value into a subsequent `List Access Grants Instances` request in order to retrieve the next page of results.
Type: String

## See Also
<a name="API_control_ListAccessGrantsInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/ListAccessGrantsInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/ListAccessGrantsInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListAccessGrantsInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/ListAccessGrantsInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListAccessGrantsInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/ListAccessGrantsInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/ListAccessGrantsInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/ListAccessGrantsInstances)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/ListAccessGrantsInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListAccessGrantsInstances)
