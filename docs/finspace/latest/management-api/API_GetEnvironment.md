---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_GetEnvironment.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# GetEnvironment
<a name="API_GetEnvironment"></a>

Returns the FinSpace environment object.

## Request Syntax
<a name="API_GetEnvironment_RequestSyntax"></a>

```
GET /environment/{{environmentId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEnvironment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [environmentId](#API_GetEnvironment_RequestSyntax) **   <a name="finspace-GetEnvironment-request-uri-environmentId"></a>
The identifier of the FinSpace environment.
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]{1,26}$`
Required: Yes

## Request Body
<a name="API_GetEnvironment_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEnvironment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "environment": {
      "awsAccountId": "string",
      "dedicatedServiceAccountId": "string",
      "description": "string",
      "environmentArn": "string",
      "environmentId": "string",
      "environmentUrl": "string",
      "federationMode": "string",
      "federationParameters": {
         "applicationCallBackURL": "string",
         "attributeMap": {
            "string" : "string"
         },
         "federationProviderName": "string",
         "federationURN": "string",
         "samlMetadataDocument": "string",
         "samlMetadataURL": "string"
      },
      "kmsKeyId": "string",
      "name": "string",
      "sageMakerStudioDomainUrl": "string",
      "status": "string"
   }
}
```

## Response Elements
<a name="API_GetEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environment](#API_GetEnvironment_ResponseSyntax) **   <a name="finspace-GetEnvironment-response-environment"></a>
The name of the FinSpace environment.
Type: [Environment](API_Environment.md) object

## Errors
<a name="API_GetEnvironment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2021-03-12/GetEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2021-03-12/GetEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/GetEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2021-03-12/GetEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/GetEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2021-03-12/GetEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2021-03-12/GetEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2021-03-12/GetEnvironment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/finspace-2021-03-12/GetEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/GetEnvironment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
