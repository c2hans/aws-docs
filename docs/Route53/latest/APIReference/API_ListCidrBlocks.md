---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListCidrBlocks.html
---

# ListCidrBlocks
<a name="API_ListCidrBlocks"></a>

Returns a paginated list of location objects and their CIDR blocks.

## Request Syntax
<a name="API_ListCidrBlocks_RequestSyntax"></a>

```
GET /2013-04-01/cidrcollection/{{CidrCollectionId}}/cidrblocks?location={{LocationName}}&maxresults={{MaxResults}}&nexttoken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCidrBlocks_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CidrCollectionId](#API_ListCidrBlocks_RequestSyntax) **   <a name="Route53-ListCidrBlocks-request-uri-CollectionId"></a>
The UUID of the CIDR collection.
Pattern: `[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}`
Required: Yes

 ** [location](#API_ListCidrBlocks_RequestSyntax) **   <a name="Route53-ListCidrBlocks-request-uri-LocationName"></a>
The name of the CIDR collection location.
Length Constraints: Minimum length of 1. Maximum length of 16.
Pattern: `[0-9A-Za-z_\-]+`

 ** [maxresults](#API_ListCidrBlocks_RequestSyntax) **   <a name="Route53-ListCidrBlocks-request-uri-MaxResults"></a>
Maximum number of results you want returned.

 ** [nexttoken](#API_ListCidrBlocks_RequestSyntax) **   <a name="Route53-ListCidrBlocks-request-uri-NextToken"></a>
An opaque pagination token to indicate where the service is to begin enumerating results.
Length Constraints: Maximum length of 1024.

## Request Body
<a name="API_ListCidrBlocks_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCidrBlocks_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListCidrBlocksResponse>
   <CidrBlocks>
      <CidrBlockSummary>
         <CidrBlock>string</CidrBlock>
         <LocationName>string</LocationName>
      </CidrBlockSummary>
   </CidrBlocks>
   <NextToken>string</NextToken>
</ListCidrBlocksResponse>
```

## Response Elements
<a name="API_ListCidrBlocks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListCidrBlocksResponse](#API_ListCidrBlocks_ResponseSyntax) **   <a name="Route53-ListCidrBlocks-response-ListCidrBlocksResponse"></a>
Root level tag for the ListCidrBlocksResponse parameters.
Required: Yes

 ** [CidrBlocks](#API_ListCidrBlocks_ResponseSyntax) **   <a name="Route53-ListCidrBlocks-response-CidrBlocks"></a>
A complex type that contains information about the CIDR blocks.
Type: Array of [CidrBlockSummary](API_CidrBlockSummary.md) objects

 ** [NextToken](#API_ListCidrBlocks_ResponseSyntax) **   <a name="Route53-ListCidrBlocks-response-NextToken"></a>
An opaque pagination token to indicate where the service is to begin enumerating results.
If no value is provided, the listing of results starts from the beginning.
Type: String
Length Constraints: Maximum length of 1024.

## Errors
<a name="API_ListCidrBlocks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchCidrCollectionException **
The CIDR collection you specified, doesn't exist.
HTTP Status Code: 404

 ** NoSuchCidrLocationException **
The CIDR collection location doesn't match any locations in your account.
HTTP Status Code: 404

## Examples
<a name="API_ListCidrBlocks_Examples"></a>

### Example request
<a name="API_ListCidrBlocks_Example_1"></a>

This example illustrates one usage of ListCidrBlocks.

```
GET /2013-04-01/cidrcollection/c8c02a84-aaec-7a26-e0d2-d833a2f80106/cidrblocks?location=location-1&maxresults=1
```

### Example response
<a name="API_ListCidrBlocks_Example_2"></a>

This example illustrates one usage of ListCidrBlocks.

```
HTTP/1.1 200
<?xml version="1.0"?>
<ListCidrBlocksResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
  <NextToken>eyJjb2xsZWN0aW9uSWQiOiIwNGJmZjEyZS04NTdjLTFiNmEtNTc2OS0wMTQwMzg4NmE1NzkiLCJsb2NhdGlvbk5hbWUiOiJhMSIsImNpZHIiOiIyLjMuMS4wLzI0In0=</NextToken>
    <CidrBlocks>
      <member>
        <CidrBlock>1.1.1.0/24</CidrBlock>
        <LocationName>location-1</LocationName>
      </member>
   </CidrBlocks>
</ListCidrBlocksResponse>
```

## See Also
<a name="API_ListCidrBlocks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/ListCidrBlocks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/ListCidrBlocks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ListCidrBlocks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/ListCidrBlocks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ListCidrBlocks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/ListCidrBlocks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/ListCidrBlocks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/ListCidrBlocks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/ListCidrBlocks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ListCidrBlocks)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
