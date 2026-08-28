---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetLifecycleExecution.html
---

# GetLifecycleExecution
<a name="API_GetLifecycleExecution"></a>

Get the runtime information that was logged for a specific runtime instance of the lifecycle policy.

## Request Syntax
<a name="API_GetLifecycleExecution_RequestSyntax"></a>

```
GET /GetLifecycleExecution?lifecycleExecutionId={{lifecycleExecutionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetLifecycleExecution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [lifecycleExecutionId](#API_GetLifecycleExecution_RequestSyntax) **   <a name="imagebuilder-GetLifecycleExecution-request-uri-lifecycleExecutionId"></a>
Use the unique identifier for a runtime instance of the lifecycle policy to get runtime details.
Pattern: `^lce-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
Required: Yes

## Request Body
<a name="API_GetLifecycleExecution_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetLifecycleExecution_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "lifecycleExecution": {
      "endTime": number,
      "lifecycleExecutionId": "string",
      "lifecyclePolicyArn": "string",
      "resourcesImpactedSummary": {
         "hasImpactedResources": boolean
      },
      "startTime": number,
      "state": {
         "reason": "string",
         "status": "string"
      }
   }
}
```

## Response Elements
<a name="API_GetLifecycleExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [lifecycleExecution](#API_GetLifecycleExecution_ResponseSyntax) **   <a name="imagebuilder-GetLifecycleExecution-response-lifecycleExecution"></a>
Runtime details for the specified runtime instance of the lifecycle policy.
Type: [LifecycleExecution](API_LifecycleExecution.md) object

## Errors
<a name="API_GetLifecycleExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the specific operation.
HTTP Status Code: 429

 ** ClientException **
These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InvalidRequestException **
You have requested an action that that the service doesn't support.
HTTP Status Code: 400

 ** ServiceException **
This exception is thrown when the service encounters an unrecoverable exception.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## See Also
<a name="API_GetLifecycleExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/GetLifecycleExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/GetLifecycleExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/GetLifecycleExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/GetLifecycleExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/GetLifecycleExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/GetLifecycleExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/GetLifecycleExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/GetLifecycleExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/GetLifecycleExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/GetLifecycleExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
