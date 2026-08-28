---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateWorker.html
---

# CreateWorker
<a name="API_CreateWorker"></a>

Creates a worker. A worker tells your instance how much processing power (vCPU), and memory (GiB) you’ll need to assemble the digital assets held within a particular instance. You can specify certain instance types to use, or let the worker know which instances types to exclude.

 Deadline Cloud limits the number of workers to less than or equal to the fleet's maximum worker count. The service maintains eventual consistency for the worker count. If you make multiple rapid calls to `CreateWorker` before the field updates, you might exceed your fleet's maximum worker count. For example, if your `maxWorkerCount` is 10 and you currently have 9 workers, making two quick `CreateWorker` calls might successfully create 2 workers instead of 1, resulting in 11 total workers.

## Request Syntax
<a name="API_CreateWorker_RequestSyntax"></a>

```
POST /2023-10-12/farms/{{farmId}}/fleets/{{fleetId}}/workers HTTP/1.1
X-Amz-Client-Token: {{clientToken}}
Content-type: application/json

{
   "hostProperties": {
      "hostName": "{{string}}",
      "ipAddresses": {
         "ipV4Addresses": [ "{{string}}" ],
         "ipV6Addresses": [ "{{string}}" ]
      }
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateWorker_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_CreateWorker_RequestSyntax) **   <a name="deadlinecloud-CreateWorker-request-clientToken"></a>
The unique token which the server uses to recognize retries of the same request.
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [farmId](#API_CreateWorker_RequestSyntax) **   <a name="deadlinecloud-CreateWorker-request-uri-farmId"></a>
The farm ID of the farm to connect to the worker.
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** [fleetId](#API_CreateWorker_RequestSyntax) **   <a name="deadlinecloud-CreateWorker-request-uri-fleetId"></a>
The fleet ID to connect to the worker.
Pattern: `fleet-[0-9a-f]{32}`
Required: Yes

## Request Body
<a name="API_CreateWorker_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [hostProperties](#API_CreateWorker_RequestSyntax) **   <a name="deadlinecloud-CreateWorker-request-hostProperties"></a>
The IP address and host name of the worker.
Type: [HostPropertiesRequest](API_HostPropertiesRequest.md) object
Required: No

 ** [tags](#API_CreateWorker_RequestSyntax) **   <a name="deadlinecloud-CreateWorker-request-tags"></a>
Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.
Type: String to string map
Required: No

## Response Syntax
<a name="API_CreateWorker_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "workerId": "string"
}
```

## Response Elements
<a name="API_CreateWorker_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [workerId](#API_CreateWorker_ResponseSyntax) **   <a name="deadlinecloud-CreateWorker-response-workerId"></a>
The worker ID.
Type: String
Pattern: `worker-[0-9a-f]{32}`

## Errors
<a name="API_CreateWorker_Errors"></a>

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
<a name="API_CreateWorker_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/CreateWorker)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/deadline-2023-10-12/CreateWorker)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/CreateWorker)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/CreateWorker)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/CreateWorker)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/CreateWorker)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/CreateWorker)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/CreateWorker)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/CreateWorker)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/CreateWorker)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
