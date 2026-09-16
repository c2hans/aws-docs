---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListCidrLocations.html
---

# ListCidrLocations
<a name="API_ListCidrLocations"></a>

Returns a paginated list of CIDR locations for the given collection (metadata only, does not include CIDR blocks).

## Request Syntax
<a name="API_ListCidrLocations_RequestSyntax"></a>

```
GET /2013-04-01/cidrcollection/{{CidrCollectionId}}?maxresults={{MaxResults}}&nexttoken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCidrLocations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CidrCollectionId](#API_ListCidrLocations_RequestSyntax) **   <a name="Route53-ListCidrLocations-request-uri-CollectionId"></a>
The CIDR collection ID.
Pattern: `[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}`
Required: Yes

 ** [maxresults](#API_ListCidrLocations_RequestSyntax) **   <a name="Route53-ListCidrLocations-request-uri-MaxResults"></a>
The maximum number of CIDR collection locations to return in the response.

 ** [nexttoken](#API_ListCidrLocations_RequestSyntax) **   <a name="Route53-ListCidrLocations-request-uri-NextToken"></a>
An opaque pagination token to indicate where the service is to begin enumerating results.
If no value is provided, the listing of results starts from the beginning.
Length Constraints: Maximum length of 1024.

## Request Body
<a name="API_ListCidrLocations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCidrLocations_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListCidrLocationsResponse>
   <CidrLocations>
      <LocationSummary>
         <LocationName>string</LocationName>
      </LocationSummary>
   </CidrLocations>
   <NextToken>string</NextToken>
</ListCidrLocationsResponse>
```

## Response Elements
<a name="API_ListCidrLocations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListCidrLocationsResponse](#API_ListCidrLocations_ResponseSyntax) **   <a name="Route53-ListCidrLocations-response-ListCidrLocationsResponse"></a>
Root level tag for the ListCidrLocationsResponse parameters.
Required: Yes

 ** [CidrLocations](#API_ListCidrLocations_ResponseSyntax) **   <a name="Route53-ListCidrLocations-response-CidrLocations"></a>
A complex type that contains information about the list of CIDR locations.
Type: Array of [LocationSummary](API_LocationSummary.md) objects

 ** [NextToken](#API_ListCidrLocations_ResponseSyntax) **   <a name="Route53-ListCidrLocations-response-NextToken"></a>
An opaque pagination token to indicate where the service is to begin enumerating results.
If no value is provided, the listing of results starts from the beginning.
Type: String
Length Constraints: Maximum length of 1024.

## Errors
<a name="API_ListCidrLocations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchCidrCollectionException **
The CIDR collection you specified, doesn't exist.
HTTP Status Code: 404

## Examples
<a name="API_ListCidrLocations_Examples"></a>

### Example request
<a name="API_ListCidrLocations_Example_1"></a>

This example illustrates one usage of ListCidrLocations.

```
GET /2013-04-01/cidrcollection/c8c02a84-aaaa-bbbb-e0d2-d833a2f80106?maxresults=1
```

### Example response
<a name="API_ListCidrLocations_Example_2"></a>

This example illustrates one usage of ListCidrLocations.

```
HTTP/1.1 200
<?xml version="1.0"?>
<ListCidrLocationsResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">>
    <NextToken>eyJjb2xsZWN0aW9uSWQiOiIwNGJmZjEyZS04NTdjLTFiNmEtNTc2OS0wMTQwMzg4NmE1NzkiLCJjb2xsZWN0aW9uTmFtZSI6ImZlbndhLTEifQ==</NextToken>
      <CidrLocations>
         <member>
           <LocationName>location-1</LocationName>
         </member>
     </CidrLocations>
</ListCidrLocationsResponse>
```

## See Also
<a name="API_ListCidrLocations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/ListCidrLocations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/ListCidrLocations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ListCidrLocations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/ListCidrLocations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ListCidrLocations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/ListCidrLocations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/ListCidrLocations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/ListCidrLocations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/ListCidrLocations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ListCidrLocations)
