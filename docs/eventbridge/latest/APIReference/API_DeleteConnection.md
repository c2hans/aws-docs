---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeleteConnection.html
---

# DeleteConnection
<a name="API_DeleteConnection"></a>

Deletes a connection.

## Request Syntax
<a name="API_DeleteConnection_RequestSyntax"></a>

```
{
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteConnection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_DeleteConnection_RequestSyntax) **   <a name="eventbridge-DeleteConnection-request-Name"></a>
The name of the connection to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_DeleteConnection_ResponseSyntax"></a>

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
<a name="API_DeleteConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectionArn](#API_DeleteConnection_ResponseSyntax) **   <a name="eventbridge-DeleteConnection-response-ConnectionArn"></a>
The ARN of the connection that was deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:connection\/[\.\-_A-Za-z0-9]+\/[\-A-Za-z0-9]+$`

 ** [ConnectionState](#API_DeleteConnection_ResponseSyntax) **   <a name="eventbridge-DeleteConnection-response-ConnectionState"></a>
The state of the connection before it was deleted.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | AUTHORIZED | DEAUTHORIZED | AUTHORIZING | DEAUTHORIZING | ACTIVE | FAILED_CONNECTIVITY`

 ** [CreationTime](#API_DeleteConnection_ResponseSyntax) **   <a name="eventbridge-DeleteConnection-response-CreationTime"></a>
A time stamp for the time that the connection was created.
Type: Timestamp

 ** [LastAuthorizedTime](#API_DeleteConnection_ResponseSyntax) **   <a name="eventbridge-DeleteConnection-response-LastAuthorizedTime"></a>
A time stamp for the time that the connection was last authorized before it wa deleted.
Type: Timestamp

 ** [LastModifiedTime](#API_DeleteConnection_ResponseSyntax) **   <a name="eventbridge-DeleteConnection-response-LastModifiedTime"></a>
A time stamp for the time that the connection was last modified before it was deleted.
Type: Timestamp

## Errors
<a name="API_DeleteConnection_Errors"></a>

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
<a name="API_DeleteConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/DeleteConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/DeleteConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/DeleteConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/DeleteConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/DeleteConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/DeleteConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/DeleteConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/DeleteConnection)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/DeleteConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/DeleteConnection)
