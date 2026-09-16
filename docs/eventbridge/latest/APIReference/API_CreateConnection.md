---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateConnection.html
---

# CreateConnection
<a name="API_CreateConnection"></a>

Creates a connection. A connection defines the authorization type and credentials to use for authorization with an API destination HTTP endpoint.

For more information, see [Connections for endpoint targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-target-connection.html) in the *Amazon EventBridge User Guide*.

## Request Syntax
<a name="API_CreateConnection_RequestSyntax"></a>

```
{
   "AuthorizationType": "{{string}}",
   "AuthParameters": {
      "ApiKeyAuthParameters": {
         "ApiKeyName": "{{string}}",
         "ApiKeyValue": "{{string}}"
      },
      "BasicAuthParameters": {
         "Password": "{{string}}",
         "Username": "{{string}}"
      },
      "ConnectivityParameters": {
         "ResourceParameters": {
            "ResourceConfigurationArn": "{{string}}"
         }
      },
      "InvocationHttpParameters": {
         "BodyParameters": [
            {
               "IsValueSecret": {{boolean}},
               "Key": "{{string}}",
               "Value": "{{string}}"
            }
         ],
         "HeaderParameters": [
            {
               "IsValueSecret": {{boolean}},
               "Key": "{{string}}",
               "Value": "{{string}}"
            }
         ],
         "QueryStringParameters": [
            {
               "IsValueSecret": {{boolean}},
               "Key": "{{string}}",
               "Value": "{{string}}"
            }
         ]
      },
      "OAuthParameters": {
         "AuthorizationEndpoint": "{{string}}",
         "ClientParameters": {
            "ClientID": "{{string}}",
            "ClientSecret": "{{string}}"
         },
         "HttpMethod": "{{string}}",
         "OAuthHttpParameters": {
            "BodyParameters": [
               {
                  "IsValueSecret": {{boolean}},
                  "Key": "{{string}}",
                  "Value": "{{string}}"
               }
            ],
            "HeaderParameters": [
               {
                  "IsValueSecret": {{boolean}},
                  "Key": "{{string}}",
                  "Value": "{{string}}"
               }
            ],
            "QueryStringParameters": [
               {
                  "IsValueSecret": {{boolean}},
                  "Key": "{{string}}",
                  "Value": "{{string}}"
               }
            ]
         }
      }
   },
   "Description": "{{string}}",
   "InvocationConnectivityParameters": {
      "ResourceParameters": {
         "ResourceConfigurationArn": "{{string}}"
      }
   },
   "KmsKeyIdentifier": "{{string}}",
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateConnection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AuthorizationType](#API_CreateConnection_RequestSyntax) **   <a name="eventbridge-CreateConnection-request-AuthorizationType"></a>
The type of authorization to use for the connection.
OAUTH tokens are refreshed when a 401 or 407 response is returned.
Type: String
Valid Values: `BASIC | OAUTH_CLIENT_CREDENTIALS | API_KEY`
Required: Yes

 ** [AuthParameters](#API_CreateConnection_RequestSyntax) **   <a name="eventbridge-CreateConnection-request-AuthParameters"></a>
The authorization parameters to use to authorize with the endpoint.
You must include only authorization parameters for the `AuthorizationType` you specify.
Type: [CreateConnectionAuthRequestParameters](API_CreateConnectionAuthRequestParameters.md) object
Required: Yes

 ** [Description](#API_CreateConnection_RequestSyntax) **   <a name="eventbridge-CreateConnection-request-Description"></a>
A description for the connection to create.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`
Required: No

 ** [InvocationConnectivityParameters](#API_CreateConnection_RequestSyntax) **   <a name="eventbridge-CreateConnection-request-InvocationConnectivityParameters"></a>
For connections to private APIs, the parameters to use for invoking the API.
For more information, see [Connecting to private APIs](https://docs.aws.amazon.com/eventbridge/latest/userguide/connection-private.html) in the * *Amazon EventBridge User Guide* *.
Type: [ConnectivityResourceParameters](API_ConnectivityResourceParameters.md) object
Required: No

 ** [KmsKeyIdentifier](#API_CreateConnection_RequestSyntax) **   <a name="eventbridge-CreateConnection-request-KmsKeyIdentifier"></a>
The identifier of the AWS KMS customer managed key for EventBridge to use, if you choose to use a customer managed key to encrypt this connection. The identifier can be the key Amazon Resource Name (ARN), KeyId, key alias, or key alias ARN.
If you do not specify a customer managed key identifier, EventBridge uses an AWS owned key to encrypt the connection.
For more information, see [Identify and view keys](https://docs.aws.amazon.com/kms/latest/developerguide/viewing-keys.html) in the * AWS Key Management Service Developer Guide*.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[a-zA-Z0-9_\-/:]*$`
Required: No

 ** [Name](#API_CreateConnection_RequestSyntax) **   <a name="eventbridge-CreateConnection-request-Name"></a>
The name for the connection to create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_CreateConnection_ResponseSyntax"></a>

```
{
   "ConnectionArn": "string",
   "ConnectionState": "string",
   "CreationTime": number,
   "LastModifiedTime": number
}
```

## Response Elements
<a name="API_CreateConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectionArn](#API_CreateConnection_ResponseSyntax) **   <a name="eventbridge-CreateConnection-response-ConnectionArn"></a>
The ARN of the connection that was created by the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:connection\/[\.\-_A-Za-z0-9]+\/[\-A-Za-z0-9]+$`

 ** [ConnectionState](#API_CreateConnection_ResponseSyntax) **   <a name="eventbridge-CreateConnection-response-ConnectionState"></a>
The state of the connection that was created by the request.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | AUTHORIZED | DEAUTHORIZED | AUTHORIZING | DEAUTHORIZING | ACTIVE | FAILED_CONNECTIVITY`

 ** [CreationTime](#API_CreateConnection_ResponseSyntax) **   <a name="eventbridge-CreateConnection-response-CreationTime"></a>
A time stamp for the time that the connection was created.
Type: Timestamp

 ** [LastModifiedTime](#API_CreateConnection_ResponseSyntax) **   <a name="eventbridge-CreateConnection-response-LastModifiedTime"></a>
A time stamp for the time that the connection was last updated.
Type: Timestamp

## Errors
<a name="API_CreateConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have the necessary permissions for this action.
HTTP Status Code: 400

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** LimitExceededException **
The request failed because it attempted to create resource beyond the allowed service quota.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
The resource you are trying to create already exists.
HTTP Status Code: 400

 ** ResourceNotFoundException **
An entity that you specified does not exist.
HTTP Status Code: 400

 ** ThrottlingException **
This request cannot be completed due to throttling issues.
HTTP Status Code: 400

## See Also
<a name="API_CreateConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/CreateConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/CreateConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/CreateConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/CreateConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/CreateConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/CreateConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/CreateConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/CreateConnection)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/CreateConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/CreateConnection)
