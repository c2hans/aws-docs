---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_ServiceLifecycle.html
---

# ServiceLifecycle
<a name="API_ServiceLifecycle"></a>

Contains lifecycle information for an AWS service version, including lifecycle events and version recommendations.

## Contents
<a name="API_ServiceLifecycle_Contents"></a>

 ** lifecycleEvents **   <a name="AWSHealth-Type-ServiceLifecycle-lifecycleEvents"></a>
The list of lifecycle events for this service version.
Type: Array of [LifecycleEvent](API_LifecycleEvent.md) objects
Required: No

 ** recommendedVersion **   <a name="AWSHealth-Type-ServiceLifecycle-recommendedVersion"></a>
The recommended version to upgrade to.
Type: String
Required: No

 ** service **   <a name="AWSHealth-Type-ServiceLifecycle-service"></a>
The name of the AWS service.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 30.
Pattern: `[^:/]{2,30}`
Required: No

 ** title **   <a name="AWSHealth-Type-ServiceLifecycle-title"></a>
A human-readable title for the lifecycle entry.
Type: String
Required: No

 ** version **   <a name="AWSHealth-Type-ServiceLifecycle-version"></a>
The version of the service.
Type: String
Required: No

## See Also
<a name="API_ServiceLifecycle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/ServiceLifecycle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/ServiceLifecycle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/ServiceLifecycle)
