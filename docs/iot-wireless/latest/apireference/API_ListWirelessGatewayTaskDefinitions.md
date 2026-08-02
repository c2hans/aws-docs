---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListWirelessGatewayTaskDefinitions.html
---

# ListWirelessGatewayTaskDefinitions
<a name="API_ListWirelessGatewayTaskDefinitions"></a>

List the wireless gateway tasks definitions registered to your AWS account.

## Request Syntax
<a name="API_ListWirelessGatewayTaskDefinitions_RequestSyntax"></a>

```
GET /wireless-gateway-task-definitions?maxResults={{MaxResults}}&nextToken={{NextToken}}&taskDefinitionType={{TaskDefinitionType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListWirelessGatewayTaskDefinitions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListWirelessGatewayTaskDefinitions_RequestSyntax) **   <a name="iotwireless-ListWirelessGatewayTaskDefinitions-request-uri-MaxResults"></a>
The maximum number of results to return in this operation.
Valid Range: Minimum value of 0. Maximum value of 250.

 ** [NextToken](#API_ListWirelessGatewayTaskDefinitions_RequestSyntax) **   <a name="iotwireless-ListWirelessGatewayTaskDefinitions-request-uri-NextToken"></a>
To retrieve the next set of results, the `nextToken` value from a previous response; otherwise **null** to receive the first set of results.
Length Constraints: Maximum length of 4096.

 ** [TaskDefinitionType](#API_ListWirelessGatewayTaskDefinitions_RequestSyntax) **   <a name="iotwireless-ListWirelessGatewayTaskDefinitions-request-uri-TaskDefinitionType"></a>
A filter to list only the wireless gateway task definitions that use this task definition type.
Valid Values: `UPDATE`

## Request Body
<a name="API_ListWirelessGatewayTaskDefinitions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListWirelessGatewayTaskDefinitions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "TaskDefinitions": [
      {
         "Arn": "string",
         "Id": "string",
         "LoRaWAN": {
            "CurrentVersion": {
               "Model": "string",
               "PackageVersion": "string",
               "Station": "string"
            },
            "UpdateVersion": {
               "Model": "string",
               "PackageVersion": "string",
               "Station": "string"
            }
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListWirelessGatewayTaskDefinitions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListWirelessGatewayTaskDefinitions_ResponseSyntax) **   <a name="iotwireless-ListWirelessGatewayTaskDefinitions-response-NextToken"></a>
The token to use to get the next set of results, or **null** if there are no additional results.
Type: String
Length Constraints: Maximum length of 4096.

 ** [TaskDefinitions](#API_ListWirelessGatewayTaskDefinitions_ResponseSyntax) **   <a name="iotwireless-ListWirelessGatewayTaskDefinitions-response-TaskDefinitions"></a>
The list of task definitions.
Type: Array of [UpdateWirelessGatewayTaskEntry](API_UpdateWirelessGatewayTaskEntry.md) objects

## Errors
<a name="API_ListWirelessGatewayTaskDefinitions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing a request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied because it exceeded the allowed API request rate.
HTTP Status Code: 429

 ** ValidationException **
The input did not meet the specified constraints.
HTTP Status Code: 400

## See Also
<a name="API_ListWirelessGatewayTaskDefinitions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/ListWirelessGatewayTaskDefinitions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/ListWirelessGatewayTaskDefinitions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/ListWirelessGatewayTaskDefinitions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/ListWirelessGatewayTaskDefinitions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/ListWirelessGatewayTaskDefinitions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/ListWirelessGatewayTaskDefinitions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/ListWirelessGatewayTaskDefinitions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/ListWirelessGatewayTaskDefinitions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/ListWirelessGatewayTaskDefinitions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/ListWirelessGatewayTaskDefinitions)
