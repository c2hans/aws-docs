---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_CreateKxVolume.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# CreateKxVolume
<a name="API_CreateKxVolume"></a>

 Creates a new volume with a specific amount of throughput and storage capacity.

## Request Syntax
<a name="API_CreateKxVolume_RequestSyntax"></a>

```
POST /kx/environments/{{environmentId}}/kxvolumes HTTP/1.1
Content-type: application/json

{
   "availabilityZoneIds": [ "{{string}}" ],
   "azMode": "{{string}}",
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "nas1Configuration": {
      "size": {{number}},
      "type": "{{string}}"
   },
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "volumeName": "{{string}}",
   "volumeType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateKxVolume_RequestParameters"></a>

The request uses the following URI parameters.

 ** [environmentId](#API_CreateKxVolume_RequestSyntax) **   <a name="finspace-CreateKxVolume-request-uri-environmentId"></a>
A unique identifier for the kdb environment, whose clusters can attach to the volume.
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^[a-z0-9]+$`
Required: Yes

## Request Body
<a name="API_CreateKxVolume_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [availabilityZoneIds](#API_CreateKxVolume_RequestSyntax) **   <a name="finspace-CreateKxVolume-request-availabilityZoneIds"></a>
The identifier of the availability zones.
Type: Array of strings
Length Constraints: Minimum length of 8. Maximum length of 12.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

 ** [azMode](#API_CreateKxVolume_RequestSyntax) **   <a name="finspace-CreateKxVolume-request-azMode"></a>
The number of availability zones you want to assign per volume. Currently, FinSpace only supports `SINGLE` for volumes. This places dataview in a single AZ.
Type: String
Valid Values: `SINGLE | MULTI`
Required: Yes

 ** [volumeName](#API_CreateKxVolume_RequestSyntax) **   <a name="finspace-CreateKxVolume-request-volumeName"></a>
A unique identifier for the volume.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: Yes

 ** [volumeType](#API_CreateKxVolume_RequestSyntax) **   <a name="finspace-CreateKxVolume-request-volumeType"></a>
 The type of file system volume. Currently, FinSpace only supports `NAS_1` volume type. When you select `NAS_1` volume type, you must also provide `nas1Configuration`.
Type: String
Valid Values: `NAS_1`
Required: Yes

 ** [clientToken](#API_CreateKxVolume_RequestSyntax) **   <a name="finspace-CreateKxVolume-request-clientToken"></a>
A token that ensures idempotency. This token expires in 10 minutes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `.*\S.*`
Required: No

 ** [description](#API_CreateKxVolume_RequestSyntax) **   <a name="finspace-CreateKxVolume-request-description"></a>
 A description of the volume.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[a-zA-Z0-9. ]{1,1000}$`
Required: No

 ** [nas1Configuration](#API_CreateKxVolume_RequestSyntax) **   <a name="finspace-CreateKxVolume-request-nas1Configuration"></a>
 Specifies the configuration for the Network attached storage (NAS\_1) file system volume. This parameter is required when you choose `volumeType` as *NAS\_1*.
Type: [KxNAS1Configuration](API_KxNAS1Configuration.md) object
Required: No

 ** [tags](#API_CreateKxVolume_RequestSyntax) **   <a name="finspace-CreateKxVolume-request-tags"></a>
 A list of key-value pairs to label the volume. You can add up to 50 tags to a volume.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Value Pattern: `^[a-zA-Z0-9+-=._:@ ]+$`
Required: No

## Response Syntax
<a name="API_CreateKxVolume_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "availabilityZoneIds": [ "string" ],
   "azMode": "string",
   "createdTimestamp": number,
   "description": "string",
   "environmentId": "string",
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
<a name="API_CreateKxVolume_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [availabilityZoneIds](#API_CreateKxVolume_ResponseSyntax) **   <a name="finspace-CreateKxVolume-response-availabilityZoneIds"></a>
The identifier of the availability zones.
Type: Array of strings
Length Constraints: Minimum length of 8. Maximum length of 12.
Pattern: `^[a-zA-Z0-9-]+$`

 ** [azMode](#API_CreateKxVolume_ResponseSyntax) **   <a name="finspace-CreateKxVolume-response-azMode"></a>
The number of availability zones you want to assign per volume. Currently, FinSpace only supports `SINGLE` for volumes. This places dataview in a single AZ.
Type: String
Valid Values: `SINGLE | MULTI`

 ** [createdTimestamp](#API_CreateKxVolume_ResponseSyntax) **   <a name="finspace-CreateKxVolume-response-createdTimestamp"></a>
The timestamp at which the volume was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp

 ** [description](#API_CreateKxVolume_ResponseSyntax) **   <a name="finspace-CreateKxVolume-response-description"></a>
 A description of the volume.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[a-zA-Z0-9. ]{1,1000}$`

 ** [environmentId](#API_CreateKxVolume_ResponseSyntax) **   <a name="finspace-CreateKxVolume-response-environmentId"></a>
A unique identifier for the kdb environment, whose clusters can attach to the volume.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^[a-z0-9]+$`

 ** [nas1Configuration](#API_CreateKxVolume_ResponseSyntax) **   <a name="finspace-CreateKxVolume-response-nas1Configuration"></a>
 Specifies the configuration for the Network attached storage (NAS\_1) file system volume.
Type: [KxNAS1Configuration](API_KxNAS1Configuration.md) object

 ** [status](#API_CreateKxVolume_ResponseSyntax) **   <a name="finspace-CreateKxVolume-response-status"></a>
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

 ** [statusReason](#API_CreateKxVolume_ResponseSyntax) **   <a name="finspace-CreateKxVolume-response-statusReason"></a>
The error message when a failed state occurs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `^[a-zA-Z0-9\_\-\.\s]+$`

 ** [volumeArn](#API_CreateKxVolume_ResponseSyntax) **   <a name="finspace-CreateKxVolume-response-volumeArn"></a>
 The ARN identifier of the volume.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws:finspace:[A-Za-z0-9_/.-]{0,63}:\d+:kxEnvironment/[0-9A-Za-z_-]{1,128}(/kxSharedVolume/[a-zA-Z0-9_-]{1,255})?$`

 ** [volumeName](#API_CreateKxVolume_ResponseSyntax) **   <a name="finspace-CreateKxVolume-response-volumeName"></a>
A unique identifier for the volume.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`

 ** [volumeType](#API_CreateKxVolume_ResponseSyntax) **   <a name="finspace-CreateKxVolume-response-volumeType"></a>
 The type of file system volume. Currently, FinSpace only supports `NAS_1` volume type.
Type: String
Valid Values: `NAS_1`

## Errors
<a name="API_CreateKxVolume_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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

 ** ResourceAlreadyExistsException **
The specified resource group already exists.
HTTP Status Code: 409

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
<a name="API_CreateKxVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2021-03-12/CreateKxVolume)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2021-03-12/CreateKxVolume)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/CreateKxVolume)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2021-03-12/CreateKxVolume)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/CreateKxVolume)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2021-03-12/CreateKxVolume)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2021-03-12/CreateKxVolume)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2021-03-12/CreateKxVolume)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/finspace-2021-03-12/CreateKxVolume)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/CreateKxVolume)
