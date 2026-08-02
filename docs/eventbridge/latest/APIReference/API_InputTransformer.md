---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_InputTransformer.html
---

# InputTransformer
<a name="API_InputTransformer"></a>

Contains the parameters needed for you to provide custom input to a target based on one or more pieces of data extracted from the event.

## Contents
<a name="API_InputTransformer_Contents"></a>

 ** InputTemplate **   <a name="eventbridge-Type-InputTransformer-InputTemplate"></a>
Input template where you specify placeholders that will be filled with the values of the keys from `InputPathsMap` to customize the data sent to the target. Enclose each `InputPathsMaps` value in brackets: <*value*>
If `InputTemplate` is a JSON object (surrounded by curly braces), the following restrictions apply:
+ The placeholder cannot be used as an object key.
The following example shows the syntax for using `InputPathsMap` and `InputTemplate`.
 ` "InputTransformer":`
 `{`
 `"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},`
 `"InputTemplate": "<instance> is in state <status>"`
 `}`
To have the `InputTemplate` include quote marks within a JSON string, escape each quote marks with a slash, as in the following example:
 ` "InputTransformer":`
 `{`
 `"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},`
 `"InputTemplate": "<instance> is in state \"<status>\""`
 `}`
The `InputTemplate` can also be valid JSON with varibles in quotes or out, as in the following example:
 ` "InputTransformer":`
 `{`
 `"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},`
 `"InputTemplate": '{"myInstance": <instance>,"myStatus": "<instance> is in state \"<status>\""}'`
 `}`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: Yes

 ** InputPathsMap **   <a name="eventbridge-Type-InputTransformer-InputPathsMap"></a>
Map of JSON paths to be extracted from the event. You can then insert these in the template in `InputTemplate` to produce the output you want to be sent to the target.
 `InputPathsMap` is an array key-value pairs, where each value is a valid JSON path. You can have as many as 100 key-value pairs. You must use JSON dot notation, not bracket notation.
The keys cannot start with "AWS."
Type: String to string map
Map Entries: Maximum number of 100 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[A-Za-z0-9\_\-]+`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_InputTransformer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/InputTransformer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/InputTransformer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/InputTransformer)
