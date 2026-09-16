---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListDeployments.html
---

# ListDeployments
<a name="API_ListDeployments"></a>

Lists the deployments for an environment in descending deployment number order.

## Request Syntax
<a name="API_ListDeployments_RequestSyntax"></a>

```
GET /applications/{{ApplicationId}}/environments/{{EnvironmentId}}/deployments?max_results={{MaxResults}}&next_token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDeployments_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationId](#API_ListDeployments_RequestSyntax) **   <a name="appconfig-ListDeployments-request-uri-ApplicationId"></a>
The ID or name of the application.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [EnvironmentId](#API_ListDeployments_RequestSyntax) **   <a name="appconfig-ListDeployments-request-uri-EnvironmentId"></a>
The ID or name of the environment.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [MaxResults](#API_ListDeployments_RequestSyntax) **   <a name="appconfig-ListDeployments-request-uri-MaxResults"></a>
The maximum number of items that may be returned for this call. If there are items that have not yet been returned, the response will include a non-null `NextToken` that you can provide in a subsequent call to get the next set of results.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_ListDeployments_RequestSyntax) **   <a name="appconfig-ListDeployments-request-uri-NextToken"></a>
The token returned by a prior call to this operation indicating the next set of results to be returned. If not specified, the operation will return the first set of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Request Body
<a name="API_ListDeployments_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDeployments_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "CompletedAt": "string",
         "ConfigurationName": "string",
         "ConfigurationProfileId": "string",
         "ConfigurationVersion": "string",
         "DeploymentDurationInMinutes": number,
         "DeploymentNumber": number,
         "FinalBakeTimeInMinutes": number,
         "GrowthFactor": number,
         "GrowthType": "string",
         "PercentageComplete": number,
         "StartedAt": "string",
         "State": "string",
         "Type": "string",
         "VersionLabel": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDeployments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListDeployments_ResponseSyntax) **   <a name="appconfig-ListDeployments-response-Items"></a>
The elements from this collection.
Type: Array of [DeploymentSummary](API_DeploymentSummary.md) objects

 ** [NextToken](#API_ListDeployments_ResponseSyntax) **   <a name="appconfig-ListDeployments-response-NextToken"></a>
The token for the next set of items to return. Use this token to get the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListDeployments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input fails to satisfy the constraints specified by an AWS service.
 ** Details **
Detailed information about the input that failed to satisfy the constraints specified by a call.
HTTP Status Code: 400

 ** InternalServerException **
There was an internal failure in the AWS AppConfig service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource could not be found.
HTTP Status Code: 404

## Examples
<a name="API_ListDeployments_Examples"></a>

### Example
<a name="API_ListDeployments_Example_1"></a>

This example illustrates one usage of ListDeployments.

#### Sample Request
<a name="API_ListDeployments_Example_1_Request"></a>

```
GET /applications/abc1234/environments/54j1r29/deployments HTTP/1.1
Host: appconfig.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.134-73.228.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/appconfig.list-deployments
X-Amz-Date: 20210920T182141Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210920/us-east-1/appconfig/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
```

#### Sample Response
<a name="API_ListDeployments_Example_1_Response"></a>

```
{
    "Items": [
        {
            "DeploymentNumber": 1,
            "ConfigurationName": "Example-Configuration-Profile",
            "ConfigurationVersion": "1",
            "DeploymentDurationInMinutes": 15,
            "GrowthType": "LINEAR",
            "GrowthFactor": 25.0,
            "FinalBakeTimeInMinutes": 0,
            "State": "COMPLETE",
            "PercentageComplete": 100.0,
            "StartedAt": "2021-09-17T21:43:54.205000+00:00",
            "CompletedAt": "2021-09-17T21:59:03.888000+00:00"
        }
    ]
}
```

## See Also
<a name="API_ListDeployments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/ListDeployments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/ListDeployments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/ListDeployments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/ListDeployments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/ListDeployments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/ListDeployments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/ListDeployments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/ListDeployments)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/ListDeployments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/ListDeployments)
