---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeStacks.html
---

# DescribeStacks
<a name="API_DescribeStacks"></a>

Retrieves a list that describes one or more specified stacks, if the stack names are provided. Otherwise, all stacks in the account are described.

## Request Syntax
<a name="API_DescribeStacks_RequestSyntax"></a>

```
{
   "Names": [ "{{string}}" ],
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeStacks_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Names](#API_DescribeStacks_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeStacks-request-Names"></a>
The names of the stacks to describe.
Type: Array of strings
Length Constraints: Minimum length of 1.
Required: No

 ** [NextToken](#API_DescribeStacks_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeStacks-request-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_DescribeStacks_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Stacks": [
      {
         "AccessEndpoints": [
            {
               "EndpointType": "string",
               "VpceId": "string"
            }
         ],
         "AgentAccessConfig": {
            "S3BucketArn": "string",
            "ScreenImageFormat": "string",
            "ScreenResolution": "string",
            "ScreenshotsUploadEnabled": boolean,
            "Settings": [
               {
                  "AgentAction": "string",
                  "Permission": "string"
               }
            ],
            "UserControlMode": "string"
         },
         "ApplicationSettings": {
            "Enabled": boolean,
            "S3BucketName": "string",
            "SettingsGroup": "string"
         },
         "Arn": "string",
         "CreatedTime": number,
         "Description": "string",
         "DisplayName": "string",
         "EmbedHostDomains": [ "string" ],
         "FeedbackURL": "string",
         "Name": "string",
         "RedirectURL": "string",
         "StackErrors": [
            {
               "ErrorCode": "string",
               "ErrorMessage": "string"
            }
         ],
         "StorageConnectors": [
            {
               "ConnectorType": "string",
               "Domains": [ "string" ],
               "DomainsRequireAdminConsent": [ "string" ],
               "ResourceIdentifier": "string"
            }
         ],
         "StreamingExperienceSettings": {
            "PreferredProtocol": "string"
         },
         "UserSettings": [
            {
               "Action": "string",
               "MaximumLength": number,
               "Permission": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_DescribeStacks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeStacks_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeStacks-response-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
Type: String
Length Constraints: Minimum length of 1.

 ** [Stacks](#API_DescribeStacks_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeStacks-response-Stacks"></a>
Information about the stacks.
Type: Array of [Stack](API_Stack.md) objects

## Errors
<a name="API_DescribeStacks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_DescribeStacks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/DescribeStacks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/DescribeStacks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/DescribeStacks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/DescribeStacks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/DescribeStacks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/DescribeStacks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/DescribeStacks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/DescribeStacks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/DescribeStacks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/DescribeStacks)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
