---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/crossaccountauthorizations-crossaccountauthorization.html
---

# DeleteCrossAccountAuthorization
<a name="crossaccountauthorizations-crossaccountauthorization"></a>

## URI
<a name="crossaccountauthorizations-crossaccountauthorization-url"></a>

`/crossaccountauthorizations/{{crossAccountAuthorization}}`

## HTTP methods
<a name="crossaccountauthorizations-crossaccountauthorization-http-methods"></a>

### DELETE
<a name="crossaccountauthorizations-crossaccountauthorizationdelete"></a>

**Operation ID:** `DeleteCrossAccountAuthorization`

Deletes cross account readiness authorization.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{crossAccountAuthorization}} | String | True | The cross-account authorization. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | DeleteCrossAccountAuthorizationResult | 200 response - Success. |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | None | 403 response - Access denied exception. You do not have sufficient access to perform this action. |
| 429 | None | 429 response - Limit exceeded exception or too many requests exception.  |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### OPTIONS
<a name="crossaccountauthorizations-crossaccountauthorizationoptions"></a>

Enables CORS by returning correct headers.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{crossAccountAuthorization}} | String | True | The cross-account authorization. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response - Success. |

## Schemas
<a name="crossaccountauthorizations-crossaccountauthorization-schemas"></a>

### Response bodies
<a name="crossaccountauthorizations-crossaccountauthorization-response-examples"></a>

#### DeleteCrossAccountAuthorizationResult schema
<a name="crossaccountauthorizations-crossaccountauthorization-response-body-deletecrossaccountauthorizationresult-example"></a>

```
{
}
```

## Properties
<a name="crossaccountauthorizations-crossaccountauthorization-properties"></a>

### DeleteCrossAccountAuthorizationResult
<a name="crossaccountauthorizations-crossaccountauthorization-model-deletecrossaccountauthorizationresult"></a>

A successful `DeleteCrossAccountAuthorization` request returns no response.

## See also
<a name="crossaccountauthorizations-crossaccountauthorization-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DeleteCrossAccountAuthorization
<a name="DeleteCrossAccountAuthorization-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/DeleteCrossAccountAuthorization)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/DeleteCrossAccountAuthorization)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/DeleteCrossAccountAuthorization)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/DeleteCrossAccountAuthorization)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/DeleteCrossAccountAuthorization)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/DeleteCrossAccountAuthorization)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/DeleteCrossAccountAuthorization)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/DeleteCrossAccountAuthorization)
+ [AWS SDK for Python](/goto/boto3/aws-meridian-beta-2019-12-02/DeleteCrossAccountAuthorization)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/DeleteCrossAccountAuthorization)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recovery-readiness` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
