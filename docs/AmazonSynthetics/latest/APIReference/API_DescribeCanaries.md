---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html
---

# DescribeCanaries
<a name="API_DescribeCanaries"></a>

This operation returns a list of the canaries in your account, along with full details about each canary.

This operation supports resource-level authorization using an IAM policy and the `Names` parameter. If you specify the `Names` parameter, the operation is successful only if you have authorization to view all the canaries that you specify in your request. If you do not have permission to view any of the canaries, the request fails with a 403 response.

You are required to use the `Names` parameter if you are logged on to a user or role that has an IAM policy that restricts which canaries that you are allowed to view. For more information, see [ Limiting a user to viewing specific canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Restricted.html).

## Request Syntax
<a name="API_DescribeCanaries_RequestSyntax"></a>

```
POST /canaries HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "Names": [ "{{string}}" ],
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeCanaries_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeCanaries_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_DescribeCanaries_RequestSyntax) **   <a name="synthetics-DescribeCanaries-request-MaxResults"></a>
Specify this parameter to limit how many canaries are returned each time you use the `DescribeCanaries` operation. If you omit this parameter, the default of 20 is used.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: No

 ** [Names](#API_DescribeCanaries_RequestSyntax) **   <a name="synthetics-DescribeCanaries-request-Names"></a>
Use this parameter to return only canaries that match the names that you specify here. You can specify as many as five canary names.
If you specify this parameter, the operation is successful only if you have authorization to view all the canaries that you specify in your request. If you do not have permission to view any of the canaries, the request fails with a 403 response.
You are required to use this parameter if you are logged on to a user or role that has an IAM policy that restricts which canaries that you are allowed to view. For more information, see [ Limiting a user to viewing specific canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Restricted.html).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[0-9a-z_\-]+$`
Required: No

 ** [NextToken](#API_DescribeCanaries_RequestSyntax) **   <a name="synthetics-DescribeCanaries-request-NextToken"></a>
A token that indicates that there is more data available. You can use this token in a subsequent operation to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 252.
Required: No

## Response Syntax
<a name="API_DescribeCanaries_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Canaries": [
      {
         "ArtifactConfig": {
            "S3Encryption": {
               "EncryptionMode": "string",
               "KmsKeyArn": "string"
            }
         },
         "ArtifactS3Location": "string",
         "BrowserConfigs": [
            {
               "BrowserType": "string"
            }
         ],
         "Code": {
            "BlueprintTypes": [ "string" ],
            "Dependencies": [
               {
                  "Reference": "string",
                  "Type": "string"
               }
            ],
            "Handler": "string",
            "SourceLocationArn": "string"
         },
         "DryRunConfig": {
            "DryRunId": "string",
            "LastDryRunExecutionStatus": "string"
         },
         "EngineArn": "string",
         "EngineConfigs": [
            {
               "BrowserType": "string",
               "EngineArn": "string"
            }
         ],
         "ExecutionRoleArn": "string",
         "FailureRetentionPeriodInDays": number,
         "Id": "string",
         "MultiLocationConfig": {
            "LocationType": "string",
            "PrimaryLocation": "string",
            "Replicas": [
               {
                  "CanaryState": "string",
                  "LastModified": number,
                  "Location": "string",
                  "ReplicationStatus": {
                     "State": "string",
                     "StateReason": "string",
                     "StateReasonCode": "string"
                  },
                  "VpcConfig": {
                     "Ipv6AllowedForDualStack": boolean,
                     "SecurityGroupIds": [ "string" ],
                     "SubnetIds": [ "string" ],
                     "VpcId": "string"
                  }
               }
            ],
            "ReplicationState": "string"
         },
         "Name": "string",
         "ProvisionedResourceCleanup": "string",
         "RunConfig": {
            "ActiveTracing": boolean,
            "EphemeralStorage": number,
            "MemoryInMB": number,
            "TimeoutInSeconds": number
         },
         "RuntimeVersion": "string",
         "Schedule": {
            "DurationInSeconds": number,
            "Expression": "string",
            "RetryConfig": {
               "MaxRetries": number
            }
         },
         "Status": {
            "State": "string",
            "StateReason": "string",
            "StateReasonCode": "string"
         },
         "SuccessRetentionPeriodInDays": number,
         "Tags": {
            "string" : "string"
         },
         "Timeline": {
            "Created": number,
            "LastModified": number,
            "LastStarted": number,
            "LastStopped": number
         },
         "VisualReference": {
            "BaseCanaryRunId": "string",
            "BaseScreenshots": [
               {
                  "IgnoreCoordinates": [ "string" ],
                  "ScreenshotName": "string"
               }
            ],
            "BrowserType": "string"
         },
         "VisualReferences": [
            {
               "BaseCanaryRunId": "string",
               "BaseScreenshots": [
                  {
                     "IgnoreCoordinates": [ "string" ],
                     "ScreenshotName": "string"
                  }
               ],
               "BrowserType": "string"
            }
         ],
         "VpcConfig": {
            "Ipv6AllowedForDualStack": boolean,
            "SecurityGroupIds": [ "string" ],
            "SubnetIds": [ "string" ],
            "VpcId": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeCanaries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Canaries](#API_DescribeCanaries_ResponseSyntax) **   <a name="synthetics-DescribeCanaries-response-Canaries"></a>
Returns an array. Each item in the array contains the full information about one canary.
Type: Array of [Canary](API_Canary.md) objects

 ** [NextToken](#API_DescribeCanaries_ResponseSyntax) **   <a name="synthetics-DescribeCanaries-response-NextToken"></a>
A token that indicates that there is more data available. You can use this token in a subsequent `DescribeCanaries` operation to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 252.

## Errors
<a name="API_DescribeCanaries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An unknown internal error occurred.
HTTP Status Code: 500

 ** ValidationException **
A parameter could not be validated.
HTTP Status Code: 400

## See Also
<a name="API_DescribeCanaries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/synthetics-2017-10-11/DescribeCanaries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/synthetics-2017-10-11/DescribeCanaries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/DescribeCanaries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/synthetics-2017-10-11/DescribeCanaries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/DescribeCanaries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/synthetics-2017-10-11/DescribeCanaries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/synthetics-2017-10-11/DescribeCanaries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/synthetics-2017-10-11/DescribeCanaries)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/synthetics-2017-10-11/DescribeCanaries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/DescribeCanaries)
