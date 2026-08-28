---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeSessions.html
---

# DescribeSessions
<a name="API_DescribeSessions"></a>

Retrieves a list that describes the streaming sessions for a specified stack and fleet. If a UserId is provided for the stack and fleet, only streaming sessions for that user are described. If an authentication type is not provided, the default is to authenticate users using a streaming URL.

## Request Syntax
<a name="API_DescribeSessions_RequestSyntax"></a>

```
{
   "AuthenticationType": "{{string}}",
   "FleetName": "{{string}}",
   "InstanceId": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "StackName": "{{string}}",
   "UserId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeSessions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AuthenticationType](#API_DescribeSessions_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeSessions-request-AuthenticationType"></a>
The authentication method. Specify `API` for a user authenticated using a streaming URL or `SAML` for a SAML federated user. The default is to authenticate users using a streaming URL.
Type: String
Valid Values: `API | SAML | USERPOOL | AWS_AD`
Required: No

 ** [FleetName](#API_DescribeSessions_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeSessions-request-FleetName"></a>
The name of the fleet. This value is case-sensitive.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

 ** [InstanceId](#API_DescribeSessions_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeSessions-request-InstanceId"></a>
The identifier for the instance hosting the session.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [Limit](#API_DescribeSessions_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeSessions-request-Limit"></a>
The size of each page of results. The default value is 20 and the maximum value is 50.
Type: Integer
Required: No

 ** [NextToken](#API_DescribeSessions_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeSessions-request-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [StackName](#API_DescribeSessions_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeSessions-request-StackName"></a>
The name of the stack. This value is case-sensitive.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

 ** [UserId](#API_DescribeSessions_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeSessions-request-UserId"></a>
The user identifier (ID). If you specify a user ID, you must also specify the authentication type.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Required: No

## Response Syntax
<a name="API_DescribeSessions_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Sessions": [
      {
         "AuthenticationType": "string",
         "ConnectionState": "string",
         "FleetName": "string",
         "Id": "string",
         "InstanceDrainStatus": "string",
         "InstanceId": "string",
         "MaxExpirationTime": number,
         "NetworkAccessConfiguration": {
            "EniId": "string",
            "EniIpv6Addresses": [ "string" ],
            "EniPrivateIpAddress": "string"
         },
         "StackName": "string",
         "StartTime": number,
         "State": "string",
         "UserId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeSessions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeSessions_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeSessions-response-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
Type: String
Length Constraints: Minimum length of 1.

 ** [Sessions](#API_DescribeSessions_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeSessions-response-Sessions"></a>
Information about the streaming sessions.
Type: Array of [Session](API_Session.md) objects

## Errors
<a name="API_DescribeSessions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombinationException **
Indicates an incorrect combination of parameters, or a missing parameter.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_DescribeSessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/DescribeSessions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/DescribeSessions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/DescribeSessions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/DescribeSessions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/DescribeSessions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/DescribeSessions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/DescribeSessions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/DescribeSessions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/DescribeSessions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/DescribeSessions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
