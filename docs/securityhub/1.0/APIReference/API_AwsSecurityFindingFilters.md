---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsSecurityFindingFilters.html
---

# AwsSecurityFindingFilters
<a name="API_AwsSecurityFindingFilters"></a>

A collection of filters that are applied to all active findings aggregated by AWS Security Hub CSPM.

You can filter by up to ten finding attributes. For each attribute, you can provide up to 20 filter values.

## Contents
<a name="API_AwsSecurityFindingFilters_Contents"></a>

 ** AwsAccountId **   <a name="securityhub-Type-AwsSecurityFindingFilters-AwsAccountId"></a>
The AWS account ID in which a finding is generated.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** AwsAccountName **   <a name="securityhub-Type-AwsSecurityFindingFilters-AwsAccountName"></a>
The name of the AWS account in which a finding is generated.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** CompanyName **   <a name="securityhub-Type-AwsSecurityFindingFilters-CompanyName"></a>
The name of the findings provider (company) that owns the solution (product) that generates findings.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ComplianceAssociatedStandardsId **   <a name="securityhub-Type-AwsSecurityFindingFilters-ComplianceAssociatedStandardsId"></a>
 The unique identifier of a standard in which a control is enabled. This field consists of the resource portion of the Amazon Resource Name (ARN) returned for a standard in the [DescribeStandards](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandards.html) API response.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ComplianceSecurityControlId **   <a name="securityhub-Type-AwsSecurityFindingFilters-ComplianceSecurityControlId"></a>
 The unique identifier of a control across standards. Values for this field typically consist of an AWS service and a number, such as APIGateway.5.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ComplianceSecurityControlParametersName **   <a name="securityhub-Type-AwsSecurityFindingFilters-ComplianceSecurityControlParametersName"></a>
 The name of a security control parameter.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ComplianceSecurityControlParametersValue **   <a name="securityhub-Type-AwsSecurityFindingFilters-ComplianceSecurityControlParametersValue"></a>
 The current value of a security control parameter.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ComplianceStatus **   <a name="securityhub-Type-AwsSecurityFindingFilters-ComplianceStatus"></a>
Exclusive to findings that are generated as the result of a check run against a specific rule in a supported standard, such as CIS AWS Foundations. Contains security standard-related finding details.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** Confidence **   <a name="securityhub-Type-AwsSecurityFindingFilters-Confidence"></a>
A finding's confidence. Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify.
Confidence is scored on a 0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means 100 percent confidence.
Type: Array of [NumberFilter](API_NumberFilter.md) objects
Required: No

 ** CreatedAt **   <a name="securityhub-Type-AwsSecurityFindingFilters-CreatedAt"></a>
A timestamp that indicates when the security findings provider created the potential security issue that a finding reflects.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: Array of [DateFilter](API_DateFilter.md) objects
Required: No

 ** Criticality **   <a name="securityhub-Type-AwsSecurityFindingFilters-Criticality"></a>
The level of importance assigned to the resources associated with the finding.
A score of 0 means that the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources.
Type: Array of [NumberFilter](API_NumberFilter.md) objects
Required: No

 ** Description **   <a name="securityhub-Type-AwsSecurityFindingFilters-Description"></a>
A finding's description.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** FindingProviderFieldsConfidence **   <a name="securityhub-Type-AwsSecurityFindingFilters-FindingProviderFieldsConfidence"></a>
The finding provider value for the finding confidence. Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify.
Confidence is scored on a 0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means 100 percent confidence.
Type: Array of [NumberFilter](API_NumberFilter.md) objects
Required: No

 ** FindingProviderFieldsCriticality **   <a name="securityhub-Type-AwsSecurityFindingFilters-FindingProviderFieldsCriticality"></a>
The finding provider value for the level of importance assigned to the resources associated with the findings.
A score of 0 means that the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources.
Type: Array of [NumberFilter](API_NumberFilter.md) objects
Required: No

 ** FindingProviderFieldsRelatedFindingsId **   <a name="securityhub-Type-AwsSecurityFindingFilters-FindingProviderFieldsRelatedFindingsId"></a>
The finding identifier of a related finding that is identified by the finding provider.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** FindingProviderFieldsRelatedFindingsProductArn **   <a name="securityhub-Type-AwsSecurityFindingFilters-FindingProviderFieldsRelatedFindingsProductArn"></a>
The ARN of the solution that generated a related finding that is identified by the finding provider.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** FindingProviderFieldsSeverityLabel **   <a name="securityhub-Type-AwsSecurityFindingFilters-FindingProviderFieldsSeverityLabel"></a>
The finding provider value for the severity label.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** FindingProviderFieldsSeverityOriginal **   <a name="securityhub-Type-AwsSecurityFindingFilters-FindingProviderFieldsSeverityOriginal"></a>
The finding provider's original value for the severity.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** FindingProviderFieldsTypes **   <a name="securityhub-Type-AwsSecurityFindingFilters-FindingProviderFieldsTypes"></a>
One or more finding types that the finding provider assigned to the finding. Uses the format of `namespace/category/classifier` that classify a finding.
Valid namespace values are: Software and Configuration Checks \| TTPs \| Effects \| Unusual Behaviors \| Sensitive Data Identifications
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** FirstObservedAt **   <a name="securityhub-Type-AwsSecurityFindingFilters-FirstObservedAt"></a>
A timestamp that indicates when the security findings provider first observed the potential security issue that a finding captured.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: Array of [DateFilter](API_DateFilter.md) objects
Required: No

 ** GeneratorId **   <a name="securityhub-Type-AwsSecurityFindingFilters-GeneratorId"></a>
The identifier for the solution-specific component (a discrete unit of logic) that generated a finding. In various security findings providers' solutions, this generator can be called a rule, a check, a detector, a plugin, etc.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** Id **   <a name="securityhub-Type-AwsSecurityFindingFilters-Id"></a>
The security findings provider-specific identifier for a finding.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** Keyword **   <a name="securityhub-Type-AwsSecurityFindingFilters-Keyword"></a>
 *This member has been deprecated.*
A keyword for a finding.
Type: Array of [KeywordFilter](API_KeywordFilter.md) objects
Required: No

 ** LastObservedAt **   <a name="securityhub-Type-AwsSecurityFindingFilters-LastObservedAt"></a>
A timestamp that indicates when the security findings provider most recently observed a change in the resource that is involved in the finding.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: Array of [DateFilter](API_DateFilter.md) objects
Required: No

 ** MalwareName **   <a name="securityhub-Type-AwsSecurityFindingFilters-MalwareName"></a>
The name of the malware that was observed.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** MalwarePath **   <a name="securityhub-Type-AwsSecurityFindingFilters-MalwarePath"></a>
The filesystem path of the malware that was observed.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** MalwareState **   <a name="securityhub-Type-AwsSecurityFindingFilters-MalwareState"></a>
The state of the malware that was observed.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** MalwareType **   <a name="securityhub-Type-AwsSecurityFindingFilters-MalwareType"></a>
The type of the malware that was observed.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** NetworkDestinationDomain **   <a name="securityhub-Type-AwsSecurityFindingFilters-NetworkDestinationDomain"></a>
The destination domain of network-related information about a finding.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** NetworkDestinationIpV4 **   <a name="securityhub-Type-AwsSecurityFindingFilters-NetworkDestinationIpV4"></a>
The destination IPv4 address of network-related information about a finding.
Type: Array of [IpFilter](API_IpFilter.md) objects
Required: No

 ** NetworkDestinationIpV6 **   <a name="securityhub-Type-AwsSecurityFindingFilters-NetworkDestinationIpV6"></a>
The destination IPv6 address of network-related information about a finding.
Type: Array of [IpFilter](API_IpFilter.md) objects
Required: No

 ** NetworkDestinationPort **   <a name="securityhub-Type-AwsSecurityFindingFilters-NetworkDestinationPort"></a>
The destination port of network-related information about a finding.
Type: Array of [NumberFilter](API_NumberFilter.md) objects
Required: No

 ** NetworkDirection **   <a name="securityhub-Type-AwsSecurityFindingFilters-NetworkDirection"></a>
Indicates the direction of network traffic associated with a finding.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** NetworkProtocol **   <a name="securityhub-Type-AwsSecurityFindingFilters-NetworkProtocol"></a>
The protocol of network-related information about a finding.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** NetworkSourceDomain **   <a name="securityhub-Type-AwsSecurityFindingFilters-NetworkSourceDomain"></a>
The source domain of network-related information about a finding.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** NetworkSourceIpV4 **   <a name="securityhub-Type-AwsSecurityFindingFilters-NetworkSourceIpV4"></a>
The source IPv4 address of network-related information about a finding.
Type: Array of [IpFilter](API_IpFilter.md) objects
Required: No

 ** NetworkSourceIpV6 **   <a name="securityhub-Type-AwsSecurityFindingFilters-NetworkSourceIpV6"></a>
The source IPv6 address of network-related information about a finding.
Type: Array of [IpFilter](API_IpFilter.md) objects
Required: No

 ** NetworkSourceMac **   <a name="securityhub-Type-AwsSecurityFindingFilters-NetworkSourceMac"></a>
The source media access control (MAC) address of network-related information about a finding.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** NetworkSourcePort **   <a name="securityhub-Type-AwsSecurityFindingFilters-NetworkSourcePort"></a>
The source port of network-related information about a finding.
Type: Array of [NumberFilter](API_NumberFilter.md) objects
Required: No

 ** NoteText **   <a name="securityhub-Type-AwsSecurityFindingFilters-NoteText"></a>
The text of a note.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** NoteUpdatedAt **   <a name="securityhub-Type-AwsSecurityFindingFilters-NoteUpdatedAt"></a>
The timestamp of when the note was updated.
Type: Array of [DateFilter](API_DateFilter.md) objects
Required: No

 ** NoteUpdatedBy **   <a name="securityhub-Type-AwsSecurityFindingFilters-NoteUpdatedBy"></a>
The principal that created a note.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ProcessLaunchedAt **   <a name="securityhub-Type-AwsSecurityFindingFilters-ProcessLaunchedAt"></a>
A timestamp that identifies when the process was launched.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: Array of [DateFilter](API_DateFilter.md) objects
Required: No

 ** ProcessName **   <a name="securityhub-Type-AwsSecurityFindingFilters-ProcessName"></a>
The name of the process.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ProcessParentPid **   <a name="securityhub-Type-AwsSecurityFindingFilters-ProcessParentPid"></a>
The parent process ID. This field accepts positive integers between `O` and `2147483647`.
Type: Array of [NumberFilter](API_NumberFilter.md) objects
Required: No

 ** ProcessPath **   <a name="securityhub-Type-AwsSecurityFindingFilters-ProcessPath"></a>
The path to the process executable.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ProcessPid **   <a name="securityhub-Type-AwsSecurityFindingFilters-ProcessPid"></a>
The process ID.
Type: Array of [NumberFilter](API_NumberFilter.md) objects
Required: No

 ** ProcessTerminatedAt **   <a name="securityhub-Type-AwsSecurityFindingFilters-ProcessTerminatedAt"></a>
A timestamp that identifies when the process was terminated.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: Array of [DateFilter](API_DateFilter.md) objects
Required: No

 ** ProductArn **   <a name="securityhub-Type-AwsSecurityFindingFilters-ProductArn"></a>
The ARN generated by Security Hub CSPM that uniquely identifies a third-party company (security findings provider) after this provider's product (solution that generates findings) is registered with Security Hub CSPM.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ProductFields **   <a name="securityhub-Type-AwsSecurityFindingFilters-ProductFields"></a>
A data type where security findings providers can include additional solution-specific details that aren't part of the defined `AwsSecurityFinding` format.
Type: Array of [MapFilter](API_MapFilter.md) objects
Required: No

 ** ProductName **   <a name="securityhub-Type-AwsSecurityFindingFilters-ProductName"></a>
The name of the solution (product) that generates findings.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** RecommendationText **   <a name="securityhub-Type-AwsSecurityFindingFilters-RecommendationText"></a>
The recommendation of what to do about the issue described in a finding.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** RecordState **   <a name="securityhub-Type-AwsSecurityFindingFilters-RecordState"></a>
The updated record state for the finding.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** Region **   <a name="securityhub-Type-AwsSecurityFindingFilters-Region"></a>
The Region from which the finding was generated.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** RelatedFindingsId **   <a name="securityhub-Type-AwsSecurityFindingFilters-RelatedFindingsId"></a>
The solution-generated identifier for a related finding.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** RelatedFindingsProductArn **   <a name="securityhub-Type-AwsSecurityFindingFilters-RelatedFindingsProductArn"></a>
The ARN of the solution that generated a related finding.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceApplicationArn **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceApplicationArn"></a>
 The ARN of the application that is related to a finding.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceApplicationName **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceApplicationName"></a>
 The name of the application that is related to a finding.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceAwsEc2InstanceIamInstanceProfileArn **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceAwsEc2InstanceIamInstanceProfileArn"></a>
The IAM profile ARN of the instance.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceAwsEc2InstanceImageId **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceAwsEc2InstanceImageId"></a>
The Amazon Machine Image (AMI) ID of the instance.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceAwsEc2InstanceIpV4Addresses **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceAwsEc2InstanceIpV4Addresses"></a>
The IPv4 addresses associated with the instance.
Type: Array of [IpFilter](API_IpFilter.md) objects
Required: No

 ** ResourceAwsEc2InstanceIpV6Addresses **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceAwsEc2InstanceIpV6Addresses"></a>
The IPv6 addresses associated with the instance.
Type: Array of [IpFilter](API_IpFilter.md) objects
Required: No

 ** ResourceAwsEc2InstanceKeyName **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceAwsEc2InstanceKeyName"></a>
The key name associated with the instance.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceAwsEc2InstanceLaunchedAt **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceAwsEc2InstanceLaunchedAt"></a>
The date and time the instance was launched.
Type: Array of [DateFilter](API_DateFilter.md) objects
Required: No

 ** ResourceAwsEc2InstanceSubnetId **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceAwsEc2InstanceSubnetId"></a>
The identifier of the subnet that the instance was launched in.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceAwsEc2InstanceType **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceAwsEc2InstanceType"></a>
The instance type of the instance.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceAwsEc2InstanceVpcId **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceAwsEc2InstanceVpcId"></a>
The identifier of the VPC that the instance was launched in.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceAwsIamAccessKeyCreatedAt **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceAwsIamAccessKeyCreatedAt"></a>
The creation date/time of the IAM access key related to a finding.
Type: Array of [DateFilter](API_DateFilter.md) objects
Required: No

 ** ResourceAwsIamAccessKeyPrincipalName **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceAwsIamAccessKeyPrincipalName"></a>
The name of the principal that is associated with an IAM access key.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceAwsIamAccessKeyStatus **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceAwsIamAccessKeyStatus"></a>
The status of the IAM access key related to a finding.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceAwsIamAccessKeyUserName **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceAwsIamAccessKeyUserName"></a>
 *This member has been deprecated.*
The user associated with the IAM access key related to a finding.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceAwsIamUserUserName **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceAwsIamUserUserName"></a>
The name of an IAM user.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceAwsS3BucketOwnerId **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceAwsS3BucketOwnerId"></a>
The canonical user ID of the owner of the S3 bucket.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceAwsS3BucketOwnerName **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceAwsS3BucketOwnerName"></a>
The display name of the owner of the S3 bucket.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceContainerImageId **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceContainerImageId"></a>
The identifier of the image related to a finding.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceContainerImageName **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceContainerImageName"></a>
The name of the image related to a finding.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceContainerLaunchedAt **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceContainerLaunchedAt"></a>
A timestamp that identifies when the container was started.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: Array of [DateFilter](API_DateFilter.md) objects
Required: No

 ** ResourceContainerName **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceContainerName"></a>
The name of the container related to a finding.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceDetailsOther **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceDetailsOther"></a>
The details of a resource that doesn't have a specific subfield for the resource type defined.
Type: Array of [MapFilter](API_MapFilter.md) objects
Required: No

 ** ResourceId **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceId"></a>
The canonical identifier for the given resource type.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceOwnerAccountId **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceOwnerAccountId"></a>
The unique identifier of the account that owns the resource that the finding applies to, for example, Azure Subscription Id or AWS Account Id
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceOwnerOrgId **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceOwnerOrgId"></a>
The unique identifier of the organization that owns the resource that the finding applies to, for example, Azure Tenant Id
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourcePartition **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourcePartition"></a>
The canonical AWS partition name that the Region is assigned to.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceProvider **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceProvider"></a>
The cloud provider that the resource belongs to. Valid values are `AWS` and `Azure`.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceRegion **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceRegion"></a>
The canonical AWS external Region name where this resource is located.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ResourceTags **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceTags"></a>
A list of AWS tags associated with a resource at the time the finding was processed.
Type: Array of [MapFilter](API_MapFilter.md) objects
Required: No

 ** ResourceType **   <a name="securityhub-Type-AwsSecurityFindingFilters-ResourceType"></a>
Specifies the type of the resource that details are provided for.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** Sample **   <a name="securityhub-Type-AwsSecurityFindingFilters-Sample"></a>
Indicates whether or not sample findings are included in the filter results.
Type: Array of [BooleanFilter](API_BooleanFilter.md) objects
Required: No

 ** SeverityLabel **   <a name="securityhub-Type-AwsSecurityFindingFilters-SeverityLabel"></a>
The label of a finding's severity.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** SeverityNormalized **   <a name="securityhub-Type-AwsSecurityFindingFilters-SeverityNormalized"></a>
 *This member has been deprecated.*
The normalized severity of a finding.
Type: Array of [NumberFilter](API_NumberFilter.md) objects
Required: No

 ** SeverityProduct **   <a name="securityhub-Type-AwsSecurityFindingFilters-SeverityProduct"></a>
 *This member has been deprecated.*
The native severity as defined by the security findings provider's solution that generated the finding.
Type: Array of [NumberFilter](API_NumberFilter.md) objects
Required: No

 ** SourceUrl **   <a name="securityhub-Type-AwsSecurityFindingFilters-SourceUrl"></a>
A URL that links to a page about the current finding in the security findings provider's solution.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ThreatIntelIndicatorCategory **   <a name="securityhub-Type-AwsSecurityFindingFilters-ThreatIntelIndicatorCategory"></a>
The category of a threat intelligence indicator.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ThreatIntelIndicatorLastObservedAt **   <a name="securityhub-Type-AwsSecurityFindingFilters-ThreatIntelIndicatorLastObservedAt"></a>
A timestamp that identifies the last observation of a threat intelligence indicator.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: Array of [DateFilter](API_DateFilter.md) objects
Required: No

 ** ThreatIntelIndicatorSource **   <a name="securityhub-Type-AwsSecurityFindingFilters-ThreatIntelIndicatorSource"></a>
The source of the threat intelligence.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ThreatIntelIndicatorSourceUrl **   <a name="securityhub-Type-AwsSecurityFindingFilters-ThreatIntelIndicatorSourceUrl"></a>
The URL for more details from the source of the threat intelligence.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ThreatIntelIndicatorType **   <a name="securityhub-Type-AwsSecurityFindingFilters-ThreatIntelIndicatorType"></a>
The type of a threat intelligence indicator.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** ThreatIntelIndicatorValue **   <a name="securityhub-Type-AwsSecurityFindingFilters-ThreatIntelIndicatorValue"></a>
The value of a threat intelligence indicator.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** Title **   <a name="securityhub-Type-AwsSecurityFindingFilters-Title"></a>
A finding's title.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** Type **   <a name="securityhub-Type-AwsSecurityFindingFilters-Type"></a>
A finding type in the format of `namespace/category/classifier` that classifies a finding.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** UpdatedAt **   <a name="securityhub-Type-AwsSecurityFindingFilters-UpdatedAt"></a>
A timestamp that indicates when the security findings provider last updated the finding record.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: Array of [DateFilter](API_DateFilter.md) objects
Required: No

 ** UserDefinedFields **   <a name="securityhub-Type-AwsSecurityFindingFilters-UserDefinedFields"></a>
A list of name/value string pairs associated with the finding. These are custom, user-defined fields added to a finding.
Type: Array of [MapFilter](API_MapFilter.md) objects
Required: No

 ** VerificationState **   <a name="securityhub-Type-AwsSecurityFindingFilters-VerificationState"></a>
The veracity of a finding.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** VulnerabilitiesExploitAvailable **   <a name="securityhub-Type-AwsSecurityFindingFilters-VulnerabilitiesExploitAvailable"></a>
 Indicates whether a software vulnerability in your environment has a known exploit. You can filter findings by this field only if you use Security Hub CSPM and Amazon Inspector.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** VulnerabilitiesFixAvailable **   <a name="securityhub-Type-AwsSecurityFindingFilters-VulnerabilitiesFixAvailable"></a>
 Indicates whether a vulnerability is fixed in a newer version of the affected software packages. You can filter findings by this field only if you use Security Hub CSPM and Amazon Inspector.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** WorkflowState **   <a name="securityhub-Type-AwsSecurityFindingFilters-WorkflowState"></a>
The workflow state of a finding.
Note that this field is deprecated. To search for a finding based on its workflow status, use `WorkflowStatus`.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

 ** WorkflowStatus **   <a name="securityhub-Type-AwsSecurityFindingFilters-WorkflowStatus"></a>
The status of the investigation into a finding. Allowed values are the following.
+  `NEW` - The initial state of a finding, before it is reviewed.

  Security Hub CSPM also resets the workflow status from `NOTIFIED` or `RESOLVED` to `NEW` in the following cases:
  +  `RecordState` changes from `ARCHIVED` to `ACTIVE`.
  +  `Compliance.Status` changes from `PASSED` to either `WARNING`, `FAILED`, or `NOT_AVAILABLE`.
+  `NOTIFIED` - Indicates that the resource owner has been notified about the security issue. Used when the initial reviewer is not the resource owner, and needs intervention from the resource owner.

  If one of the following occurs, the workflow status is changed automatically from `NOTIFIED` to `NEW`:
  +  `RecordState` changes from `ARCHIVED` to `ACTIVE`.
  +  `Compliance.Status` changes from `PASSED` to `FAILED`, `WARNING`, or `NOT_AVAILABLE`.
+  `SUPPRESSED` - Indicates that you reviewed the finding and don't believe that any action is needed.

  The workflow status of a `SUPPRESSED` finding does not change if `RecordState` changes from `ARCHIVED` to `ACTIVE`.
+  `RESOLVED` - The finding was reviewed and remediated and is now considered resolved.

  The finding remains `RESOLVED` unless one of the following occurs:
  +  `RecordState` changes from `ARCHIVED` to `ACTIVE`.
  +  `Compliance.Status` changes from `PASSED` to `FAILED`, `WARNING`, or `NOT_AVAILABLE`.

  In those cases, the workflow status is automatically reset to `NEW`.

  For findings from controls, if `Compliance.Status` is `PASSED`, then Security Hub CSPM automatically sets the workflow status to `RESOLVED`.
Type: Array of [StringFilter](API_StringFilter.md) objects
Required: No

## See Also
<a name="API_AwsSecurityFindingFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsSecurityFindingFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsSecurityFindingFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsSecurityFindingFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
