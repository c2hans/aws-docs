---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeConnection.html
---

# DescribeConnection
<a name="API_DescribeConnection"></a>

Retrieves details about a connection.

## Request Syntax
<a name="API_DescribeConnection_RequestSyntax"></a>

```
{
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeConnection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_DescribeConnection_RequestSyntax) **   <a name="eventbridge-DescribeConnection-request-Name"></a>
The name of the connection to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_DescribeConnection_ResponseSyntax"></a>

```
{
   "AuthorizationType": "string",
   "AuthParameters": {
      "ApiKeyAuthParameters": {
         "ApiKeyName": "string"
      },
      "BasicAuthParameters": {
         "Username": "string"
      },
      "ConnectivityParameters": {
         "ResourceParameters": {
            "ResourceAssociationArn": "string",
            "ResourceConfigurationArn": "string"
         }
      },
      "InvocationHttpParameters": {
         "BodyParameters": [
            {
               "IsValueSecret": boolean,
               "Key": "string",
               "Value": "string"
            }
         ],
         "HeaderParameters": [
            {
               "IsValueSecret": boolean,
               "Key": "string",
               "Value": "string"
            }
         ],
         "QueryStringParameters": [
            {
               "IsValueSecret": boolean,
               "Key": "string",
               "Value": "string"
            }
         ]
      },
      "OAuthParameters": {
         "AuthorizationEndpoint": "string",
         "ClientParameters": {
            "ClientID": "string"
         },
         "HttpMethod": "string",
         "OAuthHttpParameters": {
            "BodyParameters": [
               {
                  "IsValueSecret": boolean,
                  "Key": "string",
                  "Value": "string"
               }
            ],
            "HeaderParameters": [
               {
                  "IsValueSecret": boolean,
                  "Key": "string",
                  "Value": "string"
               }
            ],
            "QueryStringParameters": [
               {
                  "IsValueSecret": boolean,
                  "Key": "string",
                  "Value": "string"
               }
            ]
         }
      }
   },
   "ConnectionArn": "string",
   "ConnectionState": "string",
   "CreationTime": number,
   "Description": "string",
   "InvocationConnectivityParameters": {
      "ResourceParameters": {
         "ResourceAssociationArn": "string",
         "ResourceConfigurationArn": "string"
      }
   },
   "KmsKeyIdentifier": "string",
   "LastAuthorizedTime": number,
   "LastModifiedTime": number,
   "Name": "string",
   "SecretArn": "string",
   "StateReason": "string"
}
```

## Response Elements
<a name="API_DescribeConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthorizationType](#API_DescribeConnection_ResponseSyntax) **   <a name="eventbridge-DescribeConnection-response-AuthorizationType"></a>
The type of authorization specified for the connection.
Type: String
Valid Values: `BASIC | OAUTH_CLIENT_CREDENTIALS | API_KEY`

 ** [AuthParameters](#API_DescribeConnection_ResponseSyntax) **   <a name="eventbridge-DescribeConnection-response-AuthParameters"></a>
The parameters to use for authorization for the connection.
Type: [ConnectionAuthResponseParameters](API_ConnectionAuthResponseParameters.md) object

 ** [ConnectionArn](#API_DescribeConnection_ResponseSyntax) **   <a name="eventbridge-DescribeConnection-response-ConnectionArn"></a>
The ARN of the connection retrieved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:connection\/[\.\-_A-Za-z0-9]+\/[\-A-Za-z0-9]+$`

 ** [ConnectionState](#API_DescribeConnection_ResponseSyntax) **   <a name="eventbridge-DescribeConnection-response-ConnectionState"></a>
The state of the connection retrieved.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | AUTHORIZED | DEAUTHORIZED | AUTHORIZING | DEAUTHORIZING | ACTIVE | FAILED_CONNECTIVITY`

 ** [CreationTime](#API_DescribeConnection_ResponseSyntax) **   <a name="eventbridge-DescribeConnection-response-CreationTime"></a>
A time stamp for the time that the connection was created.
Type: Timestamp

 ** [Description](#API_DescribeConnection_ResponseSyntax) **   <a name="eventbridge-DescribeConnection-response-Description"></a>
The description for the connection retrieved.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`

 ** [InvocationConnectivityParameters](#API_DescribeConnection_ResponseSyntax) **   <a name="eventbridge-DescribeConnection-response-InvocationConnectivityParameters"></a>
For connections to private APIs The parameters EventBridge uses to invoke the resource endpoint.
For more information, see [Connecting to private APIs](https://docs.aws.amazon.com/eventbridge/latest/userguide/connection-private.html) in the * *Amazon EventBridge User Guide* *.
Type: [DescribeConnectionConnectivityParameters](API_DescribeConnectionConnectivityParameters.md) object

 ** [KmsKeyIdentifier](#API_DescribeConnection_ResponseSyntax) **   <a name="eventbridge-DescribeConnection-response-KmsKeyIdentifier"></a>
The identifier of the AWS KMS customer managed key for EventBridge to use to encrypt the connection, if one has been specified.
For more information, see [Encrypting connections](https://docs.aws.amazon.com/eventbridge/latest/userguide/encryption-connections.html) in the *Amazon EventBridge User Guide*.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[a-zA-Z0-9_\-/:]*$`

 ** [LastAuthorizedTime](#API_DescribeConnection_ResponseSyntax) **   <a name="eventbridge-DescribeConnection-response-LastAuthorizedTime"></a>
A time stamp for the time that the connection was last authorized.
Type: Timestamp

 ** [LastModifiedTime](#API_DescribeConnection_ResponseSyntax) **   <a name="eventbridge-DescribeConnection-response-LastModifiedTime"></a>
A time stamp for the time that the connection was last modified.
Type: Timestamp

 ** [Name](#API_DescribeConnection_ResponseSyntax) **   <a name="eventbridge-DescribeConnection-response-Name"></a>
The name of the connection retrieved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`

 ** [SecretArn](#API_DescribeConnection_ResponseSyntax) **   <a name="eventbridge-DescribeConnection-response-SecretArn"></a>
The ARN of the secret created from the authorization parameters specified for the connection.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws([a-z]|\-)*:secretsmanager:([a-z]|\d|\-)*:([0-9]{12})?:secret:[\/_+=\.@\-A-Za-z0-9]+$`

 ** [StateReason](#API_DescribeConnection_ResponseSyntax) **   <a name="eventbridge-DescribeConnection-response-StateReason"></a>
The reason that the connection is in the current connection state.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`

## Errors
<a name="API_DescribeConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An entity that you specified does not exist.
HTTP Status Code: 400

## See Also
<a name="API_DescribeConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/DescribeConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/DescribeConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/DescribeConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/DescribeConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/DescribeConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/DescribeConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/DescribeConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/DescribeConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/DescribeConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/DescribeConnection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
