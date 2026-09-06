---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/rules.html
---

# ListRules
<a name="rules"></a>

## URI
<a name="rules-url"></a>

`/rules`

## HTTP methods
<a name="rules-http-methods"></a>

### GET
<a name="rulesget"></a>

**Operation ID:** `ListRules`

Lists all readiness rules, or lists the readiness rules for a specific resource type.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| resourceType | String | False | The resource type that a readiness rule applies to. |
| nextToken | String | False | The token that identifies which batch of results you want to see. |
| maxResults | String | False | The number of objects that you want to return with this call. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListRulesResult | 200 response - Success. |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | None | 403 response - Access denied exception. You do not have sufficient access to perform this action. |
| 429 | None | 429 response - Limit exceeded exception or too many requests exception.  |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### OPTIONS
<a name="rulesoptions"></a>

Enable CORS by returning correct headers

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response - Success. |

## Schemas
<a name="rules-schemas"></a>

### Response bodies
<a name="rules-response-examples"></a>

#### ListRulesResult schema
<a name="rules-response-body-listrulesresult-example"></a>

```
{
  "nextToken": "string",
  "rules": [
    {
      "ruleId": "string",
      "ruleDescription": "string",
      "resourceType": "string"
    }
  ]
}
```

## Properties
<a name="rules-properties"></a>

### ListRulesOutput
<a name="rules-model-listrulesoutput"></a>

Readiness rule information, including the resource type, rule ID, and rule description.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| resourceType | string<br />MaxLength: 64 | True | The resource type that the readiness rule applies to. |
| ruleDescription | string<br />MaxLength: 256 | True | The description of a readiness rule. |
| ruleId | string<br />MaxLength: 64 | True | The ID for the readiness rule. |

### ListRulesResult
<a name="rules-model-listrulesresult"></a>

The result of a successful `ListRules` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string | False | The token that identifies which batch of results you want to see. |
| rules | Array of type [ListRulesOutput](#rules-model-listrulesoutput) | False | A list of readiness rules for a specific resource type. |

## See also
<a name="rules-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListRules
<a name="ListRules-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/ListRules)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/ListRules)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/ListRules)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/ListRules)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/ListRules)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/ListRules)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/ListRules)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/ListRules)
+ [AWS SDK for Python](/goto/boto3/aws-meridian-beta-2019-12-02/ListRules)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/ListRules)
