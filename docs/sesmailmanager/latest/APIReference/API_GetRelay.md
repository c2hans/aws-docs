---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetRelay.html
---

# GetRelay
<a name="API_GetRelay"></a>

Fetch the relay resource and it's attributes.

## Request Syntax
<a name="API_GetRelay_RequestSyntax"></a>

```
{
   "RelayId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetRelay_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RelayId](#API_GetRelay_RequestSyntax) **   <a name="sesmailmanager-GetRelay-request-RelayId"></a>
A unique relay identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_GetRelay_ResponseSyntax"></a>

```
{
   "Authentication": { ... },
   "CreatedTimestamp": number,
   "LastModifiedTimestamp": number,
   "RelayArn": "string",
   "RelayId": "string",
   "RelayName": "string",
   "ServerName": "string",
   "ServerPort": number
}
```

## Response Elements
<a name="API_GetRelay_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Authentication](#API_GetRelay_ResponseSyntax) **   <a name="sesmailmanager-GetRelay-response-Authentication"></a>
The authentication attribute—contains the secret ARN where the customer relay server credentials are stored.
Type: [RelayAuthentication](API_RelayAuthentication.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [CreatedTimestamp](#API_GetRelay_ResponseSyntax) **   <a name="sesmailmanager-GetRelay-response-CreatedTimestamp"></a>
The timestamp of when the relay was created.
Type: Timestamp

 ** [LastModifiedTimestamp](#API_GetRelay_ResponseSyntax) **   <a name="sesmailmanager-GetRelay-response-LastModifiedTimestamp"></a>
The timestamp of when relay was last updated.
Type: Timestamp

 ** [RelayArn](#API_GetRelay_ResponseSyntax) **   <a name="sesmailmanager-GetRelay-response-RelayArn"></a>
The Amazon Resource Name (ARN) of the relay.
Type: String

 ** [RelayId](#API_GetRelay_ResponseSyntax) **   <a name="sesmailmanager-GetRelay-response-RelayId"></a>
The unique relay identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`

 ** [RelayName](#API_GetRelay_ResponseSyntax) **   <a name="sesmailmanager-GetRelay-response-RelayName"></a>
The unique name of the relay.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-_]+`

 ** [ServerName](#API_GetRelay_ResponseSyntax) **   <a name="sesmailmanager-GetRelay-response-ServerName"></a>
The destination relay server address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-\.]+`

 ** [ServerPort](#API_GetRelay_ResponseSyntax) **   <a name="sesmailmanager-GetRelay-response-ServerPort"></a>
The destination relay server port.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.

## Errors
<a name="API_GetRelay_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
Occurs when a requested resource is not found.
HTTP Status Code: 400

 ** ValidationException **
The request validation has failed. For details, see the accompanying error message.
HTTP Status Code: 400

## See Also
<a name="API_GetRelay_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/GetRelay)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/GetRelay)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/GetRelay)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/GetRelay)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/GetRelay)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/GetRelay)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/GetRelay)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/GetRelay)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/GetRelay)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/GetRelay)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
