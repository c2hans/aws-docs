---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetVolume.html
---

# GetVolume
<a name="API_GetVolume"></a>

Gets a persistent volume.

## Request Syntax
<a name="API_GetVolume_RequestSyntax"></a>

```
GET /2023-10-12/farms/{{farmId}}/fleets/{{fleetId}}/volumes/{{volumeId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetVolume_RequestParameters"></a>

The request uses the following URI parameters.

 ** [farmId](#API_GetVolume_RequestSyntax) **   <a name="deadlinecloud-GetVolume-request-uri-farmId"></a>
The farm ID of the farm that contains the fleet.
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** [fleetId](#API_GetVolume_RequestSyntax) **   <a name="deadlinecloud-GetVolume-request-uri-fleetId"></a>
The fleet ID of the fleet that contains the volume.
Pattern: `fleet-[0-9a-f]{32}`
Required: Yes

 ** [volumeId](#API_GetVolume_RequestSyntax) **   <a name="deadlinecloud-GetVolume-request-uri-volumeId"></a>
The volume ID of the volume to retrieve.
Pattern: `volume-[0-9a-f]{32}`
Required: Yes

## Request Body
<a name="API_GetVolume_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetVolume_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "attachedWorkerId": "string",
   "availabilityZoneId": "string",
   "createdAt": "string",
   "expiresAt": "string",
   "farmId": "string",
   "fleetId": "string",
   "iops": number,
   "lastAssignedAt": "string",
   "lastReleasedAt": "string",
   "sizeGiB": number,
   "state": "string",
   "throughputMiB": number,
   "volumeId": "string",
   "volumeType": "string"
}
```

## Response Elements
<a name="API_GetVolume_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [attachedWorkerId](#API_GetVolume_ResponseSyntax) **   <a name="deadlinecloud-GetVolume-response-attachedWorkerId"></a>
The worker ID of the worker the volume is attached to.
Type: String
Pattern: `worker-[0-9a-f]{32}`

 ** [availabilityZoneId](#API_GetVolume_ResponseSyntax) **   <a name="deadlinecloud-GetVolume-response-availabilityZoneId"></a>
The Availability Zone ID of the volume.
Type: String

 ** [createdAt](#API_GetVolume_ResponseSyntax) **   <a name="deadlinecloud-GetVolume-response-createdAt"></a>
The date and time the resource was created.
Type: Timestamp

 ** [expiresAt](#API_GetVolume_ResponseSyntax) **   <a name="deadlinecloud-GetVolume-response-expiresAt"></a>
The date and time the volume expires and will be deleted.
Type: Timestamp

 ** [farmId](#API_GetVolume_ResponseSyntax) **   <a name="deadlinecloud-GetVolume-response-farmId"></a>
The farm ID of the farm that contains the fleet.
Type: String
Pattern: `farm-[0-9a-f]{32}`

 ** [fleetId](#API_GetVolume_ResponseSyntax) **   <a name="deadlinecloud-GetVolume-response-fleetId"></a>
The fleet ID of the fleet that contains the volume.
Type: String
Pattern: `fleet-[0-9a-f]{32}`

 ** [iops](#API_GetVolume_ResponseSyntax) **   <a name="deadlinecloud-GetVolume-response-iops"></a>
The IOPS of the volume.
Type: Integer
Valid Range: Minimum value of 100. Maximum value of 80000.

 ** [lastAssignedAt](#API_GetVolume_ResponseSyntax) **   <a name="deadlinecloud-GetVolume-response-lastAssignedAt"></a>
The date and time the volume was last assigned to a worker.
Type: Timestamp

 ** [lastReleasedAt](#API_GetVolume_ResponseSyntax) **   <a name="deadlinecloud-GetVolume-response-lastReleasedAt"></a>
The date and time the volume was last released from a worker.
Type: Timestamp

 ** [sizeGiB](#API_GetVolume_ResponseSyntax) **   <a name="deadlinecloud-GetVolume-response-sizeGiB"></a>
The volume size in GiB.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65536.

 ** [state](#API_GetVolume_ResponseSyntax) **   <a name="deadlinecloud-GetVolume-response-state"></a>
The state of the volume.
Type: String
Valid Values: `PENDING_CREATION | PENDING_ATTACHMENT | IN_USE | AVAILABLE | PENDING_DELETION`

 ** [throughputMiB](#API_GetVolume_ResponseSyntax) **   <a name="deadlinecloud-GetVolume-response-throughputMiB"></a>
The throughput of the volume in MiB.
Type: Integer
Valid Range: Minimum value of 125. Maximum value of 2000.

 ** [volumeId](#API_GetVolume_ResponseSyntax) **   <a name="deadlinecloud-GetVolume-response-volumeId"></a>
The volume ID.
Type: String
Pattern: `volume-[0-9a-f]{32}`

 ** [volumeType](#API_GetVolume_ResponseSyntax) **   <a name="deadlinecloud-GetVolume-response-volumeType"></a>
The EBS volume type.
Type: String
Valid Values: `gp3`

## Errors
<a name="API_GetVolume_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action.
 ** context **
Information about the resources in use when the exception was thrown.
HTTP Status Code: 403

 ** InternalServerErrorException **
Deadline Cloud can't process your request right now. Try again later.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource can't be found.
 ** context **
Information about the resources in use when the exception was thrown.
 ** resourceId **
The identifier of the resource that couldn't be found.
 ** resourceType **
The type of the resource that couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a request rate quota.
 ** context **
Information about the resources in use when the exception was thrown.
 ** quotaCode **
Identifies the quota that is being throttled.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
 ** serviceCode **
Identifies the service that is being throttled.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
 ** context **
Information about the resources in use when the exception was thrown.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
The reason that the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_GetVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetVolume)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/deadline-2023-10-12/GetVolume)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetVolume)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetVolume)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetVolume)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetVolume)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetVolume)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetVolume)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetVolume)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetVolume)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
