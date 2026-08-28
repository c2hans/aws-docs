---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DeletePackage.html
---

# DeletePackage
<a name="API_DeletePackage"></a>

Deletes a specific version from a software package.

 **Note:** All package versions must be deleted before deleting the software package.

Requires permission to access the [DeletePackageVersion](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DeletePackage_RequestSyntax"></a>

```
DELETE /packages/{{packageName}}?clientToken={{clientToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeletePackage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_DeletePackage_RequestSyntax) **   <a name="iot-DeletePackage-request-uri-clientToken"></a>
A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`

 ** [packageName](#API_DeletePackage_RequestSyntax) **   <a name="iot-DeletePackage-request-uri-packageName"></a>
The name of the target software package.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_.]+`
Required: Yes

## Request Body
<a name="API_DeletePackage_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeletePackage_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeletePackage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeletePackage_Errors"></a>

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ValidationException **
The request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DeletePackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DeletePackage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DeletePackage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DeletePackage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DeletePackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DeletePackage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DeletePackage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DeletePackage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DeletePackage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DeletePackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DeletePackage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
