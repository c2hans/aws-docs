---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_UpdateApplication.html
---

# UpdateApplication
<a name="API_UpdateApplication"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Updates an application and creates a new version.

## Request Syntax
<a name="API_UpdateApplication_RequestSyntax"></a>

```
PATCH /applications/{{applicationId}} HTTP/1.1
Content-type: application/json

{
   "currentApplicationVersion": {{number}},
   "definition": { ... },
   "description": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_UpdateApplication_RequestSyntax) **   <a name="m2-UpdateApplication-request-uri-applicationId"></a>
The unique identifier of the application you want to update.
Pattern: `\S{1,80}`
Required: Yes

## Request Body
<a name="API_UpdateApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [currentApplicationVersion](#API_UpdateApplication_RequestSyntax) **   <a name="m2-UpdateApplication-request-currentApplicationVersion"></a>
The current version of the application to update.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** [definition](#API_UpdateApplication_RequestSyntax) **   <a name="m2-UpdateApplication-request-definition"></a>
The application definition for this application. You can specify either inline JSON or an S3 bucket location.
Type: [Definition](API_Definition.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [description](#API_UpdateApplication_RequestSyntax) **   <a name="m2-UpdateApplication-request-description"></a>
The description of the application to update.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

## Response Syntax
<a name="API_UpdateApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationVersion": number
}
```

## Response Elements
<a name="API_UpdateApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationVersion](#API_UpdateApplication_ResponseSyntax) **   <a name="m2-UpdateApplication-response-applicationVersion"></a>
The new version of the application.
Type: Integer
Valid Range: Minimum value of 1.

## Errors
<a name="API_UpdateApplication_Errors"></a>

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
<a name="API_UpdateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/m2-2021-04-28/UpdateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/m2-2021-04-28/UpdateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/UpdateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/m2-2021-04-28/UpdateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/UpdateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/m2-2021-04-28/UpdateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/m2-2021-04-28/UpdateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/m2-2021-04-28/UpdateApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/m2-2021-04-28/UpdateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/UpdateApplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Mainframe Modernization. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query m2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
