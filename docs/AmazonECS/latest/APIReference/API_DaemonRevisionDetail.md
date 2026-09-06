---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DaemonRevisionDetail.html
---

# DaemonRevisionDetail
<a name="API_DaemonRevisionDetail"></a>

Details about a daemon revision, including the running task counts per capacity provider.

## Contents
<a name="API_DaemonRevisionDetail_Contents"></a>

 ** arn **   <a name="ECS-Type-DaemonRevisionDetail-arn"></a>
The Amazon Resource Name (ARN) of the daemon revision.
Type: String
Required: No

 ** capacityProviders **   <a name="ECS-Type-DaemonRevisionDetail-capacityProviders"></a>
The capacity providers associated with this daemon revision.
Type: Array of [DaemonCapacityProvider](API_DaemonCapacityProvider.md) objects
Required: No

 ** totalRunningCount **   <a name="ECS-Type-DaemonRevisionDetail-totalRunningCount"></a>
The total number of daemon tasks running for this revision.
Type: Integer
Required: No

 ** totalWithoutDaemonCount **   <a name="ECS-Type-DaemonRevisionDetail-totalWithoutDaemonCount"></a>
The total number of instances running without the daemon task for this revision, across all capacity providers. These instances aren't included in `totalRunningCount`.
Type: Integer
Required: No

## See Also
<a name="API_DaemonRevisionDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DaemonRevisionDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DaemonRevisionDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DaemonRevisionDetail)
