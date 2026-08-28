---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_ListConfigurationCheckOperations.html
---

# ListConfigurationCheckOperations
<a name="API_ListConfigurationCheckOperations"></a>

Lists the configuration check operations performed by AWS Systems Manager for SAP.

## Request Syntax
<a name="API_ListConfigurationCheckOperations_RequestSyntax"></a>

```
POST /list-configuration-check-operations HTTP/1.1
Content-type: application/json

{
   "ApplicationId": "{{string}}",
   "Filters": [
      {
         "Name": "{{string}}",
         "Operator": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "ListMode": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListConfigurationCheckOperations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListConfigurationCheckOperations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ApplicationId](#API_ListConfigurationCheckOperations_RequestSyntax) **   <a name="ssmsap-ListConfigurationCheckOperations-request-ApplicationId"></a>
The ID of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[\w\d\.-]+`
Required: Yes

 ** [Filters](#API_ListConfigurationCheckOperations_RequestSyntax) **   <a name="ssmsap-ListConfigurationCheckOperations-request-Filters"></a>
The filters of an operation.
Type: Array of [Filter](API_Filter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [ListMode](#API_ListConfigurationCheckOperations_RequestSyntax) **   <a name="ssmsap-ListConfigurationCheckOperations-request-ListMode"></a>
The mode for listing configuration check operations. Defaults to "LATEST\_PER\_CHECK".
+ LATEST\_PER\_CHECK - Will list the latest configuration check operation per check type.
+ ALL\_OPERATIONS - Will list all configuration check operations performed on the application.
Type: String
Valid Values: `ALL_OPERATIONS | LATEST_PER_CHECK`
Required: No

 ** [MaxResults](#API_ListConfigurationCheckOperations_RequestSyntax) **   <a name="ssmsap-ListConfigurationCheckOperations-request-MaxResults"></a>
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListConfigurationCheckOperations_RequestSyntax) **   <a name="ssmsap-ListConfigurationCheckOperations-request-NextToken"></a>
The token for the next page of results.
Type: String
Pattern: `.{16,2048}`
Required: No

## Response Syntax
<a name="API_ListConfigurationCheckOperations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConfigurationCheckOperations": [
      {
         "ApplicationId": "string",
         "ConfigurationCheckDescription": "string",
         "ConfigurationCheckId": "string",
         "ConfigurationCheckName": "string",
         "EndTime": number,
         "Id": "string",
         "RuleStatusCounts": {
            "Failed": number,
            "Info": number,
            "Passed": number,
            "Unknown": number,
            "Warning": number
         },
         "StartTime": number,
         "Status": "string",
         "StatusMessage": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListConfigurationCheckOperations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConfigurationCheckOperations](#API_ListConfigurationCheckOperations_ResponseSyntax) **   <a name="ssmsap-ListConfigurationCheckOperations-response-ConfigurationCheckOperations"></a>
The configuration check operations performed by AWS Systems Manager for SAP.
Type: Array of [ConfigurationCheckOperation](API_ConfigurationCheckOperation.md) objects

 ** [NextToken](#API_ListConfigurationCheckOperations_ResponseSyntax) **   <a name="ssmsap-ListConfigurationCheckOperations-response-NextToken"></a>
The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String
Pattern: `.{16,2048}`

## Errors
<a name="API_ListConfigurationCheckOperations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource is not available.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListConfigurationCheckOperations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-sap-2018-05-10/ListConfigurationCheckOperations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-sap-2018-05-10/ListConfigurationCheckOperations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/ListConfigurationCheckOperations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-sap-2018-05-10/ListConfigurationCheckOperations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/ListConfigurationCheckOperations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-sap-2018-05-10/ListConfigurationCheckOperations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-sap-2018-05-10/ListConfigurationCheckOperations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-sap-2018-05-10/ListConfigurationCheckOperations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-sap-2018-05-10/ListConfigurationCheckOperations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/ListConfigurationCheckOperations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager for SAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ssmsap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
