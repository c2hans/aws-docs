---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ApiConfiguration.html
---

# ApiConfiguration
<a name="API_ApiConfiguration"></a>

Describes the API configuration for a code generation job.

## Contents
<a name="API_ApiConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** dataStoreConfig **   <a name="amplifyuibuilder-Type-ApiConfiguration-dataStoreConfig"></a>
The configuration for an application using DataStore APIs.
Type: [DataStoreRenderConfig](API_DataStoreRenderConfig.md) object
Required: No

 ** graphQLConfig **   <a name="amplifyuibuilder-Type-ApiConfiguration-graphQLConfig"></a>
The configuration for an application using GraphQL APIs.
Type: [GraphQLRenderConfig](API_GraphQLRenderConfig.md) object
Required: No

 ** noApiConfig **   <a name="amplifyuibuilder-Type-ApiConfiguration-noApiConfig"></a>
The configuration for an application with no API being used.
Type: [NoApiRenderConfig](API_NoApiRenderConfig.md) object
Required: No

## See Also
<a name="API_ApiConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/ApiConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/ApiConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/ApiConfiguration)
