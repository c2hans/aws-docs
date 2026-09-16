---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_DescribeConnector.html
---

# DescribeConnector
<a name="API_DescribeConnector"></a>

Describes the given custom connector registered in your AWS account. This API can be used for custom connectors that are registered in your account and also for Amazon authored connectors.

## Request Syntax
<a name="API_DescribeConnector_RequestSyntax"></a>

```
POST /describe-connector HTTP/1.1
Content-type: application/json

{
   "connectorLabel": "{{string}}",
   "connectorType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeConnector_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeConnector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [connectorLabel](#API_DescribeConnector_RequestSyntax) **   <a name="appflow-DescribeConnector-request-connectorLabel"></a>
The label of the connector. The label is unique for each `ConnectorRegistration` in your AWS account. Only needed if calling for CUSTOMCONNECTOR connector type/.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[a-zA-Z0-9][\w!@#.-]+`
Required: No

 ** [connectorType](#API_DescribeConnector_RequestSyntax) **   <a name="appflow-DescribeConnector-request-connectorType"></a>
The connector type, such as CUSTOMCONNECTOR, Saleforce, Marketo. Please choose CUSTOMCONNECTOR for Lambda based custom connectors.
Type: String
Valid Values: `Salesforce | Singular | Slack | Redshift | S3 | Marketo | Googleanalytics | Zendesk | Servicenow | Datadog | Trendmicro | Snowflake | Dynatrace | Infornexus | Amplitude | Veeva | EventBridge | LookoutMetrics | Upsolver | Honeycode | CustomerProfiles | SAPOData | CustomConnector | Pardot`
Required: Yes

## Response Syntax
<a name="API_DescribeConnector_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "connectorConfiguration": {
      "authenticationConfig": {
         "customAuthConfigs": [
            {
               "authParameters": [
                  {
                     "connectorSuppliedValues": [ "string" ],
                     "description": "string",
                     "isRequired": boolean,
                     "isSensitiveField": boolean,
                     "key": "string",
                     "label": "string"
                  }
               ],
               "customAuthenticationType": "string"
            }
         ],
         "isApiKeyAuthSupported": boolean,
         "isBasicAuthSupported": boolean,
         "isCustomAuthSupported": boolean,
         "isOAuth2Supported": boolean,
         "oAuth2Defaults": {
            "authCodeUrls": [ "string" ],
            "oauth2CustomProperties": [
               {
                  "connectorSuppliedValues": [ "string" ],
                  "description": "string",
                  "isRequired": boolean,
                  "isSensitiveField": boolean,
                  "key": "string",
                  "label": "string",
                  "type": "string"
               }
            ],
            "oauth2GrantTypesSupported": [ "string" ],
            "oauthScopes": [ "string" ],
            "tokenUrls": [ "string" ]
         }
      },
      "canUseAsDestination": boolean,
      "canUseAsSource": boolean,
      "connectorArn": "string",
      "connectorDescription": "string",
      "connectorLabel": "string",
      "connectorMetadata": {
         "Amplitude": {
         },
         "CustomerProfiles": {
         },
         "Datadog": {
         },
         "Dynatrace": {
         },
         "EventBridge": {
         },
         "GoogleAnalytics": {
            "oAuthScopes": [ "string" ]
         },
         "Honeycode": {
            "oAuthScopes": [ "string" ]
         },
         "InforNexus": {
         },
         "Marketo": {
         },
         "Pardot": {
         },
         "Redshift": {
         },
         "S3": {
         },
         "Salesforce": {
            "dataTransferApis": [ "string" ],
            "oauth2GrantTypesSupported": [ "string" ],
            "oAuthScopes": [ "string" ]
         },
         "SAPOData": {
         },
         "ServiceNow": {
         },
         "Singular": {
         },
         "Slack": {
            "oAuthScopes": [ "string" ]
         },
         "Snowflake": {
            "supportedRegions": [ "string" ]
         },
         "Trendmicro": {
         },
         "Upsolver": {
         },
         "Veeva": {
         },
         "Zendesk": {
            "oAuthScopes": [ "string" ]
         }
      },
      "connectorModes": [ "string" ],
      "connectorName": "string",
      "connectorOwner": "string",
      "connectorProvisioningConfig": {
         "lambda": {
            "lambdaArn": "string"
         }
      },
      "connectorProvisioningType": "string",
      "connectorRuntimeSettings": [
         {
            "connectorSuppliedValueOptions": [ "string" ],
            "dataType": "string",
            "description": "string",
            "isRequired": boolean,
            "key": "string",
            "label": "string",
            "scope": "string"
         }
      ],
      "connectorType": "string",
      "connectorVersion": "string",
      "isPrivateLinkEnabled": boolean,
      "isPrivateLinkEndpointUrlRequired": boolean,
      "logoURL": "string",
      "registeredAt": number,
      "registeredBy": "string",
      "supportedApiVersions": [ "string" ],
      "supportedDataTransferApis": [
         {
            "Name": "string",
            "Type": "string"
         }
      ],
      "supportedDataTransferTypes": [ "string" ],
      "supportedDestinationConnectors": [ "string" ],
      "supportedOperators": [ "string" ],
      "supportedSchedulingFrequencies": [ "string" ],
      "supportedTriggerTypes": [ "string" ],
      "supportedWriteOperations": [ "string" ]
   }
}
```

## Response Elements
<a name="API_DescribeConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [connectorConfiguration](#API_DescribeConnector_ResponseSyntax) **   <a name="appflow-DescribeConnector-response-connectorConfiguration"></a>
Configuration info of all the connectors that the user requested.
Type: [ConnectorConfiguration](API_ConnectorConfiguration.md) object

## Errors
<a name="API_DescribeConnector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The resource specified in the request (such as the source or destination connector profile) is not found.
HTTP Status Code: 404

 ** ValidationException **
 The request has invalid or missing parameters.
HTTP Status Code: 400

## Examples
<a name="API_DescribeConnector_Examples"></a>

### Describing the given connector
<a name="API_DescribeConnector_Example_1"></a>

This example shows a sample request for the `DescribeConnector` API and a sample response.

#### Sample Request
<a name="API_DescribeConnector_Example_1_Request"></a>

```
{
  "connectorType": "connectorType",
  "connectorLabel": "connectorLabel"
}
```

#### Sample Response
<a name="API_DescribeConnector_Example_1_Response"></a>

```
{
  "connectorConfiguration":
  {
    "authenticationConfig": null,
    "canUseAsDestination": true,
    "canUseAsSource": true,
    "connectorArn": null,
    "connectorDescription": "Salesforce",
    "connectorLabel": null,
    "connectorMetadata":
    {
      "Amplitude": null,
      "AppIntegrations": null,
      "CustomerProfiles": null,
      "Datadog": null,
      "Dynatrace": null,
      "EventBridge": null,
      "GoogleAnalytics": null,
      "Honeycode": null,
      "InforNexus": null,
      "Locke": null,
      "Marketo": null,
      "Pardot": null,
      "Redshift": null,
      "S3": null,
      "SAPOData": null,
      "Salesforce":
      {
        "oAuthScopes":
        [
          "api",
          "refresh_token",
          "id"
        ]
      },
      "ServiceNow": null,
      "Singular": null,
      "Slack": null,
      "Snowflake": null,
      "Trendmicro": null,
      "Upsolver": null,
      "Veeva": null,
      "Zendesk": null
    },
    "connectorModes": null,
    "connectorName": null,
    "connectorOwner": null,
    "connectorProvisioningConfig": null,
    "connectorProvisioningType": null,
    "connectorRuntimeSettings": null,
    "connectorType": "SALESFORCE",
    "connectorVersion": null,
    "isPrivateLinkEnabled": true,
    "isPrivateLinkEndpointUrlRequired": false,
    "logoURL": "insert-logo-here",
    "registeredAt": null,
    "registeredBy": null,
    "supportedApiVersions": null,
    "supportedDestinationConnectors":
    [
      "S3",
      "Snowflake",
      "Redshift",
      "Salesforce",
      "EventBridge",
      "LookoutMetrics",
      "Locke",
      "Honeycode",
      "Upsolver",
      "CustomerProfiles",
      "Zendesk",
      "Marketo",
      "CustomConnector"
    ],
    "supportedOperators": null,
    "supportedSchedulingFrequencies":
    [
      "BYMINUTE",
      "HOURLY",
      "DAILY",
      "WEEKLY",
      "MONTHLY",
      "ONCE"
    ],
    "supportedTriggerTypes":
    [
      "Scheduled",
      "OnDemand",
      "Event"
    ],
    "supportedWriteOperations": null
  }
}
```

## See Also
<a name="API_DescribeConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appflow-2020-08-23/DescribeConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appflow-2020-08-23/DescribeConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/DescribeConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appflow-2020-08-23/DescribeConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/DescribeConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appflow-2020-08-23/DescribeConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appflow-2020-08-23/DescribeConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appflow-2020-08-23/DescribeConnector)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appflow-2020-08-23/DescribeConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/DescribeConnector)
