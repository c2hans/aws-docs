---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeauthorizeConnection.html
---

# DeauthorizeConnection
<a name="API_DeauthorizeConnection"></a>

Removes all authorization parameters from the connection. This lets you remove the secret from the connection so you can reuse it without having to create a new connection.

## Request Syntax
<a name="API_DeauthorizeConnection_RequestSyntax"></a>

```
{
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_DeauthorizeConnection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_DeauthorizeConnection_RequestSyntax) **   <a name="eventbridge-DeauthorizeConnection-request-Name"></a>
The name of the connection to remove authorization from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_DeauthorizeConnection_ResponseSyntax"></a>

```
{
   "ConnectionArn": "string",
   "ConnectionState": "string",
   "CreationTime": number,
   "LastAuthorizedTime": number,
   "LastModifiedTime": number
}
```

## Response Elements
<a name="API_DeauthorizeConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectionArn](#API_DeauthorizeConnection_ResponseSyntax) **   <a name="eventbridge-DeauthorizeConnection-response-ConnectionArn"></a>
The ARN of the connection that authorization was removed from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:connection\/[\.\-_A-Za-z0-9]+\/[\-A-Za-z0-9]+$`

 ** [ConnectionState](#API_DeauthorizeConnection_ResponseSyntax) **   <a name="eventbridge-DeauthorizeConnection-response-ConnectionState"></a>
The state of the connection.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | AUTHORIZED | DEAUTHORIZED | AUTHORIZING | DEAUTHORIZING | ACTIVE | FAILED_CONNECTIVITY`

 ** [CreationTime](#API_DeauthorizeConnection_ResponseSyntax) **   <a name="eventbridge-DeauthorizeConnection-response-CreationTime"></a>
A time stamp for the time that the connection was created.
Type: Timestamp

 ** [LastAuthorizedTime](#API_DeauthorizeConnection_ResponseSyntax) **   <a name="eventbridge-DeauthorizeConnection-response-LastAuthorizedTime"></a>
A time stamp for the time that the connection was last authorized.
Type: Timestamp

 ** [LastModifiedTime](#API_DeauthorizeConnection_ResponseSyntax) **   <a name="eventbridge-DeauthorizeConnection-response-LastModifiedTime"></a>
A time stamp for the time that the connection was last updated.
Type: Timestamp

## Errors
<a name="API_DeauthorizeConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
There is concurrent modification on a rule, target, archive, or replay.
HTTP Status Code: 400

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An entity that you specified does not exist.
HTTP Status Code: 400

## See Also
<a name="API_DeauthorizeConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/DeauthorizeConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/DeauthorizeConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/DeauthorizeConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/DeauthorizeConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/DeauthorizeConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/DeauthorizeConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/DeauthorizeConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/DeauthorizeConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/DeauthorizeConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/DeauthorizeConnection)
