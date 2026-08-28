---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_AccountQuota.html
---

# AccountQuota
<a name="API_AccountQuota"></a>

Describes a quota for an AWS account, for example the number of replication instances allowed.

## Contents
<a name="API_AccountQuota_Contents"></a>

 ** AccountQuotaName **   <a name="DMS-Type-AccountQuota-AccountQuotaName"></a>
The name of the AWS DMS quota for this AWS account.
Type: String
Required: No

 ** Max **   <a name="DMS-Type-AccountQuota-Max"></a>
The maximum allowed value for the quota.
Type: Long
Required: No

 ** Used **   <a name="DMS-Type-AccountQuota-Used"></a>
The amount currently used toward the quota maximum.
Type: Long
Required: No

## See Also
<a name="API_AccountQuota_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/AccountQuota)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/AccountQuota)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/AccountQuota)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
