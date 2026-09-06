---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingRules.html
---

# GetSamplingRules
<a name="API_GetSamplingRules"></a>

Retrieves all sampling rules.

## Request Syntax
<a name="API_GetSamplingRules_RequestSyntax"></a>

```
POST /GetSamplingRules HTTP/1.1
Content-type: application/json

{
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetSamplingRules_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetSamplingRules_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [NextToken](#API_GetSamplingRules_RequestSyntax) **   <a name="xray-GetSamplingRules-request-NextToken"></a>
Pagination token.
Type: String
Required: No

## Response Syntax
<a name="API_GetSamplingRules_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "SamplingRuleRecords": [
      {
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
   ]
}
```

## Response Elements
<a name="API_GetSamplingRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetSamplingRules_ResponseSyntax) **   <a name="xray-GetSamplingRules-response-NextToken"></a>
Pagination token.
Type: String

 ** [SamplingRuleRecords](#API_GetSamplingRules_ResponseSyntax) **   <a name="xray-GetSamplingRules-response-SamplingRuleRecords"></a>
Rule definitions and metadata.
Type: Array of [SamplingRuleRecord](API_SamplingRuleRecord.md) objects

## Errors
<a name="API_GetSamplingRules_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
The request is missing required parameters or has invalid parameters.
HTTP Status Code: 400

 ** ThrottledException **
The request exceeds the maximum number of requests per second.
HTTP Status Code: 429

## See Also
<a name="API_GetSamplingRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/GetSamplingRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/GetSamplingRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/GetSamplingRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/GetSamplingRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/GetSamplingRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/GetSamplingRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/GetSamplingRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/GetSamplingRules)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/GetSamplingRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/GetSamplingRules)
