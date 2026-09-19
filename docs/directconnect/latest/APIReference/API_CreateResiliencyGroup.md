---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateResiliencyGroup.html
---

# CreateResiliencyGroup
<a name="API_CreateResiliencyGroup"></a>

Creates a resiliency group. A resiliency group lets you group Direct Connect connections together and manage them as a single unit to meet a target resiliency model.

## Request Syntax
<a name="API_CreateResiliencyGroup_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "intendedResiliencyModel": "{{string}}",
   "resiliencyGroupName": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateResiliencyGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateResiliencyGroup_RequestSyntax) **   <a name="DX-CreateResiliencyGroup-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [intendedResiliencyModel](#API_CreateResiliencyGroup_RequestSyntax) **   <a name="DX-CreateResiliencyGroup-request-intendedResiliencyModel"></a>
The resiliency model that the resiliency group is intended to meet. The valid values are `maximum-resiliency`, `high-resiliency`, and `basic-resiliency`.
Type: String
Valid Values: `maximum-resiliency | high-resiliency | basic-resiliency`
Required: Yes

 ** [resiliencyGroupName](#API_CreateResiliencyGroup_RequestSyntax) **   <a name="DX-CreateResiliencyGroup-request-resiliencyGroupName"></a>
The name of the resiliency group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9_\-]+$`
Required: Yes

 ** [tags](#API_CreateResiliencyGroup_RequestSyntax) **   <a name="DX-CreateResiliencyGroup-request-tags"></a>
The tags to associate with the resiliency group.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.
Required: No

## Response Syntax
<a name="API_CreateResiliencyGroup_ResponseSyntax"></a>

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
<a name="API_CreateResiliencyGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [resiliencyGroup](#API_CreateResiliencyGroup_ResponseSyntax) **   <a name="DX-CreateResiliencyGroup-response-resiliencyGroup"></a>
Information about the resiliency group.
Type: [ResiliencyGroup](API_ResiliencyGroup.md) object

## Errors
<a name="API_CreateResiliencyGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

 ** DuplicateTagKeysException **
A tag key was specified more than once.
HTTP Status Code: 400

 ** LimitExceededException **
The rate limiter limit has been exceeded for the connection. You cannot add more rate limiters to virtual interfaces on this connection.
HTTP Status Code: 400

 ** TooManyTagsException **
You have reached the limit on the number of tags that can be assigned.
HTTP Status Code: 400

## See Also
<a name="API_CreateResiliencyGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/CreateResiliencyGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/CreateResiliencyGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/CreateResiliencyGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/CreateResiliencyGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/CreateResiliencyGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/CreateResiliencyGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/CreateResiliencyGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/CreateResiliencyGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/CreateResiliencyGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/CreateResiliencyGroup)
