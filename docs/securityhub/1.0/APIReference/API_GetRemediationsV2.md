---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetRemediationsV2.html
---

# GetRemediationsV2
<a name="API_GetRemediationsV2"></a>

Retrieves remediation targets for the account, or for all member accounts if the caller is the delegated administrator. Results are sorted by priority, highest first, and are paginated. Use `TargetUid` or `MetadataUid` to scope the request to a single target or finding.

## Request Syntax
<a name="API_GetRemediationsV2_RequestSyntax"></a>

```
POST /GetRemediationsV2 HTTP/1.1
Content-type: application/json

{
   "Filters": {
      "CompositeFilters": [
         {
            "StringFilters": [
               {
                  "FieldName": "{{string}}",
                  "Filter": {
                     "Value": "{{string}}"
                  }
               }
            ]
         }
      ]
   },
   "GuidanceFormat": "{{string}}",
   "MaxResults": {{number}},
   "MetadataUid": "{{string}}",
   "NextToken": "{{string}}",
   "ShowGuidance": {{boolean}},
   "TargetUid": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetRemediationsV2_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetRemediationsV2_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_GetRemediationsV2_RequestSyntax) **   <a name="securityhub-GetRemediationsV2-request-Filters"></a>
Filters remediation targets based on a set of criteria. You can't use `Filters` together with `TargetUid` or `MetadataUid`.
Type: [RemediationFilters](API_RemediationFilters.md) object
Required: No

 ** [GuidanceFormat](#API_GetRemediationsV2_RequestSyntax) **   <a name="securityhub-GetRemediationsV2-request-GuidanceFormat"></a>
The format of the remediation guidance examples to return. Valid values are `All`, `AwsCli`, `Cli`, `Python`, `Terraform`, `Cdk`, `CloudFormation`, `IaC`, and `Template`. If you don't specify a value, all formats are returned. Applies only when `ShowGuidance` is `true`.
Type: String
Valid Values: `All | AwsCli | Cli | Python | Terraform | Cdk | CloudFormation | IaC | Template`
Required: No

 ** [MaxResults](#API_GetRemediationsV2_RequestSyntax) **   <a name="securityhub-GetRemediationsV2-request-MaxResults"></a>
The maximum number of results to return. Valid range is 1-100. If you don't specify a value, the operation returns up to 25 results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [MetadataUid](#API_GetRemediationsV2_RequestSyntax) **   <a name="securityhub-GetRemediationsV2-request-MetadataUid"></a>
The unique identifier (ID) of the Security Hub exposure finding, found under the `metadata.uid` field of the finding. Returns the remediation targets associated with that finding. You can't use `MetadataUid` together with `TargetUid` or `Filters`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [NextToken](#API_GetRemediationsV2_RequestSyntax) **   <a name="securityhub-GetRemediationsV2-request-NextToken"></a>
The token used to paginate the remediations target list returned. On your first call to `GetRemediationsV2`, omit this parameter or set it to `NULL`. For subsequent calls, use the `NextToken` value returned in the previous response to retrieve the next page of results.
Type: String
Required: No

 ** [ShowGuidance](#API_GetRemediationsV2_RequestSyntax) **   <a name="securityhub-GetRemediationsV2-request-ShowGuidance"></a>
Specifies whether to show remediation target guidance.
Type: Boolean
Required: No

 ** [TargetUid](#API_GetRemediationsV2_RequestSyntax) **   <a name="securityhub-GetRemediationsV2-request-TargetUid"></a>
The unique identifier (ID) of an existing remediation target to return. Returns the single matching target. You can't use `TargetUid` together with `MetadataUid` or `Filters`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_GetRemediationsV2_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "Guidance": {
            "Context": {
               "AffectedScope": "string",
               "Prerequisites": [ "string" ],
               "ProblemStatement": "string",
               "RiskAssessment": "string"
            },
            "Examples": {
               "AwsCli": "string",
               "Cdk": "string",
               "Cli": "string",
               "CloudFormation": "string",
               "IaC": "string",
               "Python": "string",
               "Template": "string",
               "Terraform": "string"
            },
            "Metadata": {
               "AutomationLevel": "string",
               "ExposureType": "string",
               "FixEffect": "string",
               "GeneratedAt": "string",
               "HumanReviewRequired": boolean,
               "ResourceType": "string",
               "Reversibility": "string",
               "RiskLevel": "string",
               "TraitTitles": [ "string" ],
               "VerificationStatus": "string"
            },
            "Pattern": "string",
            "Specification": {
               "ExpectedEndState": "string",
               "Parameters": [
                  {
                     "Description": "string",
                     "Name": "string",
                     "Required": boolean,
                     "Type": "string"
                  }
               ],
               "RequiredPermissions": [ "string" ],
               "Steps": [
                  {
                     "Action": "string",
                     "Description": "string",
                     "Inverse": "string",
                     "Logic": "string",
                     "Phase": "string",
                     "Service": "string",
                     "VerifyAfter": "string"
                  }
               ]
            },
            "TargetTypeName": "string",
            "Version": "string"
         },
         "Outcome": {
            "ResolvedFindingsCount": number,
            "SeverityReductionFindingsCount": number,
            "SeverityUnchangedCount": number
         },
         "Priority": "string",
         "RemediationSummary": {
            "Action": "string",
            "Description": "string",
            "IsImmediate": boolean,
            "KbArticles": [
               {
                  "Title": "string",
                  "Url": "string"
               }
            ],
            "PostRemediationSteps": [ "string" ]
         },
         "Resource": {
            "AccountId": "string",
            "CloudProvider": "string",
            "Id": "string",
            "Name": "string",
            "Region": "string",
            "ResourceGuid": "string",
            "ResourceOwnerAccountId": "string",
            "ResourceOwnerOrgId": "string",
            "ResourceRegion": "string",
            "Type": "string"
         },
         "Status": "string",
         "TargetUid": "string",
         "Trait": {
            "Title": "string",
            "Type": "string"
         },
         "UpdatedAt": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetRemediationsV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_GetRemediationsV2_ResponseSyntax) **   <a name="securityhub-GetRemediationsV2-response-Items"></a>
An array of remediation targets returned by the operation.
Type: Array of [RemediationV2Item](API_RemediationV2Item.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [NextToken](#API_GetRemediationsV2_ResponseSyntax) **   <a name="securityhub-GetRemediationsV2-response-NextToken"></a>
The pagination token to use to request the next page of results. Otherwise, this parameter is null.
Type: String

## Errors
<a name="API_GetRemediationsV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** InternalServerException **
 The request has failed due to an internal failure of the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

 ** ThrottlingException **
 The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation because it's missing required fields or has invalid inputs.
HTTP Status Code: 400

## See Also
<a name="API_GetRemediationsV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/GetRemediationsV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/GetRemediationsV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/GetRemediationsV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/GetRemediationsV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/GetRemediationsV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/GetRemediationsV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/GetRemediationsV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/GetRemediationsV2)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/GetRemediationsV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/GetRemediationsV2)
