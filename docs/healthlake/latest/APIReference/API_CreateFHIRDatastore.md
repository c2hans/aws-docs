---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_CreateFHIRDatastore.html
---

# CreateFHIRDatastore
<a name="API_CreateFHIRDatastore"></a>

Create a FHIR-enabled data store.

## Request Syntax
<a name="API_CreateFHIRDatastore_RequestSyntax"></a>

```
{
   "AnalyticsConfiguration": {
      "Status": "{{string}}"
   },
   "ClientToken": "{{string}}",
   "DatastoreName": "{{string}}",
   "DatastoreTypeVersion": "{{string}}",
   "IdentityProviderConfiguration": {
      "AuthorizationStrategy": "{{string}}",
      "FineGrainedAuthorizationEnabled": {{boolean}},
      "IdpLambdaArn": "{{string}}",
      "Metadata": "{{string}}"
   },
   "NlpConfiguration": {
      "Status": "{{string}}"
   },
   "PreloadDataConfig": {
      "PreloadDataType": "{{string}}"
   },
   "ProfileConfiguration": {
      "DefaultProfiles": [ "{{string}}" ]
   },
   "SseConfiguration": {
      "KmsEncryptionConfig": {
         "CmkType": "{{string}}",
         "KmsKeyId": "{{string}}"
      }
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateFHIRDatastore_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AnalyticsConfiguration](#API_CreateFHIRDatastore_RequestSyntax) **   <a name="HealthLake-CreateFHIRDatastore-request-AnalyticsConfiguration"></a>
The analytics configuration for the data store.
Type: [AnalyticsConfiguration](API_AnalyticsConfiguration.md) object
Required: No

 ** [ClientToken](#API_CreateFHIRDatastore_RequestSyntax) **   <a name="HealthLake-CreateFHIRDatastore-request-ClientToken"></a>
An optional user-provided token to ensure API idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** [DatastoreName](#API_CreateFHIRDatastore_RequestSyntax) **   <a name="HealthLake-CreateFHIRDatastore-request-DatastoreName"></a>
The data store name (user-generated).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`
Required: No

 ** [DatastoreTypeVersion](#API_CreateFHIRDatastore_RequestSyntax) **   <a name="HealthLake-CreateFHIRDatastore-request-DatastoreTypeVersion"></a>
The FHIR release version supported by the data store. Current support is for version `R4`.
Type: String
Valid Values: `R4`
Required: Yes

 ** [IdentityProviderConfiguration](#API_CreateFHIRDatastore_RequestSyntax) **   <a name="HealthLake-CreateFHIRDatastore-request-IdentityProviderConfiguration"></a>
The identity provider configuration to use for the data store.
Type: [IdentityProviderConfiguration](API_IdentityProviderConfiguration.md) object
Required: No

 ** [NlpConfiguration](#API_CreateFHIRDatastore_RequestSyntax) **   <a name="HealthLake-CreateFHIRDatastore-request-NlpConfiguration"></a>
The natural language processing (NLP) configuration for the data store.
Type: [NlpConfiguration](API_NlpConfiguration.md) object
Required: No

 ** [PreloadDataConfig](#API_CreateFHIRDatastore_RequestSyntax) **   <a name="HealthLake-CreateFHIRDatastore-request-PreloadDataConfig"></a>
An optional parameter to preload (import) open source Synthea FHIR data upon creation of the data store.
Type: [PreloadDataConfig](API_PreloadDataConfig.md) object
Required: No

 ** [ProfileConfiguration](#API_CreateFHIRDatastore_RequestSyntax) **   <a name="HealthLake-CreateFHIRDatastore-request-ProfileConfiguration"></a>
The profile configuration for the data store.
Type: [ProfileConfiguration](API_ProfileConfiguration.md) object
Required: No

 ** [SseConfiguration](#API_CreateFHIRDatastore_RequestSyntax) **   <a name="HealthLake-CreateFHIRDatastore-request-SseConfiguration"></a>
The server-side encryption key configuration for a customer-provided encryption key specified for creating a data store.
Type: [SseConfiguration](API_SseConfiguration.md) object
Required: No

 ** [Tags](#API_CreateFHIRDatastore_RequestSyntax) **   <a name="HealthLake-CreateFHIRDatastore-request-Tags"></a>
The resource tags applied to a data store when it is created.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateFHIRDatastore_ResponseSyntax"></a>

```
{
   "DatastoreArn": "string",
   "DatastoreEndpoint": "string",
   "DatastoreId": "string",
   "DatastoreStatus": "string"
}
```

## Response Elements
<a name="API_CreateFHIRDatastore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DatastoreArn](#API_CreateFHIRDatastore_ResponseSyntax) **   <a name="HealthLake-CreateFHIRDatastore-response-DatastoreArn"></a>
The Amazon Resource Name (ARN) for the data store.
Type: String
Pattern: `arn:aws((-us-gov)|(-iso)|(-iso-b)|(-cn))?:healthlake:[a-zA-Z0-9-]+:[0-9]{12}:datastore/.+?`

 ** [DatastoreEndpoint](#API_CreateFHIRDatastore_ResponseSyntax) **   <a name="HealthLake-CreateFHIRDatastore-response-DatastoreEndpoint"></a>
The AWS endpoint created for the data store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5000.
Pattern: `[\P{M}\p{M}]{1,5000}`

 ** [DatastoreId](#API_CreateFHIRDatastore_ResponseSyntax) **   <a name="HealthLake-CreateFHIRDatastore-response-DatastoreId"></a>
The data store identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`

 ** [DatastoreStatus](#API_CreateFHIRDatastore_ResponseSyntax) **   <a name="HealthLake-CreateFHIRDatastore-response-DatastoreStatus"></a>
The data store status.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | DELETED | CREATE_FAILED | UPDATING | UPDATE_FAILED`

## Errors
<a name="API_CreateFHIRDatastore_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied. Your account is not authorized to perform this operation.
HTTP Status Code: 400

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
<a name="API_CreateFHIRDatastore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/healthlake-2017-07-01/CreateFHIRDatastore)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/healthlake-2017-07-01/CreateFHIRDatastore)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/CreateFHIRDatastore)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/healthlake-2017-07-01/CreateFHIRDatastore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/CreateFHIRDatastore)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/healthlake-2017-07-01/CreateFHIRDatastore)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/healthlake-2017-07-01/CreateFHIRDatastore)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/healthlake-2017-07-01/CreateFHIRDatastore)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/CreateFHIRDatastore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/CreateFHIRDatastore)
