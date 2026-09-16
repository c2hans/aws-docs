---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListVPCAssociationAuthorizations.html
---

# ListVPCAssociationAuthorizations
<a name="API_ListVPCAssociationAuthorizations"></a>

Gets a list of the VPCs that were created by other accounts and that can be associated with a specified hosted zone because you've submitted one or more `CreateVPCAssociationAuthorization` requests.

The response includes a `VPCs` element with a `VPC` child element for each VPC that can be associated with the hosted zone.

## Request Syntax
<a name="API_ListVPCAssociationAuthorizations_RequestSyntax"></a>

```
GET /2013-04-01/hostedzone/{{Id}}/authorizevpcassociation?maxresults={{MaxResults}}&nexttoken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListVPCAssociationAuthorizations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_ListVPCAssociationAuthorizations_RequestSyntax) **   <a name="Route53-ListVPCAssociationAuthorizations-request-uri-HostedZoneId"></a>
The ID of the hosted zone for which you want a list of VPCs that can be associated with the hosted zone.
Length Constraints: Maximum length of 32.
Required: Yes

 ** [maxresults](#API_ListVPCAssociationAuthorizations_RequestSyntax) **   <a name="Route53-ListVPCAssociationAuthorizations-request-uri-MaxResults"></a>
 *Optional*: An integer that specifies the maximum number of VPCs that you want Amazon Route 53 to return. If you don't specify a value for `MaxResults`, Route 53 returns up to 50 VPCs per page.

 ** [nexttoken](#API_ListVPCAssociationAuthorizations_RequestSyntax) **   <a name="Route53-ListVPCAssociationAuthorizations-request-uri-NextToken"></a>
 *Optional*: If a response includes a `NextToken` element, there are more VPCs that can be associated with the specified hosted zone. To get the next page of results, submit another request, and include the value of `NextToken` from the response in the `nexttoken` parameter in another `ListVPCAssociationAuthorizations` request.
Length Constraints: Maximum length of 1024.

## Request Body
<a name="API_ListVPCAssociationAuthorizations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListVPCAssociationAuthorizations_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListVPCAssociationAuthorizationsResponse>
   <HostedZoneId>string</HostedZoneId>
   <NextToken>string</NextToken>
   <VPCs>
      <VPC>
         <VPCId>string</VPCId>
         <VPCRegion>string</VPCRegion>
      </VPC>
   </VPCs>
</ListVPCAssociationAuthorizationsResponse>
```

## Response Elements
<a name="API_ListVPCAssociationAuthorizations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListVPCAssociationAuthorizationsResponse](#API_ListVPCAssociationAuthorizations_ResponseSyntax) **   <a name="Route53-ListVPCAssociationAuthorizations-response-ListVPCAssociationAuthorizationsResponse"></a>
Root level tag for the ListVPCAssociationAuthorizationsResponse parameters.
Required: Yes

 ** [HostedZoneId](#API_ListVPCAssociationAuthorizations_ResponseSyntax) **   <a name="Route53-ListVPCAssociationAuthorizations-response-HostedZoneId"></a>
The ID of the hosted zone that you can associate the listed VPCs with.
Type: String
Length Constraints: Maximum length of 32.

 ** [NextToken](#API_ListVPCAssociationAuthorizations_ResponseSyntax) **   <a name="Route53-ListVPCAssociationAuthorizations-response-NextToken"></a>
When the response includes a `NextToken` element, there are more VPCs that can be associated with the specified hosted zone. To get the next page of VPCs, submit another `ListVPCAssociationAuthorizations` request, and include the value of the `NextToken` element from the response in the `nexttoken` request parameter.
Type: String
Length Constraints: Maximum length of 1024.

 ** [VPCs](#API_ListVPCAssociationAuthorizations_ResponseSyntax) **   <a name="Route53-ListVPCAssociationAuthorizations-response-VPCs"></a>
The list of VPCs that are authorized to be associated with the specified hosted zone.
Type: Array of [VPC](API_VPC.md) objects
Array Members: Minimum number of 1 item.

## Errors
<a name="API_ListVPCAssociationAuthorizations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** InvalidPaginationToken **
The value that you specified to get the second or subsequent page of results is invalid.
HTTP Status Code: 400

 ** NoSuchHostedZone **
No hosted zone exists with the ID that you specified.
 ** message **

HTTP Status Code: 404

## Examples
<a name="API_ListVPCAssociationAuthorizations_Examples"></a>

### Example Request
<a name="API_ListVPCAssociationAuthorizations_Example_1"></a>

This example illustrates one usage of ListVPCAssociationAuthorizations.

```
GET /2013-04-01/hostedzone/Z1PA6795UKMFR9/authorizevpcassociation&maxresults=1 HTTP/1.1
```

### Example Response
<a name="API_ListVPCAssociationAuthorizations_Example_2"></a>

This example illustrates one usage of ListVPCAssociationAuthorizations.

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListVPCAssociationAuthorizationsResponse>
   <HostedZoneId>Z1PA6795UKMFR9</HostedZoneId>
   <NextToken>Z222222VVVVVVV</NextToken>
   <VPCs>
      <VPC>
         <VPCId>vpc-a1b2c3d4e5</VPCId>
         <VPCRegion>us-east-2</VPCRegion>
      </VPC>
   </VPCs>
</ListVPCAssociationAuthorizationsResponse>
```

## See Also
<a name="API_ListVPCAssociationAuthorizations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/ListVPCAssociationAuthorizations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/ListVPCAssociationAuthorizations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ListVPCAssociationAuthorizations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/ListVPCAssociationAuthorizations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ListVPCAssociationAuthorizations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/ListVPCAssociationAuthorizations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/ListVPCAssociationAuthorizations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/ListVPCAssociationAuthorizations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/ListVPCAssociationAuthorizations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ListVPCAssociationAuthorizations)
