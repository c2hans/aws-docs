---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_CreateRelay.html
---

# CreateRelay
<a name="API_CreateRelay"></a>

Creates a relay resource which can be used in rules to relay incoming emails to defined relay destinations.

## Request Syntax
<a name="API_CreateRelay_RequestSyntax"></a>

```
{
   "Authentication": { ... },
   "ClientToken": "{{string}}",
   "RelayName": "{{string}}",
   "ServerName": "{{string}}",
   "ServerPort": {{number}},
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateRelay_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Authentication](#API_CreateRelay_RequestSyntax) **   <a name="sesmailmanager-CreateRelay-request-Authentication"></a>
Authentication for the relay destination server—specify the secretARN where the SMTP credentials are stored.
Type: [RelayAuthentication](API_RelayAuthentication.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [ClientToken](#API_CreateRelay_RequestSyntax) **   <a name="sesmailmanager-CreateRelay-request-ClientToken"></a>
A unique token that Amazon SES uses to recognize subsequent retries of the same request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [RelayName](#API_CreateRelay_RequestSyntax) **   <a name="sesmailmanager-CreateRelay-request-RelayName"></a>
The unique name of the relay resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-_]+`
Required: Yes

 ** [ServerName](#API_CreateRelay_RequestSyntax) **   <a name="sesmailmanager-CreateRelay-request-ServerName"></a>
The destination relay server address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-\.]+`
Required: Yes

 ** [ServerPort](#API_CreateRelay_RequestSyntax) **   <a name="sesmailmanager-CreateRelay-request-ServerPort"></a>
The destination relay server port.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: Yes

 ** [Tags](#API_CreateRelay_RequestSyntax) **   <a name="sesmailmanager-CreateRelay-request-Tags"></a>
The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateRelay_ResponseSyntax"></a>

```
{
   "RelayId": "string"
}
```

## Response Elements
<a name="API_CreateRelay_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RelayId](#API_CreateRelay_ResponseSyntax) **   <a name="sesmailmanager-CreateRelay-response-RelayId"></a>
A unique identifier of the created relay resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`

## Errors
<a name="API_CreateRelay_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request configuration has conflicts. For details, see the accompanying error message.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
Occurs when an operation exceeds a predefined service quota or limit.
HTTP Status Code: 400

 ** ValidationException **
The request validation has failed. For details, see the accompanying error message.
HTTP Status Code: 400

## See Also
<a name="API_CreateRelay_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/CreateRelay)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/CreateRelay)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/CreateRelay)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/CreateRelay)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/CreateRelay)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/CreateRelay)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/CreateRelay)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/CreateRelay)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/CreateRelay)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/CreateRelay)
