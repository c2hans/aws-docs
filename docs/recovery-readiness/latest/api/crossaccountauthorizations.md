---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/crossaccountauthorizations.html
---

# ListCrossAccountAuthorizations, CreateCrossAccountAuthorization
<a name="crossaccountauthorizations"></a>

## URI
<a name="crossaccountauthorizations-url"></a>

`/crossaccountauthorizations`

## HTTP methods
<a name="crossaccountauthorizations-http-methods"></a>

### GET
<a name="crossaccountauthorizationsget"></a>

**Operation ID:** `ListCrossAccountAuthorizations`

Lists the cross-account readiness authorizations that are in place for an account.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The token that identifies which batch of results you want to see. |
| maxResults | String | False | The number of objects that you want to return with this call. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListCrossAccountAuthorizationsResult | 200 response - Success. |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | None | 403 response - Access denied exception. You do not have sufficient access to perform this action. |
| 429 | None | 429 response - Limit exceeded exception or too many requests exception.  |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### POST
<a name="crossaccountauthorizationspost"></a>

**Operation ID:** `CreateCrossAccountAuthorization`

Creates a cross-account readiness authorization. This lets you authorize another account to work with Route 53 Application Recovery Controller, for example, to check the readiness status of resources in a separate account.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | CreateCrossAccountAuthorizationResult | 200 response - Success. |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | None | 403 response - Access denied exception. You do not have sufficient access to perform this action. |
| 409 | None | 409 response - Conflict exception. You might be using a predefined variable. |
| 429 | None | 429 response - Limit exceeded exception or too many requests exception.  |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### OPTIONS
<a name="crossaccountauthorizationsoptions"></a>

Enables CORS by returning correct headers.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response - Success. |

## Schemas
<a name="crossaccountauthorizations-schemas"></a>

### Request bodies
<a name="crossaccountauthorizations-request-examples"></a>

#### POST schema
<a name="crossaccountauthorizations-request-body-post-example"></a>

```
{
  "crossAccountAuthorization": "string"
}
```

### Response bodies
<a name="crossaccountauthorizations-response-examples"></a>

#### ListCrossAccountAuthorizationsResult schema
<a name="crossaccountauthorizations-response-body-listcrossaccountauthorizationsresult-example"></a>

```
{
  "nextToken": "string",
  "crossAccountAuthorizations": [
    "string"
  ]
}
```

#### CreateCrossAccountAuthorizationResult schema
<a name="crossaccountauthorizations-response-body-createcrossaccountauthorizationresult-example"></a>

```
{
  "crossAccountAuthorization": "string"
}
```

## Properties
<a name="crossaccountauthorizations-properties"></a>

### CreateCrossAccountAuthorizationParameters
<a name="crossaccountauthorizations-model-createcrossaccountauthorizationparameters"></a>

Parameters used to create a cross-account authorization.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| crossAccountAuthorization | string | True | The cross-account authorization. |

### CreateCrossAccountAuthorizationResult
<a name="crossaccountauthorizations-model-createcrossaccountauthorizationresult"></a>

The result of a successful `CreateCrossAccountAuthorization` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| crossAccountAuthorization | string | False | The cross-account authorization. |

### ListCrossAccountAuthorizationsResult
<a name="crossaccountauthorizations-model-listcrossaccountauthorizationsresult"></a>

The result of a successful `ListCrossAccountAuthorizations` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| crossAccountAuthorizations | Array of type string | True | A list of cross-account authorizations. |
| nextToken | string | False | The token that identifies which batch of results you want to see. |

## See also
<a name="crossaccountauthorizations-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListCrossAccountAuthorizations
<a name="ListCrossAccountAuthorizations-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/ListCrossAccountAuthorizations)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/ListCrossAccountAuthorizations)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/ListCrossAccountAuthorizations)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/ListCrossAccountAuthorizations)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/ListCrossAccountAuthorizations)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/ListCrossAccountAuthorizations)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/ListCrossAccountAuthorizations)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/ListCrossAccountAuthorizations)
+ [AWS SDK for Python (Boto3)](/goto/boto3/aws-meridian-beta-2019-12-02/ListCrossAccountAuthorizations)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/ListCrossAccountAuthorizations)

### CreateCrossAccountAuthorization
<a name="CreateCrossAccountAuthorization-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/CreateCrossAccountAuthorization)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/CreateCrossAccountAuthorization)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/CreateCrossAccountAuthorization)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/CreateCrossAccountAuthorization)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/CreateCrossAccountAuthorization)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/CreateCrossAccountAuthorization)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/CreateCrossAccountAuthorization)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/CreateCrossAccountAuthorization)
+ [AWS SDK for Python (Boto3)](/goto/boto3/aws-meridian-beta-2019-12-02/CreateCrossAccountAuthorization)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/CreateCrossAccountAuthorization)
