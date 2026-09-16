---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeKnowledgeBase.html
---

# DescribeKnowledgeBase
<a name="API_DescribeKnowledgeBase"></a>

Describes a knowledge base.

## Request Syntax
<a name="API_DescribeKnowledgeBase_RequestSyntax"></a>

```
GET /v1/accounts/{{AwsAccountId}}/knowledge-bases/{{KnowledgeBaseId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeKnowledgeBase_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DescribeKnowledgeBase_RequestSyntax) **   <a name="QS-DescribeKnowledgeBase-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the knowledge base.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]*`
Required: Yes

 ** [KnowledgeBaseId](#API_DescribeKnowledgeBase_RequestSyntax) **   <a name="QS-DescribeKnowledgeBase-request-uri-KnowledgeBaseId"></a>
The unique identifier for the knowledge base.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[0-9a-zA-Z-_=.+]+`
Required: Yes

## Request Body
<a name="API_DescribeKnowledgeBase_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeKnowledgeBase_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "KnowledgeBase": {
      "AccessControlConfiguration": {
         "isACLEnabled": boolean
      },
      "CreatedAt": number,
      "DataSourceArn": "string",
      "Description": "string",
      "DocumentCount": number,
      "FirstCompletedIngestionSummary": {
         "EndTime": number,
         "IngestionId": "string",
         "IngestionStatus": "string",
         "StartTime": number
      },
      "FirstIncompleteIngestionSummary": {
         "EndTime": number,
         "IngestionId": "string",
         "IngestionStatus": "string",
         "StartTime": number
      },
      "IsEmailNotificationOptedForIngestionFailures": boolean,
      "KnowledgeBaseArn": "string",
      "KnowledgeBaseConfiguration": {
         "templateConfiguration": {
            "template": JSON value
         }
      },
      "KnowledgeBaseId": "string",
      "KnowledgeBaseSizeBytes": number,
      "LatestIngestionSummary": {
         "EndTime": number,
         "IngestionId": "string",
         "IngestionStatus": "string",
         "StartTime": number
      },
      "MediaExtractionConfiguration": {
         "audioExtractionConfiguration": {
            "audioExtractionStatus": "string"
         },
         "imageExtractionConfiguration": {
            "imageExtractionStatus": "string"
         },
         "videoExtractionConfiguration": {
            "videoExtractionStatus": "string",
            "videoExtractionType": "string"
         }
      },
      "Name": "string",
      "PrimaryOwnerArn": "string",
      "PrimaryOwnerUsername": "string",
      "Status": "string",
      "Type": "string",
      "UpdatedAt": number
   },
   "RequestId": "string"
}
```

## Response Elements
<a name="API_DescribeKnowledgeBase_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DescribeKnowledgeBase_ResponseSyntax) **   <a name="QS-DescribeKnowledgeBase-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [KnowledgeBase](#API_DescribeKnowledgeBase_ResponseSyntax) **   <a name="QS-DescribeKnowledgeBase-response-KnowledgeBase"></a>
The knowledge base.
Type: [KnowledgeBase](API_KnowledgeBase.md) object

 ** [RequestId](#API_DescribeKnowledgeBase_ResponseSyntax) **   <a name="QS-DescribeKnowledgeBase-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_DescribeKnowledgeBase_Errors"></a>

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

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** InvalidRequestException **
You don't have this feature activated for your account. To fix this issue, contact AWS support.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **
A limit is exceeded.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
Limit exceeded.
HTTP Status Code: 409

 ** PreconditionNotMetException **
One or more preconditions aren't met.
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

## See Also
<a name="API_DescribeKnowledgeBase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeKnowledgeBase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeKnowledgeBase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeKnowledgeBase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeKnowledgeBase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeKnowledgeBase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeKnowledgeBase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeKnowledgeBase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeKnowledgeBase)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeKnowledgeBase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeKnowledgeBase)
