---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ResourceRecordSetChange.html
---

# ResourceRecordSetChange

One change to a resource record set in the change history of a hosted zone, with the resource record set that the change wrote or deleted.

## Contents
<a name="API_ResourceRecordSetChange_Contents"></a>

 ** Action **   <a name="Route53-Type-ResourceRecordSetChange-Action"></a>
The action in the change: `CREATE`, `DELETE`, or `UPSERT`.
Type: String
Valid Values: `CREATE | DELETE | UPSERT`
Required: Yes

 ** ChangeId **   <a name="Route53-Type-ResourceRecordSetChange-ChangeId"></a>
The ID of the change batch that contains the change. To get every change in the change batch, specify this ID in `GetHostedZoneChangeBatch`.
Type: String
Length Constraints: Maximum length of 32.
Required: Yes

 ** Operation **   <a name="Route53-Type-ResourceRecordSetChange-Operation"></a>
The Route 53 API operation that submitted the change. New values might be added, so ignore values that your code doesn't recognize.
Type: String
Valid Values: `CreateHostedZone | DeleteHostedZone | ChangeResourceRecordSets`
Required: Yes

 ** ResourceRecordSet **   <a name="Route53-Type-ResourceRecordSetChange-ResourceRecordSet"></a>
The resource record set that the change wrote or deleted, in the same form that `ListResourceRecordSets` returns. For example, the name is in lowercase and ends with a dot. For an `UPSERT` or a `DELETE`, the response doesn't contain the values that the resource record set had before the change.
Type: [ResourceRecordSet](API_ResourceRecordSet.md) object
Required: Yes

 ** SubmittedAt **   <a name="Route53-Type-ResourceRecordSetChange-SubmittedAt"></a>
The date and time, in UTC, when the change batch that contains the change was submitted.
Type: Timestamp
Required: Yes

 ** RequestId **   <a name="Route53-Type-ResourceRecordSetChange-RequestId"></a>
The request ID of the call that submitted the change. CloudTrail records the same value in `requestID`. This element is absent when there was no request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** SubmittedBy **   <a name="Route53-Type-ResourceRecordSetChange-SubmittedBy"></a>
The Amazon Resource Name of the principal that submitted the request. This element is absent when Route 53 has no principal to record for the change.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_ResourceRecordSetChange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ResourceRecordSetChange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ResourceRecordSetChange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ResourceRecordSetChange)
