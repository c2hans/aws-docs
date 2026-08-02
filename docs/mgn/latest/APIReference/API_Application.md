---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_Application.html
---

# Application
<a name="API_Application"></a>

## Contents
<a name="API_Application_Contents"></a>

 ** applicationAggregatedStatus **   <a name="mgn-Type-Application-applicationAggregatedStatus"></a>
Application aggregated status.
Type: [ApplicationAggregatedStatus](API_ApplicationAggregatedStatus.md) object
Required: No

 ** applicationID **   <a name="mgn-Type-Application-applicationID"></a>
Application ID.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `app-[0-9a-zA-Z]{17}`
Required: No

 ** arn **   <a name="mgn-Type-Application-arn"></a>
Application ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** creationDateTime **   <a name="mgn-Type-Application-creationDateTime"></a>
Application creation dateTime.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** description **   <a name="mgn-Type-Application-description"></a>
Application description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 600.
Pattern: `[^\x00]*`
Required: No

 ** isArchived **   <a name="mgn-Type-Application-isArchived"></a>
Application archival status.
Type: Boolean
Required: No

 ** lastModifiedDateTime **   <a name="mgn-Type-Application-lastModifiedDateTime"></a>
Application last modified dateTime.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** name **   <a name="mgn-Type-Application-name"></a>
Application name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\s\x00]( *[^\s\x00])*`
Required: No

 ** tags **   <a name="mgn-Type-Application-tags"></a>
Application tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** waveID **   <a name="mgn-Type-Application-waveID"></a>
Application wave ID.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `wave-[0-9a-zA-Z]{17}`
Required: No

## See Also
<a name="API_Application_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/Application)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/Application)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/Application)
