---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_CreateConnectorProfile.html
---

# CreateConnectorProfile
<a name="API_CreateConnectorProfile"></a>

 Creates a new connector profile associated with your AWS account. There is a soft quota of 100 connector profiles per AWS account. If you need more connector profiles than this quota allows, you can submit a request to the Amazon AppFlow team through the Amazon AppFlow support channel. In each connector profile that you create, you can provide the credentials and properties for only one connector.

## Request Syntax
<a name="API_CreateConnectorProfile_RequestSyntax"></a>

```
POST /create-connector-profile HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "connectionMode": "{{string}}",
   "connectorLabel": "{{string}}",
   "connectorProfileConfig": {
      "connectorProfileCredentials": {
         "Amplitude": {
            "apiKey": "{{string}}",
            "secretKey": "{{string}}"
         },
         "CustomConnector": {
            "apiKey": {
               "apiKey": "{{string}}",
               "apiSecretKey": "{{string}}"
            },
            "authenticationType": "{{string}}",
            "basic": {
               "password": "{{string}}",
               "username": "{{string}}"
            },
            "custom": {
               "credentialsMap": {
                  "{{string}}" : "{{string}}"
               },
               "customAuthenticationType": "{{string}}"
            },
            "oauth2": {
               "accessToken": "{{string}}",
               "clientId": "{{string}}",
               "clientSecret": "{{string}}",
               "oAuthRequest": {
                  "authCode": "{{string}}",
                  "redirectUri": "{{string}}"
               },
               "refreshToken": "{{string}}"
            }
         },
         "Datadog": {
            "apiKey": "{{string}}",
            "applicationKey": "{{string}}"
         },
         "Dynatrace": {
            "apiToken": "{{string}}"
         },
         "GoogleAnalytics": {
            "accessToken": "{{string}}",
            "clientId": "{{string}}",
            "clientSecret": "{{string}}",
            "oAuthRequest": {
               "authCode": "{{string}}",
               "redirectUri": "{{string}}"
            },
            "refreshToken": "{{string}}"
         },
         "Honeycode": {
            "accessToken": "{{string}}",
            "oAuthRequest": {
               "authCode": "{{string}}",
               "redirectUri": "{{string}}"
            },
            "refreshToken": "{{string}}"
         },
         "InforNexus": {
            "accessKeyId": "{{string}}",
            "datakey": "{{string}}",
            "secretAccessKey": "{{string}}",
            "userId": "{{string}}"
         },
         "Marketo": {
            "accessToken": "{{string}}",
            "clientId": "{{string}}",
            "clientSecret": "{{string}}",
            "oAuthRequest": {
               "authCode": "{{string}}",
               "redirectUri": "{{string}}"
            }
         },
         "Pardot": {
            "accessToken": "{{string}}",
            "clientCredentialsArn": "{{string}}",
            "oAuthRequest": {
               "authCode": "{{string}}",
               "redirectUri": "{{string}}"
            },
            "refreshToken": "{{string}}"
         },
         "Redshift": {
            "password": "{{string}}",
            "username": "{{string}}"
         },
         "Salesforce": {
            "accessToken": "{{string}}",
            "clientCredentialsArn": "{{string}}",
            "jwtToken": "{{string}}",
            "oAuth2GrantType": "{{string}}",
            "oAuthRequest": {
               "authCode": "{{string}}",
               "redirectUri": "{{string}}"
            },
            "refreshToken": "{{string}}"
         },
         "SAPOData": {
            "basicAuthCredentials": {
               "password": "{{string}}",
               "username": "{{string}}"
            },
            "oAuthCredentials": {
               "accessToken": "{{string}}",
               "clientId": "{{string}}",
               "clientSecret": "{{string}}",
               "oAuthRequest": {
                  "authCode": "{{string}}",
                  "redirectUri": "{{string}}"
               },
               "refreshToken": "{{string}}"
            }
         },
         "ServiceNow": {
            "oAuth2Credentials": {
               "accessToken": "{{string}}",
               "clientId": "{{string}}",
               "clientSecret": "{{string}}",
               "oAuthRequest": {
                  "authCode": "{{string}}",
                  "redirectUri": "{{string}}"
               },
               "refreshToken": "{{string}}"
            },
            "password": "{{string}}",
            "username": "{{string}}"
         },
         "Singular": {
            "apiKey": "{{string}}"
         },
         "Slack": {
            "accessToken": "{{string}}",
            "clientId": "{{string}}",
            "clientSecret": "{{string}}",
            "oAuthRequest": {
               "authCode": "{{string}}",
               "redirectUri": "{{string}}"
            }
         },
         "Snowflake": {
            "password": "{{string}}",
            "username": "{{string}}"
         },
         "Trendmicro": {
            "apiSecretKey": "{{string}}"
         },
         "Veeva": {
            "password": "{{string}}",
            "username": "{{string}}"
         },
         "Zendesk": {
            "accessToken": "{{string}}",
            "clientId": "{{string}}",
            "clientSecret": "{{string}}",
            "oAuthRequest": {
               "authCode": "{{string}}",
               "redirectUri": "{{string}}"
            }
         }
      },
      "connectorProfileProperties": {
         "Amplitude": {
         },
         "CustomConnector": {
            "oAuth2Properties": {
               "oAuth2GrantType": "{{string}}",
               "tokenUrl": "{{string}}",
               "tokenUrlCustomProperties": {
                  "{{string}}" : "{{string}}"
               }
            },
            "profileProperties": {
               "{{string}}" : "{{string}}"
            }
         },
         "Datadog": {
            "instanceUrl": "{{string}}"
         },
         "Dynatrace": {
            "instanceUrl": "{{string}}"
         },
         "GoogleAnalytics": {
         },
         "Honeycode": {
         },
         "InforNexus": {
            "instanceUrl": "{{string}}"
         },
         "Marketo": {
            "instanceUrl": "{{string}}"
         },
         "Pardot": {
            "businessUnitId": "{{string}}",
            "instanceUrl": "{{string}}",
            "isSandboxEnvironment": {{boolean}}
         },
         "Redshift": {
            "bucketName": "{{string}}",
            "bucketPrefix": "{{string}}",
            "clusterIdentifier": "{{string}}",
            "dataApiRoleArn": "{{string}}",
            "databaseName": "{{string}}",
            "databaseUrl": "{{string}}",
            "isRedshiftServerless": {{boolean}},
            "roleArn": "{{string}}",
            "workgroupName": "{{string}}"
         },
         "Salesforce": {
            "instanceUrl": "{{string}}",
            "isSandboxEnvironment": {{boolean}},
            "usePrivateLinkForMetadataAndAuthorization": {{boolean}}
         },
         "SAPOData": {
            "applicationHostUrl": "{{string}}",
            "applicationServicePath": "{{string}}",
            "clientNumber": "{{string}}",
            "disableSSO": {{boolean}},
            "logonLanguage": "{{string}}",
            "oAuthProperties": {
               "authCodeUrl": "{{string}}",
               "oAuthScopes": [ "{{string}}" ],
               "tokenUrl": "{{string}}"
            },
            "portNumber": {{number}},
            "privateLinkServiceName": "{{string}}"
         },
         "ServiceNow": {
            "instanceUrl": "{{string}}"
         },
         "Singular": {
         },
         "Slack": {
            "instanceUrl": "{{string}}"
         },
         "Snowflake": {
            "accountName": "{{string}}",
            "bucketName": "{{string}}",
            "bucketPrefix": "{{string}}",
            "privateLinkServiceName": "{{string}}",
            "region": "{{string}}",
            "stage": "{{string}}",
            "warehouse": "{{string}}"
         },
         "Trendmicro": {
         },
         "Veeva": {
            "instanceUrl": "{{string}}"
         },
         "Zendesk": {
            "instanceUrl": "{{string}}"
         }
      }
   },
   "connectorProfileName": "{{string}}",
   "connectorType": "{{string}}",
   "kmsArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateConnectorProfile_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateConnectorProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateConnectorProfile_RequestSyntax) **   <a name="appflow-CreateConnectorProfile-request-clientToken"></a>
The `clientToken` parameter is an idempotency token. It ensures that your `CreateConnectorProfile` request completes only once. You choose the value to pass. For example, if you don't receive a response from your request, you can safely retry the request with the same `clientToken` parameter value.
If you omit a `clientToken` value, the AWS SDK that you are using inserts a value for you. This way, the SDK can safely retry requests multiple times after a network error. You must provide your own value for other use cases.
If you specify input parameters that differ from your first request, an error occurs. If you use a different value for `clientToken`, Amazon AppFlow considers it a new call to `CreateConnectorProfile`. The token is active for 8 hours.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[ -~]+`
Required: No

 ** [connectionMode](#API_CreateConnectorProfile_RequestSyntax) **   <a name="appflow-CreateConnectorProfile-request-connectionMode"></a>
 Indicates the connection mode and specifies whether it is public or private. Private flows use AWS PrivateLink to route data over AWS infrastructure without exposing it to the public internet.
Type: String
Valid Values: `Public | Private`
Required: Yes

 ** [connectorLabel](#API_CreateConnectorProfile_RequestSyntax) **   <a name="appflow-CreateConnectorProfile-request-connectorLabel"></a>
The label of the connector. The label is unique for each `ConnectorRegistration` in your AWS account. Only needed if calling for CUSTOMCONNECTOR connector type/.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[a-zA-Z0-9][\w!@#.-]+`
Required: No

 ** [connectorProfileConfig](#API_CreateConnectorProfile_RequestSyntax) **   <a name="appflow-CreateConnectorProfile-request-connectorProfileConfig"></a>
 Defines the connector-specific configuration and credentials.
Type: [ConnectorProfileConfig](API_ConnectorProfileConfig.md) object
Required: Yes

 ** [connectorProfileName](#API_CreateConnectorProfile_RequestSyntax) **   <a name="appflow-CreateConnectorProfile-request-connectorProfileName"></a>
 The name of the connector profile. The name is unique for each `ConnectorProfile` in your AWS account.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[\w/!@#+=.-]+`
Required: Yes

 ** [connectorType](#API_CreateConnectorProfile_RequestSyntax) **   <a name="appflow-CreateConnectorProfile-request-connectorType"></a>
 The type of connector, such as Salesforce, Amplitude, and so on.
Type: String
Valid Values: `Salesforce | Singular | Slack | Redshift | S3 | Marketo | Googleanalytics | Zendesk | Servicenow | Datadog | Trendmicro | Snowflake | Dynatrace | Infornexus | Amplitude | Veeva | EventBridge | LookoutMetrics | Upsolver | Honeycode | CustomerProfiles | SAPOData | CustomConnector | Pardot`
Required: Yes

 ** [kmsArn](#API_CreateConnectorProfile_RequestSyntax) **   <a name="appflow-CreateConnectorProfile-request-kmsArn"></a>
 The ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption. This is required if you do not want to use the Amazon AppFlow-managed KMS key. If you don't provide anything here, Amazon AppFlow uses the Amazon AppFlow-managed KMS key.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:kms:.*:[0-9]+:.*`
Required: No

## Response Syntax
<a name="API_CreateConnectorProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "connectorProfileArn": "string"
}
```

## Response Elements
<a name="API_CreateConnectorProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [connectorProfileArn](#API_CreateConnectorProfile_ResponseSyntax) **   <a name="appflow-CreateConnectorProfile-response-connectorProfileArn"></a>
 The Amazon Resource Name (ARN) of the connector profile.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `arn:aws:appflow:.*:[0-9]+:.*`

## Errors
<a name="API_CreateConnectorProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
 There was a conflict when processing the request (for example, a flow with the given name already exists within the account. Check for conflicting resource names and try again.
HTTP Status Code: 409

 ** ConnectorAuthenticationException **
 An error occurred when authenticating with the connector endpoint.
HTTP Status Code: 401

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
 The request would cause a service quota (such as the number of flows) to be exceeded.
HTTP Status Code: 402

 ** ValidationException **
 The request has invalid or missing parameters.
HTTP Status Code: 400

## Examples
<a name="API_CreateConnectorProfile_Examples"></a>

### CustomConnector
<a name="API_CreateConnectorProfile_Example_1"></a>

This example shows a sample request for the `CreateConnectorProfile` API (without OAuth) and a sample response.

#### Sample Request
<a name="API_CreateConnectorProfile_Example_1_Request"></a>

```
{
  "connectorProfileName": "Connector_Profile_Name_Value",
  "kmsArn": null,
  "connectorType": "CUSTOMCONNECTOR",
  "connectorLabel": "MyCustomConnector",
  "connectionMode": "Public",
  "connectorProfileConfig":
  {
    "connectorProfileProperties":
    {
      "salesforce":
      {
        "instanceUrl": "InstanceUrl_value",
        "isSandboxEnvironment": false
      }
    },
    "connectorProfileCredentials":
    {
      "salesforce":
      {
        "accessToken": "<AccessToken>",
        "refreshToken": "<RefreshToken>",
        "oauthRequest":
        {
          "authCode": null,
          "redirectUri": null
        }
      }
    }
  }
}
```

#### Sample Response
<a name="API_CreateConnectorProfile_Example_1_Response"></a>

```
{
  "connectorProfileArn": "arn:aws:appflow:region:<AccountId>:connectorprofile/Connector_Profile_Name"
}
```

### Salesforce without OAuth
<a name="API_CreateConnectorProfile_Example_2"></a>

This example shows a sample request for the `CreateConnectorProfile` API (without OAuth) and a sample response.

#### Sample Request
<a name="API_CreateConnectorProfile_Example_2_Request"></a>

```
{
  "connectorProfileName": "Connector_Profile_Name_Value",
  "kmsArn": null,
  "connectorType": "Salesforce",
  "connectorLabel": "Salesforce",
  "connectionMode": "Public",
  "connectorProfileConfig": {
    "connectorProfileProperties": {
      "salesforce": {
        "instanceUrl": "InstanceUrl_value",
        "isSandboxEnvironment": false
      }
    },
    "connectorProfileCredentials": {
      "salesforce": {
        "accessToken": "<AccessToken>",
        "refreshToken": "<RefreshToken>",
        "oauthRequest": {
          "authCode": null,
          "redirectUri": null
        }
      }
    }
  }
}
```

#### Sample Response
<a name="API_CreateConnectorProfile_Example_2_Response"></a>

```
{
  "connectorProfileArn": "arn:aws:appflow:region:<AccountId>:connectorprofile/Connector_Profile_Name"
}
```

### Salesforce with OAuth
<a name="API_CreateConnectorProfile_Example_3"></a>

These examples show a request with OAuth and a sample response.

#### Sample Request
<a name="API_CreateConnectorProfile_Example_3_Request"></a>

```
{
  "connectorProfileName": "connector-profile-name_value",
  "kmsArn": null,
  "connectorType": "Salesforce",
  "connectionMode": "Public",
  "connectorProfileConfig": {
    "connectorProfileProperties": {
      "salesforce": {
        "isSandboxEnvironment": false
      }
    },
    "connectorProfileCredentials": {
      "salesforce": {
        "oauthRequest": {
          "authCode": "<AuthCode>",
          "redirectUri": "redirectUri"
        }
      }
    }
  }
}
```

#### Sample Response
<a name="API_CreateConnectorProfile_Example_3_Response"></a>

```
{
  "connectorProfileArn": "arn:aws:appflow:region:<AccountId>:connectorprofile/connector-profile-name"
}
```

### Zendesk
<a name="API_CreateConnectorProfile_Example_4"></a>

This example shows a sample request and response for the `CreateConnectorProfile` API using Zendesk.

#### Sample Request
<a name="API_CreateConnectorProfile_Example_4_Request"></a>

```
{
  "connectorProfileName": "connector-profile-name",
  "connectorType": "Zendesk",
  "connectionMode": "Public",
  "connectorProfileConfig": {
    "connectorProfileProperties": {
      "zendesk": {
        "instanceUrl": "Zendesk_Url"
      }
    },
    "connectorProfileCredentials": {
      "zendesk": {
        "clientId": "aws_integration_to_zendesk",
        "clientSecret": "<ClientSecret>",
        "accessToken": "<AccessToken>",
        "oauthRequest": {
          "authCode": null,
          "redirectUri": null
        }
      }
    }
  }
}
```

#### Sample Response
<a name="API_CreateConnectorProfile_Example_4_Response"></a>

```
{
  "connectorProfileArn": "arn:aws:appflow:region:<AccountId>:connectorprofile/connector-profile-name"
}
```

### Google Analytics
<a name="API_CreateConnectorProfile_Example_5"></a>

This example shows a sample request and response for the `CreateConnectorProfile` API using Google Analytics.

#### Sample Request
<a name="API_CreateConnectorProfile_Example_5_Request"></a>

```
{
  "connectorProfileName": "connector-profile-name",
  "connectorType": "Googleanalytics",
  "connectionMode": "Public",
  "connectorProfileConfig": {
    "connectorProfileProperties": {
      "googleAnalytics": {}
    },
    "connectorProfileCredentials": {
      "googleAnalytics": {
        "clientId": "<ClientId>",
        "clientSecret": "<ClientSecret>",
        "accessToken": "<AccessToken>",
        "refreshToken": "<RefreshToken>",
        "oauthRequest": {
          "authCode": null,
          "redirectUri": null
        }
      }
    }
  }
}
```

```
{
  "connectorProfileArn": "arn:aws:appflow:region:<AccountId>:connectorprofile/connector-profile-name"
}
```

### Marketo
<a name="API_CreateConnectorProfile_Example_6"></a>

This example shows a sample request and response for the `CreateConnectorProfile` API using Marketo.

#### Sample Request
<a name="API_CreateConnectorProfile_Example_6_Request"></a>

```
{
  "connectorProfileName": "Connector-profile-new",
  "connectorType": "Marketo",
  "connectionMode": "Public",
  "connectorProfileConfig": {
    "connectorProfileProperties": {
      "marketo": {
        "instanceUrl": "Marketo_Url"
      }
    },
    "connectorProfileCredentials": {
      "marketo": {
        "clientId": "<ClientId>>",
        "clientSecret": "<ClientSecret>",
        "accessToken": "<AccessToken>",
        "oauthRequest": {
          "authCode": null,
          "redirectUri": null
        }
      }
    }
  }
}
```

#### Sample Response
<a name="API_CreateConnectorProfile_Example_6_Response"></a>

```
{
  "connectorProfileArn": "arn:aws:appflow:region:<AccountId>:connectorprofile/Connector-profile-new"
}
```

## See Also
<a name="API_CreateConnectorProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appflow-2020-08-23/CreateConnectorProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appflow-2020-08-23/CreateConnectorProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/CreateConnectorProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appflow-2020-08-23/CreateConnectorProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/CreateConnectorProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appflow-2020-08-23/CreateConnectorProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appflow-2020-08-23/CreateConnectorProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appflow-2020-08-23/CreateConnectorProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appflow-2020-08-23/CreateConnectorProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/CreateConnectorProfile)
