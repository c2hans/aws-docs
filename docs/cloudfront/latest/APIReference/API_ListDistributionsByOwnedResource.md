---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListDistributionsByOwnedResource.html
---

# ListDistributionsByOwnedResource

Lists the CloudFront distributions that are associated with the specified resource that you own.

## Request Syntax
<a name="API_ListDistributionsByOwnedResource_RequestSyntax"></a>

```
GET /2020-05-31/distributionsByOwnedResource/{{ResourceArn}}?Marker={{Marker}}&MaxItems={{MaxItems}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDistributionsByOwnedResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Marker](#API_ListDistributionsByOwnedResource_RequestSyntax) **   <a name="cloudfront-ListDistributionsByOwnedResource-request-uri-Marker"></a>
Use this field when paginating results to indicate where to begin in your list of distributions. The response includes distributions in the list that occur after the marker. To get the next page of the list, set this field's value to the value of `NextMarker` from the current page's response.

 ** [MaxItems](#API_ListDistributionsByOwnedResource_RequestSyntax) **   <a name="cloudfront-ListDistributionsByOwnedResource-request-uri-MaxItems"></a>
The maximum number of distributions to return.

 ** [ResourceArn](#API_ListDistributionsByOwnedResource_RequestSyntax) **   <a name="cloudfront-ListDistributionsByOwnedResource-request-uri-ResourceArn"></a>
The ARN of the CloudFront resource that you've shared with other AWS accounts.
Required: Yes

## Request Body
<a name="API_ListDistributionsByOwnedResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDistributionsByOwnedResource_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<DistributionList>
   <IsTruncated>boolean</IsTruncated>
   <Items>
      <DistributionIdOwner>
         <DistributionId>string</DistributionId>
         <OwnerAccountId>string</OwnerAccountId>
      </DistributionIdOwner>
   </Items>
   <Marker>string</Marker>
   <MaxItems>integer</MaxItems>
   <NextMarker>string</NextMarker>
   <Quantity>integer</Quantity>
</DistributionList>
```

## Response Elements
<a name="API_ListDistributionsByOwnedResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [DistributionList](#API_ListDistributionsByOwnedResource_ResponseSyntax) **   <a name="cloudfront-ListDistributionsByOwnedResource-response-DistributionList"></a>
Root level tag for the DistributionList parameters.
Required: Yes

 ** [IsTruncated](#API_ListDistributionsByOwnedResource_ResponseSyntax) **   <a name="cloudfront-ListDistributionsByOwnedResource-response-IsTruncated"></a>
A flag that indicates whether more `DistributionIdOwner` objects remain to be listed. If your results were truncated, you can make a follow-up pagination request using the `Marker` request parameter to retrieve more results in the list.
Type: Boolean

 ** [Items](#API_ListDistributionsByOwnedResource_ResponseSyntax) **   <a name="cloudfront-ListDistributionsByOwnedResource-response-Items"></a>
The number of `DistributionIdOwner` objects.
Type: Array of [DistributionIdOwner](API_DistributionIdOwner.md) objects

 ** [Marker](#API_ListDistributionsByOwnedResource_ResponseSyntax) **   <a name="cloudfront-ListDistributionsByOwnedResource-response-Marker"></a>
Use this field when paginating results to indicate where to begin in your list of `DistributionIdOwner` objects. The response includes distributions in the list that occur after the marker. To get the next page of the list, set this field's value to the value of `NextMarker` from the current page's response.
Type: String

 ** [MaxItems](#API_ListDistributionsByOwnedResource_ResponseSyntax) **   <a name="cloudfront-ListDistributionsByOwnedResource-response-MaxItems"></a>
The maximum number of `DistributionIdOwner` objects to return.
Type: Integer

 ** [NextMarker](#API_ListDistributionsByOwnedResource_ResponseSyntax) **   <a name="cloudfront-ListDistributionsByOwnedResource-response-NextMarker"></a>
A token used for pagination of results returned in the response. You can use the token from the previous request to define where the current request should begin.
Type: String

 ** [Quantity](#API_ListDistributionsByOwnedResource_ResponseSyntax) **   <a name="cloudfront-ListDistributionsByOwnedResource-response-Quantity"></a>
Specifies the actual number of `DistributionIdOwner` objects included in the list for the current page.
Type: Integer

## Errors
<a name="API_ListDistributionsByOwnedResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **
Access denied.
HTTP Status Code: 403

 ** EntityNotFound **
The entity was not found.
HTTP Status Code: 404

 ** InvalidArgument **
An argument is invalid.
HTTP Status Code: 400

 ** UnsupportedOperation **
This operation is not supported in this AWS Region.
HTTP Status Code: 400

## See Also
<a name="API_ListDistributionsByOwnedResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListDistributionsByOwnedResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/ListDistributionsByOwnedResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListDistributionsByOwnedResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListDistributionsByOwnedResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListDistributionsByOwnedResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListDistributionsByOwnedResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListDistributionsByOwnedResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListDistributionsByOwnedResource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListDistributionsByOwnedResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListDistributionsByOwnedResource)
