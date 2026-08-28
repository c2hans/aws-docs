---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_Bundle.html
---

# Bundle
<a name="API_Bundle"></a>

Describes a bundle, which is a set of specs describing your virtual private server (or *instance*).

## Contents
<a name="API_Bundle_Contents"></a>

 ** bundleId **   <a name="Lightsail-Type-Bundle-bundleId"></a>
The bundle ID (`micro_x_x`).
Type: String
Pattern: `.*\S.*`
Required: No

 ** cpuCount **   <a name="Lightsail-Type-Bundle-cpuCount"></a>
The number of vCPUs included in the bundle (`2`).
Type: Integer
Required: No

 ** diskSizeInGb **   <a name="Lightsail-Type-Bundle-diskSizeInGb"></a>
The size of the SSD (`30`).
Type: Integer
Required: No

 ** instanceType **   <a name="Lightsail-Type-Bundle-instanceType"></a>
The instance type (`micro`).
Type: String
Required: No

 ** isActive **   <a name="Lightsail-Type-Bundle-isActive"></a>
A Boolean value indicating whether the bundle is active.
Type: Boolean
Required: No

 ** name **   <a name="Lightsail-Type-Bundle-name"></a>
A friendly name for the bundle (`Micro`).
Type: String
Required: No

 ** power **   <a name="Lightsail-Type-Bundle-power"></a>
A numeric value that represents the power of the bundle (`500`). You can use the bundle's power value in conjunction with a blueprint's minimum power value to determine whether the blueprint will run on the bundle. For example, you need a bundle with a power value of 500 or more to create an instance that uses a blueprint with a minimum power value of 500.
Type: Integer
Required: No

 ** price **   <a name="Lightsail-Type-Bundle-price"></a>
The price in US dollars (`5.0`) of the bundle.
Type: Float
Required: No

 ** publicIpv4AddressCount **   <a name="Lightsail-Type-Bundle-publicIpv4AddressCount"></a>
An integer that indicates the public ipv4 address count included in the bundle, the value is either 0 or 1.
Type: Integer
Required: No

 ** ramSizeInGb **   <a name="Lightsail-Type-Bundle-ramSizeInGb"></a>
The amount of RAM in GB (`2.0`).
Type: Float
Required: No

 ** supportedAppCategories **   <a name="Lightsail-Type-Bundle-supportedAppCategories"></a>
Virtual computer blueprints that are supported by a Lightsail for Research bundle.
This parameter only applies to Lightsail for Research resources.
Type: Array of strings
Valid Values: `LfR`
Required: No

 ** supportedPlatforms **   <a name="Lightsail-Type-Bundle-supportedPlatforms"></a>
The operating system platform (Linux/Unix-based or Windows Server-based) that the bundle supports. You can only launch a `WINDOWS` bundle on a blueprint that supports the `WINDOWS` platform. `LINUX_UNIX` blueprints require a `LINUX_UNIX` bundle.
Type: Array of strings
Valid Values: `LINUX_UNIX | WINDOWS`
Required: No

 ** transferPerMonthInGb **   <a name="Lightsail-Type-Bundle-transferPerMonthInGb"></a>
The data transfer rate per month in GB (`2000`).
Type: Integer
Required: No

## See Also
<a name="API_Bundle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/Bundle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/Bundle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/Bundle)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
