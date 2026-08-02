---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ServerlessV2PlatformVersionInfo.html
---

# ServerlessV2PlatformVersionInfo
<a name="API_ServerlessV2PlatformVersionInfo"></a>

This data type is used as a response element in the action `DescribeServerlessV2PlatformVersions`.

## Contents
<a name="API_ServerlessV2PlatformVersionInfo_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Engine **
The name of the database engine.
Type: String
Required: No

 ** IsDefault **
Indicates whether this platform version is the default version for the engine. The default platform version is the version used for new DB clusters.
Type: Boolean
Required: No

 ** ServerlessV2FeaturesSupport **
Specifies any Aurora Serverless v2 properties or limits that differ between Aurora Serverless v2 platform versions. You can retrieve the platform version of an existing DB cluster and check whether that version supports certain Aurora Serverless v2 features before you attempt to use those features.
Type: [ServerlessV2FeaturesSupport](API_ServerlessV2FeaturesSupport.md) object
Required: No

 ** ServerlessV2PlatformVersion **
The version number of the serverless platform.
Type: String
Required: No

 ** ServerlessV2PlatformVersionDescription **
The description of the serverless platform.
Type: String
Required: No

 ** Status **
The status of the serverless platform. Valid statuses are the following:
+  `enabled` - The platform version is in use.
+  `disabled` - The platform version is not in use.
Type: String
Required: No

## See Also
<a name="API_ServerlessV2PlatformVersionInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ServerlessV2PlatformVersionInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ServerlessV2PlatformVersionInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ServerlessV2PlatformVersionInfo)
