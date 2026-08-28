---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_JobError.html
---

# JobError
<a name="API_JobError"></a>

An error that occurred with the job request.

## Contents
<a name="API_JobError_Contents"></a>

 ** Code **   <a name="dataexchange-Type-JobError-Code"></a>
The code for the job error.
Type: String
Valid Values: `ACCESS_DENIED_EXCEPTION | INTERNAL_SERVER_EXCEPTION | MALWARE_DETECTED | RESOURCE_NOT_FOUND_EXCEPTION | SERVICE_QUOTA_EXCEEDED_EXCEPTION | VALIDATION_EXCEPTION | MALWARE_SCAN_ENCRYPTED_FILE`
Required: Yes

 ** Message **   <a name="dataexchange-Type-JobError-Message"></a>
The message related to the job error.
Type: String
Required: Yes

 ** Details **   <a name="dataexchange-Type-JobError-Details"></a>
The details about the job error.
Type: [Details](API_Details.md) object
Required: No

 ** LimitName **   <a name="dataexchange-Type-JobError-LimitName"></a>
The name of the limit that was reached.
Type: String
Valid Values: `Assets per revision | Asset size in GB | Amazon Redshift datashare assets per revision | AWS Lake Formation data permission assets per revision | Amazon S3 data access assets per revision`
Required: No

 ** LimitValue **   <a name="dataexchange-Type-JobError-LimitValue"></a>
The value of the exceeded limit.
Type: Double
Required: No

 ** ResourceId **   <a name="dataexchange-Type-JobError-ResourceId"></a>
The unique identifier for the resource related to the error.
Type: String
Required: No

 ** ResourceType **   <a name="dataexchange-Type-JobError-ResourceType"></a>
The type of resource related to the error.
Type: String
Valid Values: `REVISION | ASSET | DATA_SET`
Required: No

## See Also
<a name="API_JobError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/JobError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/JobError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/JobError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
