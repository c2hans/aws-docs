---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDataSource.html
---

# UpdateDataSource
<a name="API_UpdateDataSource"></a>

Updates a data source.

## Request Syntax
<a name="API_UpdateDataSource_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/data-sources/{{DataSourceId}} HTTP/1.1
Content-type: application/json

{
   "Credentials": {
      "CopySourceArn": "{{string}}",
      "CredentialPair": {
         "AlternateDataSourceParameters": [
            {
               "AmazonElasticsearchParameters": {
                  "Domain": "{{string}}"
               },
               "AmazonOpenSearchParameters": {
                  "Domain": "{{string}}"
               },
               "AthenaParameters": {
                  "ConsumerAccountRoleArn": "{{string}}",
                  "IdentityCenterConfiguration": {
                     "EnableIdentityPropagation": {{boolean}}
                  },
                  "RoleArn": "{{string}}",
                  "WorkGroup": "{{string}}"
               },
               "AuroraParameters": {
                  "Database": "{{string}}",
                  "Host": "{{string}}",
                  "Port": {{number}}
               },
               "AuroraPostgreSqlParameters": {
                  "Database": "{{string}}",
                  "Host": "{{string}}",
                  "Port": {{number}}
               },
               "AwsIotAnalyticsParameters": {
                  "DataSetName": "{{string}}"
               },
               "BigQueryParameters": {
                  "DataSetRegion": "{{string}}",
                  "ProjectId": "{{string}}"
               },
               "ConfluenceParameters": {
                  "ConfluenceUrl": "{{string}}"
               },
               "CustomConnectionParameters": {
                  "ConnectionType": "{{string}}"
               },
               "DatabricksParameters": {
                  "Host": "{{string}}",
                  "Port": {{number}},
                  "SqlEndpointPath": "{{string}}"
               },
               "ExasolParameters": {
                  "Host": "{{string}}",
                  "Port": {{number}}
               },
               "FMKBParameters": {
                  "KnowledgeBaseArn": "{{string}}",
                  "LinkedDataSourceIds": [ "{{string}}" ]
               },
               "GoogleDriveParameters": {
                  "AuthType": "{{string}}"
               },
               "ImpalaParameters": {
                  "Database": "{{string}}",
                  "Host": "{{string}}",
                  "Port": {{number}},
                  "SqlEndpointPath": "{{string}}"
               },
               "JiraParameters": {
                  "SiteBaseUrl": "{{string}}"
               },
               "MariaDbParameters": {
                  "Database": "{{string}}",
                  "Host": "{{string}}",
                  "Port": {{number}}
               },
               "MySqlParameters": {
                  "Database": "{{string}}",
                  "Host": "{{string}}",
                  "Port": {{number}}
               },
               "OneDriveParameters": {
                  "AuthType": "{{string}}",
                  "ClientId": "{{string}}",
                  "TenantId": "{{string}}"
               },
               "OracleParameters": {
                  "Database": "{{string}}",
                  "Host": "{{string}}",
                  "Port": {{number}},
                  "UseServiceName": {{boolean}}
               },
               "PostgreSqlParameters": {
                  "Database": "{{string}}",
                  "Host": "{{string}}",
                  "Port": {{number}}
               },
               "PrestoParameters": {
                  "Catalog": "{{string}}",
                  "Host": "{{string}}",
                  "Port": {{number}}
               },
               "QBusinessParameters": {
                  "ApplicationArn": "{{string}}"
               },
               "RdsParameters": {
                  "Database": "{{string}}",
                  "InstanceId": "{{string}}"
               },
               "RedshiftParameters": {
                  "ClusterId": "{{string}}",
                  "Database": "{{string}}",
                  "Host": "{{string}}",
                  "IAMParameters": {
                     "AutoCreateDatabaseUser": {{boolean}},
                     "DatabaseGroups": [ "{{string}}" ],
                     "DatabaseUser": "{{string}}",
                     "RoleArn": "{{string}}"
                  },
                  "IdentityCenterConfiguration": {
                     "EnableIdentityPropagation": {{boolean}}
                  },
                  "Port": {{number}}
               },
               "S3KnowledgeBaseParameters": {
                  "BucketUrl": "{{string}}",
                  "MetadataFilesLocation": "{{string}}",
                  "RoleArn": "{{string}}"
               },
               "S3Parameters": {
                  "ManifestFileLocation": {
                     "Bucket": "{{string}}",
                     "Key": "{{string}}"
                  },
                  "RoleArn": "{{string}}"
               },
               "S3TablesParameters": {
                  "TableBucketArn": "{{string}}"
               },
               "ServiceNowParameters": {
                  "SiteBaseUrl": "{{string}}"
               },
               "SharePointParameters": {
                  "AuthType": "{{string}}",
                  "ClientId": "{{string}}",
                  "SharePointDomain": "{{string}}",
                  "TenantId": "{{string}}"
               },
               "SnowflakeParameters": {
                  "AuthenticationType": "{{string}}",
                  "Database": "{{string}}",
                  "DatabaseAccessControlRole": "{{string}}",
                  "Host": "{{string}}",
                  "OAuthParameters": {
                     "IdentityProviderCACertificatesBundleS3Uri": "{{string}}",
                     "IdentityProviderResourceUri": "{{string}}",
                     "IdentityProviderVpcConnectionProperties": {
                        "VpcConnectionArn": "{{string}}"
                     },
                     "OAuthScope": "{{string}}",
                     "TokenProviderUrl": "{{string}}"
                  },
                  "Warehouse": "{{string}}"
               },
               "SparkParameters": {
                  "Host": "{{string}}",
                  "Port": {{number}}
               },
               "SqlServerParameters": {
                  "Database": "{{string}}",
                  "Host": "{{string}}",
                  "Port": {{number}}
               },
               "StarburstParameters": {
                  "AuthenticationType": "{{string}}",
                  "Catalog": "{{string}}",
                  "DatabaseAccessControlRole": "{{string}}",
                  "Host": "{{string}}",
                  "OAuthParameters": {
                     "IdentityProviderCACertificatesBundleS3Uri": "{{string}}",
                     "IdentityProviderResourceUri": "{{string}}",
                     "IdentityProviderVpcConnectionProperties": {
                        "VpcConnectionArn": "{{string}}"
                     },
                     "OAuthScope": "{{string}}",
                     "TokenProviderUrl": "{{string}}"
                  },
                  "Port": {{number}},
                  "ProductType": "{{string}}"
               },
               "TeradataParameters": {
                  "Database": "{{string}}",
                  "Host": "{{string}}",
                  "Port": {{number}}
               },
               "TrinoParameters": {
                  "Catalog": "{{string}}",
                  "Host": "{{string}}",
                  "Port": {{number}}
               },
               "TwitterParameters": {
                  "MaxRows": {{number}},
                  "Query": "{{string}}"
               },
               "WebCrawlerParameters": {
                  "LoginPageUrl": "{{string}}",
                  "PasswordButtonXpath": "{{string}}",
                  "PasswordFieldXpath": "{{string}}",
                  "UsernameButtonXpath": "{{string}}",
                  "UsernameFieldXpath": "{{string}}",
                  "WebCrawlerAuthType": "{{string}}",
                  "WebProxyHostName": "{{string}}",
                  "WebProxyPortNumber": {{number}}
               }
            }
         ],
         "Password": "{{string}}",
         "Username": "{{string}}"
      },
      "KeyPairCredentials": {
         "KeyPairUsername": "{{string}}",
         "PrivateKey": "{{string}}",
         "PrivateKeyPassphrase": "{{string}}"
      },
      "OAuthClientCredentials": {
         "ClientId": "{{string}}",
         "ClientSecret": "{{string}}",
         "Username": "{{string}}"
      },
      "SecretArn": "{{string}}",
      "WebProxyCredentials": {
         "WebProxyPassword": "{{string}}",
         "WebProxyUsername": "{{string}}"
      }
   },
   "DataSourceParameters": {
      "AmazonElasticsearchParameters": {
         "Domain": "{{string}}"
      },
      "AmazonOpenSearchParameters": {
         "Domain": "{{string}}"
      },
      "AthenaParameters": {
         "ConsumerAccountRoleArn": "{{string}}",
         "IdentityCenterConfiguration": {
            "EnableIdentityPropagation": {{boolean}}
         },
         "RoleArn": "{{string}}",
         "WorkGroup": "{{string}}"
      },
      "AuroraParameters": {
         "Database": "{{string}}",
         "Host": "{{string}}",
         "Port": {{number}}
      },
      "AuroraPostgreSqlParameters": {
         "Database": "{{string}}",
         "Host": "{{string}}",
         "Port": {{number}}
      },
      "AwsIotAnalyticsParameters": {
         "DataSetName": "{{string}}"
      },
      "BigQueryParameters": {
         "DataSetRegion": "{{string}}",
         "ProjectId": "{{string}}"
      },
      "ConfluenceParameters": {
         "ConfluenceUrl": "{{string}}"
      },
      "CustomConnectionParameters": {
         "ConnectionType": "{{string}}"
      },
      "DatabricksParameters": {
         "Host": "{{string}}",
         "Port": {{number}},
         "SqlEndpointPath": "{{string}}"
      },
      "ExasolParameters": {
         "Host": "{{string}}",
         "Port": {{number}}
      },
      "FMKBParameters": {
         "KnowledgeBaseArn": "{{string}}",
         "LinkedDataSourceIds": [ "{{string}}" ]
      },
      "GoogleDriveParameters": {
         "AuthType": "{{string}}"
      },
      "ImpalaParameters": {
         "Database": "{{string}}",
         "Host": "{{string}}",
         "Port": {{number}},
         "SqlEndpointPath": "{{string}}"
      },
      "JiraParameters": {
         "SiteBaseUrl": "{{string}}"
      },
      "MariaDbParameters": {
         "Database": "{{string}}",
         "Host": "{{string}}",
         "Port": {{number}}
      },
      "MySqlParameters": {
         "Database": "{{string}}",
         "Host": "{{string}}",
         "Port": {{number}}
      },
      "OneDriveParameters": {
         "AuthType": "{{string}}",
         "ClientId": "{{string}}",
         "TenantId": "{{string}}"
      },
      "OracleParameters": {
         "Database": "{{string}}",
         "Host": "{{string}}",
         "Port": {{number}},
         "UseServiceName": {{boolean}}
      },
      "PostgreSqlParameters": {
         "Database": "{{string}}",
         "Host": "{{string}}",
         "Port": {{number}}
      },
      "PrestoParameters": {
         "Catalog": "{{string}}",
         "Host": "{{string}}",
         "Port": {{number}}
      },
      "QBusinessParameters": {
         "ApplicationArn": "{{string}}"
      },
      "RdsParameters": {
         "Database": "{{string}}",
         "InstanceId": "{{string}}"
      },
      "RedshiftParameters": {
         "ClusterId": "{{string}}",
         "Database": "{{string}}",
         "Host": "{{string}}",
         "IAMParameters": {
            "AutoCreateDatabaseUser": {{boolean}},
            "DatabaseGroups": [ "{{string}}" ],
            "DatabaseUser": "{{string}}",
            "RoleArn": "{{string}}"
         },
         "IdentityCenterConfiguration": {
            "EnableIdentityPropagation": {{boolean}}
         },
         "Port": {{number}}
      },
      "S3KnowledgeBaseParameters": {
         "BucketUrl": "{{string}}",
         "MetadataFilesLocation": "{{string}}",
         "RoleArn": "{{string}}"
      },
      "S3Parameters": {
         "ManifestFileLocation": {
            "Bucket": "{{string}}",
            "Key": "{{string}}"
         },
         "RoleArn": "{{string}}"
      },
      "S3TablesParameters": {
         "TableBucketArn": "{{string}}"
      },
      "ServiceNowParameters": {
         "SiteBaseUrl": "{{string}}"
      },
      "SharePointParameters": {
         "AuthType": "{{string}}",
         "ClientId": "{{string}}",
         "SharePointDomain": "{{string}}",
         "TenantId": "{{string}}"
      },
      "SnowflakeParameters": {
         "AuthenticationType": "{{string}}",
         "Database": "{{string}}",
         "DatabaseAccessControlRole": "{{string}}",
         "Host": "{{string}}",
         "OAuthParameters": {
            "IdentityProviderCACertificatesBundleS3Uri": "{{string}}",
            "IdentityProviderResourceUri": "{{string}}",
            "IdentityProviderVpcConnectionProperties": {
               "VpcConnectionArn": "{{string}}"
            },
            "OAuthScope": "{{string}}",
            "TokenProviderUrl": "{{string}}"
         },
         "Warehouse": "{{string}}"
      },
      "SparkParameters": {
         "Host": "{{string}}",
         "Port": {{number}}
      },
      "SqlServerParameters": {
         "Database": "{{string}}",
         "Host": "{{string}}",
         "Port": {{number}}
      },
      "StarburstParameters": {
         "AuthenticationType": "{{string}}",
         "Catalog": "{{string}}",
         "DatabaseAccessControlRole": "{{string}}",
         "Host": "{{string}}",
         "OAuthParameters": {
            "IdentityProviderCACertificatesBundleS3Uri": "{{string}}",
            "IdentityProviderResourceUri": "{{string}}",
            "IdentityProviderVpcConnectionProperties": {
               "VpcConnectionArn": "{{string}}"
            },
            "OAuthScope": "{{string}}",
            "TokenProviderUrl": "{{string}}"
         },
         "Port": {{number}},
         "ProductType": "{{string}}"
      },
      "TeradataParameters": {
         "Database": "{{string}}",
         "Host": "{{string}}",
         "Port": {{number}}
      },
      "TrinoParameters": {
         "Catalog": "{{string}}",
         "Host": "{{string}}",
         "Port": {{number}}
      },
      "TwitterParameters": {
         "MaxRows": {{number}},
         "Query": "{{string}}"
      },
      "WebCrawlerParameters": {
         "LoginPageUrl": "{{string}}",
         "PasswordButtonXpath": "{{string}}",
         "PasswordFieldXpath": "{{string}}",
         "UsernameButtonXpath": "{{string}}",
         "UsernameFieldXpath": "{{string}}",
         "WebCrawlerAuthType": "{{string}}",
         "WebProxyHostName": "{{string}}",
         "WebProxyPortNumber": {{number}}
      }
   },
   "Name": "{{string}}",
   "SslProperties": {
      "DisableSsl": {{boolean}}
   },
   "VpcConnectionProperties": {
      "VpcConnectionArn": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateDataSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateDataSource_RequestSyntax) **   <a name="QS-UpdateDataSource-request-uri-AwsAccountId"></a>
The AWS account ID.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [DataSourceId](#API_UpdateDataSource_RequestSyntax) **   <a name="QS-UpdateDataSource-request-uri-DataSourceId"></a>
The ID of the data source. This ID is unique per AWS Region for each AWS account.
Required: Yes

## Request Body
<a name="API_UpdateDataSource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_UpdateDataSource_RequestSyntax) **   <a name="QS-UpdateDataSource-request-Name"></a>
A display name for the data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [Credentials](#API_UpdateDataSource_RequestSyntax) **   <a name="QS-UpdateDataSource-request-Credentials"></a>
The credentials that Amazon Quick Sight that uses to connect to your underlying source. Currently, only credentials based on user name and password are supported.
Type: [DataSourceCredentials](API_DataSourceCredentials.md) object
Required: No

 ** [DataSourceParameters](#API_UpdateDataSource_RequestSyntax) **   <a name="QS-UpdateDataSource-request-DataSourceParameters"></a>
The parameters that Amazon Quick Sight uses to connect to your underlying source.
Type: [DataSourceParameters](API_DataSourceParameters.md) object
Required: No

 ** [SslProperties](#API_UpdateDataSource_RequestSyntax) **   <a name="QS-UpdateDataSource-request-SslProperties"></a>
Secure Socket Layer (SSL) properties that apply when Amazon Quick Sight connects to your underlying source.
Type: [SslProperties](API_SslProperties.md) object
Required: No

 ** [VpcConnectionProperties](#API_UpdateDataSource_RequestSyntax) **   <a name="QS-UpdateDataSource-request-VpcConnectionProperties"></a>
Use this parameter only when you want Amazon Quick Sight to use a VPC connection when connecting to your underlying source.
Type: [VpcConnectionProperties](API_VpcConnectionProperties.md) object
Required: No

## Response Syntax
<a name="API_UpdateDataSource_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "DataSourceId": "string",
   "RequestId": "string",
   "UpdateStatus": "string"
}
```

## Response Elements
<a name="API_UpdateDataSource_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateDataSource_ResponseSyntax) **   <a name="QS-UpdateDataSource-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateDataSource_ResponseSyntax) **   <a name="QS-UpdateDataSource-response-Arn"></a>
The Amazon Resource Name (ARN) of the data source.
Type: String

 ** [DataSourceId](#API_UpdateDataSource_ResponseSyntax) **   <a name="QS-UpdateDataSource-response-DataSourceId"></a>
The ID of the data source. This ID is unique per AWS Region for each AWS account.
Type: String

 ** [RequestId](#API_UpdateDataSource_ResponseSyntax) **   <a name="QS-UpdateDataSource-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [UpdateStatus](#API_UpdateDataSource_ResponseSyntax) **   <a name="QS-UpdateDataSource-response-UpdateStatus"></a>
The update status of the data source's last update.
Type: String
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETED`

## Errors
<a name="API_UpdateDataSource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 409

 ** CustomerManagedKeyUnavailableException **
The customer managed key that is registered to your Amazon Quick Sight account is unavailable.
 ** RequestId **
The AWS request ID for this operation.
HTTP Status Code: 400

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## Examples
<a name="API_UpdateDataSource_Examples"></a>

### Example
<a name="API_UpdateDataSource_Example_1"></a>

This example illustrates one usage of UpdateDataSource.

#### Sample Request
<a name="API_UpdateDataSource_Example_1_Request"></a>

```
PUT /accounts/{AwsAccountId}/data-sources/{DataSourceId} HTTP/1.1
Content-type: application/json
```

## See Also
<a name="API_UpdateDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateDataSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateDataSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateDataSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateDataSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateDataSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateDataSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateDataSource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateDataSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
