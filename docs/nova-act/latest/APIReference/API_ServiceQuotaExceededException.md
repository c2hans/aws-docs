---
source_url: https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ServiceQuotaExceededException.html
---

# ServiceQuotaExceededException
<a name="API_ServiceQuotaExceededException"></a>

The request would exceed a service quota limit.

HTTP Status Code returned: 402

## Contents
<a name="API_ServiceQuotaExceededException_Contents"></a>

 ** message **   <a name="novaact-Type-ServiceQuotaExceededException-message"></a>
The request would exceed one or more service quotas for your account.
Type: String
Pattern: `[\s\S]+`
Required: Yes

 ** quotaCode **   <a name="novaact-Type-ServiceQuotaExceededException-quotaCode"></a>
The code for the specific quota that was exceeded.
Type: String
Pattern: `[\s\S]+`
Required: Yes

 ** resourceId **   <a name="novaact-Type-ServiceQuotaExceededException-resourceId"></a>
The identifier of the resource that exceeded the quota.
Type: String
Pattern: `[\s\S]+`
Required: Yes

 ** resourceType **   <a name="novaact-Type-ServiceQuotaExceededException-resourceType"></a>
The type of resource that exceeded the quota.
Type: String
Pattern: `[\s\S]+`
Required: Yes

 ** serviceCode **   <a name="novaact-Type-ServiceQuotaExceededException-serviceCode"></a>
The service code for the quota that was exceeded.
Type: String
Pattern: `[\s\S]+`
Required: Yes

## See Also
<a name="API_ServiceQuotaExceededException_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/nova-act-2025-08-22/ServiceQuotaExceededException)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova Act. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova-act` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
