---
source_url: https://docs.aws.amazon.com/workspaces-instances/latest/api/API_SupportedInstanceConfiguration.html
---

# SupportedInstanceConfiguration
<a name="API_SupportedInstanceConfiguration"></a>

Represents a single valid configuration combination that an instance type supports, combining tenancy, platform type, and billing mode into one complete configuration specification.

## Contents
<a name="API_SupportedInstanceConfiguration_Contents"></a>

 ** BillingMode **   <a name="workspacesinstances-Type-SupportedInstanceConfiguration-BillingMode"></a>
Specifies the billing mode supported in this configuration combination.
Type: String
Valid Values: `MONTHLY | HOURLY`
Required: No

 ** PlatformType **   <a name="workspacesinstances-Type-SupportedInstanceConfiguration-PlatformType"></a>
Specifies the operating system platform supported in this configuration combination.
Type: String
Valid Values: `Windows | Windows BYOL | Linux/UNIX | Ubuntu Pro Linux | Red Hat Enterprise Linux | Red Hat BYOL Linux | SUSE Linux`
Required: No

 ** Tenancy **   <a name="workspacesinstances-Type-SupportedInstanceConfiguration-Tenancy"></a>
Specifies the tenancy model supported in this configuration combination.
Type: String
Valid Values: `SHARED | DEDICATED`
Required: No

## See Also
<a name="API_SupportedInstanceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-instances-2022-07-26/SupportedInstanceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-instances-2022-07-26/SupportedInstanceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-instances-2022-07-26/SupportedInstanceConfiguration)
