---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_CloneToRefreshableConfiguration.html
---

# CloneToRefreshableConfiguration
<a name="API_CloneToRefreshableConfiguration"></a>

The configuration for creating an Autonomous Database as a refreshable clone.

## Contents
<a name="API_CloneToRefreshableConfiguration_Contents"></a>

 ** sourceAutonomousDatabaseId **   <a name="odb-Type-CloneToRefreshableConfiguration-sourceAutonomousDatabaseId"></a>
The unique identifier of the source Autonomous Database to create the refreshable clone from.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

 ** autoRefreshFrequencyInSeconds **   <a name="odb-Type-CloneToRefreshableConfiguration-autoRefreshFrequencyInSeconds"></a>
The frequency, in seconds, at which the refreshable clone is automatically refreshed.
Type: Integer
Valid Range: Minimum value of 3600. Maximum value of 604800.
Required: No

 ** autoRefreshPointLagInSeconds **   <a name="odb-Type-CloneToRefreshableConfiguration-autoRefreshPointLagInSeconds"></a>
The time lag, in seconds, between the refreshable clone and its source database.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 604800.
Required: No

 ** cloneType **   <a name="odb-Type-CloneToRefreshableConfiguration-cloneType"></a>
The type of clone to create.
Type: String
Valid Values: `FULL | METADATA | PARTIAL`
Required: No

 ** openMode **   <a name="odb-Type-CloneToRefreshableConfiguration-openMode"></a>
The mode in which to open the refreshable clone, either read-only or read/write.
Type: String
Valid Values: `READ_ONLY | READ_WRITE`
Required: No

 ** refreshableMode **   <a name="odb-Type-CloneToRefreshableConfiguration-refreshableMode"></a>
The refresh mode of the refreshable clone, either automatic or manual.
Type: String
Valid Values: `AUTOMATIC | MANUAL`
Required: No

 ** timeOfAutoRefreshStart **   <a name="odb-Type-CloneToRefreshableConfiguration-timeOfAutoRefreshStart"></a>
The date and time at which the automatic refresh of the refreshable clone starts.
Type: Timestamp
Required: No

## See Also
<a name="API_CloneToRefreshableConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/CloneToRefreshableConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/CloneToRefreshableConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/CloneToRefreshableConfiguration)
