---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/sap-abap_comprehend_code_examples.html
---

# Amazon Comprehend examples using SDK for SAP ABAP
<a name="sap-abap_comprehend_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for SAP ABAP with Amazon Comprehend.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `CreateDocumentClassifier`
<a name="comprehend_CreateDocumentClassifier_sap-abap_topic"></a>

The following code example shows how to use `CreateDocumentClassifier`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/cpd#code-examples).

```
    TRY.
        oo_result = lo_cpd->createdocumentclassifier(
          iv_documentclassifiername = iv_classifier_name
          iv_languagecode = iv_language_code
          io_inputdataconfig = NEW /aws1/cl_cpddocclifierinpdat00(
            iv_s3uri = iv_training_s3_uri
          )
          iv_dataaccessrolearn = iv_data_access_role_arn
          iv_mode = iv_mode
        ).
        MESSAGE 'Document classifier creation started.' TYPE 'I'.
      CATCH /aws1/cx_cpdinvalidrequestex.
        MESSAGE 'Invalid request.' TYPE 'E'.
      CATCH /aws1/cx_cpdresrclimitexcdex.
        MESSAGE 'Resource limit exceeded.' TYPE 'E'.
      CATCH /aws1/cx_cpdtoomanyrequestsex.
        MESSAGE 'Too many requests.' TYPE 'E'.
      CATCH /aws1/cx_cpdtoomanytagsex.
        MESSAGE 'Too many tags.' TYPE 'E'.
      CATCH /aws1/cx_cpdinternalserverex.
        MESSAGE 'Internal server error occurred.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [CreateDocumentClassifier](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DeleteDocumentClassifier`
<a name="comprehend_DeleteDocumentClassifier_sap-abap_topic"></a>

The following code example shows how to use `DeleteDocumentClassifier`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/cpd#code-examples).

```
    TRY.
        oo_result = lo_cpd->deletedocumentclassifier(
          iv_documentclassifierarn = iv_classifier_arn
        ).
        MESSAGE 'Document classifier deleted.' TYPE 'I'.
      CATCH /aws1/cx_cpdinvalidrequestex.
        MESSAGE 'Invalid request.' TYPE 'E'.
      CATCH /aws1/cx_cpdtoomanyrequestsex.
        MESSAGE 'Too many requests.' TYPE 'E'.
      CATCH /aws1/cx_cpdresourcenotfoundex.
        MESSAGE 'Resource not found.' TYPE 'E'.
      CATCH /aws1/cx_cpdresourceinuseex.
        MESSAGE 'Resource in use.' TYPE 'E'.
      CATCH /aws1/cx_cpdinternalserverex.
        MESSAGE 'Internal server error occurred.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [DeleteDocumentClassifier](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DescribeDocumentClassificationJob`
<a name="comprehend_DescribeDocumentClassificationJob_sap-abap_topic"></a>

The following code example shows how to use `DescribeDocumentClassificationJob`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/cpd#code-examples).

```
    TRY.
        oo_result = lo_cpd->describedocclassificationjob(
          iv_jobid = iv_job_id
        ).
        MESSAGE 'Document classification job described.' TYPE 'I'.
      CATCH /aws1/cx_cpdinvalidrequestex.
        MESSAGE 'Invalid request.' TYPE 'E'.
      CATCH /aws1/cx_cpdjobnotfoundex.
        MESSAGE 'Job not found.' TYPE 'E'.
      CATCH /aws1/cx_cpdtoomanyrequestsex.
        MESSAGE 'Too many requests.' TYPE 'E'.
      CATCH /aws1/cx_cpdinternalserverex.
        MESSAGE 'Internal server error occurred.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [DescribeDocumentClassificationJob](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DescribeDocumentClassifier`
<a name="comprehend_DescribeDocumentClassifier_sap-abap_topic"></a>

The following code example shows how to use `DescribeDocumentClassifier`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/cpd#code-examples).

```
    TRY.
        oo_result = lo_cpd->describedocumentclassifier(
          iv_documentclassifierarn = iv_classifier_arn
        ).
        MESSAGE 'Document classifier described.' TYPE 'I'.
      CATCH /aws1/cx_cpdinvalidrequestex.
        MESSAGE 'Invalid request.' TYPE 'E'.
      CATCH /aws1/cx_cpdtoomanyrequestsex.
        MESSAGE 'Too many requests.' TYPE 'E'.
      CATCH /aws1/cx_cpdresourcenotfoundex.
        MESSAGE 'Resource not found.' TYPE 'E'.
      CATCH /aws1/cx_cpdinternalserverex.
        MESSAGE 'Internal server error occurred.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [DescribeDocumentClassifier](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DescribeTopicsDetectionJob`
<a name="comprehend_DescribeTopicsDetectionJob_sap-abap_topic"></a>

The following code example shows how to use `DescribeTopicsDetectionJob`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/cpd#code-examples).

```
    TRY.
        oo_result = lo_cpd->describetopicsdetectionjob(
          iv_jobid = iv_job_id
        ).
        MESSAGE 'Topics detection job described.' TYPE 'I'.
      CATCH /aws1/cx_cpdinvalidrequestex.
        MESSAGE 'Invalid request.' TYPE 'E'.
      CATCH /aws1/cx_cpdjobnotfoundex.
        MESSAGE 'Job not found.' TYPE 'E'.
      CATCH /aws1/cx_cpdtoomanyrequestsex.
        MESSAGE 'Too many requests.' TYPE 'E'.
      CATCH /aws1/cx_cpdinternalserverex.
        MESSAGE 'Internal server error occurred.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [DescribeTopicsDetectionJob](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DetectDominantLanguage`
<a name="comprehend_DetectDominantLanguage_sap-abap_topic"></a>

The following code example shows how to use `DetectDominantLanguage`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/cpd#code-examples).

```
    TRY.
        oo_result = lo_cpd->detectdominantlanguage( iv_text = iv_text ).
        MESSAGE 'Languages detected.' TYPE 'I'.
      CATCH /aws1/cx_cpdtextsizelmtexcdex.
        MESSAGE 'Text size exceeds limit.' TYPE 'E'.
      CATCH /aws1/cx_cpdinternalserverex.
        MESSAGE 'Internal server error occurred.' TYPE 'E'.
      CATCH /aws1/cx_cpdinvalidrequestex.
        MESSAGE 'Invalid request.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [DetectDominantLanguage](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DetectEntities`
<a name="comprehend_DetectEntities_sap-abap_topic"></a>

The following code example shows how to use `DetectEntities`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/cpd#code-examples).

```
    TRY.
        oo_result = lo_cpd->detectentities(
          iv_text = iv_text
          iv_languagecode = iv_language_code
        ).
        MESSAGE 'Entities detected.' TYPE 'I'.
      CATCH /aws1/cx_cpdtextsizelmtexcdex.
        MESSAGE 'Text size exceeds limit.' TYPE 'E'.
      CATCH /aws1/cx_cpdunsuppedlanguageex.
        MESSAGE 'Unsupported language.' TYPE 'E'.
      CATCH /aws1/cx_cpdinternalserverex.
        MESSAGE 'Internal server error occurred.' TYPE 'E'.
      CATCH /aws1/cx_cpdinvalidrequestex.
        MESSAGE 'Invalid request.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [DetectEntities](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DetectKeyPhrases`
<a name="comprehend_DetectKeyPhrases_sap-abap_topic"></a>

The following code example shows how to use `DetectKeyPhrases`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/cpd#code-examples).

```
    TRY.
        oo_result = lo_cpd->detectkeyphrases(
          iv_text = iv_text
          iv_languagecode = iv_language_code
        ).
        MESSAGE 'Key phrases detected.' TYPE 'I'.
      CATCH /aws1/cx_cpdtextsizelmtexcdex.
        MESSAGE 'Text size exceeds limit.' TYPE 'E'.
      CATCH /aws1/cx_cpdunsuppedlanguageex.
        MESSAGE 'Unsupported language.' TYPE 'E'.
      CATCH /aws1/cx_cpdinternalserverex.
        MESSAGE 'Internal server error occurred.' TYPE 'E'.
      CATCH /aws1/cx_cpdinvalidrequestex.
        MESSAGE 'Invalid request.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [DetectKeyPhrases](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DetectPiiEntities`
<a name="comprehend_DetectPiiEntities_sap-abap_topic"></a>

The following code example shows how to use `DetectPiiEntities`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/cpd#code-examples).

```
    TRY.
        oo_result = lo_cpd->detectpiientities(
          iv_text = iv_text
          iv_languagecode = iv_language_code
        ).
        MESSAGE 'PII entities detected.' TYPE 'I'.
      CATCH /aws1/cx_cpdtextsizelmtexcdex.
        MESSAGE 'Text size exceeds limit.' TYPE 'E'.
      CATCH /aws1/cx_cpdunsuppedlanguageex.
        MESSAGE 'Unsupported language.' TYPE 'E'.
      CATCH /aws1/cx_cpdinternalserverex.
        MESSAGE 'Internal server error occurred.' TYPE 'E'.
      CATCH /aws1/cx_cpdinvalidrequestex.
        MESSAGE 'Invalid request.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [DetectPiiEntities](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DetectSentiment`
<a name="comprehend_DetectSentiment_sap-abap_topic"></a>

The following code example shows how to use `DetectSentiment`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/cpd#code-examples).

```
    TRY.
        oo_result = lo_cpd->detectsentiment(
          iv_text = iv_text
          iv_languagecode = iv_language_code
        ).
        MESSAGE 'Sentiment detected.' TYPE 'I'.
      CATCH /aws1/cx_cpdtextsizelmtexcdex.
        MESSAGE 'Text size exceeds limit.' TYPE 'E'.
      CATCH /aws1/cx_cpdunsuppedlanguageex.
        MESSAGE 'Unsupported language.' TYPE 'E'.
      CATCH /aws1/cx_cpdinternalserverex.
        MESSAGE 'Internal server error occurred.' TYPE 'E'.
      CATCH /aws1/cx_cpdinvalidrequestex.
        MESSAGE 'Invalid request.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [DetectSentiment](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DetectSyntax`
<a name="comprehend_DetectSyntax_sap-abap_topic"></a>

The following code example shows how to use `DetectSyntax`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/cpd#code-examples).

```
    TRY.
        oo_result = lo_cpd->detectsyntax(
          iv_text = iv_text
          iv_languagecode = iv_language_code
        ).
        MESSAGE 'Syntax tokens detected.' TYPE 'I'.
      CATCH /aws1/cx_cpdtextsizelmtexcdex.
        MESSAGE 'Text size exceeds limit.' TYPE 'E'.
      CATCH /aws1/cx_cpdunsuppedlanguageex.
        MESSAGE 'Unsupported language.' TYPE 'E'.
      CATCH /aws1/cx_cpdinternalserverex.
        MESSAGE 'Internal server error occurred.' TYPE 'E'.
      CATCH /aws1/cx_cpdinvalidrequestex.
        MESSAGE 'Invalid request.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [DetectSyntax](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `ListDocumentClassificationJobs`
<a name="comprehend_ListDocumentClassificationJobs_sap-abap_topic"></a>

The following code example shows how to use `ListDocumentClassificationJobs`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/cpd#code-examples).

```
    TRY.
        oo_result = lo_cpd->listdocclassificationjobs( ).
        MESSAGE 'Document classification jobs listed.' TYPE 'I'.
      CATCH /aws1/cx_cpdinvalidrequestex.
        MESSAGE 'Invalid request.' TYPE 'E'.
      CATCH /aws1/cx_cpdtoomanyrequestsex.
        MESSAGE 'Too many requests.' TYPE 'E'.
      CATCH /aws1/cx_cpdinvalidfilterex.
        MESSAGE 'Invalid filter.' TYPE 'E'.
      CATCH /aws1/cx_cpdinternalserverex.
        MESSAGE 'Internal server error occurred.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [ListDocumentClassificationJobs](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `ListDocumentClassifiers`
<a name="comprehend_ListDocumentClassifiers_sap-abap_topic"></a>

The following code example shows how to use `ListDocumentClassifiers`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/cpd#code-examples).

```
    TRY.
        oo_result = lo_cpd->listdocumentclassifiers( ).
        MESSAGE 'Document classifiers listed.' TYPE 'I'.
      CATCH /aws1/cx_cpdinvalidrequestex.
        MESSAGE 'Invalid request.' TYPE 'E'.
      CATCH /aws1/cx_cpdtoomanyrequestsex.
        MESSAGE 'Too many requests.' TYPE 'E'.
      CATCH /aws1/cx_cpdinvalidfilterex.
        MESSAGE 'Invalid filter.' TYPE 'E'.
      CATCH /aws1/cx_cpdinternalserverex.
        MESSAGE 'Internal server error occurred.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [ListDocumentClassifiers](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `ListTopicsDetectionJobs`
<a name="comprehend_ListTopicsDetectionJobs_sap-abap_topic"></a>

The following code example shows how to use `ListTopicsDetectionJobs`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/cpd#code-examples).

```
    TRY.
        oo_result = lo_cpd->listtopicsdetectionjobs( ).
        MESSAGE 'Topics detection jobs listed.' TYPE 'I'.
      CATCH /aws1/cx_cpdinvalidrequestex.
        MESSAGE 'Invalid request.' TYPE 'E'.
      CATCH /aws1/cx_cpdtoomanyrequestsex.
        MESSAGE 'Too many requests.' TYPE 'E'.
      CATCH /aws1/cx_cpdinvalidfilterex.
        MESSAGE 'Invalid filter.' TYPE 'E'.
      CATCH /aws1/cx_cpdinternalserverex.
        MESSAGE 'Internal server error occurred.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [ListTopicsDetectionJobs](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `StartDocumentClassificationJob`
<a name="comprehend_StartDocumentClassificationJob_sap-abap_topic"></a>

The following code example shows how to use `StartDocumentClassificationJob`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/cpd#code-examples).

```
    TRY.
        oo_result = lo_cpd->startdocclassificationjob(
          iv_jobname = iv_job_name
          iv_documentclassifierarn = iv_classifier_arn
          io_inputdataconfig = NEW /aws1/cl_cpdinputdataconfig(
            iv_s3uri = iv_input_s3_uri
            iv_inputformat = iv_input_format
          )
          io_outputdataconfig = NEW /aws1/cl_cpdoutputdataconfig(
            iv_s3uri = iv_output_s3_uri
          )
          iv_dataaccessrolearn = iv_data_access_role_arn
        ).
        MESSAGE 'Document classification job started.' TYPE 'I'.
      CATCH /aws1/cx_cpdinvalidrequestex.
        MESSAGE 'Invalid request.' TYPE 'E'.
      CATCH /aws1/cx_cpdtoomanyrequestsex.
        MESSAGE 'Too many requests.' TYPE 'E'.
      CATCH /aws1/cx_cpdresourcenotfoundex.
        MESSAGE 'Resource not found.' TYPE 'E'.
      CATCH /aws1/cx_cpdresourceunavailex.
        MESSAGE 'Resource unavailable.' TYPE 'E'.
      CATCH /aws1/cx_cpdkmskeyvalidationex.
        MESSAGE 'KMS key validation error.' TYPE 'E'.
      CATCH /aws1/cx_cpdtoomanytagsex.
        MESSAGE 'Too many tags.' TYPE 'E'.
      CATCH /aws1/cx_cpdresrclimitexcdex.
        MESSAGE 'Resource limit exceeded.' TYPE 'E'.
      CATCH /aws1/cx_cpdinternalserverex.
        MESSAGE 'Internal server error occurred.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [StartDocumentClassificationJob](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `StartTopicsDetectionJob`
<a name="comprehend_StartTopicsDetectionJob_sap-abap_topic"></a>

The following code example shows how to use `StartTopicsDetectionJob`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/cpd#code-examples).

```
    TRY.
        oo_result = lo_cpd->starttopicsdetectionjob(
          iv_jobname = iv_job_name
          io_inputdataconfig = NEW /aws1/cl_cpdinputdataconfig(
            iv_s3uri = iv_input_s3_uri
            iv_inputformat = iv_input_format
          )
          io_outputdataconfig = NEW /aws1/cl_cpdoutputdataconfig(
            iv_s3uri = iv_output_s3_uri
          )
          iv_dataaccessrolearn = iv_data_access_role_arn
        ).
        MESSAGE 'Topics detection job started.' TYPE 'I'.
      CATCH /aws1/cx_cpdinvalidrequestex.
        MESSAGE 'Invalid request.' TYPE 'E'.
      CATCH /aws1/cx_cpdtoomanyrequestsex.
        MESSAGE 'Too many requests.' TYPE 'E'.
      CATCH /aws1/cx_cpdkmskeyvalidationex.
        MESSAGE 'KMS key validation error.' TYPE 'E'.
      CATCH /aws1/cx_cpdtoomanytagsex.
        MESSAGE 'Too many tags.' TYPE 'E'.
      CATCH /aws1/cx_cpdresrclimitexcdex.
        MESSAGE 'Resource limit exceeded.' TYPE 'E'.
      CATCH /aws1/cx_cpdinternalserverex.
        MESSAGE 'Internal server error occurred.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [StartTopicsDetectionJob](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for SAP ABAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-sapabap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
