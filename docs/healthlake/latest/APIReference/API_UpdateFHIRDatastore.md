---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_UpdateFHIRDatastore.html
---

# UpdateFHIRDatastore
<a name="API_UpdateFHIRDatastore"></a>

Update the properties of a FHIR-enabled data store.

## Request Syntax
<a name="API_UpdateFHIRDatastore_RequestSyntax"></a>

```
{
   "AnalyticsConfiguration": {
      "Status": "{{string}}"
   },
   "DatastoreId": "{{string}}",
   "DatastoreName": "{{string}}",
   "IdentityProviderConfiguration": {
      "AuthorizationStrategy": "{{string}}",
      "FineGrainedAuthorizationEnabled": {{boolean}},
      "IdpLambdaArn": "{{string}}",
      "Metadata": "{{string}}"
   },
   "NlpConfiguration": {
      "Status": "{{string}}"
   },
   "ProfileConfiguration": {
      "DefaultProfiles": [ "{{string}}" ]
   }
}
```

## Request Parameters
<a name="API_UpdateFHIRDatastore_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AnalyticsConfiguration](#API_UpdateFHIRDatastore_RequestSyntax) **   <a name="HealthLake-UpdateFHIRDatastore-request-AnalyticsConfiguration"></a>
The analytics configuration for the data store.
Type: [AnalyticsConfiguration](API_AnalyticsConfiguration.md) object
Required: No

 ** [DatastoreId](#API_UpdateFHIRDatastore_RequestSyntax) **   <a name="HealthLake-UpdateFHIRDatastore-request-DatastoreId"></a>
The data store identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`
Required: Yes

 ** [DatastoreName](#API_UpdateFHIRDatastore_RequestSyntax) **   <a name="HealthLake-UpdateFHIRDatastore-request-DatastoreName"></a>
The data store name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`
Required: No

 ** [IdentityProviderConfiguration](#API_UpdateFHIRDatastore_RequestSyntax) **   <a name="HealthLake-UpdateFHIRDatastore-request-IdentityProviderConfiguration"></a>
The identity provider configuration for the data store.
Type: [IdentityProviderConfiguration](API_IdentityProviderConfiguration.md) object
Required: No

 ** [NlpConfiguration](#API_UpdateFHIRDatastore_RequestSyntax) **   <a name="HealthLake-UpdateFHIRDatastore-request-NlpConfiguration"></a>
The natural language processing (NLP) configuration for the data store.
Type: [NlpConfiguration](API_NlpConfiguration.md) object
Required: No

 ** [ProfileConfiguration](#API_UpdateFHIRDatastore_RequestSyntax) **   <a name="HealthLake-UpdateFHIRDatastore-request-ProfileConfiguration"></a>
The profile configuration for the data store.
Type: [ProfileConfiguration](API_ProfileConfiguration.md) object
Required: No

## Response Syntax
<a name="API_UpdateFHIRDatastore_ResponseSyntax"></a>

```
{
   "DatastoreProperties": {
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
}
```

## Response Elements
<a name="API_UpdateFHIRDatastore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DatastoreProperties](#API_UpdateFHIRDatastore_ResponseSyntax) **   <a name="HealthLake-UpdateFHIRDatastore-response-DatastoreProperties"></a>
The data store properties.
Type: [DatastoreProperties](API_DatastoreProperties.md) object

## Errors
<a name="API_UpdateFHIRDatastore_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied. Your account is not authorized to perform this operation.
HTTP Status Code: 400

 ** ConflictException **
The data store is in a transition state and the user requested action cannot be performed.
HTTP Status Code: 400

 ** InternalServerException **
An unknown internal error occurred in the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested data store was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The user has exceeded their maximum number of allowed calls to the given API.
HTTP Status Code: 400

 ** ValidationException **
The user input parameter was invalid.
HTTP Status Code: 400

## See Also
<a name="API_UpdateFHIRDatastore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/healthlake-2017-07-01/UpdateFHIRDatastore)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/healthlake-2017-07-01/UpdateFHIRDatastore)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/UpdateFHIRDatastore)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/healthlake-2017-07-01/UpdateFHIRDatastore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/UpdateFHIRDatastore)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/healthlake-2017-07-01/UpdateFHIRDatastore)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/healthlake-2017-07-01/UpdateFHIRDatastore)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/healthlake-2017-07-01/UpdateFHIRDatastore)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/UpdateFHIRDatastore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/UpdateFHIRDatastore)
