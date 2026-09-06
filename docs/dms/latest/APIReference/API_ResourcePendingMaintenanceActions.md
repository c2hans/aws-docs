---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_ResourcePendingMaintenanceActions.html
---

# ResourcePendingMaintenanceActions
<a name="API_ResourcePendingMaintenanceActions"></a>

Identifies an AWS DMS resource and any pending actions for it.

## Contents
<a name="API_ResourcePendingMaintenanceActions_Contents"></a>

 ** PendingMaintenanceActionDetails **   <a name="DMS-Type-ResourcePendingMaintenanceActions-PendingMaintenanceActionDetails"></a>
Detailed information about the pending maintenance action.
Type: Array of [PendingMaintenanceAction](API_PendingMaintenanceAction.md) objects
Required: No

 ** ResourceIdentifier **   <a name="DMS-Type-ResourcePendingMaintenanceActions-ResourceIdentifier"></a>
The Amazon Resource Name (ARN) of the DMS resource that the pending maintenance action applies to. For information about creating an ARN, see [ Constructing an Amazon Resource Name (ARN) for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.AWS.ARN.html) in the AWS DMS documentation.
Type: String
Required: No

## See Also
<a name="API_ResourcePendingMaintenanceActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/ResourcePendingMaintenanceActions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/ResourcePendingMaintenanceActions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/ResourcePendingMaintenanceActions)
