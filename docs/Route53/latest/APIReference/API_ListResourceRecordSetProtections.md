---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListResourceRecordSetProtections.html
---

# ListResourceRecordSetProtections
<a name="API_ListResourceRecordSetProtections"></a>

Lists the resource record set protections in a hosted zone. We recommend using pagination to ensure that the operation returns quickly and successfully.

If the response includes a `NextToken` element, there are more protections to list. To get the next page of results, submit another request and specify the value of `NextToken` in the `NextToken` parameter.

## Request Syntax
<a name="API_ListResourceRecordSetProtections_RequestSyntax"></a>

```
GET /2013-04-01/hostedzone/{{Id}}/rrsetprotection?maxresults={{MaxResults}}&name={{StartRecordName}}&nexttoken={{NextToken}}&type={{StartRecordType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListResourceRecordSetProtections_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_ListResourceRecordSetProtections_RequestSyntax) **   <a name="Route53-ListResourceRecordSetProtections-request-uri-HostedZoneId"></a>
The ID of the hosted zone that contains the protections that you want to list.
Length Constraints: Maximum length of 32.
Required: Yes

 ** [maxresults](#API_ListResourceRecordSetProtections_RequestSyntax) **   <a name="Route53-ListResourceRecordSetProtections-request-uri-MaxResults"></a>
The maximum number of protections that you want Route 53 to return in this response. If you don't specify a value, or if you specify a value greater than 300, Route 53 returns up to 300 protections.

 ** [name](#API_ListResourceRecordSetProtections_RequestSyntax) **   <a name="Route53-ListResourceRecordSetProtections-request-uri-StartRecordName"></a>
The first resource record set name that you want Route 53 to list protections for. If you don't specify a value, the list starts with the first protection in the hosted zone.
If you specify `NextToken`, Route 53 ignores `StartRecordName`.
Length Constraints: Maximum length of 1024.

 ** [nexttoken](#API_ListResourceRecordSetProtections_RequestSyntax) **   <a name="Route53-ListResourceRecordSetProtections-request-uri-NextToken"></a>
If the response to a previous `ListResourceRecordSetProtections` request included a `NextToken` element, specify that value here to get the next page of results.
Length Constraints: Maximum length of 1024.

 ** [type](#API_ListResourceRecordSetProtections_RequestSyntax) **   <a name="Route53-ListResourceRecordSetProtections-request-uri-StartRecordType"></a>
The first resource record set type, within the name specified by `StartRecordName`, that you want Route 53 to list protections for. If you specify `StartRecordType`, you must also specify `StartRecordName`.
If you specify `NextToken`, Route 53 ignores `StartRecordType`.
Valid Values: `SOA | A | TXT | NS | CNAME | MX | NAPTR | PTR | SRV | SPF | AAAA | CAA | DS | TLSA | SSHFP | SVCB | HTTPS`

## Request Body
<a name="API_ListResourceRecordSetProtections_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListResourceRecordSetProtections_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListResourceRecordSetProtectionsResponse>
   <NextToken>string</NextToken>
   <ResourceRecordSetProtections>
      <ResourceRecordSetProtection>
         <Comment>string</Comment>
         <RecordName>string</RecordName>
         <RecordType>string</RecordType>
      </ResourceRecordSetProtection>
   </ResourceRecordSetProtections>
</ListResourceRecordSetProtectionsResponse>
```

## Response Elements
<a name="API_ListResourceRecordSetProtections_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListResourceRecordSetProtectionsResponse](#API_ListResourceRecordSetProtections_ResponseSyntax) **   <a name="Route53-ListResourceRecordSetProtections-response-ListResourceRecordSetProtectionsResponse"></a>
Root level tag for the ListResourceRecordSetProtectionsResponse parameters.
Required: Yes

 ** [NextToken](#API_ListResourceRecordSetProtections_ResponseSyntax) **   <a name="Route53-ListResourceRecordSetProtections-response-NextToken"></a>
If there are more protections to list, a token that you can specify in the `NextToken` parameter of another request to get the next page of results. If there are no more protections to list, the response doesn't include `NextToken`.
Type: String
Length Constraints: Maximum length of 1024.

 ** [ResourceRecordSetProtections](#API_ListResourceRecordSetProtections_ResponseSyntax) **   <a name="Route53-ListResourceRecordSetProtections-response-ResourceRecordSetProtections"></a>
The protections in the hosted zone. The list is empty if the hosted zone has no protections.
Type: Array of [ResourceRecordSetProtection](API_ResourceRecordSetProtection.md) objects

## Errors
<a name="API_ListResourceRecordSetProtections_Errors"></a>

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

## See Also
<a name="API_ListResourceRecordSetProtections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/ListResourceRecordSetProtections)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/ListResourceRecordSetProtections)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ListResourceRecordSetProtections)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/ListResourceRecordSetProtections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ListResourceRecordSetProtections)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/ListResourceRecordSetProtections)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/ListResourceRecordSetProtections)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/ListResourceRecordSetProtections)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/ListResourceRecordSetProtections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ListResourceRecordSetProtections)
