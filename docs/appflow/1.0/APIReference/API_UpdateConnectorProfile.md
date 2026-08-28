---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_UpdateConnectorProfile.html
---

# UpdateConnectorProfile
<a name="API_UpdateConnectorProfile"></a>

 Updates a given connector profile associated with your account.

## Request Syntax
<a name="API_UpdateConnectorProfile_RequestSyntax"></a>

```
POST /update-connector-profile HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "connectionMode": "{{string}}",
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
   "connectorProfileName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateConnectorProfile_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateConnectorProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateConnectorProfile_RequestSyntax) **   <a name="appflow-UpdateConnectorProfile-request-clientToken"></a>
The `clientToken` parameter is an idempotency token. It ensures that your `UpdateConnectorProfile` request completes only once. You choose the value to pass. For example, if you don't receive a response from your request, you can safely retry the request with the same `clientToken` parameter value.
If you omit a `clientToken` value, the AWS SDK that you are using inserts a value for you. This way, the SDK can safely retry requests multiple times after a network error. You must provide your own value for other use cases.
If you specify input parameters that differ from your first request, an error occurs. If you use a different value for `clientToken`, Amazon AppFlow considers it a new call to `UpdateConnectorProfile`. The token is active for 8 hours.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[ -~]+`
Required: No

 ** [connectionMode](#API_UpdateConnectorProfile_RequestSyntax) **   <a name="appflow-UpdateConnectorProfile-request-connectionMode"></a>
 Indicates the connection mode and if it is public or private.
Type: String
Valid Values: `Public | Private`
Required: Yes

 ** [connectorProfileConfig](#API_UpdateConnectorProfile_RequestSyntax) **   <a name="appflow-UpdateConnectorProfile-request-connectorProfileConfig"></a>
 Defines the connector-specific profile configuration and credentials.
Type: [ConnectorProfileConfig](API_ConnectorProfileConfig.md) object
Required: Yes

 ** [connectorProfileName](#API_UpdateConnectorProfile_RequestSyntax) **   <a name="appflow-UpdateConnectorProfile-request-connectorProfileName"></a>
 The name of the connector profile and is unique for each `ConnectorProfile` in the AWS account.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[\w/!@#+=.-]+`
Required: Yes

## Response Syntax
<a name="API_UpdateConnectorProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "connectorProfileArn": "string"
}
```

## Response Elements
<a name="API_UpdateConnectorProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [connectorProfileArn](#API_UpdateConnectorProfile_ResponseSyntax) **   <a name="appflow-UpdateConnectorProfile-response-connectorProfileArn"></a>
 The Amazon Resource Name (ARN) of the connector profile.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `arn:aws:appflow:.*:[0-9]+:.*`

## Errors
<a name="API_UpdateConnectorProfile_Errors"></a>

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

 ** ResourceNotFoundException **
 The resource specified in the request (such as the source or destination connector profile) is not found.
HTTP Status Code: 404

 ** ValidationException **
 The request has invalid or missing parameters.
HTTP Status Code: 400

## Examples
<a name="API_UpdateConnectorProfile_Examples"></a>

### UpdateConnectorProfile example using Salesforce
<a name="API_UpdateConnectorProfile_Example_1"></a>

This example shows a sample request and response for the `UpdateConnectorProfile` API using Salesforce.

#### Sample Request
<a name="API_UpdateConnectorProfile_Example_1_Request"></a>

```
{
  "connectorProfileName": "Connector_Profile_Name_value",
  "kmsArn": null,
  "connectorType": "Salesforce",
  "connectionMode": "Public",
  "connectorProfileConfig":
  {
    "connectorProfileProperties":
    {
      "salesforce":
      {
        "instanceUrl": "Instance_url_value",
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
<a name="API_UpdateConnectorProfile_Example_1_Response"></a>

```
{
  "connectorProfileArn": "arn:aws:appflow:region:<AccountId>:connectorprofile/Connector_Profile_Name"
}
```

## See Also
<a name="API_UpdateConnectorProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appflow-2020-08-23/UpdateConnectorProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appflow-2020-08-23/UpdateConnectorProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/UpdateConnectorProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appflow-2020-08-23/UpdateConnectorProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/UpdateConnectorProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appflow-2020-08-23/UpdateConnectorProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appflow-2020-08-23/UpdateConnectorProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appflow-2020-08-23/UpdateConnectorProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appflow-2020-08-23/UpdateConnectorProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/UpdateConnectorProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
