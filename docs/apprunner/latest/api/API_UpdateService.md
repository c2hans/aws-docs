---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_UpdateService.html
---

# UpdateService
<a name="API_UpdateService"></a>

**Important**
 AWS App Runner will no longer be open to new customers starting March 31, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

Update an AWS App Runner service. You can update the source configuration and instance configuration of the service. You can also update the ARN of the auto scaling configuration resource that's associated with the service. However, you can't change the name or the encryption configuration of the service. These can be set only when you create the service.

To update the tags applied to your service, use the separate actions [TagResource](API_TagResource.md) and [UntagResource](API_UntagResource.md).

This is an asynchronous operation. On a successful call, you can use the returned `OperationId` and the [ListOperations](API_ListOperations.md) call to track the operation's progress.

## Request Syntax
<a name="API_UpdateService_RequestSyntax"></a>

```
{
   "AutoScalingConfigurationArn": "{{string}}",
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
   "ServiceArn": "{{string}}",
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
   }
}
```

## Request Parameters
<a name="API_UpdateService_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AutoScalingConfigurationArn](#API_UpdateService_RequestSyntax) **   <a name="apprunner-UpdateService-request-AutoScalingConfigurationArn"></a>
The Amazon Resource Name (ARN) of an App Runner automatic scaling configuration resource that you want to associate with the App Runner service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: No

 ** [HealthCheckConfiguration](#API_UpdateService_RequestSyntax) **   <a name="apprunner-UpdateService-request-HealthCheckConfiguration"></a>
The settings for the health check that AWS App Runner performs to monitor the health of the App Runner service.
Type: [HealthCheckConfiguration](API_HealthCheckConfiguration.md) object
Required: No

 ** [InstanceConfiguration](#API_UpdateService_RequestSyntax) **   <a name="apprunner-UpdateService-request-InstanceConfiguration"></a>
The runtime configuration to apply to instances (scaling units) of your service.
Type: [InstanceConfiguration](API_InstanceConfiguration.md) object
Required: No

 ** [NetworkConfiguration](#API_UpdateService_RequestSyntax) **   <a name="apprunner-UpdateService-request-NetworkConfiguration"></a>
Configuration settings related to network traffic of the web application that the App Runner service runs.
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object
Required: No

 ** [ObservabilityConfiguration](#API_UpdateService_RequestSyntax) **   <a name="apprunner-UpdateService-request-ObservabilityConfiguration"></a>
The observability configuration of your service.
Type: [ServiceObservabilityConfiguration](API_ServiceObservabilityConfiguration.md) object
Required: No

 ** [ServiceArn](#API_UpdateService_RequestSyntax) **   <a name="apprunner-UpdateService-request-ServiceArn"></a>
The Amazon Resource Name (ARN) of the App Runner service that you want to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: Yes

 ** [SourceConfiguration](#API_UpdateService_RequestSyntax) **   <a name="apprunner-UpdateService-request-SourceConfiguration"></a>
The source configuration to apply to the App Runner service.
You can change the configuration of the code or image repository that the service uses. However, you can't switch from code to image or the other way around. This means that you must provide the same structure member of `SourceConfiguration` that you originally included when you created the service. Specifically, you can include either `CodeRepository` or `ImageRepository`. To update the source configuration, set the values to members of the structure that you include.
Type: [SourceConfiguration](API_SourceConfiguration.md) object
Required: No

## Response Syntax
<a name="API_UpdateService_ResponseSyntax"></a>

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
<a name="API_UpdateService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OperationId](#API_UpdateService_ResponseSyntax) **   <a name="apprunner-UpdateService-response-OperationId"></a>
The unique ID of the asynchronous operation that this request started. You can use it combined with the [ListOperations](API_ListOperations.md) call to track the operation's progress.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}`

 ** [Service](#API_UpdateService_ResponseSyntax) **   <a name="apprunner-UpdateService-response-Service"></a>
A description of the App Runner service updated by this request. All configuration values in the returned `Service` structure reflect configuration changes that are being applied by this request.
Type: [Service](API_Service.md) object

## Errors
<a name="API_UpdateService_Errors"></a>

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
<a name="API_UpdateService_Examples"></a>

### Update memory size
<a name="API_UpdateService_Example_1"></a>

This example illustrates how to update the memory size of instances (scaling units) of an App Runner service to 2048 MiB.

When the call succeeds, App Runner starts an asynchronous update process. The `Service` structure that's returned by the call reflects the new memory value that's being applied by this call.

#### Sample Request
<a name="API_UpdateService_Example_1_Request"></a>

```
$ aws apprunner update-service --cli-input-json "`cat`"
{
  "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa",
  "InstanceConfiguration": {
    "Memory": "4 GB"
  }
}
```

#### Sample Response
<a name="API_UpdateService_Example_1_Response"></a>

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
      "Memory": "4 GB"
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
<a name="API_UpdateService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apprunner-2020-05-15/UpdateService)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apprunner-2020-05-15/UpdateService)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/UpdateService)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apprunner-2020-05-15/UpdateService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/UpdateService)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apprunner-2020-05-15/UpdateService)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apprunner-2020-05-15/UpdateService)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apprunner-2020-05-15/UpdateService)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apprunner-2020-05-15/UpdateService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/UpdateService)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
