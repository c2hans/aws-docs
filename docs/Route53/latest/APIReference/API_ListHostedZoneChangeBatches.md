---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListHostedZoneChangeBatches.html
---

# ListHostedZoneChangeBatches

Lists the change batches in an Amazon Route 53 hosted zone. For each change batch, the response contains its change ID, the operation that submitted it, and when and by whom it was submitted. It also contains the request ID, the comment if there is one, and the number of changes. Use this list to review who changed the hosted zone and when.

Each change batch records one `ChangeResourceRecordSets` or `CreateHostedZone` request. A `CreateHostedZone` change batch has a `ChangeCount` of 0.

You can read a change batch for 365 days after it was submitted, but not from before the `RetentionStartsAt` time that `GetHostedZone` returns in `Features/ChangeHistory`. If Change History isn't turned on for the hosted zone, Route 53 returns a `FeatureNotEnabled` error.

Results are paginated. To get the next page, use the `NextToken` value from the response. To get the changes in a change batch, use `GetHostedZoneChangeBatch`.

## Request Syntax
<a name="API_ListHostedZoneChangeBatches_RequestSyntax"></a>

```
GET /2013-04-01/hostedzone/{{Id}}/changebatches?maxresults={{MaxResults}}&nexttoken={{NextToken}}&sortorder={{SortOrder}}&startafterchangeid={{StartAfterChangeId}}&submittedafter={{SubmittedAfter}}&submittedbefore={{SubmittedBefore}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListHostedZoneChangeBatches_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_ListHostedZoneChangeBatches_RequestSyntax) **   <a name="Route53-ListHostedZoneChangeBatches-request-uri-HostedZoneId"></a>
The ID of the hosted zone that you want to list change batches for.
Length Constraints: Maximum length of 32.
Required: Yes

 ** [maxresults](#API_ListHostedZoneChangeBatches_RequestSyntax) **   <a name="Route53-ListHostedZoneChangeBatches-request-uri-MaxResults"></a>
The maximum number of change batches that you want Route 53 to return in this response. Specify a value from 1 to 1,000. If you don't specify a value, Route 53 returns up to 100 change batches.

 ** [nexttoken](#API_ListHostedZoneChangeBatches_RequestSyntax) **   <a name="Route53-ListHostedZoneChangeBatches-request-uri-NextToken"></a>
If the response to a previous `ListHostedZoneChangeBatches` request included a `NextToken` element, specify that value here to get the next page of results. If the previous request included any of the following parameters, include them with exactly the same values: `SubmittedAfter`, `SubmittedBefore`, `SortOrder`, and `StartAfterChangeId`. If you don't, Route 53 returns an `InvalidInput` error. If you don't specify `NextToken`, Route 53 returns the first page of results.
A `NextToken` expires 24 hours after Route 53 returns it, and you can use it only with the hosted zone that it was returned for.
Length Constraints: Maximum length of 1024.

 ** [sortorder](#API_ListHostedZoneChangeBatches_RequestSyntax) **   <a name="Route53-ListHostedZoneChangeBatches-request-uri-SortOrder"></a>
The order in which you want Route 53 to return change batches. Valid values:
+  `DESCENDING` – Newest first. This is the default.
+  `ASCENDING` – Oldest first.
Valid Values: `ASCENDING | DESCENDING`

 ** [startafterchangeid](#API_ListHostedZoneChangeBatches_RequestSyntax) **   <a name="Route53-ListHostedZoneChangeBatches-request-uri-StartAfterChangeId"></a>
Returns the change batches after the specified change batch, not including it. Use this to read new change batches since the last change batch that you processed.
If you specify `StartAfterChangeId`, you must also specify `SortOrder` `ASCENDING`, and you can't specify `SubmittedAfter` or `SubmittedBefore`. If the change batch has expired, is from before `RetentionStartsAt`, or isn't in the hosted zone, Route 53 returns an `InvalidInput` error.
Length Constraints: Maximum length of 32.

 ** [submittedafter](#API_ListHostedZoneChangeBatches_RequestSyntax) **   <a name="Route53-ListHostedZoneChangeBatches-request-uri-SubmittedAfter"></a>
The start of the time range, in ISO 8601 format with a UTC offset, for example `2026-12-01T00:00:00Z` or `2026-12-01T05:30:00.123+05:30`. You can specify up to nine fractional digits. Route 53 rounds a value with more than millisecond precision up to the next millisecond. The range includes `SubmittedAfter`.
If you don't specify a value, the range starts at `RetentionStartsAt`. If you specify a value that's earlier than `RetentionStartsAt`, Route 53 returns an `InvalidInput` error that includes the earliest time that you can specify.
Because submit times can be slightly out of order, a returned `SubmittedAt` can fall just outside the range that you requested.
Length Constraints: Maximum length of 35.
Pattern: `^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]{1,9})?(Z|[+-]([01][0-9]|2[0-3]):[0-5][0-9])$`

 ** [submittedbefore](#API_ListHostedZoneChangeBatches_RequestSyntax) **   <a name="Route53-ListHostedZoneChangeBatches-request-uri-SubmittedBefore"></a>
The end of the time range, in ISO 8601 format with a UTC offset, for example `2026-12-02T00:00:00Z` or `2026-12-02T05:30:00.123+05:30`. You can specify up to nine fractional digits. Route 53 rounds a value with more than millisecond precision up to the next millisecond. The range excludes `SubmittedBefore`. The value must be at least one millisecond later than `SubmittedAfter`, or later than `RetentionStartsAt` if you omit `SubmittedAfter`.
If the range ends within a few seconds of the current time, a later request for the same range might return more change batches.
Length Constraints: Maximum length of 35.
Pattern: `^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]{1,9})?(Z|[+-]([01][0-9]|2[0-3]):[0-5][0-9])$`

## Request Body
<a name="API_ListHostedZoneChangeBatches_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListHostedZoneChangeBatches_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListHostedZoneChangeBatchesResponse>
   <ChangeBatchSummaries>
      <ChangeBatchSummary>
         <ChangeCount>long</ChangeCount>
         <ChangeId>string</ChangeId>
         <Comment>string</Comment>
         <Operation>string</Operation>
         <RequestId>string</RequestId>
         <SubmittedAt>timestamp</SubmittedAt>
         <SubmittedBy>string</SubmittedBy>
      </ChangeBatchSummary>
   </ChangeBatchSummaries>
   <NextToken>string</NextToken>
</ListHostedZoneChangeBatchesResponse>
```

## Response Elements
<a name="API_ListHostedZoneChangeBatches_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListHostedZoneChangeBatchesResponse](#API_ListHostedZoneChangeBatches_ResponseSyntax) **   <a name="Route53-ListHostedZoneChangeBatches-response-ListHostedZoneChangeBatchesResponse"></a>
Root level tag for the ListHostedZoneChangeBatchesResponse parameters.
Required: Yes

 ** [ChangeBatchSummaries](#API_ListHostedZoneChangeBatches_ResponseSyntax) **   <a name="Route53-ListHostedZoneChangeBatches-response-ChangeBatchSummaries"></a>
A summary of each change batch on this page of results. The list is empty if there are no change batches in the range that you specified.
Type: Array of [ChangeBatchSummary](API_ChangeBatchSummary.md) objects

 ** [NextToken](#API_ListHostedZoneChangeBatches_ResponseSyntax) **   <a name="Route53-ListHostedZoneChangeBatches-response-NextToken"></a>
If there might be more change batches to list, a token that you can specify in the `NextToken` parameter of another request to get the next page of results. If there are no more change batches to list, the response doesn't include `NextToken`.
Type: String
Length Constraints: Maximum length of 1024.

## Errors
<a name="API_ListHostedZoneChangeBatches_Errors"></a>

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
<a name="API_ListHostedZoneChangeBatches_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/ListHostedZoneChangeBatches)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/ListHostedZoneChangeBatches)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ListHostedZoneChangeBatches)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/ListHostedZoneChangeBatches)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ListHostedZoneChangeBatches)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/ListHostedZoneChangeBatches)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/ListHostedZoneChangeBatches)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/ListHostedZoneChangeBatches)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/ListHostedZoneChangeBatches)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ListHostedZoneChangeBatches)
