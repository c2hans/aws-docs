---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_RegisterConnectionType.html
---

# RegisterConnectionType
<a name="API_RegisterConnectionType"></a>

Registers a custom connection type in AWS Glue based on the configuration provided. This operation enables customers to configure custom connectors for any data source with REST-based APIs, eliminating the need for building custom Lambda connectors.

The registered connection type stores details about how requests and responses are interpreted by REST sources, including connection properties, authentication configuration, and REST configuration with entity definitions. Once registered, customers can create connections using this connection type and work with them the same way as natively supported AWS Glue connectors.

Supports multiple authentication types including Basic, OAuth2 (Client Credentials, JWT Bearer, Authorization Code), and Custom Auth configurations.

## Request Syntax
<a name="API_RegisterConnectionType_RequestSyntax"></a>

```
{
   "ConnectionProperties": {
      "AdditionalRequestParameters": [
         {
            "AllowedValues": [ "{{string}}" ],
            "DefaultValue": "{{string}}",
            "KeyOverride": "{{string}}",
            "Name": "{{string}}",
            "PropertyLocation": "{{string}}",
            "PropertyType": "{{string}}",
            "Required": {{boolean}}
         }
      ],
      "Url": {
         "AllowedValues": [ "{{string}}" ],
         "DefaultValue": "{{string}}",
         "KeyOverride": "{{string}}",
         "Name": "{{string}}",
         "PropertyLocation": "{{string}}",
         "PropertyType": "{{string}}",
         "Required": {{boolean}}
      }
   },
   "ConnectionType": "{{string}}",
   "ConnectorAuthenticationConfiguration": {
      "AuthenticationTypes": [ "{{string}}" ],
      "BasicAuthenticationProperties": {
         "Password": {
            "AllowedValues": [ "{{string}}" ],
            "DefaultValue": "{{string}}",
            "KeyOverride": "{{string}}",
            "Name": "{{string}}",
            "PropertyLocation": "{{string}}",
            "PropertyType": "{{string}}",
            "Required": {{boolean}}
         },
         "Username": {
            "AllowedValues": [ "{{string}}" ],
            "DefaultValue": "{{string}}",
            "KeyOverride": "{{string}}",
            "Name": "{{string}}",
            "PropertyLocation": "{{string}}",
            "PropertyType": "{{string}}",
            "Required": {{boolean}}
         }
      },
      "CustomAuthenticationProperties": {
         "AuthenticationParameters": [
            {
               "AllowedValues": [ "{{string}}" ],
               "DefaultValue": "{{string}}",
               "KeyOverride": "{{string}}",
               "Name": "{{string}}",
               "PropertyLocation": "{{string}}",
               "PropertyType": "{{string}}",
               "Required": {{boolean}}
            }
         ]
      },
      "OAuth2Properties": {
         "AuthorizationCodeProperties": {
            "AuthorizationCode": {
               "AllowedValues": [ "{{string}}" ],
               "DefaultValue": "{{string}}",
               "KeyOverride": "{{string}}",
               "Name": "{{string}}",
               "PropertyLocation": "{{string}}",
               "PropertyType": "{{string}}",
               "Required": {{boolean}}
            },
            "AuthorizationCodeUrl": {
               "AllowedValues": [ "{{string}}" ],
               "DefaultValue": "{{string}}",
               "KeyOverride": "{{string}}",
               "Name": "{{string}}",
               "PropertyLocation": "{{string}}",
               "PropertyType": "{{string}}",
               "Required": {{boolean}}
            },
            "ClientId": {
               "AllowedValues": [ "{{string}}" ],
               "DefaultValue": "{{string}}",
               "KeyOverride": "{{string}}",
               "Name": "{{string}}",
               "PropertyLocation": "{{string}}",
               "PropertyType": "{{string}}",
               "Required": {{boolean}}
            },
            "ClientSecret": {
               "AllowedValues": [ "{{string}}" ],
               "DefaultValue": "{{string}}",
               "KeyOverride": "{{string}}",
               "Name": "{{string}}",
               "PropertyLocation": "{{string}}",
               "PropertyType": "{{string}}",
               "Required": {{boolean}}
            },
            "ContentType": "{{string}}",
            "Prompt": {
               "AllowedValues": [ "{{string}}" ],
               "DefaultValue": "{{string}}",
               "KeyOverride": "{{string}}",
               "Name": "{{string}}",
               "PropertyLocation": "{{string}}",
               "PropertyType": "{{string}}",
               "Required": {{boolean}}
            },
            "RedirectUri": {
               "AllowedValues": [ "{{string}}" ],
               "DefaultValue": "{{string}}",
               "KeyOverride": "{{string}}",
               "Name": "{{string}}",
               "PropertyLocation": "{{string}}",
               "PropertyType": "{{string}}",
               "Required": {{boolean}}
            },
            "RequestMethod": "{{string}}",
            "Scope": {
               "AllowedValues": [ "{{string}}" ],
               "DefaultValue": "{{string}}",
               "KeyOverride": "{{string}}",
               "Name": "{{string}}",
               "PropertyLocation": "{{string}}",
               "PropertyType": "{{string}}",
               "Required": {{boolean}}
            },
            "TokenUrl": {
               "AllowedValues": [ "{{string}}" ],
               "DefaultValue": "{{string}}",
               "KeyOverride": "{{string}}",
               "Name": "{{string}}",
               "PropertyLocation": "{{string}}",
               "PropertyType": "{{string}}",
               "Required": {{boolean}}
            },
            "TokenUrlParameters": [
               {
                  "AllowedValues": [ "{{string}}" ],
                  "DefaultValue": "{{string}}",
                  "KeyOverride": "{{string}}",
                  "Name": "{{string}}",
                  "PropertyLocation": "{{string}}",
                  "PropertyType": "{{string}}",
                  "Required": {{boolean}}
               }
            ]
         },
         "ClientCredentialsProperties": {
            "ClientId": {
               "AllowedValues": [ "{{string}}" ],
               "DefaultValue": "{{string}}",
               "KeyOverride": "{{string}}",
               "Name": "{{string}}",
               "PropertyLocation": "{{string}}",
               "PropertyType": "{{string}}",
               "Required": {{boolean}}
            },
            "ClientSecret": {
               "AllowedValues": [ "{{string}}" ],
               "DefaultValue": "{{string}}",
               "KeyOverride": "{{string}}",
               "Name": "{{string}}",
               "PropertyLocation": "{{string}}",
               "PropertyType": "{{string}}",
               "Required": {{boolean}}
            },
            "ContentType": "{{string}}",
            "RequestMethod": "{{string}}",
            "Scope": {
               "AllowedValues": [ "{{string}}" ],
               "DefaultValue": "{{string}}",
               "KeyOverride": "{{string}}",
               "Name": "{{string}}",
               "PropertyLocation": "{{string}}",
               "PropertyType": "{{string}}",
               "Required": {{boolean}}
            },
            "TokenUrl": {
               "AllowedValues": [ "{{string}}" ],
               "DefaultValue": "{{string}}",
               "KeyOverride": "{{string}}",
               "Name": "{{string}}",
               "PropertyLocation": "{{string}}",
               "PropertyType": "{{string}}",
               "Required": {{boolean}}
            },
            "TokenUrlParameters": [
               {
                  "AllowedValues": [ "{{string}}" ],
                  "DefaultValue": "{{string}}",
                  "KeyOverride": "{{string}}",
                  "Name": "{{string}}",
                  "PropertyLocation": "{{string}}",
                  "PropertyType": "{{string}}",
                  "Required": {{boolean}}
               }
            ]
         },
         "JWTBearerProperties": {
            "ContentType": "{{string}}",
            "JwtToken": {
               "AllowedValues": [ "{{string}}" ],
               "DefaultValue": "{{string}}",
               "KeyOverride": "{{string}}",
               "Name": "{{string}}",
               "PropertyLocation": "{{string}}",
               "PropertyType": "{{string}}",
               "Required": {{boolean}}
            },
            "RequestMethod": "{{string}}",
            "TokenUrl": {
               "AllowedValues": [ "{{string}}" ],
               "DefaultValue": "{{string}}",
               "KeyOverride": "{{string}}",
               "Name": "{{string}}",
               "PropertyLocation": "{{string}}",
               "PropertyType": "{{string}}",
               "Required": {{boolean}}
            },
            "TokenUrlParameters": [
               {
                  "AllowedValues": [ "{{string}}" ],
                  "DefaultValue": "{{string}}",
                  "KeyOverride": "{{string}}",
                  "Name": "{{string}}",
                  "PropertyLocation": "{{string}}",
                  "PropertyType": "{{string}}",
                  "Required": {{boolean}}
               }
            ]
         },
         "OAuth2GrantType": "{{string}}"
      }
   },
   "Description": "{{string}}",
   "IntegrationType": "{{string}}",
   "RestConfiguration": {
      "EntityConfigurations": {
         "{{string}}" : {
            "Schema": {
               "{{string}}" : {
                  "FieldDataType": "{{string}}",
                  "Name": "{{string}}"
               }
            },
            "SourceConfiguration": {
               "PaginationConfiguration": {
                  "CursorConfiguration": {
                     "LimitParameter": {
                        "DefaultValue": "{{string}}",
                        "Key": "{{string}}",
                        "PropertyLocation": "{{string}}",
                        "Value": {
                           "ContentPath": "{{string}}",
                           "HeaderKey": "{{string}}"
                        }
                     },
                     "NextPage": {
                        "DefaultValue": "{{string}}",
                        "Key": "{{string}}",
                        "PropertyLocation": "{{string}}",
                        "Value": {
                           "ContentPath": "{{string}}",
                           "HeaderKey": "{{string}}"
                        }
                     }
                  },
                  "OffsetConfiguration": {
                     "LimitParameter": {
                        "DefaultValue": "{{string}}",
                        "Key": "{{string}}",
                        "PropertyLocation": "{{string}}",
                        "Value": {
                           "ContentPath": "{{string}}",
                           "HeaderKey": "{{string}}"
                        }
                     },
                     "OffsetParameter": {
                        "DefaultValue": "{{string}}",
                        "Key": "{{string}}",
                        "PropertyLocation": "{{string}}",
                        "Value": {
                           "ContentPath": "{{string}}",
                           "HeaderKey": "{{string}}"
                        }
                     }
                  }
               },
               "RequestMethod": "{{string}}",
               "RequestParameters": [
                  {
                     "AllowedValues": [ "{{string}}" ],
                     "DefaultValue": "{{string}}",
                     "KeyOverride": "{{string}}",
                     "Name": "{{string}}",
                     "PropertyLocation": "{{string}}",
                     "PropertyType": "{{string}}",
                     "Required": {{boolean}}
                  }
               ],
               "RequestPath": "{{string}}",
               "ResponseConfiguration": {
                  "ErrorPath": "{{string}}",
                  "ResultPath": "{{string}}"
               }
            }
         }
      },
      "GlobalSourceConfiguration": {
         "PaginationConfiguration": {
            "CursorConfiguration": {
               "LimitParameter": {
                  "DefaultValue": "{{string}}",
                  "Key": "{{string}}",
                  "PropertyLocation": "{{string}}",
                  "Value": {
                     "ContentPath": "{{string}}",
                     "HeaderKey": "{{string}}"
                  }
               },
               "NextPage": {
                  "DefaultValue": "{{string}}",
                  "Key": "{{string}}",
                  "PropertyLocation": "{{string}}",
                  "Value": {
                     "ContentPath": "{{string}}",
                     "HeaderKey": "{{string}}"
                  }
               }
            },
            "OffsetConfiguration": {
               "LimitParameter": {
                  "DefaultValue": "{{string}}",
                  "Key": "{{string}}",
                  "PropertyLocation": "{{string}}",
                  "Value": {
                     "ContentPath": "{{string}}",
                     "HeaderKey": "{{string}}"
                  }
               },
               "OffsetParameter": {
                  "DefaultValue": "{{string}}",
                  "Key": "{{string}}",
                  "PropertyLocation": "{{string}}",
                  "Value": {
                     "ContentPath": "{{string}}",
                     "HeaderKey": "{{string}}"
                  }
               }
            }
         },
         "RequestMethod": "{{string}}",
         "RequestParameters": [
            {
               "AllowedValues": [ "{{string}}" ],
               "DefaultValue": "{{string}}",
               "KeyOverride": "{{string}}",
               "Name": "{{string}}",
               "PropertyLocation": "{{string}}",
               "PropertyType": "{{string}}",
               "Required": {{boolean}}
            }
         ],
         "RequestPath": "{{string}}",
         "ResponseConfiguration": {
            "ErrorPath": "{{string}}",
            "ResultPath": "{{string}}"
         }
      },
      "ValidationEndpointConfiguration": {
         "PaginationConfiguration": {
            "CursorConfiguration": {
               "LimitParameter": {
                  "DefaultValue": "{{string}}",
                  "Key": "{{string}}",
                  "PropertyLocation": "{{string}}",
                  "Value": {
                     "ContentPath": "{{string}}",
                     "HeaderKey": "{{string}}"
                  }
               },
               "NextPage": {
                  "DefaultValue": "{{string}}",
                  "Key": "{{string}}",
                  "PropertyLocation": "{{string}}",
                  "Value": {
                     "ContentPath": "{{string}}",
                     "HeaderKey": "{{string}}"
                  }
               }
            },
            "OffsetConfiguration": {
               "LimitParameter": {
                  "DefaultValue": "{{string}}",
                  "Key": "{{string}}",
                  "PropertyLocation": "{{string}}",
                  "Value": {
                     "ContentPath": "{{string}}",
                     "HeaderKey": "{{string}}"
                  }
               },
               "OffsetParameter": {
                  "DefaultValue": "{{string}}",
                  "Key": "{{string}}",
                  "PropertyLocation": "{{string}}",
                  "Value": {
                     "ContentPath": "{{string}}",
                     "HeaderKey": "{{string}}"
                  }
               }
            }
         },
         "RequestMethod": "{{string}}",
         "RequestParameters": [
            {
               "AllowedValues": [ "{{string}}" ],
               "DefaultValue": "{{string}}",
               "KeyOverride": "{{string}}",
               "Name": "{{string}}",
               "PropertyLocation": "{{string}}",
               "PropertyType": "{{string}}",
               "Required": {{boolean}}
            }
         ],
         "RequestPath": "{{string}}",
         "ResponseConfiguration": {
            "ErrorPath": "{{string}}",
            "ResultPath": "{{string}}"
         }
      }
   },
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_RegisterConnectionType_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConnectionProperties](#API_RegisterConnectionType_RequestSyntax) **   <a name="Glue-RegisterConnectionType-request-ConnectionProperties"></a>
Defines the base URL and additional request parameters needed during connection creation for this connection type.
Type: [ConnectionPropertiesConfiguration](API_ConnectionPropertiesConfiguration.md) object
Required: Yes

 ** [ConnectionType](#API_RegisterConnectionType_RequestSyntax) **   <a name="Glue-RegisterConnectionType-request-ConnectionType"></a>
The name of the connection type. Must be between 1 and 255 characters and must be prefixed with "REST-" to indicate it is a REST-based connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [ConnectorAuthenticationConfiguration](#API_RegisterConnectionType_RequestSyntax) **   <a name="Glue-RegisterConnectionType-request-ConnectorAuthenticationConfiguration"></a>
Defines the supported authentication types and required properties for this connection type, including Basic, OAuth2, and Custom authentication methods.
Type: [ConnectorAuthenticationConfiguration](API_ConnectorAuthenticationConfiguration.md) object
Required: Yes

 ** [Description](#API_RegisterConnectionType_RequestSyntax) **   <a name="Glue-RegisterConnectionType-request-Description"></a>
A description of the connection type. Can be up to 2048 characters and provides details about the purpose and functionality of the connection type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [IntegrationType](#API_RegisterConnectionType_RequestSyntax) **   <a name="Glue-RegisterConnectionType-request-IntegrationType"></a>
The integration type for the connection. Currently only "REST" protocol is supported.
Type: String
Valid Values: `REST`
Required: Yes

 ** [RestConfiguration](#API_RegisterConnectionType_RequestSyntax) **   <a name="Glue-RegisterConnectionType-request-RestConfiguration"></a>
Defines the HTTP request and response configuration, validation endpoint, and entity configurations for REST API interactions.
Type: [RestConfiguration](API_RestConfiguration.md) object
Required: Yes

 ** [Tags](#API_RegisterConnectionType_RequestSyntax) **   <a name="Glue-RegisterConnectionType-request-Tags"></a>
The tags you assign to the connection type.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_RegisterConnectionType_ResponseSyntax"></a>

```
{
   "ConnectionTypeArn": "string"
}
```

## Response Elements
<a name="API_RegisterConnectionType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectionTypeArn](#API_RegisterConnectionType_ResponseSyntax) **   <a name="Glue-RegisterConnectionType-response-ConnectionTypeArn"></a>
The Amazon Resource Name (ARN) of the registered connection type. This unique identifier can be used to reference the connection type in other AWS Glue operations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.
Pattern: `arn:aws(-(cn|us-gov|iso(-[bef])?))?:glue:.*`

## Errors
<a name="API_RegisterConnectionType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ResourceNumberLimitExceededException **
A resource numerical limit was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ValidationException **
A value could not be validated.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_RegisterConnectionType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/RegisterConnectionType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/RegisterConnectionType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/RegisterConnectionType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/RegisterConnectionType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/RegisterConnectionType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/RegisterConnectionType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/RegisterConnectionType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/RegisterConnectionType)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/RegisterConnectionType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/RegisterConnectionType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
