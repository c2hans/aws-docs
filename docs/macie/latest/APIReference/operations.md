---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/operations.html
---

# Operations
<a name="operations"></a>

The Amazon Macie REST API includes the following operations.
+ [AcceptInvitation](invitations-accept.md#AcceptInvitation)

  Accepts an Amazon Macie membership invitation that was received from a specific account.
+ [BatchGetCustomDataIdentifiers](custom-data-identifiers-get.md#BatchGetCustomDataIdentifiers)

  Retrieves information about one or more custom data identifiers.
+ [BatchUpdateAutomatedDiscoveryAccounts](automated-discovery-accounts.md#BatchUpdateAutomatedDiscoveryAccounts)

  Changes the status of automated sensitive data discovery for one or more accounts.
+ [CreateAllowList](allow-lists.md#CreateAllowList)

  Creates and defines the settings for an allow list.
+ [CreateClassificationJob](jobs.md#CreateClassificationJob)

  Creates and defines the settings for a classification job.
+ [CreateCustomDataIdentifier](custom-data-identifiers.md#CreateCustomDataIdentifier)

  Creates and defines the criteria and other settings for a custom data identifier.
+ [CreateFindingsFilter](findingsfilters.md#CreateFindingsFilter)

  Creates and defines the criteria and other settings for a findings filter.
+ [CreateInvitations](invitations.md#CreateInvitations)

  Sends an Amazon Macie membership invitation to one or more accounts.
+ [CreateMember](members.md#CreateMember)

  Associates an account with an Amazon Macie administrator account.
+ [CreateSampleFindings](findings-sample.md#CreateSampleFindings)

  Creates sample findings.
+ [DeclineInvitations](invitations-decline.md#DeclineInvitations)

  Declines Amazon Macie membership invitations that were received from specific accounts.
+ [DeleteAllowList](allow-lists-id.md#DeleteAllowList)

  Deletes an allow list.
+ [DeleteCustomDataIdentifier](custom-data-identifiers-id.md#DeleteCustomDataIdentifier)

  Soft deletes a custom data identifier.
+ [DeleteFindingsFilter](findingsfilters-id.md#DeleteFindingsFilter)

  Deletes a findings filter.
+ [DeleteInvitations](invitations-delete.md#DeleteInvitations)

  Deletes Amazon Macie membership invitations that were received from specific accounts.
+ [DeleteMember](members-id.md#DeleteMember)

  Deletes the association between an Amazon Macie administrator account and an account.
+ [DescribeBuckets](datasources-s3.md#DescribeBuckets)

  Retrieves (queries) statistical data and other information about one or more S3 buckets that Amazon Macie monitors and analyzes for an account.
+ [DescribeClassificationJob](jobs-jobid.md#DescribeClassificationJob)

  Retrieves the status and settings for a classification job.
+ [DescribeOrganizationConfiguration](admin-configuration.md#DescribeOrganizationConfiguration)

  Retrieves the Amazon Macie configuration settings for an organization in AWS Organizations.
+ [DisableMacie](macie.md#DisableMacie)

  Disables Amazon Macie and deletes all settings and resources for a Macie account.
+ [DisableOrganizationAdminAccount](admin.md#DisableOrganizationAdminAccount)

  Disables an account as the delegated Amazon Macie administrator account for an organization in AWS Organizations.
+ [DisassociateFromAdministratorAccount](administrator-disassociate.md#DisassociateFromAdministratorAccount)

  Disassociates a member account from its Amazon Macie administrator account.
+ [DisassociateFromMasterAccount](master-disassociate.md#DisassociateFromMasterAccount)

  (Deprecated) Disassociates a member account from its Amazon Macie administrator account. This operation has been replaced by the [DisassociateFromAdministratorAccount](administrator-disassociate.md#DisassociateFromAdministratorAccount) operation.
+ [DisassociateMember](members-disassociate-id.md#DisassociateMember)

  Disassociates an Amazon Macie administrator account from a member account.
+ [EnableMacie](macie.md#EnableMacie)

  Enables Amazon Macie and specifies the configuration settings for a Macie account.
+ [EnableOrganizationAdminAccount](admin.md#EnableOrganizationAdminAccount)

  Designates an account as the delegated Amazon Macie administrator account for an organization in AWS Organizations.
+ [GetAdministratorAccount](administrator.md#GetAdministratorAccount)

  Retrieves information about the Amazon Macie administrator account for an account.
+ [GetAllowList](allow-lists-id.md#GetAllowList)

  Retrieves the settings and status of an allow list.
+ [GetAutomatedDiscoveryConfiguration](automated-discovery-configuration.md#GetAutomatedDiscoveryConfiguration)

  Retrieves the configuration settings and status of automated sensitive data discovery for an organization or standalone account.
+ [GetBucketStatistics](datasources-s3-statistics.md#GetBucketStatistics)

  Retrieves (queries) aggregated statistical data about all the S3 buckets that Amazon Macie monitors and analyzes for an account.
+ [GetClassificationExportConfiguration](classification-export-configuration.md#GetClassificationExportConfiguration)

  Retrieves the configuration settings for storing data classification results.
+ [GetClassificationScope](classification-scopes-id.md#GetClassificationScope)

  Retrieves the classification scope settings for an account.
+ [GetCustomDataIdentifier](custom-data-identifiers-id.md#GetCustomDataIdentifier)

  Retrieves the criteria and other settings for a custom data identifier.
+ [GetFindings](findings-describe.md#GetFindings)

  Retrieves the details of one or more findings.
+ [GetFindingsFilter](findingsfilters-id.md#GetFindingsFilter)

  Retrieves the criteria and other settings for a findings filter.
+ [GetFindingsPublicationConfiguration](findings-publication-configuration.md#GetFindingsPublicationConfiguration)

  Retrieves the configuration settings for publishing findings to AWS Security Hub CSPM.
+ [GetFindingStatistics](findings-statistics.md#GetFindingStatistics)

  Retrieves (queries) aggregated statistical data about findings.
+ [GetInvitationsCount](invitations-count.md#GetInvitationsCount)

  Retrieves the count of Amazon Macie membership invitations that were received by an account.
+ [GetMacieSession](macie.md#GetMacieSession)

  Retrieves the status and configuration settings for an Amazon Macie account.
+ [GetMasterAccount](master.md#GetMasterAccount)

  (Deprecated) Retrieves information about the Amazon Macie administrator account for an account. This operation has been replaced by the [GetAdministratorAccount](administrator.md#GetAdministratorAccount) operation.
+ [GetMember](members-id.md#GetMember)

  Retrieves information about an account that's associated with an Amazon Macie administrator account.
+ [GetResourceProfile](resource-profiles.md#GetResourceProfile)

  Retrieves (queries) sensitive data discovery statistics and the sensitivity score for an S3 bucket.
+ [GetRevealConfiguration](reveal-configuration.md#GetRevealConfiguration)

  Retrieves the status and configuration settings for retrieving occurrences of sensitive data reported by findings.
+ [GetSensitiveDataOccurrences](findings-findingid-reveal.md#GetSensitiveDataOccurrences)

  Retrieves occurrences of sensitive data reported by a finding.
+ [GetSensitiveDataOccurrencesAvailability](findings-findingid-reveal-availability.md#GetSensitiveDataOccurrencesAvailability)

  Checks whether occurrences of sensitive data can be retrieved for a finding.
+ [GetSensitivityInspectionTemplate](templates-sensitivity-inspections-id.md#GetSensitivityInspectionTemplate)

  Retrieves the settings for the sensitivity inspection template for an account.
+ [GetUsageStatistics](usage-statistics.md#GetUsageStatistics)

  Retrieves (queries) quotas and aggregated usage data for one or more accounts.
+ [GetUsageTotals](usage.md#GetUsageTotals)

  Retrieves (queries) aggregated usage data for an account.
+ [ListAllowLists](allow-lists.md#ListAllowLists)

  Retrieves a subset of information about all the allow lists for an account.
+ [ListAutomatedDiscoveryAccounts](automated-discovery-accounts.md#ListAutomatedDiscoveryAccounts)

  Retrieves the status of automated sensitive data discovery for one or more accounts.
+ [ListClassificationJobs](jobs-list.md#ListClassificationJobs)

  Retrieves a subset of information about one or more classification jobs.
+ [ListClassificationScopes](classification-scopes.md#ListClassificationScopes)

  Retrieves a subset of information about the classification scope for an account.
+ [ListCustomDataIdentifiers](custom-data-identifiers-list.md#ListCustomDataIdentifiers)

  Retrieves a subset of information about the custom data identifiers for an account.
+ [ListFindings](findings.md#ListFindings)

  Retrieves a subset of information about one or more findings.
+ [ListFindingsFilters](findingsfilters.md#ListFindingsFilters)

  Retrieves a subset of information about all the findings filters for an account.
+ [ListInvitations](invitations.md#ListInvitations)

  Retrieves information about Amazon Macie membership invitations that were received by an account.
+ [ListManagedDataIdentifiers](managed-data-identifiers-list.md#ListManagedDataIdentifiers)

  Retrieves information about all the managed data identifiers that Amazon Macie currently provides.
+ [ListMembers](members.md#ListMembers)

  Retrieves information about the accounts that are associated with an Amazon Macie administrator account.
+ [ListOrganizationAdminAccounts](admin.md#ListOrganizationAdminAccounts)

  Retrieves information about the delegated Amazon Macie administrator account for an organization in AWS Organizations.
+ [ListResourceProfileArtifacts](resource-profiles-artifacts.md#ListResourceProfileArtifacts)

  Retrieves information about objects that Amazon Macie selected from an S3 bucket for automated sensitive data discovery.
+ [ListResourceProfileDetections](resource-profiles-detections.md#ListResourceProfileDetections)

  Retrieves information about the types and amount of sensitive data that Amazon Macie found in an S3 bucket.
+ [ListSensitivityInspectionTemplates](templates-sensitivity-inspections.md#ListSensitivityInspectionTemplates)

  Retrieves a subset of information about the sensitivity inspection template for an account.
+ [ListTagsForResource](tags-resourcearn.md#ListTagsForResource)

  Retrieves the tags (keys and values) that are associated with an Amazon Macie resource.
+ [PutClassificationExportConfiguration](classification-export-configuration.md#PutClassificationExportConfiguration)

  Adds or updates the configuration settings for storing data classification results.
+ [PutFindingsPublicationConfiguration](findings-publication-configuration.md#PutFindingsPublicationConfiguration)

  Updates the configuration settings for publishing findings to AWS Security Hub CSPM.
+ [SearchResources](datasources-search-resources.md#SearchResources)

  Retrieves (queries) statistical data and other information about AWS resources that Amazon Macie monitors and analyzes for an account.
+ [TagResource](tags-resourcearn.md#TagResource)

  Adds or updates one or more tags (keys and values) that are associated with an Amazon Macie resource.
+ [TestCustomDataIdentifier](custom-data-identifiers-test.md#TestCustomDataIdentifier)

  Tests criteria for a custom data identifier.
+ [UntagResource](tags-resourcearn.md#UntagResource)

  Removes one or more tags (keys and values) from an Amazon Macie resource.
+ [UpdateAllowList](allow-lists-id.md#UpdateAllowList)

  Updates the settings for an allow list.
+ [UpdateAutomatedDiscoveryConfiguration](automated-discovery-configuration.md#UpdateAutomatedDiscoveryConfiguration)

  Changes the configuration settings and status of automated sensitive data discovery for an organization or standalone account.
+ [UpdateClassificationJob](jobs-jobid.md#UpdateClassificationJob)

  Changes the status of a classification job.
+ [UpdateClassificationScope](classification-scopes-id.md#UpdateClassificationScope)

  Updates the classification scope settings for an account.
+ [UpdateFindingsFilter](findingsfilters-id.md#UpdateFindingsFilter)

  Updates the criteria and other settings for a findings filter.
+ [UpdateMacieSession](macie.md#UpdateMacieSession)

  Suspends or re-enables Amazon Macie, or updates the configuration settings for a Macie account.
+ [UpdateMemberSession](macie-members-id.md#UpdateMemberSession)

  Enables an Amazon Macie administrator to suspend or re-enable Macie for a member account.
+ [UpdateOrganizationConfiguration](admin-configuration.md#UpdateOrganizationConfiguration)

  Updates the Amazon Macie configuration settings for an organization in AWS Organizations.
+ [UpdateResourceProfile](resource-profiles.md#UpdateResourceProfile)

  Updates the sensitivity score for an S3 bucket.
+ [UpdateResourceProfileDetections](resource-profiles-detections.md#UpdateResourceProfileDetections)

  Updates the sensitivity scoring settings for an S3 bucket.
+ [UpdateRevealConfiguration](reveal-configuration.md#UpdateRevealConfiguration)

  Updates the status and configuration settings for retrieving occurrences of sensitive data reported by findings.
+ [UpdateSensitivityInspectionTemplate](templates-sensitivity-inspections-id.md#UpdateSensitivityInspectionTemplate)

  Updates the settings for the sensitivity inspection template for an account.
