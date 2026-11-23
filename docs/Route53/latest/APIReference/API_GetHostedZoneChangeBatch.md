---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHostedZoneChangeBatch.html
---

# GetHostedZoneChangeBatch

Returns one change batch from the change history of a hosted zone, including every change in the batch. Each resource record set is in the same form that `ListResourceRecordSets` returns. For example, the name is in lowercase and ends with a dot. For an `UPSERT` or a `DELETE`, the response doesn't contain the values that the resource record set had before the change.

If the change batch isn't in the hosted zone's retained change history, for example because it's in another hosted zone, it expired, or it's from before `RetentionStartsAt`, Route 53 returns a `NoSuchChange` error. If Change History isn't turned on for the hosted zone, Route 53 returns a `FeatureNotEnabled` error.

## Request Syntax
<a name="API_GetHostedZoneChangeBatch_RequestSyntax"></a>

```
GET /2013-04-01/hostedzone/{{Id}}/changebatches/{{ChangeId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetHostedZoneChangeBatch_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChangeId](#API_GetHostedZoneChangeBatch_RequestSyntax) **   <a name="Route53-GetHostedZoneChangeBatch-request-uri-ChangeId"></a>
The ID of the change batch that you want to get. This is the ID that `ChangeResourceRecordSets` returns in `ChangeInfo/Id`. You can specify the ID with or without the `/change/` prefix.
Length Constraints: Maximum length of 32.
Required: Yes

 ** [Id](#API_GetHostedZoneChangeBatch_RequestSyntax) **   <a name="Route53-GetHostedZoneChangeBatch-request-uri-HostedZoneId"></a>
The ID of the hosted zone that contains the change batch.
Length Constraints: Maximum length of 32.
Required: Yes

## Request Body
<a name="API_GetHostedZoneChangeBatch_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetHostedZoneChangeBatch_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetHostedZoneChangeBatchResponse>
   <ChangeBatch>
      <Changes>
         <Change>
            <Action>string</Action>
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
         </Change>
      </Changes>
      <Comment>string</Comment>
   </ChangeBatch>
   <ChangeBatchSummary>
      <ChangeCount>long</ChangeCount>
      <ChangeId>string</ChangeId>
      <Comment>string</Comment>
      <Operation>string</Operation>
      <RequestId>string</RequestId>
      <SubmittedAt>timestamp</SubmittedAt>
      <SubmittedBy>string</SubmittedBy>
   </ChangeBatchSummary>
</GetHostedZoneChangeBatchResponse>
```

## Response Elements
<a name="API_GetHostedZoneChangeBatch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetHostedZoneChangeBatchResponse](#API_GetHostedZoneChangeBatch_ResponseSyntax) **   <a name="Route53-GetHostedZoneChangeBatch-response-GetHostedZoneChangeBatchResponse"></a>
Root level tag for the GetHostedZoneChangeBatchResponse parameters.
Required: Yes

 ** [ChangeBatch](#API_GetHostedZoneChangeBatch_ResponseSyntax) **   <a name="Route53-GetHostedZoneChangeBatch-response-ChangeBatch"></a>
The changes in the change batch. Each resource record set is in the same form that `ListResourceRecordSets` returns. For example, the name is in lowercase and ends with a dot.
Type: [ChangeBatch](API_ChangeBatch.md) object

 ** [ChangeBatchSummary](#API_GetHostedZoneChangeBatch_ResponseSyntax) **   <a name="Route53-GetHostedZoneChangeBatch-response-ChangeBatchSummary"></a>
A summary of the change batch, including who submitted it and when.
Type: [ChangeBatchSummary](API_ChangeBatchSummary.md) object

## Errors
<a name="API_GetHostedZoneChangeBatch_Errors"></a>

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

 ** NoSuchChange **
A change with the specified change ID does not exist.
HTTP Status Code: 404

 ** NoSuchHostedZone **
No hosted zone exists with the ID that you specified.
 ** message **

HTTP Status Code: 404

## See Also
<a name="API_GetHostedZoneChangeBatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/GetHostedZoneChangeBatch)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/GetHostedZoneChangeBatch)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/GetHostedZoneChangeBatch)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/GetHostedZoneChangeBatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/GetHostedZoneChangeBatch)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/GetHostedZoneChangeBatch)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/GetHostedZoneChangeBatch)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/GetHostedZoneChangeBatch)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/GetHostedZoneChangeBatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/GetHostedZoneChangeBatch)
