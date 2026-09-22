---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateInfrastructureConfiguration.html
---

# CreateInfrastructureConfiguration
<a name="API_CreateInfrastructureConfiguration"></a>

Creates a new infrastructure configuration. An infrastructure configuration defines the environment in which your image will be built and tested.

## Request Syntax
<a name="API_CreateInfrastructureConfiguration_RequestSyntax"></a>

```
PUT /CreateInfrastructureConfiguration HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "dryRun": {{boolean}},
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
   "name": "{{string}}",
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
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "terminateInstanceOnFailure": {{boolean}}
}
```

## URI Request Parameters
<a name="API_CreateInfrastructureConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateInfrastructureConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-CreateInfrastructureConfiguration-request-clientToken"></a>
A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [description](#API_CreateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-CreateInfrastructureConfiguration-request-description"></a>
The description of the infrastructure configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [dryRun](#API_CreateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-CreateInfrastructureConfiguration-request-dryRun"></a>
Validates the required permissions and request parameters without performing the operation. If validation succeeds, the operation returns a `DryRunOperationException` error response.
Type: Boolean
Required: No

 ** [instanceMetadataOptions](#API_CreateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-CreateInfrastructureConfiguration-request-instanceMetadataOptions"></a>
The instance metadata service (IMDS) settings that Image Builder applies to the EC2 build and test instances it launches during image creation. If you don't set these options, the EC2 launch defaults for the instance apply. For more information about instance metadata options, see one of the following links:
+  [Configure the instance metadata options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html) in the * *Amazon EC2 User Guide* * for Linux instances.
+  [Configure the instance metadata options](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/configuring-instance-metadata-options.html) in the * *Amazon EC2 Windows Guide* * for Windows instances.
Type: [InstanceMetadataOptions](API_InstanceMetadataOptions.md) object
Required: No

 ** [instanceProfileName](#API_CreateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-CreateInfrastructureConfiguration-request-instanceProfileName"></a>
The instance profile to associate with the instance used to customize your Amazon EC2 AMI. The instance profile must exist in your account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[\w+=,.@-]+$`
Required: Yes

 ** [instanceTypes](#API_CreateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-CreateInfrastructureConfiguration-request-instanceTypes"></a>
The instance types of the infrastructure configuration. You can specify one or more instance types to use for this build. Image Builder picks one of these instance types based on availability. If you don't specify instance types, Image Builder selects compatible instance types automatically. If you specify a Dedicated Host, Image Builder uses only instance types that the host supports.
Type: Array of strings
Required: No

 ** [keyPair](#API_CreateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-CreateInfrastructureConfiguration-request-keyPair"></a>
The key pair of the infrastructure configuration. You can use this to log on to and debug the instance used to create your image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [logging](#API_CreateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-CreateInfrastructureConfiguration-request-logging"></a>
The logging configuration of the infrastructure configuration. When you configure S3 logs, Image Builder writes logs from the build and test process to the specified bucket under the key prefix.
Type: [Logging](API_Logging.md) object
Required: No

 ** [name](#API_CreateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-CreateInfrastructureConfiguration-request-name"></a>
The name of the infrastructure configuration. Infrastructure configuration names must be unique to your account in each AWS Region. Image Builder generates the infrastructure configuration ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: Yes

 ** [placement](#API_CreateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-CreateInfrastructureConfiguration-request-placement"></a>
The instance placement settings that define where the build and test instances that Image Builder launches during image creation run. These settings don't affect instances that you launch from the output image.
Type: [Placement](API_Placement.md) object
Required: No

 ** [resourceTags](#API_CreateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-CreateInfrastructureConfiguration-request-resourceTags"></a>
The metadata tags to assign to the Amazon EC2 instance that Image Builder launches during the build process. Tags are formatted as key value pairs. Tag keys can't begin with `aws:` or match one of the following reserved keys: `CreatedBy`, `Ec2ImageBuilderArn`, `Name`, or `Tags`.
Type: String to string map
Map Entries: Maximum number of 30 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [securityGroupIds](#API_CreateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-CreateInfrastructureConfiguration-request-securityGroupIds"></a>
The security group IDs to associate with the instance used to customize your Amazon EC2 AMI.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [snsTopicArn](#API_CreateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-CreateInfrastructureConfiguration-request-snsTopicArn"></a>
The Amazon Resource Name (ARN) of the SNS topic to which Image Builder sends image build event notifications. Specify a standard topic. Image Builder doesn't support FIFO topics. Image Builder validates the topic when you create or update the configuration. You must have permission to publish to the topic.
EC2 Image Builder can't send notifications to SNS topics that are encrypted using keys from other accounts. If your SNS topic is encrypted, the key must be owned by the same account that owns your Image Builder resources.
Type: String
Pattern: `^arn:aws[^:]*:sns:[^:]+:[0-9]{12}:[a-zA-Z0-9-_]{1,256}$`
Required: No

 ** [subnetId](#API_CreateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-CreateInfrastructureConfiguration-request-subnetId"></a>
The subnet ID in which to place the instance used to customize your Amazon EC2 AMI. If you specify `subnetId`, you must also specify one or more security group IDs in `securityGroupIds`. Otherwise, the request fails.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [tags](#API_CreateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-CreateInfrastructureConfiguration-request-tags"></a>
The metadata tags to assign to the infrastructure configuration resource that Image Builder creates as output. Tags are formatted as key value pairs.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [terminateInstanceOnFailure](#API_CreateInfrastructureConfiguration_RequestSyntax) **   <a name="imagebuilder-CreateInfrastructureConfiguration-request-terminateInstanceOnFailure"></a>
Specifies whether to terminate the instance on failure. Set to false if you want Image Builder to retain the instance used to configure your AMI if the build or test phase of your workflow fails. Defaults to `true`.
Type: Boolean
Required: No

## Response Syntax
<a name="API_CreateInfrastructureConfiguration_ResponseSyntax"></a>

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
<a name="API_CreateInfrastructureConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_CreateInfrastructureConfiguration_ResponseSyntax) **   <a name="imagebuilder-CreateInfrastructureConfiguration-response-clientToken"></a>
The client token that uniquely identifies the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [infrastructureConfigurationArn](#API_CreateInfrastructureConfiguration_ResponseSyntax) **   <a name="imagebuilder-CreateInfrastructureConfiguration-response-infrastructureConfigurationArn"></a>
The Amazon Resource Name (ARN) of the infrastructure configuration that was created by this request.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):infrastructure-configuration/[a-z0-9-_]+$`

 ** [requestId](#API_CreateInfrastructureConfiguration_ResponseSyntax) **   <a name="imagebuilder-CreateInfrastructureConfiguration-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_CreateInfrastructureConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.
HTTP Status Code: 429

 ** ClientException **
A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.
HTTP Status Code: 400

 ** DryRunOperationException **
The dry run operation of the resource was successful, and no resources or mutations were actually performed due to the dry run flag in the request.
HTTP Status Code: 412

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** IdempotentParameterMismatchException **
You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is malformed or otherwise invalid. Verify the request and try again.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
The resource that you are trying to create already exists.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource that you are trying to operate on is currently in use. Review the message details and retry later.
HTTP Status Code: 400

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
You have exceeded the number of permitted resources or operations for this service. For service quotas, see [EC2 Image Builder endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder).
HTTP Status Code: 402

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_CreateInfrastructureConfiguration_Examples"></a>

### Create an infrastructure configuration
<a name="API_CreateInfrastructureConfiguration_Example_1"></a>

The following example creates an infrastructure configuration that gives Image Builder a choice of two instance types for its build and test instances.

#### Sample Request
<a name="API_CreateInfrastructureConfiguration_Example_1_Request"></a>

```
PUT /CreateInfrastructureConfiguration HTTP/1.1
Content-type: application/json

{
    "name": "my-example-infrastructure",
    "description": "An infrastructure configuration for Amazon Linux builds",
    "instanceProfileName": "EC2InstanceProfileForImageBuilder",
    "instanceTypes": ["t3.medium", "t3.large"],
    "terminateInstanceOnFailure": true,
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333"
}
```

#### Sample Response
<a name="API_CreateInfrastructureConfiguration_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "67082698-415b-4d9f-8be0-84a58380b93f",
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
    "infrastructureConfigurationArn": "arn:aws:imagebuilder:us-west-2:111122223333:infrastructure-configuration/my-example-infrastructure"
}
```

### Create an infrastructure configuration with instance placement and metadata options
<a name="API_CreateInfrastructureConfiguration_Example_2"></a>

The following example creates an infrastructure configuration. It places your build and test instances in a single Availability Zone and requires IMDSv2 for instance metadata requests. It also applies resource tags to the resources that Image Builder creates during the build.

#### Sample Request
<a name="API_CreateInfrastructureConfiguration_Example_2_Request"></a>

```
PUT /CreateInfrastructureConfiguration HTTP/1.1
Content-type: application/json

{
    "name": "my-example-infrastructure",
    "description": "An infrastructure configuration that pins build instances to one Availability Zone and requires IMDSv2",
    "instanceProfileName": "my-example-instance-role",
    "placement": {
        "availabilityZone": "us-west-2a"
    },
    "instanceMetadataOptions": {
        "httpTokens": "required",
        "httpPutResponseHopLimit": 2
    },
    "resourceTags": {
        "CostCenter": "12345",
        "Environment": "test"
    },
    "terminateInstanceOnFailure": true,
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE98765"
}
```

#### Sample Response
<a name="API_CreateInfrastructureConfiguration_Example_2_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "b96b54d8-daa6-4fdf-b25a-7b570bc2ab25",
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE98765",
    "infrastructureConfigurationArn": "arn:aws:imagebuilder:us-west-2:111122223333:infrastructure-configuration/my-example-infrastructure"
}
```

## See Also
<a name="API_CreateInfrastructureConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/CreateInfrastructureConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/CreateInfrastructureConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/CreateInfrastructureConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/CreateInfrastructureConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/CreateInfrastructureConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/CreateInfrastructureConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/CreateInfrastructureConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/CreateInfrastructureConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/CreateInfrastructureConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/CreateInfrastructureConfiguration)
