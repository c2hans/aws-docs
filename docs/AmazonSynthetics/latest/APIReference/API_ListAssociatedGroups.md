---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_ListAssociatedGroups.html
---

# ListAssociatedGroups
<a name="API_ListAssociatedGroups"></a>

Returns a list of the groups that the specified canary is associated with. The canary that you specify must be in the current Region.

## Request Syntax
<a name="API_ListAssociatedGroups_RequestSyntax"></a>

```
POST /resource/{{resourceArn}}/groups HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListAssociatedGroups_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_ListAssociatedGroups_RequestSyntax) **   <a name="synthetics-ListAssociatedGroups-request-uri-ResourceArn"></a>
The ARN of the canary that you want to view groups for.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:synthetics:[a-z]{2,4}(-[a-z]{2,4})?-[a-z]+-\d{1}:\d{12}:canary:[0-9a-z_\-]{1,255}`
Required: Yes

## Request Body
<a name="API_ListAssociatedGroups_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListAssociatedGroups_RequestSyntax) **   <a name="synthetics-ListAssociatedGroups-request-MaxResults"></a>
Specify this parameter to limit how many groups are returned each time you use the `ListAssociatedGroups` operation. If you omit this parameter, the default of 20 is used.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: No

 ** [NextToken](#API_ListAssociatedGroups_RequestSyntax) **   <a name="synthetics-ListAssociatedGroups-request-NextToken"></a>
A token that indicates that there is more data available. You can use this token in a subsequent operation to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^.+$`
Required: No

## Response Syntax
<a name="API_ListAssociatedGroups_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Groups": [
      {
         "Arn": "string",
         "Id": "string",
         "Name": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAssociatedGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Groups](#API_ListAssociatedGroups_ResponseSyntax) **   <a name="synthetics-ListAssociatedGroups-response-Groups"></a>
An array of structures that contain information about the groups that this canary is associated with.
Type: Array of [GroupSummary](API_GroupSummary.md) objects

 ** [NextToken](#API_ListAssociatedGroups_ResponseSyntax) **   <a name="synthetics-ListAssociatedGroups-response-NextToken"></a>
A token that indicates that there is more data available. You can use this token in a subsequent `ListAssociatedGroups` operation to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^.+$`

## Errors
<a name="API_ListAssociatedGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An unknown internal error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
One of the specified resources was not found.
HTTP Status Code: 404

 ** ValidationException **
A parameter could not be validated.
HTTP Status Code: 400

## See Also
<a name="API_ListAssociatedGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/synthetics-2017-10-11/ListAssociatedGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/synthetics-2017-10-11/ListAssociatedGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/ListAssociatedGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/synthetics-2017-10-11/ListAssociatedGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/ListAssociatedGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/synthetics-2017-10-11/ListAssociatedGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/synthetics-2017-10-11/ListAssociatedGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/synthetics-2017-10-11/ListAssociatedGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/synthetics-2017-10-11/ListAssociatedGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/ListAssociatedGroups)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Synthetics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSynthetics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
