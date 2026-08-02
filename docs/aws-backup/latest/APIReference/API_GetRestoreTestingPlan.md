---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_GetRestoreTestingPlan.html
---

# GetRestoreTestingPlan
<a name="API_GetRestoreTestingPlan"></a>

Returns `RestoreTestingPlan` details for the specified `RestoreTestingPlanName`. The details are the body of a restore testing plan in JSON format, in addition to plan metadata.

## Request Syntax
<a name="API_GetRestoreTestingPlan_RequestSyntax"></a>

```
GET /restore-testing/plans/{{RestoreTestingPlanName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRestoreTestingPlan_RequestParameters"></a>

The request uses the following URI parameters.

 ** [RestoreTestingPlanName](#API_GetRestoreTestingPlan_RequestSyntax) **   <a name="Backup-GetRestoreTestingPlan-request-uri-RestoreTestingPlanName"></a>
Required unique name of the restore testing plan.
Required: Yes

## Request Body
<a name="API_GetRestoreTestingPlan_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRestoreTestingPlan_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "RestoreTestingPlan": {
      "CreationTime": number,
      "CreatorRequestId": "string",
      "LastExecutionTime": number,
      "LastUpdateTime": number,
      "RecoveryPointSelection": {
         "Algorithm": "string",
         "ExcludeVaults": [ "string" ],
         "IncludeVaults": [ "string" ],
         "RecoveryPointTypes": [ "string" ],
         "SelectionWindowDays": number
      },
      "RestoreTestingPlanArn": "string",
      "RestoreTestingPlanName": "string",
      "ScheduleExpression": "string",
      "ScheduleExpressionTimezone": "string",
      "StartWindowHours": number
   }
}
```

## Response Elements
<a name="API_GetRestoreTestingPlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RestoreTestingPlan](#API_GetRestoreTestingPlan_ResponseSyntax) **   <a name="Backup-GetRestoreTestingPlan-response-RestoreTestingPlan"></a>
Specifies the body of a restore testing plan. Includes `RestoreTestingPlanName`.
Type: [RestoreTestingPlanForGet](API_RestoreTestingPlanForGet.md) object

## Errors
<a name="API_GetRestoreTestingPlan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
A resource that is required for the action doesn't exist.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ServiceUnavailableException **
The request failed due to a temporary failure of the server.
 ** Context **

 ** Type **

HTTP Status Code: 500

## See Also
<a name="API_GetRestoreTestingPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/GetRestoreTestingPlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/GetRestoreTestingPlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/GetRestoreTestingPlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/GetRestoreTestingPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/GetRestoreTestingPlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/GetRestoreTestingPlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/GetRestoreTestingPlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/GetRestoreTestingPlan)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/GetRestoreTestingPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/GetRestoreTestingPlan)
