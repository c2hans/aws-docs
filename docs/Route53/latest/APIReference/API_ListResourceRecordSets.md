---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListResourceRecordSets.html
---

# ListResourceRecordSets
<a name="API_ListResourceRecordSets"></a>

Lists the resource record sets in a specified hosted zone.

 `ListResourceRecordSets` returns up to 300 resource record sets at a time in ASCII order, beginning at a position specified by the `name` and `type` elements.

 **Sort order**

 `ListResourceRecordSets` sorts results first by DNS name with the labels reversed, for example:

 `com.example.www.`

Note the trailing dot, which can change the sort order when the record name contains characters that appear before `.` (decimal 46) in the ASCII table. These characters include the following: `! " # $ % & ' ( ) * + , -`

When multiple records have the same DNS name, `ListResourceRecordSets` sorts results by the record type.

 **Specifying where to start listing records**

You can use the name and type elements to specify the resource record set that the list begins with:

If you do not specify Name or Type
The results begin with the first resource record set that the hosted zone contains.

If you specify Name but not Type
The results begin with the first resource record set in the list whose name is greater than or equal to `Name`.

If you specify Type but not Name
Amazon Route 53 returns the `InvalidInput` error.

If you specify both Name and Type
The results begin with the first resource record set in the list whose name is greater than or equal to `Name`, and whose type is greater than or equal to `Type`.
Type is only used to sort between records with the same record Name.

 **Resource record sets that are PENDING**

This action returns the most current version of the records. This includes records that are `PENDING`, and that are not yet available on all Route 53 DNS servers.

 **Changing resource record sets**

To ensure that you get an accurate listing of the resource record sets for a hosted zone at a point in time, do not submit a `ChangeResourceRecordSets` request while you're paging through the results of a `ListResourceRecordSets` request. If you do, some pages may display results without the latest changes while other pages display results with the latest changes.

 **Displaying the next page of results**

If a `ListResourceRecordSets` command returns more than one page of results, the value of `IsTruncated` is `true`. To display the next page of results, get the values of `NextRecordName`, `NextRecordType`, and `NextRecordIdentifier` (if any) from the response. Then submit another `ListResourceRecordSets` request, and specify those values for `StartRecordName`, `StartRecordType`, and `StartRecordIdentifier`.

## Request Syntax
<a name="API_ListResourceRecordSets_RequestSyntax"></a>

```
GET /2013-04-01/hostedzone/{{Id}}/rrset?identifier={{StartRecordIdentifier}}&maxitems={{MaxItems}}&name={{StartRecordName}}&type={{StartRecordType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListResourceRecordSets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_ListResourceRecordSets_RequestSyntax) **   <a name="Route53-ListResourceRecordSets-request-uri-HostedZoneId"></a>
The ID of the hosted zone that contains the resource record sets that you want to list.
Length Constraints: Maximum length of 32.
Required: Yes

 ** [identifier](#API_ListResourceRecordSets_RequestSyntax) **   <a name="Route53-ListResourceRecordSets-request-uri-StartRecordIdentifier"></a>
 *Resource record sets that have a routing policy other than simple:* If results were truncated for a given DNS name and type, specify the value of `NextRecordIdentifier` from the previous response to get the next resource record set that has the current DNS name and type.
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [maxitems](#API_ListResourceRecordSets_RequestSyntax) **   <a name="Route53-ListResourceRecordSets-request-uri-MaxItems"></a>
(Optional) The maximum number of resource records sets to include in the response body for this request. If the response includes more than `maxitems` resource record sets, the value of the `IsTruncated` element in the response is `true`, and the values of the `NextRecordName` and `NextRecordType` elements in the response identify the first resource record set in the next group of `maxitems` resource record sets.

 ** [name](#API_ListResourceRecordSets_RequestSyntax) **   <a name="Route53-ListResourceRecordSets-request-uri-StartRecordName"></a>
The first name in the lexicographic ordering of resource record sets that you want to list. If the specified record name doesn't exist, the results begin with the first resource record set that has a name greater than the value of `name`.
Length Constraints: Maximum length of 1024.

 ** [type](#API_ListResourceRecordSets_RequestSyntax) **   <a name="Route53-ListResourceRecordSets-request-uri-StartRecordType"></a>
The type of resource record set to begin the record listing from.
Valid values for basic resource record sets: `A` \| `AAAA` \| `CAA` \| `CNAME` \| `MX` \| `NAPTR` \| `NS` \| `PTR` \| `SOA` \| `SPF` \| `SRV` \| `TXT`
Values for weighted, latency, geolocation, and failover resource record sets: `A` \| `AAAA` \| `CAA` \| `CNAME` \| `MX` \| `NAPTR` \| `PTR` \| `SPF` \| `SRV` \| `TXT`
Values for alias resource record sets:
+  **API Gateway custom regional API or edge-optimized API**: A
+  **CloudFront distribution**: A or AAAA
+  **Elastic Beanstalk environment that has a regionalized subdomain**: A
+  **Elastic Load Balancing load balancer**: A \| AAAA
+  **S3 bucket**: A
+  **VPC interface VPC endpoint**: A
+  **Another resource record set in this hosted zone:** The type of the resource record set that the alias references.
Constraint: Specifying `type` without specifying `name` returns an `InvalidInput` error.
Valid Values: `SOA | A | TXT | NS | CNAME | MX | NAPTR | PTR | SRV | SPF | AAAA | CAA | DS | TLSA | SSHFP | SVCB | HTTPS`

## Request Body
<a name="API_ListResourceRecordSets_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListResourceRecordSets_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListResourceRecordSetsResponse>
   <IsTruncated>boolean</IsTruncated>
   <MaxItems>string</MaxItems>
   <NextRecordIdentifier>string</NextRecordIdentifier>
   <NextRecordName>string</NextRecordName>
   <NextRecordType>string</NextRecordType>
   <ResourceRecordSets>
      <ResourceRecordSet>
         <AliasTarget>
            <DNSName>string</DNSName>
            <EvaluateTargetHealth>boolean</EvaluateTargetHealth>
            <HostedZoneId>string</HostedZoneId>
         </AliasTarget>
         <CidrRoutingConfig>
            <CollectionId>string</CollectionId>
            <LocationName>string</LocationName>
         </CidrRoutingConfig>
         <Failover>string</Failover>
         <GeoLocation>
            <ContinentCode>string</ContinentCode>
            <CountryCode>string</CountryCode>
            <SubdivisionCode>string</SubdivisionCode>
         </GeoLocation>
         <GeoProximityLocation>
            <AWSRegion>string</AWSRegion>
            <Bias>integer</Bias>
            <Coordinates>
               <Latitude>string</Latitude>
               <Longitude>string</Longitude>
            </Coordinates>
            <LocalZoneGroup>string</LocalZoneGroup>
         </GeoProximityLocation>
         <HealthCheckId>string</HealthCheckId>
         <MultiValueAnswer>boolean</MultiValueAnswer>
         <Name>string</Name>
         <Region>string</Region>
         <ResourceRecords>
            <ResourceRecord>
               <Value>string</Value>
            </ResourceRecord>
         </ResourceRecords>
         <SetIdentifier>string</SetIdentifier>
         <TrafficPolicyInstanceId>string</TrafficPolicyInstanceId>
         <TTL>long</TTL>
         <Type>string</Type>
         <Weight>long</Weight>
      </ResourceRecordSet>
   </ResourceRecordSets>
</ListResourceRecordSetsResponse>
```

## Response Elements
<a name="API_ListResourceRecordSets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListResourceRecordSetsResponse](#API_ListResourceRecordSets_ResponseSyntax) **   <a name="Route53-ListResourceRecordSets-response-ListResourceRecordSetsResponse"></a>
Root level tag for the ListResourceRecordSetsResponse parameters.
Required: Yes

 ** [IsTruncated](#API_ListResourceRecordSets_ResponseSyntax) **   <a name="Route53-ListResourceRecordSets-response-IsTruncated"></a>
A flag that indicates whether more resource record sets remain to be listed. If your results were truncated, you can make a follow-up pagination request by using the `NextRecordName` element.
Type: Boolean

 ** [MaxItems](#API_ListResourceRecordSets_ResponseSyntax) **   <a name="Route53-ListResourceRecordSets-response-MaxItems"></a>
The maximum number of records you requested.
Type: String

 ** [NextRecordIdentifier](#API_ListResourceRecordSets_ResponseSyntax) **   <a name="Route53-ListResourceRecordSets-response-NextRecordIdentifier"></a>
 *Resource record sets that have a routing policy other than simple:* If results were truncated for a given DNS name and type, the value of `SetIdentifier` for the next resource record set that has the current DNS name and type.
For information about routing policies, see [Choosing a Routing Policy](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html) in the *Amazon Route 53 Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [NextRecordName](#API_ListResourceRecordSets_ResponseSyntax) **   <a name="Route53-ListResourceRecordSets-response-NextRecordName"></a>
If the results were truncated, the name of the next record in the list.
This element is present only if `IsTruncated` is true.
Type: String
Length Constraints: Maximum length of 1024.

 ** [NextRecordType](#API_ListResourceRecordSets_ResponseSyntax) **   <a name="Route53-ListResourceRecordSets-response-NextRecordType"></a>
If the results were truncated, the type of the next record in the list.
This element is present only if `IsTruncated` is true.
Type: String
Valid Values: `SOA | A | TXT | NS | CNAME | MX | NAPTR | PTR | SRV | SPF | AAAA | CAA | DS | TLSA | SSHFP | SVCB | HTTPS`

 ** [ResourceRecordSets](#API_ListResourceRecordSets_ResponseSyntax) **   <a name="Route53-ListResourceRecordSets-response-ResourceRecordSets"></a>
Information about multiple resource record sets.
Type: Array of [ResourceRecordSet](API_ResourceRecordSet.md) objects

## Errors
<a name="API_ListResourceRecordSets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchHostedZone **
No hosted zone exists with the ID that you specified.
 ** message **

HTTP Status Code: 404

## Examples
<a name="API_ListResourceRecordSets_Examples"></a>

### Example Request
<a name="API_ListResourceRecordSets_Example_1"></a>

This example illustrates one usage of ListResourceRecordSets.

```
GET /2013-04-01/hostedzone/Z1PA6795UKMFR9/rrset?maxitems=1
```

### Example Response
<a name="API_ListResourceRecordSets_Example_2"></a>

This example illustrates one usage of ListResourceRecordSets.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<ListResourceRecordSetsResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <ResourceRecordSets>
      <ResourceRecordSet>
         <Name>example.com.</Name>
         <Type>SOA</Type>
         <TTL>900</TTL>
         <ResourceRecords>
            <ResourceRecord>
               <Value>ns-2048.awsdns-64.net. hostmaster.awsdns.com. 1 7200 900 1209600 86400</Value>
            </ResourceRecord>
         </ResourceRecords>
      </ResourceRecordSet>
   </ResourceRecordSets>
   <IsTruncated>true</IsTruncated>
   <MaxItems>1</MaxItems>
   <NextRecordName>example.com.</NextRecordName>
   <NextRecordType>NS</NextRecordType>
</ListResourceRecordSetsResponse>
```

## See Also
<a name="API_ListResourceRecordSets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/ListResourceRecordSets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/ListResourceRecordSets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ListResourceRecordSets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/ListResourceRecordSets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ListResourceRecordSets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/ListResourceRecordSets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/ListResourceRecordSets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/ListResourceRecordSets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/ListResourceRecordSets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ListResourceRecordSets)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
