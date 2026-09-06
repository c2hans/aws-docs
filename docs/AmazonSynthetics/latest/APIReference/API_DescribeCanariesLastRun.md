---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanariesLastRun.html
---

# DescribeCanariesLastRun
<a name="API_DescribeCanariesLastRun"></a>

Use this operation to see information from the most recent run of each canary that you have created.

This operation supports resource-level authorization using an IAM policy and the `Names` parameter. If you specify the `Names` parameter, the operation is successful only if you have authorization to view all the canaries that you specify in your request. If you do not have permission to view any of the canaries, the request fails with a 403 response.

You are required to use the `Names` parameter if you are logged on to a user or role that has an IAM policy that restricts which canaries that you are allowed to view. For more information, see [ Limiting a user to viewing specific canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Restricted.html).

## Request Syntax
<a name="API_DescribeCanariesLastRun_RequestSyntax"></a>

```
POST /canaries/last-run HTTP/1.1
Content-type: application/json

{
   "BrowserType": "{{string}}",
   "MaxResults": {{number}},
   "Names": [ "{{string}}" ],
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeCanariesLastRun_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeCanariesLastRun_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [BrowserType](#API_DescribeCanariesLastRun_RequestSyntax) **   <a name="synthetics-DescribeCanariesLastRun-request-BrowserType"></a>
The type of browser to use for the canary run.
Type: String
Valid Values: `CHROME | FIREFOX`
Required: No

 ** [MaxResults](#API_DescribeCanariesLastRun_RequestSyntax) **   <a name="synthetics-DescribeCanariesLastRun-request-MaxResults"></a>
Specify this parameter to limit how many runs are returned each time you use the `DescribeLastRun` operation. If you omit this parameter, the default of 100 is used.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [Names](#API_DescribeCanariesLastRun_RequestSyntax) **   <a name="synthetics-DescribeCanariesLastRun-request-Names"></a>
Use this parameter to return only canaries that match the names that you specify here. You can specify as many as five canary names.
If you specify this parameter, the operation is successful only if you have authorization to view all the canaries that you specify in your request. If you do not have permission to view any of the canaries, the request fails with a 403 response.
You are required to use the `Names` parameter if you are logged on to a user or role that has an IAM policy that restricts which canaries that you are allowed to view. For more information, see [ Limiting a user to viewing specific canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Restricted.html).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[0-9a-z_\-]+$`
Required: No

 ** [NextToken](#API_DescribeCanariesLastRun_RequestSyntax) **   <a name="synthetics-DescribeCanariesLastRun-request-NextToken"></a>
A token that indicates that there is more data available. You can use this token in a subsequent `DescribeCanariesLastRun` operation to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 252.
Required: No

## Response Syntax
<a name="API_DescribeCanariesLastRun_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CanariesLastRun": [
      {
         "CanaryName": "string",
         "LastRun": {
            "ArtifactS3Location": "string",
            "BrowserType": "string",
            "DryRunConfig": {
               "DryRunId": "string"
            },
            "Id": "string",
            "Location": "string",
            "Name": "string",
            "RetryAttempt": number,
            "ScheduledRunId": "string",
            "Status": {
               "State": "string",
               "StateReason": "string",
               "StateReasonCode": "string",
               "TestResult": "string"
            },
            "Timeline": {
               "Completed": number,
               "MetricTimestampForRunAndRetries": number,
               "Started": number
            }
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeCanariesLastRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CanariesLastRun](#API_DescribeCanariesLastRun_ResponseSyntax) **   <a name="synthetics-DescribeCanariesLastRun-response-CanariesLastRun"></a>
An array that contains the information from the most recent run of each canary.
Type: Array of [CanaryLastRun](API_CanaryLastRun.md) objects

 ** [NextToken](#API_DescribeCanariesLastRun_ResponseSyntax) **   <a name="synthetics-DescribeCanariesLastRun-response-NextToken"></a>
A token that indicates that there is more data available. You can use this token in a subsequent `DescribeCanariesLastRun` operation to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 252.

## Errors
<a name="API_DescribeCanariesLastRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An unknown internal error occurred.
HTTP Status Code: 500

 ** ValidationException **
A parameter could not be validated.
HTTP Status Code: 400

## See Also
<a name="API_DescribeCanariesLastRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/synthetics-2017-10-11/DescribeCanariesLastRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/synthetics-2017-10-11/DescribeCanariesLastRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/DescribeCanariesLastRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/synthetics-2017-10-11/DescribeCanariesLastRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/DescribeCanariesLastRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/synthetics-2017-10-11/DescribeCanariesLastRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/synthetics-2017-10-11/DescribeCanariesLastRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/synthetics-2017-10-11/DescribeCanariesLastRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/synthetics-2017-10-11/DescribeCanariesLastRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/DescribeCanariesLastRun)
