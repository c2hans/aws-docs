---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateContainerService.html
---

# CreateContainerService
<a name="API_CreateContainerService"></a>

Creates an Amazon Lightsail container service.

A Lightsail container service is a compute resource to which you can deploy containers. For more information, see [Container services in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-container-services) in the *Lightsail Dev Guide*.

## Request Syntax
<a name="API_CreateContainerService_RequestSyntax"></a>

```
{
   "deployment": {
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
      }
   },
   "power": "{{string}}",
   "privateRegistryAccess": {
      "ecrImagePullerRole": {
         "isActive": {{boolean}}
      }
   },
   "publicDomainNames": {
      "{{string}}" : [ "{{string}}" ]
   },
   "scale": {{number}},
   "serviceName": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateContainerService_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [deployment](#API_CreateContainerService_RequestSyntax) **   <a name="Lightsail-CreateContainerService-request-deployment"></a>
An object that describes a deployment for the container service.
A deployment specifies the containers that will be launched on the container service and their settings, such as the ports to open, the environment variables to apply, and the launch command to run. It also specifies the container that will serve as the public endpoint of the deployment and its settings, such as the HTTP or HTTPS port to use, and the health check configuration.
Type: [ContainerServiceDeploymentRequest](API_ContainerServiceDeploymentRequest.md) object
Required: No

 ** [power](#API_CreateContainerService_RequestSyntax) **   <a name="Lightsail-CreateContainerService-request-power"></a>
The power specification for the container service.
The power specifies the amount of memory, vCPUs, and base monthly cost of each node of the container service. The `power` and `scale` of a container service makes up its configured capacity. To determine the monthly price of your container service, multiply the base price of the `power` with the `scale` (the number of nodes) of the service.
Use the `GetContainerServicePowers` action to get a list of power options that you can specify using this parameter, and their base monthly cost.
Type: String
Valid Values: `nano | micro | small | medium | large | xlarge`
Required: Yes

 ** [privateRegistryAccess](#API_CreateContainerService_RequestSyntax) **   <a name="Lightsail-CreateContainerService-request-privateRegistryAccess"></a>
An object to describe the configuration for the container service to access private container image repositories, such as Amazon Elastic Container Registry (Amazon ECR) private repositories.
For more information, see [Configuring access to an Amazon ECR private repository for an Amazon Lightsail container service](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-container-service-ecr-private-repo-access) in the *Amazon Lightsail Developer Guide*.
Type: [PrivateRegistryAccessRequest](API_PrivateRegistryAccessRequest.md) object
Required: No

 ** [publicDomainNames](#API_CreateContainerService_RequestSyntax) **   <a name="Lightsail-CreateContainerService-request-publicDomainNames"></a>
The public domain names to use with the container service, such as `example.com` and `www.example.com`.
You can specify up to four public domain names for a container service. The domain names that you specify are used when you create a deployment with a container configured as the public endpoint of your container service.
If you don't specify public domain names, then you can use the default domain of the container service.
You must create and validate an SSL/TLS certificate before you can use public domain names with your container service. Use the `CreateCertificate` action to create a certificate for the public domain names you want to use with your container service.
You can specify public domain names using a string to array map as shown in the example later on this page.
Type: String to array of strings map
Required: No

 ** [scale](#API_CreateContainerService_RequestSyntax) **   <a name="Lightsail-CreateContainerService-request-scale"></a>
The scale specification for the container service.
The scale specifies the allocated compute nodes of the container service. The `power` and `scale` of a container service makes up its configured capacity. To determine the monthly price of your container service, multiply the base price of the `power` with the `scale` (the number of nodes) of the service.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: Yes

 ** [serviceName](#API_CreateContainerService_RequestSyntax) **   <a name="Lightsail-CreateContainerService-request-serviceName"></a>
The name for the container service.
The name that you specify for your container service will make up part of its default domain. The default domain of a container service is typically `https://<ServiceName>.<RandomGUID>.<AWSRegion>.cs.amazonlightsail.com`. If the name of your container service is `container-service-1`, and it's located in the US East (Ohio) AWS Region (`us-east-2`), then the domain for your container service will be like the following example: `https://container-service-1.ur4EXAMPLE2uq.us-east-2.cs.amazonlightsail.com`
The following are the requirements for container service names:
+ Must be unique within each AWS Region in your Lightsail account.
+ Must contain 1 to 63 characters.
+ Must contain only alphanumeric characters and hyphens.
+ A hyphen (-) can separate words but cannot be at the start or end of the name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-z0-9]{1,2}|[a-z0-9][a-z0-9-]+[a-z0-9]$`
Required: Yes

 ** [tags](#API_CreateContainerService_RequestSyntax) **   <a name="Lightsail-CreateContainerService-request-tags"></a>
The tag keys and optional values to add to the container service during create.
Use the `TagResource` action to tag a resource after it's created.
For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags).
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateContainerService_ResponseSyntax"></a>

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
<a name="API_CreateContainerService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [containerService](#API_CreateContainerService_ResponseSyntax) **   <a name="Lightsail-CreateContainerService-response-containerService"></a>
An object that describes a container service.
Type: [ContainerService](API_ContainerService.md) object

## Errors
<a name="API_CreateContainerService_Errors"></a>

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

## Examples
<a name="API_CreateContainerService_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Create container service
<a name="API_CreateContainerService_Example_1"></a>

The following example creates a new container service named `container-service-1` in the `us-west-2` AWS Region. It also specifies the `example.com`, `applications.example.com`, `www.example.com`, and `containers.example.com` public domains of the `example-com` SSL/TLS certificate.

#### Sample Request
<a name="API_CreateContainerService_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: lightsail.us-west-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: Lightsail_20161128.CreateContainerService
Content-Type: application/x-amz-json-1.1
User-Agent: AGENT
X-Amz-Date: 20201022T175000Z
Authorization: AUTHPARAMS
Content-Length: 195

{
    "serviceName": "container-service-1",
    "power": "nano",
    "scale": 1,
    "publicDomainNames": {
        "example-com": [
            "example.com",
            "applications.example.com",
            "www.example.com",
            "containers.example.com"
        ]
    }
}
```

#### Sample Response
<a name="API_CreateContainerService_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Thu, 22 Oct 2020 17:50:03 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 689
x-amzn-RequestId: 0459d37f-f6a7-4786-bc26-9EXAMPLEea99
Connection: keep-alive

{
    "containerService": {
        "arn": "arn:aws:lightsail:us-west-2:111122223333:ContainerService/9059c34a-f681-482f-b41d-0EXAMPLEc85e",
        "containerServiceName": "container-service-1",
        "createdAt": 1.603389001E9,
        "isDisabled": false,
        "location": {
            "availabilityZone": "all",
            "regionName": "us-west-2"
        },
        "power": "nano",
        "powerId": "nano-1",
        "principalArn": "",
        "privateDomainName": "container-service-1.service.local",
        "publicDomainNames": {
            "example-com": [
                "example.com",
                "applications.example.com",
                "www.example.com",
                "containers.example.com"
            ]
        },
        "resourceType": "ContainerService",
        "scale": 1,
        "state": "PENDING",
        "tags": [],
        "url": "https://container-service-1.ur1EXAMPLE2uq.us-west-2.cs.amazonlightsail.com/"
    }
}
```

## See Also
<a name="API_CreateContainerService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/CreateContainerService)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/CreateContainerService)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/CreateContainerService)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/CreateContainerService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/CreateContainerService)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/CreateContainerService)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/CreateContainerService)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/CreateContainerService)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/CreateContainerService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/CreateContainerService)
