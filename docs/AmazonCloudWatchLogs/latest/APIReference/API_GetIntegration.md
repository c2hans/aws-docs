---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetIntegration.html
---

# GetIntegration
<a name="API_GetIntegration"></a>

Returns information about one integration between CloudWatch Logs and OpenSearch Service.

## Request Syntax
<a name="API_GetIntegration_RequestSyntax"></a>

```
{
   "integrationName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetIntegration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [integrationName](#API_GetIntegration_RequestSyntax) **   <a name="CWL-GetIntegration-request-integrationName"></a>
The name of the integration that you want to find information about. To find the name of your integration, use [ListIntegrations](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListIntegrations.html)
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_GetIntegration_ResponseSyntax"></a>

```
{
   "integrationDetails": { ... },
   "integrationName": "string",
   "integrationStatus": "string",
   "integrationType": "string"
}
```

## Response Elements
<a name="API_GetIntegration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [integrationDetails](#API_GetIntegration_ResponseSyntax) **   <a name="CWL-GetIntegration-response-integrationDetails"></a>
A structure that contains information about the integration configuration. For an integration with OpenSearch Service, this includes information about OpenSearch Service resources such as the collection, the workspace, and policies.
Type: [IntegrationDetails](API_IntegrationDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [integrationName](#API_GetIntegration_ResponseSyntax) **   <a name="CWL-GetIntegration-response-integrationName"></a>
The name of the integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[\.\-_/#A-Za-z0-9]+`

 ** [integrationStatus](#API_GetIntegration_ResponseSyntax) **   <a name="CWL-GetIntegration-response-integrationStatus"></a>
The current status of this integration.
Type: String
Valid Values: `PROVISIONING | ACTIVE | FAILED`

 ** [integrationType](#API_GetIntegration_ResponseSyntax) **   <a name="CWL-GetIntegration-response-integrationType"></a>
The type of integration. Integrations with OpenSearch Service have the type `OPENSEARCH`.
Type: String
Valid Values: `OPENSEARCH`

## Errors
<a name="API_GetIntegration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

## See Also
<a name="API_GetIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/GetIntegration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/GetIntegration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/GetIntegration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/GetIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/GetIntegration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/GetIntegration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/GetIntegration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/GetIntegration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/GetIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/GetIntegration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
