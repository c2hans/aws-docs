---
source_url: https://docs.aws.amazon.com/lambda/latest/microvm-api/API_GetMicrovmImageBuild.html
---

# GetMicrovmImageBuild
<a name="API_GetMicrovmImageBuild"></a>

Retrieves the details of a specific MicroVM image build, including its state, target architecture, and snapshot information.

## Request Syntax
<a name="API_GetMicrovmImageBuild_RequestSyntax"></a>

```
GET /2025-09-09/microvm-images/{{imageIdentifier}}/versions/{{imageVersion}}/builds/{{buildId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMicrovmImageBuild_RequestParameters"></a>

The request uses the following URI parameters.

 ** [buildId](#API_GetMicrovmImageBuild_RequestSyntax) **   <a name="lambdamicrovm-GetMicrovmImageBuild-request-uri-buildId"></a>
The unique identifier of the build to retrieve.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`
Required: Yes

 ** [imageIdentifier](#API_GetMicrovmImageBuild_RequestSyntax) **   <a name="lambdamicrovm-GetMicrovmImageBuild-request-uri-imageIdentifier"></a>
The unique identifier (ARN or ID) of the MicroVM image.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [imageVersion](#API_GetMicrovmImageBuild_RequestSyntax) **   <a name="lambdamicrovm-GetMicrovmImageBuild-request-uri-imageVersion"></a>
The version of the MicroVM image.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`
Required: Yes

## Request Body
<a name="API_GetMicrovmImageBuild_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMicrovmImageBuild_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "architecture": "string",
   "buildId": "string",
   "buildState": "string",
   "chipset": "string",
   "chipsetGeneration": "string",
   "createdAt": number,
   "imageArn": "string",
   "imageVersion": "string",
   "snapshotBuild": {
      "codeInstallSizeInBytes": number,
      "diskSnapshotSizeInBytes": number,
      "memorySnapshotSizeInBytes": number
   },
   "stateReason": "string"
}
```

## Response Elements
<a name="API_GetMicrovmImageBuild_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [architecture](#API_GetMicrovmImageBuild_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovmImageBuild-response-architecture"></a>
The target CPU architecture for the build. Supported value: ARM\_64.
Type: String
Valid Values: `ARM_64`

 ** [buildId](#API_GetMicrovmImageBuild_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovmImageBuild-response-buildId"></a>
The build request ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [buildState](#API_GetMicrovmImageBuild_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovmImageBuild-response-buildState"></a>
The current state of the build.
Type: String
Valid Values: `PENDING | IN_PROGRESS | SUCCESSFUL | FAILED`

 ** [chipset](#API_GetMicrovmImageBuild_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovmImageBuild-response-chipset"></a>
The target chipset for the build.
Type: String
Valid Values: `GRAVITON`

 ** [chipsetGeneration](#API_GetMicrovmImageBuild_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovmImageBuild-response-chipsetGeneration"></a>
The target chipset generation for the build.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [createdAt](#API_GetMicrovmImageBuild_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovmImageBuild-response-createdAt"></a>
The timestamp when the build was created.
Type: Timestamp

 ** [imageArn](#API_GetMicrovmImageBuild_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovmImageBuild-response-imageArn"></a>
The ARN of the MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [imageVersion](#API_GetMicrovmImageBuild_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovmImageBuild-response-imageVersion"></a>
The version of the MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [snapshotBuild](#API_GetMicrovmImageBuild_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovmImageBuild-response-snapshotBuild"></a>
The snapshot build details, including memory and disk snapshot sizes.
Type: [SnapshotBuild](API_SnapshotBuild.md) object

 ** [stateReason](#API_GetMicrovmImageBuild_ResponseSyntax) **   <a name="lambdamicrovm-GetMicrovmImageBuild-response-stateReason"></a>
The reason for the build state, if applicable.
Type: String

## Errors
<a name="API_GetMicrovmImageBuild_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An internal server error occurred. Retry the request later.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of the resource that was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling. Retry the request later.
 ** quotaCode **
The quota code of the throttled service quota.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
 ** serviceCode **
The service code of the throttled service quota.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_GetMicrovmImageBuild_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-microvms-2025-09-09/GetMicrovmImageBuild)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-microvms-2025-09-09/GetMicrovmImageBuild)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-microvms-2025-09-09/GetMicrovmImageBuild)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-microvms-2025-09-09/GetMicrovmImageBuild)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-microvms-2025-09-09/GetMicrovmImageBuild)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-microvms-2025-09-09/GetMicrovmImageBuild)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-microvms-2025-09-09/GetMicrovmImageBuild)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-microvms-2025-09-09/GetMicrovmImageBuild)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-microvms-2025-09-09/GetMicrovmImageBuild)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-microvms-2025-09-09/GetMicrovmImageBuild)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda MicroVMs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
