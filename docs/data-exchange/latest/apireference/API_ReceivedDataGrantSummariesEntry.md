---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ReceivedDataGrantSummariesEntry.html
---

# ReceivedDataGrantSummariesEntry
<a name="API_ReceivedDataGrantSummariesEntry"></a>

Information about a received data grant.

## Contents
<a name="API_ReceivedDataGrantSummariesEntry_Contents"></a>

 ** AcceptanceState **   <a name="dataexchange-Type-ReceivedDataGrantSummariesEntry-AcceptanceState"></a>
The acceptance state of the data grant.
Type: String
Valid Values: `PENDING_RECEIVER_ACCEPTANCE | ACCEPTED`
Required: Yes

 ** Arn **   <a name="dataexchange-Type-ReceivedDataGrantSummariesEntry-Arn"></a>
The Amazon Resource Name (ARN) of the data grant.
Type: String
Required: Yes

 ** CreatedAt **   <a name="dataexchange-Type-ReceivedDataGrantSummariesEntry-CreatedAt"></a>
The timestamp of when the data grant was created.
Type: Timestamp
Required: Yes

 ** DataSetId **   <a name="dataexchange-Type-ReceivedDataGrantSummariesEntry-DataSetId"></a>
The ID of the data set associated to the data grant.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** Id **   <a name="dataexchange-Type-ReceivedDataGrantSummariesEntry-Id"></a>
The ID of the data grant.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** Name **   <a name="dataexchange-Type-ReceivedDataGrantSummariesEntry-Name"></a>
The name of the data grant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** ReceiverPrincipal **   <a name="dataexchange-Type-ReceivedDataGrantSummariesEntry-ReceiverPrincipal"></a>
The AWS account ID of the data grant receiver.
Type: String
Pattern: `\d{12}`
Required: Yes

 ** SenderPrincipal **   <a name="dataexchange-Type-ReceivedDataGrantSummariesEntry-SenderPrincipal"></a>
The AWS account ID of the data grant sender.
Type: String
Pattern: `\d{12}`
Required: Yes

 ** UpdatedAt **   <a name="dataexchange-Type-ReceivedDataGrantSummariesEntry-UpdatedAt"></a>
The timestamp of when the data grant was last updated.
Type: Timestamp
Required: Yes

 ** AcceptedAt **   <a name="dataexchange-Type-ReceivedDataGrantSummariesEntry-AcceptedAt"></a>
The timestamp of when the data grant was accepted.
Type: Timestamp
Required: No

 ** EndsAt **   <a name="dataexchange-Type-ReceivedDataGrantSummariesEntry-EndsAt"></a>
The timestamp of when access to the associated data set ends.
Type: Timestamp
Required: No

## See Also
<a name="API_ReceivedDataGrantSummariesEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/ReceivedDataGrantSummariesEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/ReceivedDataGrantSummariesEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/ReceivedDataGrantSummariesEntry)
