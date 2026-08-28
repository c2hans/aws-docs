---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_PutMetadataFlag.html
---

# PutMetadataFlag
<a name="API_PutMetadataFlag"></a>

Stores the metadata information about a feature on a form.

## Request Syntax
<a name="API_PutMetadataFlag_RequestSyntax"></a>

```
PUT /app/{{appId}}/environment/{{environmentName}}/metadata/features/{{featureName}} HTTP/1.1
Content-type: application/json

{
   "newValue": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutMetadataFlag_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_PutMetadataFlag_RequestSyntax) **   <a name="amplifyuibuilder-PutMetadataFlag-request-uri-appId"></a>
The unique ID for the Amplify app.
Required: Yes

 ** [environmentName](#API_PutMetadataFlag_RequestSyntax) **   <a name="amplifyuibuilder-PutMetadataFlag-request-uri-environmentName"></a>
The name of the backend environment that is part of the Amplify app.
Required: Yes

 ** [featureName](#API_PutMetadataFlag_RequestSyntax) **   <a name="amplifyuibuilder-PutMetadataFlag-request-uri-featureName"></a>
The name of the feature associated with the metadata.
Required: Yes

## Request Body
<a name="API_PutMetadataFlag_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [newValue](#API_PutMetadataFlag_RequestSyntax) **   <a name="amplifyuibuilder-PutMetadataFlag-request-newValue"></a>
The new information to store.
Type: String
Required: Yes

## Response Syntax
<a name="API_PutMetadataFlag_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutMetadataFlag_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutMetadataFlag_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
An invalid or out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

 ** UnauthorizedException **
You don't have permission to perform this operation.
HTTP Status Code: 401

## See Also
<a name="API_PutMetadataFlag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplifyuibuilder-2021-08-11/PutMetadataFlag)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplifyuibuilder-2021-08-11/PutMetadataFlag)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/PutMetadataFlag)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplifyuibuilder-2021-08-11/PutMetadataFlag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/PutMetadataFlag)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplifyuibuilder-2021-08-11/PutMetadataFlag)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplifyuibuilder-2021-08-11/PutMetadataFlag)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplifyuibuilder-2021-08-11/PutMetadataFlag)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplifyuibuilder-2021-08-11/PutMetadataFlag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/PutMetadataFlag)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmplifyUIBuilder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplifyuibuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
