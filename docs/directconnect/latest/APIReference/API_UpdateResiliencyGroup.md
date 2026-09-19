---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_UpdateResiliencyGroup.html
---

# UpdateResiliencyGroup
<a name="API_UpdateResiliencyGroup"></a>

Updates the name of the specified resiliency group.

## Request Syntax
<a name="API_UpdateResiliencyGroup_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "resiliencyGroupId": "{{string}}",
   "resiliencyGroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateResiliencyGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateResiliencyGroup_RequestSyntax) **   <a name="DX-UpdateResiliencyGroup-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [resiliencyGroupId](#API_UpdateResiliencyGroup_RequestSyntax) **   <a name="DX-UpdateResiliencyGroup-request-resiliencyGroupId"></a>
The ID of the resiliency group.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `^(dxrg|DXRG)-[0-9a-zA-Z]{17}$`
Required: Yes

 ** [resiliencyGroupName](#API_UpdateResiliencyGroup_RequestSyntax) **   <a name="DX-UpdateResiliencyGroup-request-resiliencyGroupName"></a>
The new name of the resiliency group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9_\-]+$`
Required: Yes

## Response Syntax
<a name="API_UpdateResiliencyGroup_ResponseSyntax"></a>

```
{
   "resiliencyGroup": {
      "ownerAccount": "string",
      "resiliencyGroupArn": "string",
      "resiliencyGroupId": "string",
      "resiliencyGroupName": "string",
      "resiliencyGroupType": "string",
      "state": "string",
      "tags": [
         {
            "key": "string",
            "value": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_UpdateResiliencyGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [resiliencyGroup](#API_UpdateResiliencyGroup_ResponseSyntax) **   <a name="DX-UpdateResiliencyGroup-response-resiliencyGroup"></a>
Information about the resiliency group.
Type: [ResiliencyGroup](API_ResiliencyGroup.md) object

## Errors
<a name="API_UpdateResiliencyGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_UpdateResiliencyGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/UpdateResiliencyGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/UpdateResiliencyGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/UpdateResiliencyGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/UpdateResiliencyGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/UpdateResiliencyGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/UpdateResiliencyGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/UpdateResiliencyGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/UpdateResiliencyGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/UpdateResiliencyGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/UpdateResiliencyGroup)
