---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_UpdateApplication.html
---

# UpdateApplication
<a name="API_app-registry_UpdateApplication"></a>

**Note**
 AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

Updates an existing application with new attributes.

## Request Syntax
<a name="API_app-registry_UpdateApplication_RequestSyntax"></a>

```
PATCH /applications/{{application}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_app-registry_UpdateApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [application](#API_app-registry_UpdateApplication_RequestSyntax) **   <a name="servicecatalog-app-registry_UpdateApplication-request-uri-application"></a>
 The name, ID, or ARN of the application that will be updated.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `([-.\w]+)|(arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[-.\w]+)`
Required: Yes

## Request Body
<a name="API_app-registry_UpdateApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_app-registry_UpdateApplication_RequestSyntax) **   <a name="servicecatalog-app-registry_UpdateApplication-request-description"></a>
The new description of the application.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** [name](#API_app-registry_UpdateApplication_RequestSyntax) **   <a name="servicecatalog-app-registry_UpdateApplication-request-name"></a>
Deprecated: The new name of the application. The name must be unique in the region in which you are updating the application. Please do not use this field as we have stopped supporting name updates.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-.\w]+`
Required: No

## Response Syntax
<a name="API_app-registry_UpdateApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_app-registry_UpdateApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [application](#API_app-registry_UpdateApplication_ResponseSyntax) **   <a name="servicecatalog-app-registry_UpdateApplication-response-application"></a>
The updated information of the application.
Type: [Application](API_app-registry_Application.md) object

## Errors
<a name="API_app-registry_UpdateApplication_Errors"></a>

 ** ConflictException **
There was a conflict when processing the request (for example, a resource with the given name already exists within the account).
HTTP Status Code: 409

 ** InternalServerException **
The service is experiencing internal problems.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

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
<a name="API_app-registry_UpdateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/AWS242AppRegistry-2020-06-24/UpdateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/UpdateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWS242AppRegistry-2020-06-24/UpdateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/UpdateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/UpdateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/UpdateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/UpdateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/UpdateApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/AWS242AppRegistry-2020-06-24/UpdateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/UpdateApplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
