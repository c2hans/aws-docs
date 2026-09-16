---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateConnection.html
---

# CreateConnection
<a name="API_CreateConnection"></a>

Creates a new connection. In Amazon DataZone, a connection enables you to connect your resources (domains, projects, and environments) to external resources and services.

## Request Syntax
<a name="API_CreateConnection_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/connections HTTP/1.1
Content-type: application/json

{
   "awsLocation": {
      "accessRole": "{{string}}",
      "awsAccountId": "{{string}}",
      "awsRegion": "{{string}}",
      "iamConnectionId": "{{string}}"
   },
   "clientToken": "{{string}}",
   "configurations": [
      {
         "classification": "{{string}}",
         "properties": {
            "{{string}}" : "{{string}}"
         }
      }
   ],
   "description": "{{string}}",
   "enableTrustedIdentityPropagation": {{boolean}},
   "environmentIdentifier": "{{string}}",
   "name": "{{string}}",
   "props": { ... },
   "scope": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateConnection_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_CreateConnection_RequestSyntax) **   <a name="datazone-CreateConnection-request-uri-domainIdentifier"></a>
The ID of the domain where the connection is created.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_CreateConnection_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [awsLocation](#API_CreateConnection_RequestSyntax) **   <a name="datazone-CreateConnection-request-awsLocation"></a>
The location where the connection is created.
Type: [AwsLocation](API_AwsLocation.md) object
Required: No

 ** [clientToken](#API_CreateConnection_RequestSyntax) **   <a name="datazone-CreateConnection-request-clientToken"></a>
A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.
Type: String
Required: No

 ** [configurations](#API_CreateConnection_RequestSyntax) **   <a name="datazone-CreateConnection-request-configurations"></a>
The configurations of the connection.
Type: Array of [Configuration](API_Configuration.md) objects
Required: No

 ** [description](#API_CreateConnection_RequestSyntax) **   <a name="datazone-CreateConnection-request-description"></a>
A connection description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** [enableTrustedIdentityPropagation](#API_CreateConnection_RequestSyntax) **   <a name="datazone-CreateConnection-request-enableTrustedIdentityPropagation"></a>
Specifies whether the trusted identity propagation is enabled.
Type: Boolean
Required: No

 ** [environmentIdentifier](#API_CreateConnection_RequestSyntax) **   <a name="datazone-CreateConnection-request-environmentIdentifier"></a>
The ID of the environment where the connection is created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** [name](#API_CreateConnection_RequestSyntax) **   <a name="datazone-CreateConnection-request-name"></a>
The connection name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: Yes

 ** [props](#API_CreateConnection_RequestSyntax) **   <a name="datazone-CreateConnection-request-props"></a>
The connection props.
Type: [ConnectionPropertiesInput](API_ConnectionPropertiesInput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [scope](#API_CreateConnection_RequestSyntax) **   <a name="datazone-CreateConnection-request-scope"></a>
The scope of the connection.
Type: String
Valid Values: `DOMAIN | PROJECT`
Required: No

## Response Syntax
<a name="API_CreateConnection_ResponseSyntax"></a>

```
HTTP/1.1 201
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
   "connectionId": "string",
   "description": "string",
   "domainId": "string",
   "domainUnitId": "string",
   "environmentId": "string",
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
<a name="API_CreateConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [configurations](#API_CreateConnection_ResponseSyntax) **   <a name="datazone-CreateConnection-response-configurations"></a>
The configurations of the connection.
Type: Array of [Configuration](API_Configuration.md) objects

 ** [connectionId](#API_CreateConnection_ResponseSyntax) **   <a name="datazone-CreateConnection-response-connectionId"></a>
The ID of the connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.

 ** [description](#API_CreateConnection_ResponseSyntax) **   <a name="datazone-CreateConnection-response-description"></a>
The connection description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_CreateConnection_ResponseSyntax) **   <a name="datazone-CreateConnection-response-domainId"></a>
The ID of the domain where the connection is created.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [domainUnitId](#API_CreateConnection_ResponseSyntax) **   <a name="datazone-CreateConnection-response-domainUnitId"></a>
The ID of the domain unit where the connection is created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`

 ** [environmentId](#API_CreateConnection_ResponseSyntax) **   <a name="datazone-CreateConnection-response-environmentId"></a>
The ID of the environment where the connection is created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [name](#API_CreateConnection_ResponseSyntax) **   <a name="datazone-CreateConnection-response-name"></a>
The connection name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.

 ** [physicalEndpoints](#API_CreateConnection_ResponseSyntax) **   <a name="datazone-CreateConnection-response-physicalEndpoints"></a>
The physical endpoints of the connection.
Type: Array of [PhysicalEndpoint](API_PhysicalEndpoint.md) objects

 ** [projectId](#API_CreateConnection_ResponseSyntax) **   <a name="datazone-CreateConnection-response-projectId"></a>
The ID of the project where the connection is created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [props](#API_CreateConnection_ResponseSyntax) **   <a name="datazone-CreateConnection-response-props"></a>
The connection props.
Type: [ConnectionPropertiesOutput](API_ConnectionPropertiesOutput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [scope](#API_CreateConnection_ResponseSyntax) **   <a name="datazone-CreateConnection-response-scope"></a>
The scope of the connection.
Type: String
Valid Values: `DOMAIN | PROJECT`

 ** [type](#API_CreateConnection_ResponseSyntax) **   <a name="datazone-CreateConnection-response-type"></a>
The connection type.
Type: String
Valid Values: `ATHENA | BIGQUERY | DATABRICKS | DOCUMENTDB | DYNAMODB | HYPERPOD | IAM | MYSQL | OPENSEARCH | ORACLE | POSTGRESQL | REDSHIFT | S3 | SAPHANA | SNOWFLAKE | SPARK | SQLSERVER | TERADATA | VERTICA | WORKFLOWS_MWAA | AMAZON_Q | MLFLOW | VPC | GIT`

## Errors
<a name="API_CreateConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict while performing this action.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request has exceeded the specified service quota.
HTTP Status Code: 402

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
<a name="API_CreateConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CreateConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CreateConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CreateConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CreateConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CreateConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CreateConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CreateConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CreateConnection)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CreateConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CreateConnection)
