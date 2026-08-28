---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_UpdateRuleset.html
---

# UpdateRuleset
<a name="API_UpdateRuleset"></a>

Updates specified ruleset.

## Request Syntax
<a name="API_UpdateRuleset_RequestSyntax"></a>

```
PUT /rulesets/{{name}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
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
   ]
}
```

## URI Request Parameters
<a name="API_UpdateRuleset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_UpdateRuleset_RequestSyntax) **   <a name="databrew-UpdateRuleset-request-uri-Name"></a>
The name of the ruleset to be updated.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Request Body
<a name="API_UpdateRuleset_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Rules](#API_UpdateRuleset_RequestSyntax) **   <a name="databrew-UpdateRuleset-request-Rules"></a>
A list of rules that are defined with the ruleset. A rule includes one or more checks to be validated on a DataBrew dataset.
Type: Array of [Rule](API_Rule.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** [Description](#API_UpdateRuleset_RequestSyntax) **   <a name="databrew-UpdateRuleset-request-Description"></a>
The description of the ruleset.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_UpdateRuleset_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Name": "string"
}
```

## Response Elements
<a name="API_UpdateRuleset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_UpdateRuleset_ResponseSyntax) **   <a name="databrew-UpdateRuleset-response-Name"></a>
The name of the updated ruleset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_UpdateRuleset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ValidationException **
The input parameters for this request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_UpdateRuleset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/UpdateRuleset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/UpdateRuleset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/UpdateRuleset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/UpdateRuleset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/UpdateRuleset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/UpdateRuleset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/UpdateRuleset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/UpdateRuleset)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/UpdateRuleset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/UpdateRuleset)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
