---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetImage.html
---

# GetImage
<a name="API_GetImage"></a>

Gets an image.

## Request Syntax
<a name="API_GetImage_RequestSyntax"></a>

```
GET /GetImage?imageBuildVersionArn={{imageBuildVersionArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetImage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [imageBuildVersionArn](#API_GetImage_RequestSyntax) **   <a name="imagebuilder-GetImage-request-uri-imageBuildVersionArn"></a>
The Amazon Resource Name (ARN) of the image that you want to get.
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):image/[a-z0-9-_]+/(?:(?:([0-9]+|x)\.([0-9]+|x)\.([0-9]+|x))|(?:[0-9]+\.[0-9]+\.[0-9]+/[0-9]+))$`
Required: Yes

## Request Body
<a name="API_GetImage_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetImage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "image": {
      "arn": "string",
      "buildType": "string",
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
      "dateCreated": "string",
      "deprecationTime": number,
      "distributionConfiguration": {
         "arn": "string",
         "dateCreated": "string",
         "dateUpdated": "string",
         "description": "string",
         "distributions": [
            {
               "amiDistributionConfiguration": {
                  "amiTags": {
                     "string" : "string"
                  },
                  "description": "string",
                  "kmsKeyId": "string",
                  "launchPermission": {
                     "organizationalUnitArns": [ "string" ],
                     "organizationArns": [ "string" ],
                     "userGroups": [ "string" ],
                     "userIds": [ "string" ]
                  },
                  "name": "string",
                  "targetAccountIds": [ "string" ]
               },
               "containerDistributionConfiguration": {
                  "containerTags": [ "string" ],
                  "description": "string",
                  "targetRepository": {
                     "repositoryName": "string",
                     "service": "string"
                  }
               },
               "fastLaunchConfigurations": [
                  {
                     "accountId": "string",
                     "enabled": boolean,
                     "launchTemplate": {
                        "launchTemplateId": "string",
                        "launchTemplateName": "string",
                        "launchTemplateVersion": "string"
                     },
                     "maxParallelLaunches": number,
                     "snapshotConfiguration": {
                        "targetResourceCount": number
                     }
                  }
               ],
               "launchTemplateConfigurations": [
                  {
                     "accountId": "string",
                     "launchTemplateId": "string",
                     "setDefaultVersion": boolean
                  }
               ],
               "licenseConfigurationArns": [ "string" ],
               "region": "string",
               "s3ExportConfiguration": {
                  "diskImageFormat": "string",
                  "roleName": "string",
                  "s3Bucket": "string",
                  "s3Prefix": "string"
               },
               "ssmParameterConfigurations": [
                  {
                     "amiAccountId": "string",
                     "dataType": "string",
                     "parameterName": "string"
                  }
               ]
            }
         ],
         "name": "string",
         "tags": {
            "string" : "string"
         },
         "timeoutMinutes": number
      },
      "enhancedImageMetadataEnabled": boolean,
      "executionRole": "string",
      "imageRecipe": {
         "additionalInstanceConfiguration": {
            "systemsManagerAgent": {
               "uninstallAfterBuild": boolean
            },
            "userDataOverride": "string"
         },
         "amiTags": {
            "string" : "string"
         },
         "amiWatermarks": [ "string" ],
         "arn": "string",
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
         "dateCreated": "string",
         "description": "string",
         "name": "string",
         "owner": "string",
         "parentImage": "string",
         "platform": "string",
         "tags": {
            "string" : "string"
         },
         "type": "string",
         "version": "string",
         "workingDirectory": "string"
      },
      "imageScanningConfiguration": {
         "ecrConfiguration": {
            "containerTags": [ "string" ],
            "repositoryName": "string"
         },
         "imageScanningEnabled": boolean
      },
      "imageSource": "string",
      "imageTestsConfiguration": {
         "imageTestsEnabled": boolean,
         "timeoutMinutes": number
      },
      "infrastructureConfiguration": {
         "arn": "string",
         "dateCreated": "string",
         "dateUpdated": "string",
         "description": "string",
         "instanceMetadataOptions": {
            "httpPutResponseHopLimit": number,
            "httpTokens": "string"
         },
         "instanceProfileName": "string",
         "instanceTypes": [ "string" ],
         "keyPair": "string",
         "logging": {
            "s3Logs": {
               "s3BucketName": "string",
               "s3KeyPrefix": "string"
            }
         },
         "name": "string",
         "placement": {
            "availabilityZone": "string",
            "hostId": "string",
            "hostResourceGroupArn": "string",
            "tenancy": "string"
         },
         "resourceTags": {
            "string" : "string"
         },
         "securityGroupIds": [ "string" ],
         "snsTopicArn": "string",
         "subnetId": "string",
         "tags": {
            "string" : "string"
         },
         "terminateInstanceOnFailure": boolean
      },
      "lifecycleExecutionId": "string",
      "loggingConfiguration": {
         "logGroupName": "string"
      },
      "name": "string",
      "osVersion": "string",
      "outputResources": {
         "amis": [
            {
               "accountId": "string",
               "description": "string",
               "image": "string",
               "name": "string",
               "region": "string",
               "state": {
                  "reason": "string",
                  "status": "string"
               }
            }
         ],
         "containers": [
            {
               "imageUris": [ "string" ],
               "region": "string"
            }
         ]
      },
      "platform": "string",
      "scanState": {
         "reason": "string",
         "status": "string"
      },
      "sourcePipelineArn": "string",
      "sourcePipelineName": "string",
      "state": {
         "reason": "string",
         "status": "string"
      },
      "tags": {
         "string" : "string"
      },
      "type": "string",
      "version": "string",
      "workflows": [
         {
            "onFailure": "string",
            "parallelGroup": "string",
            "parameters": [
               {
                  "name": "string",
                  "value": [ "string" ]
               }
            ],
            "workflowArn": "string"
         }
      ]
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
<a name="API_GetImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [image](#API_GetImage_ResponseSyntax) **   <a name="imagebuilder-GetImage-response-image"></a>
The image object.
Type: [Image](API_Image.md) object

 ** [latestVersionReferences](#API_GetImage_ResponseSyntax) **   <a name="imagebuilder-GetImage-response-latestVersionReferences"></a>
The resource ARNs with different wildcard variations of semantic versioning.
Type: [LatestVersionReferences](API_LatestVersionReferences.md) object

 ** [requestId](#API_GetImage_ResponseSyntax) **   <a name="imagebuilder-GetImage-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_GetImage_Errors"></a>

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

 ** InvalidRequestException **
You have requested an action that that the service doesn't support.
HTTP Status Code: 400

 ** ServiceException **
This exception is thrown when the service encounters an unrecoverable exception.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## See Also
<a name="API_GetImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/GetImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/GetImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/GetImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/GetImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/GetImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/GetImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/GetImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/GetImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/GetImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/GetImage)
