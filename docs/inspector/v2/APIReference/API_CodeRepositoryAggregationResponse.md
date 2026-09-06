---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CodeRepositoryAggregationResponse.html
---

# CodeRepositoryAggregationResponse
<a name="API_CodeRepositoryAggregationResponse"></a>

A response that contains the results of a finding aggregation by code repository.

## Contents
<a name="API_CodeRepositoryAggregationResponse_Contents"></a>

 ** projectNames **   <a name="inspector2-Type-CodeRepositoryAggregationResponse-projectNames"></a>
The names of the projects associated with the code repository.
Type: String
Required: Yes

 ** accountId **   <a name="inspector2-Type-CodeRepositoryAggregationResponse-accountId"></a>
The AWS account ID associated with the code repository.
Type: String
Required: No

 ** exploitAvailableActiveFindingsCount **   <a name="inspector2-Type-CodeRepositoryAggregationResponse-exploitAvailableActiveFindingsCount"></a>
The number of active findings that have an exploit available for the code repository.
Type: Long
Required: No

 ** fixAvailableActiveFindingsCount **   <a name="inspector2-Type-CodeRepositoryAggregationResponse-fixAvailableActiveFindingsCount"></a>
The number of active findings that have a fix available for the code repository.
Type: Long
Required: No

 ** providerType **   <a name="inspector2-Type-CodeRepositoryAggregationResponse-providerType"></a>
The type of repository provider for the code repository.
Type: String
Required: No

 ** resourceId **   <a name="inspector2-Type-CodeRepositoryAggregationResponse-resourceId"></a>
The resource ID of the code repository.
Type: String
Required: No

 ** severityCounts **   <a name="inspector2-Type-CodeRepositoryAggregationResponse-severityCounts"></a>
An object that contains the counts of aggregated finding per severity.
Type: [SeverityCounts](API_SeverityCounts.md) object
Required: No

## See Also
<a name="API_CodeRepositoryAggregationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CodeRepositoryAggregationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CodeRepositoryAggregationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CodeRepositoryAggregationResponse)
