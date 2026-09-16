---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateStorageProfile.html
---

# CreateStorageProfile
<a name="API_CreateStorageProfile"></a>

Creates a storage profile that specifies the operating system, file type, and file location of resources used on a farm.

## Request Syntax
<a name="API_CreateStorageProfile_RequestSyntax"></a>

```
POST /2023-10-12/farms/{{farmId}}/storage-profiles HTTP/1.1
X-Amz-Client-Token: {{clientToken}}
Content-type: application/json

{
   "displayName": "{{string}}",
   "fileSystemLocations": [
      {
         "name": "{{string}}",
         "path": "{{string}}",
         "type": "{{string}}"
      }
   ],
   "osFamily": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateStorageProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_CreateStorageProfile_RequestSyntax) **   <a name="deadlinecloud-CreateStorageProfile-request-clientToken"></a>
The unique token which the server uses to recognize retries of the same request.
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [farmId](#API_CreateStorageProfile_RequestSyntax) **   <a name="deadlinecloud-CreateStorageProfile-request-uri-farmId"></a>
The farm ID of the farm to connect to the storage profile.
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

## Request Body
<a name="API_CreateStorageProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [displayName](#API_CreateStorageProfile_RequestSyntax) **   <a name="deadlinecloud-CreateStorageProfile-request-displayName"></a>
The display name of the storage profile.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [fileSystemLocations](#API_CreateStorageProfile_RequestSyntax) **   <a name="deadlinecloud-CreateStorageProfile-request-fileSystemLocations"></a>
File system paths to include in the storage profile.
Type: Array of [FileSystemLocation](API_FileSystemLocation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [osFamily](#API_CreateStorageProfile_RequestSyntax) **   <a name="deadlinecloud-CreateStorageProfile-request-osFamily"></a>
The type of operating system (OS) for the storage profile.
Type: String
Valid Values: `WINDOWS | LINUX | MACOS`
Required: Yes

## Response Syntax
<a name="API_CreateStorageProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "storageProfileId": "string"
}
```

## Response Elements
<a name="API_CreateStorageProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [storageProfileId](#API_CreateStorageProfile_ResponseSyntax) **   <a name="deadlinecloud-CreateStorageProfile-response-storageProfileId"></a>
The storage profile ID.
Type: String
Pattern: `sp-[0-9a-f]{32}`

## Errors
<a name="API_CreateStorageProfile_Errors"></a>

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

 ** ServiceQuotaExceededException **
You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
 ** context **
Information about the resources in use when the exception was thrown.
 ** quotaCode **
Identifies the quota that has been exceeded.
 ** reason **
A string that describes the reason the quota was exceeded.
 ** resourceId **
The identifier of the affected resource.
 ** resourceType **
The type of the affected resource
 ** serviceCode **
Identifies the service that exceeded the quota.
HTTP Status Code: 402

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
<a name="API_CreateStorageProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/CreateStorageProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/deadline-2023-10-12/CreateStorageProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/CreateStorageProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/CreateStorageProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/CreateStorageProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/CreateStorageProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/CreateStorageProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/CreateStorageProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/CreateStorageProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/CreateStorageProfile)
