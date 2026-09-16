---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_DescribeRuleset.html
---

# DescribeRuleset
<a name="API_DescribeRuleset"></a>

Retrieves detailed information about the ruleset.

## Request Syntax
<a name="API_DescribeRuleset_RequestSyntax"></a>

```
GET /rulesets/{{name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeRuleset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_DescribeRuleset_RequestSyntax) **   <a name="databrew-DescribeRuleset-request-uri-Name"></a>
The name of the ruleset to be described.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Request Body
<a name="API_DescribeRuleset_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeRuleset_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreateDate": number,
   "CreatedBy": "string",
   "Description": "string",
   "LastModifiedBy": "string",
   "LastModifiedDate": number,
   "Name": "string",
   "ResourceArn": "string",
   "Rules": [
      {
         "CheckExpression": "string",
         "ColumnSelectors": [
            {
               "Name": "string",
               "Regex": "string"
            }
         ],
         "Disabled": boolean,
         "Name": "string",
         "SubstitutionMap": {
            "string" : "string"
         },
         "Threshold": {
            "Type": "string",
            "Unit": "string",
            "Value": number
         }
      }
   ],
   "Tags": {
      "string" : "string"
   },
   "TargetArn": "string"
}
```

## Response Elements
<a name="API_DescribeRuleset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_DescribeRuleset_ResponseSyntax) **   <a name="databrew-DescribeRuleset-response-Name"></a>
The name of the ruleset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [CreateDate](#API_DescribeRuleset_ResponseSyntax) **   <a name="databrew-DescribeRuleset-response-CreateDate"></a>
The date and time that the ruleset was created.
Type: Timestamp

 ** [CreatedBy](#API_DescribeRuleset_ResponseSyntax) **   <a name="databrew-DescribeRuleset-response-CreatedBy"></a>
The Amazon Resource Name (ARN) of the user who created the ruleset.
Type: String

 ** [Description](#API_DescribeRuleset_ResponseSyntax) **   <a name="databrew-DescribeRuleset-response-Description"></a>
The description of the ruleset.
Type: String
Length Constraints: Maximum length of 1024.

 ** [LastModifiedBy](#API_DescribeRuleset_ResponseSyntax) **   <a name="databrew-DescribeRuleset-response-LastModifiedBy"></a>
The Amazon Resource Name (ARN) of the user who last modified the ruleset.
Type: String

 ** [LastModifiedDate](#API_DescribeRuleset_ResponseSyntax) **   <a name="databrew-DescribeRuleset-response-LastModifiedDate"></a>
The modification date and time of the ruleset.
Type: Timestamp

 ** [ResourceArn](#API_DescribeRuleset_ResponseSyntax) **   <a name="databrew-DescribeRuleset-response-ResourceArn"></a>
The Amazon Resource Name (ARN) for the ruleset.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [Rules](#API_DescribeRuleset_ResponseSyntax) **   <a name="databrew-DescribeRuleset-response-Rules"></a>
A list of rules that are defined with the ruleset. A rule includes one or more checks to be validated on a DataBrew dataset.
Type: Array of [Rule](API_Rule.md) objects
Array Members: Minimum number of 1 item.

 ** [Tags](#API_DescribeRuleset_ResponseSyntax) **   <a name="databrew-DescribeRuleset-response-Tags"></a>
Metadata tags that have been applied to the ruleset.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.

 ** [TargetArn](#API_DescribeRuleset_ResponseSyntax) **   <a name="databrew-DescribeRuleset-response-TargetArn"></a>
The Amazon Resource Name (ARN) of a resource (dataset) that the ruleset is associated with.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

## Errors
<a name="API_DescribeRuleset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ValidationException **
The input parameters for this request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_DescribeRuleset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/DescribeRuleset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/DescribeRuleset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/DescribeRuleset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/DescribeRuleset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/DescribeRuleset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/DescribeRuleset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/DescribeRuleset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/DescribeRuleset)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/DescribeRuleset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/DescribeRuleset)
