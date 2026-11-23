---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListResourceRecordSetChanges.html
---

# ListResourceRecordSetChanges

Lists the individual changes in the change history of a hosted zone. Each entry is one change, with the full resource record set that the change wrote or deleted. To list only the changes to the resource record sets that have a specific name and type, specify `RecordName` and `RecordType`. Weighted, latency, and other resource record sets that have the same name and type appear as separate entries, each with its `SetIdentifier`.

A change can take a few seconds to appear in `ListResourceRecordSetChanges` after it appears in `ListHostedZoneChangeBatches`. For a complete, ordered list of changes, use `ListHostedZoneChangeBatches`.

Results are paginated. To get the next page, use the `NextToken` value from the response.

If Change History isn't turned on for the hosted zone, Route 53 returns a `FeatureNotEnabled` error.

## Request Syntax
<a name="API_ListResourceRecordSetChanges_RequestSyntax"></a>

```
GET /2013-04-01/hostedzone/{{Id}}/rrsetchanges?maxresults={{MaxResults}}&nexttoken={{NextToken}}&recordname={{RecordName}}&recordtype={{RecordType}}&sortorder={{SortOrder}}&submittedafter={{SubmittedAfter}}&submittedbefore={{SubmittedBefore}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListResourceRecordSetChanges_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_ListResourceRecordSetChanges_RequestSyntax) **   <a name="Route53-ListResourceRecordSetChanges-request-uri-HostedZoneId"></a>
The ID of the hosted zone that you want to list changes for.
Length Constraints: Maximum length of 32.
Required: Yes

 ** [maxresults](#API_ListResourceRecordSetChanges_RequestSyntax) **   <a name="Route53-ListResourceRecordSetChanges-request-uri-MaxResults"></a>
The maximum number of changes that you want Route 53 to return in this response. Specify a value from 1 to 100. If you don't specify a value, Route 53 returns up to 100 changes.

 ** [nexttoken](#API_ListResourceRecordSetChanges_RequestSyntax) **   <a name="Route53-ListResourceRecordSetChanges-request-uri-NextToken"></a>
If the response to a previous `ListResourceRecordSetChanges` request included a `NextToken` element, specify that value here to get the next page of results. If the previous request included any of the following parameters, include them with exactly the same values: `SubmittedAfter`, `SubmittedBefore`, `SortOrder`, `RecordName`, and `RecordType`. If you don't, Route 53 returns an `InvalidInput` error. If you don't specify `NextToken`, Route 53 returns the first page of results.
A `NextToken` expires 24 hours after Route 53 returns it, and you can use it only with the hosted zone that it was returned for.
Length Constraints: Maximum length of 1024.

 ** [recordname](#API_ListResourceRecordSetChanges_RequestSyntax) **   <a name="Route53-ListResourceRecordSetChanges-request-uri-RecordName"></a>
The name of the resource record sets that you want to list changes for, for example, `www.example.com`. The name must be the name of the hosted zone or a subdomain of it. If you specify `RecordName`, you must also specify `RecordType`. If you specify neither, the results include every change in the hosted zone.
Length Constraints: Maximum length of 1024.

 ** [recordtype](#API_ListResourceRecordSetChanges_RequestSyntax) **   <a name="Route53-ListResourceRecordSetChanges-request-uri-RecordType"></a>
The DNS record type of the resource record sets that you want to list changes for. If you specify `RecordType`, you must also specify `RecordName`.
Valid Values: `SOA | A | TXT | NS | CNAME | MX | NAPTR | PTR | SRV | SPF | AAAA | CAA | DS | TLSA | SSHFP | SVCB | HTTPS`

 ** [sortorder](#API_ListResourceRecordSetChanges_RequestSyntax) **   <a name="Route53-ListResourceRecordSetChanges-request-uri-SortOrder"></a>
The order in which you want Route 53 to return changes. Valid values:
+  `DESCENDING` – Newest first. This is the default.
+  `ASCENDING` – Oldest first.
Valid Values: `ASCENDING | DESCENDING`

 ** [submittedafter](#API_ListResourceRecordSetChanges_RequestSyntax) **   <a name="Route53-ListResourceRecordSetChanges-request-uri-SubmittedAfter"></a>
The start of the time range, in ISO 8601 format with a UTC offset, for example `2026-12-01T00:00:00Z` or `2026-12-01T05:30:00.123+05:30`. You can specify up to nine fractional digits. Route 53 rounds a value with more than millisecond precision up to the next millisecond. The range includes `SubmittedAfter`.
If you don't specify a value, the range starts at `RetentionStartsAt`. If you specify a value that's earlier than `RetentionStartsAt`, Route 53 returns an `InvalidInput` error that includes the earliest time that you can specify.
Because submit times can be slightly out of order, a returned `SubmittedAt` can fall just outside the range that you requested.
Length Constraints: Maximum length of 35.
Pattern: `^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]{1,9})?(Z|[+-]([01][0-9]|2[0-3]):[0-5][0-9])$`

 ** [submittedbefore](#API_ListResourceRecordSetChanges_RequestSyntax) **   <a name="Route53-ListResourceRecordSetChanges-request-uri-SubmittedBefore"></a>
The end of the time range, in ISO 8601 format with a UTC offset, for example `2026-12-02T00:00:00Z` or `2026-12-02T05:30:00.123+05:30`. You can specify up to nine fractional digits. Route 53 rounds a value with more than millisecond precision up to the next millisecond. The range excludes `SubmittedBefore`. The value must be at least one millisecond later than `SubmittedAfter`, or later than `RetentionStartsAt` if you omit `SubmittedAfter`.
If the range ends within a few seconds of the current time, a later request for the same range might return more changes.
Length Constraints: Maximum length of 35.
Pattern: `^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]{1,9})?(Z|[+-]([01][0-9]|2[0-3]):[0-5][0-9])$`

## Request Body
<a name="API_ListResourceRecordSetChanges_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListResourceRecordSetChanges_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListResourceRecordSetChangesResponse>
   <NextToken>string</NextToken>
   <ResourceRecordSetChanges>
      <ResourceRecordSetChange>
         <Action>string</Action>
         <ChangeId>string</ChangeId>
         <Operation>string</Operation>
         <RequestId>string</RequestId>
         <ResourceRecordSet>
            <AliasTarget>
               <DNSName>string</DNSName>
               <EvaluateTargetHealth>boolean</EvaluateTargetHealth>
               <HostedZoneId>string</HostedZoneId>
            </AliasTarget>
            <AZAffinity>
               <LocationId>string</LocationId>
               <LocationType>string</LocationType>
            </AZAffinity>
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
         <SubmittedAt>timestamp</SubmittedAt>
         <SubmittedBy>string</SubmittedBy>
      </ResourceRecordSetChange>
   </ResourceRecordSetChanges>
</ListResourceRecordSetChangesResponse>
```

## Response Elements
<a name="API_ListResourceRecordSetChanges_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListResourceRecordSetChangesResponse](#API_ListResourceRecordSetChanges_ResponseSyntax) **   <a name="Route53-ListResourceRecordSetChanges-response-ListResourceRecordSetChangesResponse"></a>
Root level tag for the ListResourceRecordSetChangesResponse parameters.
Required: Yes

 ** [NextToken](#API_ListResourceRecordSetChanges_ResponseSyntax) **   <a name="Route53-ListResourceRecordSetChanges-response-NextToken"></a>
If there might be more changes to list, a token that you can specify in the `NextToken` parameter of another request to get the next page of results. If there are no more changes to list, the response doesn't include `NextToken`.
Type: String
Length Constraints: Maximum length of 1024.

 ** [ResourceRecordSetChanges](#API_ListResourceRecordSetChanges_ResponseSyntax) **   <a name="Route53-ListResourceRecordSetChanges-response-ResourceRecordSetChanges"></a>
The changes on this page of results. The list is empty if there are no changes that match the request.
Type: Array of [ResourceRecordSetChange](API_ResourceRecordSetChange.md) objects

## Errors
<a name="API_ListResourceRecordSetChanges_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** FeatureNotEnabled **
This error occurs when a feature that the operation requires isn't turned on for the hosted zone. For example, the tier of the hosted zone doesn't include Change History. To resolve this error, turn on the feature, or move the hosted zone to a tier that includes it.
 ** message **
A message that explains which feature isn't turned on.
HTTP Status Code: 403

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
<a name="API_ListResourceRecordSetChanges_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/ListResourceRecordSetChanges)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/ListResourceRecordSetChanges)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ListResourceRecordSetChanges)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/ListResourceRecordSetChanges)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ListResourceRecordSetChanges)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/ListResourceRecordSetChanges)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/ListResourceRecordSetChanges)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/ListResourceRecordSetChanges)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/ListResourceRecordSetChanges)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ListResourceRecordSetChanges)
