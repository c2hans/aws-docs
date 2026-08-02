---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ListFlows.html
---

# ListFlows
<a name="API_ListFlows"></a>

 Lists all of the flows associated with your account.

## Request Syntax
<a name="API_ListFlows_RequestSyntax"></a>

```
POST /list-flows HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListFlows_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListFlows_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListFlows_RequestSyntax) **   <a name="appflow-ListFlows-request-maxResults"></a>
 Specifies the maximum number of items that should be returned in the result set.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListFlows_RequestSyntax) **   <a name="appflow-ListFlows-request-nextToken"></a>
 The pagination token for next page of data.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `\S+`
Required: No

## Response Syntax
<a name="API_ListFlows_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "flows": [
      {
         "createdAt": number,
         "createdBy": "string",
         "description": "string",
         "destinationConnectorLabel": "string",
         "destinationConnectorType": "string",
         "flowArn": "string",
         "flowName": "string",
         "flowStatus": "string",
         "lastRunExecutionDetails": {
            "mostRecentExecutionMessage": "string",
            "mostRecentExecutionStatus": "string",
            "mostRecentExecutionTime": number
         },
         "lastUpdatedAt": number,
         "lastUpdatedBy": "string",
         "sourceConnectorLabel": "string",
         "sourceConnectorType": "string",
         "tags": {
            "string" : "string"
         },
         "triggerType": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListFlows_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [flows](#API_ListFlows_ResponseSyntax) **   <a name="appflow-ListFlows-response-flows"></a>
 The list of flows associated with your account.
Type: Array of [FlowDefinition](API_FlowDefinition.md) objects

 ** [nextToken](#API_ListFlows_ResponseSyntax) **   <a name="appflow-ListFlows-response-nextToken"></a>
 The pagination token for next page of data.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `\S+`

## Errors
<a name="API_ListFlows_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ValidationException **
 The request has invalid or missing parameters.
HTTP Status Code: 400

## Examples
<a name="API_ListFlows_Examples"></a>

### ListFlows examples
<a name="API_ListFlows_Example_1"></a>

This example shows a sample request for the `ListFlows` API. In the second sample, note that `MaxResults` will show a number between 1 and 100.

#### Sample Request
<a name="API_ListFlows_Example_1_Request"></a>

```
{
  "flowList": [
    {
      "createdAt": "created_time_value",
      "createdBy": "arn:aws:iam::<AccountId>:user/BetaTestUser",
      "description": "test flow 1 description",
      "destinationConnectorType": "S3",
      "destinationConnectorLabel": "MyCustomDestinationConnector",
      "flowArn": "arn:aws:appflow:region:<AccountId>:flow/test-flow-1",
      "flowName": "test-flow-1",
      "flowStatus": "Active",
      "lastRunExecutionDetails":
      {
        "mostRecentExecutionMessage": "Successfully ran the flow",
        "mostRecentExecutionStatus": "Successful",
        "mostRecentExecutionTime": "execution_time_value"
      },
      "lastUpdatedAt": "lastupdated_time_value",
      "lastUpdatedBy": "arn:aws:iam::<AccountId>:user/BetaTestUser",
      "sourceConnectorType": "Salesforce",
      "sourceConnectorLabel": "MyCustomSourceConnector",
      "tags":
      {
        "internalId": "<InternalId>",
        "resourceArn": "arn:aws:appflow:region:<AccountId>:flow/test-flow-1"
      },
      "triggerType": "OnDemand"
    }
  ],
  "nextToken": "next_token_value"
}
```

```
{
  "maxResults": 1
}
```

## See Also
<a name="API_ListFlows_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appflow-2020-08-23/ListFlows)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appflow-2020-08-23/ListFlows)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/ListFlows)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appflow-2020-08-23/ListFlows)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/ListFlows)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appflow-2020-08-23/ListFlows)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appflow-2020-08-23/ListFlows)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appflow-2020-08-23/ListFlows)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appflow-2020-08-23/ListFlows)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/ListFlows)
