---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_GetAccountLevelServiceConfiguration.html
---

# GetAccountLevelServiceConfiguration
<a name="API_GetAccountLevelServiceConfiguration"></a>

Retrieves the status of your account's AWS service access, and validates the service linked role required to access the multi-account search feature. Only the management account can invoke this API call.

 **Minimum permissions**

To call this operation, you must have the following permissions:
+  **Action**: `resource-explorer-2:GetAccountLevelServiceConfiguration`

   **Resource**: No specific resource (\*).

## Request Syntax
<a name="API_GetAccountLevelServiceConfiguration_RequestSyntax"></a>

```
POST /GetAccountLevelServiceConfiguration HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAccountLevelServiceConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetAccountLevelServiceConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAccountLevelServiceConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "OrgConfiguration": {
      "AWSServiceAccessStatus": "string",
      "ServiceLinkedRole": "string"
   }
}
```

## Response Elements
<a name="API_GetAccountLevelServiceConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OrgConfiguration](#API_GetAccountLevelServiceConfiguration_ResponseSyntax) **   <a name="resourceexplorer-GetAccountLevelServiceConfiguration-response-OrgConfiguration"></a>
Details about the organization, and whether configuration is `ENABLED` or `DISABLED`.
Type: [OrgConfiguration](API_OrgConfiguration.md) object

## Errors
<a name="API_GetAccountLevelServiceConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The credentials that you used to call this operation don't have the minimum required permissions.
HTTP Status Code: 403

 ** InternalServerException **
The request failed because of internal service error. Try your request again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.
HTTP Status Code: 404

 ** ThrottlingException **
The request failed because you exceeded a rate limit for this operation. For more information, see [Quotas for Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html).
HTTP Status Code: 429

## Examples
<a name="API_GetAccountLevelServiceConfiguration_Examples"></a>

### Example
<a name="API_GetAccountLevelServiceConfiguration_Example_1"></a>

The following example shows how to configure Resource Explorer multi-account search for your organization.

#### Sample Request
<a name="API_GetAccountLevelServiceConfiguration_Example_1_Request"></a>

```
POST /GetAccountLevelServiceConfiguration HTTP/1.1
Host: resource-explorer-2.us-east-1.amazonaws.com
X-Amz-Date: 20221101T200059Z
Accept-Encoding: identity
User-Agent: <UserAgentString>
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
```

#### Sample Response
<a name="API_GetAccountLevelServiceConfiguration_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 01 Nov 2022 20:00:59 GMT
Content-Type: application/json
Content-Length: <PayloadSizeBytes>

{
    "OrgConfiguration": {
        "AWSServiceAccessStatus": "ENABLED",
        "ServiceLinkedRole": "arn:aws:iam::123456789012:role/aws-service-role/resource-explorer-2.amazonaws.com/AWSServiceRoleForResourceExplorer"
      }
 }
```

## See Also
<a name="API_GetAccountLevelServiceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-explorer-2-2022-07-28/GetAccountLevelServiceConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-explorer-2-2022-07-28/GetAccountLevelServiceConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/GetAccountLevelServiceConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-explorer-2-2022-07-28/GetAccountLevelServiceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/GetAccountLevelServiceConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-explorer-2-2022-07-28/GetAccountLevelServiceConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-explorer-2-2022-07-28/GetAccountLevelServiceConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-explorer-2-2022-07-28/GetAccountLevelServiceConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resource-explorer-2-2022-07-28/GetAccountLevelServiceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/GetAccountLevelServiceConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resource Explorer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resource-explorer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
