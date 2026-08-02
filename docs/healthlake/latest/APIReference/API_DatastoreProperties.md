---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DatastoreProperties.html
---

# DatastoreProperties
<a name="API_DatastoreProperties"></a>

The data store properties.

## Contents
<a name="API_DatastoreProperties_Contents"></a>

 ** DatastoreArn **   <a name="HealthLake-Type-DatastoreProperties-DatastoreArn"></a>
The Amazon Resource Name (ARN) used in the creation of the data store.
Type: String
Pattern: `arn:aws((-us-gov)|(-iso)|(-iso-b)|(-cn))?:healthlake:[a-zA-Z0-9-]+:[0-9]{12}:datastore/.+?`
Required: Yes

 ** DatastoreEndpoint **   <a name="HealthLake-Type-DatastoreProperties-DatastoreEndpoint"></a>
The AWS endpoint for the data store.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Pattern: `[\P{M}\p{M}]{0,10000}`
Required: Yes

 ** DatastoreId **   <a name="HealthLake-Type-DatastoreProperties-DatastoreId"></a>
The data store identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`
Required: Yes

 ** DatastoreStatus **   <a name="HealthLake-Type-DatastoreProperties-DatastoreStatus"></a>
The data store status.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | DELETED | CREATE_FAILED | UPDATING | UPDATE_FAILED`
Required: Yes

 ** DatastoreTypeVersion **   <a name="HealthLake-Type-DatastoreProperties-DatastoreTypeVersion"></a>
The FHIR release version supported by the data store. Current support is for version `R4`.
Type: String
Valid Values: `R4`
Required: Yes

 ** AnalyticsConfiguration **   <a name="HealthLake-Type-DatastoreProperties-AnalyticsConfiguration"></a>
The analytics configuration for the data store.
Type: [AnalyticsConfiguration](API_AnalyticsConfiguration.md) object
Required: No

 ** CreatedAt **   <a name="HealthLake-Type-DatastoreProperties-CreatedAt"></a>
The time the data store was created.
Type: Timestamp
Required: No

 ** DatastoreName **   <a name="HealthLake-Type-DatastoreProperties-DatastoreName"></a>
The data store name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`
Required: No

 ** ErrorCause **   <a name="HealthLake-Type-DatastoreProperties-ErrorCause"></a>
The error cause for the current data store operation.
Type: [ErrorCause](API_ErrorCause.md) object
Required: No

 ** IdentityProviderConfiguration **   <a name="HealthLake-Type-DatastoreProperties-IdentityProviderConfiguration"></a>
The identity provider selected during data store creation.
Type: [IdentityProviderConfiguration](API_IdentityProviderConfiguration.md) object
Required: No

 ** NlpConfiguration **   <a name="HealthLake-Type-DatastoreProperties-NlpConfiguration"></a>
The natural language processing (NLP) configuration for the data store.
Type: [NlpConfiguration](API_NlpConfiguration.md) object
Required: No

 ** PreloadDataConfig **   <a name="HealthLake-Type-DatastoreProperties-PreloadDataConfig"></a>
The preloaded Synthea data configuration for the data store.
Type: [PreloadDataConfig](API_PreloadDataConfig.md) object
Required: No

 ** ProfileConfiguration **   <a name="HealthLake-Type-DatastoreProperties-ProfileConfiguration"></a>
The profile configuration for the data store.
Type: [ProfileConfiguration](API_ProfileConfiguration.md) object
Required: No

 ** SseConfiguration **   <a name="HealthLake-Type-DatastoreProperties-SseConfiguration"></a>
 The server-side encryption key configuration for a customer provided encryption key.
Type: [SseConfiguration](API_SseConfiguration.md) object
Required: No

## See Also
<a name="API_DatastoreProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/DatastoreProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/DatastoreProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/DatastoreProperties)
