---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateTopicV2.html
---

# UpdateTopicV2
<a name="API_UpdateTopicV2"></a>

Updates the definition of a Q topic.

## Request Syntax
<a name="API_UpdateTopicV2_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/topicsV2/{{TopicId}} HTTP/1.1
Content-type: application/json

{
   "CustomInstructions": {
      "CustomInstructionsString": "{{string}}"
   },
   "PublishOption": "{{string}}",
   "Topic": {
      "DataSetRelations": [
         {
            "Left": {
               "ColumnNames": [ "{{string}}" ],
               "DataSetArn": "{{string}}"
            },
            "Right": {
               "ColumnNames": [ "{{string}}" ],
               "DataSetArn": "{{string}}"
            }
         }
      ],
      "DataSets": [
         {
            "DataSetArn": "{{string}}",
            "DataSetName": "{{string}}"
         }
      ],
      "Description": "{{string}}",
      "Name": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateTopicV2_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateTopicV2_RequestSyntax) **   <a name="QS-UpdateTopicV2-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the topic that you want to update.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [TopicId](#API_UpdateTopicV2_RequestSyntax) **   <a name="QS-UpdateTopicV2-request-uri-TopicId"></a>
The ID of the topic that you want to modify. This ID is unique per AWS Region for each AWS account.
Length Constraints: Maximum length of 256.
Pattern: `^[A-Za-z0-9-_.\\+]*$`
Required: Yes

## Request Body
<a name="API_UpdateTopicV2_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Topic](#API_UpdateTopicV2_RequestSyntax) **   <a name="QS-UpdateTopicV2-request-Topic"></a>
The definition of the topic that you want to update.
Type: [TopicV2Details](API_TopicV2Details.md) object
Required: Yes

 ** [CustomInstructions](#API_UpdateTopicV2_RequestSyntax) **   <a name="QS-UpdateTopicV2-request-CustomInstructions"></a>
Instructions that provide additional guidance and context for response generation.
Type: [CustomInstructions](API_CustomInstructions.md) object
Required: No

 ** [PublishOption](#API_UpdateTopicV2_RequestSyntax) **   <a name="QS-UpdateTopicV2-request-PublishOption"></a>
The publish option for the topic that you want to update.
Type: String
Valid Values: `DRAFT | PUBLISH`
Required: No

## Response Syntax
<a name="API_UpdateTopicV2_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "RequestId": "string",
   "TopicId": "string"
}
```

## Response Elements
<a name="API_UpdateTopicV2_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateTopicV2_ResponseSyntax) **   <a name="QS-UpdateTopicV2-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateTopicV2_ResponseSyntax) **   <a name="QS-UpdateTopicV2-response-Arn"></a>
The Amazon Resource Name (ARN) of the topic.
Type: String

 ** [RequestId](#API_UpdateTopicV2_ResponseSyntax) **   <a name="QS-UpdateTopicV2-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [TopicId](#API_UpdateTopicV2_ResponseSyntax) **   <a name="QS-UpdateTopicV2-response-TopicId"></a>
The ID of the topic that you want to modify. This ID is unique per AWS Region for each AWS account.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^[A-Za-z0-9-_.\\+]*$`

## Errors
<a name="API_UpdateTopicV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 409

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

 ** LimitExceededException **
A limit is exceeded.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
Limit exceeded.
HTTP Status Code: 409

 ** ResourceExistsException **
The resource specified already exists.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 409

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
<a name="API_UpdateTopicV2_Examples"></a>

### Example
<a name="API_UpdateTopicV2_Example_1"></a>

This example illustrates one usage of UpdateTopicV2.

#### Sample Request
<a name="API_UpdateTopicV2_Example_1_Request"></a>

```
PUT /accounts/{AwsAccountId}/topicsV2/{TopicId} HTTP/1.1
Content-type: application/json
```

## See Also
<a name="API_UpdateTopicV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateTopicV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateTopicV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateTopicV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateTopicV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateTopicV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateTopicV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateTopicV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateTopicV2)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateTopicV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateTopicV2)
