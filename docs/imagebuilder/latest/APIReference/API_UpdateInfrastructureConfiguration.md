---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_UpdateInfrastructureConfiguration.html
---

# UpdateInfrastructureConfiguration
<a name="API_UpdateInfrastructureConfiguration"></a>

Updates a new infrastructure configuration. An infrastructure configuration defines the environment in which your image will be built and tested.

## Request Syntax
<a name="API_UpdateInfrastructureConfiguration_RequestSyntax"></a>

```
PUT /UpdateInfrastructureConfiguration HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "infrastructureConfigurationArn": "{{string}}",
   "instanceMetadataOptions": {
      "httpPutResponseHopLimit": {{number}},
      "httpTokens": "{{string}}"
   },
   "instanceProfileName": "{{string}}",
   "instanceTypes": [ "{{string}}" ],
   "keyPair": "{{string}}",
   "logging": {
      "s3Logs": {
         "s3BucketName": "{{string}}",
         "s3KeyPrefix": "{{string}}"
      }
   },
   "placement": {
      "availabilityZone": "{{string}}",
      "hostId": "{{string}}",
      "hostResourceGroupArn": "{{string}}",
      "tenancy": "{{string}}"
   },
   "resourceTags": {
      "{{string}}" : "{{string}}"
   },
   "securityGroupIds": [ "{{string}}" ],
   "snsTopicArn": "{{string}}",
   "subnetId": "{{string}}",
   "terminateInstanceOnFailure": {{boolean}}
}
```

## URI Request Parameters
<a name="API_UpdateInfrastructureConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateInfrastructureConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-UpdateInfrastructureConfiguration-request-clientToken"></a>
Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [description](#API_UpdateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-UpdateInfrastructureConfiguration-request-description"></a>
The description of the infrastructure configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [infrastructureConfigurationArn](#API_UpdateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-UpdateInfrastructureConfiguration-request-infrastructureConfigurationArn"></a>
The Amazon Resource Name (ARN) of the infrastructure configuration that you want to update.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):infrastructure-configuration/[a-z0-9-_]+$`
Required: Yes

 ** [instanceMetadataOptions](#API_UpdateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-UpdateInfrastructureConfiguration-request-instanceMetadataOptions"></a>
The instance metadata options that you can set for the HTTP requests that pipeline builds use to launch EC2 build and test instances. For more information about instance metadata options, see one of the following links:
+  [Configure the instance metadata options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html) in the * *Amazon EC2 User Guide* * for Linux instances.
+  [Configure the instance metadata options](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/configuring-instance-metadata-options.html) in the * *Amazon EC2 Windows Guide* * for Windows instances.
Type: [InstanceMetadataOptions](API_InstanceMetadataOptions.md) object
Required: No

 ** [instanceProfileName](#API_UpdateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-UpdateInfrastructureConfiguration-request-instanceProfileName"></a>
The instance profile to associate with the instance used to customize your Amazon EC2 AMI.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[\w+=,.@-]+$`
Required: Yes

 ** [instanceTypes](#API_UpdateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-UpdateInfrastructureConfiguration-request-instanceTypes"></a>
The instance types of the infrastructure configuration. You can specify one or more instance types to use for this build. The service will pick one of these instance types based on availability.
Type: Array of strings
Required: No

 ** [keyPair](#API_UpdateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-UpdateInfrastructureConfiguration-request-keyPair"></a>
The key pair of the infrastructure configuration. You can use this to log on to and debug the instance used to create your image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [logging](#API_UpdateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-UpdateInfrastructureConfiguration-request-logging"></a>
The logging configuration of the infrastructure configuration.
Type: [Logging](API_Logging.md) object
Required: No

 ** [placement](#API_UpdateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-UpdateInfrastructureConfiguration-request-placement"></a>
The instance placement settings that define where the instances that are launched from your image will run.
Type: [Placement](API_Placement.md) object
Required: No

 ** [resourceTags](#API_UpdateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-UpdateInfrastructureConfiguration-request-resourceTags"></a>
The tags attached to the resource created by Image Builder.
Type: String to string map
Map Entries: Maximum number of 30 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [securityGroupIds](#API_UpdateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-UpdateInfrastructureConfiguration-request-securityGroupIds"></a>
The security group IDs to associate with the instance used to customize your Amazon EC2 AMI.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [snsTopicArn](#API_UpdateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-UpdateInfrastructureConfiguration-request-snsTopicArn"></a>
The Amazon Resource Name (ARN) for the SNS topic to which we send image build event notifications.
EC2 Image Builder is unable to send notifications to SNS topics that are encrypted using keys from other accounts. The key that is used to encrypt the SNS topic must reside in the account that the Image Builder service runs under.
Type: String
Pattern: `^arn:aws[^:]*:sns:[^:]+:[0-9]{12}:[a-zA-Z0-9-_]{1,256}$`
Required: No

 ** [subnetId](#API_UpdateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-UpdateInfrastructureConfiguration-request-subnetId"></a>
The subnet ID to place the instance used to customize your Amazon EC2 AMI in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [terminateInstanceOnFailure](#API_UpdateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-UpdateInfrastructureConfiguration-request-terminateInstanceOnFailure"></a>
The terminate instance on failure setting of the infrastructure configuration. Set to false if you want Image Builder to retain the instance used to configure your AMI if the build or test phase of your workflow fails.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdateInfrastructureConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clientToken": "string",
   "infrastructureConfigurationArn": "string",
   "requestId": "string"
}
```

## Response Elements
<a name="API_UpdateInfrastructureConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_UpdateInfrastructureConfiguration_ResponseSyntax) **   <a name="imagebuilder-UpdateInfrastructureConfiguration-response-clientToken"></a>
The client token that uniquely identifies the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [infrastructureConfigurationArn](#API_UpdateInfrastructureConfiguration_ResponseSyntax) **   <a name="imagebuilder-UpdateInfrastructureConfiguration-response-infrastructureConfigurationArn"></a>
The Amazon Resource Name (ARN) of the infrastructure configuration that was updated by this request.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):infrastructure-configuration/[a-z0-9-_]+$`

 ** [requestId](#API_UpdateInfrastructureConfiguration_ResponseSyntax) **   <a name="imagebuilder-UpdateInfrastructureConfiguration-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_UpdateInfrastructureConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the specific operation.
HTTP Status Code: 429

 ** ClientException **
These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** IdempotentParameterMismatchException **
You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.
HTTP Status Code: 400

 ** InvalidRequestException **
You have requested an action that that the service doesn't support.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource that you are trying to operate on is currently in use. Review the message details and retry later.
HTTP Status Code: 400

 ** ServiceException **
This exception is thrown when the service encounters an unrecoverable exception.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## See Also
<a name="API_UpdateInfrastructureConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/UpdateInfrastructureConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/UpdateInfrastructureConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/UpdateInfrastructureConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/UpdateInfrastructureConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/UpdateInfrastructureConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/UpdateInfrastructureConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/UpdateInfrastructureConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/UpdateInfrastructureConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/UpdateInfrastructureConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/UpdateInfrastructureConfiguration)
