---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListIntegrations.html
---

# ListIntegrations
<a name="API_ListIntegrations"></a>

Returns a list of integrations between CloudWatch Logs and other services in this account. Currently, only one integration can be created in an account, and this integration must be with OpenSearch Service.

## Request Syntax
<a name="API_ListIntegrations_RequestSyntax"></a>

```
{
   "integrationNamePrefix": "{{string}}",
   "integrationStatus": "{{string}}",
   "integrationType": "{{string}}"
}
```

## Request Parameters
<a name="API_ListIntegrations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [integrationNamePrefix](#API_ListIntegrations_RequestSyntax) **   <a name="CWL-ListIntegrations-request-integrationNamePrefix"></a>
To limit the results to integrations that start with a certain name prefix, specify that name prefix here.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** [integrationStatus](#API_ListIntegrations_RequestSyntax) **   <a name="CWL-ListIntegrations-request-integrationStatus"></a>
To limit the results to integrations with a certain status, specify that status here.
Type: String
Valid Values: `PROVISIONING | ACTIVE | FAILED`
Required: No

 ** [integrationType](#API_ListIntegrations_RequestSyntax) **   <a name="CWL-ListIntegrations-request-integrationType"></a>
To limit the results to integrations of a certain type, specify that type here.
Type: String
Valid Values: `OPENSEARCH`
Required: No

## Response Syntax
<a name="API_ListIntegrations_ResponseSyntax"></a>

```
{
   "integrationSummaries": [
      {
         "integrationName": "string",
         "integrationStatus": "string",
         "integrationType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListIntegrations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [integrationSummaries](#API_ListIntegrations_ResponseSyntax) **   <a name="CWL-ListIntegrations-response-integrationSummaries"></a>
An array, where each object in the array contains information about one CloudWatch Logs integration in this account.
Type: Array of [IntegrationSummary](API_IntegrationSummary.md) objects

## Errors
<a name="API_ListIntegrations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

## See Also
<a name="API_ListIntegrations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/ListIntegrations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/ListIntegrations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/ListIntegrations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/ListIntegrations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/ListIntegrations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/ListIntegrations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/ListIntegrations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/ListIntegrations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/ListIntegrations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/ListIntegrations)
