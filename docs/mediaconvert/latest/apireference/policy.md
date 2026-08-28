---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/apireference/policy.html
---

# Policy
<a name="policy"></a>

## URI
<a name="policy-url"></a>

`/2017-08-29/policy`

## HTTP methods
<a name="policy-http-methods"></a>

### GET
<a name="policyget"></a>

**Operation ID:** `GetPolicy`

Retrieve the JSON for your policy.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetPolicyResponse | 200 response |
| 400 | ExceptionBody | The service can't process your request because of a problem in the request. Please check your request form and syntax. |
| 402 | ExceptionBody | You attempted to create more resources than the service allows based on service quotas. |
| 403 | ExceptionBody | You don't have permissions for this action with the credentials you sent. |
| 404 | ExceptionBody | The resource you requested does not exist. |
| 409 | ExceptionBody | The service could not complete your request because there is a conflict with the current state of the resource. |
| 429 | ExceptionBody | Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests. |
| 500 | ExceptionBody | The service encountered an unexpected condition and cannot fulfill your request. |

### PUT
<a name="policyput"></a>

**Operation ID:** `PutPolicy`

Create or change your policy. For more information about policies, see the user guide at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | PutPolicyResponse | 200 response |
| 400 | ExceptionBody | The service can't process your request because of a problem in the request. Please check your request form and syntax. |
| 402 | ExceptionBody | You attempted to create more resources than the service allows based on service quotas. |
| 403 | ExceptionBody | You don't have permissions for this action with the credentials you sent. |
| 404 | ExceptionBody | The resource you requested does not exist. |
| 409 | ExceptionBody | The service could not complete your request because there is a conflict with the current state of the resource. |
| 429 | ExceptionBody | Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests. |
| 500 | ExceptionBody | The service encountered an unexpected condition and cannot fulfill your request. |

### DELETE
<a name="policydelete"></a>

**Operation ID:** `DeletePolicy`

Permanently delete a policy that you created.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | DeletePolicyResponse | 200 response |
| 400 | ExceptionBody | The service can't process your request because of a problem in the request. Please check your request form and syntax. |
| 402 | ExceptionBody | You attempted to create more resources than the service allows based on service quotas. |
| 403 | ExceptionBody | You don't have permissions for this action with the credentials you sent. |
| 404 | ExceptionBody | The resource you requested does not exist. |
| 409 | ExceptionBody | The service could not complete your request because there is a conflict with the current state of the resource. |
| 429 | ExceptionBody | Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests. |
| 500 | ExceptionBody | The service encountered an unexpected condition and cannot fulfill your request. |

### OPTIONS
<a name="policyoptions"></a>

Supports CORS preflight requests.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request completed successfully. |

## Schemas
<a name="policy-schemas"></a>

### Request bodies
<a name="policy-request-examples"></a>

#### GET schema
<a name="policy-request-body-get-example"></a>

```
{
}
```

#### PUT schema
<a name="policy-request-body-put-example"></a>

```
{
  "policy": {
    "s3Inputs": enum,
    "httpInputs": enum,
    "httpsInputs": enum
  }
}
```

#### DELETE schema
<a name="policy-request-body-delete-example"></a>

```
{
}
```

### Response bodies
<a name="policy-response-examples"></a>

#### GetPolicyResponse schema
<a name="policy-response-body-getpolicyresponse-example"></a>

```
{
  "policy": {
    "s3Inputs": enum,
    "httpInputs": enum,
    "httpsInputs": enum
  }
}
```

#### PutPolicyResponse schema
<a name="policy-response-body-putpolicyresponse-example"></a>

```
{
  "policy": {
    "s3Inputs": enum,
    "httpInputs": enum,
    "httpsInputs": enum
  }
}
```

#### DeletePolicyResponse schema
<a name="policy-response-body-deletepolicyresponse-example"></a>

```
{
}
```

#### ExceptionBody schema
<a name="policy-response-body-exceptionbody-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="policy-properties"></a>

### DeletePolicyRequest
<a name="policy-model-deletepolicyrequest"></a>

Send a request to permanently delete a policy that you created.

### DeletePolicyResponse
<a name="policy-model-deletepolicyresponse"></a>

Successful DELETE policy requests will return an OK message.

### ExceptionBody
<a name="policy-model-exceptionbody"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### GetPolicyRequest
<a name="policy-model-getpolicyrequest"></a>

Send a request to retrieve the JSON for your policy.

### GetPolicyResponse
<a name="policy-model-getpolicyresponse"></a>

Successful GET policy requests will return the JSON for your policy.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| policy | [Policy](#policy-model-policy) | False | A policy configures behavior that you allow or disallow for your account. For information about MediaConvert policies, see the user guide at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html |

### InputPolicy
<a name="policy-model-inputpolicy"></a>

An input policy allows or disallows a job you submit to run based on the conditions that you specify.
+ `ALLOWED`
+ `DISALLOWED`

### Policy
<a name="policy-model-policy"></a>

A policy configures behavior that you allow or disallow for your account. For information about MediaConvert policies, see the user guide at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| httpInputs | [InputPolicy](#policy-model-inputpolicy) | False | Allow or disallow jobs that specify HTTP inputs. |
| httpsInputs | [InputPolicy](#policy-model-inputpolicy) | False | Allow or disallow jobs that specify HTTPS inputs. |
| s3Inputs | [InputPolicy](#policy-model-inputpolicy) | False | Allow or disallow jobs that specify Amazon S3 inputs. |

### PutPolicyRequest
<a name="policy-model-putpolicyrequest"></a>

Create or change a policy by sending a request that includes your policy in JSON.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| policy | [Policy](#policy-model-policy) | True | A policy configures behavior that you allow or disallow for your account. For information about MediaConvert policies, see the user guide at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html |

### PutPolicyResponse
<a name="policy-model-putpolicyresponse"></a>

Successful PUT policy requests will return your policy.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| policy | [Policy](#policy-model-policy) | False | A policy configures behavior that you allow or disallow for your account. For information about MediaConvert policies, see the user guide at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html |

## See also
<a name="policy-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetPolicy
<a name="GetPolicy-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediaconvert-2017-08-29/GetPolicy)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediaconvert-2017-08-29/GetPolicy)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediaconvert-2017-08-29/GetPolicy)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediaconvert-2017-08-29/GetPolicy)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediaconvert-2017-08-29/GetPolicy)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediaconvert-2017-08-29/GetPolicy)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediaconvert-2017-08-29/GetPolicy)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediaconvert-2017-08-29/GetPolicy)
+ [AWS SDK for Python](/goto/boto3/mediaconvert-2017-08-29/GetPolicy)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediaconvert-2017-08-29/GetPolicy)

### PutPolicy
<a name="PutPolicy-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediaconvert-2017-08-29/PutPolicy)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediaconvert-2017-08-29/PutPolicy)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediaconvert-2017-08-29/PutPolicy)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediaconvert-2017-08-29/PutPolicy)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediaconvert-2017-08-29/PutPolicy)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediaconvert-2017-08-29/PutPolicy)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediaconvert-2017-08-29/PutPolicy)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediaconvert-2017-08-29/PutPolicy)
+ [AWS SDK for Python](/goto/boto3/mediaconvert-2017-08-29/PutPolicy)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediaconvert-2017-08-29/PutPolicy)

### DeletePolicy
<a name="DeletePolicy-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediaconvert-2017-08-29/DeletePolicy)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediaconvert-2017-08-29/DeletePolicy)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediaconvert-2017-08-29/DeletePolicy)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediaconvert-2017-08-29/DeletePolicy)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediaconvert-2017-08-29/DeletePolicy)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediaconvert-2017-08-29/DeletePolicy)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediaconvert-2017-08-29/DeletePolicy)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediaconvert-2017-08-29/DeletePolicy)
+ [AWS SDK for Python](/goto/boto3/mediaconvert-2017-08-29/DeletePolicy)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediaconvert-2017-08-29/DeletePolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
