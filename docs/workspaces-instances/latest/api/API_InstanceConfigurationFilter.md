---
source_url: https://docs.aws.amazon.com/workspaces-instances/latest/api/API_InstanceConfigurationFilter.html
---

# InstanceConfigurationFilter
<a name="API_InstanceConfigurationFilter"></a>

Defines filtering criteria for WorkSpace Instance type searches. Combines multiple filter conditions including billing mode, platform type, and tenancy to help customers find instance types that meet their specific requirements.

## Contents
<a name="API_InstanceConfigurationFilter_Contents"></a>

 ** BillingMode **   <a name="workspacesinstances-Type-InstanceConfigurationFilter-BillingMode"></a>
Filters WorkSpace Instance types based on supported billing modes. Allows customers to search for instance types that support their preferred billing model, such as HOURLY or MONTHLY billing.
Type: String
Valid Values: `MONTHLY | HOURLY`
Required: Yes

 ** PlatformType **   <a name="workspacesinstances-Type-InstanceConfigurationFilter-PlatformType"></a>
Filters WorkSpace Instance types by operating system platform. Allows customers to find instances that support their desired OS, such as Windows, Linux/UNIX, Ubuntu Pro, RHEL, or SUSE.
Type: String
Valid Values: `Windows | Windows BYOL | Linux/UNIX | Ubuntu Pro Linux | Red Hat Enterprise Linux | Red Hat BYOL Linux | SUSE Linux`
Required: Yes

 ** Tenancy **   <a name="workspacesinstances-Type-InstanceConfigurationFilter-Tenancy"></a>
Filters WorkSpace Instance types by tenancy model. Allows customers to find instances that match their tenancy requirements, such as SHARED or DEDICATED.
Type: String
Valid Values: `SHARED | DEDICATED`
Required: Yes

## See Also
<a name="API_InstanceConfigurationFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-instances-2022-07-26/InstanceConfigurationFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-instances-2022-07-26/InstanceConfigurationFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-instances-2022-07-26/InstanceConfigurationFilter)
