---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeProvisioningTemplateVersion.html
---

# DescribeProvisioningTemplateVersion
<a name="API_DescribeProvisioningTemplateVersion"></a>

Returns information about a provisioning template version.

Requires permission to access the [DescribeProvisioningTemplateVersion](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DescribeProvisioningTemplateVersion_RequestSyntax"></a>

```
GET /provisioning-templates/{{templateName}}/versions/{{versionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeProvisioningTemplateVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [templateName](#API_DescribeProvisioningTemplateVersion_RequestSyntax) **   <a name="iot-DescribeProvisioningTemplateVersion-request-uri-templateName"></a>
The template name.
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9A-Za-z_-]+$`
Required: Yes

 ** [versionId](#API_DescribeProvisioningTemplateVersion_RequestSyntax) **   <a name="iot-DescribeProvisioningTemplateVersion-request-uri-versionId"></a>
The provisioning template version ID.
Required: Yes

## Request Body
<a name="API_DescribeProvisioningTemplateVersion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeProvisioningTemplateVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationDate": number,
   "isDefaultVersion": boolean,
   "templateBody": "string",
   "versionId": number
}
```

## Response Elements
<a name="API_DescribeProvisioningTemplateVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationDate](#API_DescribeProvisioningTemplateVersion_ResponseSyntax) **   <a name="iot-DescribeProvisioningTemplateVersion-response-creationDate"></a>
The date when the provisioning template version was created.
Type: Timestamp

 ** [isDefaultVersion](#API_DescribeProvisioningTemplateVersion_ResponseSyntax) **   <a name="iot-DescribeProvisioningTemplateVersion-response-isDefaultVersion"></a>
True if the provisioning template version is the default version.
Type: Boolean

 ** [templateBody](#API_DescribeProvisioningTemplateVersion_ResponseSyntax) **   <a name="iot-DescribeProvisioningTemplateVersion-response-templateBody"></a>
The JSON formatted contents of the provisioning template version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.
Pattern: `[\s\S]*`

 ** [versionId](#API_DescribeProvisioningTemplateVersion_ResponseSyntax) **   <a name="iot-DescribeProvisioningTemplateVersion-response-versionId"></a>
The provisioning template version ID.
Type: Integer

## Errors
<a name="API_DescribeProvisioningTemplateVersion_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_DescribeProvisioningTemplateVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DescribeProvisioningTemplateVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DescribeProvisioningTemplateVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DescribeProvisioningTemplateVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DescribeProvisioningTemplateVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DescribeProvisioningTemplateVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DescribeProvisioningTemplateVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DescribeProvisioningTemplateVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DescribeProvisioningTemplateVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DescribeProvisioningTemplateVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DescribeProvisioningTemplateVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
