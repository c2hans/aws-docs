---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_Application.html
---

# Application
<a name="API_app-registry_Application"></a>

Represents a AWS Service Catalog AppRegistry application that is the top-level node in a hierarchy of related cloud resource abstractions.

## Contents
<a name="API_app-registry_Application_Contents"></a>

 ** applicationTag **   <a name="servicecatalog-Type-app-registry_Application-applicationTag"></a>
 A key-value pair that identifies an associated resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
Required: No

 ** arn **   <a name="servicecatalog-Type-app-registry_Application-arn"></a>
The Amazon resource name (ARN) that specifies the application across services.
Type: String
Pattern: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[a-z0-9]+`
Required: No

 ** creationTime **   <a name="servicecatalog-Type-app-registry_Application-creationTime"></a>
The ISO-8601 formatted timestamp of the moment when the application was created.
Type: Timestamp
Required: No

 ** description **   <a name="servicecatalog-Type-app-registry_Application-description"></a>
The description of the application.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** id **   <a name="servicecatalog-Type-app-registry_Application-id"></a>
The identifier of the application.
Type: String
Length Constraints: Fixed length of 26.
Pattern: `[a-z0-9]+`
Required: No

 ** lastUpdateTime **   <a name="servicecatalog-Type-app-registry_Application-lastUpdateTime"></a>
 The ISO-8601 formatted timestamp of the moment when the application was last updated.
Type: Timestamp
Required: No

 ** name **   <a name="servicecatalog-Type-app-registry_Application-name"></a>
The name of the application. The name must be unique in the region in which you are creating the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-.\w]+`
Required: No

 ** tags **   <a name="servicecatalog-Type-app-registry_Application-tags"></a>
Key-value pairs you can use to associate with the application.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
Required: No

## See Also
<a name="API_app-registry_Application_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWS242AppRegistry-2020-06-24/Application)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/Application)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/Application)
