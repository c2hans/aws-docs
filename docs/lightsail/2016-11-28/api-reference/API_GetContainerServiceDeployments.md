---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetContainerServiceDeployments.html
---

# GetContainerServiceDeployments
<a name="API_GetContainerServiceDeployments"></a>

Returns the deployments for your Amazon Lightsail container service

A deployment specifies the settings, such as the ports and launch command, of containers that are deployed to your container service.

The deployments are ordered by version in ascending order. The newest version is listed at the top of the response.

**Note**
A set number of deployments are kept before the oldest one is replaced with the newest one. For more information, see [Amazon Lightsail endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/lightsail.html) in the * AWS General Reference*.

## Request Syntax
<a name="API_GetContainerServiceDeployments_RequestSyntax"></a>

```
{
   "serviceName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetContainerServiceDeployments_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [serviceName](#API_GetContainerServiceDeployments_RequestSyntax) **   <a name="Lightsail-GetContainerServiceDeployments-request-serviceName"></a>
The name of the container service for which to return deployments.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-z0-9]{1,2}|[a-z0-9][a-z0-9-]+[a-z0-9]$`
Required: Yes

## Response Syntax
<a name="API_GetContainerServiceDeployments_ResponseSyntax"></a>

```
{
   "deployments": [
      {
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
      }
   ]
}
```

## Response Elements
<a name="API_GetContainerServiceDeployments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deployments](#API_GetContainerServiceDeployments_ResponseSyntax) **   <a name="Lightsail-GetContainerServiceDeployments-response-deployments"></a>
An array of objects that describe deployments for a container service.
Type: Array of [ContainerServiceDeployment](API_ContainerServiceDeployment.md) objects

## Errors
<a name="API_GetContainerServiceDeployments_Errors"></a>

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
<a name="API_GetContainerServiceDeployments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/GetContainerServiceDeployments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/GetContainerServiceDeployments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/GetContainerServiceDeployments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/GetContainerServiceDeployments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/GetContainerServiceDeployments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/GetContainerServiceDeployments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/GetContainerServiceDeployments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/GetContainerServiceDeployments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/GetContainerServiceDeployments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/GetContainerServiceDeployments)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
