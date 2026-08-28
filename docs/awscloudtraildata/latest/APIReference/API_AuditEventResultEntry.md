---
source_url: https://docs.aws.amazon.com/awscloudtraildata/latest/APIReference/API_AuditEventResultEntry.html
---

# AuditEventResultEntry
<a name="API_AuditEventResultEntry"></a>

A response that includes successful and failed event results.

## Contents
<a name="API_AuditEventResultEntry_Contents"></a>

 ** eventID **   <a name="awscloudtraildata-Type-AuditEventResultEntry-eventID"></a>
The event ID assigned by CloudTrail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_A-Za-z0-9]+`
Required: Yes

 ** id **   <a name="awscloudtraildata-Type-AuditEventResultEntry-id"></a>
The original event ID from the source event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_A-Za-z0-9]+`
Required: Yes

## See Also
<a name="API_AuditEventResultEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-data-2021-08-11/AuditEventResultEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-data-2021-08-11/AuditEventResultEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-data-2021-08-11/AuditEventResultEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudTrail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awscloudtraildata` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
