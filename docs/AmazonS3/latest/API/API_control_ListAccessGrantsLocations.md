---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessGrantsLocations.html
---

# ListAccessGrantsLocations
<a name="API_control_ListAccessGrantsLocations"></a>

Returns a list of the locations registered in your S3 Access Grants instance.

Permissions
You must have the `s3:ListAccessGrantsLocations` permission to use this operation.

## Request Syntax
<a name="API_control_ListAccessGrantsLocations_RequestSyntax"></a>

```
GET /v20180820/accessgrantsinstance/locations?locationscope={{LocationScope}}&maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_ListAccessGrantsLocations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [locationscope](#API_control_ListAccessGrantsLocations_RequestSyntax) **   <a name="AmazonS3-control_ListAccessGrantsLocations-request-uri-querystring-LocationScope"></a>
The S3 path to the location that you are registering. The location scope can be the default S3 location `s3://`, the S3 path to a bucket `s3://<bucket>`, or the S3 path to a bucket and prefix `s3://<bucket>/<prefix>`. A prefix in S3 is a string of characters at the beginning of an object key name used to organize the objects that you store in your S3 buckets. For example, object key names that start with the `engineering/` prefix or object key names that start with the `marketing/campaigns/` prefix.
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `^.+$`

 ** [maxResults](#API_control_ListAccessGrantsLocations_RequestSyntax) **   <a name="AmazonS3-control_ListAccessGrantsLocations-request-uri-querystring-MaxResults"></a>
The maximum number of access grants that you would like returned in the `List Access Grants` response. If the results include the pagination token `NextToken`, make another call using the `NextToken` to determine if there are more results.
Valid Range: Minimum value of 0. Maximum value of 1000.

 ** [nextToken](#API_control_ListAccessGrantsLocations_RequestSyntax) **   <a name="AmazonS3-control_ListAccessGrantsLocations-request-uri-querystring-NextToken"></a>
A pagination token to request the next page of results. Pass this value into a subsequent `List Access Grants Locations` request in order to retrieve the next page of results.

 ** [x-amz-account-id](#API_control_ListAccessGrantsLocations_RequestSyntax) **   <a name="AmazonS3-control_ListAccessGrantsLocations-request-header-AccountId"></a>
The AWS account ID of the S3 Access Grants instance.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_ListAccessGrantsLocations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_ListAccessGrantsLocations_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListAccessGrantsLocationsResult>
   <NextToken>string</NextToken>
   <AccessGrantsLocationsList>
      <AccessGrantsLocation>
         <AccessGrantsLocationArn>string</AccessGrantsLocationArn>
         <AccessGrantsLocationId>string</AccessGrantsLocationId>
         <CreatedAt>timestamp</CreatedAt>
         <IAMRoleArn>string</IAMRoleArn>
         <LocationScope>string</LocationScope>
      </AccessGrantsLocation>
   </AccessGrantsLocationsList>
</ListAccessGrantsLocationsResult>
```

## Response Elements
<a name="API_control_ListAccessGrantsLocations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListAccessGrantsLocationsResult](#API_control_ListAccessGrantsLocations_ResponseSyntax) **   <a name="AmazonS3-control_ListAccessGrantsLocations-response-ListAccessGrantsLocationsResult"></a>
Root level tag for the ListAccessGrantsLocationsResult parameters.
Required: Yes

 ** [AccessGrantsLocationsList](#API_control_ListAccessGrantsLocations_ResponseSyntax) **   <a name="AmazonS3-control_ListAccessGrantsLocations-response-AccessGrantsLocationsList"></a>
A container for a list of registered locations in an S3 Access Grants instance.
Type: Array of [ListAccessGrantsLocationsEntry](API_control_ListAccessGrantsLocationsEntry.md) data types

 ** [NextToken](#API_control_ListAccessGrantsLocations_ResponseSyntax) **   <a name="AmazonS3-control_ListAccessGrantsLocations-response-NextToken"></a>
A pagination token to request the next page of results. Pass this value into a subsequent `List Access Grants Locations` request in order to retrieve the next page of results.
Type: String

## See Also
<a name="API_control_ListAccessGrantsLocations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/ListAccessGrantsLocations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/ListAccessGrantsLocations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListAccessGrantsLocations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/ListAccessGrantsLocations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListAccessGrantsLocations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/ListAccessGrantsLocations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/ListAccessGrantsLocations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/ListAccessGrantsLocations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/ListAccessGrantsLocations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListAccessGrantsLocations)
