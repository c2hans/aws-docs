---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetLifecycleExecution.html
---

# GetLifecycleExecution
<a name="API_GetLifecycleExecution"></a>

Retrieves runtime information for a lifecycle execution – a single run of lifecycle actions that a lifecycle policy or a [StartResourceStateUpdate](API_StartResourceStateUpdate.md) request started.

## Request Syntax
<a name="API_GetLifecycleExecution_RequestSyntax"></a>

```
GET /GetLifecycleExecution?lifecycleExecutionId={{lifecycleExecutionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetLifecycleExecution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [lifecycleExecutionId](#API_GetLifecycleExecution_RequestSyntax) **   <a name="imagebuilder-GetLifecycleExecution-request-uri-lifecycleExecutionId"></a>
The unique identifier for a runtime instance of the lifecycle policy.
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
You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.
HTTP Status Code: 429

 ** ClientException **
A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InvalidRequestException **
The request is malformed or otherwise invalid. Verify the request and try again.
HTTP Status Code: 400

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_GetLifecycleExecution_Examples"></a>

### Get the details of a lifecycle execution
<a name="API_GetLifecycleExecution_Example_1"></a>

The following example retrieves the runtime status of the specified lifecycle execution. If the execution was started by StartResourceStateUpdate rather than a lifecycle policy run, the response doesn't include the lifecyclePolicyArn field.

#### Sample Request
<a name="API_GetLifecycleExecution_Example_1_Request"></a>

```
GET /GetLifecycleExecution?lifecycleExecutionId=lce-401aefc3-a829-46f6-8fc2-91497988a503 HTTP/1.1
```

#### Sample Response
<a name="API_GetLifecycleExecution_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "lifecycleExecution": {
        "lifecycleExecutionId": "lce-401aefc3-a829-46f6-8fc2-91497988a503",
        "resourcesImpactedSummary": {
            "hasImpactedResources": false
        },
        "state": {
            "status": "IN_PROGRESS"
        },
        "startTime": 1788990149.801
    }
}
```

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
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/GetLifecycleExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/GetLifecycleExecution)
