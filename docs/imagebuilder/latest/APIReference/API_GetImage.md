---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetImage.html
---

# GetImage
<a name="API_GetImage"></a>

Retrieves an image.

## Request Syntax
<a name="API_GetImage_RequestSyntax"></a>

```
GET /GetImage?imageBuildVersionArn={{imageBuildVersionArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetImage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [imageBuildVersionArn](#API_GetImage_RequestSyntax) **   <a name="imagebuilder-GetImage-request-uri-imageBuildVersionArn"></a>
The Amazon Resource Name (ARN) of the image that you want to get. You can specify a full build version ARN, or a version ARN with or without wildcards (`x.x.x`, `1.x.x`, or `1.0.x`). A version or wildcard ARN resolves to the latest matching build version that has reached `AVAILABLE` status. Builds that were later deprecated, disabled, or deleted don't resolve. To get an image in any other state, such as a failed or in-progress build, specify the full build version ARN.
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
                  "failureContext": {
                     "componentFailure": {
                        "action": "string",
                        "componentArn": "string",
                        "errorMessage": "string",
                        "phaseName": "string",
                        "stepName": "string"
                     },
                     "distributionFailure": {
                        "errorMessage": "string",
                        "regionFailures": [
                           {
                              "errorMessage": "string",
                              "imageConfigurationStep": "string",
                              "region": "string",
                              "status": "string",
                              "targetAccountId": "string"
                           }
                        ]
                     },
                     "failedStep": "string",
                     "imageStatus": "string",
                     "stepExecutionId": "string",
                     "workflowArn": "string",
                     "workflowExecutionId": "string"
                  },
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
         "failureContext": {
            "componentFailure": {
               "action": "string",
               "componentArn": "string",
               "errorMessage": "string",
               "phaseName": "string",
               "stepName": "string"
            },
            "distributionFailure": {
               "errorMessage": "string",
               "regionFailures": [
                  {
                     "errorMessage": "string",
                     "imageConfigurationStep": "string",
                     "region": "string",
                     "status": "string",
                     "targetAccountId": "string"
                  }
               ]
            },
            "failedStep": "string",
            "imageStatus": "string",
            "stepExecutionId": "string",
            "workflowArn": "string",
            "workflowExecutionId": "string"
         },
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
A set of wildcard version ARNs that always reference the latest version of the resource. ARNs are included for the latest version overall, and for the latest versions within the same major, minor, and patch levels.
Type: [LatestVersionReferences](API_LatestVersionReferences.md) object

 ** [requestId](#API_GetImage_ResponseSyntax) **   <a name="imagebuilder-GetImage-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_GetImage_Errors"></a>

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
<a name="API_GetImage_Examples"></a>

### Check the status of an image build
<a name="API_GetImage_Example_1"></a>

The following example retrieves an image build version to check its status while the build is running. The response is shortened to show a subset of the fields that Image Builder returns.

#### Sample Request
<a name="API_GetImage_Example_1_Request"></a>

```
GET /GetImage?imageBuildVersionArn=arn%3Aaws%3Aimagebuilder%3Aus-west-2%3A111122223333%3Aimage%2Fmy-example-recipe%2F1.0.0%2F1 HTTP/1.1
```

#### Sample Response
<a name="API_GetImage_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "4be892f0-e1d1-47f9-8bc1-d08ec5dec640",
    "image": {
        "arn": "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0/1",
        "type": "AMI",
        "name": "my-example-recipe",
        "version": "1.0.0/1",
        "platform": "Linux",
        "enhancedImageMetadataEnabled": true,
        "state": {
            "status": "BUILDING"
        },
        "sourcePipelineArn": "arn:aws:imagebuilder:us-west-2:111122223333:image-pipeline/my-example-pipeline",
        "dateCreated": "2026-09-03T05:44:21.121Z",
        "tags": {}
    }
}
```

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
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/GetImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/GetImage)
