---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetFarm.html
---

# GetFarm
<a name="API_GetFarm"></a>

Get a farm.

## Request Syntax
<a name="API_GetFarm_RequestSyntax"></a>

```
GET /2023-10-12/farms/{{farmId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetFarm_RequestParameters"></a>

The request uses the following URI parameters.

 ** [farmId](#API_GetFarm_RequestSyntax) **   <a name="deadlinecloud-GetFarm-request-uri-farmId"></a>
The farm ID of the farm.
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

## Request Body
<a name="API_GetFarm_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetFarm_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "costScaleFactor": number,
   "createdAt": "string",
   "createdBy": "string",
   "description": "string",
   "displayName": "string",
   "farmId": "string",
   "kmsKeyArn": "string",
   "updatedAt": "string",
   "updatedBy": "string"
}
```

## Response Elements
<a name="API_GetFarm_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [costScaleFactor](#API_GetFarm_ResponseSyntax) **   <a name="deadlinecloud-GetFarm-response-costScaleFactor"></a>
A multiplier applied to the farm's calculated costs for usage data and budget tracking. A value less than 1 represents a discount, a value greater than 1 represents a premium, and a value of 1 represents no adjustment.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.

 ** [createdAt](#API_GetFarm_ResponseSyntax) **   <a name="deadlinecloud-GetFarm-response-createdAt"></a>
The date and time the resource was created.
Type: Timestamp

 ** [createdBy](#API_GetFarm_ResponseSyntax) **   <a name="deadlinecloud-GetFarm-response-createdBy"></a>
The user or system that created this resource.
Type: String

 ** [description](#API_GetFarm_ResponseSyntax) **   <a name="deadlinecloud-GetFarm-response-description"></a>
The description of the farm.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.

 ** [displayName](#API_GetFarm_ResponseSyntax) **   <a name="deadlinecloud-GetFarm-response-displayName"></a>
The display name of the farm.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [farmId](#API_GetFarm_ResponseSyntax) **   <a name="deadlinecloud-GetFarm-response-farmId"></a>
The farm ID of the farm to get.
Type: String
Pattern: `farm-[0-9a-f]{32}`

 ** [kmsKeyArn](#API_GetFarm_ResponseSyntax) **   <a name="deadlinecloud-GetFarm-response-kmsKeyArn"></a>
The ARN of the KMS key used on the farm.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):kms:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}:\d{12}:key/[\w-]{1,120}`

 ** [updatedAt](#API_GetFarm_ResponseSyntax) **   <a name="deadlinecloud-GetFarm-response-updatedAt"></a>
The date and time the resource was updated.
Type: Timestamp

 ** [updatedBy](#API_GetFarm_ResponseSyntax) **   <a name="deadlinecloud-GetFarm-response-updatedBy"></a>
The user or system that updated this resource.
Type: String

## Errors
<a name="API_GetFarm_Errors"></a>

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
<a name="API_GetFarm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetFarm)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/deadline-2023-10-12/GetFarm)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetFarm)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetFarm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetFarm)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetFarm)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetFarm)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetFarm)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetFarm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetFarm)
