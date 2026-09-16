---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_BatchCheckLayerAvailability.html
---

# BatchCheckLayerAvailability
<a name="API_BatchCheckLayerAvailability"></a>

Checks the availability of one or more image layers that are within a repository in a public registry. When an image is pushed to a repository, each image layer is checked to verify if it has been uploaded before. If it has been uploaded, then the image layer is skipped.

**Note**
This operation is used by the Amazon ECR proxy and is not generally used by customers for pulling and pushing images. In most cases, you should use the `docker` CLI to pull, tag, and push images.

## Request Syntax
<a name="API_BatchCheckLayerAvailability_RequestSyntax"></a>

```
{
   "layerDigests": [ "{{string}}" ],
   "registryId": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_BatchCheckLayerAvailability_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [layerDigests](#API_BatchCheckLayerAvailability_RequestSyntax) **   <a name="ecrpublic-BatchCheckLayerAvailability-request-layerDigests"></a>
The digests of the image layers to check.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

 ** [registryId](#API_BatchCheckLayerAvailability_RequestSyntax) **   <a name="ecrpublic-BatchCheckLayerAvailability-request-registryId"></a>
The AWS account ID, or registry alias, associated with the public registry that contains the image layers to check. If you do not specify a registry, the default public registry is assumed.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 50.
Required: No

 ** [repositoryName](#API_BatchCheckLayerAvailability_RequestSyntax) **   <a name="ecrpublic-BatchCheckLayerAvailability-request-repositoryName"></a>
The name of the repository that's associated with the image layers to check.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 205.
Pattern: `(?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*`
Required: Yes

## Response Syntax
<a name="API_BatchCheckLayerAvailability_ResponseSyntax"></a>

```
{
   "failures": [
      {
         "failureCode": "string",
         "failureReason": "string",
         "layerDigest": "string"
      }
   ],
   "layers": [
      {
         "layerAvailability": "string",
         "layerDigest": "string",
         "layerSize": number,
         "mediaType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchCheckLayerAvailability_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failures](#API_BatchCheckLayerAvailability_ResponseSyntax) **   <a name="ecrpublic-BatchCheckLayerAvailability-response-failures"></a>
Any failures associated with the call.
Type: Array of [LayerFailure](API_LayerFailure.md) objects

 ** [layers](#API_BatchCheckLayerAvailability_ResponseSyntax) **   <a name="ecrpublic-BatchCheckLayerAvailability-response-layers"></a>
A list of image layer objects that correspond to the image layer references in the request.
Type: Array of [Layer](API_Layer.md) objects

## Errors
<a name="API_BatchCheckLayerAvailability_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
HTTP Status Code: 400

 ** RegistryNotFoundException **
The registry doesn't exist.
HTTP Status Code: 400

 ** RepositoryNotFoundException **
The specified repository can't be found. Check the spelling of the specified repository and ensure that you're performing operations on the correct registry.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server-side issue.
HTTP Status Code: 500

 ** UnsupportedCommandException **
The action isn't supported in this Region.
HTTP Status Code: 400

## See Also
<a name="API_BatchCheckLayerAvailability_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-public-2020-10-30/BatchCheckLayerAvailability)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-public-2020-10-30/BatchCheckLayerAvailability)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/BatchCheckLayerAvailability)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-public-2020-10-30/BatchCheckLayerAvailability)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/BatchCheckLayerAvailability)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-public-2020-10-30/BatchCheckLayerAvailability)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-public-2020-10-30/BatchCheckLayerAvailability)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-public-2020-10-30/BatchCheckLayerAvailability)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecr-public-2020-10-30/BatchCheckLayerAvailability)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/BatchCheckLayerAvailability)
