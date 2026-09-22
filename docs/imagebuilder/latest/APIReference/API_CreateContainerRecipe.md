---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateContainerRecipe.html
---

# CreateContainerRecipe
<a name="API_CreateContainerRecipe"></a>

Creates a new container recipe. Container recipes define how images are configured, tested, and assessed.

## Request Syntax
<a name="API_CreateContainerRecipe_RequestSyntax"></a>

```
PUT /CreateContainerRecipe HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "components": [
      {
         "componentArn": "{{string}}",
         "parameters": [
            {
               "name": "{{string}}",
               "value": [ "{{string}}" ]
            }
         ]
      }
   ],
   "containerType": "{{string}}",
   "description": "{{string}}",
   "dockerfileTemplateData": "{{string}}",
   "dockerfileTemplateUri": "{{string}}",
   "dryRun": {{boolean}},
   "imageOsVersionOverride": "{{string}}",
   "instanceConfiguration": {
      "blockDeviceMappings": [
         {
            "deviceName": "{{string}}",
            "ebs": {
               "deleteOnTermination": {{boolean}},
               "encrypted": {{boolean}},
               "iops": {{number}},
               "kmsKeyId": "{{string}}",
               "snapshotId": "{{string}}",
               "throughput": {{number}},
               "volumeSize": {{number}},
               "volumeType": "{{string}}"
            },
            "noDevice": "{{string}}",
            "virtualName": "{{string}}"
         }
      ],
      "image": "{{string}}"
   },
   "kmsKeyId": "{{string}}",
   "name": "{{string}}",
   "parentImage": "{{string}}",
   "platformOverride": "{{string}}",
   "semanticVersion": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "targetRepository": {
      "repositoryName": "{{string}}",
      "service": "{{string}}"
   },
   "workingDirectory": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateContainerRecipe_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateContainerRecipe_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateContainerRecipe_RequestSyntax) **   <a name="imagebuilder-CreateContainerRecipe-request-clientToken"></a>
A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [components](#API_CreateContainerRecipe_RequestSyntax) **   <a name="imagebuilder-CreateContainerRecipe-request-components"></a>
The components included in the container recipe. You can specify each component only one time in a recipe.
Type: Array of [ComponentConfiguration](API_ComponentConfiguration.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [containerType](#API_CreateContainerRecipe_RequestSyntax) **   <a name="imagebuilder-CreateContainerRecipe-request-containerType"></a>
The type of container to create.
Type: String
Valid Values: `DOCKER`
Required: Yes

 ** [description](#API_CreateContainerRecipe_RequestSyntax) **   <a name="imagebuilder-CreateContainerRecipe-request-description"></a>
The description of the container recipe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [dockerfileTemplateData](#API_CreateContainerRecipe_RequestSyntax) **   <a name="imagebuilder-CreateContainerRecipe-request-dockerfileTemplateData"></a>
The Dockerfile template used to build your image, as an inline data blob. You must specify exactly one of the `dockerfileTemplateData` or `dockerfileTemplateUri` properties. For the contextual variables that the template can include, see [Create a new version of a container recipe](https://docs.aws.amazon.com/imagebuilder/latest/userguide/create-container-recipes.html) in the *EC2 Image Builder User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16000.
Pattern: `[^\x00]+`
Required: No

 ** [dockerfileTemplateUri](#API_CreateContainerRecipe_RequestSyntax) **   <a name="imagebuilder-CreateContainerRecipe-request-dockerfileTemplateUri"></a>
The Amazon S3 URI for the Dockerfile template that is used to build your container image. You must have permission to read the object. Image Builder reads the object once, when it creates the recipe, and stores its content in the recipe. Later changes to the S3 object don't affect the recipe. You must specify exactly one of the `dockerfileTemplateData` or `dockerfileTemplateUri` properties.
Type: String
Required: No

 ** [dryRun](#API_CreateContainerRecipe_RequestSyntax) **   <a name="imagebuilder-CreateContainerRecipe-request-dryRun"></a>
Validates the required permissions and request parameters without performing the operation. If validation succeeds, the operation returns a `DryRunOperationException` error response.
Type: Boolean
Required: No

 ** [imageOsVersionOverride](#API_CreateContainerRecipe_RequestSyntax) **   <a name="imagebuilder-CreateContainerRecipe-request-imageOsVersionOverride"></a>
Specifies the operating system version for the base image. Use this property only when the base image is a container image from a registry. When the base image is an Image Builder image, the operating system version comes from the parent image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [instanceConfiguration](#API_CreateContainerRecipe_RequestSyntax) **   <a name="imagebuilder-CreateContainerRecipe-request-instanceConfiguration"></a>
A group of options that can be used to configure an instance for building and testing container images.
Type: [InstanceConfiguration](API_InstanceConfiguration.md) object
Required: No

 ** [kmsKeyId](#API_CreateContainerRecipe_RequestSyntax) **   <a name="imagebuilder-CreateContainerRecipe-request-kmsKeyId"></a>
The Amazon Resource Name (ARN) that uniquely identifies which KMS key is used to encrypt the Dockerfile template. This can be either the Key ARN or the Alias ARN. For more information, see [Key identifiers (KeyId)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN) in the * AWS Key Management Service Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [name](#API_CreateContainerRecipe_RequestSyntax) **   <a name="imagebuilder-CreateContainerRecipe-request-name"></a>
The name of the container recipe. The recipe name, combined with the semantic version, must be unique to your account in each AWS Region. Image Builder generates the container recipe ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: Yes

 ** [parentImage](#API_CreateContainerRecipe_RequestSyntax) **   <a name="imagebuilder-CreateContainerRecipe-request-parentImage"></a>
The base image for the container recipe. This can be an Image Builder image resource ARN or a container image URI from a registry, for example `amazonlinux:latest`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [platformOverride](#API_CreateContainerRecipe_RequestSyntax) **   <a name="imagebuilder-CreateContainerRecipe-request-platformOverride"></a>
Specifies the operating system platform when you use a custom base image. Container recipes support only the Linux and Windows platforms.
Type: String
Valid Values: `Windows | Linux | macOS`
Required: No

 ** [semanticVersion](#API_CreateContainerRecipe_RequestSyntax) **   <a name="imagebuilder-CreateContainerRecipe-request-semanticVersion"></a>
The semantic version of the container recipe. This version follows the semantic version syntax.
The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.
 **Assignment:** For the first three nodes, you can assign any positive integer value, including zero. The upper limit is 2^30-1, or 1073741823, for each node. Image Builder automatically assigns the build number to the fourth node.
 **Patterns:** You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.
Type: String
Pattern: `^(?:[0-9]+|x)\.(?:[0-9]+|x)\.(?:[0-9]+|x)$`
Required: Yes

 ** [tags](#API_CreateContainerRecipe_RequestSyntax) **   <a name="imagebuilder-CreateContainerRecipe-request-tags"></a>
Tags that are attached to the container recipe.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [targetRepository](#API_CreateContainerRecipe_RequestSyntax) **   <a name="imagebuilder-CreateContainerRecipe-request-targetRepository"></a>
The destination repository for the container image. The Amazon ECR repository must already exist in the AWS Region where the build runs.
Type: [TargetContainerRepository](API_TargetContainerRepository.md) object
Required: Yes

 ** [workingDirectory](#API_CreateContainerRecipe_RequestSyntax) **   <a name="imagebuilder-CreateContainerRecipe-request-workingDirectory"></a>
The working directory for use during build and test workflows.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_CreateContainerRecipe_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clientToken": "string",
   "containerRecipeArn": "string",
   "latestVersionReferences": {
      "latestMajorVersionArn": "string",
      "latestMinorVersionArn": "string",
      "latestPatchVersionArn": "string",
      "latestVersionArn": "string"
   },
   "requestId": "string"
}
```

## Response Elements
<a name="API_CreateContainerRecipe_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_CreateContainerRecipe_ResponseSyntax) **   <a name="imagebuilder-CreateContainerRecipe-response-clientToken"></a>
The client token that uniquely identifies the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [containerRecipeArn](#API_CreateContainerRecipe_ResponseSyntax) **   <a name="imagebuilder-CreateContainerRecipe-response-containerRecipeArn"></a>
Returns the Amazon Resource Name (ARN) of the container recipe that the request created.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):container-recipe/[a-z0-9-_]+/(?:[0-9]+|x)\.(?:[0-9]+|x)\.(?:[0-9]+|x)$`

 ** [latestVersionReferences](#API_CreateContainerRecipe_ResponseSyntax) **   <a name="imagebuilder-CreateContainerRecipe-response-latestVersionReferences"></a>
A set of wildcard version ARNs that always reference the latest version of the resource. ARNs are included for the latest version overall, and for the latest versions within the same major, minor, and patch levels.
Type: [LatestVersionReferences](API_LatestVersionReferences.md) object

 ** [requestId](#API_CreateContainerRecipe_ResponseSyntax) **   <a name="imagebuilder-CreateContainerRecipe-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_CreateContainerRecipe_Errors"></a>

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

 ** InvalidVersionNumberException **
Your version number is out of bounds or does not follow the required syntax.
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
<a name="API_CreateContainerRecipe_Examples"></a>

### Create a container recipe with an inline Dockerfile template
<a name="API_CreateContainerRecipe_Example_1"></a>

The following example creates a Docker container recipe that applies one build component, using the latest Amazon Linux container image as the parent and an existing ECR repository as the target.

#### Sample Request
<a name="API_CreateContainerRecipe_Example_1_Request"></a>

```
PUT /CreateContainerRecipe HTTP/1.1
Content-type: application/json

{
    "containerType": "DOCKER",
    "name": "my-example-container-recipe",
    "semanticVersion": "1.0.0",
    "parentImage": "amazonlinux:latest",
    "components": [
        {
            "componentArn": "arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-container-component/1.0.0/1"
        }
    ],
    "dockerfileTemplateData": "FROM {{{ imagebuilder:parentImage }}}\n{{{ imagebuilder:environments }}}\n{{{ imagebuilder:components }}}\n",
    "targetRepository": {
        "service": "ECR",
        "repositoryName": "my-example-container-repo"
    },
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE99999"
}
```

#### Sample Response
<a name="API_CreateContainerRecipe_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "20b16948-45a4-4b3a-9a17-d54779847365",
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE99999",
    "containerRecipeArn": "arn:aws:imagebuilder:us-west-2:111122223333:container-recipe/my-example-container-recipe/1.0.0",
    "latestVersionReferences": {
        "latestVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:container-recipe/my-example-container-recipe/x.x.x",
        "latestMajorVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:container-recipe/my-example-container-recipe/1.x.x",
        "latestMinorVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:container-recipe/my-example-container-recipe/1.0.x",
        "latestPatchVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:container-recipe/my-example-container-recipe/1.0.0"
    }
}
```

### Create a container recipe with a custom build instance configuration
<a name="API_CreateContainerRecipe_Example_2"></a>

The following example creates a container recipe that customizes the Amazon EC2 instance that builds the container image. The build instance launches from an Amazon ECS-optimized instance image and uses a 40 GiB gp3 volume.

#### Sample Request
<a name="API_CreateContainerRecipe_Example_2_Request"></a>

```
PUT /CreateContainerRecipe HTTP/1.1
Content-type: application/json

{
    "containerType": "DOCKER",
    "name": "my-example-container-recipe",
    "semanticVersion": "1.1.0",
    "description": "A container recipe that builds on an ECS-optimized instance image with a larger build volume",
    "parentImage": "amazonlinux:latest",
    "components": [
        {
            "componentArn": "arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-container-component/1.0.0/1"
        }
    ],
    "instanceConfiguration": {
        "image": "ami-1234567890abcdef0",
        "blockDeviceMappings": [
            {
                "deviceName": "/dev/xvda",
                "ebs": {
                    "volumeSize": 40,
                    "volumeType": "gp3",
                    "deleteOnTermination": true
                }
            }
        ]
    },
    "dockerfileTemplateData": "FROM {{{ imagebuilder:parentImage }}}\n{{{ imagebuilder:environments }}}\n{{{ imagebuilder:components }}}\n",
    "targetRepository": {
        "service": "ECR",
        "repositoryName": "my-example-container-repo"
    },
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE40404"
}
```

#### Sample Response
<a name="API_CreateContainerRecipe_Example_2_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "4b6fc7f3-5b6b-4086-858e-22d4c7f9a37f",
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE40404",
    "containerRecipeArn": "arn:aws:imagebuilder:us-west-2:111122223333:container-recipe/my-example-container-recipe/1.1.0",
    "latestVersionReferences": {
        "latestVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:container-recipe/my-example-container-recipe/x.x.x",
        "latestMajorVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:container-recipe/my-example-container-recipe/1.x.x",
        "latestMinorVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:container-recipe/my-example-container-recipe/1.1.x",
        "latestPatchVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:container-recipe/my-example-container-recipe/1.1.0"
    }
}
```

## See Also
<a name="API_CreateContainerRecipe_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/CreateContainerRecipe)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/CreateContainerRecipe)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/CreateContainerRecipe)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/CreateContainerRecipe)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/CreateContainerRecipe)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/CreateContainerRecipe)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/CreateContainerRecipe)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/CreateContainerRecipe)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/CreateContainerRecipe)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/CreateContainerRecipe)
