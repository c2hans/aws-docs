---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ResourceTenantMetadata.html
---

# ResourceTenantMetadata
<a name="API_ResourceTenantMetadata"></a>

A structure that contains information about a tenant associated with a resource.

## Contents
<a name="API_ResourceTenantMetadata_Contents"></a>

 ** AssociatedTimestamp **   <a name="SES-Type-ResourceTenantMetadata-AssociatedTimestamp"></a>
The date and time when the resource was associated with the tenant.
Type: Timestamp
Required: No

 ** ResourceArn **   <a name="SES-Type-ResourceTenantMetadata-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** TenantId **   <a name="SES-Type-ResourceTenantMetadata-TenantId"></a>
A unique identifier for the tenant associated with the resource.
Type: String
Required: No

 ** TenantName **   <a name="SES-Type-ResourceTenantMetadata-TenantName"></a>
The name of the tenant associated with the resource.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_ResourceTenantMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ResourceTenantMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ResourceTenantMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ResourceTenantMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
