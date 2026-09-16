---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetConnection.html
---

# GetConnection
<a name="API_GetConnection"></a>

Gets a connection. In Amazon DataZone, a connection enables you to connect your resources (domains, projects, and environments) to external resources and services.

## Request Syntax
<a name="API_GetConnection_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/connections/{{identifier}}?withSecret={{withSecret}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetConnection_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetConnection_RequestSyntax) **   <a name="datazone-GetConnection-request-uri-domainIdentifier"></a>
The ID of the domain where we get the connection.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_GetConnection_RequestSyntax) **   <a name="datazone-GetConnection-request-uri-identifier"></a>
The connection ID.
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: Yes

 ** [withSecret](#API_GetConnection_RequestSyntax) **   <a name="datazone-GetConnection-request-uri-withSecret"></a>
Specifies whether a connection has a secret.

## Request Body
<a name="API_GetConnection_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetConnection_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configurations": [
      {
         "classification": "string",
         "properties": {
            "string" : "string"
         }
      }
   ],
   "connectionCredentials": {
      "accessKeyId": "string",
      "expiration": "string",
      "secretAccessKey": "string",
      "sessionToken": "string"
   },
   "connectionId": "string",
   "description": "string",
   "domainId": "string",
   "domainUnitId": "string",
   "environmentId": "string",
   "environmentUserRole": "string",
   "name": "string",
   "physicalEndpoints": [
      {
         "awsLocation": {
            "accessRole": "string",
            "awsAccountId": "string",
            "awsRegion": "string",
            "iamConnectionId": "string"
         },
         "enableTrustedIdentityPropagation": boolean,
         "glueConnection": {
            "athenaProperties": {
               "string" : "string"
            },
            "authenticationConfiguration": {
               "authenticationType": "string",
               "oAuth2Properties": {
                  "authorizationCodeProperties": {
                     "authorizationCode": "string",
                     "redirectUri": "string"
                  },
                  "oAuth2ClientApplication": {
                     "aWSManagedClientApplicationReference": "string",
                     "userManagedClientApplicationClientId": "string"
                  },
                  "oAuth2Credentials": {
                     "accessToken": "string",
                     "jwtToken": "string",
                     "refreshToken": "string",
                     "userManagedClientApplicationClientSecret": "string"
                  },
                  "oAuth2GrantType": "string",
                  "tokenUrl": "string",
                  "tokenUrlParametersMap": {
                     "string" : "string"
                  }
               },
               "secretArn": "string"
            },
            "compatibleComputeEnvironments": [ "string" ],
            "connectionProperties": {
               "string" : "string"
            },
            "connectionSchemaVersion": number,
            "connectionType": "string",
            "creationTime": number,
            "description": "string",
            "lastConnectionValidationTime": number,
            "lastUpdatedBy": "string",
            "lastUpdatedTime": number,
            "matchCriteria": [ "string" ],
            "name": "string",
            "physicalConnectionRequirements": {
               "availabilityZone": "string",
               "securityGroupIdList": [ "string" ],
               "subnetId": "string",
               "subnetIdList": [ "string" ]
            },
            "pythonProperties": {
               "string" : "string"
            },
            "sparkProperties": {
               "string" : "string"
            },
            "status": "string",
            "statusReason": "string"
         },
         "glueConnectionName": "string",
         "glueConnectionNames": [ "string" ],
         "host": "string",
         "port": number,
         "protocol": "string",
         "stage": "string"
      }
   ],
   "projectId": "string",
   "props": { ... },
   "scope": "string",
   "type": "string"
}
```

## Response Elements
<a name="API_GetConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configurations](#API_GetConnection_ResponseSyntax) **   <a name="datazone-GetConnection-response-configurations"></a>
The configurations of the connection.
Type: Array of [Configuration](API_Configuration.md) objects

 ** [connectionCredentials](#API_GetConnection_ResponseSyntax) **   <a name="datazone-GetConnection-response-connectionCredentials"></a>
Connection credentials.
Type: [ConnectionCredentials](API_ConnectionCredentials.md) object

 ** [connectionId](#API_GetConnection_ResponseSyntax) **   <a name="datazone-GetConnection-response-connectionId"></a>
The ID of the connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.

 ** [description](#API_GetConnection_ResponseSyntax) **   <a name="datazone-GetConnection-response-description"></a>
Connection description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_GetConnection_ResponseSyntax) **   <a name="datazone-GetConnection-response-domainId"></a>
The domain ID of the connection.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [domainUnitId](#API_GetConnection_ResponseSyntax) **   <a name="datazone-GetConnection-response-domainUnitId"></a>
The domain unit ID of the connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`

 ** [environmentId](#API_GetConnection_ResponseSyntax) **   <a name="datazone-GetConnection-response-environmentId"></a>
The ID of the environment.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [environmentUserRole](#API_GetConnection_ResponseSyntax) **   <a name="datazone-GetConnection-response-environmentUserRole"></a>
The environment user role.
Type: String

 ** [name](#API_GetConnection_ResponseSyntax) **   <a name="datazone-GetConnection-response-name"></a>
The name of the connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.

 ** [physicalEndpoints](#API_GetConnection_ResponseSyntax) **   <a name="datazone-GetConnection-response-physicalEndpoints"></a>
The physical endpoints of the connection.
Type: Array of [PhysicalEndpoint](API_PhysicalEndpoint.md) objects

 ** [projectId](#API_GetConnection_ResponseSyntax) **   <a name="datazone-GetConnection-response-projectId"></a>
The ID of the project.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [props](#API_GetConnection_ResponseSyntax) **   <a name="datazone-GetConnection-response-props"></a>
Connection props.
Type: [ConnectionPropertiesOutput](API_ConnectionPropertiesOutput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [scope](#API_GetConnection_ResponseSyntax) **   <a name="datazone-GetConnection-response-scope"></a>
The scope of the connection.
Type: String
Valid Values: `DOMAIN | PROJECT`

 ** [type](#API_GetConnection_ResponseSyntax) **   <a name="datazone-GetConnection-response-type"></a>
The type of the connection.
Type: String
Valid Values: `ATHENA | BIGQUERY | DATABRICKS | DOCUMENTDB | DYNAMODB | HYPERPOD | IAM | MYSQL | OPENSEARCH | ORACLE | POSTGRESQL | REDSHIFT | S3 | SAPHANA | SNOWFLAKE | SPARK | SQLSERVER | TERADATA | VERTICA | WORKFLOWS_MWAA | AMAZON_Q | MLFLOW | VPC | GIT`

## Errors
<a name="API_GetConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetConnection)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetConnection)
