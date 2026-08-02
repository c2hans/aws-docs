---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_PlatformFilter.html
---

# PlatformFilter
<a name="API_PlatformFilter"></a>

Describes criteria to restrict the results when listing platform versions.

The filter is evaluated as follows: `Type Operator Values[1]`

## Contents
<a name="API_PlatformFilter_Contents"></a>

 ** Operator **
The operator to apply to the `Type` with each of the `Values`.
Valid values: `=` \| `!=` \| `<` \| `<=` \| `>` \| `>=` \| `contains` \| `begins_with` \| `ends_with`
Type: String
Required: No

 ** Type **
The platform version attribute to which the filter values are applied.
Valid values: `PlatformName` \| `PlatformVersion` \| `PlatformStatus` \| `PlatformBranchName` \| `PlatformLifecycleState` \| `PlatformOwner` \| `SupportedTier` \| `SupportedAddon` \| `ProgrammingLanguageName` \| `OperatingSystemName`
Type: String
Required: No

 ** Values.member.N **
The list of values applied to the filtering platform version attribute. Only one value is supported for all current operators.
The following list shows valid filter values for some filter attributes.
+  `PlatformStatus`: `Creating` \| `Failed` \| `Ready` \| `Deleting` \| `Deleted`
+  `PlatformLifecycleState`: `recommended`
+  `SupportedTier`: `WebServer/Standard` \| `Worker/SQS/HTTP`
+  `SupportedAddon`: `Log/S3` \| `Monitoring/Healthd` \| `WorkerDaemon/SQSD`
Type: Array of strings
Required: No

## See Also
<a name="API_PlatformFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/PlatformFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/PlatformFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/PlatformFilter)
