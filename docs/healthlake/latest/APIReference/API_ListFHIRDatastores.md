---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ListFHIRDatastores.html
---

# ListFHIRDatastores
<a name="API_ListFHIRDatastores"></a>

List all FHIR-enabled data stores in a user’s account, regardless of data store status.

## Request Syntax
<a name="API_ListFHIRDatastores_RequestSyntax"></a>

```
{
   "Filter": {
      "CreatedAfter": {{number}},
      "CreatedBefore": {{number}},
      "DatastoreName": "{{string}}",
      "DatastoreStatus": "{{string}}"
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListFHIRDatastores_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filter](#API_ListFHIRDatastores_RequestSyntax) **   <a name="HealthLake-ListFHIRDatastores-request-Filter"></a>
List all filters associated with a FHIR data store request.
Type: [DatastoreFilter](API_DatastoreFilter.md) object
Required: No

 ** [MaxResults](#API_ListFHIRDatastores_RequestSyntax) **   <a name="HealthLake-ListFHIRDatastores-request-MaxResults"></a>
The maximum number of data stores returned on a page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [NextToken](#API_ListFHIRDatastores_RequestSyntax) **   <a name="HealthLake-ListFHIRDatastores-request-NextToken"></a>
The token used to retrieve the next page of data stores when results are paginated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `\p{ASCII}{0,8192}`
Required: No

## Response Syntax
<a name="API_ListFHIRDatastores_ResponseSyntax"></a>

```
{
   "DatastorePropertiesList": [
      {
         "AnalyticsConfiguration": {
            "Status": "string"
         },
         "CreatedAt": number,
         "DatastoreArn": "string",
         "DatastoreEndpoint": "string",
         "DatastoreId": "string",
         "DatastoreName": "string",
         "DatastoreStatus": "string",
         "DatastoreTypeVersion": "string",
         "ErrorCause": {
            "ErrorCategory": "string",
            "ErrorMessage": "string"
         },
         "IdentityProviderConfiguration": {
            "AuthorizationStrategy": "string",
            "FineGrainedAuthorizationEnabled": boolean,
            "IdpLambdaArn": "string",
            "Metadata": "string"
         },
         "NlpConfiguration": {
            "Status": "string"
         },
         "PreloadDataConfig": {
            "PreloadDataType": "string"
         },
         "ProfileConfiguration": {
            "DefaultProfiles": [ "string" ]
         },
         "SseConfiguration": {
            "KmsEncryptionConfig": {
               "CmkType": "string",
               "KmsKeyId": "string"
            }
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListFHIRDatastores_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DatastorePropertiesList](#API_ListFHIRDatastores_ResponseSyntax) **   <a name="HealthLake-ListFHIRDatastores-response-DatastorePropertiesList"></a>
The properties associated with all listed data stores.
Type: Array of [DatastoreProperties](API_DatastoreProperties.md) objects

 ** [NextToken](#API_ListFHIRDatastores_ResponseSyntax) **   <a name="HealthLake-ListFHIRDatastores-response-NextToken"></a>
The pagination token used to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `\p{ASCII}{0,8192}`

## Errors
<a name="API_ListFHIRDatastores_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An unknown internal error occurred in the service.
HTTP Status Code: 500

 ** ThrottlingException **
The user has exceeded their maximum number of allowed calls to the given API.
HTTP Status Code: 400

 ** ValidationException **
The user input parameter was invalid.
HTTP Status Code: 400

## See Also
<a name="API_ListFHIRDatastores_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/healthlake-2017-07-01/ListFHIRDatastores)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/healthlake-2017-07-01/ListFHIRDatastores)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/ListFHIRDatastores)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/healthlake-2017-07-01/ListFHIRDatastores)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/ListFHIRDatastores)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/healthlake-2017-07-01/ListFHIRDatastores)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/healthlake-2017-07-01/ListFHIRDatastores)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/healthlake-2017-07-01/ListFHIRDatastores)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/ListFHIRDatastores)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/ListFHIRDatastores)
