---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetConnections.html
---

# GetConnections
<a name="API_GetConnections"></a>

Retrieves a list of connection definitions from the Data Catalog.

## Request Syntax
<a name="API_GetConnections_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "Filter": {
      "ConnectionSchemaVersion": {{number}},
      "ConnectionType": "{{string}}",
      "MatchCriteria": [ "{{string}}" ]
   },
   "HidePassword": {{boolean}},
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetConnections_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_GetConnections_RequestSyntax) **   <a name="Glue-GetConnections-request-CatalogId"></a>
The ID of the Data Catalog in which the connections reside. If none is provided, the AWS account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Filter](#API_GetConnections_RequestSyntax) **   <a name="Glue-GetConnections-request-Filter"></a>
A filter that controls which connections are returned.
Type: [GetConnectionsFilter](API_GetConnectionsFilter.md) object
Required: No

 ** [HidePassword](#API_GetConnections_RequestSyntax) **   <a name="Glue-GetConnections-request-HidePassword"></a>
Allows you to retrieve the connection metadata without returning the password. For instance, the AWS Glue console uses this flag to retrieve the connection, and does not display the password. Set this parameter when the caller might not have permission to use the AWS KMS key to decrypt the password, but it does have permission to access the rest of the connection properties.
Type: Boolean
Required: No

 ** [MaxResults](#API_GetConnections_RequestSyntax) **   <a name="Glue-GetConnections-request-MaxResults"></a>
The maximum number of connections to return in one response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_GetConnections_RequestSyntax) **   <a name="Glue-GetConnections-request-NextToken"></a>
A continuation token, if this is a continuation call.
Type: String
Required: No

## Response Syntax
<a name="API_GetConnections_ResponseSyntax"></a>

```
{
   "ConnectionList": [
      {
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
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetConnections_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectionList](#API_GetConnections_ResponseSyntax) **   <a name="Glue-GetConnections-response-ConnectionList"></a>
A list of requested connection definitions.
Type: Array of [Connection](API_Connection.md) objects

 ** [NextToken](#API_GetConnections_ResponseSyntax) **   <a name="Glue-GetConnections-response-NextToken"></a>
A continuation token, if the list of connections returned does not include the last of the filtered connections.
Type: String

## Errors
<a name="API_GetConnections_Errors"></a>

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
<a name="API_GetConnections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetConnections)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetConnections)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetConnections)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetConnections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetConnections)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetConnections)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetConnections)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetConnections)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetConnections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetConnections)
