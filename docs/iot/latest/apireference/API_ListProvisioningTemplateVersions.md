---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListProvisioningTemplateVersions.html
---

# ListProvisioningTemplateVersions
<a name="API_ListProvisioningTemplateVersions"></a>

A list of provisioning template versions.

Requires permission to access the [ListProvisioningTemplateVersions](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListProvisioningTemplateVersions_RequestSyntax"></a>

```
GET /provisioning-templates/{{templateName}}/versions?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListProvisioningTemplateVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListProvisioningTemplateVersions_RequestSyntax) **   <a name="iot-ListProvisioningTemplateVersions-request-uri-maxResults"></a>
The maximum number of results to return at one time.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListProvisioningTemplateVersions_RequestSyntax) **   <a name="iot-ListProvisioningTemplateVersions-request-uri-nextToken"></a>
A token to retrieve the next set of results.

 ** [templateName](#API_ListProvisioningTemplateVersions_RequestSyntax) **   <a name="iot-ListProvisioningTemplateVersions-request-uri-templateName"></a>
The name of the provisioning template.
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9A-Za-z_-]+$`
Required: Yes

## Request Body
<a name="API_ListProvisioningTemplateVersions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListProvisioningTemplateVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "versions": [
      {
         "creationDate": number,
         "isDefaultVersion": boolean,
         "versionId": number
      }
   ]
}
```

## Response Elements
<a name="API_ListProvisioningTemplateVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListProvisioningTemplateVersions_ResponseSyntax) **   <a name="iot-ListProvisioningTemplateVersions-response-nextToken"></a>
A token to retrieve the next set of results.
Type: String

 ** [versions](#API_ListProvisioningTemplateVersions_ResponseSyntax) **   <a name="iot-ListProvisioningTemplateVersions-response-versions"></a>
The list of provisioning template versions.
Type: Array of [ProvisioningTemplateVersionSummary](API_ProvisioningTemplateVersionSummary.md) objects

## Errors
<a name="API_ListProvisioningTemplateVersions_Errors"></a>

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
<a name="API_ListProvisioningTemplateVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListProvisioningTemplateVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListProvisioningTemplateVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListProvisioningTemplateVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListProvisioningTemplateVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListProvisioningTemplateVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListProvisioningTemplateVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListProvisioningTemplateVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListProvisioningTemplateVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListProvisioningTemplateVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListProvisioningTemplateVersions)
