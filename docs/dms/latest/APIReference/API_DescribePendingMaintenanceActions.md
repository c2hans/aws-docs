---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribePendingMaintenanceActions.html
---

# DescribePendingMaintenanceActions
<a name="API_DescribePendingMaintenanceActions"></a>

Returns a list of upcoming maintenance events for replication instances in your account in the current Region.

## Request Syntax
<a name="API_DescribePendingMaintenanceActions_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "Marker": "{{string}}",
   "MaxRecords": {{number}},
   "ReplicationInstanceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribePendingMaintenanceActions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribePendingMaintenanceActions_RequestSyntax) **   <a name="DMS-DescribePendingMaintenanceActions-request-Filters"></a>

Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [Marker](#API_DescribePendingMaintenanceActions_RequestSyntax) **   <a name="DMS-DescribePendingMaintenanceActions-request-Marker"></a>
 An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** [MaxRecords](#API_DescribePendingMaintenanceActions_RequestSyntax) **   <a name="DMS-DescribePendingMaintenanceActions-request-MaxRecords"></a>
 The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
Default: 100
Constraints: Minimum 20, maximum 100.
Type: Integer
Required: No

 ** [ReplicationInstanceArn](#API_DescribePendingMaintenanceActions_RequestSyntax) **   <a name="DMS-DescribePendingMaintenanceActions-request-ReplicationInstanceArn"></a>
The Amazon Resource Name (ARN) of the replication instance.
Type: String
Required: No

## Response Syntax
<a name="API_DescribePendingMaintenanceActions_ResponseSyntax"></a>

```
{
   "Marker": "string",
   "PendingMaintenanceActions": [
      {
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
   ]
}
```

## Response Elements
<a name="API_DescribePendingMaintenanceActions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Marker](#API_DescribePendingMaintenanceActions_ResponseSyntax) **   <a name="DMS-DescribePendingMaintenanceActions-response-Marker"></a>
 An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String

 ** [PendingMaintenanceActions](#API_DescribePendingMaintenanceActions_ResponseSyntax) **   <a name="DMS-DescribePendingMaintenanceActions-response-PendingMaintenanceActions"></a>
The pending maintenance action.
Type: Array of [ResourcePendingMaintenanceActions](API_ResourcePendingMaintenanceActions.md) objects

## Errors
<a name="API_DescribePendingMaintenanceActions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_DescribePendingMaintenanceActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribePendingMaintenanceActions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribePendingMaintenanceActions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribePendingMaintenanceActions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribePendingMaintenanceActions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribePendingMaintenanceActions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribePendingMaintenanceActions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribePendingMaintenanceActions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribePendingMaintenanceActions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribePendingMaintenanceActions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribePendingMaintenanceActions)
