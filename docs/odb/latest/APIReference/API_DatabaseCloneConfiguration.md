---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_DatabaseCloneConfiguration.html
---

# DatabaseCloneConfiguration
<a name="API_DatabaseCloneConfiguration"></a>

The configuration for creating an Autonomous Database as a clone of an existing database.

## Contents
<a name="API_DatabaseCloneConfiguration_Contents"></a>

 ** cloneType **   <a name="odb-Type-DatabaseCloneConfiguration-cloneType"></a>
The type of clone to create, either a full clone, a metadata clone, or a partial clone.
Type: String
Valid Values: `FULL | METADATA | PARTIAL`
Required: Yes

 ** sourceAutonomousDatabaseId **   <a name="odb-Type-DatabaseCloneConfiguration-sourceAutonomousDatabaseId"></a>
The unique identifier of the source Autonomous Database to clone.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

## See Also
<a name="API_DatabaseCloneConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/DatabaseCloneConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/DatabaseCloneConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/DatabaseCloneConfiguration)
