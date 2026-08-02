---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_DescribeLaunchConfigurationTemplates.html
---

# DescribeLaunchConfigurationTemplates
<a name="API_DescribeLaunchConfigurationTemplates"></a>

Lists all Launch Configuration Templates, filtered by Launch Configuration Template IDs

## Request Syntax
<a name="API_DescribeLaunchConfigurationTemplates_RequestSyntax"></a>

```
POST /DescribeLaunchConfigurationTemplates HTTP/1.1
Content-type: application/json

{
   "launchConfigurationTemplateIDs": [ "{{string}}" ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeLaunchConfigurationTemplates_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeLaunchConfigurationTemplates_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [launchConfigurationTemplateIDs](#API_DescribeLaunchConfigurationTemplates_RequestSyntax) **   <a name="mgn-DescribeLaunchConfigurationTemplates-request-launchConfigurationTemplateIDs"></a>
Request to filter Launch Configuration Templates list by Launch Configuration Template ID.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Length Constraints: Fixed length of 21.
Pattern: `lct-[0-9a-zA-Z]{17}`
Required: No

 ** [maxResults](#API_DescribeLaunchConfigurationTemplates_RequestSyntax) **   <a name="mgn-DescribeLaunchConfigurationTemplates-request-maxResults"></a>
Maximum results to be returned in DescribeLaunchConfigurationTemplates.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_DescribeLaunchConfigurationTemplates_RequestSyntax) **   <a name="mgn-DescribeLaunchConfigurationTemplates-request-nextToken"></a>
Next pagination token returned from DescribeLaunchConfigurationTemplates.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_DescribeLaunchConfigurationTemplates_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "arn": "string",
         "associatePublicIpAddress": boolean,
         "bootMode": "string",
         "copyPrivateIp": boolean,
         "copyTags": boolean,
         "ec2LaunchTemplateID": "string",
         "enableMapAutoTagging": boolean,
         "enableParametersEncryption": boolean,
         "largeVolumeConf": {
            "iops": number,
            "throughput": number,
            "volumeType": "string"
         },
         "launchConfigurationTemplateID": "string",
         "launchDisposition": "string",
         "licensing": {
            "osByol": boolean
         },
         "mapAutoTaggingMpeID": "string",
         "parametersEncryptionKey": "string",
         "postLaunchActions": {
            "cloudWatchLogGroupName": "string",
            "deployment": "string",
            "s3LogBucket": "string",
            "s3OutputKeyPrefix": "string",
            "ssmDocuments": [
               {
                  "actionName": "string",
                  "externalParameters": {
                     "string" : { ... }
                  },
                  "mustSucceedForCutover": boolean,
                  "parameters": {
                     "string" : [
                        {
                           "parameterName": "string",
                           "parameterType": "string"
                        }
                     ]
                  },
                  "ssmDocumentName": "string",
                  "timeoutSeconds": number
               }
            ]
         },
         "smallVolumeConf": {
            "iops": number,
            "throughput": number,
            "volumeType": "string"
         },
         "smallVolumeMaxSize": number,
         "tags": {
            "string" : "string"
         },
         "targetInstanceTypeRightSizingMethod": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeLaunchConfigurationTemplates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_DescribeLaunchConfigurationTemplates_ResponseSyntax) **   <a name="mgn-DescribeLaunchConfigurationTemplates-response-items"></a>
List of items returned by DescribeLaunchConfigurationTemplates.
Type: Array of [LaunchConfigurationTemplate](API_LaunchConfigurationTemplate.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

 ** [nextToken](#API_DescribeLaunchConfigurationTemplates_ResponseSyntax) **   <a name="mgn-DescribeLaunchConfigurationTemplates-response-nextToken"></a>
Next pagination token returned from DescribeLaunchConfigurationTemplates.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_DescribeLaunchConfigurationTemplates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
Resource not found exception.
 ** resourceId **
Resource ID not found error.
 ** resourceType **
Resource type not found error.
HTTP Status Code: 404

 ** UninitializedAccountException **
Uninitialized account exception.
HTTP Status Code: 400

 ** ValidationException **
Validate exception.
 ** fieldList **
Validate exception field list.
 ** reason **
Validate exception reason.
HTTP Status Code: 400

## See Also
<a name="API_DescribeLaunchConfigurationTemplates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/DescribeLaunchConfigurationTemplates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/DescribeLaunchConfigurationTemplates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/DescribeLaunchConfigurationTemplates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/DescribeLaunchConfigurationTemplates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/DescribeLaunchConfigurationTemplates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/DescribeLaunchConfigurationTemplates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/DescribeLaunchConfigurationTemplates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/DescribeLaunchConfigurationTemplates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/DescribeLaunchConfigurationTemplates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/DescribeLaunchConfigurationTemplates)
