---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeCases.html
---

# DescribeCases
<a name="API_DescribeCases"></a>

Returns a list of cases that you specify by passing one or more case IDs. You can use the `afterTime` and `beforeTime` parameters to filter the cases by date. You can set values for the `includeResolvedCases` and `includeCommunications` parameters to specify how much information to return.

The response returns the following in JSON format:
+ One or more [CaseDetails](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_CaseDetails.html) data types.
+ One or more `nextToken` values, which specify where to paginate the returned records represented by the `CaseDetails` objects.

Case data is available for 24 months after creation. If a case was created more than 24 months ago, a request might return an error.

**Note**
You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the AWS Support API.
If you call the AWS Support API from an account that doesn't have a Business, Enterprise On-Ramp, or Enterprise Support plan, the `SubscriptionRequiredException` error message appears. For information about changing your support plan, see [AWS Support](http://aws.amazon.com/premiumsupport/).

## Request Syntax
<a name="API_DescribeCases_RequestSyntax"></a>

```
{
   "afterTime": "{{string}}",
   "beforeTime": "{{string}}",
   "caseIdList": [ "{{string}}" ],
   "displayId": "{{string}}",
   "includeCommunications": {{boolean}},
   "includeResolvedCases": {{boolean}},
   "language": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeCases_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [afterTime](#API_DescribeCases_RequestSyntax) **   <a name="AWSSupport-DescribeCases-request-afterTime"></a>
The start date for a filtered date search on support case communications. Case communications are available for 24 months after creation.
Type: String

 ** [beforeTime](#API_DescribeCases_RequestSyntax) **   <a name="AWSSupport-DescribeCases-request-beforeTime"></a>
The end date for a filtered date search on support case communications. Case communications are available for 24 months after creation.
Type: String

 ** [caseIdList](#API_DescribeCases_RequestSyntax) **   <a name="AWSSupport-DescribeCases-request-caseIdList"></a>
A list of ID numbers of the support cases you want returned. The maximum number of cases is 100.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [displayId](#API_DescribeCases_RequestSyntax) **   <a name="AWSSupport-DescribeCases-request-displayId"></a>
The ID displayed for a case in the AWS Support Center user interface.
Type: String

 ** [includeCommunications](#API_DescribeCases_RequestSyntax) **   <a name="AWSSupport-DescribeCases-request-includeCommunications"></a>
Specifies whether to include communications in the `DescribeCases` response. By default, communications are included.
Type: Boolean

 ** [includeResolvedCases](#API_DescribeCases_RequestSyntax) **   <a name="AWSSupport-DescribeCases-request-includeResolvedCases"></a>
Specifies whether to include resolved support cases in the `DescribeCases` response. By default, resolved cases aren't included.
Type: Boolean

 ** [language](#API_DescribeCases_RequestSyntax) **   <a name="AWSSupport-DescribeCases-request-language"></a>
The language in which AWS Support handles the case. AWS Support currently supports Chinese (“zh”), English ("en"), Japanese ("ja") , Chinese ("zh"), Spanish ("es"), Portuguese ("pt"), French ("fr"), Korean (“ko”), and Turkish ("tr"). You must specify the ISO 639-1 code for the `language` parameter if you want support in that language.
Type: String

 ** [maxResults](#API_DescribeCases_RequestSyntax) **   <a name="AWSSupport-DescribeCases-request-maxResults"></a>
The maximum number of results to return before paginating.
Type: Integer
Valid Range: Minimum value of 10. Maximum value of 100.

 ** [nextToken](#API_DescribeCases_RequestSyntax) **   <a name="AWSSupport-DescribeCases-request-nextToken"></a>
A resumption point for pagination.
Type: String

## Response Syntax
<a name="API_DescribeCases_ResponseSyntax"></a>

```
{
   "cases": [
      {
         "caseId": "string",
         "categoryCode": "string",
         "ccEmailAddresses": [ "string" ],
         "displayId": "string",
         "language": "string",
         "recentCommunications": {
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
         },
         "serviceCode": "string",
         "severityCode": "string",
         "status": "string",
         "subject": "string",
         "submittedBy": "string",
         "timeCreated": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeCases_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cases](#API_DescribeCases_ResponseSyntax) **   <a name="AWSSupport-DescribeCases-response-cases"></a>
The details for the cases that match the request.
Type: Array of [CaseDetails](API_CaseDetails.md) objects

 ** [nextToken](#API_DescribeCases_ResponseSyntax) **   <a name="AWSSupport-DescribeCases-response-nextToken"></a>
A resumption point for pagination.
Type: String

## Errors
<a name="API_DescribeCases_Errors"></a>

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
<a name="API_DescribeCases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/support-2013-04-15/DescribeCases)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/support-2013-04-15/DescribeCases)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/DescribeCases)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/support-2013-04-15/DescribeCases)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/DescribeCases)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/support-2013-04-15/DescribeCases)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/support-2013-04-15/DescribeCases)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/support-2013-04-15/DescribeCases)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/support-2013-04-15/DescribeCases)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/DescribeCases)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awssupport` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
