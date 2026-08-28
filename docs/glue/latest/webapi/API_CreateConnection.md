---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CreateConnection.html
---

# CreateConnection
<a name="API_CreateConnection"></a>

Creates a connection definition in the Data Catalog.

Connections used for creating federated resources require the IAM `glue:PassConnection` permission.

## Request Syntax
<a name="API_CreateConnection_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "ConnectionInput": {
      "AthenaProperties": {
         "{{string}}" : "{{string}}"
      },
      "AuthenticationConfiguration": {
         "AuthenticationType": "{{string}}",
         "BasicAuthenticationCredentials": {
            "Password": "{{string}}",
            "Username": "{{string}}"
         },
         "CustomAuthenticationCredentials": {
            "{{string}}" : "{{string}}"
         },
         "KmsKeyArn": "{{string}}",
         "OAuth2Properties": {
            "AuthorizationCodeProperties": {
               "AuthorizationCode": "{{string}}",
               "RedirectUri": "{{string}}"
            },
            "OAuth2ClientApplication": {
               "AWSManagedClientApplicationReference": "{{string}}",
               "UserManagedClientApplicationClientId": "{{string}}"
            },
            "OAuth2Credentials": {
               "AccessToken": "{{string}}",
               "JwtToken": "{{string}}",
               "RefreshToken": "{{string}}",
               "UserManagedClientApplicationClientSecret": "{{string}}"
            },
            "OAuth2GrantType": "{{string}}",
            "TokenUrl": "{{string}}",
            "TokenUrlParametersMap": {
               "{{string}}" : "{{string}}"
            }
         },
         "SecretArn": "{{string}}"
      },
      "ConnectionProperties": {
         "{{string}}" : "{{string}}"
      },
      "ConnectionType": "{{string}}",
      "Description": "{{string}}",
      "MatchCriteria": [ "{{string}}" ],
      "Name": "{{string}}",
      "PhysicalConnectionRequirements": {
         "AvailabilityZone": "{{string}}",
         "SecurityGroupIdList": [ "{{string}}" ],
         "SubnetId": "{{string}}"
      },
      "PythonProperties": {
         "{{string}}" : "{{string}}"
      },
      "SparkProperties": {
         "{{string}}" : "{{string}}"
      },
      "ValidateCredentials": {{boolean}},
      "ValidateForComputeEnvironments": [ "{{string}}" ]
   },
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateConnection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_CreateConnection_RequestSyntax) **   <a name="Glue-CreateConnection-request-CatalogId"></a>
The ID of the Data Catalog in which to create the connection. If none is provided, the AWS account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [ConnectionInput](#API_CreateConnection_RequestSyntax) **   <a name="Glue-CreateConnection-request-ConnectionInput"></a>
A `ConnectionInput` object defining the connection to create.
Type: [ConnectionInput](API_ConnectionInput.md) object
Required: Yes

 ** [Tags](#API_CreateConnection_RequestSyntax) **   <a name="Glue-CreateConnection-request-Tags"></a>
The tags you assign to the connection.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateConnection_ResponseSyntax"></a>

```
{
   "CreateConnectionStatus": "string"
}
```

## Response Elements
<a name="API_CreateConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreateConnectionStatus](#API_CreateConnection_ResponseSyntax) **   <a name="Glue-CreateConnection-response-CreateConnectionStatus"></a>
The status of the connection creation request. The request can take some time for certain authentication types, for example when creating an OAuth connection with token exchange over VPC.
Type: String
Valid Values: `READY | IN_PROGRESS | FAILED`

## Errors
<a name="API_CreateConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExistsException **
A resource to be created or added already exists.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** GlueEncryptionException **
An encryption operation failed.
 ** Message **
The message describing the problem.
HTTP Status Code: 400

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ResourceNumberLimitExceededException **
A resource numerical limit was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_CreateConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/CreateConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/CreateConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CreateConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/CreateConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CreateConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/CreateConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/CreateConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/CreateConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/CreateConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CreateConnection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
