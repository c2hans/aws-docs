---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_LifecycleEvent.html
---

# LifecycleEvent
<a name="API_LifecycleEvent"></a>

Information about a deployment lifecycle event.

## Contents
<a name="API_LifecycleEvent_Contents"></a>

 ** diagnostics **   <a name="CodeDeploy-Type-LifecycleEvent-diagnostics"></a>
Diagnostic information about the deployment lifecycle event.
Type: [Diagnostics](API_Diagnostics.md) object
Required: No

 ** endTime **   <a name="CodeDeploy-Type-LifecycleEvent-endTime"></a>
A timestamp that indicates when the deployment lifecycle event ended.
Type: Timestamp
Required: No

 ** lifecycleEventName **   <a name="CodeDeploy-Type-LifecycleEvent-lifecycleEventName"></a>
The deployment lifecycle event name, such as `ApplicationStop`, `BeforeInstall`, `AfterInstall`, `ApplicationStart`, or `ValidateService`.
Type: String
Required: No

 ** startTime **   <a name="CodeDeploy-Type-LifecycleEvent-startTime"></a>
A timestamp that indicates when the deployment lifecycle event started.
Type: Timestamp
Required: No

 ** status **   <a name="CodeDeploy-Type-LifecycleEvent-status"></a>
The deployment lifecycle event status:
+ Pending: The deployment lifecycle event is pending.
+ InProgress: The deployment lifecycle event is in progress.
+ Succeeded: The deployment lifecycle event ran successfully.
+ Failed: The deployment lifecycle event has failed.
+ Skipped: The deployment lifecycle event has been skipped.
+ Unknown: The deployment lifecycle event is unknown.
Type: String
Valid Values: `Pending | InProgress | Succeeded | Failed | Skipped | Unknown`
Required: No

## See Also
<a name="API_LifecycleEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/LifecycleEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/LifecycleEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/LifecycleEvent)
