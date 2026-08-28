---
source_url: https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListControls.html
---

# ListControls
<a name="API_ListControls"></a>

Returns a paginated list of all available controls in the Control Catalog library. Allows you to discover available controls. The list of controls is given as structures of type *controlSummary*. The ARN is returned in the global *controlcatalog* format, as shown in the examples.

## Request Syntax
<a name="API_ListControls_RequestSyntax"></a>

```
POST /list-controls?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
Content-type: application/json

{
   "Filter": {
      "GovernedProviders": [ "{{string}}" ],
      "Implementations": {
         "Identifiers": [ "{{string}}" ],
         "Types": [ "{{string}}" ]
      }
   }
}
```

## URI Request Parameters
<a name="API_ListControls_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListControls_RequestSyntax) **   <a name="controlcatalog-ListControls-request-uri-MaxResults"></a>
The maximum number of results on a page or for an API request call.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListControls_RequestSyntax) **   <a name="controlcatalog-ListControls-request-uri-NextToken"></a>
The pagination token that's used to fetch the next set of results.
Length Constraints: Minimum length of 0. Maximum length of 1024.

## Request Body
<a name="API_ListControls_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filter](#API_ListControls_RequestSyntax) **   <a name="controlcatalog-ListControls-request-Filter"></a>
An optional filter that narrows the results to controls with specific implementation types or identifiers. If you don't provide a filter, the operation returns all available controls.
Type: [ControlFilter](API_ControlFilter.md) object
Required: No

## Response Syntax
<a name="API_ListControls_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Controls": [
      {
         "Aliases": [ "string" ],
         "Arn": "string",
         "Behavior": "string",
         "CreateTime": number,
         "Description": "string",
         "GovernedProviders": [ "string" ],
         "GovernedResources": [ "string" ],
         "Implementation": {
            "Identifier": "string",
            "Type": "string"
         },
         "Name": "string",
         "ParameterRequirementSummary": "string",
         "Severity": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListControls_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Controls](#API_ListControls_ResponseSyntax) **   <a name="controlcatalog-ListControls-response-Controls"></a>
Returns a list of controls, given as structures of type *controlSummary*.
Type: Array of [ControlSummary](API_ControlSummary.md) objects

 ** [NextToken](#API_ListControls_ResponseSyntax) **   <a name="controlcatalog-ListControls-response-NextToken"></a>
The pagination token that's used to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

## Errors
<a name="API_ListControls_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request has invalid or missing parameters.
HTTP Status Code: 400

## Examples
<a name="API_ListControls_Examples"></a>

### Retrieve a list of controls
<a name="API_ListControls_Example_1"></a>

Use this operation to retrieve a paginated list of available controls, by Region.

#### Sample Request
<a name="API_ListControls_Example_1_Request"></a>

```
aws controlcatalog list-controls --max-result 2 --region us-east-1
```

#### Sample Response
<a name="API_ListControls_Example_1_Response"></a>

```
{
    "Controls": [
        {
            "Arn": "arn:aws:controlcatalog:::control/m7a5gbdf08wg2o0en010mkng",
            "Aliases": [
                "BACKUP_RECOVERY_POINT_MINIMUM_RETENTION_CHECK"
            ],
            "Name": "Checks if a recovery point expires no earlier than after the specified period",
            "Description": "Checks if a recovery point expires no earlier than after the specified period. The rule is NON_COMPLIANT if the recovery point has a retention point that is less than the required retention period.",
            "Behavior": "DETECTIVE",
            "Severity": "MEDIUM",
            "Implementation": {
                "Type": "AWS::Config::ConfigRule",
                "Identifier": "BACKUP_RECOVERY_POINT_MINIMUM_RETENTION_CHECK"
            },
            "CreateTime": "2021-07-22T17:00:00-07:00",
            "GovernedResources": []
        },
        {
            "Arn": "arn:aws:controlcatalog:::control/4b0nsxnd47747up54ytdqesxi",
            "Aliases": [
                "CT.CODEBUILD.PR.3"
            ],
            "Name": "Require any AWS CodeBuild project environment to have logging configured",
            "Description": "This control checks whether AWS CodeBuild projects environment has at least one logging option enabled.",
            "Behavior": "PROACTIVE",
            "Severity": "MEDIUM",
            "Implementation": {
                "Type": "AWS::CloudFormation::Type::HOOK"
            },
            "CreateTime": "2022-11-27T16:00:00-08:00",
            "GovernedResources": [
                "AWS::CodeBuild::Project"
            ]
        }
    ],
    "NextToken": "..."
}
```

### Retrieve a list of controls with a filter
<a name="API_ListControls_Example_2"></a>

Use this operation to retrieve a paginated list of available controls, filtered by identifier and implementation type.

#### Sample Request
<a name="API_ListControls_Example_2_Request"></a>

```
aws controlcatalog list-controls --filter "{\"Implementations\":{\"Identifiers\":[\"CODEPIPELINE_DEPLOYMENT_COUNT_CHECK\"], \"Types\":[\"AWS::Config::ConfigRule\"]}}" --region us-east-1
```

#### Sample Response
<a name="API_ListControls_Example_2_Response"></a>

```
{
    "Controls": [
        {
            "Arn": "arn:aws:controlcatalog:::control/8k65jh499ji8qa5tb3it7tdi5",
            "Aliases": [
                "CONFIG.CODEPIPELINE.DT.1"
            ],
            "Name": "Checks if the first deployment stage of AWS CodePipeline performs more than one deployment",
            "Description": "Checks if the first deployment stage of AWS CodePipeline performs more than one deployment. Optionally checks if each of the subsequent remaining stages deploy to more than the specified number of deployments (deploymentLimit).",
            "Behavior": "DETECTIVE",
            "Severity": "MEDIUM",
            "Implementation": {
                "Type": "AWS::Config::ConfigRule",
                "Identifier": "CODEPIPELINE_DEPLOYMENT_COUNT_CHECK"
            },
            "CreateTime": "2018-10-31T17:00:00-07:00",
            "GovernedResources": ["AWS::CodePipeline::Pipeline"]
        }
    ]
}
```

## See Also
<a name="API_ListControls_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/controlcatalog-2018-05-10/ListControls)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/controlcatalog-2018-05-10/ListControls)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controlcatalog-2018-05-10/ListControls)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/controlcatalog-2018-05-10/ListControls)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controlcatalog-2018-05-10/ListControls)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/controlcatalog-2018-05-10/ListControls)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/controlcatalog-2018-05-10/ListControls)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/controlcatalog-2018-05-10/ListControls)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/controlcatalog-2018-05-10/ListControls)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controlcatalog-2018-05-10/ListControls)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controlcatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
