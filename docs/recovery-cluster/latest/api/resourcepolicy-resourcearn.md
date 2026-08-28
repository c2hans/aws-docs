---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/resourcepolicy-resourcearn.html
---

# GetResourcePolicy
<a name="resourcepolicy-resourcearn"></a>

Returns the current resource policy for a cluster. You can use this information, for example, to verify that permissions in AWS RAM are set up correctly.

## URI
<a name="resourcepolicy-resourcearn-url"></a>

`/resourcePolicy/{{ResourceArn}}`

## HTTP methods
<a name="resourcepolicy-resourcearn-http-methods"></a>

### GET
<a name="resourcepolicy-resourcearnget"></a>

**Operation ID:** `GetResourcePolicy`

Get information about the resource policy for a cluster.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{ResourceArn}} | String | True | The Amazon Resource Name (ARN) for the resource. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetResourcePolicyResponse | 200 response - Success. |
| 404 | ResourceNotFoundException | 404 response - MalformedQueryString. The query string contains a syntax error or resource not found. |
| 500 | InternalServerException | 500 response - InternalServiceError. Temporary service error. Retry the request. |

### OPTIONS
<a name="resourcepolicy-resourcearnoptions"></a>

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{ResourceArn}} | String | True | The Amazon Resource Name (ARN) for the resource. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method. |

## Schemas
<a name="resourcepolicy-resourcearn-schemas"></a>

### Response bodies
<a name="resourcepolicy-resourcearn-response-examples"></a>

#### GetResourcePolicyResponse schema
<a name="resourcepolicy-resourcearn-response-body-getresourcepolicyresponse-example"></a>

```
{
  "Policy": "string"
}
```

#### ResourceNotFoundException schema
<a name="resourcepolicy-resourcearn-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="resourcepolicy-resourcearn-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="resourcepolicy-resourcearn-properties"></a>

### GetResourcePolicyResponse
<a name="resourcepolicy-resourcearn-model-getresourcepolicyresponse"></a>

Returns the current Amazon Resource Access Manager resource policy for a cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Policy | string<br />Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]+`<br />MinLength: 2<br />MaxLength: 10240 | True | The resource policy. |

### InternalServerException
<a name="resourcepolicy-resourcearn-model-internalserverexception"></a>

500 response - InternalServiceError. Temporary service error. Retry the request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### ResourceNotFoundException
<a name="resourcepolicy-resourcearn-model-resourcenotfoundexception"></a>

404 response - MalformedQueryString. The query string contains a syntax error or resource not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

## See also
<a name="resourcepolicy-resourcearn-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetResourcePolicy
<a name="GetResourcePolicy-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/route53-recovery-control-config-2020-11-02/GetResourcePolicy)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/route53-recovery-control-config-2020-11-02/GetResourcePolicy)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/route53-recovery-control-config-2020-11-02/GetResourcePolicy)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/route53-recovery-control-config-2020-11-02/GetResourcePolicy)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/route53-recovery-control-config-2020-11-02/GetResourcePolicy)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/route53-recovery-control-config-2020-11-02/GetResourcePolicy)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/route53-recovery-control-config-2020-11-02/GetResourcePolicy)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/route53-recovery-control-config-2020-11-02/GetResourcePolicy)
+ [AWS SDK for Python](/goto/boto3/route53-recovery-control-config-2020-11-02/GetResourcePolicy)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/route53-recovery-control-config-2020-11-02/GetResourcePolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recovery-cluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
