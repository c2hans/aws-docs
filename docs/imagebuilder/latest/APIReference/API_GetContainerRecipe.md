---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetContainerRecipe.html
---

# GetContainerRecipe
<a name="API_GetContainerRecipe"></a>

Retrieves a container recipe.

## Request Syntax
<a name="API_GetContainerRecipe_RequestSyntax"></a>

```
GET /GetContainerRecipe?containerRecipeArn={{containerRecipeArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetContainerRecipe_RequestParameters"></a>

The request uses the following URI parameters.

 ** [containerRecipeArn](#API_GetContainerRecipe_RequestSyntax) **   <a name="imagebuilder-GetContainerRecipe-request-uri-containerRecipeArn"></a>
The Amazon Resource Name (ARN) of the container recipe to retrieve.
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):container-recipe/[a-z0-9-_]+/(?:[0-9]+|x)\.(?:[0-9]+|x)\.(?:[0-9]+|x)$`
Required: Yes

## Request Body
<a name="API_GetContainerRecipe_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetContainerRecipe_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "containerRecipe": {
      "arn": "string",
      "components": [
         {
            "componentArn": "string",
            "parameters": [
               {
                  "name": "string",
                  "value": [ "string" ]
               }
            ]
         }
      ],
      "containerType": "string",
      "dateCreated": "string",
      "description": "string",
      "dockerfileTemplateData": "string",
      "encrypted": boolean,
      "instanceConfiguration": {
         "blockDeviceMappings": [
            {
               "deviceName": "string",
               "ebs": {
                  "deleteOnTermination": boolean,
                  "encrypted": boolean,
                  "iops": number,
                  "kmsKeyId": "string",
                  "snapshotId": "string",
                  "throughput": number,
                  "volumeSize": number,
                  "volumeType": "string"
               },
               "noDevice": "string",
               "virtualName": "string"
            }
         ],
         "image": "string"
      },
      "kmsKeyId": "string",
      "name": "string",
      "owner": "string",
      "parentImage": "string",
      "platform": "string",
      "tags": {
         "string" : "string"
      },
      "targetRepository": {
         "repositoryName": "string",
         "service": "string"
      },
      "version": "string",
      "workingDirectory": "string"
   },
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
<a name="API_GetContainerRecipe_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [containerRecipe](#API_GetContainerRecipe_ResponseSyntax) **   <a name="imagebuilder-GetContainerRecipe-response-containerRecipe"></a>
The container recipe object that is returned.
Type: [ContainerRecipe](API_ContainerRecipe.md) object

 ** [latestVersionReferences](#API_GetContainerRecipe_ResponseSyntax) **   <a name="imagebuilder-GetContainerRecipe-response-latestVersionReferences"></a>
A set of wildcard version ARNs that always reference the latest version of the resource. ARNs are included for the latest version overall, and for the latest versions within the same major, minor, and patch levels.
Type: [LatestVersionReferences](API_LatestVersionReferences.md) object

 ** [requestId](#API_GetContainerRecipe_ResponseSyntax) **   <a name="imagebuilder-GetContainerRecipe-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_GetContainerRecipe_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.
HTTP Status Code: 429

 ** ClientException **
A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InvalidRequestException **
The request is malformed or otherwise invalid. Verify the request and try again.
HTTP Status Code: 400

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_GetContainerRecipe_Examples"></a>

### Get the details of a container recipe
<a name="API_GetContainerRecipe_Example_1"></a>

The following example retrieves the details of the specified container recipe.

#### Sample Request
<a name="API_GetContainerRecipe_Example_1_Request"></a>

```
GET /GetContainerRecipe?containerRecipeArn=arn%3Aaws%3Aimagebuilder%3Aus-west-2%3A111122223333%3Acontainer-recipe%2Fmy-example-container-recipe%2F1.0.0 HTTP/1.1
```

#### Sample Response
<a name="API_GetContainerRecipe_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "15b03ca7-050f-46d4-945e-00232cff6b19",
    "containerRecipe": {
        "arn": "arn:aws:imagebuilder:us-west-2:111122223333:container-recipe/my-example-container-recipe/1.0.0",
        "containerType": "DOCKER",
        "name": "my-example-container-recipe",
        "description": "A container recipe that installs my application on Amazon Linux",
        "platform": "Linux",
        "owner": "111122223333",
        "version": "1.0.0",
        "components": [
            {
                "componentArn": "arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-container-component/1.0.0/1"
            }
        ],
        "dockerfileTemplateData": "FROM {{{ imagebuilder:parentImage }}}\n{{{ imagebuilder:environments }}}\n{{{ imagebuilder:components }}}\n",
        "encrypted": true,
        "parentImage": "amazonlinux:latest",
        "dateCreated": "2026-09-09T19:32:53.983Z",
        "tags": {},
        "targetRepository": {
            "service": "ECR",
            "repositoryName": "my-example-container-repo"
        }
    },
    "latestVersionReferences": {
        "latestVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:container-recipe/my-example-container-recipe/x.x.x",
        "latestMajorVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:container-recipe/my-example-container-recipe/1.x.x",
        "latestMinorVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:container-recipe/my-example-container-recipe/1.0.x",
        "latestPatchVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:container-recipe/my-example-container-recipe/1.0.0"
    }
}
```

## See Also
<a name="API_GetContainerRecipe_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/GetContainerRecipe)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/GetContainerRecipe)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/GetContainerRecipe)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/GetContainerRecipe)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/GetContainerRecipe)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/GetContainerRecipe)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/GetContainerRecipe)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/GetContainerRecipe)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/GetContainerRecipe)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/GetContainerRecipe)
