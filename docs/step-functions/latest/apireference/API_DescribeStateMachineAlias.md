---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeStateMachineAlias.html
---

# DescribeStateMachineAlias
<a name="API_DescribeStateMachineAlias"></a>

Returns details about a state machine [alias](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html).

 **Related operations:**
+  [CreateStateMachineAlias](API_CreateStateMachineAlias.md)
+  [ListStateMachineAliases](API_ListStateMachineAliases.md)
+  [UpdateStateMachineAlias](API_UpdateStateMachineAlias.md)
+  [DeleteStateMachineAlias](API_DeleteStateMachineAlias.md)

## Request Syntax
<a name="API_DescribeStateMachineAlias_RequestSyntax"></a>

```
{
   "stateMachineAliasArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeStateMachineAlias_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [stateMachineAliasArn](#API_DescribeStateMachineAlias_RequestSyntax) **   <a name="StepFunctions-DescribeStateMachineAlias-request-stateMachineAliasArn"></a>
The Amazon Resource Name (ARN) of the state machine alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_DescribeStateMachineAlias_ResponseSyntax"></a>

```
{
   "creationDate": number,
   "description": "string",
   "name": "string",
   "routingConfiguration": [
      {
         "stateMachineVersionArn": "string",
         "weight": number
      }
   ],
   "stateMachineAliasArn": "string",
   "updateDate": number
}
```

## Response Elements
<a name="API_DescribeStateMachineAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationDate](#API_DescribeStateMachineAlias_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachineAlias-response-creationDate"></a>
The date the state machine alias was created.
Type: Timestamp

 ** [description](#API_DescribeStateMachineAlias_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachineAlias-response-description"></a>
A description of the alias.
Type: String
Length Constraints: Maximum length of 256.

 ** [name](#API_DescribeStateMachineAlias_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachineAlias-response-name"></a>
The name of the state machine alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.

 ** [routingConfiguration](#API_DescribeStateMachineAlias_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachineAlias-response-routingConfiguration"></a>
The routing configuration of the alias.
Type: Array of [RoutingConfigurationListItem](API_RoutingConfigurationListItem.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.

 ** [stateMachineAliasArn](#API_DescribeStateMachineAlias_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachineAlias-response-stateMachineAliasArn"></a>
The Amazon Resource Name (ARN) of the state machine alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [updateDate](#API_DescribeStateMachineAlias_ResponseSyntax) **   <a name="StepFunctions-DescribeStateMachineAlias-response-updateDate"></a>
The date the state machine alias was last updated.
For a newly created state machine, this is the same as the creation date.
Type: Timestamp

## Errors
<a name="API_DescribeStateMachineAlias_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArn **
The provided Amazon Resource Name (ARN) is not valid.
HTTP Status Code: 400

 ** ResourceNotFound **
Could not find the referenced resource.
HTTP Status Code: 400

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
 ** reason **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_DescribeStateMachineAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/states-2016-11-23/DescribeStateMachineAlias)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/states-2016-11-23/DescribeStateMachineAlias)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/DescribeStateMachineAlias)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/states-2016-11-23/DescribeStateMachineAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/DescribeStateMachineAlias)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/states-2016-11-23/DescribeStateMachineAlias)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/states-2016-11-23/DescribeStateMachineAlias)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/states-2016-11-23/DescribeStateMachineAlias)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/states-2016-11-23/DescribeStateMachineAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/DescribeStateMachineAlias)
