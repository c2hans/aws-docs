---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_EngineVersion.html
---

# EngineVersion
<a name="API_EngineVersion"></a>

Provides information about a replication instance version.

## Contents
<a name="API_EngineVersion_Contents"></a>

 ** AutoUpgradeDate **   <a name="DMS-Type-EngineVersion-AutoUpgradeDate"></a>
The date when the replication instance will be automatically upgraded. This setting only applies if the `auto-minor-version` setting is enabled.
Type: Timestamp
Required: No

 ** AvailableUpgrades **   <a name="DMS-Type-EngineVersion-AvailableUpgrades"></a>
The list of valid replication instance versions that you can upgrade to.
Type: Array of strings
Required: No

 ** DeprecationDate **   <a name="DMS-Type-EngineVersion-DeprecationDate"></a>
The date when the replication instance version will be deprecated and can no longer be requested.
Type: Timestamp
Required: No

 ** ForceUpgradeDate **   <a name="DMS-Type-EngineVersion-ForceUpgradeDate"></a>
The date when the replication instance will have a version upgrade forced.
Type: Timestamp
Required: No

 ** LaunchDate **   <a name="DMS-Type-EngineVersion-LaunchDate"></a>
The date when the replication instance version became publicly available.
Type: Timestamp
Required: No

 ** Lifecycle **   <a name="DMS-Type-EngineVersion-Lifecycle"></a>
The lifecycle status of the replication instance version. Valid values are `DEPRECATED`, `DEFAULT_VERSION`, and `ACTIVE`.
Type: String
Required: No

 ** ReleaseStatus **   <a name="DMS-Type-EngineVersion-ReleaseStatus"></a>
The release status of the replication instance version.
Type: String
Valid Values: `beta | prod`
Required: No

 ** Version **   <a name="DMS-Type-EngineVersion-Version"></a>
The version number of the replication instance.
Type: String
Required: No

## See Also
<a name="API_EngineVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/EngineVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/EngineVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/EngineVersion)
