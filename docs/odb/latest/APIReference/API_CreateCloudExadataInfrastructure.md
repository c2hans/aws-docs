---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_CreateCloudExadataInfrastructure.html
---

# CreateCloudExadataInfrastructure
<a name="API_CreateCloudExadataInfrastructure"></a>

Creates an Exadata infrastructure.

## Request Syntax
<a name="API_CreateCloudExadataInfrastructure_RequestSyntax"></a>

```
{
   "availabilityZone": "{{string}}",
   "availabilityZoneId": "{{string}}",
   "clientToken": "{{string}}",
   "computeCount": {{number}},
   "customerContactsToSendToOCI": [
      {
         "email": "{{string}}"
      }
   ],
   "databaseServerType": "{{string}}",
   "displayName": "{{string}}",
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
   },
   "shape": "{{string}}",
   "storageCount": {{number}},
   "storageServerType": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateCloudExadataInfrastructure_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [availabilityZone](#API_CreateCloudExadataInfrastructure_RequestSyntax) **   <a name="odb-CreateCloudExadataInfrastructure-request-availabilityZone"></a>
The name of the Availability Zone (AZ) where the Exadata infrastructure is located.
This operation requires that you specify a value for either `availabilityZone` or `availabilityZoneId`.
Example: `us-east-1a`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [availabilityZoneId](#API_CreateCloudExadataInfrastructure_RequestSyntax) **   <a name="odb-CreateCloudExadataInfrastructure-request-availabilityZoneId"></a>
The AZ ID of the AZ where the Exadata infrastructure is located.
This operation requires that you specify a value for either `availabilityZone` or `availabilityZoneId`.
Example: `use1-az1`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [clientToken](#API_CreateCloudExadataInfrastructure_RequestSyntax) **   <a name="odb-CreateCloudExadataInfrastructure-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. The client token is valid for up to 24 hours after it's first used.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 64.
Pattern: `[a-zA-Z0-9_\/.=-]+`
Required: No

 ** [computeCount](#API_CreateCloudExadataInfrastructure_RequestSyntax) **   <a name="odb-CreateCloudExadataInfrastructure-request-computeCount"></a>
The number of database servers for the Exadata infrastructure. Valid values for this parameter depend on the shape. To get information about the minimum and maximum values, use the `ListDbSystemShapes` operation.
Type: Integer
Required: Yes

 ** [customerContactsToSendToOCI](#API_CreateCloudExadataInfrastructure_RequestSyntax) **   <a name="odb-CreateCloudExadataInfrastructure-request-customerContactsToSendToOCI"></a>
The email addresses of contacts to receive notification from Oracle about maintenance updates for the Exadata infrastructure.
Type: Array of [CustomerContact](API_CustomerContact.md) objects
Required: No

 ** [databaseServerType](#API_CreateCloudExadataInfrastructure_RequestSyntax) **   <a name="odb-CreateCloudExadataInfrastructure-request-databaseServerType"></a>
The database server model type of the Exadata infrastructure. For the list of valid model names, use the `ListDbSystemShapes` operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_\/.=-]+`
Required: No

 ** [displayName](#API_CreateCloudExadataInfrastructure_RequestSyntax) **   <a name="odb-CreateCloudExadataInfrastructure-request-displayName"></a>
A user-friendly name for the Exadata infrastructure.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_](?!.*--)[a-zA-Z0-9_-]*`
Required: Yes

 ** [maintenanceWindow](#API_CreateCloudExadataInfrastructure_RequestSyntax) **   <a name="odb-CreateCloudExadataInfrastructure-request-maintenanceWindow"></a>
The maintenance window configuration for the Exadata Cloud infrastructure.
This allows you to define when maintenance operations such as patching and updates can be performed on the infrastructure.
Type: [MaintenanceWindow](API_MaintenanceWindow.md) object
Required: No

 ** [shape](#API_CreateCloudExadataInfrastructure_RequestSyntax) **   <a name="odb-CreateCloudExadataInfrastructure-request-shape"></a>
The model name of the Exadata infrastructure. For the list of valid model names, use the `ListDbSystemShapes` operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_\/.=-]+`
Required: Yes

 ** [storageCount](#API_CreateCloudExadataInfrastructure_RequestSyntax) **   <a name="odb-CreateCloudExadataInfrastructure-request-storageCount"></a>
The number of storage servers to activate for this Exadata infrastructure. Valid values for this parameter depend on the shape. To get information about the minimum and maximum values, use the `ListDbSystemShapes` operation.
Type: Integer
Required: Yes

 ** [storageServerType](#API_CreateCloudExadataInfrastructure_RequestSyntax) **   <a name="odb-CreateCloudExadataInfrastructure-request-storageServerType"></a>
The storage server model type of the Exadata infrastructure. For the list of valid model names, use the `ListDbSystemShapes` operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_\/.=-]+`
Required: No

 ** [tags](#API_CreateCloudExadataInfrastructure_RequestSyntax) **   <a name="odb-CreateCloudExadataInfrastructure-request-tags"></a>
The list of resource tags to apply to the Exadata infrastructure.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateCloudExadataInfrastructure_ResponseSyntax"></a>

```
{
   "cloudExadataInfrastructureId": "string",
   "displayName": "string",
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_CreateCloudExadataInfrastructure_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cloudExadataInfrastructureId](#API_CreateCloudExadataInfrastructure_ResponseSyntax) **   <a name="odb-CreateCloudExadataInfrastructure-response-cloudExadataInfrastructureId"></a>
The unique identifier of the Exadata infrastructure.
Type: String

 ** [displayName](#API_CreateCloudExadataInfrastructure_ResponseSyntax) **   <a name="odb-CreateCloudExadataInfrastructure-response-displayName"></a>
The user-friendly name for the Exadata infrastructure.
Type: String

 ** [status](#API_CreateCloudExadataInfrastructure_ResponseSyntax) **   <a name="odb-CreateCloudExadataInfrastructure-response-status"></a>
The current status of the Exadata infrastructure.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`

 ** [statusReason](#API_CreateCloudExadataInfrastructure_ResponseSyntax) **   <a name="odb-CreateCloudExadataInfrastructure-response-statusReason"></a>
Additional information about the status of the Exadata infrastructure.
Type: String

## Errors
<a name="API_CreateCloudExadataInfrastructure_Errors"></a>

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

 ** ServiceQuotaExceededException **
You have exceeded the service quota.
 ** quotaCode **
The unqiue identifier of the service quota that was exceeded.
 ** resourceId **
The identifier of the resource that exceeded the service quota.
 ** resourceType **
The type of resource that exceeded the service quota.
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
<a name="API_CreateCloudExadataInfrastructure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/CreateCloudExadataInfrastructure)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/CreateCloudExadataInfrastructure)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/CreateCloudExadataInfrastructure)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/CreateCloudExadataInfrastructure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/CreateCloudExadataInfrastructure)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/CreateCloudExadataInfrastructure)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/CreateCloudExadataInfrastructure)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/CreateCloudExadataInfrastructure)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/CreateCloudExadataInfrastructure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/CreateCloudExadataInfrastructure)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
