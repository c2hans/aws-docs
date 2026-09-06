---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_TenantResource.html
---

# TenantResource
<a name="API_TenantResource"></a>

A structure that contains information about a resource associated with a tenant.

## Contents
<a name="API_TenantResource_Contents"></a>

 ** ResourceArn **   <a name="SES-Type-TenantResource-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource associated with the tenant.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** ResourceType **   <a name="SES-Type-TenantResource-ResourceType"></a>
The type of resource associated with the tenant. Valid values are `EMAIL_IDENTITY`, `CONFIGURATION_SET`, or `EMAIL_TEMPLATE`.
Type: String
Valid Values: `EMAIL_IDENTITY | CONFIGURATION_SET | EMAIL_TEMPLATE`
Required: No

## See Also
<a name="API_TenantResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/TenantResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/TenantResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/TenantResource)
