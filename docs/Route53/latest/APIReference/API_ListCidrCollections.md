---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListCidrCollections.html
---

# ListCidrCollections
<a name="API_ListCidrCollections"></a>

Returns a paginated list of CIDR collections in the AWS account (metadata only).

## Request Syntax
<a name="API_ListCidrCollections_RequestSyntax"></a>

```
GET /2013-04-01/cidrcollection?maxresults={{MaxResults}}&nexttoken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCidrCollections_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxresults](#API_ListCidrCollections_RequestSyntax) **   <a name="Route53-ListCidrCollections-request-uri-MaxResults"></a>
The maximum number of CIDR collections to return in the response.

 ** [nexttoken](#API_ListCidrCollections_RequestSyntax) **   <a name="Route53-ListCidrCollections-request-uri-NextToken"></a>
An opaque pagination token to indicate where the service is to begin enumerating results.
If no value is provided, the listing of results starts from the beginning.
Length Constraints: Maximum length of 1024.

## Request Body
<a name="API_ListCidrCollections_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCidrCollections_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListCidrCollectionsResponse>
   <CidrCollections>
      <CollectionSummary>
         <Arn>string</Arn>
         <Id>string</Id>
         <Name>string</Name>
         <Version>long</Version>
      </CollectionSummary>
   </CidrCollections>
   <NextToken>string</NextToken>
</ListCidrCollectionsResponse>
```

## Response Elements
<a name="API_ListCidrCollections_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListCidrCollectionsResponse](#API_ListCidrCollections_ResponseSyntax) **   <a name="Route53-ListCidrCollections-response-ListCidrCollectionsResponse"></a>
Root level tag for the ListCidrCollectionsResponse parameters.
Required: Yes

 ** [CidrCollections](#API_ListCidrCollections_ResponseSyntax) **   <a name="Route53-ListCidrCollections-response-CidrCollections"></a>
A complex type with information about the CIDR collection.
Type: Array of [CollectionSummary](API_CollectionSummary.md) objects

 ** [NextToken](#API_ListCidrCollections_ResponseSyntax) **   <a name="Route53-ListCidrCollections-response-NextToken"></a>
An opaque pagination token to indicate where the service is to begin enumerating results.
If no value is provided, the listing of results starts from the beginning.
Type: String
Length Constraints: Maximum length of 1024.

## Errors
<a name="API_ListCidrCollections_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_ListCidrCollections_Examples"></a>

### Example request
<a name="API_ListCidrCollections_Example_1"></a>

This example illustrates one usage of ListCidrCollections.

```
GET /2013-04-01/cidrcollection?maxresults=1
```

### Example response
<a name="API_ListCidrCollections_Example_2"></a>

This example illustrates one usage of ListCidrCollections.

```
HTTP/1.1 200
<?xml version="1.0"?>
<ListCidrCollectionsResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">>
   <NextToken>eyJjb2xsZWN0aW9uSWQiOiIwNGJmZjEyZS04NTdjLTFiNmEtNTc2OS0wMTQwMzg4NmE1NzkiLCJjb2xsZWN0aW9uTmFtZSI6ImZlbndhLTEifQ==</NextToken>
     <CidrCollections>
       <member>
         <Arn>arn:aws:route53:::cidrcollection/c8c02a84-aaaa-bbbb-e0d2-d833a2f80106</<Arn>
         <Id>c8c02a84-aaaa-bbbb-e0d2-d833a2f80106</Id>
         <Name>isp-city-cidrs</Name>
         <Version>1</ersion>
       </member>
    </CidrCollections>
</ListCidrCollectionsResponse>
```

## See Also
<a name="API_ListCidrCollections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/ListCidrCollections)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/ListCidrCollections)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ListCidrCollections)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/ListCidrCollections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ListCidrCollections)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/ListCidrCollections)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/ListCidrCollections)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/ListCidrCollections)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/ListCidrCollections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ListCidrCollections)
