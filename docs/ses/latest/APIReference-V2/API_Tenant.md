---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_Tenant.html
---

# Tenant
<a name="API_Tenant"></a>

A structure that contains details about a tenant.

## Contents
<a name="API_Tenant_Contents"></a>

 ** CreatedTimestamp **   <a name="SES-Type-Tenant-CreatedTimestamp"></a>
The date and time when the tenant was created.
Type: Timestamp
Required: No

 ** SendingStatus **   <a name="SES-Type-Tenant-SendingStatus"></a>
The status of sending capability for the tenant.
Type: String
Valid Values: `ENABLED | REINSTATED | DISABLED`
Required: No

 ** SuppressionAttributes **   <a name="SES-Type-Tenant-SuppressionAttributes"></a>
An object that contains information about the suppression list preferences for the tenant.
Type: [TenantSuppressionAttributes](API_TenantSuppressionAttributes.md) object
Required: No

 ** Tags **   <a name="SES-Type-Tenant-Tags"></a>
An array of objects that define the tags (keys and values) associated with the tenant.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** TenantArn **   <a name="SES-Type-Tenant-TenantArn"></a>
The Amazon Resource Name (ARN) of the tenant.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** TenantId **   <a name="SES-Type-Tenant-TenantId"></a>
A unique identifier for the tenant.
Type: String
Required: No

 ** TenantName **   <a name="SES-Type-Tenant-TenantName"></a>
The name of the tenant.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_Tenant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/Tenant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/Tenant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/Tenant)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
