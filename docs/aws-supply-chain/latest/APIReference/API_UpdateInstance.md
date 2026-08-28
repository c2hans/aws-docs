---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_UpdateInstance.html
---

# UpdateInstance
<a name="API_UpdateInstance"></a>

Enables you to programmatically update an AWS Supply Chain instance description by providing all the relevant information such as account ID, instance ID and so on without using the AWS console.

## Request Syntax
<a name="API_UpdateInstance_RequestSyntax"></a>

```
PATCH /api/instance/{{instanceId}} HTTP/1.1
Content-type: application/json

{
   "instanceDescription": "{{string}}",
   "instanceName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateInstance_RequestParameters"></a>

The request uses the following URI parameters.

 ** [instanceId](#API_UpdateInstance_RequestSyntax) **   <a name="supplychain-UpdateInstance-request-uri-instanceId"></a>
The AWS Supply Chain instance identifier.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Request Body
<a name="API_UpdateInstance_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [instanceDescription](#API_UpdateInstance_RequestSyntax) **   <a name="supplychain-UpdateInstance-request-instanceDescription"></a>
The AWS Supply Chain instance description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 501.
Pattern: `([a-zA-Z0-9., _ʼ'%-]){0,500}`
Required: No

 ** [instanceName](#API_UpdateInstance_RequestSyntax) **   <a name="supplychain-UpdateInstance-request-instanceName"></a>
The AWS Supply Chain instance name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `(?![ _ʼ'%-])[a-zA-Z0-9 _ʼ'%-]{0,62}[a-zA-Z0-9]`
Required: No

## Response Syntax
<a name="API_UpdateInstance_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "instance": {
      "awsAccountId": "string",
      "createdTime": number,
      "errorMessage": "string",
      "instanceDescription": "string",
      "instanceId": "string",
      "instanceName": "string",
      "kmsKeyArn": "string",
      "lastModifiedTime": number,
      "state": "string",
      "versionNumber": number,
      "webAppDnsDomain": "string"
   }
}
```

## Response Elements
<a name="API_UpdateInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [instance](#API_UpdateInstance_ResponseSyntax) **   <a name="supplychain-UpdateInstance-response-instance"></a>
The instance resource data details.
Type: [Instance](API_Instance.md) object

## Errors
<a name="API_UpdateInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have the required privileges to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Request would cause a service quota to be exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
Request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/supplychain-2024-01-01/UpdateInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/supplychain-2024-01-01/UpdateInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/UpdateInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/supplychain-2024-01-01/UpdateInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/UpdateInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/supplychain-2024-01-01/UpdateInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/supplychain-2024-01-01/UpdateInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/supplychain-2024-01-01/UpdateInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/supplychain-2024-01-01/UpdateInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/UpdateInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Supply Chain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-supply-chain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
