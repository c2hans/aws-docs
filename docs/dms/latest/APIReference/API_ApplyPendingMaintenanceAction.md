---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_ApplyPendingMaintenanceAction.html
---

# ApplyPendingMaintenanceAction
<a name="API_ApplyPendingMaintenanceAction"></a>

Applies a pending maintenance action to a resource (for example, to a replication instance).

## Request Syntax
<a name="API_ApplyPendingMaintenanceAction_RequestSyntax"></a>

```
{
   "ApplyAction": "{{string}}",
   "OptInType": "{{string}}",
   "ReplicationInstanceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ApplyPendingMaintenanceAction_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApplyAction](#API_ApplyPendingMaintenanceAction_RequestSyntax) **   <a name="DMS-ApplyPendingMaintenanceAction-request-ApplyAction"></a>
The pending maintenance action to apply to this resource.
Valid values: `os-upgrade`, `system-update`, `db-upgrade`, `os-patch`
Type: String
Required: Yes

 ** [OptInType](#API_ApplyPendingMaintenanceAction_RequestSyntax) **   <a name="DMS-ApplyPendingMaintenanceAction-request-OptInType"></a>
A value that specifies the type of opt-in request, or undoes an opt-in request. You can't undo an opt-in request of type `immediate`.
Valid values:
+  `immediate` - Apply the maintenance action immediately.
+  `next-maintenance` - Apply the maintenance action during the next maintenance window for the resource.
+  `undo-opt-in` - Cancel any existing `next-maintenance` opt-in requests.
Type: String
Required: Yes

 ** [ReplicationInstanceArn](#API_ApplyPendingMaintenanceAction_RequestSyntax) **   <a name="DMS-ApplyPendingMaintenanceAction-request-ReplicationInstanceArn"></a>
The Amazon Resource Name (ARN) of the AWS DMS resource that the pending maintenance action applies to.
Type: String
Required: Yes

## Response Syntax
<a name="API_ApplyPendingMaintenanceAction_ResponseSyntax"></a>

```
{
   "ResourcePendingMaintenanceActions": {
      "PendingMaintenanceActionDetails": [
         {
            "Action": "string",
            "AutoAppliedAfterDate": number,
            "CurrentApplyDate": number,
            "Description": "string",
            "ForcedApplyDate": number,
            "OptInStatus": "string"
         }
      ],
      "ResourceIdentifier": "string"
   }
}
```

## Response Elements
<a name="API_ApplyPendingMaintenanceAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResourcePendingMaintenanceActions](#API_ApplyPendingMaintenanceAction_ResponseSyntax) **   <a name="DMS-ApplyPendingMaintenanceAction-response-ResourcePendingMaintenanceActions"></a>
The AWS DMS resource that the pending maintenance action will be applied to.
Type: [ResourcePendingMaintenanceActions](API_ResourcePendingMaintenanceActions.md) object

## Errors
<a name="API_ApplyPendingMaintenanceAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_ApplyPendingMaintenanceAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/ApplyPendingMaintenanceAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/ApplyPendingMaintenanceAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/ApplyPendingMaintenanceAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/ApplyPendingMaintenanceAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/ApplyPendingMaintenanceAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/ApplyPendingMaintenanceAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/ApplyPendingMaintenanceAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/ApplyPendingMaintenanceAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/ApplyPendingMaintenanceAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/ApplyPendingMaintenanceAction)
