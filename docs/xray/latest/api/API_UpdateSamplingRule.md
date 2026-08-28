---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_UpdateSamplingRule.html
---

# UpdateSamplingRule
<a name="API_UpdateSamplingRule"></a>

Modifies a sampling rule's configuration.

## Request Syntax
<a name="API_UpdateSamplingRule_RequestSyntax"></a>

```
POST /UpdateSamplingRule HTTP/1.1
Content-type: application/json

{
   "SamplingRuleUpdate": {
      "Attributes": {
         "{{string}}" : "{{string}}"
      },
      "FixedRate": {{number}},
      "Host": "{{string}}",
      "HTTPMethod": "{{string}}",
      "Priority": {{number}},
      "ReservoirSize": {{number}},
      "ResourceARN": "{{string}}",
      "RuleARN": "{{string}}",
      "RuleName": "{{string}}",
      "SamplingRateBoost": {
         "CooldownWindowMinutes": {{number}},
         "MaxRate": {{number}}
      },
      "ServiceName": "{{string}}",
      "ServiceType": "{{string}}",
      "URLPath": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateSamplingRule_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateSamplingRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SamplingRuleUpdate](#API_UpdateSamplingRule_RequestSyntax) **   <a name="xray-UpdateSamplingRule-request-SamplingRuleUpdate"></a>
The rule and fields to change.
Type: [SamplingRuleUpdate](API_SamplingRuleUpdate.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateSamplingRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "SamplingRuleRecord": {
      "CreatedAt": number,
      "ModifiedAt": number,
      "SamplingRule": {
         "Attributes": {
            "string" : "string"
         },
         "FixedRate": number,
         "Host": "string",
         "HTTPMethod": "string",
         "Priority": number,
         "ReservoirSize": number,
         "ResourceARN": "string",
         "RuleARN": "string",
         "RuleName": "string",
         "SamplingRateBoost": {
            "CooldownWindowMinutes": number,
            "MaxRate": number
         },
         "ServiceName": "string",
         "ServiceType": "string",
         "URLPath": "string",
         "Version": number
      }
   }
}
```

## Response Elements
<a name="API_UpdateSamplingRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SamplingRuleRecord](#API_UpdateSamplingRule_ResponseSyntax) **   <a name="xray-UpdateSamplingRule-response-SamplingRuleRecord"></a>
The updated rule definition and metadata.
Type: [SamplingRuleRecord](API_SamplingRuleRecord.md) object

## Errors
<a name="API_UpdateSamplingRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
The request is missing required parameters or has invalid parameters.
HTTP Status Code: 400

 ** ThrottledException **
The request exceeds the maximum number of requests per second.
HTTP Status Code: 429

## See Also
<a name="API_UpdateSamplingRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/UpdateSamplingRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/UpdateSamplingRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/UpdateSamplingRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/UpdateSamplingRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/UpdateSamplingRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/UpdateSamplingRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/UpdateSamplingRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/UpdateSamplingRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/UpdateSamplingRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/UpdateSamplingRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
