---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_GetPackageConfiguration.html
---

# GetPackageConfiguration
<a name="API_GetPackageConfiguration"></a>

Gets information about the specified software package's configuration.

Requires permission to access the [GetPackageConfiguration](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_GetPackageConfiguration_RequestSyntax"></a>

```
GET /package-configuration HTTP/1.1
```

## URI Request Parameters
<a name="API_GetPackageConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetPackageConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetPackageConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "versionUpdateByJobsConfig": {
      "enabled": boolean,
      "roleArn": "string"
   }
}
```

## Response Elements
<a name="API_GetPackageConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [versionUpdateByJobsConfig](#API_GetPackageConfiguration_ResponseSyntax) **   <a name="iot-GetPackageConfiguration-response-versionUpdateByJobsConfig"></a>
The version that is associated to a specific job.
Type: [VersionUpdateByJobsConfig](API_VersionUpdateByJobsConfig.md) object

## Errors
<a name="API_GetPackageConfiguration_Errors"></a>

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_GetPackageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/GetPackageConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/GetPackageConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/GetPackageConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/GetPackageConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/GetPackageConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/GetPackageConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/GetPackageConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/GetPackageConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/GetPackageConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/GetPackageConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
