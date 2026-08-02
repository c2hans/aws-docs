---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_UpdateCloudExadataInfrastructure.html
---

# UpdateCloudExadataInfrastructure
<a name="API_UpdateCloudExadataInfrastructure"></a>

Updates the properties of an Exadata infrastructure resource.

## Request Syntax
<a name="API_UpdateCloudExadataInfrastructure_RequestSyntax"></a>

```
{
   "cloudExadataInfrastructureId": "{{string}}",
   "maintenanceWindow": {
      "customActionTimeoutInMins": {{number}},
      "daysOfWeek": [
         {
            "name": "{{string}}"
         }
      ],
      "hoursOfDay": [ {{number}} ],
      "isCustomActionTimeoutEnabled": {{boolean}},
      "leadTimeInWeeks": {{number}},
      "months": [
         {
            "name": "{{string}}"
         }
      ],
      "patchingMode": "{{string}}",
      "preference": "{{string}}",
      "skipRu": {{boolean}},
      "weeksOfMonth": [ {{number}} ]
   }
}
```

## Request Parameters
<a name="API_UpdateCloudExadataInfrastructure_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cloudExadataInfrastructureId](#API_UpdateCloudExadataInfrastructure_RequestSyntax) **   <a name="odb-UpdateCloudExadataInfrastructure-request-cloudExadataInfrastructureId"></a>
The unique identifier of the Exadata infrastructure to update.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

 ** [maintenanceWindow](#API_UpdateCloudExadataInfrastructure_RequestSyntax) **   <a name="odb-UpdateCloudExadataInfrastructure-request-maintenanceWindow"></a>
The scheduling details for the maintenance window. Patching and system updates take place during the maintenance window.
Type: [MaintenanceWindow](API_MaintenanceWindow.md) object
Required: No

## Response Syntax
<a name="API_UpdateCloudExadataInfrastructure_ResponseSyntax"></a>

```
{
   "cloudExadataInfrastructureId": "string",
   "displayName": "string",
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_UpdateCloudExadataInfrastructure_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cloudExadataInfrastructureId](#API_UpdateCloudExadataInfrastructure_ResponseSyntax) **   <a name="odb-UpdateCloudExadataInfrastructure-response-cloudExadataInfrastructureId"></a>
The unique identifier of the updated Exadata infrastructure.
Type: String

 ** [displayName](#API_UpdateCloudExadataInfrastructure_ResponseSyntax) **   <a name="odb-UpdateCloudExadataInfrastructure-response-displayName"></a>
The user-friendly name of the updated Exadata infrastructure.
Type: String

 ** [status](#API_UpdateCloudExadataInfrastructure_ResponseSyntax) **   <a name="odb-UpdateCloudExadataInfrastructure-response-status"></a>
The current status of the Exadata infrastructure after the update operation.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`

 ** [statusReason](#API_UpdateCloudExadataInfrastructure_ResponseSyntax) **   <a name="odb-UpdateCloudExadataInfrastructure-response-statusReason"></a>
Additional information about the status of the Exadata infrastructure after the update operation.
Type: String

## Errors
<a name="API_UpdateCloudExadataInfrastructure_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.
HTTP Status Code: 400

 ** ConflictException **
Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.
 ** resourceId **
The identifier of the resource that caused the conflict.
 ** resourceType **
The type of resource that caused the conflict.
HTTP Status Code: 400

 ** InternalServerException **
Occurs when there is an internal failure in the Oracle Database@AWS service. Wait and try again.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after an internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of resource that was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after being throttled.
HTTP Status Code: 400

 ** ValidationException **
The request has failed validation because it is missing required fields or has invalid inputs.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
The reason why the validation failed.
HTTP Status Code: 400

## See Also
<a name="API_UpdateCloudExadataInfrastructure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/UpdateCloudExadataInfrastructure)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/UpdateCloudExadataInfrastructure)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/UpdateCloudExadataInfrastructure)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/UpdateCloudExadataInfrastructure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/UpdateCloudExadataInfrastructure)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/UpdateCloudExadataInfrastructure)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/UpdateCloudExadataInfrastructure)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/UpdateCloudExadataInfrastructure)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/UpdateCloudExadataInfrastructure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/UpdateCloudExadataInfrastructure)
