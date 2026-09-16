---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_GetEnvironment.html
---

# GetEnvironment
<a name="API_GetEnvironment"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Describes a specific runtime environment.

## Request Syntax
<a name="API_GetEnvironment_RequestSyntax"></a>

```
GET /environments/{{environmentId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEnvironment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [environmentId](#API_GetEnvironment_RequestSyntax) **   <a name="m2-GetEnvironment-request-uri-environmentId"></a>
The unique identifier of the runtime environment.
Pattern: `\S{1,80}`
Required: Yes

## Request Body
<a name="API_GetEnvironment_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEnvironment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "actualCapacity": number,
   "creationTime": number,
   "description": "string",
   "engineType": "string",
   "engineVersion": "string",
   "environmentArn": "string",
   "environmentId": "string",
   "highAvailabilityConfig": {
      "desiredCapacity": number
   },
   "instanceType": "string",
   "kmsKeyId": "string",
   "loadBalancerArn": "string",
   "name": "string",
   "networkType": "string",
   "pendingMaintenance": {
      "engineVersion": "string",
      "schedule": {
         "endTime": number,
         "startTime": number
      }
   },
   "preferredMaintenanceWindow": "string",
   "publiclyAccessible": boolean,
   "securityGroupIds": [ "string" ],
   "status": "string",
   "statusReason": "string",
   "storageConfigurations": [
      { ... }
   ],
   "subnetIds": [ "string" ],
   "tags": {
      "string" : "string"
   },
   "vpcId": "string"
}
```

## Response Elements
<a name="API_GetEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actualCapacity](#API_GetEnvironment_ResponseSyntax) **   <a name="m2-GetEnvironment-response-actualCapacity"></a>
The number of instances included in the runtime environment. A standalone runtime environment has a maximum of one instance. Currently, a high availability runtime environment has a maximum of two instances.
Type: Integer

 ** [creationTime](#API_GetEnvironment_ResponseSyntax) **   <a name="m2-GetEnvironment-response-creationTime"></a>
The timestamp when the runtime environment was created.
Type: Timestamp

 ** [description](#API_GetEnvironment_ResponseSyntax) **   <a name="m2-GetEnvironment-response-description"></a>
The description of the runtime environment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [engineType](#API_GetEnvironment_ResponseSyntax) **   <a name="m2-GetEnvironment-response-engineType"></a>
The target platform for the runtime environment.
Type: String
Valid Values: `microfocus | bluage`

 ** [engineVersion](#API_GetEnvironment_ResponseSyntax) **   <a name="m2-GetEnvironment-response-engineVersion"></a>
The version of the runtime engine.
Type: String
Pattern: `\S{1,10}`

 ** [environmentArn](#API_GetEnvironment_ResponseSyntax) **   <a name="m2-GetEnvironment-response-environmentArn"></a>
The Amazon Resource Name (ARN) of the runtime environment.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]|):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+=,@.-]{0,1023}`

 ** [environmentId](#API_GetEnvironment_ResponseSyntax) **   <a name="m2-GetEnvironment-response-environmentId"></a>
The unique identifier of the runtime environment.
Type: String
Pattern: `\S{1,80}`

 ** [highAvailabilityConfig](#API_GetEnvironment_ResponseSyntax) **   <a name="m2-GetEnvironment-response-highAvailabilityConfig"></a>
The desired capacity of the high availability configuration for the runtime environment.
Type: [HighAvailabilityConfig](API_HighAvailabilityConfig.md) object

 ** [instanceType](#API_GetEnvironment_ResponseSyntax) **   <a name="m2-GetEnvironment-response-instanceType"></a>
The type of instance underlying the runtime environment.
Type: String
Pattern: `\S{1,20}`

 ** [kmsKeyId](#API_GetEnvironment_ResponseSyntax) **   <a name="m2-GetEnvironment-response-kmsKeyId"></a>
The identifier of a customer managed key.
Type: String

 ** [loadBalancerArn](#API_GetEnvironment_ResponseSyntax) **   <a name="m2-GetEnvironment-response-loadBalancerArn"></a>
The Amazon Resource Name (ARN) for the load balancer used with the runtime environment.
Type: String

 ** [name](#API_GetEnvironment_ResponseSyntax) **   <a name="m2-GetEnvironment-response-name"></a>
The name of the runtime environment. Must be unique within the account.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`

 ** [networkType](#API_GetEnvironment_ResponseSyntax) **   <a name="m2-GetEnvironment-response-networkType"></a>
The network type supported by the runtime environment.
Type: String
Valid Values: `ipv4 | dual`

 ** [pendingMaintenance](#API_GetEnvironment_ResponseSyntax) **   <a name="m2-GetEnvironment-response-pendingMaintenance"></a>
Indicates the pending maintenance scheduled on this environment.
Type: [PendingMaintenance](API_PendingMaintenance.md) object

 ** [preferredMaintenanceWindow](#API_GetEnvironment_ResponseSyntax) **   <a name="m2-GetEnvironment-response-preferredMaintenanceWindow"></a>
The maintenance window for the runtime environment. If you don't provide a value for the maintenance window, the service assigns a random value.
Type: String
Pattern: `\S{1,50}`

 ** [publiclyAccessible](#API_GetEnvironment_ResponseSyntax) **   <a name="m2-GetEnvironment-response-publiclyAccessible"></a>
Whether applications running in this runtime environment are publicly accessible.
Type: Boolean

 ** [securityGroupIds](#API_GetEnvironment_ResponseSyntax) **   <a name="m2-GetEnvironment-response-securityGroupIds"></a>
The unique identifiers of the security groups assigned to this runtime environment.
Type: Array of strings
Pattern: `\S{1,50}`

 ** [status](#API_GetEnvironment_ResponseSyntax) **   <a name="m2-GetEnvironment-response-status"></a>
The status of the runtime environment. If the AWS Mainframe Modernization environment is missing a connection to the customer owned dependent resource, the status will be `Unhealthy`.
Type: String
Valid Values: `Creating | Available | Updating | Deleting | Failed | UnHealthy`

 ** [statusReason](#API_GetEnvironment_ResponseSyntax) **   <a name="m2-GetEnvironment-response-statusReason"></a>
The reason for the reported status.
Type: String

 ** [storageConfigurations](#API_GetEnvironment_ResponseSyntax) **   <a name="m2-GetEnvironment-response-storageConfigurations"></a>
The storage configurations defined for the runtime environment.
Type: Array of [StorageConfiguration](API_StorageConfiguration.md) objects

 ** [subnetIds](#API_GetEnvironment_ResponseSyntax) **   <a name="m2-GetEnvironment-response-subnetIds"></a>
The unique identifiers of the subnets assigned to this runtime environment.
Type: Array of strings
Pattern: `\S{1,50}`

 ** [tags](#API_GetEnvironment_ResponseSyntax) **   <a name="m2-GetEnvironment-response-tags"></a>
The tags defined for this runtime environment.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:).+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [vpcId](#API_GetEnvironment_ResponseSyntax) **   <a name="m2-GetEnvironment-response-vpcId"></a>
The unique identifier for the VPC used with this runtime environment.
Type: String
Pattern: `\S{1,50}`

## Errors
<a name="API_GetEnvironment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The account or role doesn't have the right permissions to make the request.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred during the processing of the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
 ** resourceId **
The ID of the missing resource.
 ** resourceType **
The type of the missing resource.
HTTP Status Code: 404

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
<a name="API_GetEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/m2-2021-04-28/GetEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/m2-2021-04-28/GetEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/GetEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/m2-2021-04-28/GetEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/GetEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/m2-2021-04-28/GetEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/m2-2021-04-28/GetEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/m2-2021-04-28/GetEnvironment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/m2-2021-04-28/GetEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/GetEnvironment)
