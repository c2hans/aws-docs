---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_ApplyPendingMaintenanceAction.html
---

# ApplyPendingMaintenanceAction
<a name="API_ApplyPendingMaintenanceAction"></a>

Applies a pending maintenance action to a resource (for example, to a DB instance).

## Request Parameters
<a name="API_ApplyPendingMaintenanceAction_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ApplyAction **
The pending maintenance action to apply to this resource.
Valid values: `system-update`, `db-upgrade`
Type: String
Required: Yes

 ** OptInType **
A value that specifies the type of opt-in request, or undoes an opt-in request. An opt-in request of type `immediate` can't be undone.
Valid values:
+  `immediate` - Apply the maintenance action immediately.
+  `next-maintenance` - Apply the maintenance action during the next maintenance window for the resource.
+  `undo-opt-in` - Cancel any existing `next-maintenance` opt-in requests.
Type: String
Required: Yes

 ** ResourceIdentifier **
The Amazon Resource Name (ARN) of the resource that the pending maintenance action applies to. For information about creating an ARN, see [ Constructing an Amazon Resource Name (ARN)](https://docs.aws.amazon.com/neptune/latest/UserGuide/tagging.ARN.html#tagging.ARN.Constructing).
Type: String
Required: Yes

## Response Elements
<a name="API_ApplyPendingMaintenanceAction_ResponseElements"></a>

The following element is returned by the service.

 ** ResourcePendingMaintenanceActions **
Describes the pending maintenance actions for a resource.
Type: [ResourcePendingMaintenanceActions](API_ResourcePendingMaintenanceActions.md) object

## Errors
<a name="API_ApplyPendingMaintenanceAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundFault **
The specified resource ID was not found.
HTTP Status Code: 404

## See Also
<a name="API_ApplyPendingMaintenanceAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/ApplyPendingMaintenanceAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/ApplyPendingMaintenanceAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/ApplyPendingMaintenanceAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/ApplyPendingMaintenanceAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/ApplyPendingMaintenanceAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/ApplyPendingMaintenanceAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/ApplyPendingMaintenanceAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/ApplyPendingMaintenanceAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/ApplyPendingMaintenanceAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/ApplyPendingMaintenanceAction)
