---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateInsight.html
---

# UpdateInsight
<a name="API_UpdateInsight"></a>

Updates the Security Hub CSPM insight identified by the specified insight ARN.

## Request Syntax
<a name="API_UpdateInsight_RequestSyntax"></a>

```
PATCH /insights/{{InsightArn+}} HTTP/1.1
Content-type: application/json

{
   "Filters": {
      "AwsAccountId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "AwsAccountName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "CompanyName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ComplianceAssociatedStandardsId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ComplianceSecurityControlId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ComplianceSecurityControlParametersName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ComplianceSecurityControlParametersValue": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ComplianceStatus": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "Confidence": [
         {
            "Eq": {{number}},
            "Gt": {{number}},
            "Gte": {{number}},
            "Lt": {{number}},
            "Lte": {{number}}
         }
      ],
      "CreatedAt": [
         {
            "DateRange": {
               "Comparison": "{{string}}",
               "Unit": "{{string}}",
               "Value": {{number}}
            },
            "End": "{{string}}",
            "Start": "{{string}}"
         }
      ],
      "Criticality": [
         {
            "Eq": {{number}},
            "Gt": {{number}},
            "Gte": {{number}},
            "Lt": {{number}},
            "Lte": {{number}}
         }
      ],
      "Description": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "FindingProviderFieldsConfidence": [
         {
            "Eq": {{number}},
            "Gt": {{number}},
            "Gte": {{number}},
            "Lt": {{number}},
            "Lte": {{number}}
         }
      ],
      "FindingProviderFieldsCriticality": [
         {
            "Eq": {{number}},
            "Gt": {{number}},
            "Gte": {{number}},
            "Lt": {{number}},
            "Lte": {{number}}
         }
      ],
      "FindingProviderFieldsRelatedFindingsId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "FindingProviderFieldsRelatedFindingsProductArn": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "FindingProviderFieldsSeverityLabel": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "FindingProviderFieldsSeverityOriginal": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "FindingProviderFieldsTypes": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "FirstObservedAt": [
         {
            "DateRange": {
               "Comparison": "{{string}}",
               "Unit": "{{string}}",
               "Value": {{number}}
            },
            "End": "{{string}}",
            "Start": "{{string}}"
         }
      ],
      "GeneratorId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "Id": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "Keyword": [
         {
            "Value": "{{string}}"
         }
      ],
      "LastObservedAt": [
         {
            "DateRange": {
               "Comparison": "{{string}}",
               "Unit": "{{string}}",
               "Value": {{number}}
            },
            "End": "{{string}}",
            "Start": "{{string}}"
         }
      ],
      "MalwareName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "MalwarePath": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "MalwareState": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "MalwareType": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "NetworkDestinationDomain": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "NetworkDestinationIpV4": [
         {
            "Cidr": "{{string}}"
         }
      ],
      "NetworkDestinationIpV6": [
         {
            "Cidr": "{{string}}"
         }
      ],
      "NetworkDestinationPort": [
         {
            "Eq": {{number}},
            "Gt": {{number}},
            "Gte": {{number}},
            "Lt": {{number}},
            "Lte": {{number}}
         }
      ],
      "NetworkDirection": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "NetworkProtocol": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "NetworkSourceDomain": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "NetworkSourceIpV4": [
         {
            "Cidr": "{{string}}"
         }
      ],
      "NetworkSourceIpV6": [
         {
            "Cidr": "{{string}}"
         }
      ],
      "NetworkSourceMac": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "NetworkSourcePort": [
         {
            "Eq": {{number}},
            "Gt": {{number}},
            "Gte": {{number}},
            "Lt": {{number}},
            "Lte": {{number}}
         }
      ],
      "NoteText": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "NoteUpdatedAt": [
         {
            "DateRange": {
               "Comparison": "{{string}}",
               "Unit": "{{string}}",
               "Value": {{number}}
            },
            "End": "{{string}}",
            "Start": "{{string}}"
         }
      ],
      "NoteUpdatedBy": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ProcessLaunchedAt": [
         {
            "DateRange": {
               "Comparison": "{{string}}",
               "Unit": "{{string}}",
               "Value": {{number}}
            },
            "End": "{{string}}",
            "Start": "{{string}}"
         }
      ],
      "ProcessName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ProcessParentPid": [
         {
            "Eq": {{number}},
            "Gt": {{number}},
            "Gte": {{number}},
            "Lt": {{number}},
            "Lte": {{number}}
         }
      ],
      "ProcessPath": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ProcessPid": [
         {
            "Eq": {{number}},
            "Gt": {{number}},
            "Gte": {{number}},
            "Lt": {{number}},
            "Lte": {{number}}
         }
      ],
      "ProcessTerminatedAt": [
         {
            "DateRange": {
               "Comparison": "{{string}}",
               "Unit": "{{string}}",
               "Value": {{number}}
            },
            "End": "{{string}}",
            "Start": "{{string}}"
         }
      ],
      "ProductArn": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ProductFields": [
         {
            "Comparison": "{{string}}",
            "Key": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ProductName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "RecommendationText": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "RecordState": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "Region": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "RelatedFindingsId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "RelatedFindingsProductArn": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceApplicationArn": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceApplicationName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceAwsEc2InstanceIamInstanceProfileArn": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceAwsEc2InstanceImageId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceAwsEc2InstanceIpV4Addresses": [
         {
            "Cidr": "{{string}}"
         }
      ],
      "ResourceAwsEc2InstanceIpV6Addresses": [
         {
            "Cidr": "{{string}}"
         }
      ],
      "ResourceAwsEc2InstanceKeyName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceAwsEc2InstanceLaunchedAt": [
         {
            "DateRange": {
               "Comparison": "{{string}}",
               "Unit": "{{string}}",
               "Value": {{number}}
            },
            "End": "{{string}}",
            "Start": "{{string}}"
         }
      ],
      "ResourceAwsEc2InstanceSubnetId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceAwsEc2InstanceType": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceAwsEc2InstanceVpcId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceAwsIamAccessKeyCreatedAt": [
         {
            "DateRange": {
               "Comparison": "{{string}}",
               "Unit": "{{string}}",
               "Value": {{number}}
            },
            "End": "{{string}}",
            "Start": "{{string}}"
         }
      ],
      "ResourceAwsIamAccessKeyPrincipalName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceAwsIamAccessKeyStatus": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceAwsIamAccessKeyUserName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceAwsIamUserUserName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceAwsS3BucketOwnerId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceAwsS3BucketOwnerName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceContainerImageId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceContainerImageName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceContainerLaunchedAt": [
         {
            "DateRange": {
               "Comparison": "{{string}}",
               "Unit": "{{string}}",
               "Value": {{number}}
            },
            "End": "{{string}}",
            "Start": "{{string}}"
         }
      ],
      "ResourceContainerName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceDetailsOther": [
         {
            "Comparison": "{{string}}",
            "Key": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceOwnerAccountId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceOwnerOrgId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourcePartition": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceProvider": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceRegion": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceTags": [
         {
            "Comparison": "{{string}}",
            "Key": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceType": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "Sample": [
         {
            "Value": {{boolean}}
         }
      ],
      "SeverityLabel": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "SeverityNormalized": [
         {
            "Eq": {{number}},
            "Gt": {{number}},
            "Gte": {{number}},
            "Lt": {{number}},
            "Lte": {{number}}
         }
      ],
      "SeverityProduct": [
         {
            "Eq": {{number}},
            "Gt": {{number}},
            "Gte": {{number}},
            "Lt": {{number}},
            "Lte": {{number}}
         }
      ],
      "SourceUrl": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ThreatIntelIndicatorCategory": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ThreatIntelIndicatorLastObservedAt": [
         {
            "DateRange": {
               "Comparison": "{{string}}",
               "Unit": "{{string}}",
               "Value": {{number}}
            },
            "End": "{{string}}",
            "Start": "{{string}}"
         }
      ],
      "ThreatIntelIndicatorSource": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ThreatIntelIndicatorSourceUrl": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ThreatIntelIndicatorType": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ThreatIntelIndicatorValue": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "Title": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "Type": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "UpdatedAt": [
         {
            "DateRange": {
               "Comparison": "{{string}}",
               "Unit": "{{string}}",
               "Value": {{number}}
            },
            "End": "{{string}}",
            "Start": "{{string}}"
         }
      ],
      "UserDefinedFields": [
         {
            "Comparison": "{{string}}",
            "Key": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "VerificationState": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "VulnerabilitiesExploitAvailable": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "VulnerabilitiesFixAvailable": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "WorkflowState": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "WorkflowStatus": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ]
   },
   "GroupByAttribute": "{{string}}",
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateInsight_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InsightArn](#API_UpdateInsight_RequestSyntax) **   <a name="securityhub-UpdateInsight-request-uri-InsightArn"></a>
The ARN of the insight that you want to update.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_UpdateInsight_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_UpdateInsight_RequestSyntax) **   <a name="securityhub-UpdateInsight-request-Filters"></a>
The updated filters that define this insight.
Type: [AwsSecurityFindingFilters](API_AwsSecurityFindingFilters.md) object
Required: No

 ** [GroupByAttribute](#API_UpdateInsight_RequestSyntax) **   <a name="securityhub-UpdateInsight-request-GroupByAttribute"></a>
The updated `GroupBy` attribute that defines this insight.
Type: String
Pattern: `.*\S.*`
Required: No

 ** [Name](#API_UpdateInsight_RequestSyntax) **   <a name="securityhub-UpdateInsight-request-Name"></a>
The updated name for the insight.
Type: String
Pattern: `.*\S.*`
Required: No

## Response Syntax
<a name="API_UpdateInsight_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateInsight_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateInsight_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

## See Also
<a name="API_UpdateInsight_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/UpdateInsight)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/UpdateInsight)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/UpdateInsight)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/UpdateInsight)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/UpdateInsight)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/UpdateInsight)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/UpdateInsight)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/UpdateInsight)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/UpdateInsight)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/UpdateInsight)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
