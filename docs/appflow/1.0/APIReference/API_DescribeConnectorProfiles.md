---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_DescribeConnectorProfiles.html
---

# DescribeConnectorProfiles
<a name="API_DescribeConnectorProfiles"></a>

 Returns a list of `connector-profile` details matching the provided `connector-profile` names and `connector-types`. Both input lists are optional, and you can use them to filter the result.

If no names or `connector-types` are provided, returns all connector profiles in a paginated form. If there is no match, this operation returns an empty list.

## Request Syntax
<a name="API_DescribeConnectorProfiles_RequestSyntax"></a>

```
POST /describe-connector-profiles HTTP/1.1
Content-type: application/json

{
   "connectorLabel": "{{string}}",
   "connectorProfileNames": [ "{{string}}" ],
   "connectorType": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeConnectorProfiles_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeConnectorProfiles_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [connectorLabel](#API_DescribeConnectorProfiles_RequestSyntax) **   <a name="appflow-DescribeConnectorProfiles-request-connectorLabel"></a>
The name of the connector. The name is unique for each `ConnectorRegistration` in your AWS account. Only needed if calling for CUSTOMCONNECTOR connector type/.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[a-zA-Z0-9][\w!@#.-]+`
Required: No

 ** [connectorProfileNames](#API_DescribeConnectorProfiles_RequestSyntax) **   <a name="appflow-DescribeConnectorProfiles-request-connectorProfileNames"></a>
 The name of the connector profile. The name is unique for each `ConnectorProfile` in the AWS account.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Maximum length of 256.
Pattern: `[\w/!@#+=.-]+`
Required: No

 ** [connectorType](#API_DescribeConnectorProfiles_RequestSyntax) **   <a name="appflow-DescribeConnectorProfiles-request-connectorType"></a>
 The type of connector, such as Salesforce, Amplitude, and so on.
Type: String
Valid Values: `Salesforce | Singular | Slack | Redshift | S3 | Marketo | Googleanalytics | Zendesk | Servicenow | Datadog | Trendmicro | Snowflake | Dynatrace | Infornexus | Amplitude | Veeva | EventBridge | LookoutMetrics | Upsolver | Honeycode | CustomerProfiles | SAPOData | CustomConnector | Pardot`
Required: No

 ** [maxResults](#API_DescribeConnectorProfiles_RequestSyntax) **   <a name="appflow-DescribeConnectorProfiles-request-maxResults"></a>
 Specifies the maximum number of items that should be returned in the result set. The default for `maxResults` is 20 (for all paginated API operations).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_DescribeConnectorProfiles_RequestSyntax) **   <a name="appflow-DescribeConnectorProfiles-request-nextToken"></a>
 The pagination token for the next page of data.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `\S+`
Required: No

## Response Syntax
<a name="API_DescribeConnectorProfiles_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "connectorProfileDetails": [
      {
         "connectionMode": "string",
         "connectorLabel": "string",
         "connectorProfileArn": "string",
         "connectorProfileName": "string",
         "connectorProfileProperties": {
            "Amplitude": {
            },
            "CustomConnector": {
               "oAuth2Properties": {
                  "oAuth2GrantType": "string",
                  "tokenUrl": "string",
                  "tokenUrlCustomProperties": {
                     "string" : "string"
                  }
               },
               "profileProperties": {
                  "string" : "string"
               }
            },
            "Datadog": {
               "instanceUrl": "string"
            },
            "Dynatrace": {
               "instanceUrl": "string"
            },
            "GoogleAnalytics": {
            },
            "Honeycode": {
            },
            "InforNexus": {
               "instanceUrl": "string"
            },
            "Marketo": {
               "instanceUrl": "string"
            },
            "Pardot": {
               "businessUnitId": "string",
               "instanceUrl": "string",
               "isSandboxEnvironment": boolean
            },
            "Redshift": {
               "bucketName": "string",
               "bucketPrefix": "string",
               "clusterIdentifier": "string",
               "dataApiRoleArn": "string",
               "databaseName": "string",
               "databaseUrl": "string",
               "isRedshiftServerless": boolean,
               "roleArn": "string",
               "workgroupName": "string"
            },
            "Salesforce": {
               "instanceUrl": "string",
               "isSandboxEnvironment": boolean,
               "usePrivateLinkForMetadataAndAuthorization": boolean
            },
            "SAPOData": {
               "applicationHostUrl": "string",
               "applicationServicePath": "string",
               "clientNumber": "string",
               "disableSSO": boolean,
               "logonLanguage": "string",
               "oAuthProperties": {
                  "authCodeUrl": "string",
                  "oAuthScopes": [ "string" ],
                  "tokenUrl": "string"
               },
               "portNumber": number,
               "privateLinkServiceName": "string"
            },
            "ServiceNow": {
               "instanceUrl": "string"
            },
            "Singular": {
            },
            "Slack": {
               "instanceUrl": "string"
            },
            "Snowflake": {
               "accountName": "string",
               "bucketName": "string",
               "bucketPrefix": "string",
               "privateLinkServiceName": "string",
               "region": "string",
               "stage": "string",
               "warehouse": "string"
            },
            "Trendmicro": {
            },
            "Veeva": {
               "instanceUrl": "string"
            },
            "Zendesk": {
               "instanceUrl": "string"
            }
         },
         "connectorType": "string",
         "createdAt": number,
         "credentialsArn": "string",
         "lastUpdatedAt": number,
         "privateConnectionProvisioningState": {
            "failureCause": "string",
            "failureMessage": "string",
            "status": "string"
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeConnectorProfiles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [connectorProfileDetails](#API_DescribeConnectorProfiles_ResponseSyntax) **   <a name="appflow-DescribeConnectorProfiles-response-connectorProfileDetails"></a>
 Returns information about the connector profiles associated with the flow.
Type: Array of [ConnectorProfile](API_ConnectorProfile.md) objects

 ** [nextToken](#API_DescribeConnectorProfiles_ResponseSyntax) **   <a name="appflow-DescribeConnectorProfiles-response-nextToken"></a>
 The pagination token for the next page of data. If `nextToken=null`, this means that all records have been fetched.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `\S+`

## Errors
<a name="API_DescribeConnectorProfiles_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ValidationException **
 The request has invalid or missing parameters.
HTTP Status Code: 400

## Examples
<a name="API_DescribeConnectorProfiles_Examples"></a>

### DescribeConnectorProfiles example
<a name="API_DescribeConnectorProfiles_Example_1"></a>

This example shows a sample request and response for the `DescribeConnectorProfiles` API.

#### Sample Request
<a name="API_DescribeConnectorProfiles_Example_1_Request"></a>

```
{
  "connectorProfileNames": ["OldMarketoProfile","non-existing-name"],
  "connectorTypes": ["Marketo","Salesforce"]
}
```

#### Sample Response
<a name="API_DescribeConnectorProfiles_Example_1_Response"></a>

```
{
  "connectorProfileDetails": [
    {
      "arn": "arn:aws:appflow:region:<AccountId>:connectorprofile/OldMarketoProfile",
      "configuration": {
        "api_version": "v1",
        "connection_mode": "Public",
        "credentials_arn": "arn:aws:secretsmanager:region:<AccountId>:secret:<secret>",
        "instanceUrl": "MarketoUrl"
      },
      "connectionMode": "Public",
      "connectorProfileArn": "arn:aws:appflow:region:<AccountId>:connectorprofile/OldMarketoProfile",
      "connectorProfileName": "OldMarketoProfile",
      "connectorProfileProps": {
        "Amplitude": null,
        "Datadog": null,
        "Dynatrace": null,
        "GoogleAnalytics": null,
        "InforNexus": null,
        "Marketo": {
          "apiVersion": "v1",
          "instanceUrl": "MarketoUrl"
        },
        "Redshift": null,
        "Salesforce": null,
        "ServiceNow": null,
        "Singular": null,
        "Slack": null,
        "Snowflake": null,
        "Trendmicro": null,
        "Veeva": null,
        "Zendesk": null
      },
      "connectorType": "Marketo",
      "createdAt": "created_at_value",
      "credentialsArn": "arn:aws:secretsmanager:region:<AccountId>:secret:<secret>",
      "label": "OldMarketoProfile",
      "lastUpdated": "lastupdated_value",
      "lastUpdatedAt": "lastupdated_at_value"
    }
  ],
  "nextToken": null
}
```

### DescribeConnectorProfiles example
<a name="API_DescribeConnectorProfiles_Example_2"></a>

This example shows a sample request and response for the `DescribeConnectorProfiles` API.

#### Sample Request
<a name="API_DescribeConnectorProfiles_Example_2_Request"></a>

```
{
   "connectorProfileNames": ["OldMarketoProfile", "non-existing-name"],
   "connectorTypes": ["Marketo", "Salesforce", "CustomConnector"],
   "connectorLabel": "MyCustomConnectorLabel"
}
```

#### Sample Response
<a name="API_DescribeConnectorProfiles_Example_2_Response"></a>

```
{
  "connectorProfileDetails": [
    {
      "arn": "arn:aws:appflow:region:<AccountId>:connectorprofile/OldMarketoProfile",
      "configuration":
      {
        "api_version": "v1",
        "connection_mode": "Public",
        "credentials_arn": "arn:aws:secretsmanager:region:<AccountId>:secret:<secret>",
        "instanceUrl": "MarketoUrl"
      },
      "connectionMode": "Public",
      "connectorProfileArn": "arn:aws:appflow:region:<AccountId>:connectorprofile/OldMarketoProfile",
      "connectorProfileName": "OldMarketoProfile",
      "connectorProfileProps":
      {
        "Amplitude": null,
        "Datadog": null,
        "Dynatrace": null,
        "GoogleAnalytics": null,
        "InforNexus": null,
        "Marketo":
        {
          "apiVersion": "v1",
          "instanceUrl": "MarketoUrl"
        },
        "Redshift": null,
        "Salesforce": null,
        "ServiceNow": null,
        "Singular": null,
        "Slack": null,
        "Snowflake": null,
        "Trendmicro": null,
        "Veeva": null,
        "Zendesk": null
      },
      "connectorType": "Marketo",
      "createdAt": "2022-02-22T15:31:41.467000-08:00",
      "credentialsArn": "arn:aws:secretsmanager:region:<AccountId>:secret:<secret>",
      "label": "OldMarketoProfile",
      "lastUpdatedAt": "2022-02-22T15:31:41.467000-08:00"
    }
  ],
  "nextToken": null
}
```

## See Also
<a name="API_DescribeConnectorProfiles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appflow-2020-08-23/DescribeConnectorProfiles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appflow-2020-08-23/DescribeConnectorProfiles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/DescribeConnectorProfiles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appflow-2020-08-23/DescribeConnectorProfiles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/DescribeConnectorProfiles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appflow-2020-08-23/DescribeConnectorProfiles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appflow-2020-08-23/DescribeConnectorProfiles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appflow-2020-08-23/DescribeConnectorProfiles)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appflow-2020-08-23/DescribeConnectorProfiles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/DescribeConnectorProfiles)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
