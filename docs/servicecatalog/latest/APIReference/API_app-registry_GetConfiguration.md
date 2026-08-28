---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_app-registry_GetConfiguration.html
---

# GetConfiguration
<a name="API_app-registry_GetConfiguration"></a>

**Note**
 AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

 Retrieves a `TagKey` configuration from an account.

## Request Syntax
<a name="API_app-registry_GetConfiguration_RequestSyntax"></a>

```
GET /configuration HTTP/1.1
```

## URI Request Parameters
<a name="API_app-registry_GetConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_app-registry_GetConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_app-registry_GetConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configuration": {
      "tagQueryConfiguration": {
         "tagKey": "string"
      }
   }
}
```

## Response Elements
<a name="API_app-registry_GetConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuration](#API_app-registry_GetConfiguration_ResponseSyntax) **   <a name="servicecatalog-app-registry_GetConfiguration-response-configuration"></a>
 Retrieves `TagKey` configuration from an account.
Type: [AppRegistryConfiguration](API_app-registry_AppRegistryConfiguration.md) object

## Errors
<a name="API_app-registry_GetConfiguration_Errors"></a>

 ** InternalServerException **
The service is experiencing internal problems.
HTTP Status Code: 500

## See Also
<a name="API_app-registry_GetConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/AWS242AppRegistry-2020-06-24/GetConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/GetConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWS242AppRegistry-2020-06-24/GetConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/GetConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/GetConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/GetConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/GetConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/GetConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/AWS242AppRegistry-2020-06-24/GetConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/GetConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
