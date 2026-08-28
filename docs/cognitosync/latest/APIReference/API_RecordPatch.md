---
source_url: https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_RecordPatch.html
---

# RecordPatch
<a name="API_RecordPatch"></a>

An update operation for a record.

## Contents
<a name="API_RecordPatch_Contents"></a>

 ** Key **   <a name="Cognito-Type-RecordPatch-Key"></a>
The key associated with the record patch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** Op **   <a name="Cognito-Type-RecordPatch-Op"></a>
An operation, either replace or remove.
Type: String
Valid Values: `replace | remove`
Required: Yes

 ** SyncCount **   <a name="Cognito-Type-RecordPatch-SyncCount"></a>
Last known server sync count for this record. Set to 0 if unknown.
Type: Long
Required: Yes

 ** DeviceLastModifiedDate **   <a name="Cognito-Type-RecordPatch-DeviceLastModifiedDate"></a>
The last modified date of the client device.
Type: Timestamp
Required: No

 ** Value **   <a name="Cognito-Type-RecordPatch-Value"></a>
The value associated with the record patch.
Type: String
Length Constraints: Maximum length of 4194304.
Required: No

## See Also
<a name="API_RecordPatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-sync-2014-06-30/RecordPatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-sync-2014-06-30/RecordPatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-sync-2014-06-30/RecordPatch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito Sync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognitosync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
