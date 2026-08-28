---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CreateConnector.html
---

# CreateConnector
<a name="API_CreateConnector"></a>

Creates a connector that links an external cloud provider to Amazon Inspector for vulnerability scanning.

## Request Syntax
<a name="API_CreateConnector_RequestSyntax"></a>

```
POST /connector/create HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "provider": "{{string}}",
   "providerDetail": { ... },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateConnector_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateConnector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateConnector_RequestSyntax) **   <a name="inspector2-CreateConnector-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request but does not return an error.
Type: String
Required: No

 ** [description](#API_CreateConnector_RequestSyntax) **   <a name="inspector2-CreateConnector-request-description"></a>
A description of the connector.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `[^\p{C}]*`
Required: No

 ** [name](#API_CreateConnector_RequestSyntax) **   <a name="inspector2-CreateConnector-request-name"></a>
The name of the connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[\p{L}\p{N}_-]+`
Required: Yes

 ** [provider](#API_CreateConnector_RequestSyntax) **   <a name="inspector2-CreateConnector-request-provider"></a>
The cloud provider for the connector.
Type: String
Valid Values: `AZURE`
Required: Yes

 ** [providerDetail](#API_CreateConnector_RequestSyntax) **   <a name="inspector2-CreateConnector-request-providerDetail"></a>
The provider-specific configuration details for the connector.
Type: [ProviderDetailCreate](API_ProviderDetailCreate.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [tags](#API_CreateConnector_RequestSyntax) **   <a name="inspector2-CreateConnector-request-tags"></a>
The tags to apply to the connector.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateConnector_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "connectorArn": "string"
}
```

## Response Elements
<a name="API_CreateConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [connectorArn](#API_CreateConnector_ResponseSyntax) **   <a name="inspector2-CreateConnector-response-connectorArn"></a>
The Amazon Resource Name (ARN) of the created connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws(-[a-z]+)*:inspector2:[a-z0-9-]+:[0-9]{12}:connector/([a-f0-9-]+|aws-service-connector/.+/[a-f0-9-]+)`

## Errors
<a name="API_CreateConnector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 For `Enable`, you receive this error if you attempt to use a feature in an unsupported AWS Region.
HTTP Status Code: 403

 ** ConflictException **
A conflict occurred. This exception occurs when the same resource is being modified by concurrent requests.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed due to an internal failure of the Amazon Inspector service.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
You have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use Service Quotas to request a service quota increase.
 ** resourceId **
The ID of the resource that exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation due to missing required fields or having invalid inputs.
 ** fields **
The fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_CreateConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/CreateConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/CreateConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CreateConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/CreateConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CreateConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/CreateConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/CreateConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/CreateConnector)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/CreateConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CreateConnector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
