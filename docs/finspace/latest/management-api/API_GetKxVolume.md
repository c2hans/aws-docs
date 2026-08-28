---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_GetKxVolume.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# GetKxVolume
<a name="API_GetKxVolume"></a>

 Retrieves the information about the volume.

## Request Syntax
<a name="API_GetKxVolume_RequestSyntax"></a>

```
GET /kx/environments/{{environmentId}}/kxvolumes/{{volumeName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetKxVolume_RequestParameters"></a>

The request uses the following URI parameters.

 ** [environmentId](#API_GetKxVolume_RequestSyntax) **   <a name="finspace-GetKxVolume-request-uri-environmentId"></a>
A unique identifier for the kdb environment, whose clusters can attach to the volume.
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^[a-z0-9]+$`
Required: Yes

 ** [volumeName](#API_GetKxVolume_RequestSyntax) **   <a name="finspace-GetKxVolume-request-uri-volumeName"></a>
A unique identifier for the volume.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: Yes

## Request Body
<a name="API_GetKxVolume_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetKxVolume_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "attachedClusters": [
      {
         "clusterName": "string",
         "clusterStatus": "string",
         "clusterType": "string"
      }
   ],
   "availabilityZoneIds": [ "string" ],
   "azMode": "string",
   "createdTimestamp": number,
   "description": "string",
   "environmentId": "string",
   "lastModifiedTimestamp": number,
   "nas1Configuration": {
      "size": number,
      "type": "string"
   },
   "status": "string",
   "statusReason": "string",
   "volumeArn": "string",
   "volumeName": "string",
   "volumeType": "string"
}
```

## Response Elements
<a name="API_GetKxVolume_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [attachedClusters](#API_GetKxVolume_ResponseSyntax) **   <a name="finspace-GetKxVolume-response-attachedClusters"></a>
 A list of cluster identifiers that a volume is attached to.
Type: Array of [KxAttachedCluster](API_KxAttachedCluster.md) objects

 ** [availabilityZoneIds](#API_GetKxVolume_ResponseSyntax) **   <a name="finspace-GetKxVolume-response-availabilityZoneIds"></a>
The identifier of the availability zones.
Type: Array of strings
Length Constraints: Minimum length of 8. Maximum length of 12.
Pattern: `^[a-zA-Z0-9-]+$`

 ** [azMode](#API_GetKxVolume_ResponseSyntax) **   <a name="finspace-GetKxVolume-response-azMode"></a>
The number of availability zones you want to assign per volume. Currently, FinSpace only supports `SINGLE` for volumes. This places dataview in a single AZ.
Type: String
Valid Values: `SINGLE | MULTI`

 ** [createdTimestamp](#API_GetKxVolume_ResponseSyntax) **   <a name="finspace-GetKxVolume-response-createdTimestamp"></a>
 The timestamp at which the volume was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp

 ** [description](#API_GetKxVolume_ResponseSyntax) **   <a name="finspace-GetKxVolume-response-description"></a>
 A description of the volume.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[a-zA-Z0-9. ]{1,1000}$`

 ** [environmentId](#API_GetKxVolume_ResponseSyntax) **   <a name="finspace-GetKxVolume-response-environmentId"></a>
A unique identifier for the kdb environment, whose clusters can attach to the volume.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^[a-z0-9]+$`

 ** [lastModifiedTimestamp](#API_GetKxVolume_ResponseSyntax) **   <a name="finspace-GetKxVolume-response-lastModifiedTimestamp"></a>
The last time that the volume was updated in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp

 ** [nas1Configuration](#API_GetKxVolume_ResponseSyntax) **   <a name="finspace-GetKxVolume-response-nas1Configuration"></a>
 Specifies the configuration for the Network attached storage (NAS\_1) file system volume.
Type: [KxNAS1Configuration](API_KxNAS1Configuration.md) object

 ** [status](#API_GetKxVolume_ResponseSyntax) **   <a name="finspace-GetKxVolume-response-status"></a>
The status of volume creation.
+ CREATING – The volume creation is in progress.
+ CREATE\_FAILED – The volume creation has failed.
+ ACTIVE – The volume is active.
+ UPDATING – The volume is in the process of being updated.
+ UPDATE\_FAILED – The update action failed.
+ UPDATED – The volume is successfully updated.
+ DELETING – The volume is in the process of being deleted.
+ DELETE\_FAILED – The system failed to delete the volume.
+ DELETED – The volume is successfully deleted.
Type: String
Valid Values: `CREATING | CREATE_FAILED | ACTIVE | UPDATING | UPDATED | UPDATE_FAILED | DELETING | DELETED | DELETE_FAILED`

 ** [statusReason](#API_GetKxVolume_ResponseSyntax) **   <a name="finspace-GetKxVolume-response-statusReason"></a>
The error message when a failed state occurs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `^[a-zA-Z0-9\_\-\.\s]+$`

 ** [volumeArn](#API_GetKxVolume_ResponseSyntax) **   <a name="finspace-GetKxVolume-response-volumeArn"></a>
 The ARN identifier of the volume.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws:finspace:[A-Za-z0-9_/.-]{0,63}:\d+:kxEnvironment/[0-9A-Za-z_-]{1,128}(/kxSharedVolume/[a-zA-Z0-9_-]{1,255})?$`

 ** [volumeName](#API_GetKxVolume_ResponseSyntax) **   <a name="finspace-GetKxVolume-response-volumeName"></a>
 A unique identifier for the volume.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`

 ** [volumeType](#API_GetKxVolume_ResponseSyntax) **   <a name="finspace-GetKxVolume-response-volumeType"></a>
 The type of file system volume. Currently, FinSpace only supports `NAS_1` volume type.
Type: String
Valid Values: `NAS_1`

## Errors
<a name="API_GetKxVolume_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There was a conflict with this action, and it could not be completed.
 ** reason **
The reason for the conflict exception.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** LimitExceededException **
A service limit or quota is exceeded.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetKxVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2021-03-12/GetKxVolume)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2021-03-12/GetKxVolume)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/GetKxVolume)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2021-03-12/GetKxVolume)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/GetKxVolume)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2021-03-12/GetKxVolume)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2021-03-12/GetKxVolume)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2021-03-12/GetKxVolume)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/finspace-2021-03-12/GetKxVolume)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/GetKxVolume)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
