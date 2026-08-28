---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_UpdateEnvironment.html
---

# UpdateEnvironment
<a name="API_UpdateEnvironment"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Updates the configuration details for a specific runtime environment.

## Request Syntax
<a name="API_UpdateEnvironment_RequestSyntax"></a>

```
PATCH /environments/{{environmentId}} HTTP/1.1
Content-type: application/json

{
   "applyDuringMaintenanceWindow": {{boolean}},
   "desiredCapacity": {{number}},
   "engineVersion": "{{string}}",
   "forceUpdate": {{boolean}},
   "instanceType": "{{string}}",
   "preferredMaintenanceWindow": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateEnvironment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [environmentId](#API_UpdateEnvironment_RequestSyntax) **   <a name="m2-UpdateEnvironment-request-uri-environmentId"></a>
The unique identifier of the runtime environment that you want to update.
Pattern: `\S{1,80}`
Required: Yes

## Request Body
<a name="API_UpdateEnvironment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [applyDuringMaintenanceWindow](#API_UpdateEnvironment_RequestSyntax) **   <a name="m2-UpdateEnvironment-request-applyDuringMaintenanceWindow"></a>
Indicates whether to update the runtime environment during the maintenance window. The default is false. Currently, AWS Mainframe Modernization accepts the `engineVersion` parameter only if `applyDuringMaintenanceWindow` is true. If any parameter other than `engineVersion` is provided in `UpdateEnvironmentRequest`, it will fail if `applyDuringMaintenanceWindow` is set to true.
Type: Boolean
Required: No

 ** [desiredCapacity](#API_UpdateEnvironment_RequestSyntax) **   <a name="m2-UpdateEnvironment-request-desiredCapacity"></a>
The desired capacity for the runtime environment to update. The minimum possible value is 0 and the maximum is 100.
Type: Integer
Required: No

 ** [engineVersion](#API_UpdateEnvironment_RequestSyntax) **   <a name="m2-UpdateEnvironment-request-engineVersion"></a>
The version of the runtime engine for the runtime environment.
Type: String
Pattern: `\S{1,10}`
Required: No

 ** [forceUpdate](#API_UpdateEnvironment_RequestSyntax) **   <a name="m2-UpdateEnvironment-request-forceUpdate"></a>
Forces the updates on the environment. This option is needed if the applications in the environment are not stopped or if there are ongoing application-related activities in the environment.
If you use this option, be aware that it could lead to data corruption in the applications, and that you might need to perform repair and recovery procedures for the applications.
This option is not needed if the attribute being updated is `preferredMaintenanceWindow`.
Type: Boolean
Required: No

 ** [instanceType](#API_UpdateEnvironment_RequestSyntax) **   <a name="m2-UpdateEnvironment-request-instanceType"></a>
The instance type for the runtime environment to update.
Type: String
Pattern: `\S{1,20}`
Required: No

 ** [preferredMaintenanceWindow](#API_UpdateEnvironment_RequestSyntax) **   <a name="m2-UpdateEnvironment-request-preferredMaintenanceWindow"></a>
Configures the maintenance window that you want for the runtime environment. The maintenance window must have the format `ddd:hh24:mi-ddd:hh24:mi` and must be less than 24 hours. The following two examples are valid maintenance windows: `sun:23:45-mon:00:15` or `sat:01:00-sat:03:00`.
If you do not provide a value, a random system-generated value will be assigned.
Type: String
Required: No

## Response Syntax
<a name="API_UpdateEnvironment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "environmentId": "string"
}
```

## Response Elements
<a name="API_UpdateEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environmentId](#API_UpdateEnvironment_ResponseSyntax) **   <a name="m2-UpdateEnvironment-response-environmentId"></a>
The unique identifier of the runtime environment that was updated.
Type: String
Pattern: `\S{1,80}`

## Errors
<a name="API_UpdateEnvironment_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource was not found.
 ** resourceId **
The ID of the missing resource.
 ** resourceType **
The type of the missing resource.
HTTP Status Code: 404

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
<a name="API_UpdateEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/m2-2021-04-28/UpdateEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/m2-2021-04-28/UpdateEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/UpdateEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/m2-2021-04-28/UpdateEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/UpdateEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/m2-2021-04-28/UpdateEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/m2-2021-04-28/UpdateEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/m2-2021-04-28/UpdateEnvironment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/m2-2021-04-28/UpdateEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/UpdateEnvironment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Mainframe Modernization. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query m2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
