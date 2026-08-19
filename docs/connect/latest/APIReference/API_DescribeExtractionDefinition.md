---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeExtractionDefinition.html
---

# DescribeExtractionDefinition
<a name="API_DescribeExtractionDefinition"></a>

Describes an extraction definition in the specified Connect Customer instance.

## Request Syntax
<a name="API_DescribeExtractionDefinition_RequestSyntax"></a>

```
GET /extraction-definitions/{{InstanceId}}/{{ExtractionDefinitionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeExtractionDefinition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ExtractionDefinitionId](#API_DescribeExtractionDefinition_RequestSyntax) **   <a name="connect-DescribeExtractionDefinition-request-uri-ExtractionDefinitionId"></a>
The identifier of the extraction definition to describe.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_DescribeExtractionDefinition_RequestSyntax) **   <a name="connect-DescribeExtractionDefinition-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_DescribeExtractionDefinition_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeExtractionDefinition_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ExtractionDefinition": {
      "CreatedTime": number,
      "Display": {
         "Label": "string"
      },
      "ExtractionConfiguration": {
         "NotFoundBehavior": {
            "Behavior": "string",
            "DefaultValue": "string"
         },
         "PromptHint": "string"
      },
      "ExtractionDefinitionArn": "string",
      "ExtractionDefinitionId": "string",
      "LastUpdatedBy": "string",
      "LastUpdatedTime": number,
      "Name": "string",
      "Tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_DescribeExtractionDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExtractionDefinition](#API_DescribeExtractionDefinition_ResponseSyntax) **   <a name="connect-DescribeExtractionDefinition-response-ExtractionDefinition"></a>
The extraction definition.
Type: [ExtractionDefinition](API_ExtractionDefinition.md) object

## Errors
<a name="API_DescribeExtractionDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

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
<a name="API_DescribeExtractionDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DescribeExtractionDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DescribeExtractionDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DescribeExtractionDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DescribeExtractionDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DescribeExtractionDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DescribeExtractionDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DescribeExtractionDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DescribeExtractionDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DescribeExtractionDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DescribeExtractionDefinition)
