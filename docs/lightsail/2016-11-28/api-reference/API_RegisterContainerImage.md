---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_RegisterContainerImage.html
---

# RegisterContainerImage
<a name="API_RegisterContainerImage"></a>

Registers a container image to your Amazon Lightsail container service.

**Note**
This action is not required if you install and use the Lightsail Control (lightsailctl) plugin to push container images to your Lightsail container service. For more information, see [Pushing and managing container images on your Amazon Lightsail container services](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-pushing-container-images) in the *Amazon Lightsail Developer Guide*.

## Request Syntax
<a name="API_RegisterContainerImage_RequestSyntax"></a>

```
{
   "digest": "{{string}}",
   "label": "{{string}}",
   "serviceName": "{{string}}"
}
```

## Request Parameters
<a name="API_RegisterContainerImage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [digest](#API_RegisterContainerImage_RequestSyntax) **   <a name="Lightsail-RegisterContainerImage-request-digest"></a>
The digest of the container image to be registered.
Type: String
Required: Yes

 ** [label](#API_RegisterContainerImage_RequestSyntax) **   <a name="Lightsail-RegisterContainerImage-request-label"></a>
The label for the container image when it's registered to the container service.
Use a descriptive label that you can use to track the different versions of your registered container images.
Use the `GetContainerImages` action to return the container images registered to a Lightsail container service. The label is the `<imagelabel>` portion of the following image name example:
+  `:container-service-1.<imagelabel>.1`
If the name of your container service is `mycontainerservice`, and the label that you specify is `mystaticwebsite`, then the name of the registered container image will be `:mycontainerservice.mystaticwebsite.1`.
The number at the end of these image name examples represents the version of the registered container image. If you push and register another container image to the same Lightsail container service, with the same label, then the version number for the new registered container image will be `2`. If you push and register another container image, the version number will be `3`, and so on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 53.
Pattern: `^[a-z0-9]{1,2}|[a-z0-9][a-z0-9-]+[a-z0-9]$`
Required: Yes

 ** [serviceName](#API_RegisterContainerImage_RequestSyntax) **   <a name="Lightsail-RegisterContainerImage-request-serviceName"></a>
The name of the container service for which to register a container image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-z0-9]{1,2}|[a-z0-9][a-z0-9-]+[a-z0-9]$`
Required: Yes

## Response Syntax
<a name="API_RegisterContainerImage_ResponseSyntax"></a>

```
{
   "containerImage": {
      "createdAt": number,
      "digest": "string",
      "image": "string"
   }
}
```

## Response Elements
<a name="API_RegisterContainerImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [containerImage](#API_RegisterContainerImage_ResponseSyntax) **   <a name="Lightsail-RegisterContainerImage-response-containerImage"></a>
An object that describes a container image that is registered to a Lightsail container service
Type: [ContainerImage](API_ContainerImage.md) object

## Errors
<a name="API_RegisterContainerImage_Errors"></a>

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
<a name="API_RegisterContainerImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/RegisterContainerImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/RegisterContainerImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/RegisterContainerImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/RegisterContainerImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/RegisterContainerImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/RegisterContainerImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/RegisterContainerImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/RegisterContainerImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/RegisterContainerImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/RegisterContainerImage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
