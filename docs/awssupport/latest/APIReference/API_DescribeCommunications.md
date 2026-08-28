---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeCommunications.html
---

# DescribeCommunications
<a name="API_DescribeCommunications"></a>

Returns communications and attachments for one or more support cases. Use the `afterTime` and `beforeTime` parameters to filter by date. You can use the `caseId` parameter to restrict the results to a specific case.

Case data is available for 24 months after creation. If a case was created more than 24 months ago, a request for data might cause an error.

You can use the `maxResults` and `nextToken` parameters to control the pagination of the results. Set `maxResults` to the number of cases that you want to display on each page, and use `nextToken` to specify the resumption of pagination.

**Note**
You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the AWS Support API.
If you call the AWS Support API from an account that doesn't have a Business, Enterprise On-Ramp, or Enterprise Support plan, the `SubscriptionRequiredException` error message appears. For information about changing your support plan, see [AWS Support](http://aws.amazon.com/premiumsupport/).

## Request Syntax
<a name="API_DescribeCommunications_RequestSyntax"></a>

```
{
   "afterTime": "{{string}}",
   "beforeTime": "{{string}}",
   "caseId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeCommunications_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [afterTime](#API_DescribeCommunications_RequestSyntax) **   <a name="AWSSupport-DescribeCommunications-request-afterTime"></a>
The start date for a filtered date search on support case communications. Case communications are available for 24 months after creation.
Type: String

 ** [beforeTime](#API_DescribeCommunications_RequestSyntax) **   <a name="AWSSupport-DescribeCommunications-request-beforeTime"></a>
The end date for a filtered date search on support case communications. Case communications are available for 24 months after creation.
Type: String

 ** [caseId](#API_DescribeCommunications_RequestSyntax) **   <a name="AWSSupport-DescribeCommunications-request-caseId"></a>
The support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-*12345678910-exen-2025-c4c1d2bf33c5cf47*
Type: String

 ** [maxResults](#API_DescribeCommunications_RequestSyntax) **   <a name="AWSSupport-DescribeCommunications-request-maxResults"></a>
The maximum number of results to return before paginating.
Type: Integer
Valid Range: Minimum value of 10. Maximum value of 100.

 ** [nextToken](#API_DescribeCommunications_RequestSyntax) **   <a name="AWSSupport-DescribeCommunications-request-nextToken"></a>
A resumption point for pagination.
Type: String

## Response Syntax
<a name="API_DescribeCommunications_ResponseSyntax"></a>

```
{
   "communications": [
      {
         "attachmentSet": [
            {
               "attachmentId": "string",
               "fileName": "string"
            }
         ],
         "body": "string",
         "caseId": "string",
         "submittedBy": "string",
         "timeCreated": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeCommunications_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [communications](#API_DescribeCommunications_ResponseSyntax) **   <a name="AWSSupport-DescribeCommunications-response-communications"></a>
The communications for the case.
Type: Array of [Communication](API_Communication.md) objects

 ** [nextToken](#API_DescribeCommunications_ResponseSyntax) **   <a name="AWSSupport-DescribeCommunications-response-nextToken"></a>
A resumption point for pagination.
Type: String

## Errors
<a name="API_DescribeCommunications_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CaseIdNotFound **
The requested `caseId` couldn't be located.
 ** message **
The requested `CaseId` could not be located.
HTTP Status Code: 400

 ** InternalServerError **
An internal server error occurred.
 ** message **
An internal server error occurred.
HTTP Status Code: 500

## See Also
<a name="API_DescribeCommunications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/support-2013-04-15/DescribeCommunications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/support-2013-04-15/DescribeCommunications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/DescribeCommunications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/support-2013-04-15/DescribeCommunications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/DescribeCommunications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/support-2013-04-15/DescribeCommunications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/support-2013-04-15/DescribeCommunications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/support-2013-04-15/DescribeCommunications)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/support-2013-04-15/DescribeCommunications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/DescribeCommunications)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awssupport` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
