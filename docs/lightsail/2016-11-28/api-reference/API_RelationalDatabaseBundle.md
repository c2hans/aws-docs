---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_RelationalDatabaseBundle.html
---

# RelationalDatabaseBundle
<a name="API_RelationalDatabaseBundle"></a>

Describes a database bundle. A bundle describes the performance specifications of the database.

## Contents
<a name="API_RelationalDatabaseBundle_Contents"></a>

 ** bundleId **   <a name="Lightsail-Type-RelationalDatabaseBundle-bundleId"></a>
The ID for the database bundle.
Type: String
Required: No

 ** cpuCount **   <a name="Lightsail-Type-RelationalDatabaseBundle-cpuCount"></a>
The number of virtual CPUs (vCPUs) for the database bundle.
Type: Integer
Required: No

 ** diskSizeInGb **   <a name="Lightsail-Type-RelationalDatabaseBundle-diskSizeInGb"></a>
The size of the disk for the database bundle.
Type: Integer
Required: No

 ** isActive **   <a name="Lightsail-Type-RelationalDatabaseBundle-isActive"></a>
A Boolean value indicating whether the database bundle is active.
Type: Boolean
Required: No

 ** isEncrypted **   <a name="Lightsail-Type-RelationalDatabaseBundle-isEncrypted"></a>
A Boolean value indicating whether the database bundle is encrypted.
Type: Boolean
Required: No

 ** name **   <a name="Lightsail-Type-RelationalDatabaseBundle-name"></a>
The name for the database bundle.
Type: String
Required: No

 ** price **   <a name="Lightsail-Type-RelationalDatabaseBundle-price"></a>
The cost of the database bundle in US currency.
Type: Float
Required: No

 ** ramSizeInGb **   <a name="Lightsail-Type-RelationalDatabaseBundle-ramSizeInGb"></a>
The amount of RAM in GB (for example, `2.0`) for the database bundle.
Type: Float
Required: No

 ** transferPerMonthInGb **   <a name="Lightsail-Type-RelationalDatabaseBundle-transferPerMonthInGb"></a>
The data transfer rate per month in GB for the database bundle.
Type: Integer
Required: No

## See Also
<a name="API_RelationalDatabaseBundle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/RelationalDatabaseBundle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/RelationalDatabaseBundle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/RelationalDatabaseBundle)
