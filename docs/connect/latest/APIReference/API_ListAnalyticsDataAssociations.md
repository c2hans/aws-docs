---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListAnalyticsDataAssociations.html
---

# ListAnalyticsDataAssociations
<a name="API_ListAnalyticsDataAssociations"></a>

Lists the association status of requested dataset ID for a given Connect Customer instance.

## Request Syntax
<a name="API_ListAnalyticsDataAssociations_RequestSyntax"></a>

```
GET /analytics-data/instance/{{InstanceId}}/association?DataSetId={{DataSetId}}&maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAnalyticsDataAssociations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DataSetId](#API_ListAnalyticsDataAssociations_RequestSyntax) **   <a name="connect-ListAnalyticsDataAssociations-request-uri-DataSetId"></a>
The identifier of the dataset to get the association status.
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [InstanceId](#API_ListAnalyticsDataAssociations_RequestSyntax) **   <a name="connect-ListAnalyticsDataAssociations-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_ListAnalyticsDataAssociations_RequestSyntax) **   <a name="connect-ListAnalyticsDataAssociations-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListAnalyticsDataAssociations_RequestSyntax) **   <a name="connect-ListAnalyticsDataAssociations-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

## Request Body
<a name="API_ListAnalyticsDataAssociations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAnalyticsDataAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Results": [
      {
         "DataSetId": "string",
         "ResourceShareArn": "string",
         "ResourceShareId": "string",
         "ResourceShareStatus": "string",
         "TargetAccountId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListAnalyticsDataAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListAnalyticsDataAssociations_ResponseSyntax) **   <a name="connect-ListAnalyticsDataAssociations-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

 ** [Results](#API_ListAnalyticsDataAssociations_ResponseSyntax) **   <a name="connect-ListAnalyticsDataAssociations-response-Results"></a>
An array of successful results: `DataSetId`, `TargetAccountId`, `ResourceShareId`, `ResourceShareArn`. This is a paginated API, so `nextToken` is given if there are more results to be returned.
Type: Array of [AnalyticsDataAssociationResult](API_AnalyticsDataAssociationResult.md) objects

## Errors
<a name="API_ListAnalyticsDataAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_ListAnalyticsDataAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListAnalyticsDataAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListAnalyticsDataAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListAnalyticsDataAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListAnalyticsDataAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListAnalyticsDataAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListAnalyticsDataAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListAnalyticsDataAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListAnalyticsDataAssociations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListAnalyticsDataAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListAnalyticsDataAssociations)
