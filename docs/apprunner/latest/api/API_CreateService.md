---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_CreateService.html
---

# CreateService
<a name="API_CreateService"></a>

**Important**
 AWS App Runner will no longer be open to new customers starting March 31, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

Create an AWS App Runner service. After the service is created, the action also automatically starts a deployment.

This is an asynchronous operation. On a successful call, you can use the returned `OperationId` and the [ListOperations](https://docs.aws.amazon.com/apprunner/latest/api/API_ListOperations.html) call to track the operation's progress.

## Request Syntax
<a name="API_CreateService_RequestSyntax"></a>

```
{
   "AutoScalingConfigurationArn": "{{string}}",
   "EncryptionConfiguration": {
      "KmsKey": "{{string}}"
   },
   "HealthCheckConfiguration": {
      "HealthyThreshold": {{number}},
      "Interval": {{number}},
      "Path": "{{string}}",
      "Protocol": "{{string}}",
      "Timeout": {{number}},
      "UnhealthyThreshold": {{number}}
   },
   "InstanceConfiguration": {
      "Cpu": "{{string}}",
      "InstanceRoleArn": "{{string}}",
      "Memory": "{{string}}"
   },
   "NetworkConfiguration": {
      "EgressConfiguration": {
         "EgressType": "{{string}}",
         "VpcConnectorArn": "{{string}}"
      },
      "IngressConfiguration": {
         "IsPubliclyAccessible": {{boolean}}
      },
      "IpAddressType": "{{string}}"
   },
   "ObservabilityConfiguration": {
      "ObservabilityConfigurationArn": "{{string}}",
      "ObservabilityEnabled": {{boolean}}
   },
   "ServiceName": "{{string}}",
   "SourceConfiguration": {
      "AuthenticationConfiguration": {
         "AccessRoleArn": "{{string}}",
         "ConnectionArn": "{{string}}"
      },
      "AutoDeploymentsEnabled": {{boolean}},
      "CodeRepository": {
         "CodeConfiguration": {
            "CodeConfigurationValues": {
               "BuildCommand": "{{string}}",
               "Port": "{{string}}",
               "Runtime": "{{string}}",
               "RuntimeEnvironmentSecrets": {
                  "{{string}}" : "{{string}}"
               },
               "RuntimeEnvironmentVariables": {
                  "{{string}}" : "{{string}}"
               },
               "StartCommand": "{{string}}"
            },
            "ConfigurationSource": "{{string}}"
         },
         "RepositoryUrl": "{{string}}",
         "SourceCodeVersion": {
            "Type": "{{string}}",
            "Value": "{{string}}"
         },
         "SourceDirectory": "{{string}}"
      },
      "ImageRepository": {
         "ImageConfiguration": {
            "Port": "{{string}}",
            "RuntimeEnvironmentSecrets": {
               "{{string}}" : "{{string}}"
            },
            "RuntimeEnvironmentVariables": {
               "{{string}}" : "{{string}}"
            },
            "StartCommand": "{{string}}"
         },
         "ImageIdentifier": "{{string}}",
         "ImageRepositoryType": "{{string}}"
      }
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateService_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AutoScalingConfigurationArn](#API_CreateService_RequestSyntax) **   <a name="apprunner-CreateService-request-AutoScalingConfigurationArn"></a>
The Amazon Resource Name (ARN) of an App Runner automatic scaling configuration resource that you want to associate with your service. If not provided, App Runner associates the latest revision of a default auto scaling configuration.
Specify an ARN with a name and a revision number to associate that revision. For example: `arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/3`
Specify just the name to associate the latest revision. For example: `arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: No

 ** [EncryptionConfiguration](#API_CreateService_RequestSyntax) **   <a name="apprunner-CreateService-request-EncryptionConfiguration"></a>
An optional custom encryption key that App Runner uses to encrypt the copy of your source repository that it maintains and your service logs. By default, App Runner uses an AWS managed key.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: No

 ** [HealthCheckConfiguration](#API_CreateService_RequestSyntax) **   <a name="apprunner-CreateService-request-HealthCheckConfiguration"></a>
The settings for the health check that AWS App Runner performs to monitor the health of the App Runner service.
Type: [HealthCheckConfiguration](API_HealthCheckConfiguration.md) object
Required: No

 ** [InstanceConfiguration](#API_CreateService_RequestSyntax) **   <a name="apprunner-CreateService-request-InstanceConfiguration"></a>
The runtime configuration of instances (scaling units) of your service.
Type: [InstanceConfiguration](API_InstanceConfiguration.md) object
Required: No

 ** [NetworkConfiguration](#API_CreateService_RequestSyntax) **   <a name="apprunner-CreateService-request-NetworkConfiguration"></a>
Configuration settings related to network traffic of the web application that the App Runner service runs.
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object
Required: No

 ** [ObservabilityConfiguration](#API_CreateService_RequestSyntax) **   <a name="apprunner-CreateService-request-ObservabilityConfiguration"></a>
The observability configuration of your service.
Type: [ServiceObservabilityConfiguration](API_ServiceObservabilityConfiguration.md) object
Required: No

 ** [ServiceName](#API_CreateService_RequestSyntax) **   <a name="apprunner-CreateService-request-ServiceName"></a>
A name for the App Runner service. It must be unique across all the running App Runner services in your AWS account in the AWS Region.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Pattern: `[A-Za-z0-9][A-Za-z0-9-_]{3,39}`
Required: Yes

 ** [SourceConfiguration](#API_CreateService_RequestSyntax) **   <a name="apprunner-CreateService-request-SourceConfiguration"></a>
The source to deploy to the App Runner service. It can be a code or an image repository.
Type: [SourceConfiguration](API_SourceConfiguration.md) object
Required: Yes

 ** [Tags](#API_CreateService_RequestSyntax) **   <a name="apprunner-CreateService-request-Tags"></a>
An optional list of metadata items that you can associate with the App Runner service resource. A tag is a key-value pair.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateService_ResponseSyntax"></a>

```
{
   "OperationId": "string",
   "Service": {
      "AutoScalingConfigurationSummary": {
         "AutoScalingConfigurationArn": "string",
         "AutoScalingConfigurationName": "string",
         "AutoScalingConfigurationRevision": number,
         "CreatedAt": number,
         "HasAssociatedService": boolean,
         "IsDefault": boolean,
         "Status": "string"
      },
      "CreatedAt": number,
      "DeletedAt": number,
      "EncryptionConfiguration": {
         "KmsKey": "string"
      },
      "HealthCheckConfiguration": {
         "HealthyThreshold": number,
         "Interval": number,
         "Path": "string",
         "Protocol": "string",
         "Timeout": number,
         "UnhealthyThreshold": number
      },
      "InstanceConfiguration": {
         "Cpu": "string",
         "InstanceRoleArn": "string",
         "Memory": "string"
      },
      "NetworkConfiguration": {
         "EgressConfiguration": {
            "EgressType": "string",
            "VpcConnectorArn": "string"
         },
         "IngressConfiguration": {
            "IsPubliclyAccessible": boolean
         },
         "IpAddressType": "string"
      },
      "ObservabilityConfiguration": {
         "ObservabilityConfigurationArn": "string",
         "ObservabilityEnabled": boolean
      },
      "ServiceArn": "string",
      "ServiceId": "string",
      "ServiceName": "string",
      "ServiceUrl": "string",
      "SourceConfiguration": {
         "AuthenticationConfiguration": {
            "AccessRoleArn": "string",
            "ConnectionArn": "string"
         },
         "AutoDeploymentsEnabled": boolean,
         "CodeRepository": {
            "CodeConfiguration": {
               "CodeConfigurationValues": {
                  "BuildCommand": "string",
                  "Port": "string",
                  "Runtime": "string",
                  "RuntimeEnvironmentSecrets": {
                     "string" : "string"
                  },
                  "RuntimeEnvironmentVariables": {
                     "string" : "string"
                  },
                  "StartCommand": "string"
               },
               "ConfigurationSource": "string"
            },
            "RepositoryUrl": "string",
            "SourceCodeVersion": {
               "Type": "string",
               "Value": "string"
            },
            "SourceDirectory": "string"
         },
         "ImageRepository": {
            "ImageConfiguration": {
               "Port": "string",
               "RuntimeEnvironmentSecrets": {
                  "string" : "string"
               },
               "RuntimeEnvironmentVariables": {
                  "string" : "string"
               },
               "StartCommand": "string"
            },
            "ImageIdentifier": "string",
            "ImageRepositoryType": "string"
         }
      },
      "Status": "string",
      "UpdatedAt": number
   }
}
```

## Response Elements
<a name="API_CreateService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OperationId](#API_CreateService_ResponseSyntax) **   <a name="apprunner-CreateService-response-OperationId"></a>
The unique ID of the asynchronous operation that this request started. You can use it combined with the [ListOperations](https://docs.aws.amazon.com/apprunner/latest/api/API_ListOperations.html) call to track the operation's progress.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}`

 ** [Service](#API_CreateService_ResponseSyntax) **   <a name="apprunner-CreateService-response-Service"></a>
A description of the App Runner service that's created by this request.
Type: [Service](API_Service.md) object

## Errors
<a name="API_CreateService_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceErrorException **
An unexpected service exception occurred.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
App Runner can't create this resource. You've reached your account quota for this resource type.
For App Runner per-resource quotas, see [AWS App Runner endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/apprunner.html) in the * AWS General Reference*.
HTTP Status Code: 400

## Examples
<a name="API_CreateService_Examples"></a>

### Create a source code repository service
<a name="API_CreateService_Example_1"></a>

This example illustrates how to create an App Runner service based on a Python source code repository.

#### Sample Request
<a name="API_CreateService_Example_1_Request"></a>

```
$ aws apprunner create-service --cli-input-json "`cat`"
{
  "ServiceName": "python-app",
  "SourceConfiguration": {
    "AuthenticationConfiguration": {
      "ConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:connection/my-github-connection/e7656250f67242d7819feade6800f59e"
    },
    "AutoDeploymentsEnabled": true,
    "CodeRepository": {
      "RepositoryUrl": "https://github.com/my-account/python-hello",
      "SourceCodeVersion": {
        "Type": "BRANCH",
        "Value": "main"
      },
      "CodeConfiguration": {
        "ConfigurationSource": "API",
        "CodeConfigurationValues": {
          "Runtime": "PYTHON_3",
          "BuildCommand": "pip install -r requirements.txt",
          "StartCommand": "python server.py",
          "Port": "8080",
          "RuntimeEnvironmentVariables": [
            {
              "NAME": "Jane"
            }
          ]
        }
      }
    }
  },
  "InstanceConfiguration": {
    "CPU": "1 vCPU",
    "Memory": "3 GB"
  }
}
```

#### Sample Response
<a name="API_CreateService_Example_1_Response"></a>

```
{
  "OperationId": "17fe9f55-7e91-4097-b243-fcabbb69a4cf",
  "Service": {
    "CreatedAt": "2020-11-20T19:05:25Z",
    "UpdatedAt": "2020-11-20T19:05:25Z",
    "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa",
    "ServiceId": "8fe1e10304f84fd2b0df550fe98a71fa",
    "ServiceName": "python-app",
    "ServiceUrl": "psbqam834h.us-east-1.awsapprunner.com",
    "SourceConfiguration": {
      "AuthenticationConfiguration": {
        "ConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:connection/my-github-connection/e7656250f67242d7819feade6800f59e"
      },
      "AutoDeploymentsEnabled": true,
      "CodeRepository": {
        "CodeConfiguration": {
          "CodeConfigurationValues": {
            "BuildCommand": "pip install -r requirements.txt",
            "Port": "8080",
            "Runtime": "PYTHON_3",
            "RuntimeEnvironmentVariables": [
              {
                "NAME": "Jane"
              }
            ],
            "StartCommand": "python server.py"
          },
          "ConfigurationSource": "Api"
        },
        "RepositoryUrl": "https://github.com/my-account/python-hello",
        "SourceCodeVersion": {
          "Type": "BRANCH",
          "Value": "main"
        }
      }
    },
    "Status": "OPERATION_IN_PROGRESS",
    "InstanceConfiguration": {
      "CPU": "1 vCPU",
      "Memory": "3 GB"
    },
    "NetworkConfiguration": {
      "IpAddressType": "IPV4",
      "EgressConfiguration": {
        "EgressType": "DEFAULT"
      },
      "IngressConfiguration": {
        "IsPubliclyAccessible": true
      }
    },
    "ObservabilityConfiguration": {
      "ObservabilityEnabled": false
    }
  }
}
```

### Create a source image repository service
<a name="API_CreateService_Example_2"></a>

This example illustrates how to create an App Runner service based on an image stored in Elastic Container Registry (ECR).

#### Sample Request
<a name="API_CreateService_Example_2_Request"></a>

```
$ aws apprunner create-service --cli-input-json "`cat`"
{
  "ServiceName": "golang-container-app",
  "SourceConfiguration": {
    "AuthenticationConfiguration": {
      "AccessRoleArn": "arn:aws:iam::123456789012:role/my-ecr-role"
    },
    "AutoDeploymentsEnabled": true,
    "ImageRepository": {
      "ImageIdentifier": "123456789012.dkr.ecr.us-east-1.amazonaws.com/golang-app:latest",
      "ImageConfiguration": {
        "Port": "8080",
        "RuntimeEnvironmentVariables": [
          {
            "NAME": "Jane"
          }
        ]
      },
      "ImageRepositoryType": "ECR"
    }
  },
  "InstanceConfiguration": {
    "CPU": "1 vCPU",
    "Memory": "3 GB"
  }
}
```

#### Sample Response
<a name="API_CreateService_Example_2_Response"></a>

```
{
  "OperationId": "17fe9f55-7e91-4097-b243-fcabbb69a4cf",
  "Service": {
    "CreatedAt": "2020-11-06T23:15:30Z",
    "UpdatedAt": "2020-11-06T23:15:30Z",
    "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/golang-container-app/51728f8a20ce46d39b25398a6c8e9d1a",
    "ServiceId": "51728f8a20ce46d39b25398a6c8e9d1a",
    "ServiceName": "golang-container-app",
    "ServiceUrl": "psbqam834h.us-east-1.awsapprunner.com",
    "SourceConfiguration": {
      "AuthenticationConfiguration": {
        "AccessRoleArn": "arn:aws:iam::123456789012:role/my-ecr-role"
      },
      "AutoDeploymentsEnabled": true,
      "ImageRepository": {
        "ImageIdentifier": "123456789012.dkr.ecr.us-east-1.amazonaws.com/golang-app:latest",
        "ImageConfiguration": {
          "Port": "8080",
          "RuntimeEnvironmentVariables": [
            {
              "NAME": "Jane"
            }
          ]
        },
        "ImageRepositoryType": "ECR"
      }
    },
    "Status": "OPERATION_IN_PROGRESS",
    "InstanceConfiguration": {
      "CPU": "1 vCPU",
      "Memory": "3 GB"
    },
    "NetworkConfiguration": {
      "IpAddressType": "IPV4",
      "EgressConfiguration": {
        "EgressType": "DEFAULT"
      },
      "IngressConfiguration": {
        "IsPubliclyAccessible": true
      }
    },
    "ObservabilityConfiguration": {
      "ObservabilityEnabled": false
    }
  }
}
```

## See Also
<a name="API_CreateService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apprunner-2020-05-15/CreateService)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apprunner-2020-05-15/CreateService)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/CreateService)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apprunner-2020-05-15/CreateService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/CreateService)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apprunner-2020-05-15/CreateService)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apprunner-2020-05-15/CreateService)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apprunner-2020-05-15/CreateService)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/apprunner-2020-05-15/CreateService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/CreateService)
