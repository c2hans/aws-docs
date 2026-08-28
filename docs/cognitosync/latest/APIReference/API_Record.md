---
source_url: https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_Record.html
---

# Record
<a name="API_Record"></a>

The basic data structure of a dataset.

## Contents
<a name="API_Record_Contents"></a>

 ** DeviceLastModifiedDate **   <a name="Cognito-Type-Record-DeviceLastModifiedDate"></a>
The last modified date of the client device.
Type: Timestamp
Required: No

 ** Key **   <a name="Cognito-Type-Record-Key"></a>
The key for the record.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** LastModifiedBy **   <a name="Cognito-Type-Record-LastModifiedBy"></a>
The user/device that made the last change to this record.
Type: String
Required: No

 ** LastModifiedDate **   <a name="Cognito-Type-Record-LastModifiedDate"></a>
The date on which the record was last modified.
Type: Timestamp
Required: No

 ** SyncCount **   <a name="Cognito-Type-Record-SyncCount"></a>
The server sync count for this record.
Type: Long
Required: No

 ** Value **   <a name="Cognito-Type-Record-Value"></a>
The value for the record.
Type: String
Length Constraints: Maximum length of 4194304.
Required: No

## See Also
<a name="API_Record_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-sync-2014-06-30/Record)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-sync-2014-06-30/Record)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-sync-2014-06-30/Record)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito Sync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognitosync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
