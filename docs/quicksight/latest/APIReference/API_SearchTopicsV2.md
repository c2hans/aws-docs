---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SearchTopicsV2.html
---

# SearchTopicsV2
<a name="API_SearchTopicsV2"></a>

Searches for any Q topic that exists in an AWS account.

## Request Syntax
<a name="API_SearchTopicsV2_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/search/topicsV2 HTTP/1.1
Content-type: application/json

{
   "Filters": [
      {
         "Name": "{{string}}",
         "Operator": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SearchTopicsV2_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_SearchTopicsV2_RequestSyntax) **   <a name="QS-SearchTopicsV2-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the topic that you want to search.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

## Request Body
<a name="API_SearchTopicsV2_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_SearchTopicsV2_RequestSyntax) **   <a name="QS-SearchTopicsV2-request-Filters"></a>
The filters that you want to use to search for the topic.
Type: Array of [TopicSearchFilter](API_TopicSearchFilter.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** [MaxResults](#API_SearchTopicsV2_RequestSyntax) **   <a name="QS-SearchTopicsV2-request-MaxResults"></a>
The maximum number of results to be returned per request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_SearchTopicsV2_RequestSyntax) **   <a name="QS-SearchTopicsV2-request-NextToken"></a>
The token for the next set of results, or null if there are no more results.
Type: String
Required: No

## Response Syntax
<a name="API_SearchTopicsV2_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "NextToken": "string",
   "RequestId": "string",
   "TopicSummaryList": [
      {
         "Arn": "string",
         "Name": "string",
         "TopicId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_SearchTopicsV2_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_SearchTopicsV2_ResponseSyntax) **   <a name="QS-SearchTopicsV2-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_SearchTopicsV2_ResponseSyntax) **   <a name="QS-SearchTopicsV2-response-NextToken"></a>
The token for the next set of results, or null if there are no more results.
Type: String

 ** [RequestId](#API_SearchTopicsV2_ResponseSyntax) **   <a name="QS-SearchTopicsV2-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [TopicSummaryList](#API_SearchTopicsV2_ResponseSyntax) **   <a name="QS-SearchTopicsV2-response-TopicSummaryList"></a>
A list of topic summaries that is returned by the search topic request.
Type: Array of [TopicV2Summary](API_TopicV2Summary.md) objects

## Errors
<a name="API_SearchTopicsV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidNextTokenException **
The `NextToken` value isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## Examples
<a name="API_SearchTopicsV2_Examples"></a>

### Example
<a name="API_SearchTopicsV2_Example_1"></a>

This example illustrates one usage of SearchTopicsV2.

#### Sample Request
<a name="API_SearchTopicsV2_Example_1_Request"></a>

```
POST /accounts/{AwsAccountId}/search/topicsV2 HTTP/1.1
Content-type: application/json
```

## See Also
<a name="API_SearchTopicsV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/SearchTopicsV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/SearchTopicsV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SearchTopicsV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/SearchTopicsV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SearchTopicsV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/SearchTopicsV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/SearchTopicsV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/SearchTopicsV2)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/SearchTopicsV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SearchTopicsV2)
