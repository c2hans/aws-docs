---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ListManagedEndpoints.html
---

# ListManagedEndpoints
<a name="API_ListManagedEndpoints"></a>

Lists managed endpoints based on a set of parameters. A managed endpoint is a gateway that connects Amazon EMR Studio to Amazon EMR on EKS so that Amazon EMR Studio can communicate with your virtual cluster.

## Request Syntax
<a name="API_ListManagedEndpoints_RequestSyntax"></a>

```
GET /virtualclusters/{{virtualClusterId}}/endpoints?createdAfter={{createdAfter}}&createdBefore={{createdBefore}}&maxResults={{maxResults}}&nextToken={{nextToken}}&states={{states}}&types={{types}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListManagedEndpoints_RequestParameters"></a>

The request uses the following URI parameters.

 ** [createdAfter](#API_ListManagedEndpoints_RequestSyntax) **   <a name="emroneks-ListManagedEndpoints-request-uri-createdAfter"></a>
 The date and time after which the endpoints are created.

 ** [createdBefore](#API_ListManagedEndpoints_RequestSyntax) **   <a name="emroneks-ListManagedEndpoints-request-uri-createdBefore"></a>
The date and time before which the endpoints are created.

 ** [maxResults](#API_ListManagedEndpoints_RequestSyntax) **   <a name="emroneks-ListManagedEndpoints-request-uri-maxResults"></a>
The maximum number of managed endpoints that can be listed.

 ** [nextToken](#API_ListManagedEndpoints_RequestSyntax) **   <a name="emroneks-ListManagedEndpoints-request-uri-nextToken"></a>
 The token for the next set of managed endpoints to return.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`

 ** [states](#API_ListManagedEndpoints_RequestSyntax) **   <a name="emroneks-ListManagedEndpoints-request-uri-states"></a>
The states of the managed endpoints.
Array Members: Maximum number of 10 items.
Valid Values: `CREATING | ACTIVE | TERMINATING | TERMINATED | TERMINATED_WITH_ERRORS`

 ** [types](#API_ListManagedEndpoints_RequestSyntax) **   <a name="emroneks-ListManagedEndpoints-request-uri-types"></a>
The types of the managed endpoints.
Array Members: Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*\S.*`

 ** [virtualClusterId](#API_ListManagedEndpoints_RequestSyntax) **   <a name="emroneks-ListManagedEndpoints-request-uri-virtualClusterId"></a>
The ID of the virtual cluster.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

## Request Body
<a name="API_ListManagedEndpoints_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListManagedEndpoints_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "endpoints": [
      {
         "arn": "string",
         "authProxyUrl": "string",
         "certificateArn": "string",
         "certificateAuthority": {
            "certificateArn": "string",
            "certificateData": "string"
         },
         "configurationOverrides": {
            "applicationConfiguration": [
               {
                  "classification": "string",
                  "configurations": [
                     "Configuration"
                  ],
                  "properties": {
                     "string" : "string"
                  }
               }
            ],
            "monitoringConfiguration": {
               "cloudWatchMonitoringConfiguration": {
                  "logGroupName": "string",
                  "logStreamNamePrefix": "string"
               },
               "containerLogRotationConfiguration": {
                  "maxFilesToKeep": number,
                  "rotationSize": "string"
               },
               "managedLogs": {
                  "allowAWSToRetainLogs": "string",
                  "encryptionKeyArn": "string"
               },
               "persistentAppUI": "string",
               "s3MonitoringConfiguration": {
                  "encryptionKeyArn": "string",
                  "logUri": "string"
               }
            }
         },
         "createdAt": "string",
         "executionRoleArn": "string",
         "failureReason": "string",
         "id": "string",
         "name": "string",
         "releaseLabel": "string",
         "securityGroup": "string",
         "serverUrl": "string",
         "state": "string",
         "stateDetails": "string",
         "subnetIds": [ "string" ],
         "tags": {
            "string" : "string"
         },
         "type": "string",
         "virtualClusterId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListManagedEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [endpoints](#API_ListManagedEndpoints_ResponseSyntax) **   <a name="emroneks-ListManagedEndpoints-response-endpoints"></a>
The managed endpoints to be listed.
Type: Array of [Endpoint](API_Endpoint.md) objects

 ** [nextToken](#API_ListManagedEndpoints_ResponseSyntax) **   <a name="emroneks-ListManagedEndpoints-response-nextToken"></a>
 The token for the next set of endpoints to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`

## Errors
<a name="API_ListManagedEndpoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
This is an internal server exception.
HTTP Status Code: 500

 ** ValidationException **
There are invalid parameters in the client request.
HTTP Status Code: 400

## See Also
<a name="API_ListManagedEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-containers-2020-10-01/ListManagedEndpoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-containers-2020-10-01/ListManagedEndpoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/ListManagedEndpoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-containers-2020-10-01/ListManagedEndpoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/ListManagedEndpoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-containers-2020-10-01/ListManagedEndpoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-containers-2020-10-01/ListManagedEndpoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-containers-2020-10-01/ListManagedEndpoints)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/emr-containers-2020-10-01/ListManagedEndpoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/ListManagedEndpoints)
