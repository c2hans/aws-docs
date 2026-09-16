---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_CreateEnvironment.html
---

# CreateEnvironment
<a name="API_CreateEnvironment"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Creates a runtime environment for a given runtime engine.

## Request Syntax
<a name="API_CreateEnvironment_RequestSyntax"></a>

```
POST /environments HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "engineType": "{{string}}",
   "engineVersion": "{{string}}",
   "highAvailabilityConfig": {
      "desiredCapacity": {{number}}
   },
   "instanceType": "{{string}}",
   "kmsKeyId": "{{string}}",
   "name": "{{string}}",
   "networkType": "{{string}}",
   "preferredMaintenanceWindow": "{{string}}",
   "publiclyAccessible": {{boolean}},
   "securityGroupIds": [ "{{string}}" ],
   "storageConfigurations": [
      { ... }
   ],
   "subnetIds": [ "{{string}}" ],
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateEnvironment_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateEnvironment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateEnvironment_RequestSyntax) **   <a name="m2-CreateEnvironment-request-clientToken"></a>
Unique, case-sensitive identifier you provide to ensure the idempotency of the request to create an environment. The service generates the clientToken when the API call is triggered. The token expires after one hour, so if you retry the API within this timeframe with the same clientToken, you will get the same response. The service also handles deleting the clientToken after it expires.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[!-~]+`
Required: No

 ** [description](#API_CreateEnvironment_RequestSyntax) **   <a name="m2-CreateEnvironment-request-description"></a>
The description of the runtime environment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [engineType](#API_CreateEnvironment_RequestSyntax) **   <a name="m2-CreateEnvironment-request-engineType"></a>
The engine type for the runtime environment.
Type: String
Valid Values: `microfocus | bluage`
Required: Yes

 ** [engineVersion](#API_CreateEnvironment_RequestSyntax) **   <a name="m2-CreateEnvironment-request-engineVersion"></a>
The version of the engine type for the runtime environment.
Type: String
Pattern: `\S{1,10}`
Required: No

 ** [highAvailabilityConfig](#API_CreateEnvironment_RequestSyntax) **   <a name="m2-CreateEnvironment-request-highAvailabilityConfig"></a>
The details of a high availability configuration for this runtime environment.
Type: [HighAvailabilityConfig](API_HighAvailabilityConfig.md) object
Required: No

 ** [instanceType](#API_CreateEnvironment_RequestSyntax) **   <a name="m2-CreateEnvironment-request-instanceType"></a>
The type of instance for the runtime environment.
Type: String
Pattern: `\S{1,20}`
Required: Yes

 ** [kmsKeyId](#API_CreateEnvironment_RequestSyntax) **   <a name="m2-CreateEnvironment-request-kmsKeyId"></a>
The identifier of a customer managed key.
Type: String
Required: No

 ** [name](#API_CreateEnvironment_RequestSyntax) **   <a name="m2-CreateEnvironment-request-name"></a>
The name of the runtime environment. Must be unique within the account.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: Yes

 ** [networkType](#API_CreateEnvironment_RequestSyntax) **   <a name="m2-CreateEnvironment-request-networkType"></a>
The network type required for the runtime environment.
Type: String
Valid Values: `ipv4 | dual`
Required: No

 ** [preferredMaintenanceWindow](#API_CreateEnvironment_RequestSyntax) **   <a name="m2-CreateEnvironment-request-preferredMaintenanceWindow"></a>
Configures the maintenance window that you want for the runtime environment. The maintenance window must have the format `ddd:hh24:mi-ddd:hh24:mi` and must be less than 24 hours. The following two examples are valid maintenance windows: `sun:23:45-mon:00:15` or `sat:01:00-sat:03:00`.
If you do not provide a value, a random system-generated value will be assigned.
Type: String
Pattern: `\S{1,50}`
Required: No

 ** [publiclyAccessible](#API_CreateEnvironment_RequestSyntax) **   <a name="m2-CreateEnvironment-request-publiclyAccessible"></a>
Specifies whether the runtime environment is publicly accessible.
Type: Boolean
Required: No

 ** [securityGroupIds](#API_CreateEnvironment_RequestSyntax) **   <a name="m2-CreateEnvironment-request-securityGroupIds"></a>
The list of security groups for the VPC associated with this runtime environment.
Type: Array of strings
Pattern: `\S{1,50}`
Required: No

 ** [storageConfigurations](#API_CreateEnvironment_RequestSyntax) **   <a name="m2-CreateEnvironment-request-storageConfigurations"></a>
Optional. The storage configurations for this runtime environment.
Type: Array of [StorageConfiguration](API_StorageConfiguration.md) objects
Required: No

 ** [subnetIds](#API_CreateEnvironment_RequestSyntax) **   <a name="m2-CreateEnvironment-request-subnetIds"></a>
The list of subnets associated with the VPC for this runtime environment.
Type: Array of strings
Pattern: `\S{1,50}`
Required: No

 ** [tags](#API_CreateEnvironment_RequestSyntax) **   <a name="m2-CreateEnvironment-request-tags"></a>
The tags for the runtime environment.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:).+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateEnvironment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "environmentId": "string"
}
```

## Response Elements
<a name="API_CreateEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environmentId](#API_CreateEnvironment_ResponseSyntax) **   <a name="m2-CreateEnvironment-response-environmentId"></a>
The unique identifier of the runtime environment.
Type: String
Pattern: `\S{1,80}`

## Errors
<a name="API_CreateEnvironment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The account or role doesn't have the right permissions to make the request.
HTTP Status Code: 403

 ** ConflictException **
The parameters provided in the request conflict with existing resources.
 ** resourceId **
The ID of the conflicting resource.
 ** resourceType **
The type of the conflicting resource.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred during the processing of the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).
One or more quotas for AWS Mainframe Modernization exceeds the limit.
 ** quotaCode **
The identifier of the exceeded quota.
 ** resourceId **
The ID of the resource that is exceeding the quota limit.
 ** resourceType **
The type of resource that is exceeding the quota limit for AWS Mainframe Modernization.
 ** serviceCode **
A code that identifies the service that the exceeded quota belongs to.
HTTP Status Code: 402

 ** ThrottlingException **
The number of requests made exceeds the limit.
 ** quotaCode **
The identifier of the throttled request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
 ** serviceCode **
The identifier of the service that the throttled request was made to.
HTTP Status Code: 429

 ** ValidationException **
One or more parameters provided in the request is not valid.
 ** fieldList **
The list of fields that failed service validation.
 ** reason **
The reason why it failed service validation.
HTTP Status Code: 400

## See Also
<a name="API_CreateEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/m2-2021-04-28/CreateEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/m2-2021-04-28/CreateEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/CreateEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/m2-2021-04-28/CreateEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/CreateEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/m2-2021-04-28/CreateEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/m2-2021-04-28/CreateEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/m2-2021-04-28/CreateEnvironment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/m2-2021-04-28/CreateEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/CreateEnvironment)
