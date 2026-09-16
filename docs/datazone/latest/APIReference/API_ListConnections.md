---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListConnections.html
---

# ListConnections
<a name="API_ListConnections"></a>

Lists connections. In Amazon DataZone, a connection enables you to connect your resources (domains, projects, and environments) to external resources and services.

## Request Syntax
<a name="API_ListConnections_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/connections?environmentIdentifier={{environmentIdentifier}}&maxResults={{maxResults}}&name={{name}}&nextToken={{nextToken}}&projectIdentifier={{projectIdentifier}}&scope={{scope}}&sortBy={{sortBy}}&sortOrder={{sortOrder}}&type={{type}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListConnections_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_ListConnections_RequestSyntax) **   <a name="datazone-ListConnections-request-uri-domainIdentifier"></a>
The ID of the domain where you want to list connections.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [environmentIdentifier](#API_ListConnections_RequestSyntax) **   <a name="datazone-ListConnections-request-uri-environmentIdentifier"></a>
The ID of the environment where you want to list connections.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [maxResults](#API_ListConnections_RequestSyntax) **   <a name="datazone-ListConnections-request-uri-maxResults"></a>
The maximum number of connections to return in a single call to ListConnections. When the number of connections to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListConnections to list the next set of connections.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [name](#API_ListConnections_RequestSyntax) **   <a name="datazone-ListConnections-request-uri-name"></a>
The name of the connection.
Length Constraints: Minimum length of 0. Maximum length of 64.

 ** [nextToken](#API_ListConnections_RequestSyntax) **   <a name="datazone-ListConnections-request-uri-nextToken"></a>
When the number of connections is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of connections, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListConnections to list the next set of connections.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [projectIdentifier](#API_ListConnections_RequestSyntax) **   <a name="datazone-ListConnections-request-uri-projectIdentifier"></a>
The ID of the project where you want to list connections.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [scope](#API_ListConnections_RequestSyntax) **   <a name="datazone-ListConnections-request-uri-scope"></a>
The scope of the connection.
Valid Values: `DOMAIN | PROJECT`

 ** [sortBy](#API_ListConnections_RequestSyntax) **   <a name="datazone-ListConnections-request-uri-sortBy"></a>
Specifies how you want to sort the listed connections.
Valid Values: `NAME`

 ** [sortOrder](#API_ListConnections_RequestSyntax) **   <a name="datazone-ListConnections-request-uri-sortOrder"></a>
Specifies the sort order for the listed connections.
Valid Values: `ASCENDING | DESCENDING`

 ** [type](#API_ListConnections_RequestSyntax) **   <a name="datazone-ListConnections-request-uri-type"></a>
The type of connection.
Valid Values: `ATHENA | BIGQUERY | DATABRICKS | DOCUMENTDB | DYNAMODB | HYPERPOD | IAM | MYSQL | OPENSEARCH | ORACLE | POSTGRESQL | REDSHIFT | S3 | SAPHANA | SNOWFLAKE | SPARK | SQLSERVER | TERADATA | VERTICA | WORKFLOWS_MWAA | AMAZON_Q | MLFLOW | VPC | GIT`

## Request Body
<a name="API_ListConnections_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListConnections_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
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
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListConnections_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListConnections_ResponseSyntax) **   <a name="datazone-ListConnections-response-items"></a>
The results of the ListConnections action.
Type: Array of [ConnectionSummary](API_ConnectionSummary.md) objects

 ** [nextToken](#API_ListConnections_ResponseSyntax) **   <a name="datazone-ListConnections-response-nextToken"></a>
When the number of connections is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of connections, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListConnections to list the next set of connections.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListConnections_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

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
<a name="API_ListConnections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListConnections)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListConnections)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListConnections)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListConnections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListConnections)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListConnections)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListConnections)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListConnections)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListConnections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListConnections)
