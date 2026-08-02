---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ServerlessFunctionAggregationResponse.html
---

# ServerlessFunctionAggregationResponse
<a name="API_ServerlessFunctionAggregationResponse"></a>

A response that contains the results of a serverless function aggregation.

## Contents
<a name="API_ServerlessFunctionAggregationResponse_Contents"></a>

 ** resourceId **   <a name="inspector2-Type-ServerlessFunctionAggregationResponse-resourceId"></a>
The resource ID for the serverless function.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** accountId **   <a name="inspector2-Type-ServerlessFunctionAggregationResponse-accountId"></a>
The account ID associated with the serverless function.
Type: String
Required: No

 ** cloudAccountId **   <a name="inspector2-Type-ServerlessFunctionAggregationResponse-cloudAccountId"></a>
The cloud account ID for the serverless function aggregation.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 36.
Pattern: `(\d{12}|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})`
Required: No

 ** cloudOrgId **   <a name="inspector2-Type-ServerlessFunctionAggregationResponse-cloudOrgId"></a>
The cloud organization ID for the serverless function aggregation.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 36.
Pattern: `(o-[a-z0-9]{10,32}|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})`
Required: No

 ** cloudPartition **   <a name="inspector2-Type-ServerlessFunctionAggregationResponse-cloudPartition"></a>
The cloud infrastructure partition associated with this serverless function aggregation. Valid values:
+  `aws` – AWS commercial Regions.
+  `aws-cn` – AWS China Regions.
+  `aws-us-gov` – AWS GovCloud (US) Regions.
+  `AzureCloud` – Azure commercial Regions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(aws(-[a-z]+)*|Azure[A-Za-z]+)`
Required: No

 ** cloudProvider **   <a name="inspector2-Type-ServerlessFunctionAggregationResponse-cloudProvider"></a>
The cloud service provider associated with this serverless function aggregation. Valid values:
+  `AWS` – Findings from AWS resources.
+  `AZURE` – Findings from Microsoft Azure resources.
Type: String
Valid Values: `AWS | AZURE`
Required: No

 ** cloudRegion **   <a name="inspector2-Type-ServerlessFunctionAggregationResponse-cloudRegion"></a>
The cloud Region associated with this serverless function aggregation. The value format depends on the cloud provider:
+ An AWS Region, such as `us-east-1`.
+ An Azure region, such as `eastus`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `([a-z]{2}(-[a-z]+)+-\d+|[a-z][a-z0-9]+)`
Required: No

 ** exploitAvailableActiveFindingsCount **   <a name="inspector2-Type-ServerlessFunctionAggregationResponse-exploitAvailableActiveFindingsCount"></a>
The number of active findings with an exploit available for the serverless function.
Type: Long
Required: No

 ** fixAvailableActiveFindingsCount **   <a name="inspector2-Type-ServerlessFunctionAggregationResponse-fixAvailableActiveFindingsCount"></a>
The number of active findings with a fix available for the serverless function.
Type: Long
Required: No

 ** functionName **   <a name="inspector2-Type-ServerlessFunctionAggregationResponse-functionName"></a>
The name of the serverless function.
Type: String
Required: No

 ** lastModifiedAt **   <a name="inspector2-Type-ServerlessFunctionAggregationResponse-lastModifiedAt"></a>
The date and time the serverless function was last modified.
Type: Timestamp
Required: No

 ** runtime **   <a name="inspector2-Type-ServerlessFunctionAggregationResponse-runtime"></a>
The runtime of the serverless function.
Type: String
Required: No

 ** severityCounts **   <a name="inspector2-Type-ServerlessFunctionAggregationResponse-severityCounts"></a>
An object that contains the counts of aggregated finding per severity.
Type: [SeverityCounts](API_SeverityCounts.md) object
Required: No

 ** tags **   <a name="inspector2-Type-ServerlessFunctionAggregationResponse-tags"></a>
The tags attached to the serverless function.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_ServerlessFunctionAggregationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ServerlessFunctionAggregationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ServerlessFunctionAggregationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ServerlessFunctionAggregationResponse)
