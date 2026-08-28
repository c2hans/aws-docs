---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DistributionTenant.html
---

# DistributionTenant
<a name="API_DistributionTenant"></a>

The distribution tenant.

## Contents
<a name="API_DistributionTenant_Contents"></a>

 ** Arn **   <a name="cloudfront-Type-DistributionTenant-Arn"></a>
The Amazon Resource Name (ARN) of the distribution tenant.
Type: String
Required: No

 ** ConnectionGroupId **   <a name="cloudfront-Type-DistributionTenant-ConnectionGroupId"></a>
The ID of the connection group for the distribution tenant. If you don't specify a connection group, CloudFront uses the default connection group.
Type: String
Required: No

 ** CreatedTime **   <a name="cloudfront-Type-DistributionTenant-CreatedTime"></a>
The date and time when the distribution tenant was created.
Type: Timestamp
Required: No

 ** Customizations **   <a name="cloudfront-Type-DistributionTenant-Customizations"></a>
Customizations for the distribution tenant. For each distribution tenant, you can specify the geographic restrictions, and the Amazon Resource Names (ARNs) for the ACM certificate and AWS WAF web ACL. These are specific values that you can override or disable from the multi-tenant distribution that was used to create the distribution tenant.
Type: [Customizations](API_Customizations.md) object
Required: No

 ** DistributionId **   <a name="cloudfront-Type-DistributionTenant-DistributionId"></a>
The ID of the multi-tenant distribution.
Type: String
Required: No

 ** Domains **   <a name="cloudfront-Type-DistributionTenant-Domains"></a>
The domains associated with the distribution tenant.
Type: Array of [DomainResult](API_DomainResult.md) objects
Required: No

 ** Enabled **   <a name="cloudfront-Type-DistributionTenant-Enabled"></a>
Indicates whether the distribution tenant is in an enabled state. If disabled, the distribution tenant won't serve traffic.
Type: Boolean
Required: No

 ** Id **   <a name="cloudfront-Type-DistributionTenant-Id"></a>
The ID of the distribution tenant.
Type: String
Required: No

 ** LastModifiedTime **   <a name="cloudfront-Type-DistributionTenant-LastModifiedTime"></a>
The date and time when the distribution tenant was updated.
Type: Timestamp
Required: No

 ** Name **   <a name="cloudfront-Type-DistributionTenant-Name"></a>
The name of the distribution tenant.
Type: String
Required: No

 ** Parameters **   <a name="cloudfront-Type-DistributionTenant-Parameters"></a>
A list of parameter values to add to the resource. A parameter is specified as a key-value pair. A valid parameter value must exist for any parameter that is marked as required in the multi-tenant distribution.
Type: Array of [Parameter](API_Parameter.md) objects
Required: No

 ** Status **   <a name="cloudfront-Type-DistributionTenant-Status"></a>
The status of the distribution tenant.
Type: String
Required: No

 ** Tags **   <a name="cloudfront-Type-DistributionTenant-Tags"></a>
A complex type that contains zero or more `Tag` elements.
Type: [Tags](API_Tags.md) object
Required: No

## See Also
<a name="API_DistributionTenant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DistributionTenant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DistributionTenant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DistributionTenant)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
