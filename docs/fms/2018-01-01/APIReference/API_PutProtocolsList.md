---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_PutProtocolsList.html
---

# PutProtocolsList
<a name="API_PutProtocolsList"></a>

Creates an AWS Firewall Manager protocols list.

## Request Syntax
<a name="API_PutProtocolsList_RequestSyntax"></a>

```
{
   "ProtocolsList": {
      "CreateTime": {{number}},
      "LastUpdateTime": {{number}},
      "ListId": "{{string}}",
      "ListName": "{{string}}",
      "ListUpdateToken": "{{string}}",
      "PreviousProtocolsList": {
         "{{string}}" : [ "{{string}}" ]
      },
      "ProtocolsList": [ "{{string}}" ]
   },
   "TagList": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_PutProtocolsList_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ProtocolsList](#API_PutProtocolsList_RequestSyntax) **   <a name="fms-PutProtocolsList-request-ProtocolsList"></a>
The details of the AWS Firewall Manager protocols list to be created.
Type: [ProtocolsListData](API_ProtocolsListData.md) object
Required: Yes

 ** [TagList](#API_PutProtocolsList_RequestSyntax) **   <a name="fms-PutProtocolsList-request-TagList"></a>
The tags associated with the resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_PutProtocolsList_ResponseSyntax"></a>

```
{
   "ProtocolsList": {
      "CreateTime": number,
      "LastUpdateTime": number,
      "ListId": "string",
      "ListName": "string",
      "ListUpdateToken": "string",
      "PreviousProtocolsList": {
         "string" : [ "string" ]
      },
      "ProtocolsList": [ "string" ]
   },
   "ProtocolsListArn": "string"
}
```

## Response Elements
<a name="API_PutProtocolsList_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProtocolsList](#API_PutProtocolsList_ResponseSyntax) **   <a name="fms-PutProtocolsList-response-ProtocolsList"></a>
The details of the AWS Firewall Manager protocols list.
Type: [ProtocolsListData](API_ProtocolsListData.md) object

 ** [ProtocolsListArn](#API_PutProtocolsList_ResponseSyntax) **   <a name="fms-PutProtocolsList-response-ProtocolsListArn"></a>
The Amazon Resource Name (ARN) of the protocols list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

## Errors
<a name="API_PutProtocolsList_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
The operation failed because of a system problem, even though the request was valid. Retry your request.
HTTP Status Code: 400

 ** InvalidInputException **
The parameters of the request were invalid.
HTTP Status Code: 400

 ** InvalidOperationException **
The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an `AssociateAdminAccount` request for an account ID that was already set as the AWS Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for AWS Organizations before you can access it.
HTTP Status Code: 400

 ** LimitExceededException **
The operation exceeds a resource limit, for example, the maximum number of `policy` objects that you can create for an AWS account. For more information, see [Firewall Manager Limits](https://docs.aws.amazon.com/waf/latest/developerguide/fms-limits.html) in the * AWS WAF Developer Guide*.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_PutProtocolsList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fms-2018-01-01/PutProtocolsList)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fms-2018-01-01/PutProtocolsList)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/PutProtocolsList)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fms-2018-01-01/PutProtocolsList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/PutProtocolsList)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fms-2018-01-01/PutProtocolsList)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fms-2018-01-01/PutProtocolsList)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fms-2018-01-01/PutProtocolsList)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/fms-2018-01-01/PutProtocolsList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/PutProtocolsList)
