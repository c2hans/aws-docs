---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_CreateRuleset.html
---

# CreateRuleset
<a name="API_CreateRuleset"></a>

Creates a new ruleset that can be used in a profile job to validate the data quality of a dataset.

## Request Syntax
<a name="API_CreateRuleset_RequestSyntax"></a>

```
POST /rulesets HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Name": "{{string}}",
   "Rules": [
      {
         "CheckExpression": "{{string}}",
         "ColumnSelectors": [
            {
               "Name": "{{string}}",
               "Regex": "{{string}}"
            }
         ],
         "Disabled": {{boolean}},
         "Name": "{{string}}",
         "SubstitutionMap": {
            "{{string}}" : "{{string}}"
         },
         "Threshold": {
            "Type": "{{string}}",
            "Unit": "{{string}}",
            "Value": {{number}}
         }
      }
   ],
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "TargetArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateRuleset_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateRuleset_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_CreateRuleset_RequestSyntax) **   <a name="databrew-CreateRuleset-request-Name"></a>
The name of the ruleset to be created. Valid characters are alphanumeric (A-Z, a-z, 0-9), hyphen (-), period (.), and space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [Rules](#API_CreateRuleset_RequestSyntax) **   <a name="databrew-CreateRuleset-request-Rules"></a>
A list of rules that are defined with the ruleset. A rule includes one or more checks to be validated on a DataBrew dataset.
Type: Array of [Rule](API_Rule.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** [TargetArn](#API_CreateRuleset_RequestSyntax) **   <a name="databrew-CreateRuleset-request-TargetArn"></a>
The Amazon Resource Name (ARN) of a resource (dataset) that the ruleset is associated with.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** [Description](#API_CreateRuleset_RequestSyntax) **   <a name="databrew-CreateRuleset-request-Description"></a>
The description of the ruleset.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** [Tags](#API_CreateRuleset_RequestSyntax) **   <a name="databrew-CreateRuleset-request-Tags"></a>
Metadata tags to apply to the ruleset.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateRuleset_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Name": "string"
}
```

## Response Elements
<a name="API_CreateRuleset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_CreateRuleset_ResponseSyntax) **   <a name="databrew-CreateRuleset-response-Name"></a>
The unique name of the created ruleset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_CreateRuleset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** ServiceQuotaExceededException **
A service quota is exceeded.
HTTP Status Code: 402

 ** ValidationException **
The input parameters for this request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_CreateRuleset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/CreateRuleset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/CreateRuleset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/CreateRuleset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/CreateRuleset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/CreateRuleset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/CreateRuleset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/CreateRuleset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/CreateRuleset)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/CreateRuleset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/CreateRuleset)
