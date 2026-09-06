---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateLicenseEndpoint.html
---

# CreateLicenseEndpoint
<a name="API_CreateLicenseEndpoint"></a>

Creates a license endpoint to integrate your various licensed software used for rendering on Deadline Cloud.

## Request Syntax
<a name="API_CreateLicenseEndpoint_RequestSyntax"></a>

```
POST /2023-10-12/license-endpoints HTTP/1.1
X-Amz-Client-Token: {{clientToken}}
Content-type: application/json

{
   "securityGroupIds": [ "{{string}}" ],
   "subnetIds": [ "{{string}}" ],
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "vpcId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateLicenseEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_CreateLicenseEndpoint_RequestSyntax) **   <a name="deadlinecloud-CreateLicenseEndpoint-request-clientToken"></a>
The unique token which the server uses to recognize retries of the same request.
Length Constraints: Minimum length of 1. Maximum length of 64.

## Request Body
<a name="API_CreateLicenseEndpoint_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [securityGroupIds](#API_CreateLicenseEndpoint_RequestSyntax) **   <a name="deadlinecloud-CreateLicenseEndpoint-request-securityGroupIds"></a>
The security group IDs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `sg-[\w]{1,120}`
Required: Yes

 ** [subnetIds](#API_CreateLicenseEndpoint_RequestSyntax) **   <a name="deadlinecloud-CreateLicenseEndpoint-request-subnetIds"></a>
The subnet IDs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `subnet-[\w]{1,120}`
Required: Yes

 ** [tags](#API_CreateLicenseEndpoint_RequestSyntax) **   <a name="deadlinecloud-CreateLicenseEndpoint-request-tags"></a>
Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.
Type: String to string map
Required: No

 ** [vpcId](#API_CreateLicenseEndpoint_RequestSyntax) **   <a name="deadlinecloud-CreateLicenseEndpoint-request-vpcId"></a>
The VPC (virtual private cloud) ID to use with the license endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `vpc-[\w]{1,120}`
Required: Yes

## Response Syntax
<a name="API_CreateLicenseEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "licenseEndpointId": "string"
}
```

## Response Elements
<a name="API_CreateLicenseEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [licenseEndpointId](#API_CreateLicenseEndpoint_ResponseSyntax) **   <a name="deadlinecloud-CreateLicenseEndpoint-response-licenseEndpointId"></a>
The license endpoint ID.
Type: String
Pattern: `le-[0-9a-f]{32}`

## Errors
<a name="API_CreateLicenseEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action.
 ** context **
Information about the resources in use when the exception was thrown.
HTTP Status Code: 403

 ** ConflictException **
Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
 ** context **
Information about the resources in use when the exception was thrown.
 ** reason **
A description of the error.
 ** resourceId **
The identifier of the resource in use.
 ** resourceType **
The type of the resource in use.
HTTP Status Code: 409

 ** InternalServerErrorException **
Deadline Cloud can't process your request right now. Try again later.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
HTTP Status Code: 500

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
<a name="API_CreateLicenseEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/CreateLicenseEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/deadline-2023-10-12/CreateLicenseEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/CreateLicenseEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/CreateLicenseEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/CreateLicenseEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/CreateLicenseEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/CreateLicenseEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/CreateLicenseEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/CreateLicenseEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/CreateLicenseEndpoint)
