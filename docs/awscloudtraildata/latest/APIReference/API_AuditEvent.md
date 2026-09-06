---
source_url: https://docs.aws.amazon.com/awscloudtraildata/latest/APIReference/API_AuditEvent.html
---

# AuditEvent
<a name="API_AuditEvent"></a>

An event from a source outside of AWS that you want CloudTrail to log.

## Contents
<a name="API_AuditEvent_Contents"></a>

 ** eventData **   <a name="awscloudtraildata-Type-AuditEvent-eventData"></a>
The content of an audit event that comes from the event, such as `userIdentity`, `userAgent`, and `eventSource`.
Type: String
Required: Yes

 ** id **   <a name="awscloudtraildata-Type-AuditEvent-id"></a>
The original event ID from the source event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_A-Za-z0-9]+`
Required: Yes

 ** eventDataChecksum **   <a name="awscloudtraildata-Type-AuditEvent-eventDataChecksum"></a>
A checksum is a base64-SHA256 algorithm that helps you verify that CloudTrail receives the event that matches with the checksum. Calculate the checksum by running a command like the following:
 `printf %s $eventdata | openssl dgst -binary -sha256 | base64`
Type: String
Required: No

## See Also
<a name="API_AuditEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-data-2021-08-11/AuditEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-data-2021-08-11/AuditEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-data-2021-08-11/AuditEvent)
