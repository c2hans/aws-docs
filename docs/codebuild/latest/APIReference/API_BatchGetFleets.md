---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetFleets.html
---

# BatchGetFleets
<a name="API_BatchGetFleets"></a>

Gets information about one or more compute fleets.

## Request Syntax
<a name="API_BatchGetFleets_RequestSyntax"></a>

```
{
   "names": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchGetFleets_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [names](#API_BatchGetFleets_RequestSyntax) **   <a name="CodeBuild-BatchGetFleets-request-names"></a>
The names or ARNs of the compute fleets.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1.
Required: Yes

## Response Syntax
<a name="API_BatchGetFleets_ResponseSyntax"></a>

```
{
   "fleets": [
      {
         "arn": "string",
         "baseCapacity": number,
         "computeConfiguration": {
            "disk": number,
            "instanceType": "string",
            "machineType": "string",
            "memory": number,
            "vCpu": number
         },
         "computeType": "string",
         "created": number,
         "environmentType": "string",
         "fleetServiceRole": "string",
         "id": "string",
         "imageId": "string",
         "lastModified": number,
         "name": "string",
         "overflowBehavior": "string",
         "proxyConfiguration": {
            "defaultBehavior": "string",
            "orderedProxyRules": [
               {
                  "effect": "string",
                  "entities": [ "string" ],
                  "type": "string"
               }
            ]
         },
         "scalingConfiguration": {
            "desiredCapacity": number,
            "maxCapacity": number,
            "scalingType": "string",
            "targetTrackingScalingConfigs": [
               {
                  "metricType": "string",
                  "targetValue": number
               }
            ]
         },
         "status": {
            "context": "string",
            "message": "string",
            "statusCode": "string"
         },
         "tags": [
            {
               "key": "string",
               "value": "string"
            }
         ],
         "vpcConfig": {
            "securityGroupIds": [ "string" ],
            "subnets": [ "string" ],
            "vpcId": "string"
         }
      }
   ],
   "fleetsNotFound": [ "string" ]
}
```

## Response Elements
<a name="API_BatchGetFleets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [fleets](#API_BatchGetFleets_ResponseSyntax) **   <a name="CodeBuild-BatchGetFleets-response-fleets"></a>
Information about the requested compute fleets.
Type: Array of [Fleet](API_Fleet.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.

 ** [fleetsNotFound](#API_BatchGetFleets_ResponseSyntax) **   <a name="CodeBuild-BatchGetFleets-response-fleetsNotFound"></a>
The names of compute fleets for which information could not be found.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1.

## Errors
<a name="API_BatchGetFleets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

## See Also
<a name="API_BatchGetFleets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/BatchGetFleets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/BatchGetFleets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/BatchGetFleets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/BatchGetFleets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/BatchGetFleets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/BatchGetFleets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/BatchGetFleets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/BatchGetFleets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/BatchGetFleets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/BatchGetFleets)
