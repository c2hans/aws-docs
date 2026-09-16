---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetConnection.html
---

# GetConnection
<a name="API_GetConnection"></a>

Retrieves a connection definition from the Data Catalog.

## Request Syntax
<a name="API_GetConnection_RequestSyntax"></a>

```
{
   "ApplyOverrideForComputeEnvironment": "{{string}}",
   "CatalogId": "{{string}}",
   "HidePassword": {{boolean}},
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_GetConnection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApplyOverrideForComputeEnvironment](#API_GetConnection_RequestSyntax) **   <a name="Glue-GetConnection-request-ApplyOverrideForComputeEnvironment"></a>
For connections that may be used in multiple services, specifies returning properties for the specified compute environment.
Type: String
Valid Values: `SPARK | ATHENA | PYTHON`
Required: No

 ** [CatalogId](#API_GetConnection_RequestSyntax) **   <a name="Glue-GetConnection-request-CatalogId"></a>
The ID of the Data Catalog in which the connection resides. If none is provided, the AWS account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [HidePassword](#API_GetConnection_RequestSyntax) **   <a name="Glue-GetConnection-request-HidePassword"></a>
Allows you to retrieve the connection metadata without returning the password. For instance, the AWS Glue console uses this flag to retrieve the connection, and does not display the password. Set this parameter when the caller might not have permission to use the AWS KMS key to decrypt the password, but it does have permission to access the rest of the connection properties.
Type: Boolean
Required: No

 ** [Name](#API_GetConnection_RequestSyntax) **   <a name="Glue-GetConnection-request-Name"></a>
The name of the connection definition to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetConnection_ResponseSyntax"></a>

```
{
   "Connection": {
      "AthenaProperties": {
         "string" : "string"
      },
      "AuthenticationConfiguration": {
         "AuthenticationType": "string",
         "KmsKeyArn": "string",
         "OAuth2Properties": {
            "OAuth2ClientApplication": {
               "AWSManagedClientApplicationReference": "string",
               "UserManagedClientApplicationClientId": "string"
            },
            "OAuth2GrantType": "string",
            "TokenUrl": "string",
            "TokenUrlParametersMap": {
               "string" : "string"
            }
         },
         "SecretArn": "string"
      },
      "CompatibleComputeEnvironments": [ "string" ],
      "ConnectionProperties": {
         "string" : "string"
      },
      "ConnectionSchemaVersion": number,
      "ConnectionType": "string",
      "CreationTime": number,
      "Description": "string",
      "LastConnectionValidationTime": number,
      "LastUpdatedBy": "string",
      "LastUpdatedTime": number,
      "MatchCriteria": [ "string" ],
      "Name": "string",
      "PhysicalConnectionRequirements": {
         "AvailabilityZone": "string",
         "SecurityGroupIdList": [ "string" ],
         "SubnetId": "string"
      },
      "PythonProperties": {
         "string" : "string"
      },
      "SparkProperties": {
         "string" : "string"
      },
      "Status": "string",
      "StatusReason": "string"
   }
}
```

## Response Elements
<a name="API_GetConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Connection](#API_GetConnection_ResponseSyntax) **   <a name="Glue-GetConnection-response-Connection"></a>
The requested connection definition.
Type: [Connection](API_Connection.md) object

## Errors
<a name="API_GetConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
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

## See Also
<a name="API_GetConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetConnection)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetConnection)
