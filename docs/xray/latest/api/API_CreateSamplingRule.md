---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_CreateSamplingRule.html
---

# CreateSamplingRule
<a name="API_CreateSamplingRule"></a>

Creates a rule to control sampling behavior for instrumented applications. Services retrieve rules with [GetSamplingRules](https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingRules.html), and evaluate each rule in ascending order of *priority* for each request. If a rule matches, the service records a trace, borrowing it from the reservoir size. After 10 seconds, the service reports back to X-Ray with [GetSamplingTargets](https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingTargets.html) to get updated versions of each in-use rule. The updated rule contains a trace quota that the service can use instead of borrowing from the reservoir.

## Request Syntax
<a name="API_CreateSamplingRule_RequestSyntax"></a>

```
POST /CreateSamplingRule HTTP/1.1
Content-type: application/json

{
   "SamplingRule": {
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
      "URLPath": "{{string}}",
      "Version": {{number}}
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateSamplingRule_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateSamplingRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SamplingRule](#API_CreateSamplingRule_RequestSyntax) **   <a name="xray-CreateSamplingRule-request-SamplingRule"></a>
The rule definition.
Type: [SamplingRule](API_SamplingRule.md) object
Required: Yes

 ** [Tags](#API_CreateSamplingRule_RequestSyntax) **   <a name="xray-CreateSamplingRule-request-Tags"></a>
A map that contains one or more tag keys and tag values to attach to an X-Ray sampling rule. For more information about ways to use tags, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the * AWS General Reference*.
The following restrictions apply to tags:
+ Maximum number of user-applied tags per resource: 50
+ Maximum tag key length: 128 Unicode characters
+ Maximum tag value length: 256 Unicode characters
+ Valid values for key and value: a-z, A-Z, 0-9, space, and the following characters: \_ . : / = \+ - and @
+ Tag keys and values are case sensitive.
+ Don't use `aws:` as a prefix for keys; it's reserved for AWS use.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateSamplingRule_ResponseSyntax"></a>

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
<a name="API_CreateSamplingRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SamplingRuleRecord](#API_CreateSamplingRule_ResponseSyntax) **   <a name="xray-CreateSamplingRule-response-SamplingRuleRecord"></a>
The saved rule definition and metadata.
Type: [SamplingRuleRecord](API_SamplingRuleRecord.md) object

## Errors
<a name="API_CreateSamplingRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
The request is missing required parameters or has invalid parameters.
HTTP Status Code: 400

 ** RuleLimitExceededException **
You have reached the maximum number of sampling rules.
HTTP Status Code: 400

 ** ThrottledException **
The request exceeds the maximum number of requests per second.
HTTP Status Code: 429

## See Also
<a name="API_CreateSamplingRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/CreateSamplingRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/CreateSamplingRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/CreateSamplingRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/CreateSamplingRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/CreateSamplingRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/CreateSamplingRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/CreateSamplingRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/CreateSamplingRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/CreateSamplingRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/CreateSamplingRule)
