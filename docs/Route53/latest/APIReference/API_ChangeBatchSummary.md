---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeBatchSummary.html
---

# ChangeBatchSummary

A summary of one change batch in the change history of a hosted zone.

## Contents
<a name="API_ChangeBatchSummary_Contents"></a>

 ** ChangeCount **   <a name="Route53-Type-ChangeBatchSummary-ChangeCount"></a>
The number of changes in the change batch. For `CreateHostedZone`, the value is 0.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** ChangeId **   <a name="Route53-Type-ChangeBatchSummary-ChangeId"></a>
The ID of the change batch. This is the same ID that `ChangeResourceRecordSets` returns in `ChangeInfo/Id` and that you pass to `GetChange`.
Type: String
Length Constraints: Maximum length of 32.
Required: Yes

 ** Operation **   <a name="Route53-Type-ChangeBatchSummary-Operation"></a>
The Route 53 API operation that submitted the change batch: `ChangeResourceRecordSets` or `CreateHostedZone`. New values might be added, so ignore values that your code doesn't recognize.
Type: String
Valid Values: `CreateHostedZone | DeleteHostedZone | ChangeResourceRecordSets`
Required: Yes

 ** SubmittedAt **   <a name="Route53-Type-ChangeBatchSummary-SubmittedAt"></a>
The date and time, in UTC, when the change batch was submitted.
Type: Timestamp
Required: Yes

 ** Comment **   <a name="Route53-Type-ChangeBatchSummary-Comment"></a>
The comment that was submitted with the change batch, if any.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** RequestId **   <a name="Route53-Type-ChangeBatchSummary-RequestId"></a>
The request ID of the call that submitted the change batch. CloudTrail records the same value in `requestID`, so you can use it to find the CloudTrail event for the change. This element is absent when there was no request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** SubmittedBy **   <a name="Route53-Type-ChangeBatchSummary-SubmittedBy"></a>
The Amazon Resource Name of the principal that submitted the request, for example, `arn:aws:sts::111122223333:assumed-role/Admin/my-session`. This element is absent when Route 53 has no principal to record for the change.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_ChangeBatchSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ChangeBatchSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ChangeBatchSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ChangeBatchSummary)
