---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_BatchGetFlowAssociation.html
---

# BatchGetFlowAssociation
<a name="API_BatchGetFlowAssociation"></a>

Retrieve the flow associations for the given resources.

## Request Syntax
<a name="API_BatchGetFlowAssociation_RequestSyntax"></a>

```
POST /flow-associations-batch/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "ResourceIds": [ "{{string}}" ],
   "ResourceType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_BatchGetFlowAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_BatchGetFlowAssociation_RequestSyntax) **   <a name="connect-BatchGetFlowAssociation-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_BatchGetFlowAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ResourceIds](#API_BatchGetFlowAssociation_RequestSyntax) **   <a name="connect-BatchGetFlowAssociation-request-ResourceIds"></a>
A list of resource identifiers to retrieve flow associations.
+  AWS End User Messaging SMS phone number ARN when using `SMS_PHONE_NUMBER`
+  AWS End User Messaging Social phone number ARN when using `WHATSAPP_MESSAGING_PHONE_NUMBER`
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

 ** [ResourceType](#API_BatchGetFlowAssociation_RequestSyntax) **   <a name="connect-BatchGetFlowAssociation-request-ResourceType"></a>
The type of resource association.
Type: String
Valid Values: `VOICE_PHONE_NUMBER`
Required: No

## Response Syntax
<a name="API_BatchGetFlowAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "FlowAssociationSummaryList": [
      {
         "FlowId": "string",
         "ResourceId": "string",
         "ResourceType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetFlowAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FlowAssociationSummaryList](#API_BatchGetFlowAssociation_ResponseSyntax) **   <a name="connect-BatchGetFlowAssociation-response-FlowAssociationSummaryList"></a>
Information about flow associations.
Type: Array of [FlowAssociationSummary](API_FlowAssociationSummary.md) objects

## Errors
<a name="API_BatchGetFlowAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

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
<a name="API_BatchGetFlowAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/BatchGetFlowAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/BatchGetFlowAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/BatchGetFlowAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/BatchGetFlowAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/BatchGetFlowAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/BatchGetFlowAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/BatchGetFlowAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/BatchGetFlowAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/BatchGetFlowAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/BatchGetFlowAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
