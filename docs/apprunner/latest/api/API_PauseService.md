---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_PauseService.html
---

# PauseService
<a name="API_PauseService"></a>

**Important**
 AWS App Runner will no longer be open to new customers starting March 31, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

Pause an active AWS App Runner service. App Runner reduces compute capacity for the service to zero and loses state (for example, ephemeral storage is removed).

This is an asynchronous operation. On a successful call, you can use the returned `OperationId` and the [ListOperations](API_ListOperations.md) call to track the operation's progress.

## Request Syntax
<a name="API_PauseService_RequestSyntax"></a>

```
{
   "ServiceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_PauseService_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ServiceArn](#API_PauseService_RequestSyntax) **   <a name="apprunner-PauseService-request-ServiceArn"></a>
The Amazon Resource Name (ARN) of the App Runner service that you want to pause.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: Yes

## Response Syntax
<a name="API_PauseService_ResponseSyntax"></a>

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
<a name="API_PauseService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OperationId](#API_PauseService_ResponseSyntax) **   <a name="apprunner-PauseService-response-OperationId"></a>
The unique ID of the asynchronous operation that this request started. You can use it combined with the [ListOperations](API_ListOperations.md) call to track the operation's progress.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}`

 ** [Service](#API_PauseService_ResponseSyntax) **   <a name="apprunner-PauseService-response-Service"></a>
A description of the App Runner service that this request just paused.
Type: [Service](API_Service.md) object

## Errors
<a name="API_PauseService_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceErrorException **
An unexpected service exception occurred.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.
HTTP Status Code: 400

 ** InvalidStateException **
You can't perform this action when the resource is in its current state.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource doesn't exist for the specified Amazon Resource Name (ARN) in your AWS account.
HTTP Status Code: 400

## Examples
<a name="API_PauseService_Examples"></a>

### Pause a service
<a name="API_PauseService_Example_1"></a>

This example illustrates pausing an App Runner service.

#### Sample Request
<a name="API_PauseService_Example_1_Request"></a>

```
$ aws apprunner pause-service --cli-input-json "`cat`"
{
  "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa"
}
```

#### Sample Response
<a name="API_PauseService_Example_1_Response"></a>

```
{
  "OperationId": "17fe9f55-7e91-4097-b243-fcabbb69a4cf",
  "Service": {
    "CreatedAt": "2020-11-20T19:05:25Z",
    "UpdatedAt": "2020-11-23T12:41:37Z",
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
            "BuildCommand": "[pip install -r requirements.txt]",
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

## See Also
<a name="API_PauseService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apprunner-2020-05-15/PauseService)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apprunner-2020-05-15/PauseService)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/PauseService)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apprunner-2020-05-15/PauseService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/PauseService)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apprunner-2020-05-15/PauseService)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apprunner-2020-05-15/PauseService)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apprunner-2020-05-15/PauseService)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/apprunner-2020-05-15/PauseService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/PauseService)
