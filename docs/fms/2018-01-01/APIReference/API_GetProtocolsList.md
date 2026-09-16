---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetProtocolsList.html
---

# GetProtocolsList
<a name="API_GetProtocolsList"></a>

Returns information about the specified AWS Firewall Manager protocols list.

## Request Syntax
<a name="API_GetProtocolsList_RequestSyntax"></a>

```
{
   "DefaultList": {{boolean}},
   "ListId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetProtocolsList_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DefaultList](#API_GetProtocolsList_RequestSyntax) **   <a name="fms-GetProtocolsList-request-DefaultList"></a>
Specifies whether the list to retrieve is a default list owned by AWS Firewall Manager.
Type: Boolean
Required: No

 ** [ListId](#API_GetProtocolsList_RequestSyntax) **   <a name="fms-GetProtocolsList-request-ListId"></a>
The ID of the AWS Firewall Manager protocols list that you want the details for.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-z0-9A-Z-]{36}$`
Required: Yes

## Response Syntax
<a name="API_GetProtocolsList_ResponseSyntax"></a>

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
<a name="API_GetProtocolsList_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProtocolsList](#API_GetProtocolsList_ResponseSyntax) **   <a name="fms-GetProtocolsList-response-ProtocolsList"></a>
Information about the specified AWS Firewall Manager protocols list.
Type: [ProtocolsListData](API_ProtocolsListData.md) object

 ** [ProtocolsListArn](#API_GetProtocolsList_ResponseSyntax) **   <a name="fms-GetProtocolsList-response-ProtocolsListArn"></a>
The Amazon Resource Name (ARN) of the specified protocols list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

## Errors
<a name="API_GetProtocolsList_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
The operation failed because of a system problem, even though the request was valid. Retry your request.
HTTP Status Code: 400

 ** InvalidOperationException **
The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an `AssociateAdminAccount` request for an account ID that was already set as the AWS Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for AWS Organizations before you can access it.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_GetProtocolsList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fms-2018-01-01/GetProtocolsList)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fms-2018-01-01/GetProtocolsList)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/GetProtocolsList)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fms-2018-01-01/GetProtocolsList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/GetProtocolsList)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fms-2018-01-01/GetProtocolsList)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fms-2018-01-01/GetProtocolsList)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fms-2018-01-01/GetProtocolsList)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/fms-2018-01-01/GetProtocolsList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/GetProtocolsList)
