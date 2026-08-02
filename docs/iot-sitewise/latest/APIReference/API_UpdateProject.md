---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateProject.html
---

# UpdateProject
<a name="API_UpdateProject"></a>

**Important**
The AWS IoT SiteWise Monitor feature will no longer be open to new customers starting November 7, 2025 . If you would like to use the AWS IoT SiteWise Monitor feature, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS IoT SiteWise Monitor availability change](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html).

Updates an AWS IoT SiteWise Monitor project.

## Request Syntax
<a name="API_UpdateProject_RequestSyntax"></a>

```
PUT /projects/{{projectId}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "projectDescription": "{{string}}",
   "projectName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateProject_RequestParameters"></a>

The request uses the following URI parameters.

 ** [projectId](#API_UpdateProject_RequestSyntax) **   <a name="iotsitewise-UpdateProject-request-uri-projectId"></a>
The ID of the project to update.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

## Request Body
<a name="API_UpdateProject_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateProject_RequestSyntax) **   <a name="iotsitewise-UpdateProject-request-clientToken"></a>
A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`
Required: No

 ** [projectDescription](#API_UpdateProject_RequestSyntax) **   <a name="iotsitewise-UpdateProject-request-projectDescription"></a>
A new description for the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** [projectName](#API_UpdateProject_RequestSyntax) **   <a name="iotsitewise-UpdateProject-request-projectName"></a>
A new friendly name for the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

## Response Syntax
<a name="API_UpdateProject_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateProject_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_UpdateProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/UpdateProject)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/UpdateProject)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/UpdateProject)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/UpdateProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/UpdateProject)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/UpdateProject)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/UpdateProject)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/UpdateProject)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/UpdateProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/UpdateProject)
