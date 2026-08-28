---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DescribeConnectionType.html
---

# DescribeConnectionType
<a name="API_DescribeConnectionType"></a>

The `DescribeConnectionType` API provides full details of the supported options for a given connection type in AWS Glue. The response includes authentication configuration details that show supported authentication types and properties, and RestConfiguration for custom REST-based connection types registered via `RegisterConnectionType`.

See also: `ListConnectionTypes`, `RegisterConnectionType`, `DeleteConnectionType`

## Request Syntax
<a name="API_DescribeConnectionType_RequestSyntax"></a>

```
{
   "ConnectionType": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeConnectionType_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConnectionType](#API_DescribeConnectionType_RequestSyntax) **   <a name="Glue-DescribeConnectionType-request-ConnectionType"></a>
The name of the connection type to be described.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_DescribeConnectionType_ResponseSyntax"></a>

```
{
   "AthenaConnectionProperties": {
      "string" : {
         "AllowedValues": [
            {
               "Description": "string",
               "Value": "string"
            }
         ],
         "DataOperationScopes": [ "string" ],
         "DefaultValue": "string",
         "Description": "string",
         "KeyOverride": "string",
         "Name": "string",
         "PropertyLocation": "string",
         "PropertyTypes": [ "string" ],
         "Required": boolean
      }
   },
   "AuthenticationConfiguration": {
      "AuthenticationType": {
         "AllowedValues": [
            {
               "Description": "string",
               "Value": "string"
            }
         ],
         "DataOperationScopes": [ "string" ],
         "DefaultValue": "string",
         "Description": "string",
         "KeyOverride": "string",
         "Name": "string",
         "PropertyLocation": "string",
         "PropertyTypes": [ "string" ],
         "Required": boolean
      },
      "BasicAuthenticationProperties": {
         "string" : {
            "AllowedValues": [
               {
                  "Description": "string",
                  "Value": "string"
               }
            ],
            "DataOperationScopes": [ "string" ],
            "DefaultValue": "string",
            "Description": "string",
            "KeyOverride": "string",
            "Name": "string",
            "PropertyLocation": "string",
            "PropertyTypes": [ "string" ],
            "Required": boolean
         }
      },
      "CustomAuthenticationProperties": {
         "string" : {
            "AllowedValues": [
               {
                  "Description": "string",
                  "Value": "string"
               }
            ],
            "DataOperationScopes": [ "string" ],
            "DefaultValue": "string",
            "Description": "string",
            "KeyOverride": "string",
            "Name": "string",
            "PropertyLocation": "string",
            "PropertyTypes": [ "string" ],
            "Required": boolean
         }
      },
      "OAuth2Properties": {
         "string" : {
            "AllowedValues": [
               {
                  "Description": "string",
                  "Value": "string"
               }
            ],
            "DataOperationScopes": [ "string" ],
            "DefaultValue": "string",
            "Description": "string",
            "KeyOverride": "string",
            "Name": "string",
            "PropertyLocation": "string",
            "PropertyTypes": [ "string" ],
            "Required": boolean
         }
      },
      "SecretArn": {
         "AllowedValues": [
            {
               "Description": "string",
               "Value": "string"
            }
         ],
         "DataOperationScopes": [ "string" ],
         "DefaultValue": "string",
         "Description": "string",
         "KeyOverride": "string",
         "Name": "string",
         "PropertyLocation": "string",
         "PropertyTypes": [ "string" ],
         "Required": boolean
      }
   },
   "Capabilities": {
      "SupportedAuthenticationTypes": [ "string" ],
      "SupportedComputeEnvironments": [ "string" ],
      "SupportedDataOperations": [ "string" ]
   },
   "ComputeEnvironmentConfigurations": {
      "string" : {
         "ComputeEnvironment": "string",
         "ConnectionOptionNameOverrides": {
            "string" : "string"
         },
         "ConnectionOptions": {
            "string" : {
               "AllowedValues": [
                  {
                     "Description": "string",
                     "Value": "string"
                  }
               ],
               "DataOperationScopes": [ "string" ],
               "DefaultValue": "string",
               "Description": "string",
               "KeyOverride": "string",
               "Name": "string",
               "PropertyLocation": "string",
               "PropertyTypes": [ "string" ],
               "Required": boolean
            }
         },
         "ConnectionPropertiesRequiredOverrides": [ "string" ],
         "ConnectionPropertyNameOverrides": {
            "string" : "string"
         },
         "Description": "string",
         "Name": "string",
         "PhysicalConnectionPropertiesRequired": boolean,
         "SupportedAuthenticationTypes": [ "string" ]
      }
   },
   "ConnectionOptions": {
      "string" : {
         "AllowedValues": [
            {
               "Description": "string",
               "Value": "string"
            }
         ],
         "DataOperationScopes": [ "string" ],
         "DefaultValue": "string",
         "Description": "string",
         "KeyOverride": "string",
         "Name": "string",
         "PropertyLocation": "string",
         "PropertyTypes": [ "string" ],
         "Required": boolean
      }
   },
   "ConnectionProperties": {
      "string" : {
         "AllowedValues": [
            {
               "Description": "string",
               "Value": "string"
            }
         ],
         "DataOperationScopes": [ "string" ],
         "DefaultValue": "string",
         "Description": "string",
         "KeyOverride": "string",
         "Name": "string",
         "PropertyLocation": "string",
         "PropertyTypes": [ "string" ],
         "Required": boolean
      }
   },
   "ConnectionType": "string",
   "Description": "string",
   "PhysicalConnectionRequirements": {
      "string" : {
         "AllowedValues": [
            {
               "Description": "string",
               "Value": "string"
            }
         ],
         "DataOperationScopes": [ "string" ],
         "DefaultValue": "string",
         "Description": "string",
         "KeyOverride": "string",
         "Name": "string",
         "PropertyLocation": "string",
         "PropertyTypes": [ "string" ],
         "Required": boolean
      }
   },
   "PythonConnectionProperties": {
      "string" : {
         "AllowedValues": [
            {
               "Description": "string",
               "Value": "string"
            }
         ],
         "DataOperationScopes": [ "string" ],
         "DefaultValue": "string",
         "Description": "string",
         "KeyOverride": "string",
         "Name": "string",
         "PropertyLocation": "string",
         "PropertyTypes": [ "string" ],
         "Required": boolean
      }
   },
   "RestConfiguration": {
      "EntityConfigurations": {
         "string" : {
            "Schema": {
               "string" : {
                  "FieldDataType": "string",
                  "Name": "string"
               }
            },
            "SourceConfiguration": {
               "PaginationConfiguration": {
                  "CursorConfiguration": {
                     "LimitParameter": {
                        "DefaultValue": "string",
                        "Key": "string",
                        "PropertyLocation": "string",
                        "Value": {
                           "ContentPath": "string",
                           "HeaderKey": "string"
                        }
                     },
                     "NextPage": {
                        "DefaultValue": "string",
                        "Key": "string",
                        "PropertyLocation": "string",
                        "Value": {
                           "ContentPath": "string",
                           "HeaderKey": "string"
                        }
                     }
                  },
                  "OffsetConfiguration": {
                     "LimitParameter": {
                        "DefaultValue": "string",
                        "Key": "string",
                        "PropertyLocation": "string",
                        "Value": {
                           "ContentPath": "string",
                           "HeaderKey": "string"
                        }
                     },
                     "OffsetParameter": {
                        "DefaultValue": "string",
                        "Key": "string",
                        "PropertyLocation": "string",
                        "Value": {
                           "ContentPath": "string",
                           "HeaderKey": "string"
                        }
                     }
                  }
               },
               "RequestMethod": "string",
               "RequestParameters": [
                  {
                     "AllowedValues": [ "string" ],
                     "DefaultValue": "string",
                     "KeyOverride": "string",
                     "Name": "string",
                     "PropertyLocation": "string",
                     "PropertyType": "string",
                     "Required": boolean
                  }
               ],
               "RequestPath": "string",
               "ResponseConfiguration": {
                  "ErrorPath": "string",
                  "ResultPath": "string"
               }
            }
         }
      },
      "GlobalSourceConfiguration": {
         "PaginationConfiguration": {
            "CursorConfiguration": {
               "LimitParameter": {
                  "DefaultValue": "string",
                  "Key": "string",
                  "PropertyLocation": "string",
                  "Value": {
                     "ContentPath": "string",
                     "HeaderKey": "string"
                  }
               },
               "NextPage": {
                  "DefaultValue": "string",
                  "Key": "string",
                  "PropertyLocation": "string",
                  "Value": {
                     "ContentPath": "string",
                     "HeaderKey": "string"
                  }
               }
            },
            "OffsetConfiguration": {
               "LimitParameter": {
                  "DefaultValue": "string",
                  "Key": "string",
                  "PropertyLocation": "string",
                  "Value": {
                     "ContentPath": "string",
                     "HeaderKey": "string"
                  }
               },
               "OffsetParameter": {
                  "DefaultValue": "string",
                  "Key": "string",
                  "PropertyLocation": "string",
                  "Value": {
                     "ContentPath": "string",
                     "HeaderKey": "string"
                  }
               }
            }
         },
         "RequestMethod": "string",
         "RequestParameters": [
            {
               "AllowedValues": [ "string" ],
               "DefaultValue": "string",
               "KeyOverride": "string",
               "Name": "string",
               "PropertyLocation": "string",
               "PropertyType": "string",
               "Required": boolean
            }
         ],
         "RequestPath": "string",
         "ResponseConfiguration": {
            "ErrorPath": "string",
            "ResultPath": "string"
         }
      },
      "ValidationEndpointConfiguration": {
         "PaginationConfiguration": {
            "CursorConfiguration": {
               "LimitParameter": {
                  "DefaultValue": "string",
                  "Key": "string",
                  "PropertyLocation": "string",
                  "Value": {
                     "ContentPath": "string",
                     "HeaderKey": "string"
                  }
               },
               "NextPage": {
                  "DefaultValue": "string",
                  "Key": "string",
                  "PropertyLocation": "string",
                  "Value": {
                     "ContentPath": "string",
                     "HeaderKey": "string"
                  }
               }
            },
            "OffsetConfiguration": {
               "LimitParameter": {
                  "DefaultValue": "string",
                  "Key": "string",
                  "PropertyLocation": "string",
                  "Value": {
                     "ContentPath": "string",
                     "HeaderKey": "string"
                  }
               },
               "OffsetParameter": {
                  "DefaultValue": "string",
                  "Key": "string",
                  "PropertyLocation": "string",
                  "Value": {
                     "ContentPath": "string",
                     "HeaderKey": "string"
                  }
               }
            }
         },
         "RequestMethod": "string",
         "RequestParameters": [
            {
               "AllowedValues": [ "string" ],
               "DefaultValue": "string",
               "KeyOverride": "string",
               "Name": "string",
               "PropertyLocation": "string",
               "PropertyType": "string",
               "Required": boolean
            }
         ],
         "RequestPath": "string",
         "ResponseConfiguration": {
            "ErrorPath": "string",
            "ResultPath": "string"
         }
      }
   },
   "SparkConnectionProperties": {
      "string" : {
         "AllowedValues": [
            {
               "Description": "string",
               "Value": "string"
            }
         ],
         "DataOperationScopes": [ "string" ],
         "DefaultValue": "string",
         "Description": "string",
         "KeyOverride": "string",
         "Name": "string",
         "PropertyLocation": "string",
         "PropertyTypes": [ "string" ],
         "Required": boolean
      }
   }
}
```

## Response Elements
<a name="API_DescribeConnectionType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AthenaConnectionProperties](#API_DescribeConnectionType_ResponseSyntax) **   <a name="Glue-DescribeConnectionType-response-AthenaConnectionProperties"></a>
Connection properties specific to the Athena compute environment.
Type: String to [Property](API_Property.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [AuthenticationConfiguration](#API_DescribeConnectionType_ResponseSyntax) **   <a name="Glue-DescribeConnectionType-response-AuthenticationConfiguration"></a>
The type of authentication used for the connection.
Type: [AuthConfiguration](API_AuthConfiguration.md) object

 ** [Capabilities](#API_DescribeConnectionType_ResponseSyntax) **   <a name="Glue-DescribeConnectionType-response-Capabilities"></a>
The supported authentication types, data interface types (compute environments), and data operations of the connector.
Type: [Capabilities](API_Capabilities.md) object

 ** [ComputeEnvironmentConfigurations](#API_DescribeConnectionType_ResponseSyntax) **   <a name="Glue-DescribeConnectionType-response-ComputeEnvironmentConfigurations"></a>
The compute environments that are supported by the connection.
Type: String to [ComputeEnvironmentConfiguration](API_ComputeEnvironmentConfiguration.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [ConnectionOptions](#API_DescribeConnectionType_ResponseSyntax) **   <a name="Glue-DescribeConnectionType-response-ConnectionOptions"></a>
Returns properties that can be set when creating a connection in the `ConnectionInput.ConnectionProperties`. `ConnectionOptions` defines parameters that can be set in a Spark ETL script in the connection options map passed to a dataframe.
Type: String to [Property](API_Property.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [ConnectionProperties](#API_DescribeConnectionType_ResponseSyntax) **   <a name="Glue-DescribeConnectionType-response-ConnectionProperties"></a>
Connection properties which are common across compute environments.
Type: String to [Property](API_Property.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [ConnectionType](#API_DescribeConnectionType_ResponseSyntax) **   <a name="Glue-DescribeConnectionType-response-ConnectionType"></a>
The name of the connection type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [Description](#API_DescribeConnectionType_ResponseSyntax) **   <a name="Glue-DescribeConnectionType-response-Description"></a>
A description of the connection type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [PhysicalConnectionRequirements](#API_DescribeConnectionType_ResponseSyntax) **   <a name="Glue-DescribeConnectionType-response-PhysicalConnectionRequirements"></a>
Physical requirements for a connection, such as VPC, Subnet and Security Group specifications.
Type: String to [Property](API_Property.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [PythonConnectionProperties](#API_DescribeConnectionType_ResponseSyntax) **   <a name="Glue-DescribeConnectionType-response-PythonConnectionProperties"></a>
Connection properties specific to the Python compute environment.
Type: String to [Property](API_Property.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [RestConfiguration](#API_DescribeConnectionType_ResponseSyntax) **   <a name="Glue-DescribeConnectionType-response-RestConfiguration"></a>
HTTP request and response configuration, validation endpoint, and entity configurations for REST based data source.
Type: [RestConfiguration](API_RestConfiguration.md) object

 ** [SparkConnectionProperties](#API_DescribeConnectionType_ResponseSyntax) **   <a name="Glue-DescribeConnectionType-response-SparkConnectionProperties"></a>
Connection properties specific to the Spark compute environment.
Type: String to [Property](API_Property.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.

## Errors
<a name="API_DescribeConnectionType_Errors"></a>

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

 ** ValidationException **
A value could not be validated.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_DescribeConnectionType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/DescribeConnectionType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/DescribeConnectionType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DescribeConnectionType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/DescribeConnectionType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DescribeConnectionType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/DescribeConnectionType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/DescribeConnectionType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/DescribeConnectionType)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/DescribeConnectionType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DescribeConnectionType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
