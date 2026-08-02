---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_ApiKey.html
---

# ApiKey
<a name="API_ApiKey"></a>

A resource that can be distributed to callers for executing Method resources that require an API key. API keys can be mapped to any Stage on any RestApi, which indicates that the callers with the API key can make requests to that stage.

## Contents
<a name="API_ApiKey_Contents"></a>

 ** createdDate **   <a name="apigw-Type-ApiKey-createdDate"></a>
The timestamp when the API Key was created.
Type: Timestamp
Required: No

 ** customerId **   <a name="apigw-Type-ApiKey-customerId"></a>
An AWS Marketplace customer identifier, when integrating with the AWS SaaS Marketplace.
Type: String
Required: No

 ** description **   <a name="apigw-Type-ApiKey-description"></a>
The description of the API Key.
Type: String
Required: No

 ** enabled **   <a name="apigw-Type-ApiKey-enabled"></a>
Specifies whether the API Key can be used by callers.
Type: Boolean
Required: No

 ** id **   <a name="apigw-Type-ApiKey-id"></a>
The identifier of the API Key.
Type: String
Required: No

 ** lastUpdatedDate **   <a name="apigw-Type-ApiKey-lastUpdatedDate"></a>
The timestamp when the API Key was last updated.
Type: Timestamp
Required: No

 ** name **   <a name="apigw-Type-ApiKey-name"></a>
The name of the API Key.
Type: String
Required: No

 ** stageKeys **   <a name="apigw-Type-ApiKey-stageKeys"></a>
A list of Stage resources that are associated with the ApiKey resource.
Type: Array of strings
Required: No

 ** tags **   <a name="apigw-Type-ApiKey-tags"></a>
The collection of tags. Each tag element is associated with a given resource.
Type: String to string map
Required: No

 ** value **   <a name="apigw-Type-ApiKey-value"></a>
The value of the API Key.
Type: String
Required: No

## See Also
<a name="API_ApiKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/ApiKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/ApiKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/ApiKey)
