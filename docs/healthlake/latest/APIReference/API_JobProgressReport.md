---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_JobProgressReport.html
---

# JobProgressReport
<a name="API_JobProgressReport"></a>

The progress report for the import job.

## Contents
<a name="API_JobProgressReport_Contents"></a>

 ** Throughput **   <a name="HealthLake-Type-JobProgressReport-Throughput"></a>
The transaction rate the import job is processed at.
Type: Double
Required: No

 ** TotalFilesConverted **   <a name="HealthLake-Type-JobProgressReport-TotalFilesConverted"></a>
Number of CCDA files successfully transformed during the import's transformation phase. Populated only for import jobs that use the two-Step-Function (transformation \+ ingestion) flow; null for legacy single-SF imports and for pure FHIR imports that skip transformation.
Type: Long
Required: No

 ** TotalNumberOfFilesReadWithCustomerError **   <a name="HealthLake-Type-JobProgressReport-TotalNumberOfFilesReadWithCustomerError"></a>
The number of files that failed to be read from the Amazon S3 input bucket due to customer error.
Type: Long
Required: No

 ** TotalNumberOfImportedFiles **   <a name="HealthLake-Type-JobProgressReport-TotalNumberOfImportedFiles"></a>
The number of files imported.
Type: Long
Required: No

 ** TotalNumberOfImportedNonFhirFiles **   <a name="HealthLake-Type-JobProgressReport-TotalNumberOfImportedNonFhirFiles"></a>
The number of non-FHIR files imported.
Type: Long
Required: No

 ** TotalNumberOfNonFhirFilesReadWithCustomerError **   <a name="HealthLake-Type-JobProgressReport-TotalNumberOfNonFhirFilesReadWithCustomerError"></a>
The number of non-FHIR files that failed to be read from the Amazon S3 input bucket due to customer error.
Type: Long
Required: No

 ** TotalNumberOfNonFhirResourcesImported **   <a name="HealthLake-Type-JobProgressReport-TotalNumberOfNonFhirResourcesImported"></a>
The number of non-FHIR resources imported.
Type: Long
Required: No

 ** TotalNumberOfNonFhirResourcesScanned **   <a name="HealthLake-Type-JobProgressReport-TotalNumberOfNonFhirResourcesScanned"></a>
The number of non-FHIR resources scanned from the Amazon S3 input bucket.
Type: Long
Required: No

 ** TotalNumberOfNonFhirResourcesWithCustomerError **   <a name="HealthLake-Type-JobProgressReport-TotalNumberOfNonFhirResourcesWithCustomerError"></a>
The number of non-FHIR resources that failed due to customer error.
Type: Long
Required: No

 ** TotalNumberOfResourcesImported **   <a name="HealthLake-Type-JobProgressReport-TotalNumberOfResourcesImported"></a>
The number of resources imported.
Type: Long
Required: No

 ** TotalNumberOfResourcesScanned **   <a name="HealthLake-Type-JobProgressReport-TotalNumberOfResourcesScanned"></a>
The number of resources scanned from the Amazon S3 input bucket.
Type: Long
Required: No

 ** TotalNumberOfResourcesWithCustomerError **   <a name="HealthLake-Type-JobProgressReport-TotalNumberOfResourcesWithCustomerError"></a>
The number of resources that failed due to customer error.
Type: Long
Required: No

 ** TotalNumberOfScannedFiles **   <a name="HealthLake-Type-JobProgressReport-TotalNumberOfScannedFiles"></a>
The number of files scanned from the Amazon S3 input bucket.
Type: Long
Required: No

 ** TotalNumberOfScannedNonFhirFiles **   <a name="HealthLake-Type-JobProgressReport-TotalNumberOfScannedNonFhirFiles"></a>
The number of non-FHIR files scanned from the Amazon S3 input bucket.
Type: Long
Required: No

 ** TotalResourcesGenerated **   <a name="HealthLake-Type-JobProgressReport-TotalResourcesGenerated"></a>
Number of FHIR resources produced by the transformation phase. Populated only for import jobs that use the two-Step-Function flow; null for legacy single-SF imports and for pure FHIR imports.
Type: Long
Required: No

 ** TotalSizeOfScannedFilesInMB **   <a name="HealthLake-Type-JobProgressReport-TotalSizeOfScannedFilesInMB"></a>
The size (in MB) of files scanned from the Amazon S3 input bucket.
Type: Double
Required: No

 ** TotalSizeOfScannedNonFhirFilesInMB **   <a name="HealthLake-Type-JobProgressReport-TotalSizeOfScannedNonFhirFilesInMB"></a>
The size (in MB) of non-FHIR files scanned from the Amazon S3 input bucket.
Type: Double
Required: No

## See Also
<a name="API_JobProgressReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/JobProgressReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/JobProgressReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/JobProgressReport)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthLake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthlake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
