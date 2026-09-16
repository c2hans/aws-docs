---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_GetTrack.html
---

# GetTrack
<a name="API_GetTrack"></a>

Get the Redshift Serverless version for a specified track.

## Request Syntax
<a name="API_GetTrack_RequestSyntax"></a>

```
{
   "trackName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetTrack_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [trackName](#API_GetTrack_RequestSyntax) **   <a name="redshiftserverless-GetTrack-request-trackName"></a>
The name of the track of which its version is fetched.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_]+`
Required: Yes

## Response Syntax
<a name="API_GetTrack_ResponseSyntax"></a>

```
{
   "track": {
      "trackName": "string",
      "updateTargets": [
         {
            "trackName": "string",
            "workgroupVersion": "string"
         }
      ],
      "workgroupVersion": "string"
   }
}
```

## Response Elements
<a name="API_GetTrack_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [track](#API_GetTrack_ResponseSyntax) **   <a name="redshiftserverless-GetTrack-response-track"></a>
The version of the specified track.
Type: [ServerlessTrack](API_ServerlessTrack.md) object

## Errors
<a name="API_GetTrack_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConflictException **
The submitted action has conflicts.
HTTP Status Code: 400

 ** DryRunException **
This exception is thrown when the request was successful, but dry run was enabled so no action was taken.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceName **
The name of the resource that could not be found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## Examples
<a name="API_GetTrack_Examples"></a>

### Example
<a name="API_GetTrack_Example_1"></a>

This example illustrates one usage of GetTrack.

#### Sample Request
<a name="API_GetTrack_Example_1_Request"></a>

```
aws redshift-serverless get-track
 --track-name current
--region us-east-1
```

#### Sample Response
<a name="API_GetTrack_Example_1_Response"></a>

```
{
    "track": {
        "trackName": "current",
        "workgroupVersion": "1.0.107360",
        "updateTargets": [
            {
                "trackName": "trailing",
                "workgroupVersion": "1.0.106452"
            }
        ]
    }
}
```

## See Also
<a name="API_GetTrack_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/GetTrack)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/GetTrack)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/GetTrack)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/GetTrack)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/GetTrack)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/GetTrack)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/GetTrack)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/GetTrack)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/GetTrack)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/GetTrack)
