---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_CreateApplication.html
---

# CreateApplication
<a name="API_app-registry_CreateApplication"></a>

**Note**
 AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

Creates a new application that is the top-level node in a hierarchy of related cloud resource abstractions.

## Request Syntax
<a name="API_app-registry_CreateApplication_RequestSyntax"></a>

```
POST /applications HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_app-registry_CreateApplication_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_app-registry_CreateApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_app-registry_CreateApplication_RequestSyntax) **   <a name="servicecatalog-app-registry_CreateApplication-request-clientToken"></a>
A unique identifier that you provide to ensure idempotency. If you retry a request that completed successfully using the same client token and the same parameters, the retry succeeds without performing any further actions. If you retry a successful request using the same client token, but one or more of the parameters are different, the retry fails.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: Yes

 ** [description](#API_app-registry_CreateApplication_RequestSyntax) **   <a name="servicecatalog-app-registry_CreateApplication-request-description"></a>
The description of the application.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** [name](#API_app-registry_CreateApplication_RequestSyntax) **   <a name="servicecatalog-app-registry_CreateApplication-request-name"></a>
The name of the application. The name must be unique in the region in which you are creating the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-.\w]+`
Required: Yes

 ** [tags](#API_app-registry_CreateApplication_RequestSyntax) **   <a name="servicecatalog-app-registry_CreateApplication-request-tags"></a>
Key-value pairs you can use to associate with the application.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
Required: No

## Response Syntax
<a name="API_app-registry_CreateApplication_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "application": {
      "applicationTag": {
         "string" : "string"
      },
      "arn": "string",
      "creationTime": "string",
      "description": "string",
      "id": "string",
      "lastUpdateTime": "string",
      "name": "string",
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_app-registry_CreateApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [application](#API_app-registry_CreateApplication_ResponseSyntax) **   <a name="servicecatalog-app-registry_CreateApplication-response-application"></a>
Information about the application.
Type: [Application](API_app-registry_Application.md) object

## Errors
<a name="API_app-registry_CreateApplication_Errors"></a>

 ** ConflictException **
There was a conflict when processing the request (for example, a resource with the given name already exists within the account).
HTTP Status Code: 409

 ** InternalServerException **
The service is experiencing internal problems.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
 The maximum number of resources per account has been reached.
HTTP Status Code: 402

 ** ThrottlingException **
 The maximum number of API requests has been exceeded.
 ** message **
A message associated with the Throttling exception.
 ** serviceCode **
The originating service code.
HTTP Status Code: 429

 ** ValidationException **
The request has invalid or missing parameters.
HTTP Status Code: 400

## See Also
<a name="API_app-registry_CreateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/AWS242AppRegistry-2020-06-24/CreateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/CreateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWS242AppRegistry-2020-06-24/CreateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/CreateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/CreateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/CreateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/CreateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/CreateApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/AWS242AppRegistry-2020-06-24/CreateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/CreateApplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
