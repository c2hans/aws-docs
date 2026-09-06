---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateContainerServiceDeployment.html
---

# CreateContainerServiceDeployment
<a name="API_CreateContainerServiceDeployment"></a>

Creates a deployment for your Amazon Lightsail container service.

A deployment specifies the containers that will be launched on the container service and their settings, such as the ports to open, the environment variables to apply, and the launch command to run. It also specifies the container that will serve as the public endpoint of the deployment and its settings, such as the HTTP or HTTPS port to use, and the health check configuration.

You can deploy containers to your container service using container images from a public registry such as Amazon ECR Public, or from your local machine. For more information, see [Creating container images for your Amazon Lightsail container services](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-creating-container-images) in the *Amazon Lightsail Developer Guide*.

## Request Syntax
<a name="API_CreateContainerServiceDeployment_RequestSyntax"></a>

```
{
   "containers": {
      "{{string}}" : {
         "command": [ "{{string}}" ],
         "environment": {
            "{{string}}" : "{{string}}"
         },
         "image": "{{string}}",
         "ports": {
            "{{string}}" : "{{string}}"
         }
      }
   },
   "publicEndpoint": {
      "containerName": "{{string}}",
      "containerPort": {{number}},
      "healthCheck": {
         "healthyThreshold": {{number}},
         "intervalSeconds": {{number}},
         "path": "{{string}}",
         "successCodes": "{{string}}",
         "timeoutSeconds": {{number}},
         "unhealthyThreshold": {{number}}
      }
   },
   "serviceName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateContainerServiceDeployment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [containers](#API_CreateContainerServiceDeployment_RequestSyntax) **   <a name="Lightsail-CreateContainerServiceDeployment-request-containers"></a>
An object that describes the settings of the containers that will be launched on the container service.
Type: String to [Container](API_Container.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 53.
Key Pattern: `^[a-z0-9]{1,2}|[a-z0-9][a-z0-9-]+[a-z0-9]$`
Required: No

 ** [publicEndpoint](#API_CreateContainerServiceDeployment_RequestSyntax) **   <a name="Lightsail-CreateContainerServiceDeployment-request-publicEndpoint"></a>
An object that describes the settings of the public endpoint for the container service.
Type: [EndpointRequest](API_EndpointRequest.md) object
Required: No

 ** [serviceName](#API_CreateContainerServiceDeployment_RequestSyntax) **   <a name="Lightsail-CreateContainerServiceDeployment-request-serviceName"></a>
The name of the container service for which to create the deployment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-z0-9]{1,2}|[a-z0-9][a-z0-9-]+[a-z0-9]$`
Required: Yes

## Response Syntax
<a name="API_CreateContainerServiceDeployment_ResponseSyntax"></a>

```
{
   "containerService": {
      "arn": "string",
      "containerServiceName": "string",
      "createdAt": number,
      "currentDeployment": {
         "containers": {
            "string" : {
               "command": [ "string" ],
               "environment": {
                  "string" : "string"
               },
               "image": "string",
               "ports": {
                  "string" : "string"
               }
            }
         },
         "createdAt": number,
         "publicEndpoint": {
            "containerName": "string",
            "containerPort": number,
            "healthCheck": {
               "healthyThreshold": number,
               "intervalSeconds": number,
               "path": "string",
               "successCodes": "string",
               "timeoutSeconds": number,
               "unhealthyThreshold": number
            }
         },
         "state": "string",
         "version": number
      },
      "isDisabled": boolean,
      "location": {
         "availabilityZone": "string",
         "regionName": "string"
      },
      "nextDeployment": {
         "containers": {
            "string" : {
               "command": [ "string" ],
               "environment": {
                  "string" : "string"
               },
               "image": "string",
               "ports": {
                  "string" : "string"
               }
            }
         },
         "createdAt": number,
         "publicEndpoint": {
            "containerName": "string",
            "containerPort": number,
            "healthCheck": {
               "healthyThreshold": number,
               "intervalSeconds": number,
               "path": "string",
               "successCodes": "string",
               "timeoutSeconds": number,
               "unhealthyThreshold": number
            }
         },
         "state": "string",
         "version": number
      },
      "power": "string",
      "powerId": "string",
      "principalArn": "string",
      "privateDomainName": "string",
      "privateRegistryAccess": {
         "ecrImagePullerRole": {
            "isActive": boolean,
            "principalArn": "string"
         }
      },
      "publicDomainNames": {
         "string" : [ "string" ]
      },
      "resourceType": "string",
      "scale": number,
      "state": "string",
      "stateDetail": {
         "code": "string",
         "message": "string"
      },
      "tags": [
         {
            "key": "string",
            "value": "string"
         }
      ],
      "url": "string"
   }
}
```

## Response Elements
<a name="API_CreateContainerServiceDeployment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [containerService](#API_CreateContainerServiceDeployment_ResponseSyntax) **   <a name="Lightsail-CreateContainerServiceDeployment-response-containerService"></a>
An object that describes a container service.
Type: [ContainerService](API_ContainerService.md) object

## Errors
<a name="API_CreateContainerServiceDeployment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
HTTP Status Code: 400

 ** InvalidInputException **
Lightsail throws this exception when user input does not conform to the validation rules of an input field.
Domain and distribution APIs are only available in the N. Virginia (`us-east-1`) AWS Region. Please set your AWS Region configuration to `us-east-1` to create, view, or edit these resources.
HTTP Status Code: 400

 ** NotFoundException **
Lightsail throws this exception when it cannot find a resource.
HTTP Status Code: 400

 ** RegionSetupInProgressException **
Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.
 ** docs **
 [Regions and Availability Zones for Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-regions-and-availability-zones-in-amazon-lightsail.html)
 ** tip **
Opt-in Regions typically take a few minutes to finish setting up before you can work with them. Wait a few minutes and try again.
HTTP Status Code: 400

 ** ServiceException **
A general service exception.
HTTP Status Code: 500

 ** UnauthenticatedException **
Lightsail throws this exception when the user has not been authenticated.
HTTP Status Code: 400

## See Also
<a name="API_CreateContainerServiceDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/CreateContainerServiceDeployment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/CreateContainerServiceDeployment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/CreateContainerServiceDeployment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/CreateContainerServiceDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/CreateContainerServiceDeployment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/CreateContainerServiceDeployment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/CreateContainerServiceDeployment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/CreateContainerServiceDeployment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/CreateContainerServiceDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/CreateContainerServiceDeployment)
